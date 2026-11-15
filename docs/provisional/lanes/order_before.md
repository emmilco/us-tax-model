# The interview's asking order, measured

Written by `node engine/dist/main.js interview-order --write` (engine/src/interview-order.ts; deterministic, no model calls). Returns walked: the whole-return fixtures, the generated returns and the minimal returns, in the `full` profile. Walked with `--no-reach`: without the reach pass, a question is open only once the evaluation proper reaches it.

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
| whole-return fixtures | 11 | 79.6 | 0.0 | 8.7 | 3.5 | 8.2 | 0.5 | 1.3 |
| generated returns | 40 | 64.7 | 0.1 | 4.8 | 2.2 | 4.7 | 0.3 | 0.7 |
| minimal returns | 13 | 84.2 | 0.0 | 7.2 | 4.2 | 8.5 | 0.2 | 0.5 |

The counts are means per walk.

## What the late questions waited on

Every late finding, by the question that became reachable part-way and the answer it waited on, with the number of walks showing it
and what it caused (an order number re-entered, a form re-entered, a child delayed).

| question | waited on | its parent or roster? | caused | walks |
|---|---|---|---|---|
| `household.community_property` | `person.under16` | no | form | 36 |
| `$oi8z` | `s1.line8_other` | no | form | 35 |
| `person.x_other` | `s2.other` | no | form | 35 |
| `sa.gifts` | `sa.unsupported` | no | order | 34 |
| `$sales` | `sd.other_forms` | no | order | 31 |
| `person.blind` | `sa.dependent` | no | form | 31 |
| `s1a.overtime` | `$sc` | no | form, order | 28 |
| `qbi.carryforward` | `person.sav_trad` | no | order | 26 |
| `qbi.unsupported` | `person.sav_trad` | no | form, order | 26 |
| `w2.box4` | `person.rrta` | no | form, order | 23 |
| `sa.line1` | `sa.gifts` | no | order | 22 |
| `$gift` | `sa.charity_limited` | no | form, order | 12 |
| `sa.charity_limited` | `sa.gifts` | yes | order | 12 |
| `w2.box1` | `$w2` | yes | order | 12 |
| `s3.mcc` | `sa.line8a` | no | form | 11 |
| `sa.line11` | `sa.charity_limited` | no | child | 11 |
| `div.box10` | `div.box13` | no | child | 8 |
| `div.box3` | `div.box13` | no | child | 8 |
| `div.box9` | `div.box13` | no | child | 8 |
| `f1040.line3a` | `sb.ordinary_dividends` | no | form | 8 |
| `gift.special` | `$gift` | yes | order | 7 |
| `dependent.gross_income` | `dependent.qr_all_year` | no | order | 6 |
| `div.box13` | `div.box2c` | no | child | 6 |
| `div.box2c` | `sd.distributions` | no | form | 6 |
| `qbi.dividends` | `div.box2d` | no | form, order | 6 |
| `sales.box` | `$sales` | yes | order | 6 |
| `sales.code` | `sales.special` | no | order | 6 |
| `sales.route` | `sales.code` | no | order | 6 |
| `sales.special` | `sales.box` | no | order | 6 |
| `f1095a.void` | `f8962.premium_adjust` | no | form, order | 4 |
| `person.tin` | `sa.dependent` | no | form, order | 3 |
| `sales.correct_basis` | `sales.route` | no | order | 3 |
| `sales.proceeds` | `sales.route` | no | order | 3 |
| `div.box13` | `sd.distributions` | no | child, form | 2 |
| `eic.us_home` | `person.born_before_2001` | no | form | 2 |
| `f8962.fpl_table` | `f1095a.void` | no | form, order | 2 |
| `person.born_after_1960` | `eic.died_2025` | no | form | 2 |
| `person.died_before_65` | `person.work_ssn` | no | order | 2 |
| `person.plan` | `$sc` | no | form | 2 |
| `person.work_ssn` | `person.age65` | no | order | 2 |
| `retirement.box1` | `retirement.code_screen` | no | order | 2 |
| `s8812.combat_pay` | `eic.qc_of_another` | no | order | 2 |
| `dependent.absence_no_return` | `household.home_cost` | no | form | 1 |
| `dependent.kidnapped` | `f1040.tax_exempt_interest` | no | form, order | 1 |
| `dependent.months` | `household.home_cost` | no | form | 1 |
| `dependent.parent_home_paid` | `household.unmarried` | no | form | 1 |
| `dependent.ptc_files` | `sa.dependent` | no | form, order | 1 |
| `dependent.us_half` | `dependent.kidnapped` | no | order | 1 |
| `dependent.work_ssn` | `sa.dependent` | no | form, order | 1 |
| `div.box12` | `f1095a.void` | no | child | 1 |
| `div.box12` | `ssb.benefits` | no | child | 1 |
| `f1040.tax_exempt_interest` | `person.eic_ssn` | no | form | 1 |
| `f1040.tax_exempt_interest` | `f1095a.void` | no | form | 1 |
| `f1040.tax_exempt_interest` | `ssb.benefits` | no | form | 1 |
| `f1095a.b_counted` | `f8962.estimate_100` | no | form, order | 1 |
| `f1095a.uniform` | `f8962.alien_below` | no | form, order | 1 |
| `f1095a.uniform` | `f1040.tax_exempt_interest` | no | form, order | 1 |
| `f8889.last_month` | `household.married` | no | form, order | 1 |
| `f8962.alien_below` | `f1040.tax_exempt_interest` | no | form, order | 1 |
| `f8962.estimate_100` | `f1095a.in_c_sep` | no | order | 1 |
| `f8962.fpl_table` | `sa.dependent` | no | form | 1 |
| `f8962.same_state_counted` | `f8962.alien_below` | no | order | 1 |
| `ftc.carryover` | `s3.foreign_any` | yes | form | 1 |
| `ftc.carryover` | `s3.prior_other_forms` | yes | form | 1 |
| `household.credit_disallowed` | `person.sav_trad` | no | child, form, order | 1 |
| `household.credit_disallowed` | `f1040.tax_exempt_interest` | no | child, form, order | 1 |
| `household.home_cost` | `dependent.parent_home_paid` | no | form | 1 |
| `household.married` | `f8889.dec_coverage` | no | form, order | 1 |
| `household.married` | `dependent.absence_no_return` | no | form, order | 1 |
| `household.married` | `dependent.placed` | no | form, order | 1 |
| `person.eic_ssn` | `dependent.eic_ssn` | no | form | 1 |
| `person.itin_applied` | `person.tin` | no | order | 1 |
| `person.sav_born` | `f1095a.in_a_sep` | no | form | 1 |
| `person.sav_voluntary` | `w2.box12_any` | no | form | 1 |
| `person.work_ssn` | `person.died_before_65` | no | order | 1 |
| `qbi.carryforward` | `person.sav_claimed` | no | order | 1 |
| `qbi.carryforward` | `f1040.tax_exempt_interest` | no | order | 1 |
| `qbi.dividends` | `div.box9` | no | order | 1 |
| `qbi.unsupported` | `person.sav_claimed` | no | form, order | 1 |
| `qbi.unsupported` | `f1040.tax_exempt_interest` | no | form, order | 1 |
| `retirement.annuity` | `retirement.code_screen` | no | order | 1 |
| `s3.section965` | `s3.section960c` | no | child | 1 |
| `s3.virgin_islands` | `s3.section965` | no | child | 1 |
| `s8812.combat_pay` | `person.eic_ssn` | no | form, order | 1 |
| `sb.foreign_any` | `sd.distributions` | no | form | 1 |
| `sb.unsupported` | `sd.distributions` | no | form | 1 |
| `w2.box12_any` | `person.sav_student` | no | form | 1 |
| `w2.box3` | `w2.box4` | no | order | 1 |
| `w2.box5` | `person.rrta` | no | order | 1 |

## Delayed children for the sorting cause

By child and parent, with the number of walks.

| child | place | parent | place | walks |
|---|---|---|---|---|
| `sb.ordinary_dividends` | order 10 | `div.any` | order 10 | 11 |
| `sd.distributions` | order 10 | `div.any` | order 10 | 10 |
| `s3.section960c` | order 10 | `s3.foreign_any` | order 10 | 1 |

## What the bank states

Read from the built question bank alone. A question that states no `seq` is asked after those of its order number that do, by id.

| order | questions | state a seq | forms |
|---|---|---|---|
| 0 | 5 | 0 | f1040, person, scope |
| 1 | 6 | 0 | carloan, f1095a, otjob, retirement, sales, tipjob |
| 2 | 113 | 0 | carloan, dependent, f1095a, household, otjob, person, retirement, s3, sales, tipjob |
| 3 | 15 | 0 | dependent, person, retirement, sales, w2 |
| 4 | 6 | 0 | retirement, sales, w2 |
| 5 | 4 | 0 | gift, sa, sales, w2 |
| 8 | 1 | 0 | interest |
| 9 | 32 | 32 | f8889, person |
| 10 | 147 | 0 | clcw, div, f1040, f4952, f8863, f8959, f8960, f8962, ftc, gift, interest, oi8z, person, qbi, refund, s1, s1a, s2, s3, sa, sales, sb, sd, sli, ssb |
| 11 | 8 | 0 | asset, f8960, f8962, s1, sa, sc, scveh |
| 12 | 102 | 0 | asset, carloan, ltc, person, qbi, s179, sc, scveh |
| 15 | 12 | 0 | clcw26, div, s179 |
| 20 | 7 | 0 | f1040, f2441, household, s8812 |
| 21 | 35 | 0 | dependent, f2441, person, w2 |
| 22 | 8 | 0 | f2441, person |
| 23 | 9 | 0 | dcprov, ira, person |
| 24 | 2 | 0 | f5695 |
| 25 | 37 | 0 | f5695, person, retirement, w2 |
| 26 | 17 | 0 | f5695, person |
| 27 | 29 | 0 | f5695, person |
| 28 | 1 | 0 | ira |
| 30 | 13 | 0 | dependent, div, eic, f1040, person, ssb |
| 31 | 10 | 0 | dependent, f8863, person |

Gated questions the bank does not place directly after their parent: 20.

| child | parent | why |
|---|---|---|
| `s3.adoption` | `s3.adoption_any` | the child comes before the parent |
| `f4952.carryover` | `f4952.has_interest` | the child comes before the parent |
| `ftc.carryover` | `s3.prior_other_forms` | the child comes before the parent |
| `s3.prior_amt` | `s3.prior_other_forms` | the child comes before the parent |
| `s3.prior_forms` | `s3.prior_other_forms` | the child comes before the parent |
| `s3.section960c` | `s3.foreign_any` | 8 questions that the parent does not open stand between them (the first: `s3.kerosene`) |
| `s3.section965` | `s3.foreign_any` | 8 questions that the parent does not open stand between them (the first: `s3.kerosene`) |
| `s3.virgin_islands` | `s3.foreign_any` | 8 questions that the parent does not open stand between them (the first: `s3.kerosene`) |
| `sa.charity_limited` | `sa.gifts` | the parent is in order 5 and the child in order 10 |
| `sa.line11` | `sa.gifts` | the parent is in order 5 and the child in order 10 |
| `sb.fbar_required` | `sb.foreign_any` | the child comes before the parent |
| `sb.line8` | `sb.foreign_any` | 1 question that the parent does not open stand between them (the first: `sb.line7a`) |
| `sb.ordinary_dividends` | `div.any` | 129 questions that the parent does not open stand between them (the first: `f1040.line25b`) |
| `sd.distributions` | `div.any` | 131 questions that the parent does not open stand between them (the first: `f1040.line25b`) |
| `div.box10` | `div.any` | the parent is in order 10 and the child in order 15 |
| `div.box13` | `div.any` | the parent is in order 10 and the child in order 15 |
| `div.box3` | `div.any` | the parent is in order 10 and the child in order 15 |
| `div.box9` | `div.any` | the parent is in order 10 and the child in order 15 |
| `household.credit_disallowed` | `eic.us_home` | the parent is in order 30 and the child in order 20 |
| `div.box12` | `div.any` | the parent is in order 10 and the child in order 30 |

## Each walk

A walk's line of runs reads `order:form×questions`. For a minimal return with one gate opened, only the findings the
every-gate-closed return does not also have are listed.

### whole-return fixtures

**stage5.return.owed**: 107 questions, complete; order re-entries 10, form re-entries 5 sorting and 12 late, delayed children 2 sorting and 4 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 2:dependent×1 · 2:household×2 · 2:person×1 · 2:household×1 · 2:s3×1 · 5:w2×1 · 3:w2×4 · 8:interest×1 · 9:f8889×1 · 10:div×1 · 10:f1040×3 · 10:f4952×2 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:interest×2 · 10:person×3 · 3:w2×2 · 4:w2×8 · 10:refund×1 · 10:s1×2 · 10:oi8z×1 · 10:s1×8 · 10:s1a×1 · 10:s2×2 · 10:person×1 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×4 · 5:sa×1 · 10:sa×4 · 10:sb×1 · 10:f1040×1 · 10:sb×2 · 10:sd×3 · 1:sales×1 · 10:sli×1 · 10:ssb×1 · 11:sc×1 · 10:s1a×2 · 12:s179×1 · 15:div×5 · 10:qbi×1 · 20:f2441×2 · 22:person×1 · 10:qbi×1 · 12:qbi×1 · 24:f5695×2

- order 3 re-entered at step 35 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 18, 16 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 34), which its gate does not read.
- order 10 re-entered at step 45 by `refund.received` (order 10), left after step 34, 10 between. Late: left for `person[taxpayer].w2[emp_a].box4` (order 3), which sorts earlier and was reachable only after the answer to `person[taxpayer].rrta` (step 34), which its gate does not read.
- order 5 re-entered at step 76 by `sa.gifts` (order 5), left after step 14, 61 between. Late: reachable only after the answer to `sa.unsupported` (step 75), which its gate does not read.
- order 10 re-entered at step 77 by `sa.line1` (order 10), left after step 75, 1 between. Late: reachable only after the answer to `sa.gifts` (step 76), which its gate does not read.
- order 1 re-entered at step 88 by `$sales` (order 1), left after step 7, 80 between. Late: reachable only after the answer to `sd.other_forms` (step 87), which its gate does not read.
- order 10 re-entered at step 89 by `sli.interest` (order 10), left after step 87, 1 between. Late: left for `$sales` (order 1), which sorts earlier and was reachable only after the answer to `sd.other_forms` (step 87), which its gate does not read.
- order 10 re-entered at step 92 by `s1a.overtime` (order 10), left after step 90, 1 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 91), which its gate does not read.
- order 10 re-entered at step 100 by `qbi.dividends` (order 10), left after step 93, 6 between. Late: reachable only after the answer to `div.box9` (step 99), which its gate does not read.
- order 10 re-entered at step 104 by `qbi.unsupported` (order 10), left after step 100, 3 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 103), which its gate does not read.
- order 12 re-entered at step 105 by `qbi.carryforward` (order 12), left after step 94, 10 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 103), which its gate does not read.
- form person re-entered at step 11 by `person[taxpayer].under16` (order 2), left after step 1, 9 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 12 by `household.community_property` (order 2), left after step 10, 1 between. Late: reachable only after the answer to `person[taxpayer].under16` (step 11), which its gate does not read.
- form f1040 re-entered at step 22 by `f1040.line25b` (order 10), left after step 2, 19 between. Sorting: it was reachable (since step 1), and `scope.other_line16` was asked instead (the bank puts order 0 first).
- form interest re-entered at step 30 by `interest[bank_a].amount` (order 10), left after step 19, 10 between. Sorting: it was reachable (since step 20), and `$f8889@person[taxpayer]` was asked instead (the bank puts order 9 seq 1 first).
- form person re-entered at step 32 by `person[taxpayer].age65` (order 10), left after step 11, 20 between. Late: left for `household.community_property` (order 2), which sorts earlier and was reachable only after the answer to `person[taxpayer].under16` (step 11), which its gate does not read.
- form w2 re-entered at step 35 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 18, 16 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 34), which its gate does not read.
- form s1 re-entered at step 49 by `s1.cod_any` (order 10), left after step 47, 1 between. Late: left for `$oi8z` (order 10), which sorts earlier and was reachable only after the answer to `s1.line8_other` (step 47), which its gate does not read.
- form person re-entered at step 60 by `person[taxpayer].x_other` (order 10), left after step 34, 25 between. Late: reachable only after the answer to `s2.other` (step 59), which its gate does not read.
- form s3 re-entered at step 61 by `s3.credit_bond` (order 10), left after step 13, 47 between. Sorting: it was reachable (since step 14), and `$w2@person[taxpayer]` was asked instead (the bank puts order 5 first).
- form person re-entered at step 71 by `person[taxpayer].blind` (order 10), left after step 60, 10 between. Late: reachable only after the answer to `sa.dependent` (step 70), which its gate does not read.
- form sa re-entered at step 72 by `sa.elect_itemize` (order 10), left after step 70, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 70), which its gate does not read.
- form f1040 re-entered at step 82 by `f1040.line3a` (order 10), left after step 24, 57 between. Late: reachable only after the answer to `sb.ordinary_dividends` (step 81), which its gate does not read.
- form sb re-entered at step 83 by `sb.unsupported` (order 10), left after step 81, 1 between. Late: left for `f1040.line3a` (order 10), which sorts earlier and was reachable only after the answer to `sb.ordinary_dividends` (step 81), which its gate does not read.
- form s1a re-entered at step 92 by `s1a.overtime` (order 10), left after step 57, 34 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 91), which its gate does not read.
- form div re-entered at step 95 by `div.box13` (order 15), left after step 21, 73 between. Late: reachable only after the answer to `sd.distributions` (step 86), which its gate does not read.
- form person re-entered at step 103 by `person[taxpayer].sav_trad` (order 22), left after step 71, 31 between. Sorting: it was reachable (since step 2), and `sa.elect_itemize` was asked instead (the bank puts order 10 first).
- form qbi re-entered at step 104 by `qbi.unsupported` (order 10), left after step 100, 3 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 103), which its gate does not read.
- `sb.ordinary_dividends` (order 10), step 81: child of `div.any` (step 21), 59 other questions between. Sorting: it was reachable (since step 22), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `sd.distributions` (order 10), step 86: child of `div.any` (step 21), 63 other questions between. Sorting: it was reachable (since step 22), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `div.box13` (order 15), step 95: child of `div.any` (step 21), 71 other questions between. Late: reachable only after the answer to `sd.distributions` (step 86), which its gate does not read.
- `div.box10` (order 15), step 96: child of `div.any` (step 21), 71 other questions between. Late: reachable only after the answer to `div.box13` (step 95), which its gate does not read.
- `div.box3` (order 15), step 98: child of `div.any` (step 21), 72 other questions between. Late: reachable only after the answer to `div.box13` (step 95), which its gate does not read.
- `div.box9` (order 15), step 99: child of `div.any` (step 21), 72 other questions between. Late: reachable only after the answer to `div.box13` (step 95), which its gate does not read.

**stage5.return.refund**: 86 questions, complete; order re-entries 9, form re-entries 4 sorting and 8 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 2:dependent×1 · 2:household×2 · 2:person×1 · 2:household×1 · 2:s3×1 · 5:w2×1 · 3:w2×2 · 8:interest×1 · 9:f8889×1 · 10:div×1 · 10:f1040×3 · 10:f4952×2 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:person×3 · 3:w2×1 · 4:w2×2 · 10:refund×1 · 10:s1×2 · 10:oi8z×1 · 10:s1×8 · 10:s1a×1 · 10:s2×2 · 10:person×1 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×4 · 5:sa×1 · 10:sa×4 · 10:sb×1 · 10:sd×2 · 1:sales×1 · 10:sli×1 · 10:ssb×1 · 11:sc×1 · 10:s1a×2 · 12:s179×1 · 20:f2441×2 · 22:person×1 · 10:qbi×1 · 12:qbi×1 · 24:f5695×2

- order 3 re-entered at step 31 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 16, 14 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 30), which its gate does not read.
- order 10 re-entered at step 34 by `refund.received` (order 10), left after step 30, 3 between. Late: left for `person[taxpayer].w2[emp_a].box4` (order 3), which sorts earlier and was reachable only after the answer to `person[taxpayer].rrta` (step 30), which its gate does not read.
- order 5 re-entered at step 65 by `sa.gifts` (order 5), left after step 14, 50 between. Late: reachable only after the answer to `sa.unsupported` (step 64), which its gate does not read.
- order 10 re-entered at step 66 by `sa.line1` (order 10), left after step 64, 1 between. Late: reachable only after the answer to `sa.gifts` (step 65), which its gate does not read.
- order 1 re-entered at step 73 by `$sales` (order 1), left after step 7, 65 between. Late: reachable only after the answer to `sd.other_forms` (step 72), which its gate does not read.
- order 10 re-entered at step 74 by `sli.interest` (order 10), left after step 72, 1 between. Late: left for `$sales` (order 1), which sorts earlier and was reachable only after the answer to `sd.other_forms` (step 72), which its gate does not read.
- order 10 re-entered at step 77 by `s1a.overtime` (order 10), left after step 75, 1 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 76), which its gate does not read.
- order 10 re-entered at step 83 by `qbi.unsupported` (order 10), left after step 78, 4 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 82), which its gate does not read.
- order 12 re-entered at step 84 by `qbi.carryforward` (order 12), left after step 79, 4 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 82), which its gate does not read.
- form person re-entered at step 11 by `person[taxpayer].under16` (order 2), left after step 1, 9 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 12 by `household.community_property` (order 2), left after step 10, 1 between. Late: reachable only after the answer to `person[taxpayer].under16` (step 11), which its gate does not read.
- form f1040 re-entered at step 20 by `f1040.line25b` (order 10), left after step 2, 17 between. Sorting: it was reachable (since step 1), and `scope.other_line16` was asked instead (the bank puts order 0 first).
- form person re-entered at step 28 by `person[taxpayer].age65` (order 10), left after step 11, 16 between. Late: left for `household.community_property` (order 2), which sorts earlier and was reachable only after the answer to `person[taxpayer].under16` (step 11), which its gate does not read.
- form w2 re-entered at step 31 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 16, 14 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 30), which its gate does not read.
- form s1 re-entered at step 38 by `s1.cod_any` (order 10), left after step 36, 1 between. Late: left for `$oi8z` (order 10), which sorts earlier and was reachable only after the answer to `s1.line8_other` (step 36), which its gate does not read.
- form person re-entered at step 49 by `person[taxpayer].x_other` (order 10), left after step 30, 18 between. Late: reachable only after the answer to `s2.other` (step 48), which its gate does not read.
- form s3 re-entered at step 50 by `s3.credit_bond` (order 10), left after step 13, 36 between. Sorting: it was reachable (since step 14), and `$w2@person[taxpayer]` was asked instead (the bank puts order 5 first).
- form person re-entered at step 60 by `person[taxpayer].blind` (order 10), left after step 49, 10 between. Late: reachable only after the answer to `sa.dependent` (step 59), which its gate does not read.
- form sa re-entered at step 61 by `sa.elect_itemize` (order 10), left after step 59, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 59), which its gate does not read.
- form s1a re-entered at step 77 by `s1a.overtime` (order 10), left after step 46, 30 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 76), which its gate does not read.
- form person re-entered at step 82 by `person[taxpayer].sav_trad` (order 22), left after step 60, 21 between. Sorting: it was reachable (since step 2), and `sa.elect_itemize` was asked instead (the bank puts order 10 first).

**stage5.return.itemized**: 122 questions, complete; order re-entries 16, form re-entries 5 sorting and 15 late, delayed children 2 sorting and 5 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 2:dependent×1 · 2:household×2 · 2:person×1 · 2:household×1 · 2:s3×1 · 5:w2×1 · 3:w2×2 · 8:interest×1 · 9:f8889×1 · 10:div×1 · 10:f1040×3 · 10:f4952×6 · 10:f8863×1 · 10:f8959×1 · 10:ftc×5 · 10:interest×2 · 10:person×3 · 3:w2×1 · 4:w2×2 · 10:refund×1 · 10:s1×2 · 10:oi8z×1 · 10:s1×8 · 10:s1a×1 · 10:s2×2 · 10:person×1 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×3 · 10:s3×1 · 10:sa×1 · 5:sa×1 · 10:sa×1 · 5:gift×1 · 10:gift×2 · 10:sa×5 · 10:sb×1 · 10:f1040×1 · 10:sb×2 · 10:sd×3 · 1:sales×1 · 2:sales×1 · 3:sales×1 · 4:sales×1 · 5:sales×1 · 10:sales×2 · 10:sli×1 · 10:ssb×1 · 11:sc×1 · 10:s1a×2 · 12:s179×1 · 15:div×9 · 10:qbi×1 · 20:f2441×2 · 22:person×1 · 10:qbi×1 · 12:qbi×1 · 24:f5695×2

- order 3 re-entered at step 41 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 16, 24 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 40), which its gate does not read.
- order 10 re-entered at step 44 by `refund.received` (order 10), left after step 40, 3 between. Late: left for `person[taxpayer].w2[emp_a].box4` (order 3), which sorts earlier and was reachable only after the answer to `person[taxpayer].rrta` (step 40), which its gate does not read.
- order 5 re-entered at step 76 by `sa.gifts` (order 5), left after step 14, 61 between. Late: reachable only after the answer to `sa.unsupported` (step 75), which its gate does not read.
- order 10 re-entered at step 77 by `sa.charity_limited` (order 10), left after step 75, 1 between. Late: reachable only after the answer to `sa.gifts` (step 76), its parent or roster.
- order 5 re-entered at step 78 by `$gift` (order 5), left after step 76, 1 between. Late: reachable only after the answer to `sa.charity_limited` (step 77), which its gate does not read.
- order 10 re-entered at step 79 by `gift[books].special` (order 10), left after step 77, 1 between. Late: reachable only after the answer to `$gift` (step 78), its parent or roster.
- order 1 re-entered at step 93 by `$sales` (order 1), left after step 7, 85 between. Late: reachable only after the answer to `sd.other_forms` (step 92), which its gate does not read.
- order 2 re-entered at step 94 by `sales[s1].box` (order 2), left after step 13, 80 between. Late: reachable only after the answer to `$sales` (step 93), its parent or roster.
- order 3 re-entered at step 95 by `sales[s1].special` (order 3), left after step 41, 53 between. Late: reachable only after the answer to `sales[s1].box` (step 94), which its gate does not read.
- order 4 re-entered at step 96 by `sales[s1].code` (order 4), left after step 43, 52 between. Late: reachable only after the answer to `sales[s1].special` (step 95), which its gate does not read.
- order 5 re-entered at step 97 by `sales[s1].route` (order 5), left after step 78, 18 between. Late: reachable only after the answer to `sales[s1].code` (step 96), which its gate does not read.
- order 10 re-entered at step 98 by `sales[s1].proceeds` (order 10), left after step 92, 5 between. Late: reachable only after the answer to `sales[s1].route` (step 97), which its gate does not read.
- order 10 re-entered at step 103 by `s1a.overtime` (order 10), left after step 101, 1 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 102), which its gate does not read.
- order 10 re-entered at step 115 by `qbi.dividends` (order 10), left after step 104, 10 between. Late: reachable only after the answer to `div.box2d` (step 114), which its gate does not read.
- order 10 re-entered at step 119 by `qbi.unsupported` (order 10), left after step 115, 3 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 118), which its gate does not read.
- order 12 re-entered at step 120 by `qbi.carryforward` (order 12), left after step 105, 14 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 118), which its gate does not read.
- form person re-entered at step 11 by `person[taxpayer].under16` (order 2), left after step 1, 9 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 12 by `household.community_property` (order 2), left after step 10, 1 between. Late: reachable only after the answer to `person[taxpayer].under16` (step 11), which its gate does not read.
- form f1040 re-entered at step 20 by `f1040.line25b` (order 10), left after step 2, 17 between. Sorting: it was reachable (since step 1), and `scope.other_line16` was asked instead (the bank puts order 0 first).
- form interest re-entered at step 36 by `interest[bank_a].amount` (order 10), left after step 17, 18 between. Sorting: it was reachable (since step 18), and `$f8889@person[taxpayer]` was asked instead (the bank puts order 9 seq 1 first).
- form person re-entered at step 38 by `person[taxpayer].age65` (order 10), left after step 11, 26 between. Late: left for `household.community_property` (order 2), which sorts earlier and was reachable only after the answer to `person[taxpayer].under16` (step 11), which its gate does not read.
- form w2 re-entered at step 41 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 16, 24 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 40), which its gate does not read.
- form s1 re-entered at step 48 by `s1.cod_any` (order 10), left after step 46, 1 between. Late: left for `$oi8z` (order 10), which sorts earlier and was reachable only after the answer to `s1.line8_other` (step 46), which its gate does not read.
- form person re-entered at step 59 by `person[taxpayer].x_other` (order 10), left after step 40, 18 between. Late: reachable only after the answer to `s2.other` (step 58), which its gate does not read.
- form s3 re-entered at step 60 by `s3.credit_bond` (order 10), left after step 13, 46 between. Sorting: it was reachable (since step 14), and `$w2@person[taxpayer]` was asked instead (the bank puts order 5 first).
- form person re-entered at step 70 by `person[taxpayer].blind` (order 10), left after step 59, 10 between. Late: reachable only after the answer to `sa.dependent` (step 69), which its gate does not read.
- form sa re-entered at step 71 by `sa.elect_itemize` (order 10), left after step 69, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 69), which its gate does not read.
- form s3 re-entered at step 74 by `s3.mcc` (order 10), left after step 68, 5 between. Late: reachable only after the answer to `sa.line8a` (step 73), which its gate does not read.
- form sa re-entered at step 75 by `sa.unsupported` (order 10), left after step 73, 1 between. Late: left for `s3.mcc` (order 10), which sorts earlier and was reachable only after the answer to `sa.line8a` (step 73), which its gate does not read.
- form sa re-entered at step 81 by `sa.line1` (order 10), left after step 77, 3 between. Late: left for `$gift` (order 5), which sorts earlier and was reachable only after the answer to `sa.charity_limited` (step 77), which its gate does not read.
- form f1040 re-entered at step 87 by `f1040.line3a` (order 10), left after step 22, 64 between. Late: reachable only after the answer to `sb.ordinary_dividends` (step 86), which its gate does not read.
- form sb re-entered at step 88 by `sb.unsupported` (order 10), left after step 86, 1 between. Late: left for `f1040.line3a` (order 10), which sorts earlier and was reachable only after the answer to `sb.ordinary_dividends` (step 86), which its gate does not read.
- form s1a re-entered at step 103 by `s1a.overtime` (order 10), left after step 56, 46 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 102), which its gate does not read.
- form div re-entered at step 106 by `div.box2c` (order 15), left after step 19, 86 between. Late: reachable only after the answer to `sd.distributions` (step 91), which its gate does not read.
- form person re-entered at step 118 by `person[taxpayer].sav_trad` (order 22), left after step 70, 47 between. Sorting: it was reachable (since step 2), and `sa.elect_itemize` was asked instead (the bank puts order 10 first).
- form qbi re-entered at step 119 by `qbi.unsupported` (order 10), left after step 115, 3 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 118), which its gate does not read.
- `sa.line11` (order 10), step 82: child of `sa.gifts` (step 76), 4 other questions between. Late: reachable only after the answer to `sa.charity_limited` (step 77), which its gate does not read.
- `sb.ordinary_dividends` (order 10), step 86: child of `div.any` (step 19), 66 other questions between. Sorting: it was reachable (since step 20), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `sd.distributions` (order 10), step 91: child of `div.any` (step 19), 70 other questions between. Sorting: it was reachable (since step 20), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `div.box13` (order 15), step 107: child of `div.any` (step 19), 85 other questions between. Late: reachable only after the answer to `div.box2c` (step 106), which its gate does not read.
- `div.box10` (order 15), step 108: child of `div.any` (step 19), 85 other questions between. Late: reachable only after the answer to `div.box13` (step 107), which its gate does not read.
- `div.box3` (order 15), step 111: child of `div.any` (step 19), 87 other questions between. Late: reachable only after the answer to `div.box13` (step 107), which its gate does not read.
- `div.box9` (order 15), step 112: child of `div.any` (step 19), 87 other questions between. Late: reachable only after the answer to `div.box13` (step 107), which its gate does not read.

**stage5.refuse.screens**: 4 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×2

**stage5.refuse.other_income**: 5 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3

**stage5.return.refund_f4952_screens_unused**: 86 questions, complete; order re-entries 9, form re-entries 4 sorting and 8 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 2:dependent×1 · 2:household×2 · 2:person×1 · 2:household×1 · 2:s3×1 · 5:w2×1 · 3:w2×2 · 8:interest×1 · 9:f8889×1 · 10:div×1 · 10:f1040×3 · 10:f4952×2 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:person×3 · 3:w2×1 · 4:w2×2 · 10:refund×1 · 10:s1×2 · 10:oi8z×1 · 10:s1×8 · 10:s1a×1 · 10:s2×2 · 10:person×1 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×4 · 5:sa×1 · 10:sa×4 · 10:sb×1 · 10:sd×2 · 1:sales×1 · 10:sli×1 · 10:ssb×1 · 11:sc×1 · 10:s1a×2 · 12:s179×1 · 20:f2441×2 · 22:person×1 · 10:qbi×1 · 12:qbi×1 · 24:f5695×2

- order 3 re-entered at step 31 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 16, 14 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 30), which its gate does not read.
- order 10 re-entered at step 34 by `refund.received` (order 10), left after step 30, 3 between. Late: left for `person[taxpayer].w2[emp_a].box4` (order 3), which sorts earlier and was reachable only after the answer to `person[taxpayer].rrta` (step 30), which its gate does not read.
- order 5 re-entered at step 65 by `sa.gifts` (order 5), left after step 14, 50 between. Late: reachable only after the answer to `sa.unsupported` (step 64), which its gate does not read.
- order 10 re-entered at step 66 by `sa.line1` (order 10), left after step 64, 1 between. Late: reachable only after the answer to `sa.gifts` (step 65), which its gate does not read.
- order 1 re-entered at step 73 by `$sales` (order 1), left after step 7, 65 between. Late: reachable only after the answer to `sd.other_forms` (step 72), which its gate does not read.
- order 10 re-entered at step 74 by `sli.interest` (order 10), left after step 72, 1 between. Late: left for `$sales` (order 1), which sorts earlier and was reachable only after the answer to `sd.other_forms` (step 72), which its gate does not read.
- order 10 re-entered at step 77 by `s1a.overtime` (order 10), left after step 75, 1 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 76), which its gate does not read.
- order 10 re-entered at step 83 by `qbi.unsupported` (order 10), left after step 78, 4 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 82), which its gate does not read.
- order 12 re-entered at step 84 by `qbi.carryforward` (order 12), left after step 79, 4 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 82), which its gate does not read.
- form person re-entered at step 11 by `person[taxpayer].under16` (order 2), left after step 1, 9 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 12 by `household.community_property` (order 2), left after step 10, 1 between. Late: reachable only after the answer to `person[taxpayer].under16` (step 11), which its gate does not read.
- form f1040 re-entered at step 20 by `f1040.line25b` (order 10), left after step 2, 17 between. Sorting: it was reachable (since step 1), and `scope.other_line16` was asked instead (the bank puts order 0 first).
- form person re-entered at step 28 by `person[taxpayer].age65` (order 10), left after step 11, 16 between. Late: left for `household.community_property` (order 2), which sorts earlier and was reachable only after the answer to `person[taxpayer].under16` (step 11), which its gate does not read.
- form w2 re-entered at step 31 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 16, 14 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 30), which its gate does not read.
- form s1 re-entered at step 38 by `s1.cod_any` (order 10), left after step 36, 1 between. Late: left for `$oi8z` (order 10), which sorts earlier and was reachable only after the answer to `s1.line8_other` (step 36), which its gate does not read.
- form person re-entered at step 49 by `person[taxpayer].x_other` (order 10), left after step 30, 18 between. Late: reachable only after the answer to `s2.other` (step 48), which its gate does not read.
- form s3 re-entered at step 50 by `s3.credit_bond` (order 10), left after step 13, 36 between. Sorting: it was reachable (since step 14), and `$w2@person[taxpayer]` was asked instead (the bank puts order 5 first).
- form person re-entered at step 60 by `person[taxpayer].blind` (order 10), left after step 49, 10 between. Late: reachable only after the answer to `sa.dependent` (step 59), which its gate does not read.
- form sa re-entered at step 61 by `sa.elect_itemize` (order 10), left after step 59, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 59), which its gate does not read.
- form s1a re-entered at step 77 by `s1a.overtime` (order 10), left after step 46, 30 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 76), which its gate does not read.
- form person re-entered at step 82 by `person[taxpayer].sav_trad` (order 22), left after step 60, 21 between. Sorting: it was reachable (since step 2), and `sa.elect_itemize` was asked instead (the bank puts order 10 first).

**stage5.return.refund_f8960_unsupported_unused**: 86 questions, complete; order re-entries 9, form re-entries 4 sorting and 8 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 2:dependent×1 · 2:household×2 · 2:person×1 · 2:household×1 · 2:s3×1 · 5:w2×1 · 3:w2×2 · 8:interest×1 · 9:f8889×1 · 10:div×1 · 10:f1040×3 · 10:f4952×2 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:person×3 · 3:w2×1 · 4:w2×2 · 10:refund×1 · 10:s1×2 · 10:oi8z×1 · 10:s1×8 · 10:s1a×1 · 10:s2×2 · 10:person×1 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×4 · 5:sa×1 · 10:sa×4 · 10:sb×1 · 10:sd×2 · 1:sales×1 · 10:sli×1 · 10:ssb×1 · 11:sc×1 · 10:s1a×2 · 12:s179×1 · 20:f2441×2 · 22:person×1 · 10:qbi×1 · 12:qbi×1 · 24:f5695×2

- order 3 re-entered at step 31 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 16, 14 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 30), which its gate does not read.
- order 10 re-entered at step 34 by `refund.received` (order 10), left after step 30, 3 between. Late: left for `person[taxpayer].w2[emp_a].box4` (order 3), which sorts earlier and was reachable only after the answer to `person[taxpayer].rrta` (step 30), which its gate does not read.
- order 5 re-entered at step 65 by `sa.gifts` (order 5), left after step 14, 50 between. Late: reachable only after the answer to `sa.unsupported` (step 64), which its gate does not read.
- order 10 re-entered at step 66 by `sa.line1` (order 10), left after step 64, 1 between. Late: reachable only after the answer to `sa.gifts` (step 65), which its gate does not read.
- order 1 re-entered at step 73 by `$sales` (order 1), left after step 7, 65 between. Late: reachable only after the answer to `sd.other_forms` (step 72), which its gate does not read.
- order 10 re-entered at step 74 by `sli.interest` (order 10), left after step 72, 1 between. Late: left for `$sales` (order 1), which sorts earlier and was reachable only after the answer to `sd.other_forms` (step 72), which its gate does not read.
- order 10 re-entered at step 77 by `s1a.overtime` (order 10), left after step 75, 1 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 76), which its gate does not read.
- order 10 re-entered at step 83 by `qbi.unsupported` (order 10), left after step 78, 4 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 82), which its gate does not read.
- order 12 re-entered at step 84 by `qbi.carryforward` (order 12), left after step 79, 4 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 82), which its gate does not read.
- form person re-entered at step 11 by `person[taxpayer].under16` (order 2), left after step 1, 9 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 12 by `household.community_property` (order 2), left after step 10, 1 between. Late: reachable only after the answer to `person[taxpayer].under16` (step 11), which its gate does not read.
- form f1040 re-entered at step 20 by `f1040.line25b` (order 10), left after step 2, 17 between. Sorting: it was reachable (since step 1), and `scope.other_line16` was asked instead (the bank puts order 0 first).
- form person re-entered at step 28 by `person[taxpayer].age65` (order 10), left after step 11, 16 between. Late: left for `household.community_property` (order 2), which sorts earlier and was reachable only after the answer to `person[taxpayer].under16` (step 11), which its gate does not read.
- form w2 re-entered at step 31 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 16, 14 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 30), which its gate does not read.
- form s1 re-entered at step 38 by `s1.cod_any` (order 10), left after step 36, 1 between. Late: left for `$oi8z` (order 10), which sorts earlier and was reachable only after the answer to `s1.line8_other` (step 36), which its gate does not read.
- form person re-entered at step 49 by `person[taxpayer].x_other` (order 10), left after step 30, 18 between. Late: reachable only after the answer to `s2.other` (step 48), which its gate does not read.
- form s3 re-entered at step 50 by `s3.credit_bond` (order 10), left after step 13, 36 between. Sorting: it was reachable (since step 14), and `$w2@person[taxpayer]` was asked instead (the bank puts order 5 first).
- form person re-entered at step 60 by `person[taxpayer].blind` (order 10), left after step 49, 10 between. Late: reachable only after the answer to `sa.dependent` (step 59), which its gate does not read.
- form sa re-entered at step 61 by `sa.elect_itemize` (order 10), left after step 59, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 59), which its gate does not read.
- form s1a re-entered at step 77 by `s1a.overtime` (order 10), left after step 46, 30 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 76), which its gate does not read.
- form person re-entered at step 82 by `person[taxpayer].sav_trad` (order 22), left after step 60, 21 between. Sorting: it was reachable (since step 2), and `sa.elect_itemize` was asked instead (the bank puts order 10 first).

**stage5.return.f8960_unsupported_agi_at_threshold**: 86 questions, complete; order re-entries 9, form re-entries 4 sorting and 8 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 2:dependent×1 · 2:household×2 · 2:person×1 · 2:household×1 · 2:s3×1 · 5:w2×1 · 3:w2×2 · 8:interest×1 · 9:f8889×1 · 10:div×1 · 10:f1040×3 · 10:f4952×2 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:person×3 · 3:w2×1 · 4:w2×2 · 10:refund×1 · 10:s1×2 · 10:oi8z×1 · 10:s1×8 · 10:s1a×1 · 10:s2×2 · 10:person×1 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×4 · 5:sa×1 · 10:sa×4 · 10:sb×1 · 10:sd×2 · 1:sales×1 · 10:sli×1 · 10:ssb×1 · 11:sc×1 · 10:s1a×2 · 12:s179×1 · 20:f2441×2 · 22:person×1 · 10:qbi×1 · 12:qbi×1 · 24:f5695×2

- order 3 re-entered at step 31 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 16, 14 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 30), which its gate does not read.
- order 10 re-entered at step 34 by `refund.received` (order 10), left after step 30, 3 between. Late: left for `person[taxpayer].w2[emp_a].box4` (order 3), which sorts earlier and was reachable only after the answer to `person[taxpayer].rrta` (step 30), which its gate does not read.
- order 5 re-entered at step 65 by `sa.gifts` (order 5), left after step 14, 50 between. Late: reachable only after the answer to `sa.unsupported` (step 64), which its gate does not read.
- order 10 re-entered at step 66 by `sa.line1` (order 10), left after step 64, 1 between. Late: reachable only after the answer to `sa.gifts` (step 65), which its gate does not read.
- order 1 re-entered at step 73 by `$sales` (order 1), left after step 7, 65 between. Late: reachable only after the answer to `sd.other_forms` (step 72), which its gate does not read.
- order 10 re-entered at step 74 by `sli.interest` (order 10), left after step 72, 1 between. Late: left for `$sales` (order 1), which sorts earlier and was reachable only after the answer to `sd.other_forms` (step 72), which its gate does not read.
- order 10 re-entered at step 77 by `s1a.overtime` (order 10), left after step 75, 1 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 76), which its gate does not read.
- order 10 re-entered at step 83 by `qbi.unsupported` (order 10), left after step 78, 4 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 82), which its gate does not read.
- order 12 re-entered at step 84 by `qbi.carryforward` (order 12), left after step 79, 4 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 82), which its gate does not read.
- form person re-entered at step 11 by `person[taxpayer].under16` (order 2), left after step 1, 9 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 12 by `household.community_property` (order 2), left after step 10, 1 between. Late: reachable only after the answer to `person[taxpayer].under16` (step 11), which its gate does not read.
- form f1040 re-entered at step 20 by `f1040.line25b` (order 10), left after step 2, 17 between. Sorting: it was reachable (since step 1), and `scope.other_line16` was asked instead (the bank puts order 0 first).
- form person re-entered at step 28 by `person[taxpayer].age65` (order 10), left after step 11, 16 between. Late: left for `household.community_property` (order 2), which sorts earlier and was reachable only after the answer to `person[taxpayer].under16` (step 11), which its gate does not read.
- form w2 re-entered at step 31 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 16, 14 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 30), which its gate does not read.
- form s1 re-entered at step 38 by `s1.cod_any` (order 10), left after step 36, 1 between. Late: left for `$oi8z` (order 10), which sorts earlier and was reachable only after the answer to `s1.line8_other` (step 36), which its gate does not read.
- form person re-entered at step 49 by `person[taxpayer].x_other` (order 10), left after step 30, 18 between. Late: reachable only after the answer to `s2.other` (step 48), which its gate does not read.
- form s3 re-entered at step 50 by `s3.credit_bond` (order 10), left after step 13, 36 between. Sorting: it was reachable (since step 14), and `$w2@person[taxpayer]` was asked instead (the bank puts order 5 first).
- form person re-entered at step 60 by `person[taxpayer].blind` (order 10), left after step 49, 10 between. Late: reachable only after the answer to `sa.dependent` (step 59), which its gate does not read.
- form sa re-entered at step 61 by `sa.elect_itemize` (order 10), left after step 59, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 59), which its gate does not read.
- form s1a re-entered at step 77 by `s1a.overtime` (order 10), left after step 46, 30 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 76), which its gate does not read.
- form person re-entered at step 82 by `person[taxpayer].sav_trad` (order 22), left after step 60, 21 between. Sorting: it was reachable (since step 2), and `sa.elect_itemize` was asked instead (the bank puts order 10 first).

**stage5.return.refund_f8960_refund_unused**: 86 questions, complete; order re-entries 9, form re-entries 4 sorting and 8 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 2:dependent×1 · 2:household×2 · 2:person×1 · 2:household×1 · 2:s3×1 · 5:w2×1 · 3:w2×2 · 8:interest×1 · 9:f8889×1 · 10:div×1 · 10:f1040×3 · 10:f4952×2 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:person×3 · 3:w2×1 · 4:w2×2 · 10:refund×1 · 10:s1×2 · 10:oi8z×1 · 10:s1×8 · 10:s1a×1 · 10:s2×2 · 10:person×1 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×4 · 5:sa×1 · 10:sa×4 · 10:sb×1 · 10:sd×2 · 1:sales×1 · 10:sli×1 · 10:ssb×1 · 11:sc×1 · 10:s1a×2 · 12:s179×1 · 20:f2441×2 · 22:person×1 · 10:qbi×1 · 12:qbi×1 · 24:f5695×2

- order 3 re-entered at step 31 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 16, 14 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 30), which its gate does not read.
- order 10 re-entered at step 34 by `refund.received` (order 10), left after step 30, 3 between. Late: left for `person[taxpayer].w2[emp_a].box4` (order 3), which sorts earlier and was reachable only after the answer to `person[taxpayer].rrta` (step 30), which its gate does not read.
- order 5 re-entered at step 65 by `sa.gifts` (order 5), left after step 14, 50 between. Late: reachable only after the answer to `sa.unsupported` (step 64), which its gate does not read.
- order 10 re-entered at step 66 by `sa.line1` (order 10), left after step 64, 1 between. Late: reachable only after the answer to `sa.gifts` (step 65), which its gate does not read.
- order 1 re-entered at step 73 by `$sales` (order 1), left after step 7, 65 between. Late: reachable only after the answer to `sd.other_forms` (step 72), which its gate does not read.
- order 10 re-entered at step 74 by `sli.interest` (order 10), left after step 72, 1 between. Late: left for `$sales` (order 1), which sorts earlier and was reachable only after the answer to `sd.other_forms` (step 72), which its gate does not read.
- order 10 re-entered at step 77 by `s1a.overtime` (order 10), left after step 75, 1 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 76), which its gate does not read.
- order 10 re-entered at step 83 by `qbi.unsupported` (order 10), left after step 78, 4 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 82), which its gate does not read.
- order 12 re-entered at step 84 by `qbi.carryforward` (order 12), left after step 79, 4 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 82), which its gate does not read.
- form person re-entered at step 11 by `person[taxpayer].under16` (order 2), left after step 1, 9 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 12 by `household.community_property` (order 2), left after step 10, 1 between. Late: reachable only after the answer to `person[taxpayer].under16` (step 11), which its gate does not read.
- form f1040 re-entered at step 20 by `f1040.line25b` (order 10), left after step 2, 17 between. Sorting: it was reachable (since step 1), and `scope.other_line16` was asked instead (the bank puts order 0 first).
- form person re-entered at step 28 by `person[taxpayer].age65` (order 10), left after step 11, 16 between. Late: left for `household.community_property` (order 2), which sorts earlier and was reachable only after the answer to `person[taxpayer].under16` (step 11), which its gate does not read.
- form w2 re-entered at step 31 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 16, 14 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 30), which its gate does not read.
- form s1 re-entered at step 38 by `s1.cod_any` (order 10), left after step 36, 1 between. Late: left for `$oi8z` (order 10), which sorts earlier and was reachable only after the answer to `s1.line8_other` (step 36), which its gate does not read.
- form person re-entered at step 49 by `person[taxpayer].x_other` (order 10), left after step 30, 18 between. Late: reachable only after the answer to `s2.other` (step 48), which its gate does not read.
- form s3 re-entered at step 50 by `s3.credit_bond` (order 10), left after step 13, 36 between. Sorting: it was reachable (since step 14), and `$w2@person[taxpayer]` was asked instead (the bank puts order 5 first).
- form person re-entered at step 60 by `person[taxpayer].blind` (order 10), left after step 49, 10 between. Late: reachable only after the answer to `sa.dependent` (step 59), which its gate does not read.
- form sa re-entered at step 61 by `sa.elect_itemize` (order 10), left after step 59, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 59), which its gate does not read.
- form s1a re-entered at step 77 by `s1a.overtime` (order 10), left after step 46, 30 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 76), which its gate does not read.
- form person re-entered at step 82 by `person[taxpayer].sav_trad` (order 22), left after step 60, 21 between. Sorting: it was reachable (since step 2), and `sa.elect_itemize` was asked instead (the bank puts order 10 first).

**stage5.return.refund_combat_pay_no_children**: 86 questions, complete; order re-entries 9, form re-entries 4 sorting and 8 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 2:dependent×1 · 2:household×2 · 2:person×1 · 2:household×1 · 2:s3×1 · 5:w2×1 · 3:w2×2 · 8:interest×1 · 9:f8889×1 · 10:div×1 · 10:f1040×3 · 10:f4952×2 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:person×3 · 3:w2×1 · 4:w2×2 · 10:refund×1 · 10:s1×2 · 10:oi8z×1 · 10:s1×8 · 10:s1a×1 · 10:s2×2 · 10:person×1 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×4 · 5:sa×1 · 10:sa×4 · 10:sb×1 · 10:sd×2 · 1:sales×1 · 10:sli×1 · 10:ssb×1 · 11:sc×1 · 10:s1a×2 · 12:s179×1 · 20:f2441×2 · 22:person×1 · 10:qbi×1 · 12:qbi×1 · 24:f5695×2

- order 3 re-entered at step 31 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 16, 14 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 30), which its gate does not read.
- order 10 re-entered at step 34 by `refund.received` (order 10), left after step 30, 3 between. Late: left for `person[taxpayer].w2[emp_a].box4` (order 3), which sorts earlier and was reachable only after the answer to `person[taxpayer].rrta` (step 30), which its gate does not read.
- order 5 re-entered at step 65 by `sa.gifts` (order 5), left after step 14, 50 between. Late: reachable only after the answer to `sa.unsupported` (step 64), which its gate does not read.
- order 10 re-entered at step 66 by `sa.line1` (order 10), left after step 64, 1 between. Late: reachable only after the answer to `sa.gifts` (step 65), which its gate does not read.
- order 1 re-entered at step 73 by `$sales` (order 1), left after step 7, 65 between. Late: reachable only after the answer to `sd.other_forms` (step 72), which its gate does not read.
- order 10 re-entered at step 74 by `sli.interest` (order 10), left after step 72, 1 between. Late: left for `$sales` (order 1), which sorts earlier and was reachable only after the answer to `sd.other_forms` (step 72), which its gate does not read.
- order 10 re-entered at step 77 by `s1a.overtime` (order 10), left after step 75, 1 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 76), which its gate does not read.
- order 10 re-entered at step 83 by `qbi.unsupported` (order 10), left after step 78, 4 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 82), which its gate does not read.
- order 12 re-entered at step 84 by `qbi.carryforward` (order 12), left after step 79, 4 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 82), which its gate does not read.
- form person re-entered at step 11 by `person[taxpayer].under16` (order 2), left after step 1, 9 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 12 by `household.community_property` (order 2), left after step 10, 1 between. Late: reachable only after the answer to `person[taxpayer].under16` (step 11), which its gate does not read.
- form f1040 re-entered at step 20 by `f1040.line25b` (order 10), left after step 2, 17 between. Sorting: it was reachable (since step 1), and `scope.other_line16` was asked instead (the bank puts order 0 first).
- form person re-entered at step 28 by `person[taxpayer].age65` (order 10), left after step 11, 16 between. Late: left for `household.community_property` (order 2), which sorts earlier and was reachable only after the answer to `person[taxpayer].under16` (step 11), which its gate does not read.
- form w2 re-entered at step 31 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 16, 14 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 30), which its gate does not read.
- form s1 re-entered at step 38 by `s1.cod_any` (order 10), left after step 36, 1 between. Late: left for `$oi8z` (order 10), which sorts earlier and was reachable only after the answer to `s1.line8_other` (step 36), which its gate does not read.
- form person re-entered at step 49 by `person[taxpayer].x_other` (order 10), left after step 30, 18 between. Late: reachable only after the answer to `s2.other` (step 48), which its gate does not read.
- form s3 re-entered at step 50 by `s3.credit_bond` (order 10), left after step 13, 36 between. Sorting: it was reachable (since step 14), and `$w2@person[taxpayer]` was asked instead (the bank puts order 5 first).
- form person re-entered at step 60 by `person[taxpayer].blind` (order 10), left after step 49, 10 between. Late: reachable only after the answer to `sa.dependent` (step 59), which its gate does not read.
- form sa re-entered at step 61 by `sa.elect_itemize` (order 10), left after step 59, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 59), which its gate does not read.
- form s1a re-entered at step 77 by `s1a.overtime` (order 10), left after step 46, 30 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 76), which its gate does not read.
- form person re-entered at step 82 by `person[taxpayer].sav_trad` (order 22), left after step 60, 21 between. Sorting: it was reachable (since step 2), and `sa.elect_itemize` was asked instead (the bank puts order 10 first).

**stage5.return.itemized_f8960_allocation_unused**: 122 questions, complete; order re-entries 16, form re-entries 5 sorting and 15 late, delayed children 2 sorting and 5 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 2:dependent×1 · 2:household×2 · 2:person×1 · 2:household×1 · 2:s3×1 · 5:w2×1 · 3:w2×2 · 8:interest×1 · 9:f8889×1 · 10:div×1 · 10:f1040×3 · 10:f4952×6 · 10:f8863×1 · 10:f8959×1 · 10:ftc×5 · 10:interest×2 · 10:person×3 · 3:w2×1 · 4:w2×2 · 10:refund×1 · 10:s1×2 · 10:oi8z×1 · 10:s1×8 · 10:s1a×1 · 10:s2×2 · 10:person×1 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×3 · 10:s3×1 · 10:sa×1 · 5:sa×1 · 10:sa×1 · 5:gift×1 · 10:gift×2 · 10:sa×5 · 10:sb×1 · 10:f1040×1 · 10:sb×2 · 10:sd×3 · 1:sales×1 · 2:sales×1 · 3:sales×1 · 4:sales×1 · 5:sales×1 · 10:sales×2 · 10:sli×1 · 10:ssb×1 · 11:sc×1 · 10:s1a×2 · 12:s179×1 · 15:div×9 · 10:qbi×1 · 20:f2441×2 · 22:person×1 · 10:qbi×1 · 12:qbi×1 · 24:f5695×2

- order 3 re-entered at step 41 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 16, 24 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 40), which its gate does not read.
- order 10 re-entered at step 44 by `refund.received` (order 10), left after step 40, 3 between. Late: left for `person[taxpayer].w2[emp_a].box4` (order 3), which sorts earlier and was reachable only after the answer to `person[taxpayer].rrta` (step 40), which its gate does not read.
- order 5 re-entered at step 76 by `sa.gifts` (order 5), left after step 14, 61 between. Late: reachable only after the answer to `sa.unsupported` (step 75), which its gate does not read.
- order 10 re-entered at step 77 by `sa.charity_limited` (order 10), left after step 75, 1 between. Late: reachable only after the answer to `sa.gifts` (step 76), its parent or roster.
- order 5 re-entered at step 78 by `$gift` (order 5), left after step 76, 1 between. Late: reachable only after the answer to `sa.charity_limited` (step 77), which its gate does not read.
- order 10 re-entered at step 79 by `gift[books].special` (order 10), left after step 77, 1 between. Late: reachable only after the answer to `$gift` (step 78), its parent or roster.
- order 1 re-entered at step 93 by `$sales` (order 1), left after step 7, 85 between. Late: reachable only after the answer to `sd.other_forms` (step 92), which its gate does not read.
- order 2 re-entered at step 94 by `sales[s1].box` (order 2), left after step 13, 80 between. Late: reachable only after the answer to `$sales` (step 93), its parent or roster.
- order 3 re-entered at step 95 by `sales[s1].special` (order 3), left after step 41, 53 between. Late: reachable only after the answer to `sales[s1].box` (step 94), which its gate does not read.
- order 4 re-entered at step 96 by `sales[s1].code` (order 4), left after step 43, 52 between. Late: reachable only after the answer to `sales[s1].special` (step 95), which its gate does not read.
- order 5 re-entered at step 97 by `sales[s1].route` (order 5), left after step 78, 18 between. Late: reachable only after the answer to `sales[s1].code` (step 96), which its gate does not read.
- order 10 re-entered at step 98 by `sales[s1].proceeds` (order 10), left after step 92, 5 between. Late: reachable only after the answer to `sales[s1].route` (step 97), which its gate does not read.
- order 10 re-entered at step 103 by `s1a.overtime` (order 10), left after step 101, 1 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 102), which its gate does not read.
- order 10 re-entered at step 115 by `qbi.dividends` (order 10), left after step 104, 10 between. Late: reachable only after the answer to `div.box2d` (step 114), which its gate does not read.
- order 10 re-entered at step 119 by `qbi.unsupported` (order 10), left after step 115, 3 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 118), which its gate does not read.
- order 12 re-entered at step 120 by `qbi.carryforward` (order 12), left after step 105, 14 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 118), which its gate does not read.
- form person re-entered at step 11 by `person[taxpayer].under16` (order 2), left after step 1, 9 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 12 by `household.community_property` (order 2), left after step 10, 1 between. Late: reachable only after the answer to `person[taxpayer].under16` (step 11), which its gate does not read.
- form f1040 re-entered at step 20 by `f1040.line25b` (order 10), left after step 2, 17 between. Sorting: it was reachable (since step 1), and `scope.other_line16` was asked instead (the bank puts order 0 first).
- form interest re-entered at step 36 by `interest[bank_a].amount` (order 10), left after step 17, 18 between. Sorting: it was reachable (since step 18), and `$f8889@person[taxpayer]` was asked instead (the bank puts order 9 seq 1 first).
- form person re-entered at step 38 by `person[taxpayer].age65` (order 10), left after step 11, 26 between. Late: left for `household.community_property` (order 2), which sorts earlier and was reachable only after the answer to `person[taxpayer].under16` (step 11), which its gate does not read.
- form w2 re-entered at step 41 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 16, 24 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 40), which its gate does not read.
- form s1 re-entered at step 48 by `s1.cod_any` (order 10), left after step 46, 1 between. Late: left for `$oi8z` (order 10), which sorts earlier and was reachable only after the answer to `s1.line8_other` (step 46), which its gate does not read.
- form person re-entered at step 59 by `person[taxpayer].x_other` (order 10), left after step 40, 18 between. Late: reachable only after the answer to `s2.other` (step 58), which its gate does not read.
- form s3 re-entered at step 60 by `s3.credit_bond` (order 10), left after step 13, 46 between. Sorting: it was reachable (since step 14), and `$w2@person[taxpayer]` was asked instead (the bank puts order 5 first).
- form person re-entered at step 70 by `person[taxpayer].blind` (order 10), left after step 59, 10 between. Late: reachable only after the answer to `sa.dependent` (step 69), which its gate does not read.
- form sa re-entered at step 71 by `sa.elect_itemize` (order 10), left after step 69, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 69), which its gate does not read.
- form s3 re-entered at step 74 by `s3.mcc` (order 10), left after step 68, 5 between. Late: reachable only after the answer to `sa.line8a` (step 73), which its gate does not read.
- form sa re-entered at step 75 by `sa.unsupported` (order 10), left after step 73, 1 between. Late: left for `s3.mcc` (order 10), which sorts earlier and was reachable only after the answer to `sa.line8a` (step 73), which its gate does not read.
- form sa re-entered at step 81 by `sa.line1` (order 10), left after step 77, 3 between. Late: left for `$gift` (order 5), which sorts earlier and was reachable only after the answer to `sa.charity_limited` (step 77), which its gate does not read.
- form f1040 re-entered at step 87 by `f1040.line3a` (order 10), left after step 22, 64 between. Late: reachable only after the answer to `sb.ordinary_dividends` (step 86), which its gate does not read.
- form sb re-entered at step 88 by `sb.unsupported` (order 10), left after step 86, 1 between. Late: left for `f1040.line3a` (order 10), which sorts earlier and was reachable only after the answer to `sb.ordinary_dividends` (step 86), which its gate does not read.
- form s1a re-entered at step 103 by `s1a.overtime` (order 10), left after step 56, 46 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 102), which its gate does not read.
- form div re-entered at step 106 by `div.box2c` (order 15), left after step 19, 86 between. Late: reachable only after the answer to `sd.distributions` (step 91), which its gate does not read.
- form person re-entered at step 118 by `person[taxpayer].sav_trad` (order 22), left after step 70, 47 between. Sorting: it was reachable (since step 2), and `sa.elect_itemize` was asked instead (the bank puts order 10 first).
- form qbi re-entered at step 119 by `qbi.unsupported` (order 10), left after step 115, 3 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 118), which its gate does not read.
- `sa.line11` (order 10), step 82: child of `sa.gifts` (step 76), 4 other questions between. Late: reachable only after the answer to `sa.charity_limited` (step 77), which its gate does not read.
- `sb.ordinary_dividends` (order 10), step 86: child of `div.any` (step 19), 66 other questions between. Sorting: it was reachable (since step 20), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `sd.distributions` (order 10), step 91: child of `div.any` (step 19), 70 other questions between. Sorting: it was reachable (since step 20), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `div.box13` (order 15), step 107: child of `div.any` (step 19), 85 other questions between. Late: reachable only after the answer to `div.box2c` (step 106), which its gate does not read.
- `div.box10` (order 15), step 108: child of `div.any` (step 19), 85 other questions between. Late: reachable only after the answer to `div.box13` (step 107), which its gate does not read.
- `div.box3` (order 15), step 111: child of `div.any` (step 19), 87 other questions between. Late: reachable only after the answer to `div.box13` (step 107), which its gate does not read.
- `div.box9` (order 15), step 112: child of `div.any` (step 19), 87 other questions between. Late: reachable only after the answer to `div.box13` (step 107), which its gate does not read.

### generated returns

**generated.0**: 121 questions, complete; order re-entries 12, form re-entries 5 sorting and 15 late, delayed children 0 sorting and 1 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 2:dependent×1 · 2:household×2 · 2:person×1 · 2:household×1 · 2:s3×1 · 5:w2×1 · 3:w2×2 · 8:interest×1 · 9:f8889×13 · 10:div×1 · 10:f1040×3 · 10:f4952×6 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:interest×2 · 10:person×3 · 3:w2×1 · 4:w2×2 · 10:refund×1 · 10:s1×2 · 10:oi8z×1 · 10:s1×8 · 10:s1a×1 · 10:s2×2 · 10:person×1 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×3 · 10:s3×1 · 10:sa×1 · 5:sa×1 · 10:sa×1 · 5:gift×1 · 10:gift×4 · 10:sa×5 · 10:sb×2 · 10:sd×2 · 1:sales×1 · 10:sli×1 · 10:ssb×1 · 11:sc×1 · 10:s1a×2 · 12:s179×1 · 20:f2441×2 · 22:person×1 · 10:qbi×1 · 12:qbi×1 · 24:f5695×2 · 30:person×1 · 30:f1040×1 · 30:eic×1 · 30:person×2 · 30:eic×2 · 20:s8812×1

- order 3 re-entered at step 49 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 16, 32 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 48), which its gate does not read.
- order 10 re-entered at step 52 by `refund.received` (order 10), left after step 48, 3 between. Late: left for `person[taxpayer].w2[emp_a].box4` (order 3), which sorts earlier and was reachable only after the answer to `person[taxpayer].rrta` (step 48), which its gate does not read.
- order 5 re-entered at step 84 by `sa.gifts` (order 5), left after step 14, 69 between. Late: reachable only after the answer to `sa.unsupported` (step 83), which its gate does not read.
- order 10 re-entered at step 85 by `sa.charity_limited` (order 10), left after step 83, 1 between. Late: reachable only after the answer to `sa.gifts` (step 84), its parent or roster.
- order 5 re-entered at step 86 by `$gift` (order 5), left after step 84, 1 between. Late: reachable only after the answer to `sa.charity_limited` (step 85), which its gate does not read.
- order 10 re-entered at step 87 by `gift[item_a].special` (order 10), left after step 85, 1 between. Late: reachable only after the answer to `$gift` (step 86), its parent or roster.
- order 1 re-entered at step 100 by `$sales` (order 1), left after step 7, 92 between. Late: reachable only after the answer to `sd.other_forms` (step 99), which its gate does not read.
- order 10 re-entered at step 101 by `sli.interest` (order 10), left after step 99, 1 between. Late: left for `$sales` (order 1), which sorts earlier and was reachable only after the answer to `sd.other_forms` (step 99), which its gate does not read.
- order 10 re-entered at step 104 by `s1a.overtime` (order 10), left after step 102, 1 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 103), which its gate does not read.
- order 10 re-entered at step 110 by `qbi.unsupported` (order 10), left after step 105, 4 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 109), which its gate does not read.
- order 12 re-entered at step 111 by `qbi.carryforward` (order 12), left after step 106, 4 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 109), which its gate does not read.
- order 20 re-entered at step 121 by `s8812.combat_pay` (order 20), left after step 108, 12 between. Late: reachable only after the answer to `eic.qc_of_another` (step 120), which its gate does not read.
- form person re-entered at step 11 by `person[taxpayer].under16` (order 2), left after step 1, 9 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 12 by `household.community_property` (order 2), left after step 10, 1 between. Late: reachable only after the answer to `person[taxpayer].under16` (step 11), which its gate does not read.
- form f1040 re-entered at step 32 by `f1040.line25b` (order 10), left after step 2, 29 between. Sorting: it was reachable (since step 1), and `scope.other_line16` was asked instead (the bank puts order 0 first).
- form interest re-entered at step 44 by `interest[bank_a].amount` (order 10), left after step 17, 26 between. Sorting: it was reachable (since step 18), and `$f8889@person[taxpayer]` was asked instead (the bank puts order 9 seq 1 first).
- form person re-entered at step 46 by `person[taxpayer].age65` (order 10), left after step 11, 34 between. Late: left for `household.community_property` (order 2), which sorts earlier and was reachable only after the answer to `person[taxpayer].under16` (step 11), which its gate does not read.
- form w2 re-entered at step 49 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 16, 32 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 48), which its gate does not read.
- form s1 re-entered at step 56 by `s1.cod_any` (order 10), left after step 54, 1 between. Late: left for `$oi8z` (order 10), which sorts earlier and was reachable only after the answer to `s1.line8_other` (step 54), which its gate does not read.
- form person re-entered at step 67 by `person[taxpayer].x_other` (order 10), left after step 48, 18 between. Late: reachable only after the answer to `s2.other` (step 66), which its gate does not read.
- form s3 re-entered at step 68 by `s3.credit_bond` (order 10), left after step 13, 54 between. Sorting: it was reachable (since step 14), and `$w2@person[taxpayer]` was asked instead (the bank puts order 5 first).
- form person re-entered at step 78 by `person[taxpayer].blind` (order 10), left after step 67, 10 between. Late: reachable only after the answer to `sa.dependent` (step 77), which its gate does not read.
- form sa re-entered at step 79 by `sa.elect_itemize` (order 10), left after step 77, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 77), which its gate does not read.
- form s3 re-entered at step 82 by `s3.mcc` (order 10), left after step 76, 5 between. Late: reachable only after the answer to `sa.line8a` (step 81), which its gate does not read.
- form sa re-entered at step 83 by `sa.unsupported` (order 10), left after step 81, 1 between. Late: left for `s3.mcc` (order 10), which sorts earlier and was reachable only after the answer to `sa.line8a` (step 81), which its gate does not read.
- form sa re-entered at step 91 by `sa.line1` (order 10), left after step 85, 5 between. Late: left for `$gift` (order 5), which sorts earlier and was reachable only after the answer to `sa.charity_limited` (step 85), which its gate does not read.
- form s1a re-entered at step 104 by `s1a.overtime` (order 10), left after step 64, 39 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 103), which its gate does not read.
- form person re-entered at step 109 by `person[taxpayer].sav_trad` (order 22), left after step 78, 30 between. Sorting: it was reachable (since step 2), and `sa.elect_itemize` was asked instead (the bank puts order 10 first).
- form person re-entered at step 114 by `person[taxpayer].eic_ssn` (order 30), left after step 109, 4 between. Late: left for `qbi.unsupported` (order 10), which sorts earlier and was reachable only after the answer to `person[taxpayer].sav_trad` (step 109), which its gate does not read.
- form f1040 re-entered at step 115 by `f1040.tax_exempt_interest` (order 30), left after step 34, 80 between. Late: reachable only after the answer to `person[taxpayer].eic_ssn` (step 114), which its gate does not read.
- form person re-entered at step 117 by `person[taxpayer].born_after_1960` (order 30), left after step 114, 2 between. Late: reachable only after the answer to `eic.died_2025` (step 116), which its gate does not read.
- form eic re-entered at step 119 by `eic.us_home` (order 30), left after step 116, 2 between. Late: reachable only after the answer to `person[taxpayer].born_before_2001` (step 118), which its gate does not read.
- `sa.line11` (order 10), step 92: child of `sa.gifts` (step 84), 6 other questions between. Late: reachable only after the answer to `sa.charity_limited` (step 85), which its gate does not read.

**generated.1**: 41 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 2:dependent×31 · 2:household×3

**generated.2**: 2 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1

**generated.3**: 2 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1

**generated.4**: 141 questions, complete; order re-entries 16, form re-entries 6 sorting and 13 late, delayed children 2 sorting and 5 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 2:dependent×1 · 2:household×2 · 2:person×1 · 2:household×1 · 2:s3×1 · 5:w2×1 · 3:w2×2 · 8:interest×1 · 9:f8889×13 · 10:div×1 · 10:f1040×3 · 10:f4952×2 · 10:f8863×1 · 10:f8959×1 · 10:ftc×5 · 10:interest×4 · 10:person×3 · 3:w2×1 · 4:w2×2 · 10:refund×1 · 10:s1×2 · 10:oi8z×1 · 10:s1×8 · 10:s1a×1 · 10:s2×2 · 10:person×1 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×4 · 5:sa×1 · 10:sa×1 · 5:gift×1 · 10:gift×2 · 10:sa×5 · 10:sb×1 · 10:f1040×1 · 10:sb×2 · 10:sd×3 · 1:sales×1 · 2:sales×2 · 3:sales×2 · 4:sales×2 · 5:sales×2 · 10:sales×7 · 10:sli×1 · 10:ssb×1 · 11:sc×1 · 10:s1a×2 · 12:s179×1 · 15:div×9 · 10:qbi×1 · 20:f2441×2 · 22:person×1 · 24:f5695×2 · 25:person×1 · 10:qbi×1 · 12:qbi×1

- order 3 re-entered at step 51 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 16, 34 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 50), which its gate does not read.
- order 10 re-entered at step 54 by `refund.received` (order 10), left after step 50, 3 between. Late: left for `person[taxpayer].w2[emp_a].box4` (order 3), which sorts earlier and was reachable only after the answer to `person[taxpayer].rrta` (step 50), which its gate does not read.
- order 5 re-entered at step 85 by `sa.gifts` (order 5), left after step 14, 70 between. Late: reachable only after the answer to `sa.unsupported` (step 84), which its gate does not read.
- order 10 re-entered at step 86 by `sa.charity_limited` (order 10), left after step 84, 1 between. Late: reachable only after the answer to `sa.gifts` (step 85), its parent or roster.
- order 5 re-entered at step 87 by `$gift` (order 5), left after step 85, 1 between. Late: reachable only after the answer to `sa.charity_limited` (step 86), which its gate does not read.
- order 10 re-entered at step 88 by `gift[item_a].special` (order 10), left after step 86, 1 between. Late: reachable only after the answer to `$gift` (step 87), its parent or roster.
- order 1 re-entered at step 102 by `$sales` (order 1), left after step 7, 94 between. Late: reachable only after the answer to `sd.other_forms` (step 101), which its gate does not read.
- order 2 re-entered at step 103 by `sales[s1].box` (order 2), left after step 13, 89 between. Late: reachable only after the answer to `$sales` (step 102), its parent or roster.
- order 3 re-entered at step 105 by `sales[s1].special` (order 3), left after step 51, 53 between. Late: reachable only after the answer to `sales[s1].box` (step 103), which its gate does not read.
- order 4 re-entered at step 107 by `sales[s1].code` (order 4), left after step 53, 53 between. Late: reachable only after the answer to `sales[s1].special` (step 105), which its gate does not read.
- order 5 re-entered at step 109 by `sales[s1].route` (order 5), left after step 87, 21 between. Late: reachable only after the answer to `sales[s1].code` (step 107), which its gate does not read.
- order 10 re-entered at step 111 by `sales[s1].correct_basis` (order 10), left after step 101, 9 between. Late: reachable only after the answer to `sales[s2].route` (step 110), which its gate does not read.
- order 10 re-entered at step 121 by `s1a.overtime` (order 10), left after step 119, 1 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 120), which its gate does not read.
- order 10 re-entered at step 133 by `qbi.dividends` (order 10), left after step 122, 10 between. Late: reachable only after the answer to `div.box2d` (step 132), which its gate does not read.
- order 10 re-entered at step 140 by `qbi.unsupported` (order 10), left after step 133, 6 between. Late: reachable only after the answer to `person[taxpayer].sav_claimed` (step 139), which its gate does not read.
- order 12 re-entered at step 141 by `qbi.carryforward` (order 12), left after step 123, 17 between. Late: reachable only after the answer to `person[taxpayer].sav_claimed` (step 139), which its gate does not read.
- form person re-entered at step 11 by `person[taxpayer].under16` (order 2), left after step 1, 9 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 12 by `household.community_property` (order 2), left after step 10, 1 between. Late: reachable only after the answer to `person[taxpayer].under16` (step 11), which its gate does not read.
- form f1040 re-entered at step 32 by `f1040.line25b` (order 10), left after step 2, 29 between. Sorting: it was reachable (since step 1), and `scope.other_line16` was asked instead (the bank puts order 0 first).
- form interest re-entered at step 44 by `interest[bank_a].amount` (order 10), left after step 17, 26 between. Sorting: it was reachable (since step 18), and `$f8889@person[taxpayer]` was asked instead (the bank puts order 9 seq 1 first).
- form person re-entered at step 48 by `person[taxpayer].age65` (order 10), left after step 11, 36 between. Late: left for `household.community_property` (order 2), which sorts earlier and was reachable only after the answer to `person[taxpayer].under16` (step 11), which its gate does not read.
- form w2 re-entered at step 51 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 16, 34 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 50), which its gate does not read.
- form s1 re-entered at step 58 by `s1.cod_any` (order 10), left after step 56, 1 between. Late: left for `$oi8z` (order 10), which sorts earlier and was reachable only after the answer to `s1.line8_other` (step 56), which its gate does not read.
- form person re-entered at step 69 by `person[taxpayer].x_other` (order 10), left after step 50, 18 between. Late: reachable only after the answer to `s2.other` (step 68), which its gate does not read.
- form s3 re-entered at step 70 by `s3.credit_bond` (order 10), left after step 13, 56 between. Sorting: it was reachable (since step 14), and `$w2@person[taxpayer]` was asked instead (the bank puts order 5 first).
- form person re-entered at step 80 by `person[taxpayer].blind` (order 10), left after step 69, 10 between. Late: reachable only after the answer to `sa.dependent` (step 79), which its gate does not read.
- form sa re-entered at step 81 by `sa.elect_itemize` (order 10), left after step 79, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 79), which its gate does not read.
- form sa re-entered at step 90 by `sa.line1` (order 10), left after step 86, 3 between. Late: left for `$gift` (order 5), which sorts earlier and was reachable only after the answer to `sa.charity_limited` (step 86), which its gate does not read.
- form f1040 re-entered at step 96 by `f1040.line3a` (order 10), left after step 34, 61 between. Late: reachable only after the answer to `sb.ordinary_dividends` (step 95), which its gate does not read.
- form sb re-entered at step 97 by `sb.unsupported` (order 10), left after step 95, 1 between. Late: left for `f1040.line3a` (order 10), which sorts earlier and was reachable only after the answer to `sb.ordinary_dividends` (step 95), which its gate does not read.
- form s1a re-entered at step 121 by `s1a.overtime` (order 10), left after step 66, 54 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 120), which its gate does not read.
- form div re-entered at step 124 by `div.box2c` (order 15), left after step 31, 92 between. Late: reachable only after the answer to `sd.distributions` (step 100), which its gate does not read.
- form person re-entered at step 136 by `person[taxpayer].sav_trad` (order 22), left after step 80, 55 between. Sorting: it was reachable (since step 2), and `sa.elect_itemize` was asked instead (the bank puts order 10 first).
- form person re-entered at step 139 by `person[taxpayer].sav_claimed` (order 25), left after step 136, 2 between. Sorting: it was reachable (since step 119), and `f5695.part1_any` was asked instead (the bank puts order 24 first).
- form qbi re-entered at step 140 by `qbi.unsupported` (order 10), left after step 133, 6 between. Late: reachable only after the answer to `person[taxpayer].sav_claimed` (step 139), which its gate does not read.
- `sa.line11` (order 10), step 91: child of `sa.gifts` (step 85), 4 other questions between. Late: reachable only after the answer to `sa.charity_limited` (step 86), which its gate does not read.
- `sb.ordinary_dividends` (order 10), step 95: child of `div.any` (step 31), 63 other questions between. Sorting: it was reachable (since step 32), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `sd.distributions` (order 10), step 100: child of `div.any` (step 31), 67 other questions between. Sorting: it was reachable (since step 32), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `div.box13` (order 15), step 125: child of `div.any` (step 31), 91 other questions between. Late: reachable only after the answer to `div.box2c` (step 124), which its gate does not read.
- `div.box10` (order 15), step 126: child of `div.any` (step 31), 91 other questions between. Late: reachable only after the answer to `div.box13` (step 125), which its gate does not read.
- `div.box3` (order 15), step 129: child of `div.any` (step 31), 93 other questions between. Late: reachable only after the answer to `div.box13` (step 125), which its gate does not read.
- `div.box9` (order 15), step 130: child of `div.any` (step 31), 93 other questions between. Late: reachable only after the answer to `div.box13` (step 125), which its gate does not read.

**generated.5**: 20 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 2:dependent×10 · 2:household×3

**generated.6**: 172 questions, complete; order re-entries 20, form re-entries 4 sorting and 23 late, delayed children 0 sorting and 1 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 2:dependent×1 · 2:household×2 · 2:person×1 · 2:household×1 · 2:s3×1 · 5:w2×1 · 3:w2×2 · 8:interest×1 · 9:f8889×13 · 10:div×1 · 10:f1040×3 · 10:f4952×6 · 10:f8863×1 · 10:f8959×1 · 10:f8962×3 · 2:f1095a×2 · 10:f8962×1 · 10:ftc×1 · 10:person×3 · 3:w2×1 · 4:w2×2 · 10:refund×1 · 10:s1×2 · 10:oi8z×1 · 10:s1×8 · 10:s1a×1 · 10:s2×2 · 10:person×1 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×3 · 10:s3×1 · 10:sa×1 · 5:sa×1 · 10:sa×1 · 5:gift×1 · 10:sa×5 · 10:sb×1 · 10:sd×2 · 1:sales×1 · 10:sli×1 · 10:ssb×1 · 11:sc×1 · 10:s1a×2 · 12:s179×1 · 20:f2441×2 · 22:person×1 · 10:qbi×1 · 12:qbi×1 · 24:f5695×2 · 30:f1040×1 · 11:f8962×1 · 2:f1095a×15 · 10:f8962×1 · 11:f8962×1 · 2:f1095a×28 · 25:person×4 · 25:w2×1 · 25:person×1 · 30:person×1 · 30:eic×1 · 30:person×2 · 30:eic×2 · 20:s8812×1

- order 2 re-entered at step 46 by `f1095a[mkt_a].void` (order 2), left after step 13, 32 between. Late: reachable only after the answer to `f8962.premium_adjust` (step 45), which its gate does not read.
- order 10 re-entered at step 48 by `f8962.fpl_table` (order 10), left after step 45, 2 between. Late: reachable only after the answer to `f1095a[mkt_b].void` (step 47), which its gate does not read.
- order 3 re-entered at step 53 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 16, 36 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 52), which its gate does not read.
- order 10 re-entered at step 56 by `refund.received` (order 10), left after step 52, 3 between. Late: left for `person[taxpayer].w2[emp_a].box4` (order 3), which sorts earlier and was reachable only after the answer to `person[taxpayer].rrta` (step 52), which its gate does not read.
- order 5 re-entered at step 88 by `sa.gifts` (order 5), left after step 14, 73 between. Late: reachable only after the answer to `sa.unsupported` (step 87), which its gate does not read.
- order 10 re-entered at step 89 by `sa.charity_limited` (order 10), left after step 87, 1 between. Late: reachable only after the answer to `sa.gifts` (step 88), its parent or roster.
- order 5 re-entered at step 90 by `$gift` (order 5), left after step 88, 1 between. Late: reachable only after the answer to `sa.charity_limited` (step 89), which its gate does not read.
- order 10 re-entered at step 91 by `sa.line1` (order 10), left after step 89, 1 between. Late: left for `$gift` (order 5), which sorts earlier and was reachable only after the answer to `sa.charity_limited` (step 89), which its gate does not read.
- order 1 re-entered at step 99 by `$sales` (order 1), left after step 7, 91 between. Late: reachable only after the answer to `sd.other_forms` (step 98), which its gate does not read.
- order 10 re-entered at step 100 by `sli.interest` (order 10), left after step 98, 1 between. Late: left for `$sales` (order 1), which sorts earlier and was reachable only after the answer to `sd.other_forms` (step 98), which its gate does not read.
- order 10 re-entered at step 103 by `s1a.overtime` (order 10), left after step 101, 1 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 102), which its gate does not read.
- order 10 re-entered at step 109 by `qbi.unsupported` (order 10), left after step 104, 4 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 108), which its gate does not read.
- order 12 re-entered at step 110 by `qbi.carryforward` (order 12), left after step 105, 4 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 108), which its gate does not read.
- order 11 re-entered at step 114 by `f8962.alien_below` (order 11), left after step 102, 11 between. Late: reachable only after the answer to `f1040.tax_exempt_interest` (step 113), which its gate does not read.
- order 2 re-entered at step 115 by `f1095a[mkt_a].uniform` (order 2), left after step 47, 67 between. Late: reachable only after the answer to `f8962.alien_below` (step 114), which its gate does not read.
- order 10 re-entered at step 130 by `f8962.same_state_counted` (order 10), left after step 109, 20 between. Late: reachable only after the answer to `f8962.alien_below` (step 114), which its gate does not read.
- order 11 re-entered at step 131 by `f8962.estimate_100` (order 11), left after step 114, 16 between. Late: reachable only after the answer to `f1095a[mkt_b].in_c_sep` (step 129), which its gate does not read.
- order 2 re-entered at step 132 by `f1095a[mkt_a].b_counted` (order 2), left after step 129, 2 between. Late: reachable only after the answer to `f8962.estimate_100` (step 131), which its gate does not read.
- order 30 re-entered at step 166 by `person[taxpayer].eic_ssn` (order 30), left after step 113, 52 between. Late: left for `f8962.alien_below` (order 11), which sorts earlier and was reachable only after the answer to `f1040.tax_exempt_interest` (step 113), which its gate does not read.
- order 20 re-entered at step 172 by `s8812.combat_pay` (order 20), left after step 107, 64 between. Late: reachable only after the answer to `eic.qc_of_another` (step 171), which its gate does not read.
- form person re-entered at step 11 by `person[taxpayer].under16` (order 2), left after step 1, 9 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 12 by `household.community_property` (order 2), left after step 10, 1 between. Late: reachable only after the answer to `person[taxpayer].under16` (step 11), which its gate does not read.
- form f1040 re-entered at step 32 by `f1040.line25b` (order 10), left after step 2, 29 between. Sorting: it was reachable (since step 1), and `scope.other_line16` was asked instead (the bank puts order 0 first).
- form f1095a re-entered at step 46 by `f1095a[mkt_a].void` (order 2), left after step 6, 39 between. Late: reachable only after the answer to `f8962.premium_adjust` (step 45), which its gate does not read.
- form f8962 re-entered at step 48 by `f8962.fpl_table` (order 10), left after step 45, 2 between. Late: reachable only after the answer to `f1095a[mkt_b].void` (step 47), which its gate does not read.
- form person re-entered at step 50 by `person[taxpayer].age65` (order 10), left after step 11, 38 between. Late: left for `household.community_property` (order 2), which sorts earlier and was reachable only after the answer to `person[taxpayer].under16` (step 11), which its gate does not read.
- form w2 re-entered at step 53 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 16, 36 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 52), which its gate does not read.
- form s1 re-entered at step 60 by `s1.cod_any` (order 10), left after step 58, 1 between. Late: left for `$oi8z` (order 10), which sorts earlier and was reachable only after the answer to `s1.line8_other` (step 58), which its gate does not read.
- form person re-entered at step 71 by `person[taxpayer].x_other` (order 10), left after step 52, 18 between. Late: reachable only after the answer to `s2.other` (step 70), which its gate does not read.
- form s3 re-entered at step 72 by `s3.credit_bond` (order 10), left after step 13, 58 between. Sorting: it was reachable (since step 14), and `$w2@person[taxpayer]` was asked instead (the bank puts order 5 first).
- form person re-entered at step 82 by `person[taxpayer].blind` (order 10), left after step 71, 10 between. Late: reachable only after the answer to `sa.dependent` (step 81), which its gate does not read.
- form sa re-entered at step 83 by `sa.elect_itemize` (order 10), left after step 81, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 81), which its gate does not read.
- form s3 re-entered at step 86 by `s3.mcc` (order 10), left after step 80, 5 between. Late: reachable only after the answer to `sa.line8a` (step 85), which its gate does not read.
- form sa re-entered at step 87 by `sa.unsupported` (order 10), left after step 85, 1 between. Late: left for `s3.mcc` (order 10), which sorts earlier and was reachable only after the answer to `sa.line8a` (step 85), which its gate does not read.
- form sa re-entered at step 91 by `sa.line1` (order 10), left after step 89, 1 between. Late: left for `$gift` (order 5), which sorts earlier and was reachable only after the answer to `sa.charity_limited` (step 89), which its gate does not read.
- form s1a re-entered at step 103 by `s1a.overtime` (order 10), left after step 68, 34 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 102), which its gate does not read.
- form person re-entered at step 108 by `person[taxpayer].sav_trad` (order 22), left after step 82, 25 between. Sorting: it was reachable (since step 2), and `sa.elect_itemize` was asked instead (the bank puts order 10 first).
- form f1040 re-entered at step 113 by `f1040.tax_exempt_interest` (order 30), left after step 34, 78 between. Late: reachable only after the answer to `f1095a[mkt_b].void` (step 47), which its gate does not read.
- form f8962 re-entered at step 114 by `f8962.alien_below` (order 11), left after step 48, 65 between. Late: reachable only after the answer to `f1040.tax_exempt_interest` (step 113), which its gate does not read.
- form f1095a re-entered at step 115 by `f1095a[mkt_a].uniform` (order 2), left after step 47, 67 between. Late: reachable only after the answer to `f8962.alien_below` (step 114), which its gate does not read.
- form f8962 re-entered at step 130 by `f8962.same_state_counted` (order 10), left after step 114, 15 between. Late: left for `f1095a[mkt_a].uniform` (order 2), which sorts earlier and was reachable only after the answer to `f8962.alien_below` (step 114), which its gate does not read.
- form f1095a re-entered at step 132 by `f1095a[mkt_a].b_counted` (order 2), left after step 129, 2 between. Late: reachable only after the answer to `f8962.estimate_100` (step 131), which its gate does not read.
- form person re-entered at step 160 by `person[taxpayer].sav_born` (order 25), left after step 108, 51 between. Late: reachable only after the answer to `f1095a[mkt_b].in_a_sep` (step 159), which its gate does not read.
- form w2 re-entered at step 164 by `person[taxpayer].w2[emp_a].box12_any` (order 25), left after step 55, 108 between. Late: reachable only after the answer to `person[taxpayer].sav_student` (step 161), which its gate does not read.
- form person re-entered at step 165 by `person[taxpayer].sav_voluntary` (order 25), left after step 163, 1 between. Late: reachable only after the answer to `person[taxpayer].w2[emp_a].box12_any` (step 164), which its gate does not read.
- form person re-entered at step 168 by `person[taxpayer].born_after_1960` (order 30), left after step 166, 1 between. Late: reachable only after the answer to `eic.died_2025` (step 167), which its gate does not read.
- form eic re-entered at step 170 by `eic.us_home` (order 30), left after step 167, 2 between. Late: reachable only after the answer to `person[taxpayer].born_before_2001` (step 169), which its gate does not read.
- `sa.line11` (order 10), step 92: child of `sa.gifts` (step 88), 2 other questions between. Late: reachable only after the answer to `sa.charity_limited` (step 89), which its gate does not read.

**generated.7**: 4 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:scope×3

**generated.8**: 2 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1

**generated.9**: 3 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×1

**generated.10**: 197 questions, refused; order re-entries 14, form re-entries 8 sorting and 11 late, delayed children 2 sorting and 1 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 2:dependent×9 · 2:household×2 · 2:person×1 · 2:household×1 · 2:s3×1 · 3:dependent×2 · 2:dependent×2 · 5:w2×1 · 3:w2×4 · 8:interest×1 · 9:f8889×13 · 10:div×1 · 10:f1040×3 · 10:f4952×2 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:interest×2 · 10:person×3 · 3:w2×2 · 4:w2×8 · 10:refund×1 · 10:s1×2 · 10:oi8z×1 · 10:s1×8 · 10:s1a×1 · 10:s2×2 · 10:person×1 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×3 · 10:s3×1 · 10:sa×1 · 5:sa×1 · 10:sa×1 · 5:gift×1 · 10:gift×4 · 10:sa×5 · 10:sb×3 · 10:sd×3 · 1:sales×1 · 2:sales×3 · 3:sales×3 · 4:sales×3 · 5:sales×3 · 10:sales×8 · 10:sli×1 · 10:ssb×1 · 11:sc×1 · 11:asset×1 · 11:scveh×1 · 12:person×1 · 12:asset×10 · 12:sc×35 · 12:scveh×7

- order 2 re-entered at step 24 by `dependent[dep_a].gross_income` (order 2), left after step 21, 2 between. Late: reachable only after the answer to `dependent[dep_a].qr_all_year` (step 23), which its gate does not read.
- order 3 re-entered at step 27 by `person[taxpayer].w2[emp_a].box1` (order 3), left after step 23, 3 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 26), its parent or roster.
- order 3 re-entered at step 59 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 30, 28 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 58), which its gate does not read.
- order 10 re-entered at step 69 by `refund.received` (order 10), left after step 58, 10 between. Late: left for `person[taxpayer].w2[emp_a].box4` (order 3), which sorts earlier and was reachable only after the answer to `person[taxpayer].rrta` (step 58), which its gate does not read.
- order 5 re-entered at step 101 by `sa.gifts` (order 5), left after step 26, 74 between. Late: reachable only after the answer to `sa.unsupported` (step 100), which its gate does not read.
- order 10 re-entered at step 102 by `sa.charity_limited` (order 10), left after step 100, 1 between. Late: reachable only after the answer to `sa.gifts` (step 101), its parent or roster.
- order 5 re-entered at step 103 by `$gift` (order 5), left after step 101, 1 between. Late: reachable only after the answer to `sa.charity_limited` (step 102), which its gate does not read.
- order 10 re-entered at step 104 by `gift[item_a].special` (order 10), left after step 102, 1 between. Late: reachable only after the answer to `$gift` (step 103), its parent or roster.
- order 1 re-entered at step 119 by `$sales` (order 1), left after step 7, 111 between. Late: reachable only after the answer to `sd.other_forms` (step 118), which its gate does not read.
- order 2 re-entered at step 120 by `sales[s1].box` (order 2), left after step 25, 94 between. Late: reachable only after the answer to `$sales` (step 119), its parent or roster.
- order 3 re-entered at step 123 by `sales[s1].special` (order 3), left after step 60, 62 between. Late: reachable only after the answer to `sales[s1].box` (step 120), which its gate does not read.
- order 4 re-entered at step 126 by `sales[s1].code` (order 4), left after step 68, 57 between. Late: reachable only after the answer to `sales[s1].special` (step 123), which its gate does not read.
- order 5 re-entered at step 129 by `sales[s1].route` (order 5), left after step 103, 25 between. Late: reachable only after the answer to `sales[s1].code` (step 126), which its gate does not read.
- order 10 re-entered at step 132 by `sales[s1].proceeds` (order 10), left after step 118, 13 between. Late: reachable only after the answer to `sales[s3].route` (step 131), which its gate does not read.
- form person re-entered at step 19 by `person[taxpayer].under16` (order 2), left after step 1, 17 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 20 by `household.community_property` (order 2), left after step 18, 1 between. Late: reachable only after the answer to `person[taxpayer].under16` (step 19), which its gate does not read.
- form dependent re-entered at step 22 by `dependent[dep_a].lawful` (order 3), left after step 16, 5 between. Sorting: it was reachable (since step 17), and `household.married` was asked instead (the bank puts order 2 first).
- form f1040 re-entered at step 46 by `f1040.line25b` (order 10), left after step 2, 43 between. Sorting: it was reachable (since step 1), and `scope.other_line16` was asked instead (the bank puts order 0 first).
- form interest re-entered at step 54 by `interest[bank_a].amount` (order 10), left after step 31, 22 between. Sorting: it was reachable (since step 32), and `$f8889@person[taxpayer]` was asked instead (the bank puts order 9 seq 1 first).
- form person re-entered at step 56 by `person[taxpayer].age65` (order 10), left after step 19, 36 between. Late: left for `household.community_property` (order 2), which sorts earlier and was reachable only after the answer to `person[taxpayer].under16` (step 19), which its gate does not read.
- form w2 re-entered at step 59 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 30, 28 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 58), which its gate does not read.
- form s1 re-entered at step 73 by `s1.cod_any` (order 10), left after step 71, 1 between. Late: left for `$oi8z` (order 10), which sorts earlier and was reachable only after the answer to `s1.line8_other` (step 71), which its gate does not read.
- form person re-entered at step 84 by `person[taxpayer].x_other` (order 10), left after step 58, 25 between. Late: reachable only after the answer to `s2.other` (step 83), which its gate does not read.
- form s3 re-entered at step 85 by `s3.credit_bond` (order 10), left after step 21, 63 between. Sorting: it was reachable (since step 22), and `dependent[dep_a].lawful` was asked instead (the bank puts order 3 first).
- form person re-entered at step 95 by `person[taxpayer].blind` (order 10), left after step 84, 10 between. Late: reachable only after the answer to `sa.dependent` (step 94), which its gate does not read.
- form sa re-entered at step 96 by `sa.elect_itemize` (order 10), left after step 94, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 94), which its gate does not read.
- form s3 re-entered at step 99 by `s3.mcc` (order 10), left after step 93, 5 between. Late: reachable only after the answer to `sa.line8a` (step 98), which its gate does not read.
- form sa re-entered at step 100 by `sa.unsupported` (order 10), left after step 98, 1 between. Late: left for `s3.mcc` (order 10), which sorts earlier and was reachable only after the answer to `sa.line8a` (step 98), which its gate does not read.
- form sa re-entered at step 108 by `sa.line1` (order 10), left after step 102, 5 between. Late: left for `$gift` (order 5), which sorts earlier and was reachable only after the answer to `sa.charity_limited` (step 102), which its gate does not read.
- form person re-entered at step 145 by `person[taxpayer].plan` (order 12), left after step 95, 49 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 142), which its gate does not read.
- form asset re-entered at step 146 by `person[taxpayer].sc[biz_a].asset[item_1].class` (order 12), left after step 143, 2 between. Sorting: it was reachable (since step 144), and `$scveh@person[taxpayer].sc[biz_a]` was asked instead (the bank puts order 11 first).
- form sc re-entered at step 156 by `person[taxpayer].sc[biz_a].hi_uses` (order 12), left after step 142, 13 between. Sorting: left for `$asset@person[taxpayer].sc[biz_a]` (order 11), a child of the question before it, which the bank places in another form.
- form scveh re-entered at step 191 by `person[taxpayer].sc[biz_a].scveh[car_1].method` (order 12), left after step 144, 46 between. Sorting: it was reachable (since step 145), and `person[taxpayer].plan` was asked instead (within order 12, sorted by id).
- `sa.line11` (order 10), step 109: child of `sa.gifts` (step 101), 6 other questions between. Late: reachable only after the answer to `sa.charity_limited` (step 102), which its gate does not read.
- `sb.ordinary_dividends` (order 10), step 113: child of `div.any` (step 45), 67 other questions between. Sorting: it was reachable (since step 46), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `sd.distributions` (order 10), step 117: child of `div.any` (step 45), 70 other questions between. Sorting: it was reachable (since step 46), and `f1040.line25b` was asked instead (within order 10, sorted by id).

**generated.11**: 24 questions, refused; order re-entries 0, form re-entries 0 sorting and 2 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 2:dependent×13 · 2:household×1 · 2:dependent×1 · 2:household×2

- form dependent re-entered at step 22 by `dependent[dep_a].parent_home_paid` (order 2), left after step 20, 1 between. Late: reachable only after the answer to `household.unmarried` (step 21), which its gate does not read.
- form household re-entered at step 23 by `household.home_cost` (order 2), left after step 21, 1 between. Late: reachable only after the answer to `dependent[dep_a].parent_home_paid` (step 22), which its gate does not read.

**generated.12**: 187 questions, complete; order re-entries 24, form re-entries 7 sorting and 21 late, delayed children 2 sorting and 7 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 2:dependent×33 · 2:household×1 · 2:person×1 · 2:household×1 · 2:s3×1 · 3:dependent×1 · 2:dependent×4 · 5:w2×1 · 3:w2×4 · 8:interest×1 · 9:f8889×13 · 10:div×1 · 10:f1040×3 · 10:f4952×2 · 10:f8863×1 · 10:f8959×1 · 10:f8962×3 · 2:f1095a×1 · 10:ftc×1 · 10:person×3 · 3:w2×2 · 4:w2×8 · 10:refund×1 · 10:s1×2 · 10:oi8z×1 · 10:s1×8 · 10:s1a×1 · 10:s2×2 · 10:person×1 · 10:s3×9 · 10:sa×1 · 2:dependent×3 · 2:person×2 · 10:f8962×1 · 10:person×1 · 10:sa×3 · 10:s3×1 · 10:sa×1 · 5:sa×1 · 10:sa×1 · 5:gift×1 · 10:sa×5 · 10:sb×1 · 10:f1040×1 · 10:sb×2 · 10:sd×3 · 1:sales×1 · 2:sales×1 · 3:sales×1 · 4:sales×1 · 5:sales×1 · 10:sales×4 · 10:sli×1 · 10:ssb×1 · 11:sc×1 · 10:s1a×2 · 12:s179×1 · 15:div×9 · 10:qbi×1 · 20:f2441×2 · 20:s8812×1 · 22:person×1 · 10:qbi×1 · 12:qbi×1 · 20:household×1 · 24:f5695×2 · 30:div×1 · 30:f1040×1 · 2:f1095a×4

- order 2 re-entered at step 46 by `dependent[dep_a].gross_income` (order 2), left after step 44, 1 between. Late: reachable only after the answer to `dependent[dep_a].qr_all_year` (step 45), which its gate does not read.
- order 3 re-entered at step 51 by `person[taxpayer].w2[emp_a].box1` (order 3), left after step 45, 5 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 50), its parent or roster.
- order 2 re-entered at step 80 by `f1095a[mkt_a].void` (order 2), left after step 49, 30 between. Late: reachable only after the answer to `f8962.premium_adjust` (step 79), which its gate does not read.
- order 10 re-entered at step 81 by `ftc.taxes` (order 10), left after step 79, 1 between. Late: left for `f1095a[mkt_a].void` (order 2), which sorts earlier and was reachable only after the answer to `f8962.premium_adjust` (step 79), which its gate does not read.
- order 3 re-entered at step 85 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 54, 30 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 84), which its gate does not read.
- order 10 re-entered at step 95 by `refund.received` (order 10), left after step 84, 10 between. Late: left for `person[taxpayer].w2[emp_a].box4` (order 3), which sorts earlier and was reachable only after the answer to `person[taxpayer].rrta` (step 84), which its gate does not read.
- order 2 re-entered at step 121 by `dependent[dep_b].ptc_files` (order 2), left after step 80, 40 between. Late: reachable only after the answer to `sa.dependent` (step 120), which its gate does not read.
- order 10 re-entered at step 126 by `f8962.fpl_table` (order 10), left after step 120, 5 between. Late: left for `dependent[dep_b].ptc_files` (order 2), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 120), which its gate does not read.
- order 5 re-entered at step 133 by `sa.gifts` (order 5), left after step 50, 82 between. Late: reachable only after the answer to `sa.unsupported` (step 132), which its gate does not read.
- order 10 re-entered at step 134 by `sa.charity_limited` (order 10), left after step 132, 1 between. Late: reachable only after the answer to `sa.gifts` (step 133), its parent or roster.
- order 5 re-entered at step 135 by `$gift` (order 5), left after step 133, 1 between. Late: reachable only after the answer to `sa.charity_limited` (step 134), which its gate does not read.
- order 10 re-entered at step 136 by `sa.line1` (order 10), left after step 134, 1 between. Late: left for `$gift` (order 5), which sorts earlier and was reachable only after the answer to `sa.charity_limited` (step 134), which its gate does not read.
- order 1 re-entered at step 148 by `$sales` (order 1), left after step 7, 140 between. Late: reachable only after the answer to `sd.other_forms` (step 147), which its gate does not read.
- order 2 re-entered at step 149 by `sales[s1].box` (order 2), left after step 125, 23 between. Late: reachable only after the answer to `$sales` (step 148), its parent or roster.
- order 3 re-entered at step 150 by `sales[s1].special` (order 3), left after step 86, 63 between. Late: reachable only after the answer to `sales[s1].box` (step 149), which its gate does not read.
- order 4 re-entered at step 151 by `sales[s1].code` (order 4), left after step 94, 56 between. Late: reachable only after the answer to `sales[s1].special` (step 150), which its gate does not read.
- order 5 re-entered at step 152 by `sales[s1].route` (order 5), left after step 135, 16 between. Late: reachable only after the answer to `sales[s1].code` (step 151), which its gate does not read.
- order 10 re-entered at step 153 by `sales[s1].correct_basis` (order 10), left after step 147, 5 between. Late: reachable only after the answer to `sales[s1].route` (step 152), which its gate does not read.
- order 10 re-entered at step 160 by `s1a.overtime` (order 10), left after step 158, 1 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 159), which its gate does not read.
- order 10 re-entered at step 172 by `qbi.dividends` (order 10), left after step 161, 10 between. Late: reachable only after the answer to `div.box2d` (step 171), which its gate does not read.
- order 10 re-entered at step 177 by `qbi.unsupported` (order 10), left after step 172, 4 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 176), which its gate does not read.
- order 12 re-entered at step 178 by `qbi.carryforward` (order 12), left after step 162, 15 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 176), which its gate does not read.
- order 20 re-entered at step 179 by `household.credit_disallowed` (order 20), left after step 175, 3 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 176), which its gate does not read.
- order 2 re-entered at step 184 by `f1095a[mkt_a].uniform` (order 2), left after step 149, 34 between. Late: reachable only after the answer to `f1040.tax_exempt_interest` (step 183), which its gate does not read.
- form person re-entered at step 42 by `person[taxpayer].under16` (order 2), left after step 1, 40 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 43 by `household.community_property` (order 2), left after step 41, 1 between. Late: reachable only after the answer to `person[taxpayer].under16` (step 42), which its gate does not read.
- form dependent re-entered at step 45 by `dependent[dep_a].qr_all_year` (order 3), left after step 40, 4 between. Sorting: it was reachable (since step 18), and `household.qss_eligible` was asked instead (the bank puts order 2 first).
- form f1040 re-entered at step 70 by `f1040.line25b` (order 10), left after step 2, 67 between. Sorting: it was reachable (since step 1), and `scope.other_line16` was asked instead (the bank puts order 0 first).
- form f1095a re-entered at step 80 by `f1095a[mkt_a].void` (order 2), left after step 6, 73 between. Late: reachable only after the answer to `f8962.premium_adjust` (step 79), which its gate does not read.
- form person re-entered at step 82 by `person[taxpayer].age65` (order 10), left after step 42, 39 between. Late: left for `household.community_property` (order 2), which sorts earlier and was reachable only after the answer to `person[taxpayer].under16` (step 42), which its gate does not read.
- form w2 re-entered at step 85 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 54, 30 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 84), which its gate does not read.
- form s1 re-entered at step 99 by `s1.cod_any` (order 10), left after step 97, 1 between. Late: left for `$oi8z` (order 10), which sorts earlier and was reachable only after the answer to `s1.line8_other` (step 97), which its gate does not read.
- form person re-entered at step 110 by `person[taxpayer].x_other` (order 10), left after step 84, 25 between. Late: reachable only after the answer to `s2.other` (step 109), which its gate does not read.
- form s3 re-entered at step 111 by `s3.credit_bond` (order 10), left after step 44, 66 between. Sorting: it was reachable (since step 45), and `dependent[dep_a].qr_all_year` was asked instead (the bank puts order 3 first).
- form dependent re-entered at step 121 by `dependent[dep_b].ptc_files` (order 2), left after step 49, 71 between. Late: reachable only after the answer to `sa.dependent` (step 120), which its gate does not read.
- form person re-entered at step 124 by `person[taxpayer].tin` (order 2), left after step 110, 13 between. Late: reachable only after the answer to `sa.dependent` (step 120), which its gate does not read.
- form f8962 re-entered at step 126 by `f8962.fpl_table` (order 10), left after step 79, 46 between. Late: reachable only after the answer to `sa.dependent` (step 120), which its gate does not read.
- form person re-entered at step 127 by `person[taxpayer].blind` (order 10), left after step 125, 1 between. Sorting: it was reachable (since step 121), and `f8962.fpl_table` was asked instead (within order 10, sorted by id).
- form sa re-entered at step 128 by `sa.elect_itemize` (order 10), left after step 120, 7 between. Late: left for `dependent[dep_b].ptc_files` (order 2), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 120), which its gate does not read.
- form s3 re-entered at step 131 by `s3.mcc` (order 10), left after step 119, 11 between. Late: reachable only after the answer to `sa.line8a` (step 130), which its gate does not read.
- form sa re-entered at step 132 by `sa.unsupported` (order 10), left after step 130, 1 between. Late: left for `s3.mcc` (order 10), which sorts earlier and was reachable only after the answer to `sa.line8a` (step 130), which its gate does not read.
- form sa re-entered at step 136 by `sa.line1` (order 10), left after step 134, 1 between. Late: left for `$gift` (order 5), which sorts earlier and was reachable only after the answer to `sa.charity_limited` (step 134), which its gate does not read.
- form f1040 re-entered at step 142 by `f1040.line3a` (order 10), left after step 72, 69 between. Late: reachable only after the answer to `sb.ordinary_dividends` (step 141), which its gate does not read.
- form sb re-entered at step 143 by `sb.unsupported` (order 10), left after step 141, 1 between. Late: left for `f1040.line3a` (order 10), which sorts earlier and was reachable only after the answer to `sb.ordinary_dividends` (step 141), which its gate does not read.
- form s1a re-entered at step 160 by `s1a.overtime` (order 10), left after step 107, 52 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 159), which its gate does not read.
- form div re-entered at step 163 by `div.box2c` (order 15), left after step 69, 93 between. Late: reachable only after the answer to `sd.distributions` (step 146), which its gate does not read.
- form person re-entered at step 176 by `person[taxpayer].sav_trad` (order 22), left after step 127, 48 between. Sorting: it was reachable (since step 2), and `sa.elect_itemize` was asked instead (the bank puts order 10 first).
- form qbi re-entered at step 177 by `qbi.unsupported` (order 10), left after step 172, 4 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 176), which its gate does not read.
- form household re-entered at step 179 by `household.credit_disallowed` (order 20), left after step 43, 135 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 176), which its gate does not read.
- form div re-entered at step 182 by `div.box12` (order 30), left after step 171, 10 between. Late: left for `qbi.dividends` (order 10), which sorts earlier and was reachable only after the answer to `div.box2d` (step 171), which its gate does not read.
- form f1040 re-entered at step 183 by `f1040.tax_exempt_interest` (order 30), left after step 142, 40 between. Sorting: it was reachable (since step 81), and `sb.unsupported` was asked instead (the bank puts order 10 first).
- form f1095a re-entered at step 184 by `f1095a[mkt_a].uniform` (order 2), left after step 80, 103 between. Late: reachable only after the answer to `f1040.tax_exempt_interest` (step 183), which its gate does not read.
- `sa.line11` (order 10), step 137: child of `sa.gifts` (step 133), 2 other questions between. Late: reachable only after the answer to `sa.charity_limited` (step 134), which its gate does not read.
- `sb.ordinary_dividends` (order 10), step 141: child of `div.any` (step 69), 71 other questions between. Sorting: it was reachable (since step 70), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `sd.distributions` (order 10), step 146: child of `div.any` (step 69), 75 other questions between. Sorting: it was reachable (since step 70), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `div.box13` (order 15), step 164: child of `div.any` (step 69), 92 other questions between. Late: reachable only after the answer to `div.box2c` (step 163), which its gate does not read.
- `div.box10` (order 15), step 165: child of `div.any` (step 69), 92 other questions between. Late: reachable only after the answer to `div.box13` (step 164), which its gate does not read.
- `div.box3` (order 15), step 168: child of `div.any` (step 69), 94 other questions between. Late: reachable only after the answer to `div.box13` (step 164), which its gate does not read.
- `div.box9` (order 15), step 169: child of `div.any` (step 69), 94 other questions between. Late: reachable only after the answer to `div.box13` (step 164), which its gate does not read.
- `household.credit_disallowed` (order 20), step 179: child of `sa.excluded_income` (step 129), 49 other questions between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 176), which its gate does not read.
- `div.box12` (order 30), step 182: child of `div.any` (step 69), 106 other questions between. Late: reachable only after the answer to `f1095a[mkt_a].void` (step 80), which its gate does not read.

**generated.13**: 3 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×1

**generated.14**: 53 questions, refused; order re-entries 2, form re-entries 3 sorting and 1 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 2:dependent×10 · 2:household×1 · 2:person×1 · 2:household×1 · 2:s3×1 · 3:dependent×2 · 2:dependent×3 · 5:w2×1 · 3:w2×2 · 8:interest×1 · 9:f8889×13 · 10:div×1 · 10:f1040×3 · 10:f4952×6

- order 2 re-entered at step 24 by `dependent[dep_a].gross_income` (order 2), left after step 21, 2 between. Late: reachable only after the answer to `dependent[dep_a].qr_all_year` (step 23), which its gate does not read.
- order 3 re-entered at step 28 by `person[taxpayer].w2[emp_a].box1` (order 3), left after step 23, 4 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 27), its parent or roster.
- form person re-entered at step 19 by `person[taxpayer].under16` (order 2), left after step 1, 17 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 20 by `household.community_property` (order 2), left after step 18, 1 between. Late: reachable only after the answer to `person[taxpayer].under16` (step 19), which its gate does not read.
- form dependent re-entered at step 22 by `dependent[dep_a].lawful` (order 3), left after step 17, 4 between. Sorting: it was reachable (since step 18), and `household.qss_eligible` was asked instead (the bank puts order 2 first).
- form f1040 re-entered at step 45 by `f1040.line25b` (order 10), left after step 2, 42 between. Sorting: it was reachable (since step 1), and `scope.other_line16` was asked instead (the bank puts order 0 first).

**generated.15**: 81 questions, refused; order re-entries 4, form re-entries 3 sorting and 2 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 2:dependent×33 · 2:household×2 · 2:person×1 · 2:household×1 · 2:s3×1 · 3:dependent×1 · 2:dependent×3 · 5:w2×1 · 3:w2×2 · 8:interest×1 · 9:f8889×13 · 10:div×1 · 10:f1040×3 · 10:f4952×4 · 10:f8863×1 · 10:f8959×1 · 10:f8962×3 · 2:f1095a×1 · 10:ftc×1

- order 2 re-entered at step 47 by `dependent[dep_a].gross_income` (order 2), left after step 45, 1 between. Late: reachable only after the answer to `dependent[dep_a].qr_all_year` (step 46), which its gate does not read.
- order 3 re-entered at step 51 by `person[taxpayer].w2[emp_a].box1` (order 3), left after step 46, 4 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 50), its parent or roster.
- order 2 re-entered at step 80 by `f1095a[mkt_a].void` (order 2), left after step 49, 30 between. Late: reachable only after the answer to `f8962.premium_adjust` (step 79), which its gate does not read.
- order 10 re-entered at step 81 by `ftc.taxes` (order 10), left after step 79, 1 between. Late: left for `f1095a[mkt_a].void` (order 2), which sorts earlier and was reachable only after the answer to `f8962.premium_adjust` (step 79), which its gate does not read.
- form person re-entered at step 43 by `person[taxpayer].under16` (order 2), left after step 1, 41 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 44 by `household.community_property` (order 2), left after step 42, 1 between. Late: reachable only after the answer to `person[taxpayer].under16` (step 43), which its gate does not read.
- form dependent re-entered at step 46 by `dependent[dep_a].qr_all_year` (order 3), left after step 40, 5 between. Sorting: it was reachable (since step 17), and `household.married` was asked instead (the bank puts order 2 first).
- form f1040 re-entered at step 68 by `f1040.line25b` (order 10), left after step 2, 65 between. Sorting: it was reachable (since step 1), and `scope.other_line16` was asked instead (the bank puts order 0 first).
- form f1095a re-entered at step 80 by `f1095a[mkt_a].void` (order 2), left after step 6, 73 between. Late: reachable only after the answer to `f8962.premium_adjust` (step 79), which its gate does not read.

**generated.16**: 2 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1

**generated.17**: 2 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1

**generated.18**: 83 questions, refused; order re-entries 0, form re-entries 1 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×2 · 2:dependent×37 · 2:household×1 · 2:person×2 · 2:s3×1 · 5:w2×2 · 3:w2×2 · 8:interest×1 · 9:f8889×30

- form person re-entered at step 46 by `person[spouse].under16` (order 2), left after step 1, 44 between. Sorting: it was reachable (since step 2), and `scope.other_line16` was asked instead (the bank puts order 0 first).

**generated.19**: 117 questions, refused; order re-entries 14, form re-entries 4 sorting and 10 late, delayed children 0 sorting and 1 late.

0:person×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×2 · 2:dependent×1 · 2:household×1 · 2:person×2 · 2:s3×1 · 5:w2×1 · 3:w2×2 · 5:w2×1 · 3:w2×2 · 8:interest×1 · 9:f8889×14 · 10:div×1 · 10:f1040×3 · 10:f4952×6 · 10:f8863×1 · 10:f8959×1 · 10:f8962×4 · 2:f1095a×1 · 10:f8962×1 · 10:ftc×1 · 10:interest×2 · 10:person×3 · 3:w2×1 · 4:w2×2 · 10:person×4 · 3:w2×1 · 4:w2×2 · 10:refund×1 · 10:s1×2 · 10:oi8z×1 · 10:s1×8 · 10:s1a×1 · 10:s2×2 · 10:person×2 · 10:s3×9 · 10:sa×1 · 10:person×2 · 10:sa×4 · 5:sa×1 · 10:sa×1 · 5:gift×1 · 10:gift×4 · 10:sa×5 · 10:sb×2 · 10:sd×2 · 1:sales×1

- order 5 re-entered at step 16 by `$w2@person[taxpayer]` (order 5), left after step 13, 2 between. Sorting: left for `person[spouse].w2[emp_a].box1` (order 3), a child of the question before it, which the bank places in another order number.
- order 3 re-entered at step 17 by `person[taxpayer].w2[emp_a].box1` (order 3), left after step 15, 1 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 16), its parent or roster.
- order 2 re-entered at step 50 by `f1095a[mkt_a].void` (order 2), left after step 12, 37 between. Late: reachable only after the answer to `f8962.premium_adjust` (step 49), which its gate does not read.
- order 10 re-entered at step 51 by `f8962.fpl_table` (order 10), left after step 49, 1 between. Late: reachable only after the answer to `f1095a[mkt_a].void` (step 50), which its gate does not read.
- order 3 re-entered at step 58 by `person[spouse].w2[emp_a].box4` (order 3), left after step 18, 39 between. Late: reachable only after the answer to `person[spouse].rrta` (step 57), which its gate does not read.
- order 10 re-entered at step 61 by `person[taxpayer].age65` (order 10), left after step 57, 3 between. Late: left for `person[spouse].w2[emp_a].box4` (order 3), which sorts earlier and was reachable only after the answer to `person[spouse].rrta` (step 57), which its gate does not read.
- order 3 re-entered at step 65 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 58, 6 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 64), which its gate does not read.
- order 4 re-entered at step 66 by `person[taxpayer].w2[emp_a].box5` (order 4), left after step 60, 5 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 64), which its gate does not read.
- order 10 re-entered at step 68 by `refund.received` (order 10), left after step 64, 3 between. Late: left for `person[taxpayer].w2[emp_a].box4` (order 3), which sorts earlier and was reachable only after the answer to `person[taxpayer].rrta` (step 64), which its gate does not read.
- order 5 re-entered at step 101 by `sa.gifts` (order 5), left after step 16, 84 between. Late: reachable only after the answer to `sa.unsupported` (step 100), which its gate does not read.
- order 10 re-entered at step 102 by `sa.charity_limited` (order 10), left after step 100, 1 between. Late: reachable only after the answer to `sa.gifts` (step 101), its parent or roster.
- order 5 re-entered at step 103 by `$gift` (order 5), left after step 101, 1 between. Late: reachable only after the answer to `sa.charity_limited` (step 102), which its gate does not read.
- order 10 re-entered at step 104 by `gift[item_a].special` (order 10), left after step 102, 1 between. Late: reachable only after the answer to `$gift` (step 103), its parent or roster.
- order 1 re-entered at step 117 by `$sales` (order 1), left after step 7, 109 between. Late: reachable only after the answer to `sd.other_forms` (step 116), which its gate does not read.
- form person re-entered at step 10 by `person[spouse].under16` (order 2), left after step 1, 8 between. Sorting: it was reachable (since step 2), and `scope.other_line16` was asked instead (the bank puts order 0 first).
- form f1095a re-entered at step 50 by `f1095a[mkt_a].void` (order 2), left after step 5, 44 between. Late: reachable only after the answer to `f8962.premium_adjust` (step 49), which its gate does not read.
- form f8962 re-entered at step 51 by `f8962.fpl_table` (order 10), left after step 49, 1 between. Late: reachable only after the answer to `f1095a[mkt_a].void` (step 50), which its gate does not read.
- form interest re-entered at step 53 by `interest[bank_a].amount` (order 10), left after step 19, 33 between. Sorting: it was reachable (since step 20), and `$f8889@person[spouse]` was asked instead (the bank puts order 9 seq 1 first).
- form person re-entered at step 55 by `person[spouse].age65` (order 10), left after step 11, 43 between. Sorting: it was reachable (since step 2), and `s3.adoption_any` was asked instead (the bank puts order 2 first).
- form w2 re-entered at step 58 by `person[spouse].w2[emp_a].box4` (order 3), left after step 18, 39 between. Late: reachable only after the answer to `person[spouse].rrta` (step 57), which its gate does not read.
- form person re-entered at step 61 by `person[taxpayer].age65` (order 10), left after step 57, 3 between. Late: left for `person[spouse].w2[emp_a].box4` (order 3), which sorts earlier and was reachable only after the answer to `person[spouse].rrta` (step 57), which its gate does not read.
- form w2 re-entered at step 65 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 60, 4 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 64), which its gate does not read.
- form s1 re-entered at step 72 by `s1.cod_any` (order 10), left after step 70, 1 between. Late: left for `$oi8z` (order 10), which sorts earlier and was reachable only after the answer to `s1.line8_other` (step 70), which its gate does not read.
- form person re-entered at step 83 by `person[spouse].x_other` (order 10), left after step 64, 18 between. Late: reachable only after the answer to `s2.other` (step 82), which its gate does not read.
- form s3 re-entered at step 85 by `s3.credit_bond` (order 10), left after step 12, 72 between. Sorting: it was reachable (since step 13), and `$w2@person[spouse]` was asked instead (the bank puts order 5 first).
- form person re-entered at step 95 by `person[spouse].blind` (order 10), left after step 84, 10 between. Late: reachable only after the answer to `sa.dependent` (step 94), which its gate does not read.
- form sa re-entered at step 97 by `sa.elect_itemize` (order 10), left after step 94, 2 between. Late: left for `person[spouse].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 94), which its gate does not read.
- form sa re-entered at step 108 by `sa.line1` (order 10), left after step 102, 5 between. Late: left for `$gift` (order 5), which sorts earlier and was reachable only after the answer to `sa.charity_limited` (step 102), which its gate does not read.
- `sa.line11` (order 10), step 109: child of `sa.gifts` (step 101), 6 other questions between. Late: reachable only after the answer to `sa.charity_limited` (step 102), which its gate does not read.

**generated.20**: 162 questions, refused; order re-entries 12, form re-entries 3 sorting and 11 late, delayed children 1 sorting and 0 late.

0:person×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×2 · 2:dependent×13 · 2:household×1 · 2:person×2 · 2:s3×1 · 5:w2×1 · 3:w2×4 · 5:w2×1 · 3:w2×4 · 8:interest×1 · 9:f8889×36 · 10:div×1 · 10:f1040×3 · 10:f4952×6 · 10:f8863×1 · 10:f8959×1 · 10:ftc×5 · 10:person×3 · 3:w2×2 · 4:w2×8 · 10:person×3 · 3:w2×2 · 4:w2×8 · 10:refund×1 · 10:s1×2 · 10:oi8z×1 · 10:s1×8 · 10:s1a×1 · 10:s2×2 · 10:person×2 · 10:s3×9 · 10:sa×1 · 2:person×2 · 3:person×1 · 10:person×2 · 10:sa×3 · 10:s3×1 · 10:sa×1 · 5:sa×1 · 10:sa×4 · 10:sb×1 · 10:f1040×1 · 10:sb×4

- order 5 re-entered at step 30 by `$w2@person[taxpayer]` (order 5), left after step 25, 4 between. Sorting: left for `person[spouse].w2[emp_a].box1` (order 3), a child of the question before it, which the bank places in another order number.
- order 3 re-entered at step 31 by `person[taxpayer].w2[emp_a].box1` (order 3), left after step 29, 1 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 30), its parent or roster.
- order 3 re-entered at step 92 by `person[spouse].w2[emp_a].box4` (order 3), left after step 34, 57 between. Late: reachable only after the answer to `person[spouse].rrta` (step 91), which its gate does not read.
- order 10 re-entered at step 102 by `person[taxpayer].age65` (order 10), left after step 91, 10 between. Late: left for `person[spouse].w2[emp_a].box4` (order 3), which sorts earlier and was reachable only after the answer to `person[spouse].rrta` (step 91), which its gate does not read.
- order 3 re-entered at step 105 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 93, 11 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 104), which its gate does not read.
- order 4 re-entered at step 107 by `person[taxpayer].w2[emp_a].box3` (order 4), left after step 101, 5 between. Late: reachable only after the answer to `person[taxpayer].w2[emp_b].box4` (step 106), which its gate does not read.
- order 10 re-entered at step 115 by `refund.received` (order 10), left after step 104, 10 between. Late: left for `person[taxpayer].w2[emp_a].box4` (order 3), which sorts earlier and was reachable only after the answer to `person[taxpayer].rrta` (step 104), which its gate does not read.
- order 2 re-entered at step 142 by `person[spouse].tin` (order 2), left after step 24, 117 between. Late: reachable only after the answer to `sa.dependent` (step 141), which its gate does not read.
- order 3 re-entered at step 144 by `person[taxpayer].itin_applied` (order 3), left after step 106, 37 between. Late: reachable only after the answer to `person[taxpayer].tin` (step 143), which its gate does not read.
- order 10 re-entered at step 145 by `person[spouse].blind` (order 10), left after step 141, 3 between. Late: left for `person[spouse].tin` (order 2), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 141), which its gate does not read.
- order 5 re-entered at step 152 by `sa.gifts` (order 5), left after step 30, 121 between. Late: reachable only after the answer to `sa.unsupported` (step 151), which its gate does not read.
- order 10 re-entered at step 153 by `sa.line1` (order 10), left after step 151, 1 between. Late: reachable only after the answer to `sa.gifts` (step 152), which its gate does not read.
- form person re-entered at step 22 by `person[spouse].under16` (order 2), left after step 1, 20 between. Sorting: it was reachable (since step 2), and `scope.other_line16` was asked instead (the bank puts order 0 first).
- form person re-entered at step 89 by `person[spouse].age65` (order 10), left after step 23, 65 between. Sorting: it was reachable (since step 2), and `s3.adoption_any` was asked instead (the bank puts order 2 first).
- form w2 re-entered at step 92 by `person[spouse].w2[emp_a].box4` (order 3), left after step 34, 57 between. Late: reachable only after the answer to `person[spouse].rrta` (step 91), which its gate does not read.
- form person re-entered at step 102 by `person[taxpayer].age65` (order 10), left after step 91, 10 between. Late: left for `person[spouse].w2[emp_a].box4` (order 3), which sorts earlier and was reachable only after the answer to `person[spouse].rrta` (step 91), which its gate does not read.
- form w2 re-entered at step 105 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 101, 3 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 104), which its gate does not read.
- form s1 re-entered at step 119 by `s1.cod_any` (order 10), left after step 117, 1 between. Late: left for `$oi8z` (order 10), which sorts earlier and was reachable only after the answer to `s1.line8_other` (step 117), which its gate does not read.
- form person re-entered at step 130 by `person[spouse].x_other` (order 10), left after step 104, 25 between. Late: reachable only after the answer to `s2.other` (step 129), which its gate does not read.
- form s3 re-entered at step 132 by `s3.credit_bond` (order 10), left after step 24, 107 between. Sorting: it was reachable (since step 25), and `$w2@person[spouse]` was asked instead (the bank puts order 5 first).
- form person re-entered at step 142 by `person[spouse].tin` (order 2), left after step 131, 10 between. Late: reachable only after the answer to `sa.dependent` (step 141), which its gate does not read.
- form sa re-entered at step 147 by `sa.elect_itemize` (order 10), left after step 141, 5 between. Late: left for `person[spouse].tin` (order 2), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 141), which its gate does not read.
- form s3 re-entered at step 150 by `s3.mcc` (order 10), left after step 140, 9 between. Late: reachable only after the answer to `sa.line8a` (step 149), which its gate does not read.
- form sa re-entered at step 151 by `sa.unsupported` (order 10), left after step 149, 1 between. Late: left for `s3.mcc` (order 10), which sorts earlier and was reachable only after the answer to `sa.line8a` (step 149), which its gate does not read.
- form f1040 re-entered at step 158 by `f1040.line3a` (order 10), left after step 75, 82 between. Late: reachable only after the answer to `sb.ordinary_dividends` (step 157), which its gate does not read.
- form sb re-entered at step 159 by `sb.unsupported` (order 10), left after step 157, 1 between. Late: left for `f1040.line3a` (order 10), which sorts earlier and was reachable only after the answer to `sb.ordinary_dividends` (step 157), which its gate does not read.
- `sb.ordinary_dividends` (order 10), step 157: child of `div.any` (step 72), 84 other questions between. Sorting: it was reachable (since step 73), and `f1040.line25b` was asked instead (within order 10, sorted by id).

**generated.21**: 34 questions, refused; order re-entries 3, form re-entries 2 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×2 · 2:dependent×10 · 2:household×1 · 2:person×2 · 2:s3×1 · 3:dependent×1 · 2:dependent×3 · 3:dependent×1 · 5:w2×2 · 3:w2×2 · 8:interest×1 · 9:f8889×3

- order 2 re-entered at step 23 by `dependent[dep_a].gross_income` (order 2), left after step 21, 1 between. Late: reachable only after the answer to `dependent[dep_a].qr_all_year` (step 22), which its gate does not read.
- order 3 re-entered at step 26 by `dependent[dep_a].spouse_relative` (order 3), left after step 22, 3 between. Late: left for `dependent[dep_a].gross_income` (order 2), which sorts earlier and was reachable only after the answer to `dependent[dep_a].qr_all_year` (step 22), which its gate does not read.
- order 3 re-entered at step 29 by `person[taxpayer].w2[emp_a].box1` (order 3), left after step 26, 2 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 28), its parent or roster.
- form person re-entered at step 19 by `person[spouse].under16` (order 2), left after step 1, 17 between. Sorting: it was reachable (since step 2), and `scope.other_line16` was asked instead (the bank puts order 0 first).
- form dependent re-entered at step 22 by `dependent[dep_a].qr_all_year` (order 3), left after step 17, 4 between. Sorting: it was reachable (since step 18), and `household.married` was asked instead (the bank puts order 2 first).

**generated.22**: 86 questions, refused; order re-entries 2, form re-entries 2 sorting and 3 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 2:dependent×24 · 2:household×2 · 2:person×1 · 2:household×1 · 2:s3×1 · 5:w2×1 · 3:w2×4 · 8:interest×1 · 9:f8889×13 · 10:div×1 · 10:f1040×3 · 10:f4952×6 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:person×3 · 3:w2×2 · 4:w2×8 · 10:refund×1 · 10:s1×2 · 10:oi8z×2

- order 3 re-entered at step 72 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 41, 30 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 71), which its gate does not read.
- order 10 re-entered at step 82 by `refund.received` (order 10), left after step 71, 10 between. Late: left for `person[taxpayer].w2[emp_a].box4` (order 3), which sorts earlier and was reachable only after the answer to `person[taxpayer].rrta` (step 71), which its gate does not read.
- form person re-entered at step 34 by `person[taxpayer].under16` (order 2), left after step 1, 32 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 35 by `household.community_property` (order 2), left after step 33, 1 between. Late: reachable only after the answer to `person[taxpayer].under16` (step 34), which its gate does not read.
- form f1040 re-entered at step 57 by `f1040.line25b` (order 10), left after step 2, 54 between. Sorting: it was reachable (since step 1), and `scope.other_line16` was asked instead (the bank puts order 0 first).
- form person re-entered at step 69 by `person[taxpayer].age65` (order 10), left after step 34, 34 between. Late: left for `household.community_property` (order 2), which sorts earlier and was reachable only after the answer to `person[taxpayer].under16` (step 34), which its gate does not read.
- form w2 re-entered at step 72 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 41, 30 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 71), which its gate does not read.

**generated.23**: 89 questions, refused; order re-entries 8, form re-entries 3 sorting and 9 late, delayed children 2 sorting and 1 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 2:dependent×1 · 2:household×1 · 2:person×1 · 2:household×1 · 2:s3×1 · 5:w2×1 · 3:w2×2 · 8:interest×1 · 9:f8889×13 · 10:div×1 · 10:f1040×3 · 10:f4952×2 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:person×2 · 2:person×1 · 10:person×2 · 3:w2×1 · 4:w2×2 · 10:refund×1 · 10:s1×2 · 10:oi8z×1 · 10:s1×8 · 10:s1a×1 · 10:s2×2 · 10:person×1 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×4 · 5:sa×1 · 10:sa×1 · 5:gift×1 · 10:sa×5 · 10:sb×1 · 10:sd×2 · 10:sb×1

- order 2 re-entered at step 41 by `person[taxpayer].work_ssn` (order 2), left after step 12, 28 between. Late: reachable only after the answer to `person[taxpayer].died_before_65` (step 40), which its gate does not read.
- order 10 re-entered at step 42 by `person[taxpayer].educator_expenses` (order 10), left after step 40, 1 between. Late: left for `person[taxpayer].work_ssn` (order 2), which sorts earlier and was reachable only after the answer to `person[taxpayer].died_before_65` (step 40), which its gate does not read.
- order 3 re-entered at step 44 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 15, 28 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 43), which its gate does not read.
- order 10 re-entered at step 47 by `refund.received` (order 10), left after step 43, 3 between. Late: left for `person[taxpayer].w2[emp_a].box4` (order 3), which sorts earlier and was reachable only after the answer to `person[taxpayer].rrta` (step 43), which its gate does not read.
- order 5 re-entered at step 78 by `sa.gifts` (order 5), left after step 13, 64 between. Late: reachable only after the answer to `sa.unsupported` (step 77), which its gate does not read.
- order 10 re-entered at step 79 by `sa.charity_limited` (order 10), left after step 77, 1 between. Late: reachable only after the answer to `sa.gifts` (step 78), its parent or roster.
- order 5 re-entered at step 80 by `$gift` (order 5), left after step 78, 1 between. Late: reachable only after the answer to `sa.charity_limited` (step 79), which its gate does not read.
- order 10 re-entered at step 81 by `sa.line1` (order 10), left after step 79, 1 between. Late: left for `$gift` (order 5), which sorts earlier and was reachable only after the answer to `sa.charity_limited` (step 79), which its gate does not read.
- form person re-entered at step 10 by `person[taxpayer].under16` (order 2), left after step 1, 8 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 11 by `household.community_property` (order 2), left after step 9, 1 between. Late: reachable only after the answer to `person[taxpayer].under16` (step 10), which its gate does not read.
- form f1040 re-entered at step 31 by `f1040.line25b` (order 10), left after step 2, 28 between. Sorting: it was reachable (since step 1), and `scope.other_line16` was asked instead (the bank puts order 0 first).
- form person re-entered at step 39 by `person[taxpayer].age65` (order 10), left after step 10, 28 between. Late: left for `household.community_property` (order 2), which sorts earlier and was reachable only after the answer to `person[taxpayer].under16` (step 10), which its gate does not read.
- form w2 re-entered at step 44 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 15, 28 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 43), which its gate does not read.
- form s1 re-entered at step 51 by `s1.cod_any` (order 10), left after step 49, 1 between. Late: left for `$oi8z` (order 10), which sorts earlier and was reachable only after the answer to `s1.line8_other` (step 49), which its gate does not read.
- form person re-entered at step 62 by `person[taxpayer].x_other` (order 10), left after step 43, 18 between. Late: reachable only after the answer to `s2.other` (step 61), which its gate does not read.
- form s3 re-entered at step 63 by `s3.credit_bond` (order 10), left after step 12, 50 between. Sorting: it was reachable (since step 13), and `$w2@person[taxpayer]` was asked instead (the bank puts order 5 first).
- form person re-entered at step 73 by `person[taxpayer].blind` (order 10), left after step 62, 10 between. Late: reachable only after the answer to `sa.dependent` (step 72), which its gate does not read.
- form sa re-entered at step 74 by `sa.elect_itemize` (order 10), left after step 72, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 72), which its gate does not read.
- form sa re-entered at step 81 by `sa.line1` (order 10), left after step 79, 1 between. Late: left for `$gift` (order 5), which sorts earlier and was reachable only after the answer to `sa.charity_limited` (step 79), which its gate does not read.
- form sb re-entered at step 89 by `sb.unsupported` (order 10), left after step 86, 2 between. Late: reachable only after the answer to `sd.distributions` (step 88), which its gate does not read.
- `sa.line11` (order 10), step 82: child of `sa.gifts` (step 78), 2 other questions between. Late: reachable only after the answer to `sa.charity_limited` (step 79), which its gate does not read.
- `sb.ordinary_dividends` (order 10), step 86: child of `div.any` (step 30), 55 other questions between. Sorting: it was reachable (since step 31), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `sd.distributions` (order 10), step 88: child of `div.any` (step 30), 56 other questions between. Sorting: it was reachable (since step 31), and `f1040.line25b` was asked instead (within order 10, sorted by id).

**generated.24**: 2 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1

**generated.25**: 87 questions, refused; order re-entries 4, form re-entries 5 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×2 · 2:dependent×34 · 2:household×1 · 2:person×1 · 2:retirement×3 · 2:person×1 · 2:s3×1 · 5:w2×1 · 3:w2×2 · 5:w2×1 · 3:w2×2 · 8:interest×1 · 9:f8889×14 · 10:div×1 · 10:f1040×3 · 10:f4952×6 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:interest×2 · 10:person×1 · 2:person×1 · 10:person×1

- order 5 re-entered at step 52 by `$w2@person[taxpayer]` (order 5), left after step 49, 2 between. Sorting: left for `person[spouse].w2[emp_a].box1` (order 3), a child of the question before it, which the bank places in another order number.
- order 3 re-entered at step 53 by `person[taxpayer].w2[emp_a].box1` (order 3), left after step 51, 1 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 52), its parent or roster.
- order 2 re-entered at step 86 by `person[spouse].work_ssn` (order 2), left after step 48, 37 between. Late: reachable only after the answer to `person[spouse].age65` (step 85), which its gate does not read.
- order 10 re-entered at step 87 by `person[spouse].died_before_65` (order 10), left after step 85, 1 between. Late: reachable only after the answer to `person[spouse].work_ssn` (step 86), which its gate does not read.
- form person re-entered at step 43 by `person[spouse].under16` (order 2), left after step 1, 41 between. Sorting: it was reachable (since step 2), and `scope.other_line16` was asked instead (the bank puts order 0 first).
- form retirement re-entered at step 44 by `person[taxpayer].retirement[r1].account` (order 2), left after step 7, 36 between. Sorting: it was reachable (since step 8), and `$dependent` was asked instead (within order 2, sorted by id).
- form person re-entered at step 47 by `person[taxpayer].under16` (order 2), left after step 43, 3 between. Sorting: it was reachable (since step 2), and `person[taxpayer].retirement[r1].account` was asked instead (within order 2, sorted by id).
- form interest re-entered at step 83 by `interest[bank_a].amount` (order 10), left after step 55, 27 between. Sorting: it was reachable (since step 56), and `$f8889@person[spouse]` was asked instead (the bank puts order 9 seq 1 first).
- form person re-entered at step 85 by `person[spouse].age65` (order 10), left after step 47, 37 between. Sorting: it was reachable (since step 2), and `s3.adoption_any` was asked instead (the bank puts order 2 first).

**generated.26**: 102 questions, refused; order re-entries 4, form re-entries 3 sorting and 3 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×2 · 2:dependent×12 · 2:household×1 · 2:person×2 · 2:s3×1 · 5:w2×2 · 3:w2×4 · 8:interest×1 · 9:f8889×14 · 10:div×1 · 10:f1040×3 · 10:f4952×6 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:person×1 · 2:person×1 · 10:person×6 · 3:w2×2 · 4:w2×8 · 10:refund×1 · 10:s1×2 · 10:oi8z×1 · 10:s1×8 · 10:s1a×1 · 10:s2×2 · 10:person×2 · 10:s3×9 · 10:sa×1

- order 2 re-entered at step 59 by `person[spouse].work_ssn` (order 2), left after step 23, 35 between. Late: reachable only after the answer to `person[spouse].age65` (step 58), which its gate does not read.
- order 10 re-entered at step 60 by `person[spouse].died_before_65` (order 10), left after step 58, 1 between. Late: reachable only after the answer to `person[spouse].work_ssn` (step 59), which its gate does not read.
- order 3 re-entered at step 66 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 29, 36 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 65), which its gate does not read.
- order 10 re-entered at step 76 by `refund.received` (order 10), left after step 65, 10 between. Late: left for `person[taxpayer].w2[emp_a].box4` (order 3), which sorts earlier and was reachable only after the answer to `person[taxpayer].rrta` (step 65), which its gate does not read.
- form person re-entered at step 21 by `person[spouse].under16` (order 2), left after step 1, 19 between. Sorting: it was reachable (since step 2), and `scope.other_line16` was asked instead (the bank puts order 0 first).
- form person re-entered at step 58 by `person[spouse].age65` (order 10), left after step 22, 35 between. Sorting: it was reachable (since step 2), and `s3.adoption_any` was asked instead (the bank puts order 2 first).
- form w2 re-entered at step 66 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 29, 36 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 65), which its gate does not read.
- form s1 re-entered at step 80 by `s1.cod_any` (order 10), left after step 78, 1 between. Late: left for `$oi8z` (order 10), which sorts earlier and was reachable only after the answer to `s1.line8_other` (step 78), which its gate does not read.
- form person re-entered at step 91 by `person[spouse].x_other` (order 10), left after step 65, 25 between. Late: reachable only after the answer to `s2.other` (step 90), which its gate does not read.
- form s3 re-entered at step 93 by `s3.credit_bond` (order 10), left after step 23, 69 between. Sorting: it was reachable (since step 24), and `$w2@person[spouse]` was asked instead (the bank puts order 5 first).

**generated.27**: 40 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 2:dependent×30 · 2:household×3

**generated.28**: 10 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×2 · 2:dependent×3

**generated.29**: 10 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 2:dependent×3

**generated.30**: 108 questions, refused; order re-entries 10, form re-entries 5 sorting and 11 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 2:dependent×1 · 2:household×1 · 2:retirement×3 · 2:person×1 · 2:household×1 · 2:s3×1 · 3:retirement×1 · 2:retirement×2 · 5:w2×1 · 3:w2×4 · 8:interest×1 · 9:f8889×12 · 2:household×1 · 9:f8889×7 · 10:div×1 · 10:f1040×3 · 10:f4952×6 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:person×3 · 3:w2×2 · 4:w2×8 · 10:refund×1 · 10:s1×2 · 10:oi8z×1 · 10:s1×8 · 10:s1a×1 · 10:s2×2 · 10:person×1 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×3 · 10:s3×1 · 10:sa×1 · 5:sa×1 · 10:sa×1 · 5:gift×1 · 10:gift×3

- order 2 re-entered at step 17 by `person[taxpayer].retirement[r1].box1` (order 2), left after step 15, 1 between. Late: reachable only after the answer to `person[taxpayer].retirement[r1].code_screen` (step 16), which its gate does not read.
- order 3 re-entered at step 20 by `person[taxpayer].w2[emp_a].box1` (order 3), left after step 16, 3 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 19), its parent or roster.
- order 2 re-entered at step 37 by `household.married` (order 2), left after step 18, 18 between. Late: reachable only after the answer to `person[taxpayer].f8889[hsa].dec_coverage` (step 36), which its gate does not read.
- order 9 re-entered at step 38 by `person[taxpayer].f8889[hsa].last_month` (order 9 seq 16), left after step 36, 1 between. Late: reachable only after the answer to `household.married` (step 37), which its gate does not read.
- order 3 re-entered at step 61 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 23, 37 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 60), which its gate does not read.
- order 10 re-entered at step 71 by `refund.received` (order 10), left after step 60, 10 between. Late: left for `person[taxpayer].w2[emp_a].box4` (order 3), which sorts earlier and was reachable only after the answer to `person[taxpayer].rrta` (step 60), which its gate does not read.
- order 5 re-entered at step 103 by `sa.gifts` (order 5), left after step 19, 83 between. Late: reachable only after the answer to `sa.unsupported` (step 102), which its gate does not read.
- order 10 re-entered at step 104 by `sa.charity_limited` (order 10), left after step 102, 1 between. Late: reachable only after the answer to `sa.gifts` (step 103), its parent or roster.
- order 5 re-entered at step 105 by `$gift` (order 5), left after step 103, 1 between. Late: reachable only after the answer to `sa.charity_limited` (step 104), which its gate does not read.
- order 10 re-entered at step 106 by `gift[item_a].special` (order 10), left after step 104, 1 between. Late: reachable only after the answer to `$gift` (step 105), its parent or roster.
- form retirement re-entered at step 10 by `person[taxpayer].retirement[r1].account` (order 2), left after step 7, 2 between. Sorting: it was reachable (since step 8), and `$dependent` was asked instead (within order 2, sorted by id).
- form person re-entered at step 13 by `person[taxpayer].under16` (order 2), left after step 1, 11 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 14 by `household.community_property` (order 2), left after step 9, 4 between. Late: reachable only after the answer to `person[taxpayer].under16` (step 13), which its gate does not read.
- form retirement re-entered at step 16 by `person[taxpayer].retirement[r1].code_screen` (order 3), left after step 12, 3 between. Sorting: it was reachable (since step 13), and `person[taxpayer].under16` was asked instead (the bank puts order 2 first).
- form household re-entered at step 37 by `household.married` (order 2), left after step 14, 22 between. Late: reachable only after the answer to `person[taxpayer].f8889[hsa].dec_coverage` (step 36), which its gate does not read.
- form f8889 re-entered at step 38 by `person[taxpayer].f8889[hsa].last_month` (order 9 seq 16), left after step 36, 1 between. Late: reachable only after the answer to `household.married` (step 37), which its gate does not read.
- form f1040 re-entered at step 46 by `f1040.line25b` (order 10), left after step 2, 43 between. Sorting: it was reachable (since step 1), and `scope.other_line16` was asked instead (the bank puts order 0 first).
- form person re-entered at step 58 by `person[taxpayer].age65` (order 10), left after step 13, 44 between. Late: left for `household.community_property` (order 2), which sorts earlier and was reachable only after the answer to `person[taxpayer].under16` (step 13), which its gate does not read.
- form w2 re-entered at step 61 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 23, 37 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 60), which its gate does not read.
- form s1 re-entered at step 75 by `s1.cod_any` (order 10), left after step 73, 1 between. Late: left for `$oi8z` (order 10), which sorts earlier and was reachable only after the answer to `s1.line8_other` (step 73), which its gate does not read.
- form person re-entered at step 86 by `person[taxpayer].x_other` (order 10), left after step 60, 25 between. Late: reachable only after the answer to `s2.other` (step 85), which its gate does not read.
- form s3 re-entered at step 87 by `s3.credit_bond` (order 10), left after step 15, 71 between. Sorting: it was reachable (since step 16), and `person[taxpayer].retirement[r1].code_screen` was asked instead (the bank puts order 3 first).
- form person re-entered at step 97 by `person[taxpayer].blind` (order 10), left after step 86, 10 between. Late: reachable only after the answer to `sa.dependent` (step 96), which its gate does not read.
- form sa re-entered at step 98 by `sa.elect_itemize` (order 10), left after step 96, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 96), which its gate does not read.
- form s3 re-entered at step 101 by `s3.mcc` (order 10), left after step 95, 5 between. Late: reachable only after the answer to `sa.line8a` (step 100), which its gate does not read.
- form sa re-entered at step 102 by `sa.unsupported` (order 10), left after step 100, 1 between. Late: left for `s3.mcc` (order 10), which sorts earlier and was reachable only after the answer to `sa.line8a` (step 100), which its gate does not read.

**generated.31**: 164 questions, refused; order re-entries 6, form re-entries 7 sorting and 10 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 2:dependent×1 · 2:household×2 · 2:person×1 · 2:household×1 · 2:s3×1 · 5:w2×1 · 3:w2×4 · 8:interest×1 · 9:f8889×13 · 10:div×1 · 10:f1040×3 · 10:f4952×6 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:interest×4 · 10:person×3 · 3:w2×2 · 4:w2×8 · 10:refund×1 · 10:s1×2 · 10:oi8z×3 · 10:s1×8 · 10:s1a×1 · 10:s2×2 · 10:person×1 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×3 · 10:s3×1 · 10:sa×1 · 5:sa×1 · 10:sa×4 · 10:sb×2 · 10:sd×2 · 1:sales×1 · 10:sli×1 · 10:ssb×1 · 11:sc×1 · 11:asset×1 · 11:scveh×1 · 12:person×1 · 12:asset×10 · 12:sc×35 · 12:scveh×7

- order 3 re-entered at step 53 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 18, 34 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 52), which its gate does not read.
- order 10 re-entered at step 63 by `refund.received` (order 10), left after step 52, 10 between. Late: left for `person[taxpayer].w2[emp_a].box4` (order 3), which sorts earlier and was reachable only after the answer to `person[taxpayer].rrta` (step 52), which its gate does not read.
- order 5 re-entered at step 97 by `sa.gifts` (order 5), left after step 14, 82 between. Late: reachable only after the answer to `sa.unsupported` (step 96), which its gate does not read.
- order 10 re-entered at step 98 by `sa.line1` (order 10), left after step 96, 1 between. Late: reachable only after the answer to `sa.gifts` (step 97), which its gate does not read.
- order 1 re-entered at step 106 by `$sales` (order 1), left after step 7, 98 between. Late: reachable only after the answer to `sd.other_forms` (step 105), which its gate does not read.
- order 10 re-entered at step 107 by `sli.interest` (order 10), left after step 105, 1 between. Late: left for `$sales` (order 1), which sorts earlier and was reachable only after the answer to `sd.other_forms` (step 105), which its gate does not read.
- form person re-entered at step 11 by `person[taxpayer].under16` (order 2), left after step 1, 9 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 12 by `household.community_property` (order 2), left after step 10, 1 between. Late: reachable only after the answer to `person[taxpayer].under16` (step 11), which its gate does not read.
- form f1040 re-entered at step 34 by `f1040.line25b` (order 10), left after step 2, 31 between. Sorting: it was reachable (since step 1), and `scope.other_line16` was asked instead (the bank puts order 0 first).
- form interest re-entered at step 46 by `interest[bank_a].amount` (order 10), left after step 19, 26 between. Sorting: it was reachable (since step 20), and `$f8889@person[taxpayer]` was asked instead (the bank puts order 9 seq 1 first).
- form person re-entered at step 50 by `person[taxpayer].age65` (order 10), left after step 11, 38 between. Late: left for `household.community_property` (order 2), which sorts earlier and was reachable only after the answer to `person[taxpayer].under16` (step 11), which its gate does not read.
- form w2 re-entered at step 53 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 18, 34 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 52), which its gate does not read.
- form s1 re-entered at step 69 by `s1.cod_any` (order 10), left after step 65, 3 between. Late: left for `$oi8z` (order 10), which sorts earlier and was reachable only after the answer to `s1.line8_other` (step 65), which its gate does not read.
- form person re-entered at step 80 by `person[taxpayer].x_other` (order 10), left after step 52, 27 between. Late: reachable only after the answer to `s2.other` (step 79), which its gate does not read.
- form s3 re-entered at step 81 by `s3.credit_bond` (order 10), left after step 13, 67 between. Sorting: it was reachable (since step 14), and `$w2@person[taxpayer]` was asked instead (the bank puts order 5 first).
- form person re-entered at step 91 by `person[taxpayer].blind` (order 10), left after step 80, 10 between. Late: reachable only after the answer to `sa.dependent` (step 90), which its gate does not read.
- form sa re-entered at step 92 by `sa.elect_itemize` (order 10), left after step 90, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 90), which its gate does not read.
- form s3 re-entered at step 95 by `s3.mcc` (order 10), left after step 89, 5 between. Late: reachable only after the answer to `sa.line8a` (step 94), which its gate does not read.
- form sa re-entered at step 96 by `sa.unsupported` (order 10), left after step 94, 1 between. Late: left for `s3.mcc` (order 10), which sorts earlier and was reachable only after the answer to `sa.line8a` (step 94), which its gate does not read.
- form person re-entered at step 112 by `person[taxpayer].plan` (order 12), left after step 91, 20 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 109), which its gate does not read.
- form asset re-entered at step 113 by `person[taxpayer].sc[biz_a].asset[item_1].class` (order 12), left after step 110, 2 between. Sorting: it was reachable (since step 111), and `$scveh@person[taxpayer].sc[biz_a]` was asked instead (the bank puts order 11 first).
- form sc re-entered at step 123 by `person[taxpayer].sc[biz_a].hi_uses` (order 12), left after step 109, 13 between. Sorting: left for `$asset@person[taxpayer].sc[biz_a]` (order 11), a child of the question before it, which the bank places in another form.
- form scveh re-entered at step 158 by `person[taxpayer].sc[biz_a].scveh[car_1].method` (order 12), left after step 111, 46 between. Sorting: it was reachable (since step 112), and `person[taxpayer].plan` was asked instead (within order 12, sorted by id).

**generated.32**: 10 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×2 · 2:dependent×3

**generated.33**: 10 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 2:dependent×3

**generated.34**: 169 questions, complete; order re-entries 20, form re-entries 7 sorting and 24 late, delayed children 2 sorting and 6 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 2:dependent×20 · 2:household×2 · 2:retirement×3 · 2:person×1 · 2:household×1 · 2:s3×1 · 3:dependent×1 · 2:household×2 · 3:dependent×2 · 2:dependent×3 · 5:w2×1 · 3:w2×4 · 8:interest×1 · 9:f8889×13 · 10:div×1 · 10:f1040×3 · 10:f4952×2 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:interest×2 · 10:person×3 · 3:w2×2 · 4:w2×8 · 10:refund×1 · 10:s1×2 · 10:oi8z×1 · 10:s1×8 · 10:s1a×1 · 10:s2×2 · 10:person×1 · 10:s3×9 · 10:sa×1 · 2:dependent×1 · 2:person×2 · 10:person×1 · 10:sa×3 · 10:s3×1 · 10:sa×1 · 5:sa×1 · 10:sa×4 · 10:sb×1 · 10:f1040×1 · 10:sb×2 · 10:sd×3 · 1:sales×1 · 10:sli×1 · 10:ssb×4 · 11:sc×1 · 10:s1a×2 · 12:s179×1 · 15:div×9 · 10:qbi×1 · 20:f2441×2 · 20:s8812×1 · 22:person×1 · 24:f5695×2 · 30:div×1 · 30:f1040×1 · 2:dependent×1 · 10:qbi×1 · 12:qbi×1 · 20:household×1 · 30:dependent×2 · 30:person×1 · 20:s8812×1

- order 2 re-entered at step 37 by `household.married` (order 2), left after step 35, 1 between. Late: reachable only after the answer to `dependent[dep_a].absence_no_return` (step 36), which its gate does not read.
- order 3 re-entered at step 39 by `dependent[dep_b].lawful` (order 3), left after step 36, 2 between. Late: left for `household.married` (order 2), which sorts earlier and was reachable only after the answer to `dependent[dep_a].absence_no_return` (step 36), which its gate does not read.
- order 2 re-entered at step 41 by `dependent[dep_b].gross_income` (order 2), left after step 38, 2 between. Late: reachable only after the answer to `dependent[dep_b].qr_all_year` (step 40), which its gate does not read.
- order 3 re-entered at step 45 by `person[taxpayer].w2[emp_a].box1` (order 3), left after step 40, 4 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 44), its parent or roster.
- order 3 re-entered at step 77 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 48, 28 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 76), which its gate does not read.
- order 10 re-entered at step 87 by `refund.received` (order 10), left after step 76, 10 between. Late: left for `person[taxpayer].w2[emp_a].box4` (order 3), which sorts earlier and was reachable only after the answer to `person[taxpayer].rrta` (step 76), which its gate does not read.
- order 2 re-entered at step 113 by `dependent[dep_a].work_ssn` (order 2), left after step 43, 69 between. Late: reachable only after the answer to `sa.dependent` (step 112), which its gate does not read.
- order 10 re-entered at step 116 by `person[taxpayer].blind` (order 10), left after step 112, 3 between. Late: left for `dependent[dep_a].work_ssn` (order 2), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 112), which its gate does not read.
- order 5 re-entered at step 122 by `sa.gifts` (order 5), left after step 44, 77 between. Late: reachable only after the answer to `sa.unsupported` (step 121), which its gate does not read.
- order 10 re-entered at step 123 by `sa.line1` (order 10), left after step 121, 1 between. Late: reachable only after the answer to `sa.gifts` (step 122), which its gate does not read.
- order 1 re-entered at step 134 by `$sales` (order 1), left after step 7, 126 between. Late: reachable only after the answer to `sd.other_forms` (step 133), which its gate does not read.
- order 10 re-entered at step 135 by `sli.interest` (order 10), left after step 133, 1 between. Late: left for `$sales` (order 1), which sorts earlier and was reachable only after the answer to `sd.other_forms` (step 133), which its gate does not read.
- order 10 re-entered at step 141 by `s1a.overtime` (order 10), left after step 139, 1 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 140), which its gate does not read.
- order 10 re-entered at step 153 by `qbi.dividends` (order 10), left after step 142, 10 between. Late: reachable only after the answer to `div.box2d` (step 152), which its gate does not read.
- order 2 re-entered at step 162 by `dependent[dep_a].kidnapped` (order 2), left after step 115, 46 between. Late: reachable only after the answer to `f1040.tax_exempt_interest` (step 161), which its gate does not read.
- order 10 re-entered at step 163 by `qbi.unsupported` (order 10), left after step 153, 9 between. Late: reachable only after the answer to `f1040.tax_exempt_interest` (step 161), which its gate does not read.
- order 12 re-entered at step 164 by `qbi.carryforward` (order 12), left after step 143, 20 between. Late: reachable only after the answer to `f1040.tax_exempt_interest` (step 161), which its gate does not read.
- order 20 re-entered at step 165 by `household.credit_disallowed` (order 20), left after step 156, 8 between. Late: reachable only after the answer to `f1040.tax_exempt_interest` (step 161), which its gate does not read.
- order 30 re-entered at step 166 by `dependent[dep_a].us_half` (order 30), left after step 161, 4 between. Late: reachable only after the answer to `dependent[dep_a].kidnapped` (step 162), which its gate does not read.
- order 20 re-entered at step 169 by `s8812.combat_pay` (order 20), left after step 165, 3 between. Late: reachable only after the answer to `person[taxpayer].eic_ssn` (step 168), which its gate does not read.
- form retirement re-entered at step 30 by `person[taxpayer].retirement[r1].account` (order 2), left after step 7, 22 between. Sorting: it was reachable (since step 8), and `$dependent` was asked instead (within order 2, sorted by id).
- form person re-entered at step 33 by `person[taxpayer].under16` (order 2), left after step 1, 31 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 34 by `household.community_property` (order 2), left after step 29, 4 between. Late: reachable only after the answer to `person[taxpayer].under16` (step 33), which its gate does not read.
- form dependent re-entered at step 36 by `dependent[dep_a].absence_no_return` (order 3), left after step 27, 8 between. Late: reachable only after the answer to `household.home_cost` (step 29), which its gate does not read.
- form household re-entered at step 37 by `household.married` (order 2), left after step 34, 2 between. Late: reachable only after the answer to `dependent[dep_a].absence_no_return` (step 36), which its gate does not read.
- form dependent re-entered at step 39 by `dependent[dep_b].lawful` (order 3), left after step 36, 2 between. Late: left for `household.married` (order 2), which sorts earlier and was reachable only after the answer to `dependent[dep_a].absence_no_return` (step 36), which its gate does not read.
- form f1040 re-entered at step 64 by `f1040.line25b` (order 10), left after step 2, 61 between. Sorting: it was reachable (since step 1), and `scope.other_line16` was asked instead (the bank puts order 0 first).
- form interest re-entered at step 72 by `interest[bank_a].amount` (order 10), left after step 49, 22 between. Sorting: it was reachable (since step 50), and `$f8889@person[taxpayer]` was asked instead (the bank puts order 9 seq 1 first).
- form person re-entered at step 74 by `person[taxpayer].age65` (order 10), left after step 33, 40 between. Late: left for `household.community_property` (order 2), which sorts earlier and was reachable only after the answer to `person[taxpayer].under16` (step 33), which its gate does not read.
- form w2 re-entered at step 77 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 48, 28 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 76), which its gate does not read.
- form s1 re-entered at step 91 by `s1.cod_any` (order 10), left after step 89, 1 between. Late: left for `$oi8z` (order 10), which sorts earlier and was reachable only after the answer to `s1.line8_other` (step 89), which its gate does not read.
- form person re-entered at step 102 by `person[taxpayer].x_other` (order 10), left after step 76, 25 between. Late: reachable only after the answer to `s2.other` (step 101), which its gate does not read.
- form s3 re-entered at step 103 by `s3.credit_bond` (order 10), left after step 35, 67 between. Sorting: it was reachable (since step 36), and `dependent[dep_a].absence_no_return` was asked instead (the bank puts order 3 first).
- form dependent re-entered at step 113 by `dependent[dep_a].work_ssn` (order 2), left after step 43, 69 between. Late: reachable only after the answer to `sa.dependent` (step 112), which its gate does not read.
- form person re-entered at step 114 by `person[taxpayer].tin` (order 2), left after step 102, 11 between. Late: reachable only after the answer to `sa.dependent` (step 112), which its gate does not read.
- form sa re-entered at step 117 by `sa.elect_itemize` (order 10), left after step 112, 4 between. Late: left for `dependent[dep_a].work_ssn` (order 2), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 112), which its gate does not read.
- form s3 re-entered at step 120 by `s3.mcc` (order 10), left after step 111, 8 between. Late: reachable only after the answer to `sa.line8a` (step 119), which its gate does not read.
- form sa re-entered at step 121 by `sa.unsupported` (order 10), left after step 119, 1 between. Late: left for `s3.mcc` (order 10), which sorts earlier and was reachable only after the answer to `sa.line8a` (step 119), which its gate does not read.
- form f1040 re-entered at step 128 by `f1040.line3a` (order 10), left after step 66, 61 between. Late: reachable only after the answer to `sb.ordinary_dividends` (step 127), which its gate does not read.
- form sb re-entered at step 129 by `sb.unsupported` (order 10), left after step 127, 1 between. Late: left for `f1040.line3a` (order 10), which sorts earlier and was reachable only after the answer to `sb.ordinary_dividends` (step 127), which its gate does not read.
- form s1a re-entered at step 141 by `s1a.overtime` (order 10), left after step 99, 41 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 140), which its gate does not read.
- form div re-entered at step 144 by `div.box2c` (order 15), left after step 63, 80 between. Late: reachable only after the answer to `sd.distributions` (step 132), which its gate does not read.
- form person re-entered at step 157 by `person[taxpayer].sav_trad` (order 22), left after step 116, 40 between. Sorting: it was reachable (since step 2), and `sa.elect_itemize` was asked instead (the bank puts order 10 first).
- form div re-entered at step 160 by `div.box12` (order 30), left after step 152, 7 between. Late: left for `qbi.dividends` (order 10), which sorts earlier and was reachable only after the answer to `div.box2d` (step 152), which its gate does not read.
- form f1040 re-entered at step 161 by `f1040.tax_exempt_interest` (order 30), left after step 128, 32 between. Late: reachable only after the answer to `ssb.benefits` (step 136), which its gate does not read.
- form dependent re-entered at step 162 by `dependent[dep_a].kidnapped` (order 2), left after step 113, 48 between. Late: reachable only after the answer to `f1040.tax_exempt_interest` (step 161), which its gate does not read.
- form qbi re-entered at step 163 by `qbi.unsupported` (order 10), left after step 153, 9 between. Late: reachable only after the answer to `f1040.tax_exempt_interest` (step 161), which its gate does not read.
- form household re-entered at step 165 by `household.credit_disallowed` (order 20), left after step 38, 126 between. Late: reachable only after the answer to `f1040.tax_exempt_interest` (step 161), which its gate does not read.
- form dependent re-entered at step 166 by `dependent[dep_a].us_half` (order 30), left after step 162, 3 between. Sorting: it was reachable (since step 163), and `qbi.unsupported` was asked instead (the bank puts order 10 first).
- form person re-entered at step 168 by `person[taxpayer].eic_ssn` (order 30), left after step 157, 10 between. Late: reachable only after the answer to `dependent[dep_a].eic_ssn` (step 167), which its gate does not read.
- form s8812 re-entered at step 169 by `s8812.combat_pay` (order 20), left after step 156, 12 between. Late: reachable only after the answer to `person[taxpayer].eic_ssn` (step 168), which its gate does not read.
- `sb.ordinary_dividends` (order 10), step 127: child of `div.any` (step 63), 63 other questions between. Sorting: it was reachable (since step 64), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `sd.distributions` (order 10), step 132: child of `div.any` (step 63), 67 other questions between. Sorting: it was reachable (since step 64), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `div.box13` (order 15), step 145: child of `div.any` (step 63), 79 other questions between. Late: reachable only after the answer to `div.box2c` (step 144), which its gate does not read.
- `div.box10` (order 15), step 146: child of `div.any` (step 63), 79 other questions between. Late: reachable only after the answer to `div.box13` (step 145), which its gate does not read.
- `div.box3` (order 15), step 149: child of `div.any` (step 63), 81 other questions between. Late: reachable only after the answer to `div.box13` (step 145), which its gate does not read.
- `div.box9` (order 15), step 150: child of `div.any` (step 63), 81 other questions between. Late: reachable only after the answer to `div.box13` (step 145), which its gate does not read.
- `div.box12` (order 30), step 160: child of `div.any` (step 63), 90 other questions between. Late: reachable only after the answer to `ssb.benefits` (step 136), which its gate does not read.
- `household.credit_disallowed` (order 20), step 165: child of `sa.excluded_income` (step 118), 46 other questions between. Late: reachable only after the answer to `f1040.tax_exempt_interest` (step 161), which its gate does not read.

**generated.35**: 2 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1

**generated.36**: 30 questions, refused; order re-entries 1, form re-entries 2 sorting and 3 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 2:dependent×12 · 2:household×2 · 2:dependent×2 · 2:person×1 · 2:household×1 · 2:s3×1 · 3:dependent×3 · 2:household×1

- order 2 re-entered at step 30 by `household.married` (order 2), left after step 26, 3 between. Late: reachable only after the answer to `dependent[dep_a].placed` (step 29), which its gate does not read.
- form dependent re-entered at step 22 by `dependent[dep_a].months` (order 2), left after step 19, 2 between. Late: reachable only after the answer to `household.home_cost` (step 21), which its gate does not read.
- form person re-entered at step 24 by `person[taxpayer].under16` (order 2), left after step 1, 22 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 25 by `household.community_property` (order 2), left after step 21, 3 between. Late: reachable only after the answer to `person[taxpayer].under16` (step 24), which its gate does not read.
- form dependent re-entered at step 27 by `dependent[dep_a].absence_no_return` (order 3), left after step 23, 3 between. Sorting: it was reachable (since step 22), and `person[taxpayer].under16` was asked instead (the bank puts order 2 first).
- form household re-entered at step 30 by `household.married` (order 2), left after step 25, 4 between. Late: reachable only after the answer to `dependent[dep_a].placed` (step 29), which its gate does not read.

**generated.37**: 144 questions, complete; order re-entries 20, form re-entries 6 sorting and 15 late, delayed children 2 sorting and 5 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 2:dependent×1 · 2:household×2 · 2:retirement×6 · 2:person×1 · 2:household×1 · 2:s3×1 · 3:retirement×1 · 2:retirement×2 · 3:retirement×1 · 2:retirement×5 · 5:w2×1 · 3:w2×2 · 8:interest×1 · 9:f8889×13 · 10:div×1 · 10:f1040×3 · 10:f4952×6 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:person×4 · 3:w2×1 · 4:w2×2 · 10:refund×1 · 10:s1×2 · 10:oi8z×1 · 10:s1×10 · 10:s1a×1 · 10:s2×2 · 10:person×1 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×3 · 10:s3×1 · 10:sa×1 · 5:sa×1 · 10:sa×1 · 5:gift×1 · 10:sa×5 · 10:sb×1 · 10:f1040×1 · 10:sb×2 · 10:sd×3 · 1:sales×1 · 2:sales×1 · 3:sales×1 · 4:sales×1 · 5:sales×1 · 10:sales×2 · 10:sli×1 · 10:ssb×1 · 11:sc×1 · 10:s1a×2 · 12:s179×1 · 15:div×9 · 10:qbi×1 · 20:f2441×2 · 22:person×1 · 10:qbi×1 · 12:qbi×1 · 24:f5695×2

- order 2 re-entered at step 21 by `person[taxpayer].retirement[r1].box1` (order 2), left after step 19, 1 between. Late: reachable only after the answer to `person[taxpayer].retirement[r1].code_screen` (step 20), which its gate does not read.
- order 3 re-entered at step 23 by `person[taxpayer].retirement[r2].code_screen` (order 3), left after step 20, 2 between. Late: left for `person[taxpayer].retirement[r1].box1` (order 2), which sorts earlier and was reachable only after the answer to `person[taxpayer].retirement[r1].code_screen` (step 20), which its gate does not read.
- order 2 re-entered at step 24 by `person[taxpayer].retirement[r2].annuity` (order 2), left after step 22, 1 between. Late: reachable only after the answer to `person[taxpayer].retirement[r2].code_screen` (step 23), which its gate does not read.
- order 3 re-entered at step 30 by `person[taxpayer].w2[emp_a].box1` (order 3), left after step 23, 6 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 29), its parent or roster.
- order 3 re-entered at step 63 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 31, 31 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 62), which its gate does not read.
- order 10 re-entered at step 66 by `refund.received` (order 10), left after step 62, 3 between. Late: left for `person[taxpayer].w2[emp_a].box4` (order 3), which sorts earlier and was reachable only after the answer to `person[taxpayer].rrta` (step 62), which its gate does not read.
- order 5 re-entered at step 100 by `sa.gifts` (order 5), left after step 29, 70 between. Late: reachable only after the answer to `sa.unsupported` (step 99), which its gate does not read.
- order 10 re-entered at step 101 by `sa.charity_limited` (order 10), left after step 99, 1 between. Late: reachable only after the answer to `sa.gifts` (step 100), its parent or roster.
- order 5 re-entered at step 102 by `$gift` (order 5), left after step 100, 1 between. Late: reachable only after the answer to `sa.charity_limited` (step 101), which its gate does not read.
- order 10 re-entered at step 103 by `sa.line1` (order 10), left after step 101, 1 between. Late: left for `$gift` (order 5), which sorts earlier and was reachable only after the answer to `sa.charity_limited` (step 101), which its gate does not read.
- order 1 re-entered at step 115 by `$sales` (order 1), left after step 7, 107 between. Late: reachable only after the answer to `sd.other_forms` (step 114), which its gate does not read.
- order 2 re-entered at step 116 by `sales[s1].box` (order 2), left after step 28, 87 between. Late: reachable only after the answer to `$sales` (step 115), its parent or roster.
- order 3 re-entered at step 117 by `sales[s1].special` (order 3), left after step 63, 53 between. Late: reachable only after the answer to `sales[s1].box` (step 116), which its gate does not read.
- order 4 re-entered at step 118 by `sales[s1].code` (order 4), left after step 65, 52 between. Late: reachable only after the answer to `sales[s1].special` (step 117), which its gate does not read.
- order 5 re-entered at step 119 by `sales[s1].route` (order 5), left after step 102, 16 between. Late: reachable only after the answer to `sales[s1].code` (step 118), which its gate does not read.
- order 10 re-entered at step 120 by `sales[s1].correct_basis` (order 10), left after step 114, 5 between. Late: reachable only after the answer to `sales[s1].route` (step 119), which its gate does not read.
- order 10 re-entered at step 125 by `s1a.overtime` (order 10), left after step 123, 1 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 124), which its gate does not read.
- order 10 re-entered at step 137 by `qbi.dividends` (order 10), left after step 126, 10 between. Late: reachable only after the answer to `div.box2d` (step 136), which its gate does not read.
- order 10 re-entered at step 141 by `qbi.unsupported` (order 10), left after step 137, 3 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 140), which its gate does not read.
- order 12 re-entered at step 142 by `qbi.carryforward` (order 12), left after step 127, 14 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 140), which its gate does not read.
- form retirement re-entered at step 11 by `person[taxpayer].retirement[r1].account` (order 2), left after step 7, 3 between. Sorting: it was reachable (since step 8), and `$dependent` was asked instead (within order 2, sorted by id).
- form person re-entered at step 17 by `person[taxpayer].under16` (order 2), left after step 1, 15 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 18 by `household.community_property` (order 2), left after step 10, 7 between. Late: reachable only after the answer to `person[taxpayer].under16` (step 17), which its gate does not read.
- form retirement re-entered at step 20 by `person[taxpayer].retirement[r1].code_screen` (order 3), left after step 16, 3 between. Sorting: it was reachable (since step 14), and `person[taxpayer].under16` was asked instead (the bank puts order 2 first).
- form f1040 re-entered at step 47 by `f1040.line25b` (order 10), left after step 2, 44 between. Sorting: it was reachable (since step 1), and `scope.other_line16` was asked instead (the bank puts order 0 first).
- form person re-entered at step 59 by `person[taxpayer].age65` (order 10), left after step 17, 41 between. Late: left for `household.community_property` (order 2), which sorts earlier and was reachable only after the answer to `person[taxpayer].under16` (step 17), which its gate does not read.
- form w2 re-entered at step 63 by `person[taxpayer].w2[emp_a].box4` (order 3), left after step 31, 31 between. Late: reachable only after the answer to `person[taxpayer].rrta` (step 62), which its gate does not read.
- form s1 re-entered at step 70 by `s1.cod_any` (order 10), left after step 68, 1 between. Late: left for `$oi8z` (order 10), which sorts earlier and was reachable only after the answer to `s1.line8_other` (step 68), which its gate does not read.
- form person re-entered at step 83 by `person[taxpayer].x_other` (order 10), left after step 62, 20 between. Late: reachable only after the answer to `s2.other` (step 82), which its gate does not read.
- form s3 re-entered at step 84 by `s3.credit_bond` (order 10), left after step 19, 64 between. Sorting: it was reachable (since step 20), and `person[taxpayer].retirement[r1].code_screen` was asked instead (the bank puts order 3 first).
- form person re-entered at step 94 by `person[taxpayer].blind` (order 10), left after step 83, 10 between. Late: reachable only after the answer to `sa.dependent` (step 93), which its gate does not read.
- form sa re-entered at step 95 by `sa.elect_itemize` (order 10), left after step 93, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 93), which its gate does not read.
- form s3 re-entered at step 98 by `s3.mcc` (order 10), left after step 92, 5 between. Late: reachable only after the answer to `sa.line8a` (step 97), which its gate does not read.
- form sa re-entered at step 99 by `sa.unsupported` (order 10), left after step 97, 1 between. Late: left for `s3.mcc` (order 10), which sorts earlier and was reachable only after the answer to `sa.line8a` (step 97), which its gate does not read.
- form sa re-entered at step 103 by `sa.line1` (order 10), left after step 101, 1 between. Late: left for `$gift` (order 5), which sorts earlier and was reachable only after the answer to `sa.charity_limited` (step 101), which its gate does not read.
- form f1040 re-entered at step 109 by `f1040.line3a` (order 10), left after step 49, 59 between. Late: reachable only after the answer to `sb.ordinary_dividends` (step 108), which its gate does not read.
- form sb re-entered at step 110 by `sb.unsupported` (order 10), left after step 108, 1 between. Late: left for `f1040.line3a` (order 10), which sorts earlier and was reachable only after the answer to `sb.ordinary_dividends` (step 108), which its gate does not read.
- form s1a re-entered at step 125 by `s1a.overtime` (order 10), left after step 80, 44 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 124), which its gate does not read.
- form div re-entered at step 128 by `div.box2c` (order 15), left after step 46, 81 between. Late: reachable only after the answer to `sd.distributions` (step 113), which its gate does not read.
- form person re-entered at step 140 by `person[taxpayer].sav_trad` (order 22), left after step 94, 45 between. Sorting: it was reachable (since step 2), and `sa.elect_itemize` was asked instead (the bank puts order 10 first).
- form qbi re-entered at step 141 by `qbi.unsupported` (order 10), left after step 137, 3 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 140), which its gate does not read.
- `sa.line11` (order 10), step 104: child of `sa.gifts` (step 100), 2 other questions between. Late: reachable only after the answer to `sa.charity_limited` (step 101), which its gate does not read.
- `sb.ordinary_dividends` (order 10), step 108: child of `div.any` (step 46), 61 other questions between. Sorting: it was reachable (since step 47), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `sd.distributions` (order 10), step 113: child of `div.any` (step 46), 65 other questions between. Sorting: it was reachable (since step 47), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `div.box13` (order 15), step 129: child of `div.any` (step 46), 80 other questions between. Late: reachable only after the answer to `div.box2c` (step 128), which its gate does not read.
- `div.box10` (order 15), step 130: child of `div.any` (step 46), 80 other questions between. Late: reachable only after the answer to `div.box13` (step 129), which its gate does not read.
- `div.box3` (order 15), step 133: child of `div.any` (step 46), 82 other questions between. Late: reachable only after the answer to `div.box13` (step 129), which its gate does not read.
- `div.box9` (order 15), step 134: child of `div.any` (step 46), 82 other questions between. Late: reachable only after the answer to `div.box13` (step 129), which its gate does not read.

**generated.38**: 21 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 2:dependent×14

**generated.39**: 51 questions, refused; order re-entries 2, form re-entries 1 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×2 · 2:dependent×1 · 2:household×1 · 2:person×2 · 2:s3×1 · 5:w2×1 · 3:w2×4 · 5:w2×1 · 3:w2×2 · 8:interest×1 · 9:f8889×30

- order 5 re-entered at step 18 by `$w2@person[taxpayer]` (order 5), left after step 13, 4 between. Sorting: left for `person[spouse].w2[emp_a].box1` (order 3), a child of the question before it, which the bank places in another order number.
- order 3 re-entered at step 19 by `person[taxpayer].w2[emp_a].box1` (order 3), left after step 17, 1 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 18), its parent or roster.
- form person re-entered at step 10 by `person[spouse].under16` (order 2), left after step 1, 8 between. Sorting: it was reachable (since step 2), and `scope.other_line16` was asked instead (the bank puts order 0 first).

### minimal returns

**every gate closed**: 82 questions, complete; order re-entries 7, form re-entries 4 sorting and 8 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 2:dependent×1 · 2:household×2 · 2:person×1 · 2:household×1 · 2:s3×1 · 5:w2×1 · 8:interest×1 · 9:f8889×1 · 10:div×1 · 10:f1040×3 · 10:f4952×2 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:person×3 · 10:refund×1 · 10:s1×2 · 10:oi8z×1 · 10:s1×8 · 10:s1a×1 · 10:s2×2 · 10:person×1 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×4 · 5:sa×1 · 10:sa×4 · 10:sb×1 · 10:sd×2 · 1:sales×1 · 10:sli×1 · 10:ssb×1 · 11:sc×1 · 10:s1a×2 · 12:s179×1 · 20:f2441×2 · 22:person×1 · 10:qbi×1 · 12:qbi×1 · 24:f5695×2 · 30:person×1

- order 5 re-entered at step 60 by `sa.gifts` (order 5), left after step 14, 45 between. Late: reachable only after the answer to `sa.unsupported` (step 59), which its gate does not read.
- order 10 re-entered at step 61 by `sa.line1` (order 10), left after step 59, 1 between. Late: reachable only after the answer to `sa.gifts` (step 60), which its gate does not read.
- order 1 re-entered at step 68 by `$sales` (order 1), left after step 7, 60 between. Late: reachable only after the answer to `sd.other_forms` (step 67), which its gate does not read.
- order 10 re-entered at step 69 by `sli.interest` (order 10), left after step 67, 1 between. Late: left for `$sales` (order 1), which sorts earlier and was reachable only after the answer to `sd.other_forms` (step 67), which its gate does not read.
- order 10 re-entered at step 72 by `s1a.overtime` (order 10), left after step 70, 1 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 71), which its gate does not read.
- order 10 re-entered at step 78 by `qbi.unsupported` (order 10), left after step 73, 4 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 77), which its gate does not read.
- order 12 re-entered at step 79 by `qbi.carryforward` (order 12), left after step 74, 4 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 77), which its gate does not read.
- form person re-entered at step 11 by `person[taxpayer].under16` (order 2), left after step 1, 9 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 12 by `household.community_property` (order 2), left after step 10, 1 between. Late: reachable only after the answer to `person[taxpayer].under16` (step 11), which its gate does not read.
- form f1040 re-entered at step 18 by `f1040.line25b` (order 10), left after step 2, 15 between. Sorting: it was reachable (since step 1), and `scope.other_line16` was asked instead (the bank puts order 0 first).
- form person re-entered at step 26 by `person[taxpayer].age65` (order 10), left after step 11, 14 between. Late: left for `household.community_property` (order 2), which sorts earlier and was reachable only after the answer to `person[taxpayer].under16` (step 11), which its gate does not read.
- form s1 re-entered at step 33 by `s1.cod_any` (order 10), left after step 31, 1 between. Late: left for `$oi8z` (order 10), which sorts earlier and was reachable only after the answer to `s1.line8_other` (step 31), which its gate does not read.
- form person re-entered at step 44 by `person[taxpayer].x_other` (order 10), left after step 28, 15 between. Late: reachable only after the answer to `s2.other` (step 43), which its gate does not read.
- form s3 re-entered at step 45 by `s3.credit_bond` (order 10), left after step 13, 31 between. Sorting: it was reachable (since step 14), and `$w2@person[taxpayer]` was asked instead (the bank puts order 5 first).
- form person re-entered at step 55 by `person[taxpayer].blind` (order 10), left after step 44, 10 between. Late: reachable only after the answer to `sa.dependent` (step 54), which its gate does not read.
- form sa re-entered at step 56 by `sa.elect_itemize` (order 10), left after step 54, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 54), which its gate does not read.
- form s1a re-entered at step 72 by `s1a.overtime` (order 10), left after step 41, 30 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 71), which its gate does not read.
- form person re-entered at step 77 by `person[taxpayer].sav_trad` (order 22), left after step 55, 21 between. Sorting: it was reachable (since step 2), and `sa.elect_itemize` was asked instead (the bank puts order 10 first).
- form person re-entered at step 82 by `person[taxpayer].eic_ssn` (order 30), left after step 77, 4 between. Late: left for `qbi.unsupported` (order 10), which sorts earlier and was reachable only after the answer to `person[taxpayer].sav_trad` (step 77), which its gate does not read.

**div.any = true alone**: 88 questions, complete; order re-entries 7, form re-entries 4 sorting and 11 late, delayed children 2 sorting and 4 late.

- form sb re-entered at step 68 by `sb.foreign_any` (order 10), left after step 65, 2 between. Late: reachable only after the answer to `sd.distributions` (step 67), which its gate does not read.
- form sd re-entered at step 69 by `sd.other_forms` (order 10), left after step 67, 1 between. Late: left for `sb.foreign_any` (order 10), which sorts earlier and was reachable only after the answer to `sd.distributions` (step 67), which its gate does not read.
- form div re-entered at step 77 by `div.box13` (order 15), left after step 17, 59 between. Late: reachable only after the answer to `sd.distributions` (step 67), which its gate does not read.
- `sb.ordinary_dividends` (order 10), step 65: child of `div.any` (step 17), 47 other questions between. Sorting: it was reachable (since step 18), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `sd.distributions` (order 10), step 67: child of `div.any` (step 17), 48 other questions between. Sorting: it was reachable (since step 18), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `div.box13` (order 15), step 77: child of `div.any` (step 17), 57 other questions between. Late: reachable only after the answer to `sd.distributions` (step 67), which its gate does not read.
- `div.box10` (order 15), step 78: child of `div.any` (step 17), 57 other questions between. Late: reachable only after the answer to `div.box13` (step 77), which its gate does not read.
- `div.box3` (order 15), step 79: child of `div.any` (step 17), 57 other questions between. Late: reachable only after the answer to `div.box13` (step 77), which its gate does not read.
- `div.box9` (order 15), step 80: child of `div.any` (step 17), 57 other questions between. Late: reachable only after the answer to `div.box13` (step 77), which its gate does not read.

**f4952.has_interest = true alone**: 84 questions, complete; order re-entries 7, form re-entries 4 sorting and 8 late, delayed children 0 sorting and 0 late.

**f8889.coverage_year = "family" alone**: 82 questions, complete; order re-entries 7, form re-entries 4 sorting and 8 late, delayed children 0 sorting and 0 late.

**f8889.coverage_year = "changed" alone**: 82 questions, complete; order re-entries 7, form re-entries 4 sorting and 8 late, delayed children 0 sorting and 0 late.

**s3.adoption_any = true alone**: 84 questions, complete; order re-entries 7, form re-entries 4 sorting and 8 late, delayed children 0 sorting and 0 late.

**s3.ev = true alone**: 85 questions, complete; order re-entries 7, form re-entries 4 sorting and 8 late, delayed children 0 sorting and 0 late.

**s3.farmland = true alone**: 83 questions, complete; order re-entries 7, form re-entries 4 sorting and 8 late, delayed children 0 sorting and 0 late.

**s3.foreign_any = true alone**: 86 questions, complete; order re-entries 7, form re-entries 5 sorting and 9 late, delayed children 1 sorting and 2 late.

- form ftc re-entered at step 50 by `ftc.carryover` (order 10), left after step 25, 24 between. Late: reachable only after the answer to `s3.foreign_any` (step 49), its parent or roster.
- form s3 re-entered at step 51 by `s3.kerosene` (order 10), left after step 49, 1 between. Sorting: left for `ftc.carryover` (order 10), a child of the question before it, which the bank places in another form.
- `s3.section960c` (order 10), step 54: child of `s3.foreign_any` (step 49), 3 other questions between. Sorting: it was reachable (since step 50), and `s3.kerosene` was asked instead (within order 10, sorted by id).
- `s3.section965` (order 10), step 55: child of `s3.foreign_any` (step 49), 3 other questions between. Late: reachable only after the answer to `s3.section960c` (step 54), which its gate does not read.
- `s3.virgin_islands` (order 10), step 56: child of `s3.foreign_any` (step 49), 3 other questions between. Late: reachable only after the answer to `s3.section965` (step 55), which its gate does not read.

**s3.kerosene = true alone**: 83 questions, complete; order re-entries 7, form re-entries 4 sorting and 8 late, delayed children 0 sorting and 0 late.

**s3.prior_other_forms = true alone**: 85 questions, complete; order re-entries 7, form re-entries 5 sorting and 9 late, delayed children 0 sorting and 0 late.

- form ftc re-entered at step 53 by `ftc.carryover` (order 10), left after step 25, 27 between. Late: reachable only after the answer to `s3.prior_other_forms` (step 52), its parent or roster.
- form s3 re-entered at step 54 by `s3.prior_amt` (order 10), left after step 52, 1 between. Sorting: left for `ftc.carryover` (order 10), a child of the question before it, which the bank places in another form.

**sa.gifts = true alone**: 85 questions, complete; order re-entries 9, form re-entries 4 sorting and 9 late, delayed children 0 sorting and 1 late.

- order 10 re-entered at step 61 by `sa.charity_limited` (order 10), left after step 59, 1 between. Late: reachable only after the answer to `sa.gifts` (step 60), its parent or roster.
- order 5 re-entered at step 62 by `$gift` (order 5), left after step 60, 1 between. Late: reachable only after the answer to `sa.charity_limited` (step 61), which its gate does not read.
- order 10 re-entered at step 63 by `sa.line1` (order 10), left after step 61, 1 between. Late: left for `$gift` (order 5), which sorts earlier and was reachable only after the answer to `sa.charity_limited` (step 61), which its gate does not read.
- form sa re-entered at step 63 by `sa.line1` (order 10), left after step 61, 1 between. Late: left for `$gift` (order 5), which sorts earlier and was reachable only after the answer to `sa.charity_limited` (step 61), which its gate does not read.
- `sa.line11` (order 10), step 64: child of `sa.gifts` (step 60), 2 other questions between. Late: reachable only after the answer to `sa.charity_limited` (step 61), which its gate does not read.

**sb.foreign_any = true alone**: 86 questions, complete; order re-entries 7, form re-entries 4 sorting and 8 late, delayed children 0 sorting and 0 late.

