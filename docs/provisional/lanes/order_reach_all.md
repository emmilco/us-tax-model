# The interview's asking order, measured

Written by `node engine/dist/main.js interview-order --write` (engine/src/interview-order.ts; deterministic, no model calls). Returns walked: the whole-return fixtures, the generated returns and the minimal returns, in the `full` profile. Walked with `--reach-all`: the reach pass applied to every question, as if each stated a `seq`; not how the interview asks today's bank.

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
| whole-return fixtures | 11 | 79.7 | 0.2 | 3.6 | 5.2 | 3.0 | 1.2 | 0.8 |
| generated returns | 40 | 69.7 | 0.4 | 2.7 | 3.7 | 2.4 | 0.9 | 0.4 |
| minimal returns | 13 | 84.2 | 0.0 | 4.0 | 5.2 | 3.2 | 0.6 | 0.2 |

The counts are means per walk.

## What the late questions waited on

Every late finding, by the question that became reachable part-way and the answer it waited on, with the number of walks showing it
and what it caused (an order number re-entered, a form re-entered, a child delayed).

| question | waited on | its parent or roster? | caused | walks |
|---|---|---|---|---|
| `sa.gifts` | `sa.elect_itemize` | no | order | 34 |
| `person.blind` | `sa.dependent` | no | form | 31 |
| `qbi.carryforward` | `person.sav_trad` | no | order | 26 |
| `qbi.unsupported` | `person.sav_trad` | no | form, order | 26 |
| `w2.box1` | `$w2` | yes | order | 18 |
| `$gift` | `sa.gifts` | no | form | 12 |
| `s3.mcc` | `sa.line8a` | no | form | 11 |
| `w2.box5` | `$w2` | yes | order | 11 |
| `f1040.line3a` | `sb.ordinary_dividends` | no | form | 8 |
| `gift.deduction` | `$gift` | yes | order | 7 |
| `dependent.gross_income` | `dependent.qr_all_year` | no | order | 6 |
| `div.box10` | `div.box2c` | no | child | 6 |
| `div.box3` | `div.box2c` | no | child | 6 |
| `div.box9` | `div.box2c` | no | child | 6 |
| `w2.box3` | `$w2` | yes | order | 6 |
| `sa.charity_limited` | `sa.gifts` | yes | order | 5 |
| `person.tin` | `sa.dependent` | no | form, order | 3 |
| `person.work_ssn` | `person.age65` | no | order | 3 |
| `div.box10` | `div.box13` | no | child | 2 |
| `div.box3` | `div.box13` | no | child | 2 |
| `eic.us_home` | `person.born_before_2001` | no | form | 2 |
| `person.born_after_1960` | `eic.died_2025` | no | form | 2 |
| `person.died_before_65` | `person.work_ssn` | no | order | 2 |
| `person.plan` | `$sc` | no | form | 2 |
| `s8812.combat_pay` | `eic.qc_of_another` | no | order | 2 |
| `dependent.absence_no_return` | `household.home_cost` | no | form | 1 |
| `dependent.kidnapped` | `f1040.tax_exempt_interest` | no | form, order | 1 |
| `dependent.months` | `household.home_cost` | no | form | 1 |
| `dependent.parent_home_paid` | `household.unmarried` | no | form | 1 |
| `dependent.ptc_files` | `sa.dependent` | no | form, order | 1 |
| `dependent.work_ssn` | `sa.dependent` | no | form, order | 1 |
| `div.box12` | `ssb.benefits` | no | child | 1 |
| `div.box9` | `div.box13` | no | child | 1 |
| `div.box9` | `sd.distributions` | no | child | 1 |
| `f1040.tax_exempt_interest` | `person.eic_ssn` | no | form | 1 |
| `f1040.tax_exempt_interest` | `ssb.benefits` | no | form | 1 |
| `f1095a.b_counted` | `f8962.estimate_100` | no | form, order | 1 |
| `f1095a.c_total` | `f1040.tax_exempt_interest` | no | form, order | 1 |
| `f1095a.mo_a` | `f1040.tax_exempt_interest` | no | form, order | 1 |
| `f8962.alien_below` | `f1040.tax_exempt_interest` | no | form, order | 1 |
| `ftc.carryover` | `s3.foreign_any` | yes | form | 1 |
| `ftc.carryover` | `s3.prior_other_forms` | yes | form | 1 |
| `household.credit_disallowed` | `person.sav_trad` | no | child, form, order | 1 |
| `household.credit_disallowed` | `f1040.tax_exempt_interest` | no | child, form, order | 1 |
| `household.home_cost` | `dependent.parent_home_paid` | no | form | 1 |
| `household.married` | `f8889.line2` | no | form, order | 1 |
| `person.eic_ssn` | `dependent.eic_ssn` | no | form | 1 |
| `person.itin_applied` | `person.tin` | no | order | 1 |
| `person.sav_born` | `f1095a.in_a_sep` | no | form | 1 |
| `qbi.carryforward` | `person.sav_claimed` | no | order | 1 |
| `qbi.carryforward` | `f1040.tax_exempt_interest` | no | order | 1 |
| `qbi.dividends` | `f1040.line3a` | no | form | 1 |
| `qbi.unsupported` | `person.sav_claimed` | no | form, order | 1 |
| `qbi.unsupported` | `f1040.tax_exempt_interest` | no | form, order | 1 |
| `s8812.combat_pay` | `person.eic_ssn` | no | form, order | 1 |
| `sales.code` | `sales.route` | no | order | 1 |
| `sb.unsupported` | `sd.distributions` | no | form | 1 |
| `w2.box12_any` | `person.sav_student` | no | form | 1 |

## Delayed children for the sorting cause

By child and parent, with the number of walks.

| child | place | parent | place | walks |
|---|---|---|---|---|
| `sa.charity_limited` | order 10 | `sa.gifts` | order 5 | 12 |
| `sa.line11` | order 10 | `sa.gifts` | order 5 | 12 |
| `sb.ordinary_dividends` | order 10 | `div.any` | order 10 | 11 |
| `sd.distributions` | order 10 | `div.any` | order 10 | 10 |
| `div.box13` | order 15 | `div.any` | order 10 | 8 |
| `div.box12` | order 30 | `div.any` | order 10 | 1 |
| `s3.section960c` | order 10 | `s3.foreign_any` | order 10 | 1 |
| `s3.section965` | order 10 | `s3.foreign_any` | order 10 | 1 |
| `s3.virgin_islands` | order 10 | `s3.foreign_any` | order 10 | 1 |

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

**stage5.return.owed**: 107 questions, complete; order re-entries 4, form re-entries 7 sorting and 5 late, delayed children 3 sorting and 3 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 1:sales×1 · 2:dependent×1 · 2:household×3 · 2:person×1 · 2:s3×1 · 5:w2×1 · 3:w2×6 · 4:w2×8 · 8:interest×1 · 9:f8889×1 · 10:oi8z×1 · 10:div×1 · 10:f1040×3 · 10:f4952×2 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:interest×2 · 10:person×4 · 10:refund×1 · 10:s1×10 · 10:s1a×3 · 10:s2×2 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×1 · 5:sa×1 · 10:sa×7 · 10:sb×2 · 10:f1040×1 · 10:qbi×1 · 10:sb×1 · 10:sd×3 · 10:sli×1 · 10:ssb×1 · 11:sc×1 · 12:s179×1 · 15:div×5 · 20:f2441×2 · 22:person×1 · 10:qbi×1 · 12:qbi×1 · 24:f5695×2

- order 5 re-entered at step 76 by `sa.gifts` (order 5), left after step 15, 60 between. Late: reachable only after the answer to `sa.elect_itemize` (step 75), which its gate does not read.
- order 10 re-entered at step 77 by `sa.excluded_income` (order 10), left after step 75, 1 between. Late: left for `sa.gifts` (order 5), which sorts earlier and was reachable only after the answer to `sa.elect_itemize` (step 75), which its gate does not read.
- order 10 re-entered at step 104 by `qbi.unsupported` (order 10), left after step 93, 10 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 103), which its gate does not read.
- order 12 re-entered at step 105 by `qbi.carryforward` (order 12), left after step 95, 9 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 103), which its gate does not read.
- form person re-entered at step 13 by `person[taxpayer].under16` (order 2), left after step 1, 11 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form f1040 re-entered at step 34 by `f1040.line25b` (order 10), left after step 2, 31 between. Sorting: it was reachable (since step 1), and `scope.other_income` was asked instead (the bank puts order 0 first).
- form interest re-entered at step 42 by `interest[bank_a].amount` (order 10), left after step 30, 11 between. Sorting: it was reachable (since step 31), and `$f8889@person[taxpayer]` was asked instead (the bank puts order 9 seq 1 first).
- form person re-entered at step 44 by `person[taxpayer].age65` (order 10), left after step 13, 30 between. Sorting: it was reachable (since step 2), and `s3.adoption_any` was asked instead (the bank puts order 2 first).
- form s3 re-entered at step 64 by `s3.credit_bond` (order 10), left after step 14, 49 between. Sorting: it was reachable (since step 1), and `$w2@person[taxpayer]` was asked instead (the bank puts order 5 first).
- form person re-entered at step 74 by `person[taxpayer].blind` (order 10), left after step 47, 26 between. Late: reachable only after the answer to `sa.dependent` (step 73), which its gate does not read.
- form sa re-entered at step 75 by `sa.elect_itemize` (order 10), left after step 73, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 73), which its gate does not read.
- form f1040 re-entered at step 86 by `f1040.line3a` (order 10), left after step 36, 49 between. Late: reachable only after the answer to `sb.ordinary_dividends` (step 85), which its gate does not read.
- form sb re-entered at step 88 by `sb.unsupported` (order 10), left after step 85, 2 between. Late: left for `f1040.line3a` (order 10), which sorts earlier and was reachable only after the answer to `sb.ordinary_dividends` (step 85), which its gate does not read.
- form div re-entered at step 96 by `div.box13` (order 15), left after step 33, 62 between. Sorting: it was reachable (since step 34), and `f1040.line25b` was asked instead (the bank puts order 10 first).
- form person re-entered at step 103 by `person[taxpayer].sav_trad` (order 22), left after step 74, 28 between. Sorting: it was reachable (since step 2), and `sa.elect_itemize` was asked instead (the bank puts order 10 first).
- form qbi re-entered at step 104 by `qbi.unsupported` (order 10), left after step 87, 16 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 103), which its gate does not read.
- `sb.ordinary_dividends` (order 10), step 85: child of `div.any` (step 33), 51 other questions between. Sorting: it was reachable (since step 34), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `sd.distributions` (order 10), step 90: child of `div.any` (step 33), 55 other questions between. Sorting: it was reachable (since step 34), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `div.box13` (order 15), step 96: child of `div.any` (step 33), 60 other questions between. Sorting: it was reachable (since step 34), and `f1040.line25b` was asked instead (the bank puts order 10 first).
- `div.box10` (order 15), step 97: child of `div.any` (step 33), 60 other questions between. Late: reachable only after the answer to `div.box13` (step 96), which its gate does not read.
- `div.box3` (order 15), step 99: child of `div.any` (step 33), 61 other questions between. Late: reachable only after the answer to `div.box13` (step 96), which its gate does not read.
- `div.box9` (order 15), step 100: child of `div.any` (step 33), 61 other questions between. Late: reachable only after the answer to `div.box13` (step 96), which its gate does not read.

**stage5.return.refund**: 86 questions, complete; order re-entries 4, form re-entries 5 sorting and 2 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 1:sales×1 · 2:dependent×1 · 2:household×3 · 2:person×1 · 2:s3×1 · 5:w2×1 · 3:w2×3 · 4:w2×2 · 8:interest×1 · 9:f8889×1 · 10:oi8z×1 · 10:div×1 · 10:f1040×3 · 10:f4952×2 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:person×4 · 10:refund×1 · 10:s1×10 · 10:s1a×3 · 10:s2×2 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×1 · 5:sa×1 · 10:sa×7 · 10:sb×1 · 10:sd×2 · 10:sli×1 · 10:ssb×1 · 11:sc×1 · 12:s179×1 · 20:f2441×2 · 22:person×1 · 10:qbi×1 · 12:qbi×1 · 24:f5695×2

- order 5 re-entered at step 65 by `sa.gifts` (order 5), left after step 15, 49 between. Late: reachable only after the answer to `sa.elect_itemize` (step 64), which its gate does not read.
- order 10 re-entered at step 66 by `sa.excluded_income` (order 10), left after step 64, 1 between. Late: left for `sa.gifts` (order 5), which sorts earlier and was reachable only after the answer to `sa.elect_itemize` (step 64), which its gate does not read.
- order 10 re-entered at step 83 by `qbi.unsupported` (order 10), left after step 77, 5 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 82), which its gate does not read.
- order 12 re-entered at step 84 by `qbi.carryforward` (order 12), left after step 79, 4 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 82), which its gate does not read.
- form person re-entered at step 13 by `person[taxpayer].under16` (order 2), left after step 1, 11 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form f1040 re-entered at step 25 by `f1040.line25b` (order 10), left after step 2, 22 between. Sorting: it was reachable (since step 1), and `scope.other_income` was asked instead (the bank puts order 0 first).
- form person re-entered at step 33 by `person[taxpayer].age65` (order 10), left after step 13, 19 between. Sorting: it was reachable (since step 2), and `s3.adoption_any` was asked instead (the bank puts order 2 first).
- form s3 re-entered at step 53 by `s3.credit_bond` (order 10), left after step 14, 38 between. Sorting: it was reachable (since step 1), and `$w2@person[taxpayer]` was asked instead (the bank puts order 5 first).
- form person re-entered at step 63 by `person[taxpayer].blind` (order 10), left after step 36, 26 between. Late: reachable only after the answer to `sa.dependent` (step 62), which its gate does not read.
- form sa re-entered at step 64 by `sa.elect_itemize` (order 10), left after step 62, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 62), which its gate does not read.
- form person re-entered at step 82 by `person[taxpayer].sav_trad` (order 22), left after step 63, 18 between. Sorting: it was reachable (since step 2), and `sa.elect_itemize` was asked instead (the bank puts order 10 first).

**stage5.return.itemized**: 122 questions, complete; order re-entries 7, form re-entries 10 sorting and 8 late, delayed children 5 sorting and 3 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 1:sales×1 · 2:dependent×1 · 2:household×3 · 2:person×1 · 2:s3×1 · 2:sales×1 · 3:sales×1 · 4:sales×1 · 5:w2×1 · 3:w2×3 · 4:w2×2 · 5:sales×1 · 8:interest×1 · 9:f8889×1 · 10:oi8z×1 · 10:div×1 · 10:f1040×3 · 10:f4952×6 · 10:f8863×1 · 10:f8959×1 · 10:ftc×5 · 10:interest×2 · 10:person×4 · 10:refund×1 · 10:s1×10 · 10:s1a×3 · 10:s2×2 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×1 · 5:sa×1 · 5:gift×1 · 10:gift×2 · 10:sa×8 · 10:s3×1 · 10:sa×1 · 10:sales×2 · 10:sb×2 · 10:f1040×1 · 10:qbi×1 · 10:sb×1 · 10:sd×3 · 10:sli×1 · 10:ssb×1 · 11:sc×1 · 12:s179×1 · 15:div×9 · 20:f2441×2 · 22:person×1 · 10:qbi×1 · 12:qbi×1 · 24:f5695×2

- order 3 re-entered at step 19 by `person[taxpayer].w2[emp_a].box1` (order 3), left after step 16, 2 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 18), its parent or roster.
- order 4 re-entered at step 22 by `person[taxpayer].w2[emp_a].box5` (order 4), left after step 17, 4 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 18), its parent or roster.
- order 5 re-entered at step 24 by `sales[s1].route` (order 5), left after step 18, 5 between. Sorting: left for `person[taxpayer].w2[emp_a].box1` (order 3), a child of the question before it, which the bank places in another order number.
- order 5 re-entered at step 79 by `sa.gifts` (order 5), left after step 24, 54 between. Late: reachable only after the answer to `sa.elect_itemize` (step 78), which its gate does not read.
- order 10 re-entered at step 81 by `gift[books].deduction` (order 10), left after step 78, 2 between. Late: reachable only after the answer to `$gift` (step 80), its parent or roster.
- order 10 re-entered at step 119 by `qbi.unsupported` (order 10), left after step 104, 14 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 118), which its gate does not read.
- order 12 re-entered at step 120 by `qbi.carryforward` (order 12), left after step 106, 13 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 118), which its gate does not read.
- form person re-entered at step 13 by `person[taxpayer].under16` (order 2), left after step 1, 11 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form sales re-entered at step 15 by `sales[s1].box` (order 2), left after step 8, 6 between. Sorting: it was reachable (since step 9), and `$dependent` was asked instead (within order 2, sorted by id).
- form sales re-entered at step 24 by `sales[s1].route` (order 5), left after step 17, 6 between. Sorting: it was reachable (since step 9), and `$w2@person[taxpayer]` was asked instead (within order 5, sorted by id).
- form f1040 re-entered at step 29 by `f1040.line25b` (order 10), left after step 2, 26 between. Sorting: it was reachable (since step 1), and `scope.other_income` was asked instead (the bank puts order 0 first).
- form interest re-entered at step 45 by `interest[bank_a].amount` (order 10), left after step 25, 19 between. Sorting: it was reachable (since step 26), and `$f8889@person[taxpayer]` was asked instead (the bank puts order 9 seq 1 first).
- form person re-entered at step 47 by `person[taxpayer].age65` (order 10), left after step 13, 33 between. Sorting: it was reachable (since step 2), and `s3.adoption_any` was asked instead (the bank puts order 2 first).
- form s3 re-entered at step 67 by `s3.credit_bond` (order 10), left after step 14, 52 between. Sorting: it was reachable (since step 1), and `sales[s1].box` was asked instead (the bank puts order 2 first).
- form person re-entered at step 77 by `person[taxpayer].blind` (order 10), left after step 50, 26 between. Late: reachable only after the answer to `sa.dependent` (step 76), which its gate does not read.
- form sa re-entered at step 78 by `sa.elect_itemize` (order 10), left after step 76, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 76), which its gate does not read.
- form sa re-entered at step 83 by `sa.charity_limited` (order 10), left after step 79, 3 between. Late: left for `$gift` (order 5), which sorts earlier and was reachable only after the answer to `sa.gifts` (step 79), which its gate does not read.
- form s3 re-entered at step 91 by `s3.mcc` (order 10), left after step 75, 15 between. Late: reachable only after the answer to `sa.line8a` (step 90), which its gate does not read.
- form sa re-entered at step 92 by `sa.unsupported` (order 10), left after step 90, 1 between. Late: left for `s3.mcc` (order 10), which sorts earlier and was reachable only after the answer to `sa.line8a` (step 90), which its gate does not read.
- form sales re-entered at step 93 by `sales[s1].proceeds` (order 10), left after step 24, 68 between. Sorting: it was reachable (since step 25), and `$interest` was asked instead (the bank puts order 8 first).
- form f1040 re-entered at step 97 by `f1040.line3a` (order 10), left after step 31, 65 between. Late: reachable only after the answer to `sb.ordinary_dividends` (step 96), which its gate does not read.
- form sb re-entered at step 99 by `sb.unsupported` (order 10), left after step 96, 2 between. Late: left for `f1040.line3a` (order 10), which sorts earlier and was reachable only after the answer to `sb.ordinary_dividends` (step 96), which its gate does not read.
- form div re-entered at step 107 by `div.box13` (order 15), left after step 28, 78 between. Sorting: it was reachable (since step 29), and `f1040.line25b` was asked instead (the bank puts order 10 first).
- form person re-entered at step 118 by `person[taxpayer].sav_trad` (order 22), left after step 77, 40 between. Sorting: it was reachable (since step 2), and `sa.elect_itemize` was asked instead (the bank puts order 10 first).
- form qbi re-entered at step 119 by `qbi.unsupported` (order 10), left after step 98, 20 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 118), which its gate does not read.
- `sa.charity_limited` (order 10), step 83: child of `sa.gifts` (step 79), 3 other questions between. Sorting: it was reachable (since step 80), and `$gift` was asked instead (the bank puts order 5 first).
- `sa.line11` (order 10), step 86: child of `sa.gifts` (step 79), 5 other questions between. Sorting: it was reachable (since step 80), and `$gift` was asked instead (the bank puts order 5 first).
- `sb.ordinary_dividends` (order 10), step 96: child of `div.any` (step 28), 67 other questions between. Sorting: it was reachable (since step 29), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `sd.distributions` (order 10), step 101: child of `div.any` (step 28), 71 other questions between. Sorting: it was reachable (since step 29), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `div.box13` (order 15), step 107: child of `div.any` (step 28), 76 other questions between. Sorting: it was reachable (since step 29), and `f1040.line25b` was asked instead (the bank puts order 10 first).
- `div.box10` (order 15), step 110: child of `div.any` (step 28), 78 other questions between. Late: reachable only after the answer to `div.box2c` (step 109), which its gate does not read.
- `div.box3` (order 15), step 114: child of `div.any` (step 28), 81 other questions between. Late: reachable only after the answer to `div.box2c` (step 109), which its gate does not read.
- `div.box9` (order 15), step 115: child of `div.any` (step 28), 81 other questions between. Late: reachable only after the answer to `div.box2c` (step 109), which its gate does not read.

**stage5.refuse.screens**: 5 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3

**stage5.refuse.other_income**: 5 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3

**stage5.return.refund_f4952_screens_unused**: 86 questions, complete; order re-entries 4, form re-entries 5 sorting and 2 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 1:sales×1 · 2:dependent×1 · 2:household×3 · 2:person×1 · 2:s3×1 · 5:w2×1 · 3:w2×3 · 4:w2×2 · 8:interest×1 · 9:f8889×1 · 10:oi8z×1 · 10:div×1 · 10:f1040×3 · 10:f4952×2 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:person×4 · 10:refund×1 · 10:s1×10 · 10:s1a×3 · 10:s2×2 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×1 · 5:sa×1 · 10:sa×7 · 10:sb×1 · 10:sd×2 · 10:sli×1 · 10:ssb×1 · 11:sc×1 · 12:s179×1 · 20:f2441×2 · 22:person×1 · 10:qbi×1 · 12:qbi×1 · 24:f5695×2

- order 5 re-entered at step 65 by `sa.gifts` (order 5), left after step 15, 49 between. Late: reachable only after the answer to `sa.elect_itemize` (step 64), which its gate does not read.
- order 10 re-entered at step 66 by `sa.excluded_income` (order 10), left after step 64, 1 between. Late: left for `sa.gifts` (order 5), which sorts earlier and was reachable only after the answer to `sa.elect_itemize` (step 64), which its gate does not read.
- order 10 re-entered at step 83 by `qbi.unsupported` (order 10), left after step 77, 5 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 82), which its gate does not read.
- order 12 re-entered at step 84 by `qbi.carryforward` (order 12), left after step 79, 4 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 82), which its gate does not read.
- form person re-entered at step 13 by `person[taxpayer].under16` (order 2), left after step 1, 11 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form f1040 re-entered at step 25 by `f1040.line25b` (order 10), left after step 2, 22 between. Sorting: it was reachable (since step 1), and `scope.other_income` was asked instead (the bank puts order 0 first).
- form person re-entered at step 33 by `person[taxpayer].age65` (order 10), left after step 13, 19 between. Sorting: it was reachable (since step 2), and `s3.adoption_any` was asked instead (the bank puts order 2 first).
- form s3 re-entered at step 53 by `s3.credit_bond` (order 10), left after step 14, 38 between. Sorting: it was reachable (since step 1), and `$w2@person[taxpayer]` was asked instead (the bank puts order 5 first).
- form person re-entered at step 63 by `person[taxpayer].blind` (order 10), left after step 36, 26 between. Late: reachable only after the answer to `sa.dependent` (step 62), which its gate does not read.
- form sa re-entered at step 64 by `sa.elect_itemize` (order 10), left after step 62, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 62), which its gate does not read.
- form person re-entered at step 82 by `person[taxpayer].sav_trad` (order 22), left after step 63, 18 between. Sorting: it was reachable (since step 2), and `sa.elect_itemize` was asked instead (the bank puts order 10 first).

**stage5.return.refund_f8960_unsupported_unused**: 86 questions, complete; order re-entries 4, form re-entries 5 sorting and 2 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 1:sales×1 · 2:dependent×1 · 2:household×3 · 2:person×1 · 2:s3×1 · 5:w2×1 · 3:w2×3 · 4:w2×2 · 8:interest×1 · 9:f8889×1 · 10:oi8z×1 · 10:div×1 · 10:f1040×3 · 10:f4952×2 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:person×4 · 10:refund×1 · 10:s1×10 · 10:s1a×3 · 10:s2×2 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×1 · 5:sa×1 · 10:sa×7 · 10:sb×1 · 10:sd×2 · 10:sli×1 · 10:ssb×1 · 11:sc×1 · 12:s179×1 · 20:f2441×2 · 22:person×1 · 10:qbi×1 · 12:qbi×1 · 24:f5695×2

- order 5 re-entered at step 65 by `sa.gifts` (order 5), left after step 15, 49 between. Late: reachable only after the answer to `sa.elect_itemize` (step 64), which its gate does not read.
- order 10 re-entered at step 66 by `sa.excluded_income` (order 10), left after step 64, 1 between. Late: left for `sa.gifts` (order 5), which sorts earlier and was reachable only after the answer to `sa.elect_itemize` (step 64), which its gate does not read.
- order 10 re-entered at step 83 by `qbi.unsupported` (order 10), left after step 77, 5 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 82), which its gate does not read.
- order 12 re-entered at step 84 by `qbi.carryforward` (order 12), left after step 79, 4 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 82), which its gate does not read.
- form person re-entered at step 13 by `person[taxpayer].under16` (order 2), left after step 1, 11 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form f1040 re-entered at step 25 by `f1040.line25b` (order 10), left after step 2, 22 between. Sorting: it was reachable (since step 1), and `scope.other_income` was asked instead (the bank puts order 0 first).
- form person re-entered at step 33 by `person[taxpayer].age65` (order 10), left after step 13, 19 between. Sorting: it was reachable (since step 2), and `s3.adoption_any` was asked instead (the bank puts order 2 first).
- form s3 re-entered at step 53 by `s3.credit_bond` (order 10), left after step 14, 38 between. Sorting: it was reachable (since step 1), and `$w2@person[taxpayer]` was asked instead (the bank puts order 5 first).
- form person re-entered at step 63 by `person[taxpayer].blind` (order 10), left after step 36, 26 between. Late: reachable only after the answer to `sa.dependent` (step 62), which its gate does not read.
- form sa re-entered at step 64 by `sa.elect_itemize` (order 10), left after step 62, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 62), which its gate does not read.
- form person re-entered at step 82 by `person[taxpayer].sav_trad` (order 22), left after step 63, 18 between. Sorting: it was reachable (since step 2), and `sa.elect_itemize` was asked instead (the bank puts order 10 first).

**stage5.return.f8960_unsupported_agi_at_threshold**: 86 questions, complete; order re-entries 4, form re-entries 5 sorting and 2 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 1:sales×1 · 2:dependent×1 · 2:household×3 · 2:person×1 · 2:s3×1 · 5:w2×1 · 3:w2×3 · 4:w2×2 · 8:interest×1 · 9:f8889×1 · 10:oi8z×1 · 10:div×1 · 10:f1040×3 · 10:f4952×2 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:person×4 · 10:refund×1 · 10:s1×10 · 10:s1a×3 · 10:s2×2 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×1 · 5:sa×1 · 10:sa×7 · 10:sb×1 · 10:sd×2 · 10:sli×1 · 10:ssb×1 · 11:sc×1 · 12:s179×1 · 20:f2441×2 · 22:person×1 · 10:qbi×1 · 12:qbi×1 · 24:f5695×2

- order 5 re-entered at step 65 by `sa.gifts` (order 5), left after step 15, 49 between. Late: reachable only after the answer to `sa.elect_itemize` (step 64), which its gate does not read.
- order 10 re-entered at step 66 by `sa.excluded_income` (order 10), left after step 64, 1 between. Late: left for `sa.gifts` (order 5), which sorts earlier and was reachable only after the answer to `sa.elect_itemize` (step 64), which its gate does not read.
- order 10 re-entered at step 83 by `qbi.unsupported` (order 10), left after step 77, 5 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 82), which its gate does not read.
- order 12 re-entered at step 84 by `qbi.carryforward` (order 12), left after step 79, 4 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 82), which its gate does not read.
- form person re-entered at step 13 by `person[taxpayer].under16` (order 2), left after step 1, 11 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form f1040 re-entered at step 25 by `f1040.line25b` (order 10), left after step 2, 22 between. Sorting: it was reachable (since step 1), and `scope.other_income` was asked instead (the bank puts order 0 first).
- form person re-entered at step 33 by `person[taxpayer].age65` (order 10), left after step 13, 19 between. Sorting: it was reachable (since step 2), and `s3.adoption_any` was asked instead (the bank puts order 2 first).
- form s3 re-entered at step 53 by `s3.credit_bond` (order 10), left after step 14, 38 between. Sorting: it was reachable (since step 1), and `$w2@person[taxpayer]` was asked instead (the bank puts order 5 first).
- form person re-entered at step 63 by `person[taxpayer].blind` (order 10), left after step 36, 26 between. Late: reachable only after the answer to `sa.dependent` (step 62), which its gate does not read.
- form sa re-entered at step 64 by `sa.elect_itemize` (order 10), left after step 62, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 62), which its gate does not read.
- form person re-entered at step 82 by `person[taxpayer].sav_trad` (order 22), left after step 63, 18 between. Sorting: it was reachable (since step 2), and `sa.elect_itemize` was asked instead (the bank puts order 10 first).

**stage5.return.refund_f8960_refund_unused**: 86 questions, complete; order re-entries 4, form re-entries 5 sorting and 2 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 1:sales×1 · 2:dependent×1 · 2:household×3 · 2:person×1 · 2:s3×1 · 5:w2×1 · 3:w2×3 · 4:w2×2 · 8:interest×1 · 9:f8889×1 · 10:oi8z×1 · 10:div×1 · 10:f1040×3 · 10:f4952×2 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:person×4 · 10:refund×1 · 10:s1×10 · 10:s1a×3 · 10:s2×2 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×1 · 5:sa×1 · 10:sa×7 · 10:sb×1 · 10:sd×2 · 10:sli×1 · 10:ssb×1 · 11:sc×1 · 12:s179×1 · 20:f2441×2 · 22:person×1 · 10:qbi×1 · 12:qbi×1 · 24:f5695×2

- order 5 re-entered at step 65 by `sa.gifts` (order 5), left after step 15, 49 between. Late: reachable only after the answer to `sa.elect_itemize` (step 64), which its gate does not read.
- order 10 re-entered at step 66 by `sa.excluded_income` (order 10), left after step 64, 1 between. Late: left for `sa.gifts` (order 5), which sorts earlier and was reachable only after the answer to `sa.elect_itemize` (step 64), which its gate does not read.
- order 10 re-entered at step 83 by `qbi.unsupported` (order 10), left after step 77, 5 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 82), which its gate does not read.
- order 12 re-entered at step 84 by `qbi.carryforward` (order 12), left after step 79, 4 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 82), which its gate does not read.
- form person re-entered at step 13 by `person[taxpayer].under16` (order 2), left after step 1, 11 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form f1040 re-entered at step 25 by `f1040.line25b` (order 10), left after step 2, 22 between. Sorting: it was reachable (since step 1), and `scope.other_income` was asked instead (the bank puts order 0 first).
- form person re-entered at step 33 by `person[taxpayer].age65` (order 10), left after step 13, 19 between. Sorting: it was reachable (since step 2), and `s3.adoption_any` was asked instead (the bank puts order 2 first).
- form s3 re-entered at step 53 by `s3.credit_bond` (order 10), left after step 14, 38 between. Sorting: it was reachable (since step 1), and `$w2@person[taxpayer]` was asked instead (the bank puts order 5 first).
- form person re-entered at step 63 by `person[taxpayer].blind` (order 10), left after step 36, 26 between. Late: reachable only after the answer to `sa.dependent` (step 62), which its gate does not read.
- form sa re-entered at step 64 by `sa.elect_itemize` (order 10), left after step 62, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 62), which its gate does not read.
- form person re-entered at step 82 by `person[taxpayer].sav_trad` (order 22), left after step 63, 18 between. Sorting: it was reachable (since step 2), and `sa.elect_itemize` was asked instead (the bank puts order 10 first).

**stage5.return.refund_combat_pay_no_children**: 86 questions, complete; order re-entries 4, form re-entries 5 sorting and 2 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 1:sales×1 · 2:dependent×1 · 2:household×3 · 2:person×1 · 2:s3×1 · 5:w2×1 · 3:w2×3 · 4:w2×2 · 8:interest×1 · 9:f8889×1 · 10:oi8z×1 · 10:div×1 · 10:f1040×3 · 10:f4952×2 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:person×4 · 10:refund×1 · 10:s1×10 · 10:s1a×3 · 10:s2×2 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×1 · 5:sa×1 · 10:sa×7 · 10:sb×1 · 10:sd×2 · 10:sli×1 · 10:ssb×1 · 11:sc×1 · 12:s179×1 · 20:f2441×2 · 22:person×1 · 10:qbi×1 · 12:qbi×1 · 24:f5695×2

- order 5 re-entered at step 65 by `sa.gifts` (order 5), left after step 15, 49 between. Late: reachable only after the answer to `sa.elect_itemize` (step 64), which its gate does not read.
- order 10 re-entered at step 66 by `sa.excluded_income` (order 10), left after step 64, 1 between. Late: left for `sa.gifts` (order 5), which sorts earlier and was reachable only after the answer to `sa.elect_itemize` (step 64), which its gate does not read.
- order 10 re-entered at step 83 by `qbi.unsupported` (order 10), left after step 77, 5 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 82), which its gate does not read.
- order 12 re-entered at step 84 by `qbi.carryforward` (order 12), left after step 79, 4 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 82), which its gate does not read.
- form person re-entered at step 13 by `person[taxpayer].under16` (order 2), left after step 1, 11 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form f1040 re-entered at step 25 by `f1040.line25b` (order 10), left after step 2, 22 between. Sorting: it was reachable (since step 1), and `scope.other_income` was asked instead (the bank puts order 0 first).
- form person re-entered at step 33 by `person[taxpayer].age65` (order 10), left after step 13, 19 between. Sorting: it was reachable (since step 2), and `s3.adoption_any` was asked instead (the bank puts order 2 first).
- form s3 re-entered at step 53 by `s3.credit_bond` (order 10), left after step 14, 38 between. Sorting: it was reachable (since step 1), and `$w2@person[taxpayer]` was asked instead (the bank puts order 5 first).
- form person re-entered at step 63 by `person[taxpayer].blind` (order 10), left after step 36, 26 between. Late: reachable only after the answer to `sa.dependent` (step 62), which its gate does not read.
- form sa re-entered at step 64 by `sa.elect_itemize` (order 10), left after step 62, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 62), which its gate does not read.
- form person re-entered at step 82 by `person[taxpayer].sav_trad` (order 22), left after step 63, 18 between. Sorting: it was reachable (since step 2), and `sa.elect_itemize` was asked instead (the bank puts order 10 first).

**stage5.return.itemized_f8960_allocation_unused**: 122 questions, complete; order re-entries 7, form re-entries 10 sorting and 8 late, delayed children 5 sorting and 3 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 1:sales×1 · 2:dependent×1 · 2:household×3 · 2:person×1 · 2:s3×1 · 2:sales×1 · 3:sales×1 · 4:sales×1 · 5:w2×1 · 3:w2×3 · 4:w2×2 · 5:sales×1 · 8:interest×1 · 9:f8889×1 · 10:oi8z×1 · 10:div×1 · 10:f1040×3 · 10:f4952×6 · 10:f8863×1 · 10:f8959×1 · 10:ftc×5 · 10:interest×2 · 10:person×4 · 10:refund×1 · 10:s1×10 · 10:s1a×3 · 10:s2×2 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×1 · 5:sa×1 · 5:gift×1 · 10:gift×2 · 10:sa×8 · 10:s3×1 · 10:sa×1 · 10:sales×2 · 10:sb×2 · 10:f1040×1 · 10:qbi×1 · 10:sb×1 · 10:sd×3 · 10:sli×1 · 10:ssb×1 · 11:sc×1 · 12:s179×1 · 15:div×9 · 20:f2441×2 · 22:person×1 · 10:qbi×1 · 12:qbi×1 · 24:f5695×2

- order 3 re-entered at step 19 by `person[taxpayer].w2[emp_a].box1` (order 3), left after step 16, 2 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 18), its parent or roster.
- order 4 re-entered at step 22 by `person[taxpayer].w2[emp_a].box5` (order 4), left after step 17, 4 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 18), its parent or roster.
- order 5 re-entered at step 24 by `sales[s1].route` (order 5), left after step 18, 5 between. Sorting: left for `person[taxpayer].w2[emp_a].box1` (order 3), a child of the question before it, which the bank places in another order number.
- order 5 re-entered at step 79 by `sa.gifts` (order 5), left after step 24, 54 between. Late: reachable only after the answer to `sa.elect_itemize` (step 78), which its gate does not read.
- order 10 re-entered at step 81 by `gift[books].deduction` (order 10), left after step 78, 2 between. Late: reachable only after the answer to `$gift` (step 80), its parent or roster.
- order 10 re-entered at step 119 by `qbi.unsupported` (order 10), left after step 104, 14 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 118), which its gate does not read.
- order 12 re-entered at step 120 by `qbi.carryforward` (order 12), left after step 106, 13 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 118), which its gate does not read.
- form person re-entered at step 13 by `person[taxpayer].under16` (order 2), left after step 1, 11 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form sales re-entered at step 15 by `sales[s1].box` (order 2), left after step 8, 6 between. Sorting: it was reachable (since step 9), and `$dependent` was asked instead (within order 2, sorted by id).
- form sales re-entered at step 24 by `sales[s1].route` (order 5), left after step 17, 6 between. Sorting: it was reachable (since step 9), and `$w2@person[taxpayer]` was asked instead (within order 5, sorted by id).
- form f1040 re-entered at step 29 by `f1040.line25b` (order 10), left after step 2, 26 between. Sorting: it was reachable (since step 1), and `scope.other_income` was asked instead (the bank puts order 0 first).
- form interest re-entered at step 45 by `interest[bank_a].amount` (order 10), left after step 25, 19 between. Sorting: it was reachable (since step 26), and `$f8889@person[taxpayer]` was asked instead (the bank puts order 9 seq 1 first).
- form person re-entered at step 47 by `person[taxpayer].age65` (order 10), left after step 13, 33 between. Sorting: it was reachable (since step 2), and `s3.adoption_any` was asked instead (the bank puts order 2 first).
- form s3 re-entered at step 67 by `s3.credit_bond` (order 10), left after step 14, 52 between. Sorting: it was reachable (since step 1), and `sales[s1].box` was asked instead (the bank puts order 2 first).
- form person re-entered at step 77 by `person[taxpayer].blind` (order 10), left after step 50, 26 between. Late: reachable only after the answer to `sa.dependent` (step 76), which its gate does not read.
- form sa re-entered at step 78 by `sa.elect_itemize` (order 10), left after step 76, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 76), which its gate does not read.
- form sa re-entered at step 83 by `sa.charity_limited` (order 10), left after step 79, 3 between. Late: left for `$gift` (order 5), which sorts earlier and was reachable only after the answer to `sa.gifts` (step 79), which its gate does not read.
- form s3 re-entered at step 91 by `s3.mcc` (order 10), left after step 75, 15 between. Late: reachable only after the answer to `sa.line8a` (step 90), which its gate does not read.
- form sa re-entered at step 92 by `sa.unsupported` (order 10), left after step 90, 1 between. Late: left for `s3.mcc` (order 10), which sorts earlier and was reachable only after the answer to `sa.line8a` (step 90), which its gate does not read.
- form sales re-entered at step 93 by `sales[s1].proceeds` (order 10), left after step 24, 68 between. Sorting: it was reachable (since step 25), and `$interest` was asked instead (the bank puts order 8 first).
- form f1040 re-entered at step 97 by `f1040.line3a` (order 10), left after step 31, 65 between. Late: reachable only after the answer to `sb.ordinary_dividends` (step 96), which its gate does not read.
- form sb re-entered at step 99 by `sb.unsupported` (order 10), left after step 96, 2 between. Late: left for `f1040.line3a` (order 10), which sorts earlier and was reachable only after the answer to `sb.ordinary_dividends` (step 96), which its gate does not read.
- form div re-entered at step 107 by `div.box13` (order 15), left after step 28, 78 between. Sorting: it was reachable (since step 29), and `f1040.line25b` was asked instead (the bank puts order 10 first).
- form person re-entered at step 118 by `person[taxpayer].sav_trad` (order 22), left after step 77, 40 between. Sorting: it was reachable (since step 2), and `sa.elect_itemize` was asked instead (the bank puts order 10 first).
- form qbi re-entered at step 119 by `qbi.unsupported` (order 10), left after step 98, 20 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 118), which its gate does not read.
- `sa.charity_limited` (order 10), step 83: child of `sa.gifts` (step 79), 3 other questions between. Sorting: it was reachable (since step 80), and `$gift` was asked instead (the bank puts order 5 first).
- `sa.line11` (order 10), step 86: child of `sa.gifts` (step 79), 5 other questions between. Sorting: it was reachable (since step 80), and `$gift` was asked instead (the bank puts order 5 first).
- `sb.ordinary_dividends` (order 10), step 96: child of `div.any` (step 28), 67 other questions between. Sorting: it was reachable (since step 29), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `sd.distributions` (order 10), step 101: child of `div.any` (step 28), 71 other questions between. Sorting: it was reachable (since step 29), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `div.box13` (order 15), step 107: child of `div.any` (step 28), 76 other questions between. Sorting: it was reachable (since step 29), and `f1040.line25b` was asked instead (the bank puts order 10 first).
- `div.box10` (order 15), step 110: child of `div.any` (step 28), 78 other questions between. Late: reachable only after the answer to `div.box2c` (step 109), which its gate does not read.
- `div.box3` (order 15), step 114: child of `div.any` (step 28), 81 other questions between. Late: reachable only after the answer to `div.box2c` (step 109), which its gate does not read.
- `div.box9` (order 15), step 115: child of `div.any` (step 28), 81 other questions between. Late: reachable only after the answer to `div.box2c` (step 109), which its gate does not read.

### generated returns

**generated.0**: 121 questions, complete; order re-entries 5, form re-entries 6 sorting and 9 late, delayed children 2 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 1:sales×1 · 2:dependent×1 · 2:household×3 · 2:person×1 · 2:s3×1 · 5:w2×1 · 3:w2×3 · 4:w2×2 · 8:interest×1 · 9:f8889×13 · 10:oi8z×1 · 10:div×1 · 10:f1040×3 · 10:f4952×6 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:interest×2 · 10:person×4 · 10:refund×1 · 10:s1×10 · 10:s1a×3 · 10:s2×2 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×1 · 5:sa×1 · 5:gift×1 · 10:gift×4 · 10:sa×8 · 10:s3×1 · 10:sa×1 · 10:sb×2 · 10:sd×2 · 10:sli×1 · 10:ssb×1 · 11:sc×1 · 12:s179×1 · 20:f2441×2 · 22:person×1 · 10:qbi×1 · 12:qbi×1 · 24:f5695×2 · 30:person×1 · 30:f1040×1 · 30:eic×1 · 30:person×2 · 30:eic×2 · 20:s8812×1

- order 5 re-entered at step 83 by `sa.gifts` (order 5), left after step 15, 67 between. Late: reachable only after the answer to `sa.elect_itemize` (step 82), which its gate does not read.
- order 10 re-entered at step 85 by `gift[item_a].deduction` (order 10), left after step 82, 2 between. Late: reachable only after the answer to `$gift` (step 84), its parent or roster.
- order 10 re-entered at step 110 by `qbi.unsupported` (order 10), left after step 104, 5 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 109), which its gate does not read.
- order 12 re-entered at step 111 by `qbi.carryforward` (order 12), left after step 106, 4 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 109), which its gate does not read.
- order 20 re-entered at step 121 by `s8812.combat_pay` (order 20), left after step 108, 12 between. Late: reachable only after the answer to `eic.qc_of_another` (step 120), which its gate does not read.
- form person re-entered at step 13 by `person[taxpayer].under16` (order 2), left after step 1, 11 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form f1040 re-entered at step 37 by `f1040.line25b` (order 10), left after step 2, 34 between. Sorting: it was reachable (since step 1), and `scope.other_income` was asked instead (the bank puts order 0 first).
- form interest re-entered at step 49 by `interest[bank_a].amount` (order 10), left after step 21, 27 between. Sorting: it was reachable (since step 22), and `$f8889@person[taxpayer]` was asked instead (the bank puts order 9 seq 1 first).
- form person re-entered at step 51 by `person[taxpayer].age65` (order 10), left after step 13, 37 between. Sorting: it was reachable (since step 2), and `s3.adoption_any` was asked instead (the bank puts order 2 first).
- form s3 re-entered at step 71 by `s3.credit_bond` (order 10), left after step 14, 56 between. Sorting: it was reachable (since step 1), and `$w2@person[taxpayer]` was asked instead (the bank puts order 5 first).
- form person re-entered at step 81 by `person[taxpayer].blind` (order 10), left after step 54, 26 between. Late: reachable only after the answer to `sa.dependent` (step 80), which its gate does not read.
- form sa re-entered at step 82 by `sa.elect_itemize` (order 10), left after step 80, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 80), which its gate does not read.
- form sa re-entered at step 89 by `sa.charity_limited` (order 10), left after step 83, 5 between. Late: left for `$gift` (order 5), which sorts earlier and was reachable only after the answer to `sa.gifts` (step 83), which its gate does not read.
- form s3 re-entered at step 97 by `s3.mcc` (order 10), left after step 79, 17 between. Late: reachable only after the answer to `sa.line8a` (step 96), which its gate does not read.
- form sa re-entered at step 98 by `sa.unsupported` (order 10), left after step 96, 1 between. Late: left for `s3.mcc` (order 10), which sorts earlier and was reachable only after the answer to `sa.line8a` (step 96), which its gate does not read.
- form person re-entered at step 109 by `person[taxpayer].sav_trad` (order 22), left after step 81, 27 between. Sorting: it was reachable (since step 2), and `sa.elect_itemize` was asked instead (the bank puts order 10 first).
- form person re-entered at step 114 by `person[taxpayer].eic_ssn` (order 30), left after step 109, 4 between. Late: left for `qbi.unsupported` (order 10), which sorts earlier and was reachable only after the answer to `person[taxpayer].sav_trad` (step 109), which its gate does not read.
- form f1040 re-entered at step 115 by `f1040.tax_exempt_interest` (order 30), left after step 39, 75 between. Late: reachable only after the answer to `person[taxpayer].eic_ssn` (step 114), which its gate does not read.
- form person re-entered at step 117 by `person[taxpayer].born_after_1960` (order 30), left after step 114, 2 between. Late: reachable only after the answer to `eic.died_2025` (step 116), which its gate does not read.
- form eic re-entered at step 119 by `eic.us_home` (order 30), left after step 116, 2 between. Late: reachable only after the answer to `person[taxpayer].born_before_2001` (step 118), which its gate does not read.
- `sa.charity_limited` (order 10), step 89: child of `sa.gifts` (step 83), 5 other questions between. Sorting: it was reachable (since step 84), and `$gift` was asked instead (the bank puts order 5 first).
- `sa.line11` (order 10), step 92: child of `sa.gifts` (step 83), 7 other questions between. Sorting: it was reachable (since step 84), and `$gift` was asked instead (the bank puts order 5 first).

**generated.1**: 47 questions, refused; order re-entries 0, form re-entries 1 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 1:sales×1 · 2:dependent×31 · 2:f1095a×3 · 2:household×5

- form f1095a re-entered at step 40 by `f1095a[mkt_a].uniform` (order 2), left after step 6, 33 between. Sorting: it was reachable (since step 7), and `$retirement@person[taxpayer]` was asked instead (the bank puts order 1 first).

**generated.2**: 2 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1

**generated.3**: 2 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1

**generated.4**: 141 questions, complete; order re-entries 7, form re-entries 11 sorting and 6 late, delayed children 5 sorting and 3 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 1:sales×1 · 2:dependent×1 · 2:household×3 · 2:person×1 · 2:s3×1 · 2:sales×2 · 3:sales×2 · 4:sales×2 · 5:w2×1 · 3:w2×3 · 4:w2×2 · 5:sales×2 · 8:interest×1 · 9:f8889×13 · 10:oi8z×1 · 10:div×1 · 10:f1040×3 · 10:f4952×2 · 10:f8863×1 · 10:f8959×1 · 10:ftc×5 · 10:interest×4 · 10:person×4 · 10:refund×1 · 10:s1×10 · 10:s1a×3 · 10:s2×2 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×1 · 5:sa×1 · 5:gift×1 · 10:gift×2 · 10:sa×9 · 10:sales×7 · 10:sb×2 · 10:f1040×1 · 10:qbi×1 · 10:sb×1 · 10:sd×3 · 10:sli×1 · 10:ssb×1 · 11:sc×1 · 12:s179×1 · 15:div×9 · 20:f2441×2 · 22:person×1 · 24:f5695×2 · 25:person×1 · 10:qbi×1 · 12:qbi×1

- order 3 re-entered at step 22 by `person[taxpayer].w2[emp_a].box1` (order 3), left after step 18, 3 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 21), its parent or roster.
- order 4 re-entered at step 25 by `person[taxpayer].w2[emp_a].box5` (order 4), left after step 20, 4 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 21), its parent or roster.
- order 5 re-entered at step 27 by `sales[s1].route` (order 5), left after step 21, 5 between. Sorting: left for `person[taxpayer].w2[emp_a].box1` (order 3), a child of the question before it, which the bank places in another order number.
- order 5 re-entered at step 93 by `sa.gifts` (order 5), left after step 28, 64 between. Late: reachable only after the answer to `sa.elect_itemize` (step 92), which its gate does not read.
- order 10 re-entered at step 95 by `gift[item_a].deduction` (order 10), left after step 92, 2 between. Late: reachable only after the answer to `$gift` (step 94), its parent or roster.
- order 10 re-entered at step 140 by `qbi.unsupported` (order 10), left after step 122, 17 between. Late: reachable only after the answer to `person[taxpayer].sav_claimed` (step 139), which its gate does not read.
- order 12 re-entered at step 141 by `qbi.carryforward` (order 12), left after step 124, 16 between. Late: reachable only after the answer to `person[taxpayer].sav_claimed` (step 139), which its gate does not read.
- form person re-entered at step 13 by `person[taxpayer].under16` (order 2), left after step 1, 11 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form sales re-entered at step 15 by `sales[s1].box` (order 2), left after step 8, 6 between. Sorting: it was reachable (since step 9), and `$dependent` was asked instead (within order 2, sorted by id).
- form sales re-entered at step 27 by `sales[s1].route` (order 5), left after step 20, 6 between. Sorting: it was reachable (since step 9), and `$w2@person[taxpayer]` was asked instead (within order 5, sorted by id).
- form f1040 re-entered at step 45 by `f1040.line25b` (order 10), left after step 2, 42 between. Sorting: it was reachable (since step 1), and `scope.other_income` was asked instead (the bank puts order 0 first).
- form interest re-entered at step 57 by `interest[bank_a].amount` (order 10), left after step 29, 27 between. Sorting: it was reachable (since step 30), and `$f8889@person[taxpayer]` was asked instead (the bank puts order 9 seq 1 first).
- form person re-entered at step 61 by `person[taxpayer].age65` (order 10), left after step 13, 47 between. Sorting: it was reachable (since step 2), and `s3.adoption_any` was asked instead (the bank puts order 2 first).
- form s3 re-entered at step 81 by `s3.credit_bond` (order 10), left after step 14, 66 between. Sorting: it was reachable (since step 1), and `sales[s1].box` was asked instead (the bank puts order 2 first).
- form person re-entered at step 91 by `person[taxpayer].blind` (order 10), left after step 64, 26 between. Late: reachable only after the answer to `sa.dependent` (step 90), which its gate does not read.
- form sa re-entered at step 92 by `sa.elect_itemize` (order 10), left after step 90, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 90), which its gate does not read.
- form sa re-entered at step 97 by `sa.charity_limited` (order 10), left after step 93, 3 between. Late: left for `$gift` (order 5), which sorts earlier and was reachable only after the answer to `sa.gifts` (step 93), which its gate does not read.
- form sales re-entered at step 106 by `sales[s1].correct_basis` (order 10), left after step 28, 77 between. Sorting: it was reachable (since step 28), and `$interest` was asked instead (the bank puts order 8 first).
- form f1040 re-entered at step 115 by `f1040.line3a` (order 10), left after step 47, 67 between. Late: reachable only after the answer to `sb.ordinary_dividends` (step 114), which its gate does not read.
- form sb re-entered at step 117 by `sb.unsupported` (order 10), left after step 114, 2 between. Late: left for `f1040.line3a` (order 10), which sorts earlier and was reachable only after the answer to `sb.ordinary_dividends` (step 114), which its gate does not read.
- form div re-entered at step 125 by `div.box13` (order 15), left after step 44, 80 between. Sorting: it was reachable (since step 45), and `f1040.line25b` was asked instead (the bank puts order 10 first).
- form person re-entered at step 136 by `person[taxpayer].sav_trad` (order 22), left after step 91, 44 between. Sorting: it was reachable (since step 2), and `sa.elect_itemize` was asked instead (the bank puts order 10 first).
- form person re-entered at step 139 by `person[taxpayer].sav_claimed` (order 25), left after step 136, 2 between. Sorting: it was reachable (since step 122), and `f5695.part1_any` was asked instead (the bank puts order 24 first).
- form qbi re-entered at step 140 by `qbi.unsupported` (order 10), left after step 116, 23 between. Late: reachable only after the answer to `person[taxpayer].sav_claimed` (step 139), which its gate does not read.
- `sa.charity_limited` (order 10), step 97: child of `sa.gifts` (step 93), 3 other questions between. Sorting: it was reachable (since step 94), and `$gift` was asked instead (the bank puts order 5 first).
- `sa.line11` (order 10), step 100: child of `sa.gifts` (step 93), 5 other questions between. Sorting: it was reachable (since step 94), and `$gift` was asked instead (the bank puts order 5 first).
- `sb.ordinary_dividends` (order 10), step 114: child of `div.any` (step 44), 69 other questions between. Sorting: it was reachable (since step 45), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `sd.distributions` (order 10), step 119: child of `div.any` (step 44), 73 other questions between. Sorting: it was reachable (since step 45), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `div.box13` (order 15), step 125: child of `div.any` (step 44), 78 other questions between. Sorting: it was reachable (since step 45), and `f1040.line25b` was asked instead (the bank puts order 10 first).
- `div.box10` (order 15), step 128: child of `div.any` (step 44), 80 other questions between. Late: reachable only after the answer to `div.box2c` (step 127), which its gate does not read.
- `div.box3` (order 15), step 132: child of `div.any` (step 44), 83 other questions between. Late: reachable only after the answer to `div.box2c` (step 127), which its gate does not read.
- `div.box9` (order 15), step 133: child of `div.any` (step 44), 83 other questions between. Late: reachable only after the answer to `div.box2c` (step 127), which its gate does not read.

**generated.5**: 23 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 1:sales×1 · 2:dependent×10 · 2:household×5

**generated.6**: 172 questions, complete; order re-entries 9, form re-entries 8 sorting and 12 late, delayed children 2 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 1:sales×1 · 2:dependent×1 · 2:f1095a×28 · 2:household×3 · 2:person×1 · 2:s3×1 · 5:w2×1 · 3:w2×3 · 4:w2×2 · 8:interest×1 · 9:f8889×13 · 10:oi8z×1 · 10:div×1 · 10:f1040×3 · 10:f4952×6 · 10:f8863×1 · 10:f8959×1 · 10:f8962×5 · 10:ftc×1 · 10:person×4 · 10:refund×1 · 10:s1×10 · 10:s1a×3 · 10:s2×2 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×1 · 5:sa×1 · 5:gift×1 · 10:sa×8 · 10:s3×1 · 10:sa×1 · 10:sb×1 · 10:sd×2 · 10:sli×1 · 10:ssb×1 · 11:sc×1 · 12:s179×1 · 20:f2441×2 · 22:person×1 · 10:qbi×1 · 12:qbi×1 · 24:f5695×2 · 30:f1040×1 · 2:f1095a×1 · 11:f8962×2 · 2:f1095a×16 · 25:person×5 · 25:w2×1 · 30:person×1 · 30:eic×1 · 30:person×2 · 30:eic×2 · 20:s8812×1

- order 5 re-entered at step 114 by `sa.gifts` (order 5), left after step 43, 70 between. Late: reachable only after the answer to `sa.elect_itemize` (step 113), which its gate does not read.
- order 10 re-entered at step 116 by `sa.charity_limited` (order 10), left after step 113, 2 between. Late: reachable only after the answer to `sa.gifts` (step 114), its parent or roster.
- order 10 re-entered at step 136 by `qbi.unsupported` (order 10), left after step 130, 5 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 135), which its gate does not read.
- order 12 re-entered at step 137 by `qbi.carryforward` (order 12), left after step 132, 4 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 135), which its gate does not read.
- order 2 re-entered at step 141 by `f1095a[mkt_a].c_total` (order 2), left after step 42, 98 between. Late: reachable only after the answer to `f1040.tax_exempt_interest` (step 140), which its gate does not read.
- order 11 re-entered at step 142 by `f8962.alien_below` (order 11), left after step 131, 10 between. Late: reachable only after the answer to `f1040.tax_exempt_interest` (step 140), which its gate does not read.
- order 2 re-entered at step 144 by `f1095a[mkt_a].b_counted` (order 2), left after step 141, 2 between. Late: reachable only after the answer to `f8962.estimate_100` (step 143), which its gate does not read.
- order 30 re-entered at step 166 by `person[taxpayer].eic_ssn` (order 30), left after step 140, 25 between. Late: left for `f1095a[mkt_a].c_total` (order 2), which sorts earlier and was reachable only after the answer to `f1040.tax_exempt_interest` (step 140), which its gate does not read.
- order 20 re-entered at step 172 by `s8812.combat_pay` (order 20), left after step 134, 37 between. Late: reachable only after the answer to `eic.qc_of_another` (step 171), which its gate does not read.
- form f1095a re-entered at step 10 by `f1095a[mkt_a].uniform` (order 2), left after step 6, 3 between. Sorting: it was reachable (since step 7), and `$retirement@person[taxpayer]` was asked instead (the bank puts order 1 first).
- form person re-entered at step 41 by `person[taxpayer].under16` (order 2), left after step 1, 39 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form f1040 re-entered at step 65 by `f1040.line25b` (order 10), left after step 2, 62 between. Sorting: it was reachable (since step 1), and `scope.other_income` was asked instead (the bank puts order 0 first).
- form person re-entered at step 82 by `person[taxpayer].age65` (order 10), left after step 41, 40 between. Sorting: it was reachable (since step 2), and `s3.adoption_any` was asked instead (the bank puts order 2 first).
- form s3 re-entered at step 102 by `s3.credit_bond` (order 10), left after step 42, 59 between. Sorting: it was reachable (since step 1), and `$w2@person[taxpayer]` was asked instead (the bank puts order 5 first).
- form person re-entered at step 112 by `person[taxpayer].blind` (order 10), left after step 85, 26 between. Late: reachable only after the answer to `sa.dependent` (step 111), which its gate does not read.
- form sa re-entered at step 113 by `sa.elect_itemize` (order 10), left after step 111, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 111), which its gate does not read.
- form sa re-entered at step 116 by `sa.charity_limited` (order 10), left after step 114, 1 between. Late: left for `$gift` (order 5), which sorts earlier and was reachable only after the answer to `sa.gifts` (step 114), which its gate does not read.
- form s3 re-entered at step 124 by `s3.mcc` (order 10), left after step 110, 13 between. Late: reachable only after the answer to `sa.line8a` (step 123), which its gate does not read.
- form sa re-entered at step 125 by `sa.unsupported` (order 10), left after step 123, 1 between. Late: left for `s3.mcc` (order 10), which sorts earlier and was reachable only after the answer to `sa.line8a` (step 123), which its gate does not read.
- form person re-entered at step 135 by `person[taxpayer].sav_trad` (order 22), left after step 112, 22 between. Sorting: it was reachable (since step 2), and `sa.elect_itemize` was asked instead (the bank puts order 10 first).
- form f1040 re-entered at step 140 by `f1040.tax_exempt_interest` (order 30), left after step 67, 72 between. Sorting: it was reachable (since step 7), and `f4952.has_interest` was asked instead (the bank puts order 10 first).
- form f1095a re-entered at step 141 by `f1095a[mkt_a].c_total` (order 2), left after step 37, 103 between. Late: reachable only after the answer to `f1040.tax_exempt_interest` (step 140), which its gate does not read.
- form f8962 re-entered at step 142 by `f8962.alien_below` (order 11), left after step 80, 61 between. Late: reachable only after the answer to `f1040.tax_exempt_interest` (step 140), which its gate does not read.
- form f1095a re-entered at step 144 by `f1095a[mkt_a].b_counted` (order 2), left after step 141, 2 between. Late: reachable only after the answer to `f8962.estimate_100` (step 143), which its gate does not read.
- form person re-entered at step 160 by `person[taxpayer].sav_born` (order 25), left after step 135, 24 between. Late: reachable only after the answer to `f1095a[mkt_b].in_a_sep` (step 159), which its gate does not read.
- form w2 re-entered at step 165 by `person[taxpayer].w2[emp_a].box12_any` (order 25), left after step 48, 116 between. Late: reachable only after the answer to `person[taxpayer].sav_student` (step 161), which its gate does not read.
- form person re-entered at step 166 by `person[taxpayer].eic_ssn` (order 30), left after step 164, 1 between. Sorting: it was reachable (since step 136), and `person[taxpayer].w2[emp_a].box12_any` was asked instead (the bank puts order 25 first).
- form person re-entered at step 168 by `person[taxpayer].born_after_1960` (order 30), left after step 166, 1 between. Late: reachable only after the answer to `eic.died_2025` (step 167), which its gate does not read.
- form eic re-entered at step 170 by `eic.us_home` (order 30), left after step 167, 2 between. Late: reachable only after the answer to `person[taxpayer].born_before_2001` (step 169), which its gate does not read.
- `sa.charity_limited` (order 10), step 116: child of `sa.gifts` (step 114), 1 other question between. Sorting: it was reachable (since step 115), and `$gift` was asked instead (the bank puts order 5 first).
- `sa.line11` (order 10), step 119: child of `sa.gifts` (step 114), 3 other questions between. Sorting: it was reachable (since step 115), and `$gift` was asked instead (the bank puts order 5 first).

**generated.7**: 4 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:scope×3

**generated.8**: 2 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1

**generated.9**: 4 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×2

**generated.10**: 202 questions, refused; order re-entries 7, form re-entries 13 sorting and 6 late, delayed children 4 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 1:sales×1 · 2:dependent×9 · 2:household×3 · 2:person×1 · 2:s3×1 · 2:sales×3 · 3:dependent×2 · 2:dependent×2 · 3:sales×3 · 4:sales×3 · 5:w2×1 · 3:w2×6 · 4:w2×8 · 5:sales×3 · 8:interest×1 · 9:f8889×13 · 10:oi8z×1 · 10:div×1 · 10:f1040×3 · 10:f4952×2 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:interest×2 · 10:person×4 · 10:refund×1 · 10:s1×10 · 10:s1a×3 · 10:s2×2 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×1 · 5:sa×1 · 5:gift×1 · 10:gift×4 · 10:sa×8 · 10:s3×1 · 10:sa×1 · 10:sales×8 · 10:sb×3 · 10:sd×3 · 10:sli×1 · 10:ssb×1 · 11:sc×1 · 11:asset×1 · 11:scveh×1 · 12:person×1 · 12:asset×10 · 12:sc×38 · 12:scveh×7

- order 2 re-entered at step 28 by `dependent[dep_a].gross_income` (order 2), left after step 25, 2 between. Late: reachable only after the answer to `dependent[dep_a].qr_all_year` (step 27), which its gate does not read.
- order 3 re-entered at step 30 by `sales[s1].special` (order 3), left after step 27, 2 between. Late: left for `dependent[dep_a].gross_income` (order 2), which sorts earlier and was reachable only after the answer to `dependent[dep_a].qr_all_year` (step 27), which its gate does not read.
- order 3 re-entered at step 37 by `person[taxpayer].w2[emp_a].box1` (order 3), left after step 32, 4 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 36), its parent or roster.
- order 4 re-entered at step 43 by `person[taxpayer].w2[emp_a].box3` (order 4), left after step 35, 7 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 36), its parent or roster.
- order 5 re-entered at step 51 by `sales[s1].route` (order 5), left after step 36, 14 between. Sorting: left for `person[taxpayer].w2[emp_a].box1` (order 3), a child of the question before it, which the bank places in another order number.
- order 5 re-entered at step 112 by `sa.gifts` (order 5), left after step 53, 58 between. Late: reachable only after the answer to `sa.elect_itemize` (step 111), which its gate does not read.
- order 10 re-entered at step 114 by `gift[item_a].deduction` (order 10), left after step 111, 2 between. Late: reachable only after the answer to `$gift` (step 113), its parent or roster.
- form person re-entered at step 21 by `person[taxpayer].under16` (order 2), left after step 1, 19 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form sales re-entered at step 23 by `sales[s1].box` (order 2), left after step 8, 14 between. Sorting: it was reachable (since step 9), and `$dependent` was asked instead (within order 2, sorted by id).
- form dependent re-entered at step 26 by `dependent[dep_a].lawful` (order 3), left after step 17, 8 between. Sorting: it was reachable (since step 18), and `household.community_property` was asked instead (the bank puts order 2 first).
- form sales re-entered at step 30 by `sales[s1].special` (order 3), left after step 25, 4 between. Sorting: it was reachable (since step 9), and `dependent[dep_a].lawful` was asked instead (within order 3, sorted by id).
- form sales re-entered at step 51 by `sales[s1].route` (order 5), left after step 35, 15 between. Sorting: it was reachable (since step 9), and `$w2@person[taxpayer]` was asked instead (within order 5, sorted by id).
- form f1040 re-entered at step 70 by `f1040.line25b` (order 10), left after step 2, 67 between. Sorting: it was reachable (since step 1), and `scope.other_income` was asked instead (the bank puts order 0 first).
- form interest re-entered at step 78 by `interest[bank_a].amount` (order 10), left after step 54, 23 between. Sorting: it was reachable (since step 55), and `$f8889@person[taxpayer]` was asked instead (the bank puts order 9 seq 1 first).
- form person re-entered at step 80 by `person[taxpayer].age65` (order 10), left after step 21, 58 between. Sorting: it was reachable (since step 2), and `s3.adoption_any` was asked instead (the bank puts order 2 first).
- form s3 re-entered at step 100 by `s3.credit_bond` (order 10), left after step 22, 77 between. Sorting: it was reachable (since step 1), and `sales[s1].box` was asked instead (the bank puts order 2 first).
- form person re-entered at step 110 by `person[taxpayer].blind` (order 10), left after step 83, 26 between. Late: reachable only after the answer to `sa.dependent` (step 109), which its gate does not read.
- form sa re-entered at step 111 by `sa.elect_itemize` (order 10), left after step 109, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 109), which its gate does not read.
- form sa re-entered at step 118 by `sa.charity_limited` (order 10), left after step 112, 5 between. Late: left for `$gift` (order 5), which sorts earlier and was reachable only after the answer to `sa.gifts` (step 112), which its gate does not read.
- form s3 re-entered at step 126 by `s3.mcc` (order 10), left after step 108, 17 between. Late: reachable only after the answer to `sa.line8a` (step 125), which its gate does not read.
- form sa re-entered at step 127 by `sa.unsupported` (order 10), left after step 125, 1 between. Late: left for `s3.mcc` (order 10), which sorts earlier and was reachable only after the answer to `sa.line8a` (step 125), which its gate does not read.
- form sales re-entered at step 128 by `sales[s1].proceeds` (order 10), left after step 53, 74 between. Sorting: it was reachable (since step 52), and `$interest` was asked instead (the bank puts order 8 first).
- form person re-entered at step 147 by `person[taxpayer].plan` (order 12), left after step 110, 36 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 144), which its gate does not read.
- form asset re-entered at step 148 by `person[taxpayer].sc[biz_a].asset[item_1].class` (order 12), left after step 145, 2 between. Sorting: it was reachable (since step 146), and `$scveh@person[taxpayer].sc[biz_a]` was asked instead (the bank puts order 11 first).
- form sc re-entered at step 158 by `person[taxpayer].sc[biz_a].business_credit` (order 12), left after step 144, 13 between. Sorting: left for `$asset@person[taxpayer].sc[biz_a]` (order 11), a child of the question before it, which the bank places in another form.
- form scveh re-entered at step 196 by `person[taxpayer].sc[biz_a].scveh[car_1].method` (order 12), left after step 146, 49 between. Sorting: it was reachable (since step 147), and `person[taxpayer].plan` was asked instead (within order 12, sorted by id).
- `sa.charity_limited` (order 10), step 118: child of `sa.gifts` (step 112), 5 other questions between. Sorting: it was reachable (since step 113), and `$gift` was asked instead (the bank puts order 5 first).
- `sa.line11` (order 10), step 121: child of `sa.gifts` (step 112), 7 other questions between. Sorting: it was reachable (since step 113), and `$gift` was asked instead (the bank puts order 5 first).
- `sb.ordinary_dividends` (order 10), step 137: child of `div.any` (step 69), 67 other questions between. Sorting: it was reachable (since step 70), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `sd.distributions` (order 10), step 140: child of `div.any` (step 69), 69 other questions between. Sorting: it was reachable (since step 70), and `f1040.line25b` was asked instead (within order 10, sorted by id).

**generated.11**: 27 questions, refused; order re-entries 0, form re-entries 0 sorting and 2 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 1:sales×1 · 2:dependent×13 · 2:household×4 · 2:dependent×1 · 2:household×1

- form dependent re-entered at step 26 by `dependent[dep_a].parent_home_paid` (order 2), left after step 21, 4 between. Late: reachable only after the answer to `household.unmarried` (step 25), which its gate does not read.
- form household re-entered at step 27 by `household.home_cost` (order 2), left after step 25, 1 between. Late: reachable only after the answer to `dependent[dep_a].parent_home_paid` (step 26), which its gate does not read.

**generated.12**: 187 questions, complete; order re-entries 13, form re-entries 13 sorting and 12 late, delayed children 6 sorting and 4 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 1:sales×1 · 2:dependent×33 · 2:f1095a×3 · 2:household×2 · 2:person×1 · 2:s3×1 · 2:sales×1 · 3:dependent×1 · 2:dependent×4 · 3:sales×1 · 4:sales×1 · 5:w2×1 · 3:w2×6 · 4:w2×8 · 5:sales×1 · 8:interest×1 · 9:f8889×13 · 10:oi8z×1 · 10:div×1 · 10:f1040×3 · 10:f4952×2 · 10:f8863×1 · 10:f8959×1 · 10:f8962×4 · 10:ftc×1 · 10:person×4 · 10:refund×1 · 10:s1×10 · 10:s1a×3 · 10:s2×2 · 10:s3×9 · 10:sa×1 · 2:dependent×3 · 2:person×2 · 10:person×1 · 10:sa×1 · 5:sa×1 · 5:gift×1 · 10:sa×8 · 10:s3×1 · 10:sa×1 · 10:sales×4 · 10:sb×2 · 10:f1040×1 · 10:qbi×1 · 10:sb×1 · 10:sd×3 · 10:sli×1 · 10:ssb×1 · 11:sc×1 · 12:s179×1 · 15:div×9 · 20:f2441×2 · 20:s8812×1 · 22:person×1 · 10:qbi×1 · 12:qbi×1 · 20:household×1 · 24:f5695×2 · 30:div×1 · 30:f1040×1 · 2:f1095a×2

- order 2 re-entered at step 51 by `dependent[dep_a].gross_income` (order 2), left after step 49, 1 between. Late: reachable only after the answer to `dependent[dep_a].qr_all_year` (step 50), which its gate does not read.
- order 3 re-entered at step 55 by `sales[s1].special` (order 3), left after step 50, 4 between. Late: left for `dependent[dep_a].gross_income` (order 2), which sorts earlier and was reachable only after the answer to `dependent[dep_a].qr_all_year` (step 50), which its gate does not read.
- order 3 re-entered at step 58 by `person[taxpayer].w2[emp_a].box1` (order 3), left after step 55, 2 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 57), its parent or roster.
- order 4 re-entered at step 64 by `person[taxpayer].w2[emp_a].box3` (order 4), left after step 56, 7 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 57), its parent or roster.
- order 5 re-entered at step 72 by `sales[s1].route` (order 5), left after step 57, 14 between. Sorting: left for `person[taxpayer].w2[emp_a].box1` (order 3), a child of the question before it, which the bank places in another order number.
- order 2 re-entered at step 131 by `dependent[dep_b].ptc_files` (order 2), left after step 54, 76 between. Late: reachable only after the answer to `sa.dependent` (step 130), which its gate does not read.
- order 10 re-entered at step 136 by `person[taxpayer].blind` (order 10), left after step 130, 5 between. Late: left for `dependent[dep_b].ptc_files` (order 2), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 130), which its gate does not read.
- order 5 re-entered at step 138 by `sa.gifts` (order 5), left after step 72, 65 between. Late: reachable only after the answer to `sa.elect_itemize` (step 137), which its gate does not read.
- order 10 re-entered at step 140 by `sa.charity_limited` (order 10), left after step 137, 2 between. Late: reachable only after the answer to `sa.gifts` (step 138), its parent or roster.
- order 10 re-entered at step 179 by `qbi.unsupported` (order 10), left after step 163, 15 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 178), which its gate does not read.
- order 12 re-entered at step 180 by `qbi.carryforward` (order 12), left after step 165, 14 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 178), which its gate does not read.
- order 20 re-entered at step 181 by `household.credit_disallowed` (order 20), left after step 177, 3 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 178), which its gate does not read.
- order 2 re-entered at step 186 by `f1095a[mkt_a].mo_a` (order 2), left after step 135, 50 between. Late: reachable only after the answer to `f1040.tax_exempt_interest` (step 185), which its gate does not read.
- form f1095a re-entered at step 42 by `f1095a[mkt_a].uniform` (order 2), left after step 6, 35 between. Sorting: it was reachable (since step 7), and `$retirement@person[taxpayer]` was asked instead (the bank puts order 1 first).
- form person re-entered at step 47 by `person[taxpayer].under16` (order 2), left after step 1, 45 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form sales re-entered at step 49 by `sales[s1].box` (order 2), left after step 8, 40 between. Sorting: it was reachable (since step 9), and `$dependent` was asked instead (within order 2, sorted by id).
- form dependent re-entered at step 50 by `dependent[dep_a].qr_all_year` (order 3), left after step 41, 8 between. Sorting: it was reachable (since step 14), and `f1095a[mkt_a].uniform` was asked instead (the bank puts order 2 first).
- form sales re-entered at step 55 by `sales[s1].special` (order 3), left after step 49, 5 between. Sorting: it was reachable (since step 9), and `dependent[dep_a].qr_all_year` was asked instead (within order 3, sorted by id).
- form sales re-entered at step 72 by `sales[s1].route` (order 5), left after step 56, 15 between. Sorting: it was reachable (since step 9), and `$w2@person[taxpayer]` was asked instead (within order 5, sorted by id).
- form f1040 re-entered at step 89 by `f1040.line25b` (order 10), left after step 2, 86 between. Sorting: it was reachable (since step 1), and `scope.other_income` was asked instead (the bank puts order 0 first).
- form person re-entered at step 101 by `person[taxpayer].age65` (order 10), left after step 47, 53 between. Sorting: it was reachable (since step 2), and `s3.adoption_any` was asked instead (the bank puts order 2 first).
- form s3 re-entered at step 121 by `s3.credit_bond` (order 10), left after step 48, 72 between. Sorting: it was reachable (since step 1), and `sales[s1].box` was asked instead (the bank puts order 2 first).
- form dependent re-entered at step 131 by `dependent[dep_b].ptc_files` (order 2), left after step 54, 76 between. Late: reachable only after the answer to `sa.dependent` (step 130), which its gate does not read.
- form person re-entered at step 134 by `person[taxpayer].tin` (order 2), left after step 104, 29 between. Late: reachable only after the answer to `sa.dependent` (step 130), which its gate does not read.
- form sa re-entered at step 137 by `sa.elect_itemize` (order 10), left after step 130, 6 between. Late: left for `dependent[dep_b].ptc_files` (order 2), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 130), which its gate does not read.
- form sa re-entered at step 140 by `sa.charity_limited` (order 10), left after step 138, 1 between. Late: left for `$gift` (order 5), which sorts earlier and was reachable only after the answer to `sa.gifts` (step 138), which its gate does not read.
- form s3 re-entered at step 148 by `s3.mcc` (order 10), left after step 129, 18 between. Late: reachable only after the answer to `sa.line8a` (step 147), which its gate does not read.
- form sa re-entered at step 149 by `sa.unsupported` (order 10), left after step 147, 1 between. Late: left for `s3.mcc` (order 10), which sorts earlier and was reachable only after the answer to `sa.line8a` (step 147), which its gate does not read.
- form sales re-entered at step 150 by `sales[s1].correct_basis` (order 10), left after step 72, 77 between. Sorting: it was reachable (since step 73), and `$interest` was asked instead (the bank puts order 8 first).
- form f1040 re-entered at step 156 by `f1040.line3a` (order 10), left after step 91, 64 between. Late: reachable only after the answer to `sb.ordinary_dividends` (step 155), which its gate does not read.
- form sb re-entered at step 158 by `sb.unsupported` (order 10), left after step 155, 2 between. Late: left for `f1040.line3a` (order 10), which sorts earlier and was reachable only after the answer to `sb.ordinary_dividends` (step 155), which its gate does not read.
- form div re-entered at step 166 by `div.box13` (order 15), left after step 88, 77 between. Sorting: it was reachable (since step 89), and `f1040.line25b` was asked instead (the bank puts order 10 first).
- form person re-entered at step 178 by `person[taxpayer].sav_trad` (order 22), left after step 136, 41 between. Sorting: it was reachable (since step 2), and `sa.elect_itemize` was asked instead (the bank puts order 10 first).
- form qbi re-entered at step 179 by `qbi.unsupported` (order 10), left after step 157, 21 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 178), which its gate does not read.
- form household re-entered at step 181 by `household.credit_disallowed` (order 20), left after step 46, 134 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 178), which its gate does not read.
- form div re-entered at step 184 by `div.box12` (order 30), left after step 174, 9 between. Sorting: it was reachable (since step 89), and `f2441.benefits` was asked instead (the bank puts order 20 first).
- form f1040 re-entered at step 185 by `f1040.tax_exempt_interest` (order 30), left after step 156, 28 between. Late: left for `qbi.dividends` (order 10), which sorts earlier and was reachable only after the answer to `f1040.line3a` (step 156), which its gate does not read.
- form f1095a re-entered at step 186 by `f1095a[mkt_a].mo_a` (order 2), left after step 44, 141 between. Late: reachable only after the answer to `f1040.tax_exempt_interest` (step 185), which its gate does not read.
- `sa.charity_limited` (order 10), step 140: child of `sa.gifts` (step 138), 1 other question between. Sorting: it was reachable (since step 139), and `$gift` was asked instead (the bank puts order 5 first).
- `sa.line11` (order 10), step 143: child of `sa.gifts` (step 138), 3 other questions between. Sorting: it was reachable (since step 139), and `$gift` was asked instead (the bank puts order 5 first).
- `sb.ordinary_dividends` (order 10), step 155: child of `div.any` (step 88), 66 other questions between. Sorting: it was reachable (since step 89), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `sd.distributions` (order 10), step 160: child of `div.any` (step 88), 70 other questions between. Sorting: it was reachable (since step 89), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `div.box13` (order 15), step 166: child of `div.any` (step 88), 75 other questions between. Sorting: it was reachable (since step 89), and `f1040.line25b` was asked instead (the bank puts order 10 first).
- `div.box10` (order 15), step 169: child of `div.any` (step 88), 77 other questions between. Late: reachable only after the answer to `div.box2c` (step 168), which its gate does not read.
- `div.box3` (order 15), step 173: child of `div.any` (step 88), 80 other questions between. Late: reachable only after the answer to `div.box2c` (step 168), which its gate does not read.
- `div.box9` (order 15), step 174: child of `div.any` (step 88), 80 other questions between. Late: reachable only after the answer to `div.box2c` (step 168), which its gate does not read.
- `household.credit_disallowed` (order 20), step 181: child of `sa.excluded_income` (step 141), 39 other questions between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 178), which its gate does not read.
- `div.box12` (order 30), step 184: child of `div.any` (step 88), 89 other questions between. Sorting: it was reachable (since step 89), and `f1040.line25b` was asked instead (the bank puts order 10 first).

**generated.13**: 4 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×2

**generated.14**: 70 questions, refused; order re-entries 5, form re-entries 6 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 1:sales×1 · 2:dependent×10 · 2:household×2 · 2:person×1 · 2:s3×1 · 2:sales×3 · 3:dependent×2 · 2:dependent×3 · 3:sales×3 · 4:sales×3 · 5:w2×1 · 3:w2×3 · 4:w2×2 · 5:sales×3 · 8:interest×1 · 9:f8889×13 · 10:oi8z×1 · 10:div×1 · 10:f1040×3 · 10:f4952×6

- order 2 re-entered at step 28 by `dependent[dep_a].gross_income` (order 2), left after step 25, 2 between. Late: reachable only after the answer to `dependent[dep_a].qr_all_year` (step 27), which its gate does not read.
- order 3 re-entered at step 31 by `sales[s1].special` (order 3), left after step 27, 3 between. Late: left for `dependent[dep_a].gross_income` (order 2), which sorts earlier and was reachable only after the answer to `dependent[dep_a].qr_all_year` (step 27), which its gate does not read.
- order 3 re-entered at step 38 by `person[taxpayer].w2[emp_a].box1` (order 3), left after step 33, 4 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 37), its parent or roster.
- order 4 re-entered at step 41 by `person[taxpayer].w2[emp_a].box5` (order 4), left after step 36, 4 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 37), its parent or roster.
- order 5 re-entered at step 43 by `sales[s1].route` (order 5), left after step 37, 5 between. Sorting: left for `person[taxpayer].w2[emp_a].box1` (order 3), a child of the question before it, which the bank places in another order number.
- form person re-entered at step 21 by `person[taxpayer].under16` (order 2), left after step 1, 19 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form sales re-entered at step 23 by `sales[s1].box` (order 2), left after step 8, 14 between. Sorting: it was reachable (since step 9), and `$dependent` was asked instead (within order 2, sorted by id).
- form dependent re-entered at step 26 by `dependent[dep_a].lawful` (order 3), left after step 18, 7 between. Sorting: it was reachable (since step 19), and `household.community_property` was asked instead (the bank puts order 2 first).
- form sales re-entered at step 31 by `sales[s1].special` (order 3), left after step 25, 5 between. Sorting: it was reachable (since step 9), and `dependent[dep_a].lawful` was asked instead (within order 3, sorted by id).
- form sales re-entered at step 43 by `sales[s1].route` (order 5), left after step 36, 6 between. Sorting: it was reachable (since step 9), and `$w2@person[taxpayer]` was asked instead (within order 5, sorted by id).
- form f1040 re-entered at step 62 by `f1040.line25b` (order 10), left after step 2, 59 between. Sorting: it was reachable (since step 1), and `scope.other_income` was asked instead (the bank puts order 0 first).

**generated.15**: 89 questions, refused; order re-entries 2, form re-entries 4 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 1:sales×1 · 2:dependent×33 · 2:f1095a×3 · 2:household×3 · 2:person×1 · 2:s3×1 · 3:dependent×1 · 2:dependent×3 · 5:w2×1 · 3:w2×3 · 4:w2×2 · 8:interest×1 · 9:f8889×13 · 10:oi8z×1 · 10:div×1 · 10:f1040×3 · 10:f4952×4 · 10:f8863×1 · 10:f8959×1 · 10:f8962×4 · 10:ftc×1

- order 2 re-entered at step 51 by `dependent[dep_a].gross_income` (order 2), left after step 49, 1 between. Late: reachable only after the answer to `dependent[dep_a].qr_all_year` (step 50), which its gate does not read.
- order 3 re-entered at step 55 by `person[taxpayer].w2[emp_a].box1` (order 3), left after step 50, 4 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 54), its parent or roster.
- form f1095a re-entered at step 42 by `f1095a[mkt_a].uniform` (order 2), left after step 6, 35 between. Sorting: it was reachable (since step 7), and `$retirement@person[taxpayer]` was asked instead (the bank puts order 1 first).
- form person re-entered at step 48 by `person[taxpayer].under16` (order 2), left after step 1, 46 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form dependent re-entered at step 50 by `dependent[dep_a].qr_all_year` (order 3), left after step 41, 8 between. Sorting: it was reachable (since step 14), and `f1095a[mkt_a].uniform` was asked instead (the bank puts order 2 first).
- form f1040 re-entered at step 76 by `f1040.line25b` (order 10), left after step 2, 73 between. Sorting: it was reachable (since step 1), and `scope.other_income` was asked instead (the bank puts order 0 first).

**generated.16**: 2 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1

**generated.17**: 2 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1

**generated.18**: 93 questions, refused; order re-entries 3, form re-entries 3 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×2 · 1:sales×1 · 2:dependent×37 · 2:household×1 · 2:person×2 · 2:s3×1 · 2:sales×1 · 3:sales×1 · 4:sales×1 · 5:w2×2 · 3:w2×3 · 4:w2×2 · 5:sales×1 · 8:interest×1 · 9:f8889×32

- order 3 re-entered at step 55 by `person[taxpayer].w2[emp_a].box1` (order 3), left after step 51, 3 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 54), its parent or roster.
- order 4 re-entered at step 58 by `person[taxpayer].w2[emp_a].box5` (order 4), left after step 52, 5 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 54), its parent or roster.
- order 5 re-entered at step 60 by `sales[s1].route` (order 5), left after step 54, 5 between. Sorting: left for `person[taxpayer].w2[emp_a].box1` (order 3), a child of the question before it, which the bank places in another order number.
- form person re-entered at step 47 by `person[spouse].under16` (order 2), left after step 1, 45 between. Sorting: it was reachable (since step 2), and `scope.other_income` was asked instead (the bank puts order 0 first).
- form sales re-entered at step 50 by `sales[s1].box` (order 2), left after step 8, 41 between. Sorting: it was reachable (since step 9), and `$dependent` was asked instead (within order 2, sorted by id).
- form sales re-entered at step 60 by `sales[s1].route` (order 5), left after step 52, 7 between. Sorting: it was reachable (since step 9), and `$w2@person[spouse]` was asked instead (within order 5, sorted by id).

**generated.19**: 132 questions, refused; order re-entries 5, form re-entries 5 sorting and 3 late, delayed children 2 sorting and 0 late.

0:person×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×2 · 1:sales×1 · 2:dependent×1 · 2:f1095a×14 · 2:household×1 · 2:person×2 · 2:s3×1 · 5:w2×1 · 3:w2×3 · 4:w2×2 · 5:w2×1 · 3:w2×3 · 4:w2×2 · 8:interest×1 · 9:f8889×14 · 10:oi8z×1 · 10:div×1 · 10:f1040×3 · 10:f4952×6 · 10:f8863×1 · 10:f8959×1 · 10:f8962×5 · 10:ftc×1 · 10:interest×2 · 10:person×9 · 10:refund×1 · 10:s1×10 · 10:s1a×3 · 10:s2×2 · 10:s3×9 · 10:sa×1 · 10:person×2 · 10:sa×1 · 5:sa×1 · 5:gift×1 · 10:gift×4 · 10:sa×9 · 10:sb×2 · 10:sd×2

- order 5 re-entered at step 34 by `$w2@person[taxpayer]` (order 5), left after step 28, 5 between. Sorting: left for `person[spouse].w2[emp_a].box1` (order 3), a child of the question before it, which the bank places in another order number.
- order 3 re-entered at step 35 by `person[taxpayer].w2[emp_a].box1` (order 3), left after step 31, 3 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 34), its parent or roster.
- order 4 re-entered at step 38 by `person[taxpayer].w2[emp_a].box5` (order 4), left after step 33, 4 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 34), its parent or roster.
- order 5 re-entered at step 114 by `sa.gifts` (order 5), left after step 34, 79 between. Late: reachable only after the answer to `sa.elect_itemize` (step 113), which its gate does not read.
- order 10 re-entered at step 116 by `gift[item_a].deduction` (order 10), left after step 113, 2 between. Late: reachable only after the answer to `$gift` (step 115), its parent or roster.
- form f1095a re-entered at step 10 by `f1095a[mkt_a].uniform` (order 2), left after step 5, 4 between. Sorting: it was reachable (since step 6), and `$retirement@person[spouse]` was asked instead (the bank puts order 1 first).
- form person re-entered at step 25 by `person[spouse].under16` (order 2), left after step 1, 23 between. Sorting: it was reachable (since step 2), and `scope.other_income` was asked instead (the bank puts order 0 first).
- form interest re-entered at step 74 by `interest[bank_a].amount` (order 10), left after step 40, 33 between. Sorting: it was reachable (since step 41), and `$f8889@person[spouse]` was asked instead (the bank puts order 9 seq 1 first).
- form person re-entered at step 76 by `person[spouse].age65` (order 10), left after step 26, 49 between. Sorting: it was reachable (since step 2), and `s3.adoption_any` was asked instead (the bank puts order 2 first).
- form s3 re-entered at step 101 by `s3.credit_bond` (order 10), left after step 27, 73 between. Sorting: it was reachable (since step 1), and `$w2@person[spouse]` was asked instead (the bank puts order 5 first).
- form person re-entered at step 111 by `person[spouse].blind` (order 10), left after step 84, 26 between. Late: reachable only after the answer to `sa.dependent` (step 110), which its gate does not read.
- form sa re-entered at step 113 by `sa.elect_itemize` (order 10), left after step 110, 2 between. Late: left for `person[spouse].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 110), which its gate does not read.
- form sa re-entered at step 120 by `sa.charity_limited` (order 10), left after step 114, 5 between. Late: left for `$gift` (order 5), which sorts earlier and was reachable only after the answer to `sa.gifts` (step 114), which its gate does not read.
- `sa.charity_limited` (order 10), step 120: child of `sa.gifts` (step 114), 5 other questions between. Sorting: it was reachable (since step 115), and `$gift` was asked instead (the bank puts order 5 first).
- `sa.line11` (order 10), step 123: child of `sa.gifts` (step 114), 7 other questions between. Sorting: it was reachable (since step 115), and `$gift` was asked instead (the bank puts order 5 first).

**generated.20**: 166 questions, refused; order re-entries 8, form re-entries 3 sorting and 6 late, delayed children 1 sorting and 0 late.

0:person×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×2 · 1:sales×1 · 2:dependent×13 · 2:household×1 · 2:person×2 · 2:s3×1 · 5:w2×1 · 3:w2×6 · 4:w2×8 · 5:w2×1 · 3:w2×6 · 4:w2×8 · 8:interest×1 · 9:f8889×36 · 10:oi8z×1 · 10:div×1 · 10:f1040×3 · 10:f4952×6 · 10:f8863×1 · 10:f8959×1 · 10:ftc×5 · 10:person×8 · 10:refund×1 · 10:s1×10 · 10:s1a×3 · 10:s2×2 · 10:s3×9 · 10:sa×1 · 2:person×2 · 3:person×1 · 10:person×2 · 10:sa×1 · 5:sa×1 · 10:sa×6 · 10:s3×1 · 10:sa×1 · 10:sb×4 · 10:f1040×1 · 10:qbi×1 · 10:sb×1

- order 5 re-entered at step 41 by `$w2@person[taxpayer]` (order 5), left after step 26, 14 between. Sorting: left for `person[spouse].w2[emp_a].box1` (order 3), a child of the question before it, which the bank places in another order number.
- order 3 re-entered at step 42 by `person[taxpayer].w2[emp_a].box1` (order 3), left after step 32, 9 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 41), its parent or roster.
- order 4 re-entered at step 48 by `person[taxpayer].w2[emp_a].box3` (order 4), left after step 40, 7 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 41), its parent or roster.
- order 2 re-entered at step 145 by `person[spouse].tin` (order 2), left after step 25, 119 between. Late: reachable only after the answer to `sa.dependent` (step 144), which its gate does not read.
- order 3 re-entered at step 147 by `person[taxpayer].itin_applied` (order 3), left after step 47, 99 between. Late: reachable only after the answer to `person[taxpayer].tin` (step 146), which its gate does not read.
- order 10 re-entered at step 148 by `person[spouse].blind` (order 10), left after step 144, 3 between. Late: left for `person[spouse].tin` (order 2), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 144), which its gate does not read.
- order 5 re-entered at step 151 by `sa.gifts` (order 5), left after step 41, 109 between. Late: reachable only after the answer to `sa.elect_itemize` (step 150), which its gate does not read.
- order 10 re-entered at step 152 by `sa.excluded_income` (order 10), left after step 150, 1 between. Late: left for `sa.gifts` (order 5), which sorts earlier and was reachable only after the answer to `sa.elect_itemize` (step 150), which its gate does not read.
- form person re-entered at step 23 by `person[spouse].under16` (order 2), left after step 1, 21 between. Sorting: it was reachable (since step 2), and `scope.other_income` was asked instead (the bank puts order 0 first).
- form person re-entered at step 111 by `person[spouse].age65` (order 10), left after step 24, 86 between. Sorting: it was reachable (since step 2), and `s3.adoption_any` was asked instead (the bank puts order 2 first).
- form s3 re-entered at step 135 by `s3.credit_bond` (order 10), left after step 25, 109 between. Sorting: it was reachable (since step 1), and `$w2@person[spouse]` was asked instead (the bank puts order 5 first).
- form person re-entered at step 145 by `person[spouse].tin` (order 2), left after step 118, 26 between. Late: reachable only after the answer to `sa.dependent` (step 144), which its gate does not read.
- form sa re-entered at step 150 by `sa.elect_itemize` (order 10), left after step 144, 5 between. Late: left for `person[spouse].tin` (order 2), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 144), which its gate does not read.
- form s3 re-entered at step 158 by `s3.mcc` (order 10), left after step 143, 14 between. Late: reachable only after the answer to `sa.line8a` (step 157), which its gate does not read.
- form sa re-entered at step 159 by `sa.unsupported` (order 10), left after step 157, 1 between. Late: left for `s3.mcc` (order 10), which sorts earlier and was reachable only after the answer to `sa.line8a` (step 157), which its gate does not read.
- form f1040 re-entered at step 164 by `f1040.line3a` (order 10), left after step 97, 66 between. Late: reachable only after the answer to `sb.ordinary_dividends` (step 163), which its gate does not read.
- form sb re-entered at step 166 by `sb.unsupported` (order 10), left after step 163, 2 between. Late: left for `f1040.line3a` (order 10), which sorts earlier and was reachable only after the answer to `sb.ordinary_dividends` (step 163), which its gate does not read.
- `sb.ordinary_dividends` (order 10), step 163: child of `div.any` (step 94), 68 other questions between. Sorting: it was reachable (since step 95), and `f1040.line25b` was asked instead (within order 10, sorted by id).

**generated.21**: 50 questions, refused; order re-entries 5, form re-entries 5 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×2 · 1:sales×1 · 2:dependent×10 · 2:household×1 · 2:person×2 · 2:s3×1 · 2:sales×3 · 3:dependent×1 · 2:dependent×3 · 3:dependent×1 · 3:sales×3 · 4:sales×3 · 5:w2×2 · 3:w2×3 · 4:w2×2 · 5:sales×3 · 8:interest×1 · 9:f8889×3

- order 2 re-entered at step 27 by `dependent[dep_a].gross_income` (order 2), left after step 25, 1 between. Late: reachable only after the answer to `dependent[dep_a].qr_all_year` (step 26), which its gate does not read.
- order 3 re-entered at step 30 by `dependent[dep_a].spouse_relative` (order 3), left after step 26, 3 between. Late: left for `dependent[dep_a].gross_income` (order 2), which sorts earlier and was reachable only after the answer to `dependent[dep_a].qr_all_year` (step 26), which its gate does not read.
- order 3 re-entered at step 39 by `person[taxpayer].w2[emp_a].box1` (order 3), left after step 33, 5 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 38), its parent or roster.
- order 4 re-entered at step 42 by `person[taxpayer].w2[emp_a].box5` (order 4), left after step 36, 5 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 38), its parent or roster.
- order 5 re-entered at step 44 by `sales[s1].route` (order 5), left after step 38, 5 between. Sorting: left for `person[taxpayer].w2[emp_a].box1` (order 3), a child of the question before it, which the bank places in another order number.
- form person re-entered at step 20 by `person[spouse].under16` (order 2), left after step 1, 18 between. Sorting: it was reachable (since step 2), and `scope.other_income` was asked instead (the bank puts order 0 first).
- form sales re-entered at step 23 by `sales[s1].box` (order 2), left after step 8, 14 between. Sorting: it was reachable (since step 9), and `$dependent` was asked instead (within order 2, sorted by id).
- form dependent re-entered at step 26 by `dependent[dep_a].qr_all_year` (order 3), left after step 18, 7 between. Sorting: it was reachable (since step 19), and `household.married` was asked instead (the bank puts order 2 first).
- form sales re-entered at step 31 by `sales[s1].special` (order 3), left after step 25, 5 between. Sorting: it was reachable (since step 9), and `dependent[dep_a].qr_all_year` was asked instead (within order 3, sorted by id).
- form sales re-entered at step 44 by `sales[s1].route` (order 5), left after step 36, 7 between. Sorting: it was reachable (since step 9), and `$w2@person[spouse]` was asked instead (within order 5, sorted by id).

**generated.22**: 103 questions, refused; order re-entries 3, form re-entries 6 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 1:sales×1 · 2:dependent×24 · 2:household×3 · 2:person×1 · 2:s3×1 · 2:sales×3 · 3:sales×3 · 4:sales×3 · 5:w2×1 · 3:w2×6 · 4:w2×8 · 5:sales×3 · 8:interest×1 · 9:f8889×13 · 10:oi8z×1 · 10:div×1 · 10:f1040×3 · 10:f4952×6 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:oi8z×2 · 10:person×4 · 10:refund×1 · 10:s1×4

- order 3 re-entered at step 48 by `person[taxpayer].w2[emp_a].box1` (order 3), left after step 43, 4 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 47), its parent or roster.
- order 4 re-entered at step 54 by `person[taxpayer].w2[emp_a].box3` (order 4), left after step 46, 7 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 47), its parent or roster.
- order 5 re-entered at step 62 by `sales[s1].route` (order 5), left after step 47, 14 between. Sorting: left for `person[taxpayer].w2[emp_a].box1` (order 3), a child of the question before it, which the bank places in another order number.
- form person re-entered at step 36 by `person[taxpayer].under16` (order 2), left after step 1, 34 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form sales re-entered at step 38 by `sales[s1].box` (order 2), left after step 8, 29 between. Sorting: it was reachable (since step 9), and `$dependent` was asked instead (within order 2, sorted by id).
- form sales re-entered at step 62 by `sales[s1].route` (order 5), left after step 46, 15 between. Sorting: it was reachable (since step 9), and `$w2@person[taxpayer]` was asked instead (within order 5, sorted by id).
- form f1040 re-entered at step 81 by `f1040.line25b` (order 10), left after step 2, 78 between. Sorting: it was reachable (since step 1), and `scope.other_income` was asked instead (the bank puts order 0 first).
- form oi8z re-entered at step 93 by `oi8z[item_a].amount` (order 10), left after step 79, 13 between. Sorting: it was reachable (since step 80), and `div.any` was asked instead (within order 10, sorted by id).
- form person re-entered at step 95 by `person[taxpayer].age65` (order 10), left after step 36, 58 between. Sorting: it was reachable (since step 2), and `s3.adoption_any` was asked instead (the bank puts order 2 first).

**generated.23**: 99 questions, refused; order re-entries 7, form re-entries 7 sorting and 4 late, delayed children 4 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 1:sales×1 · 2:dependent×1 · 2:household×2 · 2:person×1 · 2:s3×1 · 2:sales×1 · 3:sales×1 · 4:sales×1 · 5:w2×1 · 3:w2×3 · 4:w2×2 · 5:sales×1 · 8:interest×1 · 9:f8889×13 · 10:oi8z×1 · 10:div×1 · 10:f1040×3 · 10:f4952×2 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:person×1 · 2:person×1 · 10:person×4 · 10:refund×1 · 10:s1×10 · 10:s1a×3 · 10:s2×2 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×1 · 5:sa×1 · 5:gift×1 · 10:sa×9 · 10:sales×2 · 10:sb×2 · 10:sd×2 · 10:sb×1

- order 3 re-entered at step 18 by `person[taxpayer].w2[emp_a].box1` (order 3), left after step 15, 2 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 17), its parent or roster.
- order 4 re-entered at step 21 by `person[taxpayer].w2[emp_a].box5` (order 4), left after step 16, 4 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 17), its parent or roster.
- order 5 re-entered at step 23 by `sales[s1].route` (order 5), left after step 17, 5 between. Sorting: left for `person[taxpayer].w2[emp_a].box1` (order 3), a child of the question before it, which the bank places in another order number.
- order 2 re-entered at step 49 by `person[taxpayer].work_ssn` (order 2), left after step 14, 34 between. Late: reachable only after the answer to `person[taxpayer].age65` (step 48), which its gate does not read.
- order 10 re-entered at step 50 by `person[taxpayer].died_before_65` (order 10), left after step 48, 1 between. Late: left for `person[taxpayer].work_ssn` (order 2), which sorts earlier and was reachable only after the answer to `person[taxpayer].age65` (step 48), which its gate does not read.
- order 5 re-entered at step 82 by `sa.gifts` (order 5), left after step 23, 58 between. Late: reachable only after the answer to `sa.elect_itemize` (step 81), which its gate does not read.
- order 10 re-entered at step 84 by `sa.charity_limited` (order 10), left after step 81, 2 between. Late: reachable only after the answer to `sa.gifts` (step 82), its parent or roster.
- form person re-entered at step 12 by `person[taxpayer].under16` (order 2), left after step 1, 10 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form sales re-entered at step 14 by `sales[s1].box` (order 2), left after step 8, 5 between. Sorting: it was reachable (since step 9), and `$dependent` was asked instead (within order 2, sorted by id).
- form sales re-entered at step 23 by `sales[s1].route` (order 5), left after step 16, 6 between. Sorting: it was reachable (since step 9), and `$w2@person[taxpayer]` was asked instead (within order 5, sorted by id).
- form f1040 re-entered at step 40 by `f1040.line25b` (order 10), left after step 2, 37 between. Sorting: it was reachable (since step 1), and `scope.other_income` was asked instead (the bank puts order 0 first).
- form person re-entered at step 48 by `person[taxpayer].age65` (order 10), left after step 12, 35 between. Sorting: it was reachable (since step 2), and `s3.adoption_any` was asked instead (the bank puts order 2 first).
- form s3 re-entered at step 70 by `s3.credit_bond` (order 10), left after step 13, 56 between. Sorting: it was reachable (since step 1), and `sales[s1].box` was asked instead (the bank puts order 2 first).
- form person re-entered at step 80 by `person[taxpayer].blind` (order 10), left after step 53, 26 between. Late: reachable only after the answer to `sa.dependent` (step 79), which its gate does not read.
- form sa re-entered at step 81 by `sa.elect_itemize` (order 10), left after step 79, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 79), which its gate does not read.
- form sa re-entered at step 84 by `sa.charity_limited` (order 10), left after step 82, 1 between. Late: left for `$gift` (order 5), which sorts earlier and was reachable only after the answer to `sa.gifts` (step 82), which its gate does not read.
- form sales re-entered at step 93 by `sales[s1].correct_basis` (order 10), left after step 23, 69 between. Sorting: it was reachable (since step 24), and `$interest` was asked instead (the bank puts order 8 first).
- form sb re-entered at step 99 by `sb.unsupported` (order 10), left after step 96, 2 between. Late: reachable only after the answer to `sd.distributions` (step 98), which its gate does not read.
- `sa.charity_limited` (order 10), step 84: child of `sa.gifts` (step 82), 1 other question between. Sorting: it was reachable (since step 83), and `$gift` was asked instead (the bank puts order 5 first).
- `sa.line11` (order 10), step 87: child of `sa.gifts` (step 82), 3 other questions between. Sorting: it was reachable (since step 83), and `$gift` was asked instead (the bank puts order 5 first).
- `sb.ordinary_dividends` (order 10), step 96: child of `div.any` (step 39), 56 other questions between. Sorting: it was reachable (since step 40), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `sd.distributions` (order 10), step 98: child of `div.any` (step 39), 57 other questions between. Sorting: it was reachable (since step 40), and `f1040.line25b` was asked instead (within order 10, sorted by id).

**generated.24**: 2 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1

**generated.25**: 103 questions, refused; order re-entries 8, form re-entries 7 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×2 · 1:sales×1 · 2:dependent×34 · 2:household×1 · 2:person×1 · 2:retirement×3 · 2:person×1 · 2:s3×1 · 2:sales×2 · 3:sales×2 · 4:sales×2 · 5:w2×1 · 3:w2×3 · 4:w2×2 · 5:w2×1 · 3:w2×3 · 4:w2×2 · 5:sales×2 · 8:interest×1 · 9:f8889×14 · 10:oi8z×1 · 10:div×1 · 10:f1040×3 · 10:f4952×6 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:interest×2 · 10:person×1 · 2:person×1 · 10:person×1

- order 3 re-entered at step 57 by `person[spouse].w2[emp_a].box1` (order 3), left after step 53, 3 between. Late: reachable only after the answer to `$w2@person[spouse]` (step 56), its parent or roster.
- order 4 re-entered at step 60 by `person[spouse].w2[emp_a].box5` (order 4), left after step 55, 4 between. Late: reachable only after the answer to `$w2@person[spouse]` (step 56), its parent or roster.
- order 5 re-entered at step 62 by `$w2@person[taxpayer]` (order 5), left after step 56, 5 between. Sorting: left for `person[spouse].w2[emp_a].box1` (order 3), a child of the question before it, which the bank places in another order number.
- order 3 re-entered at step 63 by `person[taxpayer].w2[emp_a].box1` (order 3), left after step 59, 3 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 62), its parent or roster.
- order 4 re-entered at step 66 by `person[taxpayer].w2[emp_a].box5` (order 4), left after step 61, 4 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 62), its parent or roster.
- order 5 re-entered at step 68 by `sales[s1].route` (order 5), left after step 62, 5 between. Sorting: left for `person[taxpayer].w2[emp_a].box1` (order 3), a child of the question before it, which the bank places in another order number.
- order 2 re-entered at step 102 by `person[spouse].work_ssn` (order 2), left after step 51, 50 between. Late: reachable only after the answer to `person[spouse].age65` (step 101), which its gate does not read.
- order 10 re-entered at step 103 by `person[spouse].died_before_65` (order 10), left after step 101, 1 between. Late: reachable only after the answer to `person[spouse].work_ssn` (step 102), which its gate does not read.
- form person re-entered at step 44 by `person[spouse].under16` (order 2), left after step 1, 42 between. Sorting: it was reachable (since step 2), and `scope.other_income` was asked instead (the bank puts order 0 first).
- form retirement re-entered at step 45 by `person[taxpayer].retirement[r1].account` (order 2), left after step 7, 37 between. Sorting: it was reachable (since step 8), and `$sales` was asked instead (the bank puts order 1 first).
- form person re-entered at step 48 by `person[taxpayer].under16` (order 2), left after step 44, 3 between. Sorting: it was reachable (since step 2), and `person[taxpayer].retirement[r1].account` was asked instead (within order 2, sorted by id).
- form sales re-entered at step 50 by `sales[s1].box` (order 2), left after step 8, 41 between. Sorting: it was reachable (since step 9), and `$dependent` was asked instead (within order 2, sorted by id).
- form sales re-entered at step 68 by `sales[s1].route` (order 5), left after step 55, 12 between. Sorting: it was reachable (since step 9), and `$w2@person[spouse]` was asked instead (within order 5, sorted by id).
- form interest re-entered at step 99 by `interest[bank_a].amount` (order 10), left after step 70, 28 between. Sorting: it was reachable (since step 71), and `$f8889@person[spouse]` was asked instead (the bank puts order 9 seq 1 first).
- form person re-entered at step 101 by `person[spouse].age65` (order 10), left after step 48, 52 between. Sorting: it was reachable (since step 2), and `s3.adoption_any` was asked instead (the bank puts order 2 first).

**generated.26**: 105 questions, refused; order re-entries 2, form re-entries 3 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×2 · 1:sales×1 · 2:dependent×12 · 2:household×1 · 2:person×2 · 2:s3×1 · 5:w2×2 · 3:w2×6 · 4:w2×8 · 8:interest×1 · 9:f8889×14 · 10:oi8z×1 · 10:div×1 · 10:f1040×3 · 10:f4952×6 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:person×1 · 2:person×1 · 10:person×8 · 10:refund×1 · 10:s1×10 · 10:s1a×3 · 10:s2×2 · 10:s3×9 · 10:sa×1

- order 2 re-entered at step 71 by `person[spouse].work_ssn` (order 2), left after step 24, 46 between. Late: reachable only after the answer to `person[spouse].age65` (step 70), which its gate does not read.
- order 10 re-entered at step 72 by `person[spouse].died_before_65` (order 10), left after step 70, 1 between. Late: reachable only after the answer to `person[spouse].work_ssn` (step 71), which its gate does not read.
- form person re-entered at step 22 by `person[spouse].under16` (order 2), left after step 1, 20 between. Sorting: it was reachable (since step 2), and `scope.other_income` was asked instead (the bank puts order 0 first).
- form person re-entered at step 70 by `person[spouse].age65` (order 10), left after step 23, 46 between. Sorting: it was reachable (since step 2), and `s3.adoption_any` was asked instead (the bank puts order 2 first).
- form s3 re-entered at step 96 by `s3.credit_bond` (order 10), left after step 24, 71 between. Sorting: it was reachable (since step 1), and `$w2@person[spouse]` was asked instead (the bank puts order 5 first).

**generated.27**: 46 questions, refused; order re-entries 0, form re-entries 1 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 1:sales×1 · 2:dependent×30 · 2:f1095a×3 · 2:household×5

- form f1095a re-entered at step 39 by `f1095a[mkt_a].uniform` (order 2), left after step 6, 32 between. Sorting: it was reachable (since step 7), and `$retirement@person[taxpayer]` was asked instead (the bank puts order 1 first).

**generated.28**: 11 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×2 · 1:sales×1 · 2:dependent×3

**generated.29**: 11 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 1:sales×1 · 2:dependent×3

**generated.30**: 124 questions, refused; order re-entries 7, form re-entries 9 sorting and 7 late, delayed children 2 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 1:sales×1 · 2:dependent×1 · 2:household×2 · 2:retirement×5 · 2:person×1 · 2:s3×1 · 2:sales×2 · 3:retirement×1 · 3:sales×2 · 4:sales×2 · 5:w2×1 · 3:w2×6 · 4:w2×8 · 5:sales×2 · 8:interest×1 · 9:f8889×6 · 2:household×1 · 9:f8889×13 · 10:oi8z×1 · 10:div×1 · 10:f1040×3 · 10:f4952×6 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:person×4 · 10:refund×1 · 10:s1×10 · 10:s1a×3 · 10:s2×2 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×1 · 5:sa×1 · 5:gift×1 · 10:gift×3 · 10:sa×8 · 10:s3×1 · 10:sa×1

- order 3 re-entered at step 27 by `person[taxpayer].w2[emp_a].box1` (order 3), left after step 23, 3 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 26), its parent or roster.
- order 4 re-entered at step 33 by `person[taxpayer].w2[emp_a].box3` (order 4), left after step 25, 7 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 26), its parent or roster.
- order 5 re-entered at step 41 by `sales[s1].route` (order 5), left after step 26, 14 between. Sorting: left for `person[taxpayer].w2[emp_a].box1` (order 3), a child of the question before it, which the bank places in another order number.
- order 2 re-entered at step 50 by `household.married` (order 2), left after step 20, 29 between. Late: reachable only after the answer to `person[taxpayer].f8889[hsa].line2` (step 49), which its gate does not read.
- order 9 re-entered at step 51 by `person[taxpayer].f8889[hsa].ira_transfer` (order 9 seq 7), left after step 49, 1 between. Late: left for `household.married` (order 2), which sorts earlier and was reachable only after the answer to `person[taxpayer].f8889[hsa].line2` (step 49), which its gate does not read.
- order 5 re-entered at step 110 by `sa.gifts` (order 5), left after step 42, 67 between. Late: reachable only after the answer to `sa.elect_itemize` (step 109), which its gate does not read.
- order 10 re-entered at step 112 by `gift[item_a].deduction` (order 10), left after step 109, 2 between. Late: reachable only after the answer to `$gift` (step 111), its parent or roster.
- form retirement re-entered at step 12 by `person[taxpayer].retirement[r1].account` (order 2), left after step 7, 4 between. Sorting: it was reachable (since step 8), and `$sales` was asked instead (the bank puts order 1 first).
- form person re-entered at step 17 by `person[taxpayer].under16` (order 2), left after step 1, 15 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form sales re-entered at step 19 by `sales[s1].box` (order 2), left after step 8, 10 between. Sorting: it was reachable (since step 9), and `$dependent` was asked instead (within order 2, sorted by id).
- form retirement re-entered at step 21 by `person[taxpayer].retirement[r1].code_screen` (order 3), left after step 16, 4 between. Sorting: it was reachable (since step 15), and `person[taxpayer].under16` was asked instead (the bank puts order 2 first).
- form sales re-entered at step 22 by `sales[s1].special` (order 3), left after step 20, 1 between. Sorting: it was reachable (since step 9), and `person[taxpayer].retirement[r1].code_screen` was asked instead (within order 3, sorted by id).
- form sales re-entered at step 41 by `sales[s1].route` (order 5), left after step 25, 15 between. Sorting: it was reachable (since step 9), and `$w2@person[taxpayer]` was asked instead (within order 5, sorted by id).
- form household re-entered at step 50 by `household.married` (order 2), left after step 11, 38 between. Late: reachable only after the answer to `person[taxpayer].f8889[hsa].line2` (step 49), which its gate does not read.
- form f8889 re-entered at step 51 by `person[taxpayer].f8889[hsa].ira_transfer` (order 9 seq 7), left after step 49, 1 between. Late: left for `household.married` (order 2), which sorts earlier and was reachable only after the answer to `person[taxpayer].f8889[hsa].line2` (step 49), which its gate does not read.
- form f1040 re-entered at step 66 by `f1040.line25b` (order 10), left after step 2, 63 between. Sorting: it was reachable (since step 1), and `scope.other_income` was asked instead (the bank puts order 0 first).
- form person re-entered at step 78 by `person[taxpayer].age65` (order 10), left after step 17, 60 between. Sorting: it was reachable (since step 2), and `s3.adoption_any` was asked instead (the bank puts order 2 first).
- form s3 re-entered at step 98 by `s3.credit_bond` (order 10), left after step 18, 79 between. Sorting: it was reachable (since step 1), and `sales[s1].box` was asked instead (the bank puts order 2 first).
- form person re-entered at step 108 by `person[taxpayer].blind` (order 10), left after step 81, 26 between. Late: reachable only after the answer to `sa.dependent` (step 107), which its gate does not read.
- form sa re-entered at step 109 by `sa.elect_itemize` (order 10), left after step 107, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 107), which its gate does not read.
- form sa re-entered at step 115 by `sa.charity_limited` (order 10), left after step 110, 4 between. Late: left for `$gift` (order 5), which sorts earlier and was reachable only after the answer to `sa.gifts` (step 110), which its gate does not read.
- form s3 re-entered at step 123 by `s3.mcc` (order 10), left after step 106, 16 between. Late: reachable only after the answer to `sa.line8a` (step 122), which its gate does not read.
- form sa re-entered at step 124 by `sa.unsupported` (order 10), left after step 122, 1 between. Late: left for `s3.mcc` (order 10), which sorts earlier and was reachable only after the answer to `sa.line8a` (step 122), which its gate does not read.
- `sa.charity_limited` (order 10), step 115: child of `sa.gifts` (step 110), 4 other questions between. Sorting: it was reachable (since step 111), and `$gift` was asked instead (the bank puts order 5 first).
- `sa.line11` (order 10), step 118: child of `sa.gifts` (step 110), 6 other questions between. Sorting: it was reachable (since step 111), and `$gift` was asked instead (the bank puts order 5 first).

**generated.31**: 169 questions, refused; order re-entries 2, form re-entries 9 sorting and 5 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 1:sales×1 · 2:dependent×1 · 2:household×3 · 2:person×1 · 2:s3×1 · 5:w2×1 · 3:w2×6 · 4:w2×8 · 8:interest×1 · 9:f8889×13 · 10:oi8z×1 · 10:div×1 · 10:f1040×3 · 10:f4952×6 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:interest×4 · 10:oi8z×2 · 10:person×4 · 10:refund×1 · 10:s1×10 · 10:s1a×3 · 10:s2×2 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×1 · 5:sa×1 · 10:sa×6 · 10:s3×1 · 10:sa×1 · 10:sb×2 · 10:sd×2 · 10:sli×1 · 10:ssb×1 · 11:sc×1 · 11:asset×1 · 11:scveh×1 · 12:person×1 · 12:asset×10 · 12:sc×38 · 12:scveh×7

- order 5 re-entered at step 96 by `sa.gifts` (order 5), left after step 15, 80 between. Late: reachable only after the answer to `sa.elect_itemize` (step 95), which its gate does not read.
- order 10 re-entered at step 97 by `sa.excluded_income` (order 10), left after step 95, 1 between. Late: left for `sa.gifts` (order 5), which sorts earlier and was reachable only after the answer to `sa.elect_itemize` (step 95), which its gate does not read.
- form person re-entered at step 13 by `person[taxpayer].under16` (order 2), left after step 1, 11 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form f1040 re-entered at step 46 by `f1040.line25b` (order 10), left after step 2, 43 between. Sorting: it was reachable (since step 1), and `scope.other_income` was asked instead (the bank puts order 0 first).
- form interest re-entered at step 58 by `interest[bank_a].amount` (order 10), left after step 30, 27 between. Sorting: it was reachable (since step 31), and `$f8889@person[taxpayer]` was asked instead (the bank puts order 9 seq 1 first).
- form oi8z re-entered at step 62 by `oi8z[item_a].amount` (order 10), left after step 44, 17 between. Sorting: it was reachable (since step 45), and `div.any` was asked instead (within order 10, sorted by id).
- form person re-entered at step 64 by `person[taxpayer].age65` (order 10), left after step 13, 50 between. Sorting: it was reachable (since step 2), and `s3.adoption_any` was asked instead (the bank puts order 2 first).
- form s3 re-entered at step 84 by `s3.credit_bond` (order 10), left after step 14, 69 between. Sorting: it was reachable (since step 1), and `$w2@person[taxpayer]` was asked instead (the bank puts order 5 first).
- form person re-entered at step 94 by `person[taxpayer].blind` (order 10), left after step 67, 26 between. Late: reachable only after the answer to `sa.dependent` (step 93), which its gate does not read.
- form sa re-entered at step 95 by `sa.elect_itemize` (order 10), left after step 93, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 93), which its gate does not read.
- form s3 re-entered at step 103 by `s3.mcc` (order 10), left after step 92, 10 between. Late: reachable only after the answer to `sa.line8a` (step 102), which its gate does not read.
- form sa re-entered at step 104 by `sa.unsupported` (order 10), left after step 102, 1 between. Late: left for `s3.mcc` (order 10), which sorts earlier and was reachable only after the answer to `sa.line8a` (step 102), which its gate does not read.
- form person re-entered at step 114 by `person[taxpayer].plan` (order 12), left after step 94, 19 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 111), which its gate does not read.
- form asset re-entered at step 115 by `person[taxpayer].sc[biz_a].asset[item_1].class` (order 12), left after step 112, 2 between. Sorting: it was reachable (since step 113), and `$scveh@person[taxpayer].sc[biz_a]` was asked instead (the bank puts order 11 first).
- form sc re-entered at step 125 by `person[taxpayer].sc[biz_a].business_credit` (order 12), left after step 111, 13 between. Sorting: left for `$asset@person[taxpayer].sc[biz_a]` (order 11), a child of the question before it, which the bank places in another form.
- form scveh re-entered at step 163 by `person[taxpayer].sc[biz_a].scveh[car_1].method` (order 12), left after step 113, 49 between. Sorting: it was reachable (since step 114), and `person[taxpayer].plan` was asked instead (within order 12, sorted by id).

**generated.32**: 13 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×2 · 1:sales×1 · 2:dependent×5

**generated.33**: 13 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 1:sales×1 · 2:dependent×5

**generated.34**: 169 questions, complete; order re-entries 12, form re-entries 10 sorting and 14 late, delayed children 3 sorting and 5 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 1:sales×1 · 2:dependent×20 · 2:household×5 · 2:retirement×3 · 2:person×1 · 2:s3×1 · 3:dependent×3 · 2:dependent×3 · 5:w2×1 · 3:w2×6 · 4:w2×8 · 8:interest×1 · 9:f8889×13 · 10:oi8z×1 · 10:div×1 · 10:f1040×3 · 10:f4952×2 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:interest×2 · 10:person×4 · 10:refund×1 · 10:s1×10 · 10:s1a×3 · 10:s2×2 · 10:s3×9 · 10:sa×1 · 2:dependent×1 · 2:person×2 · 10:person×1 · 10:sa×1 · 5:sa×1 · 10:sa×6 · 10:s3×1 · 10:sa×1 · 10:sb×2 · 10:f1040×1 · 10:qbi×1 · 10:sb×1 · 10:sd×3 · 10:sli×1 · 10:ssb×4 · 11:sc×1 · 12:s179×1 · 15:div×9 · 20:f2441×2 · 20:s8812×1 · 22:person×1 · 24:f5695×2 · 30:div×1 · 30:f1040×1 · 2:dependent×1 · 10:qbi×1 · 12:qbi×1 · 20:household×1 · 30:dependent×2 · 30:person×1 · 20:s8812×1

- order 2 re-entered at step 42 by `dependent[dep_b].gross_income` (order 2), left after step 38, 3 between. Late: reachable only after the answer to `dependent[dep_b].qr_all_year` (step 41), which its gate does not read.
- order 3 re-entered at step 46 by `person[taxpayer].w2[emp_a].box1` (order 3), left after step 41, 4 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 45), its parent or roster.
- order 2 re-entered at step 116 by `dependent[dep_a].work_ssn` (order 2), left after step 44, 71 between. Late: reachable only after the answer to `sa.dependent` (step 115), which its gate does not read.
- order 10 re-entered at step 119 by `person[taxpayer].blind` (order 10), left after step 115, 3 between. Late: left for `dependent[dep_a].work_ssn` (order 2), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 115), which its gate does not read.
- order 5 re-entered at step 121 by `sa.gifts` (order 5), left after step 45, 75 between. Late: reachable only after the answer to `sa.elect_itemize` (step 120), which its gate does not read.
- order 10 re-entered at step 122 by `sa.excluded_income` (order 10), left after step 120, 1 between. Late: left for `sa.gifts` (order 5), which sorts earlier and was reachable only after the answer to `sa.elect_itemize` (step 120), which its gate does not read.
- order 2 re-entered at step 162 by `dependent[dep_a].kidnapped` (order 2), left after step 118, 43 between. Late: reachable only after the answer to `f1040.tax_exempt_interest` (step 161), which its gate does not read.
- order 10 re-entered at step 163 by `qbi.unsupported` (order 10), left after step 142, 20 between. Late: reachable only after the answer to `f1040.tax_exempt_interest` (step 161), which its gate does not read.
- order 12 re-entered at step 164 by `qbi.carryforward` (order 12), left after step 144, 19 between. Late: reachable only after the answer to `f1040.tax_exempt_interest` (step 161), which its gate does not read.
- order 20 re-entered at step 165 by `household.credit_disallowed` (order 20), left after step 156, 8 between. Late: reachable only after the answer to `f1040.tax_exempt_interest` (step 161), which its gate does not read.
- order 30 re-entered at step 166 by `dependent[dep_a].us_half` (order 30), left after step 161, 4 between. Late: left for `dependent[dep_a].kidnapped` (order 2), which sorts earlier and was reachable only after the answer to `f1040.tax_exempt_interest` (step 161), which its gate does not read.
- order 20 re-entered at step 169 by `s8812.combat_pay` (order 20), left after step 165, 3 between. Late: reachable only after the answer to `person[taxpayer].eic_ssn` (step 168), which its gate does not read.
- form retirement re-entered at step 34 by `person[taxpayer].retirement[r1].account` (order 2), left after step 7, 26 between. Sorting: it was reachable (since step 8), and `$sales` was asked instead (the bank puts order 1 first).
- form person re-entered at step 37 by `person[taxpayer].under16` (order 2), left after step 1, 35 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form dependent re-entered at step 39 by `dependent[dep_a].absence_no_return` (order 3), left after step 28, 10 between. Late: reachable only after the answer to `household.home_cost` (step 33), which its gate does not read.
- form f1040 re-entered at step 76 by `f1040.line25b` (order 10), left after step 2, 73 between. Sorting: it was reachable (since step 1), and `scope.other_income` was asked instead (the bank puts order 0 first).
- form interest re-entered at step 84 by `interest[bank_a].amount` (order 10), left after step 60, 23 between. Sorting: it was reachable (since step 61), and `$f8889@person[taxpayer]` was asked instead (the bank puts order 9 seq 1 first).
- form person re-entered at step 86 by `person[taxpayer].age65` (order 10), left after step 37, 48 between. Sorting: it was reachable (since step 2), and `s3.adoption_any` was asked instead (the bank puts order 2 first).
- form s3 re-entered at step 106 by `s3.credit_bond` (order 10), left after step 38, 67 between. Sorting: it was reachable (since step 1), and `dependent[dep_a].absence_no_return` was asked instead (the bank puts order 3 first).
- form dependent re-entered at step 116 by `dependent[dep_a].work_ssn` (order 2), left after step 44, 71 between. Late: reachable only after the answer to `sa.dependent` (step 115), which its gate does not read.
- form person re-entered at step 117 by `person[taxpayer].tin` (order 2), left after step 89, 27 between. Late: reachable only after the answer to `sa.dependent` (step 115), which its gate does not read.
- form sa re-entered at step 120 by `sa.elect_itemize` (order 10), left after step 115, 4 between. Late: left for `dependent[dep_a].work_ssn` (order 2), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 115), which its gate does not read.
- form s3 re-entered at step 128 by `s3.mcc` (order 10), left after step 114, 13 between. Late: reachable only after the answer to `sa.line8a` (step 127), which its gate does not read.
- form sa re-entered at step 129 by `sa.unsupported` (order 10), left after step 127, 1 between. Late: left for `s3.mcc` (order 10), which sorts earlier and was reachable only after the answer to `sa.line8a` (step 127), which its gate does not read.
- form f1040 re-entered at step 132 by `f1040.line3a` (order 10), left after step 78, 53 between. Late: reachable only after the answer to `sb.ordinary_dividends` (step 131), which its gate does not read.
- form sb re-entered at step 134 by `sb.unsupported` (order 10), left after step 131, 2 between. Late: left for `f1040.line3a` (order 10), which sorts earlier and was reachable only after the answer to `sb.ordinary_dividends` (step 131), which its gate does not read.
- form div re-entered at step 145 by `div.box13` (order 15), left after step 75, 69 between. Sorting: it was reachable (since step 76), and `f1040.line25b` was asked instead (the bank puts order 10 first).
- form person re-entered at step 157 by `person[taxpayer].sav_trad` (order 22), left after step 119, 37 between. Sorting: it was reachable (since step 2), and `sa.elect_itemize` was asked instead (the bank puts order 10 first).
- form div re-entered at step 160 by `div.box12` (order 30), left after step 153, 6 between. Sorting: it was reachable (since step 140), and `f2441.benefits` was asked instead (the bank puts order 20 first).
- form f1040 re-entered at step 161 by `f1040.tax_exempt_interest` (order 30), left after step 132, 28 between. Late: reachable only after the answer to `ssb.benefits` (step 139), which its gate does not read.
- form dependent re-entered at step 162 by `dependent[dep_a].kidnapped` (order 2), left after step 116, 45 between. Late: reachable only after the answer to `f1040.tax_exempt_interest` (step 161), which its gate does not read.
- form qbi re-entered at step 163 by `qbi.unsupported` (order 10), left after step 133, 29 between. Late: reachable only after the answer to `f1040.tax_exempt_interest` (step 161), which its gate does not read.
- form household re-entered at step 165 by `household.credit_disallowed` (order 20), left after step 33, 131 between. Late: reachable only after the answer to `f1040.tax_exempt_interest` (step 161), which its gate does not read.
- form dependent re-entered at step 166 by `dependent[dep_a].us_half` (order 30), left after step 162, 3 between. Sorting: it was reachable (since step 162), and `qbi.unsupported` was asked instead (the bank puts order 10 first).
- form person re-entered at step 168 by `person[taxpayer].eic_ssn` (order 30), left after step 157, 10 between. Late: reachable only after the answer to `dependent[dep_a].eic_ssn` (step 167), which its gate does not read.
- form s8812 re-entered at step 169 by `s8812.combat_pay` (order 20), left after step 156, 12 between. Late: reachable only after the answer to `person[taxpayer].eic_ssn` (step 168), which its gate does not read.
- `sb.ordinary_dividends` (order 10), step 131: child of `div.any` (step 75), 55 other questions between. Sorting: it was reachable (since step 76), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `sd.distributions` (order 10), step 136: child of `div.any` (step 75), 59 other questions between. Sorting: it was reachable (since step 76), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `div.box13` (order 15), step 145: child of `div.any` (step 75), 67 other questions between. Sorting: it was reachable (since step 76), and `f1040.line25b` was asked instead (the bank puts order 10 first).
- `div.box10` (order 15), step 148: child of `div.any` (step 75), 69 other questions between. Late: reachable only after the answer to `div.box2c` (step 147), which its gate does not read.
- `div.box3` (order 15), step 152: child of `div.any` (step 75), 72 other questions between. Late: reachable only after the answer to `div.box2c` (step 147), which its gate does not read.
- `div.box9` (order 15), step 153: child of `div.any` (step 75), 72 other questions between. Late: reachable only after the answer to `div.box2c` (step 147), which its gate does not read.
- `div.box12` (order 30), step 160: child of `div.any` (step 75), 78 other questions between. Late: reachable only after the answer to `ssb.benefits` (step 139), which its gate does not read.
- `household.credit_disallowed` (order 20), step 165: child of `sa.excluded_income` (step 122), 42 other questions between. Late: reachable only after the answer to `f1040.tax_exempt_interest` (step 161), which its gate does not read.

**generated.35**: 2 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1

**generated.36**: 35 questions, refused; order re-entries 0, form re-entries 3 sorting and 1 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 1:sales×1 · 2:dependent×12 · 2:household×5 · 2:dependent×2 · 2:person×1 · 2:s3×1 · 2:sales×3 · 3:dependent×3

- form dependent re-entered at step 26 by `dependent[dep_a].months` (order 2), left after step 20, 5 between. Late: reachable only after the answer to `household.home_cost` (step 25), which its gate does not read.
- form person re-entered at step 28 by `person[taxpayer].under16` (order 2), left after step 1, 26 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form sales re-entered at step 30 by `sales[s1].box` (order 2), left after step 8, 21 between. Sorting: it was reachable (since step 9), and `$dependent` was asked instead (within order 2, sorted by id).
- form dependent re-entered at step 33 by `dependent[dep_a].absence_no_return` (order 3), left after step 27, 5 between. Sorting: it was reachable (since step 26), and `person[taxpayer].under16` was asked instead (the bank puts order 2 first).

**generated.37**: 144 questions, complete; order re-entries 7, form re-entries 12 sorting and 8 late, delayed children 5 sorting and 3 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 1:sales×1 · 2:dependent×1 · 2:household×3 · 2:retirement×13 · 2:person×1 · 2:s3×1 · 2:sales×1 · 3:retirement×2 · 3:sales×1 · 4:sales×1 · 5:w2×1 · 3:w2×3 · 4:w2×2 · 5:sales×1 · 8:interest×1 · 9:f8889×13 · 10:oi8z×1 · 10:div×1 · 10:f1040×3 · 10:f4952×6 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:person×5 · 10:refund×1 · 10:s1×12 · 10:s1a×3 · 10:s2×2 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×1 · 5:sa×1 · 5:gift×1 · 10:sa×8 · 10:s3×1 · 10:sa×1 · 10:sales×2 · 10:sb×2 · 10:f1040×1 · 10:qbi×1 · 10:sb×1 · 10:sd×3 · 10:sli×1 · 10:ssb×1 · 11:sc×1 · 12:s179×1 · 15:div×9 · 20:f2441×2 · 22:person×1 · 10:qbi×1 · 12:qbi×1 · 24:f5695×2

- order 3 re-entered at step 34 by `person[taxpayer].w2[emp_a].box1` (order 3), left after step 31, 2 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 33), its parent or roster.
- order 4 re-entered at step 37 by `person[taxpayer].w2[emp_a].box5` (order 4), left after step 32, 4 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 33), its parent or roster.
- order 5 re-entered at step 39 by `sales[s1].route` (order 5), left after step 33, 5 between. Sorting: left for `person[taxpayer].w2[emp_a].box1` (order 3), a child of the question before it, which the bank places in another order number.
- order 5 re-entered at step 103 by `sa.gifts` (order 5), left after step 39, 63 between. Late: reachable only after the answer to `sa.elect_itemize` (step 102), which its gate does not read.
- order 10 re-entered at step 105 by `sa.charity_limited` (order 10), left after step 102, 2 between. Late: reachable only after the answer to `sa.gifts` (step 103), its parent or roster.
- order 10 re-entered at step 141 by `qbi.unsupported` (order 10), left after step 126, 14 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 140), which its gate does not read.
- order 12 re-entered at step 142 by `qbi.carryforward` (order 12), left after step 128, 13 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 140), which its gate does not read.
- form retirement re-entered at step 13 by `person[taxpayer].retirement[r1].account` (order 2), left after step 7, 5 between. Sorting: it was reachable (since step 8), and `$sales` was asked instead (the bank puts order 1 first).
- form person re-entered at step 26 by `person[taxpayer].under16` (order 2), left after step 1, 24 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form sales re-entered at step 28 by `sales[s1].box` (order 2), left after step 8, 19 between. Sorting: it was reachable (since step 9), and `$dependent` was asked instead (within order 2, sorted by id).
- form retirement re-entered at step 29 by `person[taxpayer].retirement[r1].code_screen` (order 3), left after step 25, 3 between. Sorting: it was reachable (since step 16), and `person[taxpayer].under16` was asked instead (the bank puts order 2 first).
- form sales re-entered at step 31 by `sales[s1].special` (order 3), left after step 28, 2 between. Sorting: it was reachable (since step 9), and `person[taxpayer].retirement[r1].code_screen` was asked instead (within order 3, sorted by id).
- form sales re-entered at step 39 by `sales[s1].route` (order 5), left after step 32, 6 between. Sorting: it was reachable (since step 9), and `$w2@person[taxpayer]` was asked instead (within order 5, sorted by id).
- form f1040 re-entered at step 56 by `f1040.line25b` (order 10), left after step 2, 53 between. Sorting: it was reachable (since step 1), and `scope.other_income` was asked instead (the bank puts order 0 first).
- form person re-entered at step 68 by `person[taxpayer].age65` (order 10), left after step 26, 41 between. Sorting: it was reachable (since step 2), and `s3.adoption_any` was asked instead (the bank puts order 2 first).
- form s3 re-entered at step 91 by `s3.credit_bond` (order 10), left after step 27, 63 between. Sorting: it was reachable (since step 1), and `sales[s1].box` was asked instead (the bank puts order 2 first).
- form person re-entered at step 101 by `person[taxpayer].blind` (order 10), left after step 72, 28 between. Late: reachable only after the answer to `sa.dependent` (step 100), which its gate does not read.
- form sa re-entered at step 102 by `sa.elect_itemize` (order 10), left after step 100, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 100), which its gate does not read.
- form sa re-entered at step 105 by `sa.charity_limited` (order 10), left after step 103, 1 between. Late: left for `$gift` (order 5), which sorts earlier and was reachable only after the answer to `sa.gifts` (step 103), which its gate does not read.
- form s3 re-entered at step 113 by `s3.mcc` (order 10), left after step 99, 13 between. Late: reachable only after the answer to `sa.line8a` (step 112), which its gate does not read.
- form sa re-entered at step 114 by `sa.unsupported` (order 10), left after step 112, 1 between. Late: left for `s3.mcc` (order 10), which sorts earlier and was reachable only after the answer to `sa.line8a` (step 112), which its gate does not read.
- form sales re-entered at step 115 by `sales[s1].correct_basis` (order 10), left after step 39, 75 between. Sorting: it was reachable (since step 40), and `$interest` was asked instead (the bank puts order 8 first).
- form f1040 re-entered at step 119 by `f1040.line3a` (order 10), left after step 58, 60 between. Late: reachable only after the answer to `sb.ordinary_dividends` (step 118), which its gate does not read.
- form sb re-entered at step 121 by `sb.unsupported` (order 10), left after step 118, 2 between. Late: left for `f1040.line3a` (order 10), which sorts earlier and was reachable only after the answer to `sb.ordinary_dividends` (step 118), which its gate does not read.
- form div re-entered at step 129 by `div.box13` (order 15), left after step 55, 73 between. Sorting: it was reachable (since step 56), and `f1040.line25b` was asked instead (the bank puts order 10 first).
- form person re-entered at step 140 by `person[taxpayer].sav_trad` (order 22), left after step 101, 38 between. Sorting: it was reachable (since step 2), and `sa.elect_itemize` was asked instead (the bank puts order 10 first).
- form qbi re-entered at step 141 by `qbi.unsupported` (order 10), left after step 120, 20 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 140), which its gate does not read.
- `sa.charity_limited` (order 10), step 105: child of `sa.gifts` (step 103), 1 other question between. Sorting: it was reachable (since step 104), and `$gift` was asked instead (the bank puts order 5 first).
- `sa.line11` (order 10), step 108: child of `sa.gifts` (step 103), 3 other questions between. Sorting: it was reachable (since step 104), and `$gift` was asked instead (the bank puts order 5 first).
- `sb.ordinary_dividends` (order 10), step 118: child of `div.any` (step 55), 62 other questions between. Sorting: it was reachable (since step 56), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `sd.distributions` (order 10), step 123: child of `div.any` (step 55), 66 other questions between. Sorting: it was reachable (since step 56), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `div.box13` (order 15), step 129: child of `div.any` (step 55), 71 other questions between. Sorting: it was reachable (since step 56), and `f1040.line25b` was asked instead (the bank puts order 10 first).
- `div.box10` (order 15), step 132: child of `div.any` (step 55), 73 other questions between. Late: reachable only after the answer to `div.box2c` (step 131), which its gate does not read.
- `div.box3` (order 15), step 136: child of `div.any` (step 55), 76 other questions between. Late: reachable only after the answer to `div.box2c` (step 131), which its gate does not read.
- `div.box9` (order 15), step 137: child of `div.any` (step 55), 76 other questions between. Late: reachable only after the answer to `div.box2c` (step 131), which its gate does not read.

**generated.38**: 22 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 1:sales×1 · 2:dependent×14

**generated.39**: 76 questions, refused; order re-entries 7, form re-entries 4 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×2 · 1:sales×1 · 2:dependent×1 · 2:f1095a×3 · 2:household×1 · 2:person×2 · 2:s3×1 · 2:sales×3 · 3:sales×1 · 4:sales×1 · 5:w2×1 · 3:w2×6 · 4:w2×8 · 5:w2×1 · 3:w2×3 · 4:w2×2 · 5:sales×2 · 4:sales×1 · 8:interest×1 · 9:f8889×30

- order 3 re-entered at step 23 by `person[spouse].w2[emp_a].box1` (order 3), left after step 20, 2 between. Late: reachable only after the answer to `$w2@person[spouse]` (step 22), its parent or roster.
- order 4 re-entered at step 29 by `person[spouse].w2[emp_a].box3` (order 4), left after step 21, 7 between. Late: reachable only after the answer to `$w2@person[spouse]` (step 22), its parent or roster.
- order 5 re-entered at step 37 by `$w2@person[taxpayer]` (order 5), left after step 22, 14 between. Sorting: left for `person[spouse].w2[emp_a].box1` (order 3), a child of the question before it, which the bank places in another order number.
- order 3 re-entered at step 38 by `person[taxpayer].w2[emp_a].box1` (order 3), left after step 28, 9 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 37), its parent or roster.
- order 4 re-entered at step 41 by `person[taxpayer].w2[emp_a].box5` (order 4), left after step 36, 4 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 37), its parent or roster.
- order 5 re-entered at step 43 by `sales[s1].route` (order 5), left after step 37, 5 between. Sorting: left for `person[taxpayer].w2[emp_a].box1` (order 3), a child of the question before it, which the bank places in another order number.
- order 4 re-entered at step 45 by `sales[s3].code` (order 4), left after step 42, 2 between. Late: reachable only after the answer to `sales[s3].route` (step 44), which its gate does not read.
- form f1095a re-entered at step 10 by `f1095a[mkt_a].uniform` (order 2), left after step 5, 4 between. Sorting: it was reachable (since step 6), and `$retirement@person[spouse]` was asked instead (the bank puts order 1 first).
- form person re-entered at step 14 by `person[spouse].under16` (order 2), left after step 1, 12 between. Sorting: it was reachable (since step 2), and `scope.other_income` was asked instead (the bank puts order 0 first).
- form sales re-entered at step 17 by `sales[s1].box` (order 2), left after step 8, 8 between. Sorting: it was reachable (since step 9), and `$dependent` was asked instead (within order 2, sorted by id).
- form sales re-entered at step 43 by `sales[s1].route` (order 5), left after step 21, 21 between. Sorting: it was reachable (since step 9), and `$w2@person[spouse]` was asked instead (within order 5, sorted by id).

### minimal returns

**every gate closed**: 82 questions, complete; order re-entries 4, form re-entries 5 sorting and 3 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 0:scope×3 · 1:f1095a×1 · 1:retirement×1 · 1:sales×1 · 2:dependent×1 · 2:household×3 · 2:person×1 · 2:s3×1 · 5:w2×1 · 8:interest×1 · 9:f8889×1 · 10:oi8z×1 · 10:div×1 · 10:f1040×3 · 10:f4952×2 · 10:f8863×1 · 10:f8959×1 · 10:ftc×1 · 10:person×4 · 10:refund×1 · 10:s1×10 · 10:s1a×3 · 10:s2×2 · 10:s3×9 · 10:sa×1 · 10:person×1 · 10:sa×1 · 5:sa×1 · 10:sa×7 · 10:sb×1 · 10:sd×2 · 10:sli×1 · 10:ssb×1 · 11:sc×1 · 12:s179×1 · 20:f2441×2 · 22:person×1 · 10:qbi×1 · 12:qbi×1 · 24:f5695×2 · 30:person×1

- order 5 re-entered at step 60 by `sa.gifts` (order 5), left after step 15, 44 between. Late: reachable only after the answer to `sa.elect_itemize` (step 59), which its gate does not read.
- order 10 re-entered at step 61 by `sa.excluded_income` (order 10), left after step 59, 1 between. Late: left for `sa.gifts` (order 5), which sorts earlier and was reachable only after the answer to `sa.elect_itemize` (step 59), which its gate does not read.
- order 10 re-entered at step 78 by `qbi.unsupported` (order 10), left after step 72, 5 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 77), which its gate does not read.
- order 12 re-entered at step 79 by `qbi.carryforward` (order 12), left after step 74, 4 between. Late: reachable only after the answer to `person[taxpayer].sav_trad` (step 77), which its gate does not read.
- form person re-entered at step 13 by `person[taxpayer].under16` (order 2), left after step 1, 11 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form f1040 re-entered at step 20 by `f1040.line25b` (order 10), left after step 2, 17 between. Sorting: it was reachable (since step 1), and `scope.other_income` was asked instead (the bank puts order 0 first).
- form person re-entered at step 28 by `person[taxpayer].age65` (order 10), left after step 13, 14 between. Sorting: it was reachable (since step 2), and `s3.adoption_any` was asked instead (the bank puts order 2 first).
- form s3 re-entered at step 48 by `s3.credit_bond` (order 10), left after step 14, 33 between. Sorting: it was reachable (since step 1), and `$w2@person[taxpayer]` was asked instead (the bank puts order 5 first).
- form person re-entered at step 58 by `person[taxpayer].blind` (order 10), left after step 31, 26 between. Late: reachable only after the answer to `sa.dependent` (step 57), which its gate does not read.
- form sa re-entered at step 59 by `sa.elect_itemize` (order 10), left after step 57, 1 between. Late: left for `person[taxpayer].blind` (order 10), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 57), which its gate does not read.
- form person re-entered at step 77 by `person[taxpayer].sav_trad` (order 22), left after step 58, 18 between. Sorting: it was reachable (since step 2), and `sa.elect_itemize` was asked instead (the bank puts order 10 first).
- form person re-entered at step 82 by `person[taxpayer].eic_ssn` (order 30), left after step 77, 4 between. Late: left for `qbi.unsupported` (order 10), which sorts earlier and was reachable only after the answer to `person[taxpayer].sav_trad` (step 77), which its gate does not read.

**div.any = true alone**: 88 questions, complete; order re-entries 4, form re-entries 6 sorting and 3 late, delayed children 3 sorting and 3 late.

- form div re-entered at step 77 by `div.box13` (order 15), left after step 19, 57 between. Sorting: it was reachable (since step 20), and `f1040.line25b` was asked instead (the bank puts order 10 first).
- `sb.ordinary_dividends` (order 10), step 69: child of `div.any` (step 19), 49 other questions between. Sorting: it was reachable (since step 20), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `sd.distributions` (order 10), step 71: child of `div.any` (step 19), 50 other questions between. Sorting: it was reachable (since step 20), and `f1040.line25b` was asked instead (within order 10, sorted by id).
- `div.box13` (order 15), step 77: child of `div.any` (step 19), 55 other questions between. Sorting: it was reachable (since step 20), and `f1040.line25b` was asked instead (the bank puts order 10 first).
- `div.box10` (order 15), step 78: child of `div.any` (step 19), 55 other questions between. Late: reachable only after the answer to `div.box13` (step 77), which its gate does not read.
- `div.box3` (order 15), step 79: child of `div.any` (step 19), 55 other questions between. Late: reachable only after the answer to `div.box13` (step 77), which its gate does not read.
- `div.box9` (order 15), step 80: child of `div.any` (step 19), 55 other questions between. Late: reachable only after the answer to `sd.distributions` (step 71), which its gate does not read.

**f4952.has_interest = true alone**: 84 questions, complete; order re-entries 4, form re-entries 5 sorting and 3 late, delayed children 0 sorting and 0 late.

**f8889.coverage_year = "family" alone**: 82 questions, complete; order re-entries 4, form re-entries 5 sorting and 3 late, delayed children 0 sorting and 0 late.

**f8889.coverage_year = "changed" alone**: 82 questions, complete; order re-entries 4, form re-entries 5 sorting and 3 late, delayed children 0 sorting and 0 late.

**s3.adoption_any = true alone**: 84 questions, complete; order re-entries 4, form re-entries 5 sorting and 3 late, delayed children 0 sorting and 0 late.

**s3.ev = true alone**: 85 questions, complete; order re-entries 4, form re-entries 5 sorting and 3 late, delayed children 0 sorting and 0 late.

**s3.farmland = true alone**: 83 questions, complete; order re-entries 4, form re-entries 5 sorting and 3 late, delayed children 0 sorting and 0 late.

**s3.foreign_any = true alone**: 86 questions, complete; order re-entries 4, form re-entries 6 sorting and 4 late, delayed children 3 sorting and 0 late.

- form ftc re-entered at step 53 by `ftc.carryover` (order 10), left after step 27, 25 between. Late: reachable only after the answer to `s3.foreign_any` (step 52), its parent or roster.
- form s3 re-entered at step 54 by `s3.kerosene` (order 10), left after step 52, 1 between. Sorting: left for `ftc.carryover` (order 10), a child of the question before it, which the bank places in another form.
- `s3.section960c` (order 10), step 58: child of `s3.foreign_any` (step 52), 4 other questions between. Sorting: it was reachable (since step 53), and `s3.kerosene` was asked instead (within order 10, sorted by id).
- `s3.section965` (order 10), step 59: child of `s3.foreign_any` (step 52), 4 other questions between. Sorting: it was reachable (since step 53), and `s3.kerosene` was asked instead (within order 10, sorted by id).
- `s3.virgin_islands` (order 10), step 60: child of `s3.foreign_any` (step 52), 4 other questions between. Sorting: it was reachable (since step 53), and `s3.kerosene` was asked instead (within order 10, sorted by id).

**s3.kerosene = true alone**: 83 questions, complete; order re-entries 4, form re-entries 5 sorting and 3 late, delayed children 0 sorting and 0 late.

**s3.prior_other_forms = true alone**: 85 questions, complete; order re-entries 4, form re-entries 6 sorting and 4 late, delayed children 0 sorting and 0 late.

- form ftc re-entered at step 56 by `ftc.carryover` (order 10), left after step 27, 28 between. Late: reachable only after the answer to `s3.prior_other_forms` (step 55), its parent or roster.
- form s3 re-entered at step 57 by `s3.prior_amt` (order 10), left after step 55, 1 between. Sorting: left for `ftc.carryover` (order 10), a child of the question before it, which the bank places in another form.

**sa.gifts = true alone**: 85 questions, complete; order re-entries 4, form re-entries 5 sorting and 4 late, delayed children 2 sorting and 0 late.

- order 10 re-entered at step 62 by `sa.charity_limited` (order 10), left after step 59, 2 between. Late: reachable only after the answer to `sa.gifts` (step 60), its parent or roster.
- form sa re-entered at step 62 by `sa.charity_limited` (order 10), left after step 60, 1 between. Late: left for `$gift` (order 5), which sorts earlier and was reachable only after the answer to `sa.gifts` (step 60), which its gate does not read.
- `sa.charity_limited` (order 10), step 62: child of `sa.gifts` (step 60), 1 other question between. Sorting: it was reachable (since step 61), and `$gift` was asked instead (the bank puts order 5 first).
- `sa.line11` (order 10), step 65: child of `sa.gifts` (step 60), 3 other questions between. Sorting: it was reachable (since step 61), and `$gift` was asked instead (the bank puts order 5 first).

**sb.foreign_any = true alone**: 86 questions, complete; order re-entries 4, form re-entries 5 sorting and 3 late, delayed children 0 sorting and 0 late.

