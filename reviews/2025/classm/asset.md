# Class M hand-work — asset

`Form 4562 — one item of depreciable property (other than a vehicle) of a business` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-20 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| cases | 4 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i4562 | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 34, 37, 39, 41, 98 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 34, 37, 39, 41 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

## Lines

### case classm.asset.1 — prompt sha256 8beadbee4694b2360127d72f4de608349b091d114bdc5bf19204c19d8951256a; branches: asset.outside:false, asset.screen:false, asset.screened:false, asset.pct_bad:false, asset.listed:false, asset.over_half:false, asset.over_half:true, asset.listed_low:false, asset.is2025:false, asset.is2025:true, asset.done:false, asset.s179_bad:false, asset.after179:positive, asset.after_jan19:false, asset.after_jan19:true, asset.bonus_same:true, asset.bonus_mixed:false, asset.bonus_fullcase#0, asset.bonus_fullcase#1, asset.bonus#0, asset.bonus#2, asset.ub:floor, asset.ub:positive, asset.macrs2025#0, asset.mq_q4_2025#0, asset.mq_q4_2025#3, asset.ub_prior_a:positive, asset.ub_prior:positive, asset.macrs_prior#0, asset.dep_2025#0, asset.dep_2025#1, asset.bonus_2025#0, asset.bonus_2025#1, asset.s179_2025#0, asset.s179_2025#1, asset.mq_q4#0, asset.mq_q4#1, asset.mq_total#0, asset.mq_total#1, asset.cost179#0, asset.cost179#1, asset.cost179_2025#0, asset.cost179_2025#1, asset.dep_prior#0, asset.dep_prior#1

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].period — Recovery period under GDS for the asset class
Status: **AGREE**

Value: y7

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].outside — The asset class is outside this tool
Status: **AGREE**

Value: no

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].screened — This property is outside this tool
Status: **AGREE**

Value: no

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].pct_c — The business use percentage, as cents
Status: **DISAGREE**

Project: $0.40
Model: $40.00
Work: 40% business use

Ruling: representation; project retained. The business-use percentage is carried as one cent per percentage point (multiply_count by one cent) so it can be divided like an amount; the model read the cents as dollars. Not evidence. [dropped]

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].pct_bad — The business use percentage is more than 100
Status: **AGREE**

Value: no

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].over_half — Business use is more than 50%
Status: **AGREE**

Value: no

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].listed_low — Listed property used 50% or less for business, or a percentage over 100
Status: **AGREE**

Value: no

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].basis — Basis for depreciation (business/investment use only), before section 179 and th
Status: **AGREE**

Value: $16,578.80

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].is2025 — Placed in service in 2025
Status: **AGREE**

Value: yes

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].year — Year of recovery in 2025
Status: **AGREE**

Value: 1

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].last — Last year of recovery for the recovery period
Status: **AGREE**

Value: 8

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].done — The recovery period ended before 2025
Status: **AGREE**

Value: no

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq1

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].s179_bad — The section 179 election is more than the business cost, or the property is not 
Status: **AGREE**

Value: no

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].after179 — Basis less the section 179 election
Status: **AGREE**

Value: $16,578.80

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].bonus_mixed — The special allowance choice differs within a class
Status: **AGREE**

Value: no

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].bonus_full — 100% special allowance
Status: **AGREE**

Value: $16,578.80

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].bonus_forty — 40% special allowance
Status: **AGREE**

Value: $6,631.52

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **AGREE**

Value: $16,578.80

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].bonus — Special depreciation allowance for this property
Status: **AGREE**

Value: $16,578.80

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].ub — Basis for MACRS depreciation (after section 179 and the special allowance)
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].rate_hy — MACRS rate, half-year convention
Status: **AGREE**

Value: 14.29%

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].rate_mq — MACRS rate, mid-quarter convention
Status: **AGREE**

Value: 25%

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].macrs_hy — MACRS depreciation, half-year convention
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].macrs_mq — MACRS depreciation, mid-quarter convention
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].macrs2025 — MACRS depreciation for 2025 property
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].mqbase — Depreciable basis for the mid-quarter test (after section 179, before the specia
Status: **AGREE**

Value: $16,578.80

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].mq_q4_2025 — That basis when placed in service October to December
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].ub_prior_a — Business basis less the section 179 deduction
Status: **AGREE**

Value: $16,578.80

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].ub_prior — Unadjusted basis
Status: **AGREE**

Value: $16,578.80

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].rate_prior — MACRS rate for the 2025 year of recovery
Status: **AGREE**

Value: 3.57%

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].macrs_prior_live — MACRS depreciation for 2025
Status: **AGREE**

Value: $591.86

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].macrs_prior — MACRS deduction for 2025 on property placed in service before 2025
Status: **DISAGREE**

Project: $591.86
Model: $0.00
Work: Placed in service in 2025, not before

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the 2025 lines for earlier property and the reverse, the listed-property lines for property that is not listed and the reverse, the lines after a zero basis); the Form 4562 totals take each only where it belongs (sc sums with the 2025 and listed filters), and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].dep_2025 — MACRS on 2025 property
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].bonus_2025 — Special allowance on 2025 property
Status: **AGREE**

Value: $16,578.80

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].s179_2025 — Section 179 elected on 2025 property
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].mq_q4 — Mid-quarter test basis, fourth quarter
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].mq_total — Mid-quarter test basis, all of 2025
Status: **AGREE**

Value: $16,578.80

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].cost179 — Cost of section 179 property placed in service in 2025
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].cost179_2025 — The business cost when used more than 50% in the business
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].dep_prior — MACRS on property placed in service before 2025
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].dep_listed — Depreciation of this listed property (column (h))
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].period — Recovery period under GDS for the asset class
Status: **AGREE**

Value: y20

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].outside — The asset class is outside this tool
Status: **AGREE**

Value: no

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].screened — This property is outside this tool
Status: **AGREE**

Value: no

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].pct_c — The business use percentage, as cents
Status: **DISAGREE**

Project: $1.00
Model: $100.00
Work: 100% business use

Ruling: representation; project retained. The business-use percentage is carried as one cent per percentage point (multiply_count by one cent) so it can be divided like an amount; the model read the cents as dollars. Not evidence. [dropped]

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].pct_bad — The business use percentage is more than 100
Status: **AGREE**

Value: no

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].listed_low — Listed property used 50% or less for business, or a percentage over 100
Status: **AGREE**

Value: no

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].basis — Basis for depreciation (business/investment use only), before section 179 and th
Status: **AGREE**

Value: $20,222.00

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].is2025 — Placed in service in 2025
Status: **AGREE**

Value: no

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].year — Year of recovery in 2025
Status: **AGREE**

Value: 16

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].last — Last year of recovery for the recovery period
Status: **AGREE**

Value: 21

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].done — The recovery period ended before 2025
Status: **AGREE**

Value: no

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq4

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].s179_bad — The section 179 election is more than the business cost, or the property is not 
Status: **AGREE**

Value: no

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].after179 — Basis less the section 179 election
Status: **AGREE**

Value: $20,222.00

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].bonus_mixed — The special allowance choice differs within a class
Status: **AGREE**

Value: no

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].bonus_full — 100% special allowance
Status: **AGREE**

Value: $20,222.00

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].bonus_forty — 40% special allowance
Status: **AGREE**

Value: $8,088.80

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **AGREE**

Value: $8,088.80

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].bonus — Special depreciation allowance for this property
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].ub — Basis for MACRS depreciation (after section 179 and the special allowance)
Status: **AGREE**

Value: $20,222.00

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].rate_hy — MACRS rate, half-year convention
Status: **DISAGREE**

Project: 4.461%
Model: 3.75%
Work: 20-yr 150DB, HY, year 1

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the 2025 lines for earlier property and the reverse, the listed-property lines for property that is not listed and the reverse, the lines after a zero basis); the Form 4562 totals take each only where it belongs (sc sums with the 2025 and listed filters), and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].rate_mq — MACRS rate, mid-quarter convention
Status: **DISAGREE**

Project: 4.458%
Model: 0.938%
Work: 20-yr, MQ fourth quarter, year 1 (7.5% x 0.125)

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the 2025 lines for earlier property and the reverse, the listed-property lines for property that is not listed and the reverse, the lines after a zero basis); the Form 4562 totals take each only where it belongs (sc sums with the 2025 and listed filters), and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].macrs_hy — MACRS depreciation, half-year convention
Status: **DISAGREE**

Project: $902.10
Model: $758.33
Work: 20,222.00 x 3.750%

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the 2025 lines for earlier property and the reverse, the listed-property lines for property that is not listed and the reverse, the lines after a zero basis); the Form 4562 totals take each only where it belongs (sc sums with the 2025 and listed filters), and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].macrs_mq — MACRS depreciation, mid-quarter convention
Status: **DISAGREE**

Project: $901.50
Model: $189.68
Work: 20,222.00 x 0.938%

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the 2025 lines for earlier property and the reverse, the listed-property lines for property that is not listed and the reverse, the lines after a zero basis); the Form 4562 totals take each only where it belongs (sc sums with the 2025 and listed filters), and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].macrs2025 — MACRS depreciation for 2025 property
Status: **DISAGREE**

Project: $902.10
Model: $758.33
Work: Mid-quarter test is no, so use HY amount

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the 2025 lines for earlier property and the reverse, the listed-property lines for property that is not listed and the reverse, the lines after a zero basis); the Form 4562 totals take each only where it belongs (sc sums with the 2025 and listed filters), and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].mqbase — Depreciable basis for the mid-quarter test (after section 179, before the specia
Status: **AGREE**

Value: $20,222.00

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].mq_q4_2025 — That basis when placed in service October to December
Status: **AGREE**

Value: $20,222.00

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].ub_prior_a — Business basis less the section 179 deduction
Status: **AGREE**

Value: $20,222.00

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].ub_prior — Unadjusted basis
Status: **AGREE**

Value: $20,222.00

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].rate_prior — MACRS rate for the 2025 year of recovery
Status: **AGREE**

Value: 4.458%

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].macrs_prior_live — MACRS depreciation for 2025
Status: **AGREE**

Value: $901.50

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].macrs_prior — MACRS deduction for 2025 on property placed in service before 2025
Status: **AGREE**

Value: $901.50

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].dep_2025 — MACRS on 2025 property
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].bonus_2025 — Special allowance on 2025 property
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].s179_2025 — Section 179 elected on 2025 property
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].mq_q4 — Mid-quarter test basis, fourth quarter
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].mq_total — Mid-quarter test basis, all of 2025
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].cost179 — Cost of section 179 property placed in service in 2025
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].cost179_2025 — The business cost when used more than 50% in the business
Status: **AGREE**

Value: $20,222.00

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].dep_prior — MACRS on property placed in service before 2025
Status: **AGREE**

Value: $901.50

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].dep_listed — Depreciation of this listed property (column (h))
Status: **DISAGREE**

Project: $901.50
Model: $0.00
Work: Not listed property

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the 2025 lines for earlier property and the reverse, the listed-property lines for property that is not listed and the reverse, the lines after a zero basis); the Form 4562 totals take each only where it belongs (sc sums with the 2025 and listed filters), and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### case classm.asset.2 — prompt sha256 be8a5de7e3d33c6a7cfc2322b720bc807bb3cf8fae484eaf69a1c58d51ca9a97; branches: asset.outside:false, asset.screen:false, asset.screened:false, asset.pct_bad:false, asset.listed:false, asset.listed:true, asset.over_half:true, asset.listed_low:false, asset.is2025:true, asset.done:false, asset.s179_bad:false, asset.after179:positive, asset.after_jan19:true, asset.bonus_same:true, asset.bonus_mixed:false, asset.bonus_fullcase#0, asset.bonus#1, asset.ub:positive, asset.macrs2025#1, asset.mq_q4_2025#1, asset.mq_q4_2025#3, asset.ub_prior_a:positive, asset.ub_prior:positive, asset.macrs_prior#0, asset.dep_2025#0, asset.bonus_2025#0, asset.s179_2025#0, asset.mq_q4#0, asset.mq_total#0, asset.cost179#0, asset.cost179_2025#0, asset.dep_prior#1

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].period — Recovery period under GDS for the asset class
Status: **DISAGREE**

Project: y7
Model: y15
Work: Pub. 946 Table B-2, class 48.41 telephone distribution plant: GDS recovery period 15 years

Ruling: model error; project retained. The model took the recovery period from memory ('recalled'): Pub. 946 Table B-2 (archived p946, Appendix B) gives class 48.41 (CATV, Headend) a class life of 11 years and a GDS period of 7, and class 48.44 (CATV, Service and Test) 8.5 and 5, as the project's class_lives table has them (and the table's second transcription agrees, reviews/2025/tables/class_lives.json); the model's rates, last recovery years and MACRS amounts for the asset follow from its wrong period. Not evidence. [dropped]

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].outside — The asset class is outside this tool
Status: **AGREE**

Value: no

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].screened — This property is outside this tool
Status: **AGREE**

Value: no

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].pct_c — The business use percentage, as cents
Status: **DISAGREE**

Project: $1.00
Model: $100.00
Work: 100% business use

Ruling: representation; project retained. The business-use percentage is carried as one cent per percentage point (multiply_count by one cent) so it can be divided like an amount; the model read the cents as dollars. Not evidence. [dropped]

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].pct_bad — The business use percentage is more than 100
Status: **AGREE**

Value: no

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].listed_low — Listed property used 50% or less for business, or a percentage over 100
Status: **AGREE**

Value: no

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].basis — Basis for depreciation (business/investment use only), before section 179 and th
Status: **AGREE**

Value: $44,464.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].is2025 — Placed in service in 2025
Status: **AGREE**

Value: yes

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].year — Year of recovery in 2025
Status: **AGREE**

Value: 1

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].last — Last year of recovery for the recovery period
Status: **DISAGREE**

Project: 8
Model: 16
Work: 15-year property; the convention adds one more year: 15 + 1

Ruling: model error; project retained. The model took the recovery period from memory ('recalled'): Pub. 946 Table B-2 (archived p946, Appendix B) gives class 48.41 (CATV, Headend) a class life of 11 years and a GDS period of 7, and class 48.44 (CATV, Service and Test) 8.5 and 5, as the project's class_lives table has them (and the table's second transcription agrees, reviews/2025/tables/class_lives.json); the model's rates, last recovery years and MACRS amounts for the asset follow from its wrong period. Not evidence. [dropped]

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].done — The recovery period ended before 2025
Status: **AGREE**

Value: no

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq2

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].s179_bad — The section 179 election is more than the business cost, or the property is not 
Status: **AGREE**

Value: no

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].after179 — Basis less the section 179 election
Status: **AGREE**

Value: $44,464.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].bonus_mixed — The special allowance choice differs within a class
Status: **AGREE**

Value: no

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].bonus_full — 100% special allowance
Status: **AGREE**

Value: $44,464.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].bonus_forty — 40% special allowance
Status: **AGREE**

Value: $17,785.60

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **AGREE**

Value: $44,464.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].bonus — Special depreciation allowance for this property
Status: **AGREE**

Value: $17,785.60

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].ub — Basis for MACRS depreciation (after section 179 and the special allowance)
Status: **AGREE**

Value: $26,678.40

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].rate_hy — MACRS rate, half-year convention
Status: **DISAGREE**

Project: 14.29%
Model: 5%
Work: 150DB: 1.5/15 = 10%, x 0.5 for half-year

Ruling: model error; project retained. The model took the recovery period from memory ('recalled'): Pub. 946 Table B-2 (archived p946, Appendix B) gives class 48.41 (CATV, Headend) a class life of 11 years and a GDS period of 7, and class 48.44 (CATV, Service and Test) 8.5 and 5, as the project's class_lives table has them (and the table's second transcription agrees, reviews/2025/tables/class_lives.json); the model's rates, last recovery years and MACRS amounts for the asset follow from its wrong period. Not evidence. [dropped]

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].rate_mq — MACRS rate, mid-quarter convention
Status: **DISAGREE**

Project: 17.85%
Model: 6.25%
Work: 10% x 0.625 for quarter 2

Ruling: model error; project retained. The model took the recovery period from memory ('recalled'): Pub. 946 Table B-2 (archived p946, Appendix B) gives class 48.41 (CATV, Headend) a class life of 11 years and a GDS period of 7, and class 48.44 (CATV, Service and Test) 8.5 and 5, as the project's class_lives table has them (and the table's second transcription agrees, reviews/2025/tables/class_lives.json); the model's rates, last recovery years and MACRS amounts for the asset follow from its wrong period. Not evidence. [dropped]

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].macrs_hy — MACRS depreciation, half-year convention
Status: **DISAGREE**

Project: $3,812.34
Model: $1,333.92
Work: 26,678.40 x 5.00%

Ruling: model error; project retained. The model took the recovery period from memory ('recalled'): Pub. 946 Table B-2 (archived p946, Appendix B) gives class 48.41 (CATV, Headend) a class life of 11 years and a GDS period of 7, and class 48.44 (CATV, Service and Test) 8.5 and 5, as the project's class_lives table has them (and the table's second transcription agrees, reviews/2025/tables/class_lives.json); the model's rates, last recovery years and MACRS amounts for the asset follow from its wrong period. Not evidence. [dropped]

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].macrs_mq — MACRS depreciation, mid-quarter convention
Status: **DISAGREE**

Project: $4,762.09
Model: $1,667.40
Work: 26,678.40 x 6.25%

Ruling: model error; project retained. The model took the recovery period from memory ('recalled'): Pub. 946 Table B-2 (archived p946, Appendix B) gives class 48.41 (CATV, Headend) a class life of 11 years and a GDS period of 7, and class 48.44 (CATV, Service and Test) 8.5 and 5, as the project's class_lives table has them (and the table's second transcription agrees, reviews/2025/tables/class_lives.json); the model's rates, last recovery years and MACRS amounts for the asset follow from its wrong period. Not evidence. [dropped]

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].macrs2025 — MACRS depreciation for 2025 property
Status: **DISAGREE**

Project: $4,762.09
Model: $1,667.40
Work: Mid-quarter convention applies (test = yes)

Ruling: model error; project retained. The model took the recovery period from memory ('recalled'): Pub. 946 Table B-2 (archived p946, Appendix B) gives class 48.41 (CATV, Headend) a class life of 11 years and a GDS period of 7, and class 48.44 (CATV, Service and Test) 8.5 and 5, as the project's class_lives table has them (and the table's second transcription agrees, reviews/2025/tables/class_lives.json); the model's rates, last recovery years and MACRS amounts for the asset follow from its wrong period. Not evidence. [dropped]

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].mqbase — Depreciable basis for the mid-quarter test (after section 179, before the specia
Status: **AGREE**

Value: $44,464.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].mq_q4_2025 — That basis when placed in service October to December
Status: **AGREE**

Value: $0.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].ub_prior_a — Business basis less the section 179 deduction
Status: **AGREE**

Value: $44,464.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].ub_prior — Unadjusted basis
Status: **AGREE**

Value: $44,464.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].rate_prior — MACRS rate for the 2025 year of recovery
Status: **DISAGREE**

Project: 3.57%
Model: 1.25%
Work: 15-year property, mq4 convention, year 1: 10% x 0.125

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the 2025 lines for earlier property and the reverse, the listed-property lines for property that is not listed and the reverse, the lines after a zero basis); the Form 4562 totals take each only where it belongs (sc sums with the 2025 and listed filters), and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].macrs_prior_live — MACRS depreciation for 2025
Status: **DISAGREE**

Project: $1,587.36
Model: $555.80
Work: 44,464.00 x 1.25%

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the 2025 lines for earlier property and the reverse, the listed-property lines for property that is not listed and the reverse, the lines after a zero basis); the Form 4562 totals take each only where it belongs (sc sums with the 2025 and listed filters), and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].macrs_prior — MACRS deduction for 2025 on property placed in service before 2025
Status: **DISAGREE**

Project: $1,587.36
Model: $0.00
Work: Placed in service in 2025, not before 2025

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the 2025 lines for earlier property and the reverse, the listed-property lines for property that is not listed and the reverse, the lines after a zero basis); the Form 4562 totals take each only where it belongs (sc sums with the 2025 and listed filters), and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].dep_2025 — MACRS on 2025 property
Status: **DISAGREE**

Project: $4,762.09
Model: $1,667.40
Work: Line 19 MACRS on 2025 property that is not listed

Ruling: model error; project retained. The model took the recovery period from memory ('recalled'): Pub. 946 Table B-2 (archived p946, Appendix B) gives class 48.41 (CATV, Headend) a class life of 11 years and a GDS period of 7, and class 48.44 (CATV, Service and Test) 8.5 and 5, as the project's class_lives table has them (and the table's second transcription agrees, reviews/2025/tables/class_lives.json); the model's rates, last recovery years and MACRS amounts for the asset follow from its wrong period. Not evidence. [dropped]

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].bonus_2025 — Special allowance on 2025 property
Status: **AGREE**

Value: $17,785.60

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].s179_2025 — Section 179 elected on 2025 property
Status: **AGREE**

Value: $0.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].mq_q4 — Mid-quarter test basis, fourth quarter
Status: **AGREE**

Value: $0.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].mq_total — Mid-quarter test basis, all of 2025
Status: **AGREE**

Value: $44,464.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].cost179 — Cost of section 179 property placed in service in 2025
Status: **AGREE**

Value: $44,464.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].cost179_2025 — The business cost when used more than 50% in the business
Status: **AGREE**

Value: $44,464.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].dep_prior — MACRS on property placed in service before 2025
Status: **AGREE**

Value: $0.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].dep_listed — Depreciation of this listed property (column (h))
Status: **DISAGREE**

Project: $4,762.09
Model: $0.00
Work: Not listed property

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the 2025 lines for earlier property and the reverse, the listed-property lines for property that is not listed and the reverse, the lines after a zero basis); the Form 4562 totals take each only where it belongs (sc sums with the 2025 and listed filters), and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].period — Recovery period under GDS for the asset class
Status: **AGREE**

Value: y5

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].outside — The asset class is outside this tool
Status: **AGREE**

Value: no

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].screened — This property is outside this tool
Status: **AGREE**

Value: no

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].pct_c — The business use percentage, as cents
Status: **DISAGREE**

Project: $1.00
Model: $100.00
Work: 100% business use

Ruling: representation; project retained. The business-use percentage is carried as one cent per percentage point (multiply_count by one cent) so it can be divided like an amount; the model read the cents as dollars. Not evidence. [dropped]

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].pct_bad — The business use percentage is more than 100
Status: **AGREE**

Value: no

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].listed_low — Listed property used 50% or less for business, or a percentage over 100
Status: **AGREE**

Value: no

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].basis — Basis for depreciation (business/investment use only), before section 179 and th
Status: **AGREE**

Value: $43,875.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].is2025 — Placed in service in 2025
Status: **AGREE**

Value: yes

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].year — Year of recovery in 2025
Status: **AGREE**

Value: 1

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].last — Last year of recovery for the recovery period
Status: **AGREE**

Value: 6

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].done — The recovery period ended before 2025
Status: **AGREE**

Value: no

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq4

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].s179_bad — The section 179 election is more than the business cost, or the property is not 
Status: **AGREE**

Value: no

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].after179 — Basis less the section 179 election
Status: **AGREE**

Value: $43,875.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].bonus_mixed — The special allowance choice differs within a class
Status: **AGREE**

Value: no

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].bonus_full — 100% special allowance
Status: **AGREE**

Value: $43,875.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].bonus_forty — 40% special allowance
Status: **AGREE**

Value: $17,550.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **AGREE**

Value: $43,875.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].bonus — Special depreciation allowance for this property
Status: **AGREE**

Value: $17,550.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].ub — Basis for MACRS depreciation (after section 179 and the special allowance)
Status: **AGREE**

Value: $26,325.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].rate_hy — MACRS rate, half-year convention
Status: **AGREE**

Value: 20%

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].rate_mq — MACRS rate, mid-quarter convention
Status: **AGREE**

Value: 5%

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].macrs_hy — MACRS depreciation, half-year convention
Status: **AGREE**

Value: $5,265.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].macrs_mq — MACRS depreciation, mid-quarter convention
Status: **AGREE**

Value: $1,316.25

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].macrs2025 — MACRS depreciation for 2025 property
Status: **AGREE**

Value: $1,316.25

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].mqbase — Depreciable basis for the mid-quarter test (after section 179, before the specia
Status: **AGREE**

Value: $43,875.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].mq_q4_2025 — That basis when placed in service October to December
Status: **AGREE**

Value: $43,875.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].ub_prior_a — Business basis less the section 179 deduction
Status: **AGREE**

Value: $43,875.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].ub_prior — Unadjusted basis
Status: **AGREE**

Value: $43,875.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].rate_prior — MACRS rate for the 2025 year of recovery
Status: **AGREE**

Value: 20%

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].macrs_prior_live — MACRS depreciation for 2025
Status: **AGREE**

Value: $8,775.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].macrs_prior — MACRS deduction for 2025 on property placed in service before 2025
Status: **DISAGREE**

Project: $8,775.00
Model: $0.00
Work: Placed in service in 2025, not before 2025

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the 2025 lines for earlier property and the reverse, the listed-property lines for property that is not listed and the reverse, the lines after a zero basis); the Form 4562 totals take each only where it belongs (sc sums with the 2025 and listed filters), and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].dep_2025 — MACRS on 2025 property
Status: **DISAGREE**

Project: $1,316.25
Model: $0.00
Work: Listed property is reported in Part V, not line 19

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the 2025 lines for earlier property and the reverse, the listed-property lines for property that is not listed and the reverse, the lines after a zero basis); the Form 4562 totals take each only where it belongs (sc sums with the 2025 and listed filters), and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].bonus_2025 — Special allowance on 2025 property
Status: **DISAGREE**

Project: $17,550.00
Model: $0.00
Work: Line 14 excludes listed property; its allowance goes on line 25

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the 2025 lines for earlier property and the reverse, the listed-property lines for property that is not listed and the reverse, the lines after a zero basis); the Form 4562 totals take each only where it belongs (sc sums with the 2025 and listed filters), and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].s179_2025 — Section 179 elected on 2025 property
Status: **AGREE**

Value: $0.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].mq_q4 — Mid-quarter test basis, fourth quarter
Status: **AGREE**

Value: $43,875.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].mq_total — Mid-quarter test basis, all of 2025
Status: **AGREE**

Value: $43,875.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].cost179 — Cost of section 179 property placed in service in 2025
Status: **AGREE**

Value: $43,875.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].cost179_2025 — The business cost when used more than 50% in the business
Status: **AGREE**

Value: $43,875.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].dep_prior — MACRS on property placed in service before 2025
Status: **AGREE**

Value: $0.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].dep_listed — Depreciation of this listed property (column (h))
Status: **AGREE**

Value: $1,316.25

### case classm.asset.3 — prompt sha256 5c415bb9287290c4b8397c08ed29f4cc83ffb2e63eda24e3358a94c082ac83ad; branches: asset.outside:false, asset.screen:false, asset.screened:false, asset.pct_bad:false, asset.listed:false, asset.over_half:false, asset.over_half:true, asset.listed_low:false, asset.is2025:true, asset.done:false, asset.s179_bad:false, asset.after179:floor, asset.after179:positive, asset.after_jan19:false, asset.after_jan19:true, asset.bonus_same:true, asset.bonus_mixed:false, asset.bonus_fullcase#0, asset.bonus_fullcase#1, asset.bonus#0, asset.bonus#2, asset.ub:floor, asset.ub:positive, asset.macrs2025#0, asset.mq_q4_2025#0, asset.mq_q4_2025#2, asset.ub_prior_a:positive, asset.ub_prior:positive, asset.macrs_prior#0, asset.dep_2025#0, asset.bonus_2025#0, asset.s179_2025#0, asset.mq_q4#0, asset.mq_total#0, asset.cost179#0, asset.cost179_2025#0, asset.cost179_2025#1, asset.dep_prior#1

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].period — Recovery period under GDS for the asset class
Status: **AGREE**

Value: y7

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].outside — The asset class is outside this tool
Status: **AGREE**

Value: no

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].screened — This property is outside this tool
Status: **AGREE**

Value: no

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].pct_c — The business use percentage, as cents
Status: **DISAGREE**

Project: $0.30
Model: $30.00
Work: 30%

Ruling: representation; project retained. The business-use percentage is carried as one cent per percentage point (multiply_count by one cent) so it can be divided like an amount; the model read the cents as dollars. Not evidence. [dropped]

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].pct_bad — The business use percentage is more than 100
Status: **AGREE**

Value: no

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].over_half — Business use is more than 50%
Status: **AGREE**

Value: no

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].listed_low — Listed property used 50% or less for business, or a percentage over 100
Status: **AGREE**

Value: no

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].basis — Basis for depreciation (business/investment use only), before section 179 and th
Status: **AGREE**

Value: $11,538.90

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].is2025 — Placed in service in 2025
Status: **AGREE**

Value: yes

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].year — Year of recovery in 2025
Status: **AGREE**

Value: 1

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].last — Last year of recovery for the recovery period
Status: **AGREE**

Value: 8

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].done — The recovery period ended before 2025
Status: **AGREE**

Value: no

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq1

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].s179_bad — The section 179 election is more than the business cost, or the property is not 
Status: **AGREE**

Value: no

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].after179 — Basis less the section 179 election
Status: **AGREE**

Value: $11,538.90

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].bonus_mixed — The special allowance choice differs within a class
Status: **AGREE**

Value: no

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].bonus_full — 100% special allowance
Status: **AGREE**

Value: $11,538.90

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].bonus_forty — 40% special allowance
Status: **AGREE**

Value: $4,615.56

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **AGREE**

Value: $4,615.56

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].bonus — Special depreciation allowance for this property
Status: **AGREE**

Value: $4,615.56

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].ub — Basis for MACRS depreciation (after section 179 and the special allowance)
Status: **AGREE**

Value: $6,923.34

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].rate_hy — MACRS rate, half-year convention
Status: **AGREE**

Value: 14.29%

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].rate_mq — MACRS rate, mid-quarter convention
Status: **AGREE**

Value: 25%

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].macrs_hy — MACRS depreciation, half-year convention
Status: **AGREE**

Value: $989.35

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].macrs_mq — MACRS depreciation, mid-quarter convention
Status: **AGREE**

Value: $1,730.84

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].macrs2025 — MACRS depreciation for 2025 property
Status: **AGREE**

Value: $989.35

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].mqbase — Depreciable basis for the mid-quarter test (after section 179, before the specia
Status: **AGREE**

Value: $11,538.90

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].mq_q4_2025 — That basis when placed in service October to December
Status: **AGREE**

Value: $0.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].ub_prior_a — Business basis less the section 179 deduction
Status: **AGREE**

Value: $11,538.90

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].ub_prior — Unadjusted basis
Status: **AGREE**

Value: $11,538.90

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].rate_prior — MACRS rate for the 2025 year of recovery
Status: **AGREE**

Value: 17.85%

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].macrs_prior_live — MACRS depreciation for 2025
Status: **AGREE**

Value: $2,059.69

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].macrs_prior — MACRS deduction for 2025 on property placed in service before 2025
Status: **DISAGREE**

Project: $2,059.69
Model: $0.00
Work: Placed in service in 2025, not before 2025

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the 2025 lines for earlier property and the reverse, the listed-property lines for property that is not listed and the reverse, the lines after a zero basis); the Form 4562 totals take each only where it belongs (sc sums with the 2025 and listed filters), and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].dep_2025 — MACRS on 2025 property
Status: **AGREE**

Value: $989.35

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].bonus_2025 — Special allowance on 2025 property
Status: **AGREE**

Value: $4,615.56

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].s179_2025 — Section 179 elected on 2025 property
Status: **AGREE**

Value: $0.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].mq_q4 — Mid-quarter test basis, fourth quarter
Status: **AGREE**

Value: $0.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].mq_total — Mid-quarter test basis, all of 2025
Status: **AGREE**

Value: $11,538.90

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].cost179 — Cost of section 179 property placed in service in 2025
Status: **AGREE**

Value: $0.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].cost179_2025 — The business cost when used more than 50% in the business
Status: **AGREE**

Value: $0.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].dep_prior — MACRS on property placed in service before 2025
Status: **AGREE**

Value: $0.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].dep_listed — Depreciation of this listed property (column (h))
Status: **DISAGREE**

Project: $989.35
Model: $0.00
Work: Not listed property

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the 2025 lines for earlier property and the reverse, the listed-property lines for property that is not listed and the reverse, the lines after a zero basis); the Form 4562 totals take each only where it belongs (sc sums with the 2025 and listed filters), and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].period — Recovery period under GDS for the asset class
Status: **DISAGREE**

Project: y5
Model: y7
Work: Pub. 946 asset class 48.44 (customer premises equipment): class life 10 years, GDS 7 years; recalled, the class table was not provided

Ruling: model error; project retained. The model took the recovery period from memory ('recalled'): Pub. 946 Table B-2 (archived p946, Appendix B) gives class 48.41 (CATV, Headend) a class life of 11 years and a GDS period of 7, and class 48.44 (CATV, Service and Test) 8.5 and 5, as the project's class_lives table has them (and the table's second transcription agrees, reviews/2025/tables/class_lives.json); the model's rates, last recovery years and MACRS amounts for the asset follow from its wrong period. Not evidence. [dropped]

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].outside — The asset class is outside this tool
Status: **AGREE**

Value: no

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].screened — This property is outside this tool
Status: **AGREE**

Value: no

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].pct_c — The business use percentage, as cents
Status: **DISAGREE**

Project: $1.00
Model: $100.00
Work: 100%

Ruling: representation; project retained. The business-use percentage is carried as one cent per percentage point (multiply_count by one cent) so it can be divided like an amount; the model read the cents as dollars. Not evidence. [dropped]

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].pct_bad — The business use percentage is more than 100
Status: **AGREE**

Value: no

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].listed_low — Listed property used 50% or less for business, or a percentage over 100
Status: **AGREE**

Value: no

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].basis — Basis for depreciation (business/investment use only), before section 179 and th
Status: **AGREE**

Value: $6,126.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].is2025 — Placed in service in 2025
Status: **AGREE**

Value: yes

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].year — Year of recovery in 2025
Status: **AGREE**

Value: 1

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].last — Last year of recovery for the recovery period
Status: **DISAGREE**

Project: 6
Model: 8
Work: 7-year property runs 8 tax years

Ruling: model error; project retained. The model took the recovery period from memory ('recalled'): Pub. 946 Table B-2 (archived p946, Appendix B) gives class 48.41 (CATV, Headend) a class life of 11 years and a GDS period of 7, and class 48.44 (CATV, Service and Test) 8.5 and 5, as the project's class_lives table has them (and the table's second transcription agrees, reviews/2025/tables/class_lives.json); the model's rates, last recovery years and MACRS amounts for the asset follow from its wrong period. Not evidence. [dropped]

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].done — The recovery period ended before 2025
Status: **AGREE**

Value: no

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq3

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].s179_bad — The section 179 election is more than the business cost, or the property is not 
Status: **AGREE**

Value: no

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].after179 — Basis less the section 179 election
Status: **AGREE**

Value: $0.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].bonus_mixed — The special allowance choice differs within a class
Status: **AGREE**

Value: no

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].bonus_full — 100% special allowance
Status: **AGREE**

Value: $0.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].bonus_forty — 40% special allowance
Status: **AGREE**

Value: $0.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **AGREE**

Value: $0.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].bonus — Special depreciation allowance for this property
Status: **AGREE**

Value: $0.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].ub — Basis for MACRS depreciation (after section 179 and the special allowance)
Status: **AGREE**

Value: $0.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].rate_hy — MACRS rate, half-year convention
Status: **DISAGREE**

Project: 20%
Model: 14.29%
Work: 7-year, half-year, year 1

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the 2025 lines for earlier property and the reverse, the listed-property lines for property that is not listed and the reverse, the lines after a zero basis); the Form 4562 totals take each only where it belongs (sc sums with the 2025 and listed filters), and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].rate_mq — MACRS rate, mid-quarter convention
Status: **DISAGREE**

Project: 15%
Model: 10.71%
Work: 7-year, mid-quarter Q3, year 1

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the 2025 lines for earlier property and the reverse, the listed-property lines for property that is not listed and the reverse, the lines after a zero basis); the Form 4562 totals take each only where it belongs (sc sums with the 2025 and listed filters), and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].macrs_hy — MACRS depreciation, half-year convention
Status: **AGREE**

Value: $0.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].macrs_mq — MACRS depreciation, mid-quarter convention
Status: **AGREE**

Value: $0.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].macrs2025 — MACRS depreciation for 2025 property
Status: **AGREE**

Value: $0.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].mqbase — Depreciable basis for the mid-quarter test (after section 179, before the specia
Status: **AGREE**

Value: $0.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].mq_q4_2025 — That basis when placed in service October to December
Status: **AGREE**

Value: $0.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].ub_prior_a — Business basis less the section 179 deduction
Status: **AGREE**

Value: $6,126.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].ub_prior — Unadjusted basis
Status: **AGREE**

Value: $6,126.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].rate_prior — MACRS rate for the 2025 year of recovery
Status: **DISAGREE**

Project: 25%
Model: 17.85%
Work: 7-year, mid-quarter Q2 (mq2), recovery year 1

Ruling: model error; project retained. The model took the recovery period from memory ('recalled'): Pub. 946 Table B-2 (archived p946, Appendix B) gives class 48.41 (CATV, Headend) a class life of 11 years and a GDS period of 7, and class 48.44 (CATV, Service and Test) 8.5 and 5, as the project's class_lives table has them (and the table's second transcription agrees, reviews/2025/tables/class_lives.json); the model's rates, last recovery years and MACRS amounts for the asset follow from its wrong period. Not evidence. [dropped]

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].macrs_prior_live — MACRS depreciation for 2025
Status: **DISAGREE**

Project: $1,531.50
Model: $1,093.49
Work: 6,126.00 x 17.85%

Ruling: model error; project retained. The model took the recovery period from memory ('recalled'): Pub. 946 Table B-2 (archived p946, Appendix B) gives class 48.41 (CATV, Headend) a class life of 11 years and a GDS period of 7, and class 48.44 (CATV, Service and Test) 8.5 and 5, as the project's class_lives table has them (and the table's second transcription agrees, reviews/2025/tables/class_lives.json); the model's rates, last recovery years and MACRS amounts for the asset follow from its wrong period. Not evidence. [dropped]

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].macrs_prior — MACRS deduction for 2025 on property placed in service before 2025
Status: **DISAGREE**

Project: $1,531.50
Model: $0.00
Work: Placed in service in 2025, not before 2025

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the 2025 lines for earlier property and the reverse, the listed-property lines for property that is not listed and the reverse, the lines after a zero basis); the Form 4562 totals take each only where it belongs (sc sums with the 2025 and listed filters), and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].dep_2025 — MACRS on 2025 property
Status: **AGREE**

Value: $0.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].bonus_2025 — Special allowance on 2025 property
Status: **AGREE**

Value: $0.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].s179_2025 — Section 179 elected on 2025 property
Status: **AGREE**

Value: $6,126.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].mq_q4 — Mid-quarter test basis, fourth quarter
Status: **AGREE**

Value: $0.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].mq_total — Mid-quarter test basis, all of 2025
Status: **AGREE**

Value: $0.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].cost179 — Cost of section 179 property placed in service in 2025
Status: **AGREE**

Value: $6,126.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].cost179_2025 — The business cost when used more than 50% in the business
Status: **AGREE**

Value: $6,126.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].dep_prior — MACRS on property placed in service before 2025
Status: **AGREE**

Value: $0.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].dep_listed — Depreciation of this listed property (column (h))
Status: **AGREE**

Value: $0.00

### case classm.asset.4 — prompt sha256 71b036d039c4bd773dc13121abda0fdec9b8edd8105ebc6fda4047a6792fd85a; branches: asset.outside:false, asset.screen:false, asset.screened:false, asset.pct_bad:false, asset.listed:false, asset.over_half:false, asset.listed_low:false, asset.is2025:false, asset.is2025:true, asset.done:false, asset.s179_bad:false, asset.after179:positive, asset.after_jan19:true, asset.bonus_same:true, asset.bonus_mixed:false, asset.bonus_fullcase#0, asset.bonus#2, asset.ub:positive, asset.macrs2025#0, asset.mq_q4_2025#0, asset.mq_q4_2025#3, asset.ub_prior_a:floor, asset.ub_prior_a:positive, asset.ub_prior:floor, asset.ub_prior:positive, asset.macrs_prior#0, asset.dep_2025#0, asset.dep_2025#1, asset.bonus_2025#0, asset.bonus_2025#1, asset.s179_2025#0, asset.s179_2025#1, asset.mq_q4#0, asset.mq_q4#1, asset.mq_total#0, asset.mq_total#1, asset.cost179#0, asset.cost179#1, asset.cost179_2025#1, asset.dep_prior#0, asset.dep_prior#1

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].period — Recovery period under GDS for the asset class
Status: **AGREE**

Value: y3

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].outside — The asset class is outside this tool
Status: **AGREE**

Value: no

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].screened — This property is outside this tool
Status: **AGREE**

Value: no

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].pct_c — The business use percentage, as cents
Status: **DISAGREE**

Project: $0.38
Model: $38.00
Work: 38% business use

Ruling: representation; project retained. The business-use percentage is carried as one cent per percentage point (multiply_count by one cent) so it can be divided like an amount; the model read the cents as dollars. Not evidence. [dropped]

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].pct_bad — The business use percentage is more than 100
Status: **AGREE**

Value: no

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].over_half — Business use is more than 50%
Status: **AGREE**

Value: no

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].listed_low — Listed property used 50% or less for business, or a percentage over 100
Status: **AGREE**

Value: no

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].basis — Basis for depreciation (business/investment use only), before section 179 and th
Status: **AGREE**

Value: $7,505.76

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].is2025 — Placed in service in 2025
Status: **AGREE**

Value: yes

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].year — Year of recovery in 2025
Status: **AGREE**

Value: 1

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].last — Last year of recovery for the recovery period
Status: **AGREE**

Value: 4

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].done — The recovery period ended before 2025
Status: **AGREE**

Value: no

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq1

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].s179_bad — The section 179 election is more than the business cost, or the property is not 
Status: **AGREE**

Value: no

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].after179 — Basis less the section 179 election
Status: **AGREE**

Value: $7,505.76

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].bonus_mixed — The special allowance choice differs within a class
Status: **AGREE**

Value: no

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].bonus_full — 100% special allowance
Status: **AGREE**

Value: $7,505.76

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].bonus_forty — 40% special allowance
Status: **AGREE**

Value: $3,002.30

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **AGREE**

Value: $7,505.76

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].bonus — Special depreciation allowance for this property
Status: **AGREE**

Value: $0.00

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].ub — Basis for MACRS depreciation (after section 179 and the special allowance)
Status: **AGREE**

Value: $7,505.76

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].rate_hy — MACRS rate, half-year convention
Status: **AGREE**

Value: 33.33%

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].rate_mq — MACRS rate, mid-quarter convention
Status: **AGREE**

Value: 58.33%

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].macrs_hy — MACRS depreciation, half-year convention
Status: **AGREE**

Value: $2,501.67

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].macrs_mq — MACRS depreciation, mid-quarter convention
Status: **AGREE**

Value: $4,378.11

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].macrs2025 — MACRS depreciation for 2025 property
Status: **AGREE**

Value: $2,501.67

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].mqbase — Depreciable basis for the mid-quarter test (after section 179, before the specia
Status: **AGREE**

Value: $7,505.76

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].mq_q4_2025 — That basis when placed in service October to December
Status: **AGREE**

Value: $0.00

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].ub_prior_a — Business basis less the section 179 deduction
Status: **AGREE**

Value: $7,505.76

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].ub_prior — Unadjusted basis
Status: **AGREE**

Value: $7,505.76

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].rate_prior — MACRS rate for the 2025 year of recovery
Status: **AGREE**

Value: 33.33%

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].macrs_prior_live — MACRS depreciation for 2025
Status: **AGREE**

Value: $2,501.67

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].macrs_prior — MACRS deduction for 2025 on property placed in service before 2025
Status: **DISAGREE**

Project: $2,501.67
Model: $0.00
Work: Placed in service in 2025, so not prior-year property

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the 2025 lines for earlier property and the reverse, the listed-property lines for property that is not listed and the reverse, the lines after a zero basis); the Form 4562 totals take each only where it belongs (sc sums with the 2025 and listed filters), and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].dep_2025 — MACRS on 2025 property
Status: **AGREE**

Value: $2,501.67

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].bonus_2025 — Special allowance on 2025 property
Status: **AGREE**

Value: $0.00

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].s179_2025 — Section 179 elected on 2025 property
Status: **AGREE**

Value: $0.00

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].mq_q4 — Mid-quarter test basis, fourth quarter
Status: **AGREE**

Value: $0.00

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].mq_total — Mid-quarter test basis, all of 2025
Status: **AGREE**

Value: $7,505.76

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].cost179 — Cost of section 179 property placed in service in 2025
Status: **AGREE**

Value: $0.00

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].cost179_2025 — The business cost when used more than 50% in the business
Status: **AGREE**

Value: $0.00

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].dep_prior — MACRS on property placed in service before 2025
Status: **AGREE**

Value: $0.00

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].dep_listed — Depreciation of this listed property (column (h))
Status: **DISAGREE**

Project: $2,501.67
Model: $0.00
Work: Not listed property

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the 2025 lines for earlier property and the reverse, the listed-property lines for property that is not listed and the reverse, the lines after a zero basis); the Form 4562 totals take each only where it belongs (sc sums with the 2025 and listed filters), and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].period — Recovery period under GDS for the asset class
Status: **AGREE**

Value: y7

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].outside — The asset class is outside this tool
Status: **AGREE**

Value: no

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].screened — This property is outside this tool
Status: **AGREE**

Value: no

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].pct_c — The business use percentage, as cents
Status: **DISAGREE**

Project: $0.20
Model: $20.00
Work: 20% business use

Ruling: representation; project retained. The business-use percentage is carried as one cent per percentage point (multiply_count by one cent) so it can be divided like an amount; the model read the cents as dollars. Not evidence. [dropped]

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].pct_bad — The business use percentage is more than 100
Status: **AGREE**

Value: no

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].over_half — Business use is more than 50%
Status: **AGREE**

Value: no

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].listed_low — Listed property used 50% or less for business, or a percentage over 100
Status: **AGREE**

Value: no

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].basis — Basis for depreciation (business/investment use only), before section 179 and th
Status: **AGREE**

Value: $2,167.80

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].is2025 — Placed in service in 2025
Status: **AGREE**

Value: no

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].year — Year of recovery in 2025
Status: **AGREE**

Value: 4

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].last — Last year of recovery for the recovery period
Status: **AGREE**

Value: 8

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].done — The recovery period ended before 2025
Status: **AGREE**

Value: no

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq4

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].s179_bad — The section 179 election is more than the business cost, or the property is not 
Status: **DISAGREE**

Project: no
Model: yes
Work: Section 179 of 2,168.00 is more than the business cost of 2,167.80, and use is not more than 50%

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the 2025 lines for earlier property and the reverse, the listed-property lines for property that is not listed and the reverse, the lines after a zero basis); the Form 4562 totals take each only where it belongs (sc sums with the 2025 and listed filters), and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].after179 — Basis less the section 179 election
Status: **DISAGREE**

Project: $2,167.80
Model: $0.00
Work: 2,167.80 - 2,168.00 is less than zero, so 0

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the 2025 lines for earlier property and the reverse, the listed-property lines for property that is not listed and the reverse, the lines after a zero basis); the Form 4562 totals take each only where it belongs (sc sums with the 2025 and listed filters), and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].bonus_mixed — The special allowance choice differs within a class
Status: **AGREE**

Value: no

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].bonus_full — 100% special allowance
Status: **DISAGREE**

Project: $2,167.80
Model: $0.00
Work: 100% x 0

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the 2025 lines for earlier property and the reverse, the listed-property lines for property that is not listed and the reverse, the lines after a zero basis); the Form 4562 totals take each only where it belongs (sc sums with the 2025 and listed filters), and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].bonus_forty — 40% special allowance
Status: **DISAGREE**

Project: $867.12
Model: $0.00
Work: 40% x 0

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the 2025 lines for earlier property and the reverse, the listed-property lines for property that is not listed and the reverse, the lines after a zero basis); the Form 4562 totals take each only where it belongs (sc sums with the 2025 and listed filters), and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **DISAGREE**

Project: $2,167.80
Model: $0.00
Work: 100% x 0

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the 2025 lines for earlier property and the reverse, the listed-property lines for property that is not listed and the reverse, the lines after a zero basis); the Form 4562 totals take each only where it belongs (sc sums with the 2025 and listed filters), and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].bonus — Special depreciation allowance for this property
Status: **AGREE**

Value: $0.00

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].ub — Basis for MACRS depreciation (after section 179 and the special allowance)
Status: **DISAGREE**

Project: $2,167.80
Model: $0.00
Work: 0 - 0

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the 2025 lines for earlier property and the reverse, the listed-property lines for property that is not listed and the reverse, the lines after a zero basis); the Form 4562 totals take each only where it belongs (sc sums with the 2025 and listed filters), and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].rate_hy — MACRS rate, half-year convention
Status: **DISAGREE**

Project: 12.49%
Model: 14.29%
Work: 7-year, HY, year 1

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the 2025 lines for earlier property and the reverse, the listed-property lines for property that is not listed and the reverse, the lines after a zero basis); the Form 4562 totals take each only where it belongs (sc sums with the 2025 and listed filters), and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].rate_mq — MACRS rate, mid-quarter convention
Status: **DISAGREE**

Project: 14.06%
Model: 3.57%
Work: 7-year, MQ Q4, year 1

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the 2025 lines for earlier property and the reverse, the listed-property lines for property that is not listed and the reverse, the lines after a zero basis); the Form 4562 totals take each only where it belongs (sc sums with the 2025 and listed filters), and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].macrs_hy — MACRS depreciation, half-year convention
Status: **DISAGREE**

Project: $270.76
Model: $0.00
Work: 0 x 14.29%

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the 2025 lines for earlier property and the reverse, the listed-property lines for property that is not listed and the reverse, the lines after a zero basis); the Form 4562 totals take each only where it belongs (sc sums with the 2025 and listed filters), and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].macrs_mq — MACRS depreciation, mid-quarter convention
Status: **DISAGREE**

Project: $304.79
Model: $0.00
Work: 0 x 3.57%

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the 2025 lines for earlier property and the reverse, the listed-property lines for property that is not listed and the reverse, the lines after a zero basis); the Form 4562 totals take each only where it belongs (sc sums with the 2025 and listed filters), and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].macrs2025 — MACRS depreciation for 2025 property
Status: **DISAGREE**

Project: $270.76
Model: $0.00
Work: Not 2025 property, and basis is 0

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the 2025 lines for earlier property and the reverse, the listed-property lines for property that is not listed and the reverse, the lines after a zero basis); the Form 4562 totals take each only where it belongs (sc sums with the 2025 and listed filters), and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].mqbase — Depreciable basis for the mid-quarter test (after section 179, before the specia
Status: **DISAGREE**

Project: $2,167.80
Model: $0.00
Work: after179 = 0

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the 2025 lines for earlier property and the reverse, the listed-property lines for property that is not listed and the reverse, the lines after a zero basis); the Form 4562 totals take each only where it belongs (sc sums with the 2025 and listed filters), and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].mq_q4_2025 — That basis when placed in service October to December
Status: **DISAGREE**

Project: $2,167.80
Model: $0.00
Work: Basis is 0

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the 2025 lines for earlier property and the reverse, the listed-property lines for property that is not listed and the reverse, the lines after a zero basis); the Form 4562 totals take each only where it belongs (sc sums with the 2025 and listed filters), and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].ub_prior_a — Business basis less the section 179 deduction
Status: **AGREE**

Value: $0.00

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].ub_prior — Unadjusted basis
Status: **AGREE**

Value: $0.00

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].rate_prior — MACRS rate for the 2025 year of recovery
Status: **AGREE**

Value: 10.93%

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].macrs_prior_live — MACRS depreciation for 2025
Status: **AGREE**

Value: $0.00

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].macrs_prior — MACRS deduction for 2025 on property placed in service before 2025
Status: **AGREE**

Value: $0.00

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].dep_2025 — MACRS on 2025 property
Status: **AGREE**

Value: $0.00

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].bonus_2025 — Special allowance on 2025 property
Status: **AGREE**

Value: $0.00

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].s179_2025 — Section 179 elected on 2025 property
Status: **AGREE**

Value: $0.00

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].mq_q4 — Mid-quarter test basis, fourth quarter
Status: **AGREE**

Value: $0.00

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].mq_total — Mid-quarter test basis, all of 2025
Status: **AGREE**

Value: $0.00

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].cost179 — Cost of section 179 property placed in service in 2025
Status: **AGREE**

Value: $0.00

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].cost179_2025 — The business cost when used more than 50% in the business
Status: **AGREE**

Value: $0.00

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].dep_prior — MACRS on property placed in service before 2025
Status: **AGREE**

Value: $0.00

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_2].dep_listed — Depreciation of this listed property (column (h))
Status: **AGREE**

Value: $0.00

## Raw responses

### classm.asset.1

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].period"
    value: "y7"
    work: "Pub. 946 Table B-2 class 48.36 (TOCSC satellite ground segment): 10-yr class life, 7-yr GDS (from memory; not in the supplied text)"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].outside"
    value: "no"
    work: "Class 48.36 has a GDS recovery period the tool handles"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].screened"
    value: "no"
    work: "Filer answered no to the screening questions"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].pct_c"
    value: "40.00"
    work: "40% business use"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].pct_bad"
    value: "no"
    work: "40 is not more than 100"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].over_half"
    value: "no"
    work: "40% is not more than 50%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].listed_low"
    value: "no"
    work: "Not listed property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].basis"
    value: "16578.80"
    work: "41,447.00 x 40%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].is2025"
    value: "yes"
    work: "Placed in service in y2025"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].year"
    value: "1"
    work: "2025 - 2025 + 1"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].last"
    value: "8"
    work: "7-year period + 1"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].done"
    value: "no"
    work: "Year 1 is not more than 8"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].qconv"
    value: "mq1"
    work: "Placed in service in quarter q1"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].s179_bad"
    value: "no"
    work: "Elected 0.00 is not more than the allowable cost of 0.00"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].after179"
    value: "16578.80"
    work: "16,578.80 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_mixed"
    value: "no"
    work: "Same choice for the whole class"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_full"
    value: "16578.80"
    work: "100% x 16,578.80"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_forty"
    value: "6631.52"
    work: "40% x 16,578.80"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_fullcase"
    value: "16578.80"
    work: "Acquired after Jan 19, 2025, so 100%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus"
    value: "16578.80"
    work: "Full allowance claimed; 7-yr qualified property placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].ub"
    value: "0.00"
    work: "16,578.80 - 16,578.80"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].rate_hy"
    value: "14.29%"
    work: "7-yr, HY, year 1"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].rate_mq"
    value: "25.00%"
    work: "7-yr, MQ first quarter, year 1 (Pub. 946 Table A-2 example)"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs_hy"
    value: "0.00"
    work: "0.00 x 14.29%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs_mq"
    value: "0.00"
    work: "0.00 x 25.00%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs2025"
    value: "0.00"
    work: "Mid-quarter test is no, so use HY amount"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].mqbase"
    value: "16578.80"
    work: "Business basis after section 179, before special allowance"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].mq_q4_2025"
    value: "0.00"
    work: "Placed in service in q1, not Oct-Dec"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].ub_prior_a"
    value: "16578.80"
    work: "16,578.80 - 0.00 section 179"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].ub_prior"
    value: "16578.80"
    work: "16,578.80 - 0.00 special allowance claimed"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].rate_prior"
    value: "3.57%"
    work: "7-yr, mq4 convention given, year 1"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs_prior_live"
    value: "591.86"
    work: "16,578.80 x 3.57%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs_prior"
    value: "0.00"
    work: "Placed in service in 2025, not before"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].dep_2025"
    value: "0.00"
    work: "MACRS 2025 amount 0.00"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_2025"
    value: "16578.80"
    work: "Special allowance on 2025 property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].s179_2025"
    value: "0.00"
    work: "No section 179 elected"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].mq_q4"
    value: "0.00"
    work: "No fourth-quarter basis"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].mq_total"
    value: "16578.80"
    work: "2025 basis for the mid-quarter test"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].cost179"
    value: "0.00"
    work: "Not used more than 50% in the business"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].cost179_2025"
    value: "0.00"
    work: "40% use is not more than 50%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].dep_prior"
    value: "0.00"
    work: "Not prior-year property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].dep_listed"
    value: "0.00"
    work: "Not listed property"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].period"
    value: "y20"
    work: "Pub. 946 Table B-2 class 49.4 (central steam production and distribution): 28-yr class life, 20-yr GDS (from memory; not in the supplied text)"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].outside"
    value: "no"
    work: "Class 49.4 has a GDS recovery period the tool handles"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].screened"
    value: "no"
    work: "Filer answered no to the screening questions"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].pct_c"
    value: "100.00"
    work: "100% business use"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].pct_bad"
    value: "no"
    work: "100 is not more than 100"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].over_half"
    value: "yes"
    work: "100% is more than 50%"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].listed_low"
    value: "no"
    work: "Not listed property"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].basis"
    value: "20222.00"
    work: "20,222.00 x 100%"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].is2025"
    value: "no"
    work: "Placed in service in y2010"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].year"
    value: "16"
    work: "2025 - 2010 + 1"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].last"
    value: "21"
    work: "20-year period + 1"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].done"
    value: "no"
    work: "Year 16 is not more than 21"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].qconv"
    value: "mq4"
    work: "Quarter given as q4"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].s179_bad"
    value: "no"
    work: "0.00 is not more than 20,222.00, and use is more than 50%"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].after179"
    value: "20222.00"
    work: "20,222.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].bonus_mixed"
    value: "no"
    work: "Same choice for the whole class"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].bonus_full"
    value: "20222.00"
    work: "100% x 20,222.00"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].bonus_forty"
    value: "8088.80"
    work: "40% x 20,222.00"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].bonus_fullcase"
    value: "8088.80"
    work: "Not acquired after Jan 19, 2025, so 40%"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].bonus"
    value: "0.00"
    work: "Allowance is none, and property is not placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].ub"
    value: "20222.00"
    work: "20,222.00 - 0.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].rate_hy"
    value: "3.750%"
    work: "20-yr 150DB, HY, year 1"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].rate_mq"
    value: "0.938%"
    work: "20-yr, MQ fourth quarter, year 1 (7.5% x 0.125)"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].macrs_hy"
    value: "758.33"
    work: "20,222.00 x 3.750%"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].macrs_mq"
    value: "189.68"
    work: "20,222.00 x 0.938%"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].macrs2025"
    value: "758.33"
    work: "Mid-quarter test is no, so use HY amount"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].mqbase"
    value: "20222.00"
    work: "Basis after section 179, before special allowance"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].mq_q4_2025"
    value: "20222.00"
    work: "Quarter given as q4"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].ub_prior_a"
    value: "20222.00"
    work: "20,222.00 - 0.00 section 179"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].ub_prior"
    value: "20222.00"
    work: "20,222.00 - 0.00 special allowance claimed"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].rate_prior"
    value: "4.458%"
    work: "20-yr, MQ fourth quarter, year 16 (straight-line phase, from memory of the table)"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].macrs_prior_live"
    value: "901.50"
    work: "20,222.00 x 4.458%"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].macrs_prior"
    value: "901.50"
    work: "Placed in service before 2025 and not done"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].dep_2025"
    value: "0.00"
    work: "Not 2025 property"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].bonus_2025"
    value: "0.00"
    work: "Not 2025 property"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].s179_2025"
    value: "0.00"
    work: "Not 2025 property"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].mq_q4"
    value: "0.00"
    work: "Not 2025 property"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].mq_total"
    value: "0.00"
    work: "Not 2025 property"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].cost179"
    value: "0.00"
    work: "Not placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].cost179_2025"
    value: "20222.00"
    work: "Used more than 50%: business cost"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].dep_prior"
    value: "901.50"
    work: "Line 17 MACRS amount for prior-year property"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].dep_listed"
    value: "0.00"
    work: "Not listed property"
```
```

### classm.asset.2

```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].period"
    value: "y15"
    work: "Pub. 946 Table B-2, class 48.41 telephone distribution plant: GDS recovery period 15 years"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].outside"
    value: "no"
    work: "Class 48.41 is a standard MACRS GDS class"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].screened"
    value: "no"
    work: "The filer answered no to the screening questions and the class is supported"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].pct_c"
    value: "100.00"
    work: "100% business use"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].pct_bad"
    value: "no"
    work: "100 is not more than 100"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].over_half"
    value: "yes"
    work: "100% > 50%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].listed_low"
    value: "no"
    work: "Not listed property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].basis"
    value: "44464.00"
    work: "44,464.00 x 100%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].is2025"
    value: "yes"
    work: "Placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].year"
    value: "1"
    work: "2025 - 2025 + 1"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].last"
    value: "16"
    work: "15-year property; the convention adds one more year: 15 + 1"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].done"
    value: "no"
    work: "Year 1 is not after year 16"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].qconv"
    value: "mq2"
    work: "Placed in service in quarter 2"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].s179_bad"
    value: "no"
    work: "0 is not more than 44,464 and business use is over 50%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].after179"
    value: "44464.00"
    work: "44,464.00 - 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_mixed"
    value: "no"
    work: "The filer says the choice is the same for the whole class"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_full"
    value: "44464.00"
    work: "44,464.00 x 100%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_forty"
    value: "17785.60"
    work: "44,464.00 x 40%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_fullcase"
    value: "44464.00"
    work: "Acquired after Jan 19, 2025, so 100%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus"
    value: "17785.60"
    work: "40% elected; 15-year property qualifies (20 years or less)"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].ub"
    value: "26678.40"
    work: "44,464.00 - 17,785.60"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].rate_hy"
    value: "5.00%"
    work: "150DB: 1.5/15 = 10%, x 0.5 for half-year"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].rate_mq"
    value: "6.25%"
    work: "10% x 0.625 for quarter 2"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs_hy"
    value: "1333.92"
    work: "26,678.40 x 5.00%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs_mq"
    value: "1667.40"
    work: "26,678.40 x 6.25%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs2025"
    value: "1667.40"
    work: "Mid-quarter convention applies (test = yes)"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].mqbase"
    value: "44464.00"
    work: "After section 179, before the special allowance"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].mq_q4_2025"
    value: "0.00"
    work: "Placed in service in Q2, not Q4"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].ub_prior_a"
    value: "44464.00"
    work: "44,464.00 - prior section 179 of 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].ub_prior"
    value: "44464.00"
    work: "44,464.00 - special allowance claimed of 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].rate_prior"
    value: "1.25%"
    work: "15-year property, mq4 convention, year 1: 10% x 0.125"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs_prior_live"
    value: "555.80"
    work: "44,464.00 x 1.25%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs_prior"
    value: "0.00"
    work: "Placed in service in 2025, not before 2025"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].dep_2025"
    value: "1667.40"
    work: "Line 19 MACRS on 2025 property that is not listed"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_2025"
    value: "17785.60"
    work: "Line 14 special allowance"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].s179_2025"
    value: "0.00"
    work: "No section 179 elected"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].mq_q4"
    value: "0.00"
    work: "Not placed in service in Q4"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].mq_total"
    value: "44464.00"
    work: "mqbase for 2025 property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].cost179"
    value: "44464.00"
    work: "Business cost of tangible section 179 property placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].cost179_2025"
    value: "44464.00"
    work: "Business use is over 50%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].dep_prior"
    value: "0.00"
    work: "Not property placed in service before 2025"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].dep_listed"
    value: "0.00"
    work: "Not listed property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].period"
    value: "y5"
    work: "Pub. 946 class 00.241 light general purpose trucks: GDS 5 years"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].outside"
    value: "no"
    work: "Class 00.241 is a standard MACRS GDS class"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].screened"
    value: "no"
    work: "The filer answered no to the screening questions"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].pct_c"
    value: "100.00"
    work: "100% business use"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].pct_bad"
    value: "no"
    work: "100 is not more than 100"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].over_half"
    value: "yes"
    work: "100% > 50%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].listed_low"
    value: "no"
    work: "Listed property, but used more than 50%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].basis"
    value: "43875.00"
    work: "43,875.00 x 100%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].is2025"
    value: "yes"
    work: "Placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].year"
    value: "1"
    work: "2025 - 2025 + 1"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].last"
    value: "6"
    work: "5-year property; the convention adds one more year: 5 + 1"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].done"
    value: "no"
    work: "Year 1 is not after year 6"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].qconv"
    value: "mq4"
    work: "Placed in service in quarter 4"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].s179_bad"
    value: "no"
    work: "0 is not more than the cost and business use is over 50%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].after179"
    value: "43875.00"
    work: "43,875.00 - 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].bonus_mixed"
    value: "no"
    work: "The filer says the choice is the same for the whole class"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].bonus_full"
    value: "43875.00"
    work: "43,875.00 x 100%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].bonus_forty"
    value: "17550.00"
    work: "43,875.00 x 40%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].bonus_fullcase"
    value: "43875.00"
    work: "Acquired after Jan 19, 2025, so 100%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].bonus"
    value: "17550.00"
    work: "40% elected; listed property used over 50% qualifies"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].ub"
    value: "26325.00"
    work: "43,875.00 - 17,550.00"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].rate_hy"
    value: "20.00%"
    work: "200DB: 2/5 = 40%, x 0.5 for half-year"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].rate_mq"
    value: "5.00%"
    work: "40% x 0.125 for quarter 4"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].macrs_hy"
    value: "5265.00"
    work: "26,325.00 x 20%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].macrs_mq"
    value: "1316.25"
    work: "26,325.00 x 5%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].macrs2025"
    value: "1316.25"
    work: "Mid-quarter convention applies (test = yes)"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].mqbase"
    value: "43875.00"
    work: "After section 179, before the special allowance"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].mq_q4_2025"
    value: "43875.00"
    work: "Placed in service in Q4"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].ub_prior_a"
    value: "43875.00"
    work: "43,875.00 - prior section 179 of 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].ub_prior"
    value: "43875.00"
    work: "43,875.00 - special allowance claimed of 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].rate_prior"
    value: "20.00%"
    work: "5-year property, half-year convention, year 1"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].macrs_prior_live"
    value: "8775.00"
    work: "43,875.00 x 20%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].macrs_prior"
    value: "0.00"
    work: "Placed in service in 2025, not before 2025"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].dep_2025"
    value: "0.00"
    work: "Listed property is reported in Part V, not line 19"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].bonus_2025"
    value: "0.00"
    work: "Line 14 excludes listed property; its allowance goes on line 25"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].s179_2025"
    value: "0.00"
    work: "No section 179 elected"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].mq_q4"
    value: "43875.00"
    work: "Q4 basis for the mid-quarter test"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].mq_total"
    value: "43875.00"
    work: "mqbase for 2025 property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].cost179"
    value: "43875.00"
    work: "Line 2 includes listed property from Part V"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].cost179_2025"
    value: "43875.00"
    work: "Business use is over 50%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].dep_prior"
    value: "0.00"
    work: "Not property placed in service before 2025"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].dep_listed"
    value: "1316.25"
    work: "Line 26 column (h) = MACRS 26,325.00 x 5%"
```

### classm.asset.3

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].period"
    value: "y7"
    work: "Pub. 946 Table B-2 asset class 49.5 (waste reduction and resource recovery plants): class life 10 years, GDS 7 years; recalled, the class table was not provided"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].outside"
    value: "no"
    work: "Class 49.5 is an ordinary 7-year GDS class"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].screened"
    value: "no"
    work: "The filer answered no to the screening question"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].pct_c"
    value: "30.00"
    work: "30%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].pct_bad"
    value: "no"
    work: "30 is not more than 100"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].over_half"
    value: "no"
    work: "30% is not more than 50%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].listed_low"
    value: "no"
    work: "The property is not listed property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].basis"
    value: "11538.90"
    work: "38,463.00 x 30%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].is2025"
    value: "yes"
    work: "Placed in service in 2025 (y2025)"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].year"
    value: "1"
    work: "2025 is the first year of recovery"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].last"
    value: "8"
    work: "7-year property with a HY/MQ convention runs 8 tax years"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].done"
    value: "no"
    work: "Recovery year 1 is not after year 8"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].qconv"
    value: "mq1"
    work: "Placed in service in Q1"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].s179_bad"
    value: "no"
    work: "No section 179 election ($0), so neither test is failed by an election"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].after179"
    value: "11538.90"
    work: "11,538.90 - 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_mixed"
    value: "no"
    work: "Same choice for the whole class = yes"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_full"
    value: "11538.90"
    work: "100% x 11,538.90"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_forty"
    value: "4615.56"
    work: "40% x 11,538.90"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_fullcase"
    value: "4615.56"
    work: "Not acquired after Jan 19, 2025, so 40%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus"
    value: "4615.56"
    work: "Allowance claimed (full); not listed property, not ADS"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].ub"
    value: "6923.34"
    work: "11,538.90 - 4,615.56"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].rate_hy"
    value: "14.29%"
    work: "7-year, half-year, year 1"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].rate_mq"
    value: "25.00%"
    work: "7-year, mid-quarter Q1, year 1"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs_hy"
    value: "989.35"
    work: "6,923.34 x 14.29%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs_mq"
    value: "1730.84"
    work: "6,923.34 x 25.00%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs2025"
    value: "989.35"
    work: "Mid-quarter test = no, so the half-year amount applies"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].mqbase"
    value: "11538.90"
    work: "Business basis after section 179, before the special allowance"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].mq_q4_2025"
    value: "0.00"
    work: "Placed in service in Q1, not Q4"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].ub_prior_a"
    value: "11538.90"
    work: "11,538.90 - prior section 179 of 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].ub_prior"
    value: "11538.90"
    work: "11,538.90 - prior special allowance of 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].rate_prior"
    value: "17.85%"
    work: "7-year, mid-quarter Q2 (mq2), recovery year 1"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs_prior_live"
    value: "2059.69"
    work: "11,538.90 x 17.85%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs_prior"
    value: "0.00"
    work: "Placed in service in 2025, not before 2025"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].dep_2025"
    value: "989.35"
    work: "From macrs2025"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_2025"
    value: "4615.56"
    work: "From bonus"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].s179_2025"
    value: "0.00"
    work: "No election"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].mq_q4"
    value: "0.00"
    work: "From mq_q4_2025"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].mq_total"
    value: "11538.90"
    work: "From mqbase"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].cost179"
    value: "0.00"
    work: "Not used more than 50% in the business"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].cost179_2025"
    value: "0.00"
    work: "Business use is 30%, not more than 50%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].dep_prior"
    value: "0.00"
    work: "Not prior-year property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].dep_listed"
    value: "0.00"
    work: "Not listed property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].period"
    value: "y7"
    work: "Pub. 946 asset class 48.44 (customer premises equipment): class life 10 years, GDS 7 years; recalled, the class table was not provided"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].outside"
    value: "no"
    work: "Class 48.44 is an ordinary 7-year GDS class"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].screened"
    value: "no"
    work: "The filer answered no to the screening question"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].pct_c"
    value: "100.00"
    work: "100%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].pct_bad"
    value: "no"
    work: "100 is not more than 100"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].over_half"
    value: "yes"
    work: "100% is more than 50%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].listed_low"
    value: "no"
    work: "The property is not listed property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].basis"
    value: "6126.00"
    work: "6,126.00 x 100%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].is2025"
    value: "yes"
    work: "Placed in service in 2025 (y2025)"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].year"
    value: "1"
    work: "2025 is the first year of recovery"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].last"
    value: "8"
    work: "7-year property runs 8 tax years"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].done"
    value: "no"
    work: "Recovery year 1 is not after year 8"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].qconv"
    value: "mq3"
    work: "Placed in service in Q3"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].s179_bad"
    value: "no"
    work: "6,126.00 is not more than 6,126.00, and use is more than 50%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].after179"
    value: "0.00"
    work: "6,126.00 - 6,126.00"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].bonus_mixed"
    value: "no"
    work: "Same choice for the whole class = yes"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].bonus_full"
    value: "0.00"
    work: "100% x 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].bonus_forty"
    value: "0.00"
    work: "40% x 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].bonus_fullcase"
    value: "0.00"
    work: "Acquired after Jan 19, 2025, so 100% x 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].bonus"
    value: "0.00"
    work: "Elected out for the class (none)"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].ub"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].rate_hy"
    value: "14.29%"
    work: "7-year, half-year, year 1"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].rate_mq"
    value: "10.71%"
    work: "7-year, mid-quarter Q3, year 1"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].macrs_hy"
    value: "0.00"
    work: "0 x 14.29%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].macrs_mq"
    value: "0.00"
    work: "0 x 10.71%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].macrs2025"
    value: "0.00"
    work: "Half-year convention applies; amount is 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].mqbase"
    value: "0.00"
    work: "6,126.00 - section 179 of 6,126.00"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].mq_q4_2025"
    value: "0.00"
    work: "Placed in service in Q3, not Q4"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].ub_prior_a"
    value: "6126.00"
    work: "6,126.00 - prior section 179 of 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].ub_prior"
    value: "6126.00"
    work: "6,126.00 - prior special allowance of 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].rate_prior"
    value: "17.85%"
    work: "7-year, mid-quarter Q2 (mq2), recovery year 1"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].macrs_prior_live"
    value: "1093.49"
    work: "6,126.00 x 17.85%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].macrs_prior"
    value: "0.00"
    work: "Placed in service in 2025, not before 2025"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].dep_2025"
    value: "0.00"
    work: "From macrs2025"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].bonus_2025"
    value: "0.00"
    work: "From bonus"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].s179_2025"
    value: "6126.00"
    work: "Elected section 179 cost"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].mq_q4"
    value: "0.00"
    work: "From mq_q4_2025"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].mq_total"
    value: "0.00"
    work: "From mqbase"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].cost179"
    value: "6126.00"
    work: "Business cost; use is more than 50%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].cost179_2025"
    value: "6126.00"
    work: "Business cost 6,126.00 with 100% use"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].dep_prior"
    value: "0.00"
    work: "Not prior-year property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].dep_listed"
    value: "0.00"
    work: "Not listed property"
```
```

### classm.asset.4

```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].period"
    value: "y3"
    work: "Pub. 946 App. B asset class 20.5 has a 3-year GDS recovery period (from the table, not printed in the text given)"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].outside"
    value: "no"
    work: "Class 20.5 maps to a standard GDS class"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].screened"
    value: "no"
    work: "Filer answered no to the exceptions, and the property is not listed property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].pct_c"
    value: "38.00"
    work: "38% business use"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].pct_bad"
    value: "no"
    work: "38 is not more than 100"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].over_half"
    value: "no"
    work: "38% is not more than 50%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].listed_low"
    value: "no"
    work: "Not listed property, and the percentage is not over 100"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].basis"
    value: "7505.76"
    work: "19,752.00 x 38% = 7,505.76 (line 19 col (c))"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].is2025"
    value: "yes"
    work: "Placed in service in y2025"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].year"
    value: "1"
    work: "2025 - 2025 + 1 = 1"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].last"
    value: "4"
    work: "A 3-year recovery period plus the convention year = 4 tax years"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].done"
    value: "no"
    work: "Year 1 is not more than 4"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].qconv"
    value: "mq1"
    work: "Placed in service in Q1"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].s179_bad"
    value: "no"
    work: "No section 179 elected ($0), so there is no election to fail the tests"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].after179"
    value: "7505.76"
    work: "7,505.76 - 0 = 7,505.76"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_mixed"
    value: "no"
    work: "Filer says the choice is the same for the whole class"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_full"
    value: "7505.76"
    work: "100% x 7,505.76"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_forty"
    value: "3002.30"
    work: "40% x 7,505.76 = 3,002.304, rounded to 3,002.30"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_fullcase"
    value: "7505.76"
    work: "Acquired after Jan 19, 2025, so 100%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus"
    value: "0.00"
    work: "Special allowance for this class = none"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].ub"
    value: "7505.76"
    work: "7,505.76 - 0 - 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].rate_hy"
    value: "33.33%"
    work: "MACRS table: 3-year, HY, year 1"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].rate_mq"
    value: "58.33%"
    work: "MACRS table: 3-year, MQ Q1, year 1"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs_hy"
    value: "2501.67"
    work: "7,505.76 x 33.33% = 2,501.67"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs_mq"
    value: "4378.11"
    work: "7,505.76 x 58.33% = 4,378.11"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs2025"
    value: "2501.67"
    work: "Mid-quarter test = no, so the half-year convention applies"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].mqbase"
    value: "7505.76"
    work: "Business basis after section 179 ($0), before the special allowance"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].mq_q4_2025"
    value: "0.00"
    work: "Placed in service in Q1, not Q4"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].ub_prior_a"
    value: "7505.76"
    work: "7,505.76 - 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].ub_prior"
    value: "7505.76"
    work: "7,505.76 - special allowance claimed 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].rate_prior"
    value: "33.33%"
    work: "3-year, HY, year 1"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs_prior_live"
    value: "2501.67"
    work: "7,505.76 x 33.33%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs_prior"
    value: "0.00"
    work: "Placed in service in 2025, so not prior-year property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].dep_2025"
    value: "2501.67"
    work: "macrs2025"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_2025"
    value: "0.00"
    work: "bonus = 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].s179_2025"
    value: "0.00"
    work: "No section 179 elected"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].mq_q4"
    value: "0.00"
    work: "Not placed in service in Q4"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].mq_total"
    value: "7505.76"
    work: "mqbase for 2025 property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].cost179"
    value: "0.00"
    work: "Not used more than 50% for business, so not section 179 property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].cost179_2025"
    value: "0.00"
    work: "Business use is 50% or less"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].dep_prior"
    value: "0.00"
    work: "Placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].dep_listed"
    value: "0.00"
    work: "Not listed property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].period"
    value: "y7"
    work: "Pub. 946 App. B asset class 10.0 has a 7-year GDS recovery period (from the table, not printed in the text given)"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].outside"
    value: "no"
    work: "Class 10.0 maps to a standard GDS class"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].screened"
    value: "no"
    work: "Filer answered no to the exceptions, and the property is not listed property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].pct_c"
    value: "20.00"
    work: "20% business use"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].pct_bad"
    value: "no"
    work: "20 is not more than 100"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].over_half"
    value: "no"
    work: "20% is not more than 50%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].listed_low"
    value: "no"
    work: "Not listed property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].basis"
    value: "2167.80"
    work: "10,839.00 x 20% = 2,167.80"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].is2025"
    value: "no"
    work: "Placed in service in y2022"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].year"
    value: "4"
    work: "2025 - 2022 + 1 = 4"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].last"
    value: "8"
    work: "A 7-year recovery period plus 1 = 8 tax years"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].done"
    value: "no"
    work: "Year 4 is not more than 8"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].qconv"
    value: "mq4"
    work: "Quarter given = q4"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].s179_bad"
    value: "yes"
    work: "Section 179 of 2,168.00 is more than the business cost of 2,167.80, and use is not more than 50%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].after179"
    value: "0.00"
    work: "2,167.80 - 2,168.00 is less than zero, so 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].bonus_mixed"
    value: "no"
    work: "Filer says the choice is the same for the whole class"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].bonus_full"
    value: "0.00"
    work: "100% x 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].bonus_forty"
    value: "0.00"
    work: "40% x 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].bonus_fullcase"
    value: "0.00"
    work: "100% x 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].bonus"
    value: "0.00"
    work: "Allowance = none; not 2025 property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].ub"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].rate_hy"
    value: "14.29%"
    work: "7-year, HY, year 1"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].rate_mq"
    value: "3.57%"
    work: "7-year, MQ Q4, year 1"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].macrs_hy"
    value: "0.00"
    work: "0 x 14.29%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].macrs_mq"
    value: "0.00"
    work: "0 x 3.57%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].macrs2025"
    value: "0.00"
    work: "Not 2025 property, and basis is 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].mqbase"
    value: "0.00"
    work: "after179 = 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].mq_q4_2025"
    value: "0.00"
    work: "Basis is 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].ub_prior_a"
    value: "0.00"
    work: "2,167.80 - 2,168.00 is less than zero, so 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].ub_prior"
    value: "0.00"
    work: "0 - special allowance claimed 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].rate_prior"
    value: "10.93%"
    work: "Table A-2: 7-year, MQ Q1, year 4"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].macrs_prior_live"
    value: "0.00"
    work: "0 x 10.93%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].macrs_prior"
    value: "0.00"
    work: "Pre-2025 property, recovery period not done: 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].dep_2025"
    value: "0.00"
    work: "Not 2025 property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].bonus_2025"
    value: "0.00"
    work: "Not 2025 property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].s179_2025"
    value: "0.00"
    work: "Not 2025 property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].mq_q4"
    value: "0.00"
    work: "Not 2025 property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].mq_total"
    value: "0.00"
    work: "Not 2025 property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].cost179"
    value: "0.00"
    work: "Not placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].cost179_2025"
    value: "0.00"
    work: "Business use is 50% or less"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].dep_prior"
    value: "0.00"
    work: "macrs_prior = 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].dep_listed"
    value: "0.00"
    work: "Not listed property"
```
