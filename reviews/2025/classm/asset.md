# Class M hand-work — asset

`Form 4562 — one item of depreciable property (other than a vehicle) of a business` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-20 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| subject sha256 | 4dc874fd2bcd2a44ecdc6360c0a2d3a51d0318e5e217e5a4bad17281fbc91bd1 |
| cases | 4 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i4562 | 2025 | 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 34, 37, 39, 41, 98 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 34, 37, 39, 41 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

## Lines

### case classm.asset.1 — prompt sha256 14a49449c7ca2f3ba7cf60890987b801fa69f767f5c79d30aa2e9b69c3cd384f; branches: asset.outside:false, asset.screen:false, asset.screened:false, asset.pct_bad:false, asset.listed:false, asset.over_half:false, asset.over_half:true, asset.listed_low:false, asset.is2025:false, asset.is2025:true, asset.on_19:false, asset.on_19:true, asset.on_17:false, asset.on_17:true, asset.on_26_2025:false, asset.done:false, asset.s179_bad:false, asset.after179:positive, asset.after_jan19:false, asset.after_jan19:true, asset.bonus_same:true, asset.bonus_mixed:false, asset.bonus_fullcase#0, asset.bonus_fullcase#1, asset.bonus#1, asset.bonus#2, asset.ub:positive, asset.macrs2025#1, asset.mq_q4_2025#1, asset.mq_q4_2025#3, asset.ub_prior_a:positive, asset.ub_prior:positive, asset.macrs_prior#0, asset.dep_2025#0, asset.dep_2025#1, asset.bonus_2025#0, asset.bonus_2025#1, asset.s179_2025#0, asset.s179_2025#1, asset.mq_q4#0, asset.mq_q4#1, asset.mq_total#0, asset.mq_total#1, asset.cost179#0, asset.cost179#1, asset.cost179_2025#0, asset.cost179_2025#1, asset.dep_prior#0, asset.dep_prior#1

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].period — Recovery period under GDS for the asset class
Status: **AGREE**

Value: y7

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].outside — The asset class is outside this tool
Status: **AGREE**

Value: no

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].screened — This property is outside this tool
Status: **AGREE**

Value: no

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].pct_c — The business use percentage, as cents
Status: **DISAGREE**

Project: $1.00
Model: $100.00
Work: 100% business use

Ruling: representation; project retained. pct_c carries the business-use percentage as one cent per percentage point (100% is $1.00) so that the percentage can be the part of a money ratio (prorate); the model wrote it as dollars. The basis it feeds agrees. Dropped from the fixture as not evidence. [dropped]

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].pct_bad — The business use percentage is more than 100
Status: **AGREE**

Value: no

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].listed_low — Listed property used 50% or less for business, or a percentage over 100
Status: **AGREE**

Value: no

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].basis — Basis for depreciation (business/investment use only), before section 179 and th
Status: **AGREE**

Value: $37,768.00

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].is2025 — Placed in service in 2025
Status: **AGREE**

Value: yes

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].on_19 — Reported on lines 6, 14 and 19 (property placed in service in 2025 that is not l
Status: **AGREE**

Value: yes

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].on_17 — Reported on line 17 (property placed in service before 2025 that is not listed p
Status: **AGREE**

Value: no

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].on_26_2025 — Reported on lines 25 and 26 column (i) (listed property placed in service in 202
Status: **AGREE**

Value: no

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].year — Year of recovery in 2025
Status: **AGREE**

Value: 1

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].last — Last year of recovery for the recovery period
Status: **AGREE**

Value: 8

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].done — The recovery period ended before 2025
Status: **AGREE**

Value: no

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq4

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].s179_bad — The section 179 election is more than the business cost, or the property is not 
Status: **AGREE**

Value: no

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].after179 — Basis less the section 179 election
Status: **AGREE**

Value: $37,768.00

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].bonus_mixed — The special allowance choice differs within a class
Status: **AGREE**

Value: no

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].bonus_full — 100% special allowance
Status: **AGREE**

Value: $37,768.00

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].bonus_forty — 40% special allowance
Status: **AGREE**

Value: $15,107.20

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **AGREE**

Value: $15,107.20

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].bonus — Special depreciation allowance for this property
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].ub — Basis for MACRS depreciation (after section 179 and the special allowance)
Status: **AGREE**

Value: $37,768.00

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].col19c — Basis for depreciation (business/investment use only), column (c), after the sec
Status: **AGREE**

Value: $37,768.00

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].rate_hy — MACRS rate, half-year convention
Status: **AGREE**

Value: 14.29%

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].rate_mq — MACRS rate, mid-quarter convention
Status: **AGREE**

Value: 3.57%

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].macrs_hy — MACRS depreciation, half-year convention
Status: **AGREE**

Value: $5,397.05

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].macrs_mq — MACRS depreciation, mid-quarter convention
Status: **AGREE**

Value: $1,348.32

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].macrs2025 — MACRS depreciation for 2025 property
Status: **AGREE**

Value: $1,348.32

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].mqbase — Depreciable basis for the mid-quarter test (after section 179, before the specia
Status: **AGREE**

Value: $37,768.00

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].mq_q4_2025 — That basis when placed in service October to December
Status: **AGREE**

Value: $37,768.00

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].ub_prior_a — Business basis less the section 179 deduction
Status: **AGREE**

Value: $37,768.00

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].ub_prior — Unadjusted basis
Status: **AGREE**

Value: $37,768.00

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].rate_prior — MACRS rate for the 2025 year of recovery
Status: **AGREE**

Value: 14.29%

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].macrs_prior_live — MACRS depreciation for 2025
Status: **AGREE**

Value: $5,397.05

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].dep_2025 — MACRS on 2025 property
Status: **AGREE**

Value: $1,348.32

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].bonus_2025 — Special allowance on 2025 property
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].s179_2025 — Section 179 elected on 2025 property
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].mq_q4 — Mid-quarter test basis, fourth quarter
Status: **AGREE**

Value: $37,768.00

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].mq_total — Mid-quarter test basis, all of 2025
Status: **AGREE**

Value: $37,768.00

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].cost179 — Cost of section 179 property placed in service in 2025
Status: **AGREE**

Value: $37,768.00

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].cost179_2025 — The business cost when used more than 50% in the business
Status: **AGREE**

Value: $37,768.00

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_1].dep_prior — MACRS on property placed in service before 2025
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].period — Recovery period under GDS for the asset class
Status: **AGREE**

Value: y20

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].outside — The asset class is outside this tool
Status: **AGREE**

Value: no

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].screened — This property is outside this tool
Status: **AGREE**

Value: no

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].pct_c — The business use percentage, as cents
Status: **DISAGREE**

Project: $0.01
Model: $1.00
Work: 1% business use

Ruling: representation; project retained. pct_c carries the business-use percentage as one cent per percentage point (100% is $1.00) so that the percentage can be the part of a money ratio (prorate); the model wrote it as dollars. The basis it feeds agrees. Dropped from the fixture as not evidence. [dropped]

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].pct_bad — The business use percentage is more than 100
Status: **AGREE**

Value: no

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].over_half — Business use is more than 50%
Status: **AGREE**

Value: no

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].listed_low — Listed property used 50% or less for business, or a percentage over 100
Status: **AGREE**

Value: no

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].basis — Basis for depreciation (business/investment use only), before section 179 and th
Status: **AGREE**

Value: $56.07

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].is2025 — Placed in service in 2025
Status: **AGREE**

Value: yes

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].on_19 — Reported on lines 6, 14 and 19 (property placed in service in 2025 that is not l
Status: **AGREE**

Value: yes

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].on_17 — Reported on line 17 (property placed in service before 2025 that is not listed p
Status: **AGREE**

Value: no

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].on_26_2025 — Reported on lines 25 and 26 column (i) (listed property placed in service in 202
Status: **AGREE**

Value: no

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].year — Year of recovery in 2025
Status: **AGREE**

Value: 1

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].last — Last year of recovery for the recovery period
Status: **AGREE**

Value: 21

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].done — The recovery period ended before 2025
Status: **AGREE**

Value: no

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq2

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].s179_bad — The section 179 election is more than the business cost, or the property is not 
Status: **DISAGREE**

Project: no
Model: yes
Work: Not used more than 50% in business

Ruling: model error; project retained. asset.s179_bad first requires a section 179 election greater than zero; this property's election is zero, so the gate is false whatever its business use. Dropped from the fixture as not evidence. [dropped]

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].after179 — Basis less the section 179 election
Status: **AGREE**

Value: $56.07

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].bonus_mixed — The special allowance choice differs within a class
Status: **AGREE**

Value: no

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].bonus_full — 100% special allowance
Status: **AGREE**

Value: $56.07

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].bonus_forty — 40% special allowance
Status: **AGREE**

Value: $22.43

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **AGREE**

Value: $22.43

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].bonus — Special depreciation allowance for this property
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].ub — Basis for MACRS depreciation (after section 179 and the special allowance)
Status: **AGREE**

Value: $56.07

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].col19c — Basis for depreciation (business/investment use only), column (c), after the sec
Status: **AGREE**

Value: $56.07

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].rate_hy — MACRS rate, half-year convention
Status: **AGREE**

Value: 3.75%

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].rate_mq — MACRS rate, mid-quarter convention
Status: **AGREE**

Value: 4.688%

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].macrs_hy — MACRS depreciation, half-year convention
Status: **AGREE**

Value: $2.10

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].macrs_mq — MACRS depreciation, mid-quarter convention
Status: **AGREE**

Value: $2.63

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].macrs2025 — MACRS depreciation for 2025 property
Status: **AGREE**

Value: $2.63

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].mqbase — Depreciable basis for the mid-quarter test (after section 179, before the specia
Status: **AGREE**

Value: $56.07

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].mq_q4_2025 — That basis when placed in service October to December
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].ub_prior_a — Business basis less the section 179 deduction
Status: **AGREE**

Value: $56.07

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].ub_prior — Unadjusted basis
Status: **AGREE**

Value: $56.07

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].rate_prior — MACRS rate for the 2025 year of recovery
Status: **AGREE**

Value: 6.563%

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].macrs_prior_live — MACRS depreciation for 2025
Status: **AGREE**

Value: $3.68

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].dep_2025 — MACRS on 2025 property
Status: **AGREE**

Value: $2.63

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].bonus_2025 — Special allowance on 2025 property
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].s179_2025 — Section 179 elected on 2025 property
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].mq_q4 — Mid-quarter test basis, fourth quarter
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].mq_total — Mid-quarter test basis, all of 2025
Status: **AGREE**

Value: $56.07

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].cost179 — Cost of section 179 property placed in service in 2025
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].cost179_2025 — The business cost when used more than 50% in the business
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[spouse].sc[biz_a].asset[item_2].dep_prior — MACRS on property placed in service before 2025
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].period — Recovery period under GDS for the asset class
Status: **AGREE**

Value: y5

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].outside — The asset class is outside this tool
Status: **AGREE**

Value: no

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].screened — This property is outside this tool
Status: **AGREE**

Value: no

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].pct_c — The business use percentage, as cents
Status: **DISAGREE**

Project: $1.00
Model: $100.00
Work: 100% business use

Ruling: representation; project retained. pct_c carries the business-use percentage as one cent per percentage point (100% is $1.00) so that the percentage can be the part of a money ratio (prorate); the model wrote it as dollars. The basis it feeds agrees. Dropped from the fixture as not evidence. [dropped]

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].pct_bad — The business use percentage is more than 100
Status: **AGREE**

Value: no

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].listed_low — Listed property used 50% or less for business, or a percentage over 100
Status: **AGREE**

Value: no

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].basis — Basis for depreciation (business/investment use only), before section 179 and th
Status: **AGREE**

Value: $5,325.00

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].is2025 — Placed in service in 2025
Status: **AGREE**

Value: no

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].on_19 — Reported on lines 6, 14 and 19 (property placed in service in 2025 that is not l
Status: **AGREE**

Value: no

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].on_17 — Reported on line 17 (property placed in service before 2025 that is not listed p
Status: **AGREE**

Value: yes

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].on_26_2025 — Reported on lines 25 and 26 column (i) (listed property placed in service in 202
Status: **AGREE**

Value: no

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].year — Year of recovery in 2025
Status: **AGREE**

Value: 4

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].last — Last year of recovery for the recovery period
Status: **AGREE**

Value: 6

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].done — The recovery period ended before 2025
Status: **AGREE**

Value: no

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq2

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].s179_bad — The section 179 election is more than the business cost, or the property is not 
Status: **AGREE**

Value: no

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].after179 — Basis less the section 179 election
Status: **AGREE**

Value: $5,325.00

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].bonus_mixed — The special allowance choice differs within a class
Status: **AGREE**

Value: no

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].bonus_full — 100% special allowance
Status: **AGREE**

Value: $5,325.00

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].bonus_forty — 40% special allowance
Status: **AGREE**

Value: $2,130.00

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **AGREE**

Value: $5,325.00

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].ub — Basis for MACRS depreciation (after section 179 and the special allowance)
Status: **DISAGREE**

Project: $3,195.00
Model: $5,325.00
Work: No 2025 allowance on pre-2025 property

Ruling: helper of a branch this entry does not take; project retained. The 2025-property route (basis after a 2025 allowance, the half-year and mid-quarter amounts, the 2025 section 179 cost) is figured for property placed in service before 2025 but read by no line it reaches, and the allowance alternatives are figured for property that claims none; the printed lines of the route the entry takes agree (for earlier property, the unadjusted basis, the 2025 rate and line 17). Dropped from the fixture as not evidence. [dropped]

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].rate_hy — MACRS rate, half-year convention
Status: **AGREE**

Value: 11.52%

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].rate_mq — MACRS rate, mid-quarter convention
Status: **AGREE**

Value: 11.37%

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].macrs_hy — MACRS depreciation, half-year convention
Status: **DISAGREE**

Project: $368.06
Model: $613.44
Work: 5,325 x 11.52%

Ruling: helper of a branch this entry does not take; project retained. The 2025-property route (basis after a 2025 allowance, the half-year and mid-quarter amounts, the 2025 section 179 cost) is figured for property placed in service before 2025 but read by no line it reaches, and the allowance alternatives are figured for property that claims none; the printed lines of the route the entry takes agree (for earlier property, the unadjusted basis, the 2025 rate and line 17). Dropped from the fixture as not evidence. [dropped]

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].macrs_mq — MACRS depreciation, mid-quarter convention
Status: **DISAGREE**

Project: $363.27
Model: $605.45
Work: 5,325 x 11.37%

Ruling: helper of a branch this entry does not take; project retained. The 2025-property route (basis after a 2025 allowance, the half-year and mid-quarter amounts, the 2025 section 179 cost) is figured for property placed in service before 2025 but read by no line it reaches, and the allowance alternatives are figured for property that claims none; the printed lines of the route the entry takes agree (for earlier property, the unadjusted basis, the 2025 rate and line 17). Dropped from the fixture as not evidence. [dropped]

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].mqbase — Depreciable basis for the mid-quarter test (after section 179, before the specia
Status: **AGREE**

Value: $5,325.00

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].mq_q4_2025 — That basis when placed in service October to December
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].ub_prior_a — Business basis less the section 179 deduction
Status: **AGREE**

Value: $5,325.00

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].ub_prior — Unadjusted basis
Status: **AGREE**

Value: $5,325.00

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].rate_prior — MACRS rate for the 2025 year of recovery
Status: **AGREE**

Value: 11.01%

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].macrs_prior_live — MACRS depreciation for 2025
Status: **AGREE**

Value: $586.28

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].macrs_prior — MACRS deduction for 2025 on property placed in service before 2025
Status: **AGREE**

Value: $586.28

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].dep_2025 — MACRS on 2025 property
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].bonus_2025 — Special allowance on 2025 property
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].s179_2025 — Section 179 elected on 2025 property
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].mq_q4 — Mid-quarter test basis, fourth quarter
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].mq_total — Mid-quarter test basis, all of 2025
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].cost179 — Cost of section 179 property placed in service in 2025
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].cost179_2025 — The business cost when used more than 50% in the business
Status: **AGREE**

Value: $5,325.00

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].dep_prior — MACRS on property placed in service before 2025
Status: **AGREE**

Value: $586.28

### case classm.asset.2 — prompt sha256 23361aa2a65953aa89556614eba8991857ee83af351e26adfb9922b5e02c44dd; branches: asset.outside:false, asset.screen:false, asset.screened:false, asset.pct_bad:false, asset.listed:false, asset.listed:true, asset.over_half:true, asset.listed_low:false, asset.is2025:true, asset.on_19:false, asset.on_19:true, asset.on_17:false, asset.on_26_2025:false, asset.on_26_2025:true, asset.done:false, asset.s179_bad:false, asset.after179:positive, asset.after_jan19:false, asset.after_jan19:true, asset.bonus_same:true, asset.bonus_mixed:false, asset.bonus_fullcase#0, asset.bonus_fullcase#1, asset.bonus#0, asset.bonus#2, asset.ub:floor, asset.ub:positive, asset.macrs2025#0, asset.mq_q4_2025#1, asset.mq_q4_2025#2, asset.ub_prior_a:positive, asset.ub_prior:positive, asset.macrs_prior#0, asset.dep_2025#0, asset.bonus_2025#0, asset.s179_2025#0, asset.mq_q4#0, asset.mq_total#0, asset.cost179#0, asset.cost179_2025#0, asset.dep_prior#1

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].period — Recovery period under GDS for the asset class
Status: **DISAGREE**

Project: y7
Model: y10
Work: Asset class 48.32 (Telephone Central Office Equipment), class life 18 years; 16 or more but less than 20 is 10-year property. Class life is from Pub. 946 Table B-2, which is not in the text provided.

Ruling: model error; project retained. The model recalled asset class 48.32 as having an 18-year class life ('from memory'); the archived Pub. 946 (2025) Appendix B, Table B-2, gives class 48.32 a class life of 13 years and a GDS recovery period of 7 years (tables/2025/class_lives.yaml, checked by its second transcription). The period, last year, rates and depreciation that follow from it differ for that reason. Dropped from the fixture as not evidence. [dropped]

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
Work: 100 percent expressed as cents.

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

Value: $19,315.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].is2025 — Placed in service in 2025
Status: **AGREE**

Value: yes

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].on_19 — Reported on lines 6, 14 and 19 (property placed in service in 2025 that is not l
Status: **AGREE**

Value: no

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].on_17 — Reported on line 17 (property placed in service before 2025 that is not listed p
Status: **AGREE**

Value: no

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].on_26_2025 — Reported on lines 25 and 26 column (i) (listed property placed in service in 202
Status: **AGREE**

Value: yes

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].year — Year of recovery in 2025
Status: **AGREE**

Value: 1

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].last — Last year of recovery for the recovery period
Status: **DISAGREE**

Project: 8
Model: 11
Work: 10-year recovery period plus the partial final year.

Ruling: model error; project retained. The model recalled asset class 48.32 as having an 18-year class life ('from memory'); the archived Pub. 946 (2025) Appendix B, Table B-2, gives class 48.32 a class life of 13 years and a GDS recovery period of 7 years (tables/2025/class_lives.yaml, checked by its second transcription). The period, last year, rates and depreciation that follow from it differ for that reason. Dropped from the fixture as not evidence. [dropped]

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].done — The recovery period ended before 2025
Status: **AGREE**

Value: no

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq3

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].s179_bad — The section 179 election is more than the business cost, or the property is not 
Status: **AGREE**

Value: no

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].after179 — Basis less the section 179 election
Status: **AGREE**

Value: $19,315.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].bonus_mixed — The special allowance choice differs within a class
Status: **AGREE**

Value: no

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].bonus_full — 100% special allowance
Status: **AGREE**

Value: $19,315.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].bonus_forty — 40% special allowance
Status: **AGREE**

Value: $7,726.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **AGREE**

Value: $19,315.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].f25 — Special depreciation allowance for this listed property (line 25)
Status: **AGREE**

Value: $19,315.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].f26i — Elected section 179 cost of this listed property (column (i))
Status: **AGREE**

Value: $0.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].ub — Basis for MACRS depreciation (after section 179 and the special allowance)
Status: **AGREE**

Value: $0.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].rate_hy — MACRS rate, half-year convention
Status: **DISAGREE**

Project: 14.29%
Model: 10%
Work: 2.00 / 10 = 20%, x 0.5.

Ruling: model error; project retained. The model recalled asset class 48.32 as having an 18-year class life ('from memory'); the archived Pub. 946 (2025) Appendix B, Table B-2, gives class 48.32 a class life of 13 years and a GDS recovery period of 7 years (tables/2025/class_lives.yaml, checked by its second transcription). The period, last year, rates and depreciation that follow from it differ for that reason. Dropped from the fixture as not evidence. [dropped]

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].rate_mq — MACRS rate, mid-quarter convention
Status: **DISAGREE**

Project: 10.71%
Model: 7.5%
Work: 20% x 0.375 (third quarter).

Ruling: model error; project retained. The model recalled asset class 48.32 as having an 18-year class life ('from memory'); the archived Pub. 946 (2025) Appendix B, Table B-2, gives class 48.32 a class life of 13 years and a GDS recovery period of 7 years (tables/2025/class_lives.yaml, checked by its second transcription). The period, last year, rates and depreciation that follow from it differ for that reason. Dropped from the fixture as not evidence. [dropped]

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].macrs_hy — MACRS depreciation, half-year convention
Status: **AGREE**

Value: $0.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].macrs_mq — MACRS depreciation, mid-quarter convention
Status: **AGREE**

Value: $0.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].mqbase — Depreciable basis for the mid-quarter test (after section 179, before the specia
Status: **AGREE**

Value: $19,315.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].mq_q4_2025 — That basis when placed in service October to December
Status: **AGREE**

Value: $0.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].ub_prior_a — Business basis less the section 179 deduction
Status: **AGREE**

Value: $19,315.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].ub_prior — Unadjusted basis
Status: **AGREE**

Value: $19,315.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].rate_prior — MACRS rate for the 2025 year of recovery
Status: **DISAGREE**

Project: 17.85%
Model: 12.5%
Work: Year 1, 10-year, mq2: 20% x 0.625.

Ruling: model error; project retained. The model recalled asset class 48.32 as having an 18-year class life ('from memory'); the archived Pub. 946 (2025) Appendix B, Table B-2, gives class 48.32 a class life of 13 years and a GDS recovery period of 7 years (tables/2025/class_lives.yaml, checked by its second transcription). The period, last year, rates and depreciation that follow from it differ for that reason. Dropped from the fixture as not evidence. [dropped]

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].macrs_prior_live — MACRS depreciation for 2025
Status: **DISAGREE**

Project: $3,447.73
Model: $2,414.38
Work: 19,315 x 12.50%.

Ruling: model error; project retained. The model recalled asset class 48.32 as having an 18-year class life ('from memory'); the archived Pub. 946 (2025) Appendix B, Table B-2, gives class 48.32 a class life of 13 years and a GDS recovery period of 7 years (tables/2025/class_lives.yaml, checked by its second transcription). The period, last year, rates and depreciation that follow from it differ for that reason. Dropped from the fixture as not evidence. [dropped]

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].dep_2025 — MACRS on 2025 property
Status: **AGREE**

Value: $0.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].bonus_2025 — Special allowance on 2025 property
Status: **AGREE**

Value: $19,315.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].s179_2025 — Section 179 elected on 2025 property
Status: **AGREE**

Value: $0.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].mq_q4 — Mid-quarter test basis, fourth quarter
Status: **AGREE**

Value: $0.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].mq_total — Mid-quarter test basis, all of 2025
Status: **AGREE**

Value: $19,315.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].cost179 — Cost of section 179 property placed in service in 2025
Status: **AGREE**

Value: $19,315.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].cost179_2025 — The business cost when used more than 50% in the business
Status: **AGREE**

Value: $19,315.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].dep_prior — MACRS on property placed in service before 2025
Status: **AGREE**

Value: $0.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].dep_listed — Depreciation of this listed property (column (h))
Status: **AGREE**

Value: $0.00

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].period — Recovery period under GDS for the asset class
Status: **AGREE**

Value: y15

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].outside — The asset class is outside this tool
Status: **AGREE**

Value: no

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].screened — This property is outside this tool
Status: **AGREE**

Value: no

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].pct_c — The business use percentage, as cents
Status: **DISAGREE**

Project: $1.00
Model: $100.00
Work: 100 percent expressed as cents.

Ruling: representation; project retained. pct_c carries the business-use percentage as one cent per percentage point (100% is $1.00) so that the percentage can be the part of a money ratio (prorate); the model wrote it as dollars. The basis it feeds agrees. Dropped from the fixture as not evidence. [dropped]

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].pct_bad — The business use percentage is more than 100
Status: **AGREE**

Value: no

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].listed_low — Listed property used 50% or less for business, or a percentage over 100
Status: **AGREE**

Value: no

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].basis — Basis for depreciation (business/investment use only), before section 179 and th
Status: **AGREE**

Value: $36,124.00

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].is2025 — Placed in service in 2025
Status: **AGREE**

Value: yes

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].on_19 — Reported on lines 6, 14 and 19 (property placed in service in 2025 that is not l
Status: **AGREE**

Value: yes

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].on_17 — Reported on line 17 (property placed in service before 2025 that is not listed p
Status: **AGREE**

Value: no

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].on_26_2025 — Reported on lines 25 and 26 column (i) (listed property placed in service in 202
Status: **AGREE**

Value: no

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].year — Year of recovery in 2025
Status: **AGREE**

Value: 1

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].last — Last year of recovery for the recovery period
Status: **AGREE**

Value: 16

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].done — The recovery period ended before 2025
Status: **AGREE**

Value: no

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq2

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].s179_bad — The section 179 election is more than the business cost, or the property is not 
Status: **AGREE**

Value: no

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].after179 — Basis less the section 179 election
Status: **AGREE**

Value: $32,935.00

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].bonus_mixed — The special allowance choice differs within a class
Status: **AGREE**

Value: no

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].bonus_full — 100% special allowance
Status: **AGREE**

Value: $32,935.00

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].bonus_forty — 40% special allowance
Status: **AGREE**

Value: $13,174.00

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **AGREE**

Value: $13,174.00

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].bonus — Special depreciation allowance for this property
Status: **AGREE**

Value: $0.00

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].ub — Basis for MACRS depreciation (after section 179 and the special allowance)
Status: **AGREE**

Value: $32,935.00

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].col19c — Basis for depreciation (business/investment use only), column (c), after the sec
Status: **AGREE**

Value: $32,935.00

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].rate_hy — MACRS rate, half-year convention
Status: **AGREE**

Value: 5%

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].rate_mq — MACRS rate, mid-quarter convention
Status: **AGREE**

Value: 6.25%

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].macrs_hy — MACRS depreciation, half-year convention
Status: **AGREE**

Value: $1,646.75

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].macrs_mq — MACRS depreciation, mid-quarter convention
Status: **AGREE**

Value: $2,058.44

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].macrs2025 — MACRS depreciation for 2025 property
Status: **AGREE**

Value: $1,646.75

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].mqbase — Depreciable basis for the mid-quarter test (after section 179, before the specia
Status: **AGREE**

Value: $32,935.00

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].mq_q4_2025 — That basis when placed in service October to December
Status: **AGREE**

Value: $0.00

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].ub_prior_a — Business basis less the section 179 deduction
Status: **AGREE**

Value: $36,124.00

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].ub_prior — Unadjusted basis
Status: **AGREE**

Value: $36,124.00

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].rate_prior — MACRS rate for the 2025 year of recovery
Status: **AGREE**

Value: 8.75%

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].macrs_prior_live — MACRS depreciation for 2025
Status: **AGREE**

Value: $3,160.85

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].dep_2025 — MACRS on 2025 property
Status: **AGREE**

Value: $1,646.75

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].bonus_2025 — Special allowance on 2025 property
Status: **AGREE**

Value: $0.00

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].s179_2025 — Section 179 elected on 2025 property
Status: **AGREE**

Value: $3,189.00

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].mq_q4 — Mid-quarter test basis, fourth quarter
Status: **AGREE**

Value: $0.00

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].mq_total — Mid-quarter test basis, all of 2025
Status: **AGREE**

Value: $32,935.00

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].cost179 — Cost of section 179 property placed in service in 2025
Status: **AGREE**

Value: $36,124.00

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].cost179_2025 — The business cost when used more than 50% in the business
Status: **AGREE**

Value: $36,124.00

### classm.asset.2 — person[taxpayer].sc[biz_b].asset[item_1].dep_prior — MACRS on property placed in service before 2025
Status: **AGREE**

Value: $0.00

### case classm.asset.3 — prompt sha256 8a73106a47419c393b4e19c67eee30ac906da054c36583520715b029d360b6f5; branches: asset.outside:false, asset.screen:false, asset.screened:false, asset.pct_bad:false, asset.listed:false, asset.over_half:true, asset.listed_low:false, asset.is2025:true, asset.on_19:true, asset.on_17:false, asset.on_26_2025:false, asset.done:false, asset.s179_bad:false, asset.after179:floor, asset.after179:positive, asset.after_jan19:true, asset.bonus_same:true, asset.bonus_mixed:false, asset.bonus_fullcase#0, asset.bonus#1, asset.bonus#2, asset.ub:floor, asset.ub:positive, asset.macrs2025#0, asset.mq_q4_2025#0, asset.mq_q4_2025#3, asset.ub_prior_a:positive, asset.ub_prior:positive, asset.macrs_prior#0, asset.dep_2025#0, asset.bonus_2025#0, asset.s179_2025#0, asset.mq_q4#0, asset.mq_total#0, asset.cost179#0, asset.cost179_2025#0, asset.dep_prior#1

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

Project: $1.00
Model: $100.00
Work: 100% business use

Ruling: representation; project retained. pct_c carries the business-use percentage as one cent per percentage point (100% is $1.00) so that the percentage can be the part of a money ratio (prorate); the model wrote it as dollars. The basis it feeds agrees. Dropped from the fixture as not evidence. [dropped]

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].pct_bad — The business use percentage is more than 100
Status: **AGREE**

Value: no

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].listed_low — Listed property used 50% or less for business, or a percentage over 100
Status: **AGREE**

Value: no

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].basis — Basis for depreciation (business/investment use only), before section 179 and th
Status: **AGREE**

Value: $22,713.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].is2025 — Placed in service in 2025
Status: **AGREE**

Value: yes

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].on_19 — Reported on lines 6, 14 and 19 (property placed in service in 2025 that is not l
Status: **AGREE**

Value: yes

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].on_17 — Reported on line 17 (property placed in service before 2025 that is not listed p
Status: **AGREE**

Value: no

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].on_26_2025 — Reported on lines 25 and 26 column (i) (listed property placed in service in 202
Status: **AGREE**

Value: no

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

Value: $14,788.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].bonus_mixed — The special allowance choice differs within a class
Status: **AGREE**

Value: no

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].bonus_full — 100% special allowance
Status: **AGREE**

Value: $14,788.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].bonus_forty — 40% special allowance
Status: **AGREE**

Value: $5,915.20

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **AGREE**

Value: $14,788.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].bonus — Special depreciation allowance for this property
Status: **AGREE**

Value: $5,915.20

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].ub — Basis for MACRS depreciation (after section 179 and the special allowance)
Status: **AGREE**

Value: $8,872.80

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].col19c — Basis for depreciation (business/investment use only), column (c), after the sec
Status: **AGREE**

Value: $8,872.80

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].rate_hy — MACRS rate, half-year convention
Status: **AGREE**

Value: 14.29%

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].rate_mq — MACRS rate, mid-quarter convention
Status: **AGREE**

Value: 25%

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].macrs_hy — MACRS depreciation, half-year convention
Status: **AGREE**

Value: $1,267.92

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].macrs_mq — MACRS depreciation, mid-quarter convention
Status: **AGREE**

Value: $2,218.20

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].macrs2025 — MACRS depreciation for 2025 property
Status: **AGREE**

Value: $1,267.92

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].mqbase — Depreciable basis for the mid-quarter test (after section 179, before the specia
Status: **AGREE**

Value: $14,788.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].mq_q4_2025 — That basis when placed in service October to December
Status: **AGREE**

Value: $0.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].ub_prior_a — Business basis less the section 179 deduction
Status: **AGREE**

Value: $22,713.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].ub_prior — Unadjusted basis
Status: **AGREE**

Value: $22,713.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].rate_prior — MACRS rate for the 2025 year of recovery
Status: **AGREE**

Value: 14.29%

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].macrs_prior_live — MACRS depreciation for 2025
Status: **AGREE**

Value: $3,245.69

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].dep_2025 — MACRS on 2025 property
Status: **AGREE**

Value: $1,267.92

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].bonus_2025 — Special allowance on 2025 property
Status: **AGREE**

Value: $5,915.20

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].s179_2025 — Section 179 elected on 2025 property
Status: **AGREE**

Value: $7,925.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].mq_q4 — Mid-quarter test basis, fourth quarter
Status: **AGREE**

Value: $0.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].mq_total — Mid-quarter test basis, all of 2025
Status: **AGREE**

Value: $14,788.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].cost179 — Cost of section 179 property placed in service in 2025
Status: **AGREE**

Value: $22,713.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].cost179_2025 — The business cost when used more than 50% in the business
Status: **AGREE**

Value: $22,713.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].dep_prior — MACRS on property placed in service before 2025
Status: **AGREE**

Value: $0.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].period — Recovery period under GDS for the asset class
Status: **AGREE**

Value: y5

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
Work: 100% business use

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

Value: $5,620.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].is2025 — Placed in service in 2025
Status: **AGREE**

Value: yes

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].on_19 — Reported on lines 6, 14 and 19 (property placed in service in 2025 that is not l
Status: **AGREE**

Value: yes

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].on_17 — Reported on line 17 (property placed in service before 2025 that is not listed p
Status: **AGREE**

Value: no

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].on_26_2025 — Reported on lines 25 and 26 column (i) (listed property placed in service in 202
Status: **AGREE**

Value: no

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].year — Year of recovery in 2025
Status: **AGREE**

Value: 1

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].last — Last year of recovery for the recovery period
Status: **AGREE**

Value: 6

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].done — The recovery period ended before 2025
Status: **AGREE**

Value: no

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq4

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

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].col19c — Basis for depreciation (business/investment use only), column (c), after the sec
Status: **AGREE**

Value: $0.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].rate_hy — MACRS rate, half-year convention
Status: **AGREE**

Value: 20%

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].rate_mq — MACRS rate, mid-quarter convention
Status: **AGREE**

Value: 5%

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

Value: $5,620.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].ub_prior — Unadjusted basis
Status: **AGREE**

Value: $5,620.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].rate_prior — MACRS rate for the 2025 year of recovery
Status: **AGREE**

Value: 15%

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].macrs_prior_live — MACRS depreciation for 2025
Status: **AGREE**

Value: $843.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].dep_2025 — MACRS on 2025 property
Status: **AGREE**

Value: $0.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].bonus_2025 — Special allowance on 2025 property
Status: **AGREE**

Value: $0.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].s179_2025 — Section 179 elected on 2025 property
Status: **AGREE**

Value: $5,620.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].mq_q4 — Mid-quarter test basis, fourth quarter
Status: **AGREE**

Value: $0.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].mq_total — Mid-quarter test basis, all of 2025
Status: **AGREE**

Value: $0.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].cost179 — Cost of section 179 property placed in service in 2025
Status: **AGREE**

Value: $5,620.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].cost179_2025 — The business cost when used more than 50% in the business
Status: **AGREE**

Value: $5,620.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_2].dep_prior — MACRS on property placed in service before 2025
Status: **AGREE**

Value: $0.00

### case classm.asset.4 — prompt sha256 17a1b305abc1a7c7a768881d3991299fe022f4a8a46baba43b9d17f0e51ee88c; branches: asset.outside:false, asset.screen:false, asset.screened:false, asset.pct_bad:false, asset.listed:false, asset.over_half:true, asset.listed_low:false, asset.is2025:false, asset.on_19:false, asset.on_17:true, asset.on_26_2025:false, asset.done:false, asset.s179_bad:false, asset.after179:positive, asset.after_jan19:true, asset.bonus_same:true, asset.bonus_mixed:false, asset.bonus_fullcase#0, asset.bonus#2, asset.ub:positive, asset.macrs2025#0, asset.mq_q4_2025#2, asset.ub_prior_a:positive, asset.ub_prior:floor, asset.macrs_prior#0, asset.dep_2025#1, asset.bonus_2025#1, asset.s179_2025#1, asset.mq_q4#1, asset.mq_total#1, asset.cost179#1, asset.cost179_2025#0, asset.dep_prior#0

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].period — Recovery period under GDS for the asset class
Status: **AGREE**

Value: y15

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].outside — The asset class is outside this tool
Status: **AGREE**

Value: no

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].screened — This property is outside this tool
Status: **AGREE**

Value: no

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].pct_c — The business use percentage, as cents
Status: **DISAGREE**

Project: $1.00
Model: $100.00
Work: Business use 100%, recorded as 100.00

Ruling: representation; project retained. pct_c carries the business-use percentage as one cent per percentage point (100% is $1.00) so that the percentage can be the part of a money ratio (prorate); the model wrote it as dollars. The basis it feeds agrees. Dropped from the fixture as not evidence. [dropped]

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].pct_bad — The business use percentage is more than 100
Status: **AGREE**

Value: no

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].listed_low — Listed property used 50% or less for business, or a percentage over 100
Status: **AGREE**

Value: no

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].basis — Basis for depreciation (business/investment use only), before section 179 and th
Status: **AGREE**

Value: $100.00

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].is2025 — Placed in service in 2025
Status: **AGREE**

Value: no

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].on_19 — Reported on lines 6, 14 and 19 (property placed in service in 2025 that is not l
Status: **AGREE**

Value: no

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].on_17 — Reported on line 17 (property placed in service before 2025 that is not listed p
Status: **AGREE**

Value: yes

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].on_26_2025 — Reported on lines 25 and 26 column (i) (listed property placed in service in 202
Status: **AGREE**

Value: no

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].year — Year of recovery in 2025
Status: **AGREE**

Value: 7

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].last — Last year of recovery for the recovery period
Status: **AGREE**

Value: 16

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].done — The recovery period ended before 2025
Status: **AGREE**

Value: no

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq3

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].s179_bad — The section 179 election is more than the business cost, or the property is not 
Status: **AGREE**

Value: no

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].after179 — Basis less the section 179 election
Status: **AGREE**

Value: $100.00

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].bonus_mixed — The special allowance choice differs within a class
Status: **AGREE**

Value: no

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].bonus_full — 100% special allowance
Status: **DISAGREE**

Project: $100.00
Model: $0.00
Work: Special allowance for this class is none

Ruling: helper of a branch this entry does not take; project retained. The 2025-property route (basis after a 2025 allowance, the half-year and mid-quarter amounts, the 2025 section 179 cost) is figured for property placed in service before 2025 but read by no line it reaches, and the allowance alternatives are figured for property that claims none; the printed lines of the route the entry takes agree (for earlier property, the unadjusted basis, the 2025 rate and line 17). Dropped from the fixture as not evidence. [dropped]

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].bonus_forty — 40% special allowance
Status: **DISAGREE**

Project: $40.00
Model: $0.00
Work: Special allowance for this class is none

Ruling: helper of a branch this entry does not take; project retained. The 2025-property route (basis after a 2025 allowance, the half-year and mid-quarter amounts, the 2025 section 179 cost) is figured for property placed in service before 2025 but read by no line it reaches, and the allowance alternatives are figured for property that claims none; the printed lines of the route the entry takes agree (for earlier property, the unadjusted basis, the 2025 rate and line 17). Dropped from the fixture as not evidence. [dropped]

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **DISAGREE**

Project: $100.00
Model: $0.00
Work: No allowance claimed (none)

Ruling: helper of a branch this entry does not take; project retained. The 2025-property route (basis after a 2025 allowance, the half-year and mid-quarter amounts, the 2025 section 179 cost) is figured for property placed in service before 2025 but read by no line it reaches, and the allowance alternatives are figured for property that claims none; the printed lines of the route the entry takes agree (for earlier property, the unadjusted basis, the 2025 rate and line 17). Dropped from the fixture as not evidence. [dropped]

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].ub — Basis for MACRS depreciation (after section 179 and the special allowance)
Status: **AGREE**

Value: $100.00

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].rate_hy — MACRS rate, half-year convention
Status: **DISAGREE**

Project: 5.9%
Model: 5%
Work: 15-year 150DB HY, year 1: 10% x 0.5 = 5.00%

Ruling: helper of a branch this entry does not take; project retained. The 2025-property route (basis after a 2025 allowance, the half-year and mid-quarter amounts, the 2025 section 179 cost) is figured for property placed in service before 2025 but read by no line it reaches, and the allowance alternatives are figured for property that claims none; the printed lines of the route the entry takes agree (for earlier property, the unadjusted basis, the 2025 rate and line 17). Dropped from the fixture as not evidence. [dropped]

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].rate_mq — MACRS rate, mid-quarter convention
Status: **DISAGREE**

Project: 5.9%
Model: 3.75%
Work: 15-year 150DB MQ, 3rd quarter, year 1: 10% x 0.375 = 3.75%

Ruling: helper of a branch this entry does not take; project retained. The 2025-property route (basis after a 2025 allowance, the half-year and mid-quarter amounts, the 2025 section 179 cost) is figured for property placed in service before 2025 but read by no line it reaches, and the allowance alternatives are figured for property that claims none; the printed lines of the route the entry takes agree (for earlier property, the unadjusted basis, the 2025 rate and line 17). Dropped from the fixture as not evidence. [dropped]

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].macrs_hy — MACRS depreciation, half-year convention
Status: **DISAGREE**

Project: $5.90
Model: $5.00
Work: $100.00 x 5.00% = $5.00

Ruling: helper of a branch this entry does not take; project retained. The 2025-property route (basis after a 2025 allowance, the half-year and mid-quarter amounts, the 2025 section 179 cost) is figured for property placed in service before 2025 but read by no line it reaches, and the allowance alternatives are figured for property that claims none; the printed lines of the route the entry takes agree (for earlier property, the unadjusted basis, the 2025 rate and line 17). Dropped from the fixture as not evidence. [dropped]

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].macrs_mq — MACRS depreciation, mid-quarter convention
Status: **DISAGREE**

Project: $5.90
Model: $3.75
Work: $100.00 x 3.75% = $3.75

Ruling: helper of a branch this entry does not take; project retained. The 2025-property route (basis after a 2025 allowance, the half-year and mid-quarter amounts, the 2025 section 179 cost) is figured for property placed in service before 2025 but read by no line it reaches, and the allowance alternatives are figured for property that claims none; the printed lines of the route the entry takes agree (for earlier property, the unadjusted basis, the 2025 rate and line 17). Dropped from the fixture as not evidence. [dropped]

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].mqbase — Depreciable basis for the mid-quarter test (after section 179, before the specia
Status: **AGREE**

Value: $100.00

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].mq_q4_2025 — That basis when placed in service October to December
Status: **AGREE**

Value: $0.00

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].ub_prior_a — Business basis less the section 179 deduction
Status: **AGREE**

Value: $100.00

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].ub_prior — Unadjusted basis
Status: **AGREE**

Value: $0.00

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].rate_prior — MACRS rate for the 2025 year of recovery
Status: **AGREE**

Value: 5.9%

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].macrs_prior_live — MACRS depreciation for 2025
Status: **AGREE**

Value: $0.00

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].macrs_prior — MACRS deduction for 2025 on property placed in service before 2025
Status: **AGREE**

Value: $0.00

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].dep_2025 — MACRS on 2025 property
Status: **AGREE**

Value: $0.00

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

Value: $0.00

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].cost179 — Cost of section 179 property placed in service in 2025
Status: **AGREE**

Value: $0.00

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].cost179_2025 — The business cost when used more than 50% in the business
Status: **DISAGREE**

Project: $100.00
Model: $0.00
Work: Not placed in service in 2025

Ruling: helper of a branch this entry does not take; project retained. The 2025-property route (basis after a 2025 allowance, the half-year and mid-quarter amounts, the 2025 section 179 cost) is figured for property placed in service before 2025 but read by no line it reaches, and the allowance alternatives are figured for property that claims none; the printed lines of the route the entry takes agree (for earlier property, the unadjusted basis, the 2025 rate and line 17). Dropped from the fixture as not evidence. [dropped]

### classm.asset.4 — person[taxpayer].sc[biz_a].asset[item_1].dep_prior — MACRS on property placed in service before 2025
Status: **AGREE**

Value: $0.00

## Raw responses

### classm.asset.1

```yaml
```yaml
lines:
  - printed: "person[spouse].sc[biz_a].asset[item_1].period"
    value: "y7"
    work: "Pub. 946 App. B asset class 33.2: class life 14 years, so 7-year GDS (10 or more but less than 16)"
  - printed: "person[spouse].sc[biz_a].asset[item_1].outside"
    value: "no"
    work: "Class 33.2 is ordinary MACRS GDS property"
  - printed: "person[spouse].sc[biz_a].asset[item_1].screened"
    value: "no"
    work: "Filer answered no to the exclusions"
  - printed: "person[spouse].sc[biz_a].asset[item_1].pct_c"
    value: "100.00"
    work: "100% business use"
  - printed: "person[spouse].sc[biz_a].asset[item_1].pct_bad"
    value: "no"
    work: "100 is not more than 100"
  - printed: "person[spouse].sc[biz_a].asset[item_1].over_half"
    value: "yes"
    work: "100% > 50%"
  - printed: "person[spouse].sc[biz_a].asset[item_1].listed_low"
    value: "no"
    work: "Not listed property"
  - printed: "person[spouse].sc[biz_a].asset[item_1].basis"
    value: "37768.00"
    work: "37,768.00 x 100%"
  - printed: "person[spouse].sc[biz_a].asset[item_1].is2025"
    value: "yes"
    work: "Placed in service in 2025"
  - printed: "person[spouse].sc[biz_a].asset[item_1].on_19"
    value: "yes"
    work: "2025 property, not listed"
  - printed: "person[spouse].sc[biz_a].asset[item_1].on_17"
    value: "no"
    work: "Not placed in service before 2025"
  - printed: "person[spouse].sc[biz_a].asset[item_1].on_26_2025"
    value: "no"
    work: "Not listed property"
  - printed: "person[spouse].sc[biz_a].asset[item_1].year"
    value: "1"
    work: "2025 - 2025 + 1"
  - printed: "person[spouse].sc[biz_a].asset[item_1].last"
    value: "8"
    work: "7-year period + 1 for the convention"
  - printed: "person[spouse].sc[biz_a].asset[item_1].done"
    value: "no"
    work: "Year 1 is not more than 8"
  - printed: "person[spouse].sc[biz_a].asset[item_1].qconv"
    value: "mq4"
    work: "Placed in service in Q4"
  - printed: "person[spouse].sc[biz_a].asset[item_1].s179_bad"
    value: "no"
    work: "0 elected is not more than the cost; use is over 50%"
  - printed: "person[spouse].sc[biz_a].asset[item_1].after179"
    value: "37768.00"
    work: "37,768.00 - 0"
  - printed: "person[spouse].sc[biz_a].asset[item_1].bonus_mixed"
    value: "no"
    work: "Choice is the same for the class"
  - printed: "person[spouse].sc[biz_a].asset[item_1].bonus_full"
    value: "37768.00"
    work: "100% x 37,768.00"
  - printed: "person[spouse].sc[biz_a].asset[item_1].bonus_forty"
    value: "15107.20"
    work: "40% x 37,768.00"
  - printed: "person[spouse].sc[biz_a].asset[item_1].bonus_fullcase"
    value: "15107.20"
    work: "Not acquired after 1/19/2025, so 40%"
  - printed: "person[spouse].sc[biz_a].asset[item_1].bonus"
    value: "0.00"
    work: "Class choice is none"
  - printed: "person[spouse].sc[biz_a].asset[item_1].ub"
    value: "37768.00"
    work: "37,768.00 - 0 - 0"
  - printed: "person[spouse].sc[biz_a].asset[item_1].col19c"
    value: "37768.00"
    work: "Basis after section 179 and allowance"
  - printed: "person[spouse].sc[biz_a].asset[item_1].rate_hy"
    value: "14.29%"
    work: "7-yr 200DB: 2/7 x 0.5"
  - printed: "person[spouse].sc[biz_a].asset[item_1].rate_mq"
    value: "3.57%"
    work: "7-yr 200DB: 2/7 x 0.125 (Q4)"
  - printed: "person[spouse].sc[biz_a].asset[item_1].macrs_hy"
    value: "5397.05"
    work: "37,768 x 14.29%"
  - printed: "person[spouse].sc[biz_a].asset[item_1].macrs_mq"
    value: "1348.32"
    work: "37,768 x 3.57%"
  - printed: "person[spouse].sc[biz_a].asset[item_1].macrs2025"
    value: "1348.32"
    work: "Mid-quarter test is met, so MQ amount"
  - printed: "person[spouse].sc[biz_a].asset[item_1].mqbase"
    value: "37768.00"
    work: "Basis after section 179, before the allowance"
  - printed: "person[spouse].sc[biz_a].asset[item_1].mq_q4_2025"
    value: "37768.00"
    work: "Placed in service in Q4"
  - printed: "person[spouse].sc[biz_a].asset[item_1].ub_prior_a"
    value: "37768.00"
    work: "37,768.00 - 0"
  - printed: "person[spouse].sc[biz_a].asset[item_1].ub_prior"
    value: "37768.00"
    work: "Less special allowance claimed of 0"
  - printed: "person[spouse].sc[biz_a].asset[item_1].rate_prior"
    value: "14.29%"
    work: "Original convention hy, 7-yr, year 1"
  - printed: "person[spouse].sc[biz_a].asset[item_1].macrs_prior_live"
    value: "5397.05"
    work: "37,768 x 14.29%"
  - printed: "person[spouse].sc[biz_a].asset[item_1].dep_2025"
    value: "1348.32"
    work: "2025 property MACRS"
  - printed: "person[spouse].sc[biz_a].asset[item_1].bonus_2025"
    value: "0.00"
    work: "No allowance"
  - printed: "person[spouse].sc[biz_a].asset[item_1].s179_2025"
    value: "0.00"
    work: "None elected"
  - printed: "person[spouse].sc[biz_a].asset[item_1].mq_q4"
    value: "37768.00"
    work: "2025 property in Q4"
  - printed: "person[spouse].sc[biz_a].asset[item_1].mq_total"
    value: "37768.00"
    work: "2025 property"
  - printed: "person[spouse].sc[biz_a].asset[item_1].cost179"
    value: "37768.00"
    work: "2025 property used more than 50%"
  - printed: "person[spouse].sc[biz_a].asset[item_1].cost179_2025"
    value: "37768.00"
    work: "Business cost; use is over 50%"
  - printed: "person[spouse].sc[biz_a].asset[item_1].dep_prior"
    value: "0.00"
    work: "Not prior-year property"
  - printed: "person[spouse].sc[biz_a].asset[item_2].period"
    value: "y20"
    work: "Asset class 49.4: class life 28 years, so 20-year GDS (25 or more)"
  - printed: "person[spouse].sc[biz_a].asset[item_2].outside"
    value: "no"
    work: "Ordinary MACRS GDS class"
  - printed: "person[spouse].sc[biz_a].asset[item_2].screened"
    value: "no"
    work: "Filer answered no to the exclusions"
  - printed: "person[spouse].sc[biz_a].asset[item_2].pct_c"
    value: "1.00"
    work: "1% business use"
  - printed: "person[spouse].sc[biz_a].asset[item_2].pct_bad"
    value: "no"
    work: "1 is not more than 100"
  - printed: "person[spouse].sc[biz_a].asset[item_2].over_half"
    value: "no"
    work: "1% is not more than 50%"
  - printed: "person[spouse].sc[biz_a].asset[item_2].listed_low"
    value: "no"
    work: "Not listed property"
  - printed: "person[spouse].sc[biz_a].asset[item_2].basis"
    value: "56.07"
    work: "5,607.00 x 1%"
  - printed: "person[spouse].sc[biz_a].asset[item_2].is2025"
    value: "yes"
    work: "Placed in service in 2025"
  - printed: "person[spouse].sc[biz_a].asset[item_2].on_19"
    value: "yes"
    work: "2025 property, not listed"
  - printed: "person[spouse].sc[biz_a].asset[item_2].on_17"
    value: "no"
    work: "Not prior-year property"
  - printed: "person[spouse].sc[biz_a].asset[item_2].on_26_2025"
    value: "no"
    work: "Not listed property"
  - printed: "person[spouse].sc[biz_a].asset[item_2].year"
    value: "1"
    work: "2025 - 2025 + 1"
  - printed: "person[spouse].sc[biz_a].asset[item_2].last"
    value: "21"
    work: "20-year period + 1"
  - printed: "person[spouse].sc[biz_a].asset[item_2].done"
    value: "no"
    work: "Year 1 is not more than 21"
  - printed: "person[spouse].sc[biz_a].asset[item_2].qconv"
    value: "mq2"
    work: "Placed in service in Q2"
  - printed: "person[spouse].sc[biz_a].asset[item_2].s179_bad"
    value: "yes"
    work: "Not used more than 50% in business"
  - printed: "person[spouse].sc[biz_a].asset[item_2].after179"
    value: "56.07"
    work: "56.07 - 0"
  - printed: "person[spouse].sc[biz_a].asset[item_2].bonus_mixed"
    value: "no"
    work: "Choice is the same for the class"
  - printed: "person[spouse].sc[biz_a].asset[item_2].bonus_full"
    value: "56.07"
    work: "100% x 56.07"
  - printed: "person[spouse].sc[biz_a].asset[item_2].bonus_forty"
    value: "22.43"
    work: "40% x 56.07"
  - printed: "person[spouse].sc[biz_a].asset[item_2].bonus_fullcase"
    value: "22.43"
    work: "Not acquired after 1/19/2025, so 40%"
  - printed: "person[spouse].sc[biz_a].asset[item_2].bonus"
    value: "0.00"
    work: "Class choice is none"
  - printed: "person[spouse].sc[biz_a].asset[item_2].ub"
    value: "56.07"
    work: "56.07 - 0 - 0"
  - printed: "person[spouse].sc[biz_a].asset[item_2].col19c"
    value: "56.07"
    work: "Basis after section 179 and allowance"
  - printed: "person[spouse].sc[biz_a].asset[item_2].rate_hy"
    value: "3.750%"
    work: "20-yr 150DB: 1.5/20 x 0.5"
  - printed: "person[spouse].sc[biz_a].asset[item_2].rate_mq"
    value: "4.688%"
    work: "1.5/20 x 0.625 (Q2)"
  - printed: "person[spouse].sc[biz_a].asset[item_2].macrs_hy"
    value: "2.10"
    work: "56.07 x 3.75%"
  - printed: "person[spouse].sc[biz_a].asset[item_2].macrs_mq"
    value: "2.63"
    work: "56.07 x 4.688%"
  - printed: "person[spouse].sc[biz_a].asset[item_2].macrs2025"
    value: "2.63"
    work: "Mid-quarter test is met"
  - printed: "person[spouse].sc[biz_a].asset[item_2].mqbase"
    value: "56.07"
    work: "Basis after section 179, before the allowance"
  - printed: "person[spouse].sc[biz_a].asset[item_2].mq_q4_2025"
    value: "0.00"
    work: "Placed in service in Q2, not Q4"
  - printed: "person[spouse].sc[biz_a].asset[item_2].ub_prior_a"
    value: "56.07"
    work: "56.07 - 0"
  - printed: "person[spouse].sc[biz_a].asset[item_2].ub_prior"
    value: "56.07"
    work: "Less special allowance claimed of 0"
  - printed: "person[spouse].sc[biz_a].asset[item_2].rate_prior"
    value: "6.563%"
    work: "Original convention mq1: 1.5/20 x 0.875"
  - printed: "person[spouse].sc[biz_a].asset[item_2].macrs_prior_live"
    value: "3.68"
    work: "56.07 x 6.563%"
  - printed: "person[spouse].sc[biz_a].asset[item_2].dep_2025"
    value: "2.63"
    work: "2025 property MACRS"
  - printed: "person[spouse].sc[biz_a].asset[item_2].bonus_2025"
    value: "0.00"
    work: "No allowance"
  - printed: "person[spouse].sc[biz_a].asset[item_2].s179_2025"
    value: "0.00"
    work: "None elected"
  - printed: "person[spouse].sc[biz_a].asset[item_2].mq_q4"
    value: "0.00"
    work: "Not Q4"
  - printed: "person[spouse].sc[biz_a].asset[item_2].mq_total"
    value: "56.07"
    work: "2025 property"
  - printed: "person[spouse].sc[biz_a].asset[item_2].cost179"
    value: "0.00"
    work: "Not used more than 50%"
  - printed: "person[spouse].sc[biz_a].asset[item_2].cost179_2025"
    value: "0.00"
    work: "Use is 50% or less"
  - printed: "person[spouse].sc[biz_a].asset[item_2].dep_prior"
    value: "0.00"
    work: "Not prior-year property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].period"
    value: "y5"
    work: "Asset class 48.2: class life 6 years, so 5-year GDS (more than 4 but less than 10)"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].outside"
    value: "no"
    work: "Ordinary MACRS GDS class"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].screened"
    value: "no"
    work: "Filer answered no to the exclusions"
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
    value: "5325.00"
    work: "5,325.00 x 100%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].is2025"
    value: "no"
    work: "Placed in service in 2022"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].on_19"
    value: "no"
    work: "Not 2025 property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].on_17"
    value: "yes"
    work: "Pre-2025, not listed"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].on_26_2025"
    value: "no"
    work: "Not listed property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].year"
    value: "4"
    work: "2025 - 2022 + 1"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].last"
    value: "6"
    work: "5-year period + 1"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].done"
    value: "no"
    work: "Year 4 is not more than 6"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].qconv"
    value: "mq2"
    work: "Quarter given is q2"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].s179_bad"
    value: "no"
    work: "0 elected; use is over 50%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].after179"
    value: "5325.00"
    work: "5,325.00 - 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_mixed"
    value: "no"
    work: "Choice is the same for the class"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_full"
    value: "5325.00"
    work: "100% x 5,325.00"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_forty"
    value: "2130.00"
    work: "40% x 5,325.00"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_fullcase"
    value: "5325.00"
    work: "Acquired after 1/19/2025, so 100%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].ub"
    value: "5325.00"
    work: "No 2025 allowance on pre-2025 property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].rate_hy"
    value: "11.52%"
    work: "5-yr 200DB HY, year 4"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].rate_mq"
    value: "11.37%"
    work: "5-yr 200DB MQ Q2, year 4"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs_hy"
    value: "613.44"
    work: "5,325 x 11.52%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs_mq"
    value: "605.45"
    work: "5,325 x 11.37%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].mqbase"
    value: "5325.00"
    work: "Basis after section 179"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].mq_q4_2025"
    value: "0.00"
    work: "Not Q4"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].ub_prior_a"
    value: "5325.00"
    work: "5,325.00 - 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].ub_prior"
    value: "5325.00"
    work: "Less special allowance claimed of 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].rate_prior"
    value: "11.01%"
    work: "mq1, year 4: SL 23.40/2.125 years exceeds DB"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs_prior_live"
    value: "586.28"
    work: "5,325 x 11.01%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs_prior"
    value: "586.28"
    work: "Recovery period not ended"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].dep_2025"
    value: "0.00"
    work: "Not 2025 property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_2025"
    value: "0.00"
    work: "Not 2025 property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].s179_2025"
    value: "0.00"
    work: "Not 2025 property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].mq_q4"
    value: "0.00"
    work: "Not 2025 property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].mq_total"
    value: "0.00"
    work: "Not 2025 property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].cost179"
    value: "0.00"
    work: "Not placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].cost179_2025"
    value: "5325.00"
    work: "Business cost; use is over 50%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].dep_prior"
    value: "586.28"
    work: "Line 17 amount"
```
```

### classm.asset.2

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].period"
    value: "y10"
    work: "Asset class 48.32 (Telephone Central Office Equipment), class life 18 years; 16 or more but less than 20 is 10-year property. Class life is from Pub. 946 Table B-2, which is not in the text provided."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].outside"
    value: "no"
    work: "The asset class is a standard GDS class."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].screened"
    value: "no"
    work: "Filer answered no to the screening question."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].pct_c"
    value: "100.00"
    work: "100 percent expressed as cents."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].pct_bad"
    value: "no"
    work: "100 is not more than 100."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].over_half"
    value: "yes"
    work: "100% is more than 50%."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].listed_low"
    value: "no"
    work: "Listed property used 100% for business."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].basis"
    value: "19315.00"
    work: "19,315 x 100%."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].is2025"
    value: "yes"
    work: "Placed in service in 2025."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].on_19"
    value: "no"
    work: "Listed property is reported in Part V, not on line 19."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].on_17"
    value: "no"
    work: "Placed in service in 2025, and it is listed property."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].on_26_2025"
    value: "yes"
    work: "Listed property, used more than 50%, placed in service in 2025."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].year"
    value: "1"
    work: "2025 - 2025 + 1."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].last"
    value: "11"
    work: "10-year recovery period plus the partial final year."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].done"
    value: "no"
    work: "Year 1 is not past the last year (11)."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].qconv"
    value: "mq3"
    work: "Placed in service in the third quarter."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].s179_bad"
    value: "no"
    work: "Election of 0 is not more than 19,315, and use is over 50%."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].after179"
    value: "19315.00"
    work: "19,315 - 0."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_mixed"
    value: "no"
    work: "Same choice for all property in the class."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_full"
    value: "19315.00"
    work: "19,315 x 100%."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_forty"
    value: "7726.00"
    work: "19,315 x 40%."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_fullcase"
    value: "19315.00"
    work: "Acquired after January 19, 2025, so 100% applies."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].f25"
    value: "19315.00"
    work: "Full special allowance claimed on qualified listed property."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].f26i"
    value: "0.00"
    work: "No section 179 elected."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].ub"
    value: "0.00"
    work: "19,315 - 0 - 19,315."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].rate_hy"
    value: "10.00%"
    work: "2.00 / 10 = 20%, x 0.5."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].rate_mq"
    value: "7.50%"
    work: "20% x 0.375 (third quarter)."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs_hy"
    value: "0.00"
    work: "0 x 10.00%."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs_mq"
    value: "0.00"
    work: "0 x 7.50%."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].mqbase"
    value: "19315.00"
    work: "After section 179, before the special allowance."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].mq_q4_2025"
    value: "0.00"
    work: "Not placed in service in the fourth quarter."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].ub_prior_a"
    value: "19315.00"
    work: "19,315 - 0 section 179."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].ub_prior"
    value: "19315.00"
    work: "19,315 - 0 special allowance claimed."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].rate_prior"
    value: "12.50%"
    work: "Year 1, 10-year, mq2: 20% x 0.625."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs_prior_live"
    value: "2414.38"
    work: "19,315 x 12.50%."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].dep_2025"
    value: "0.00"
    work: "Half-year MACRS on a basis of 0."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_2025"
    value: "19315.00"
    work: "Special allowance on 2025 property."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].s179_2025"
    value: "0.00"
    work: "No election."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].mq_q4"
    value: "0.00"
    work: "Third-quarter property."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].mq_total"
    value: "19315.00"
    work: "Equals mqbase."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].cost179"
    value: "19315.00"
    work: "Business cost; listed property is included on line 2."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].cost179_2025"
    value: "19315.00"
    work: "Used more than 50% in the business."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].dep_prior"
    value: "0.00"
    work: "Not placed in service before 2025."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].dep_listed"
    value: "0.00"
    work: "Column (h) equals MACRS on a basis of 0."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].period"
    value: "y15"
    work: "Asset class 44.0 (Water Transportation), class life 20 years; 20 or more but less than 25 is 15-year property. Class life is from Pub. 946 Table B-2, which is not in the text provided."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].outside"
    value: "no"
    work: "The asset class is a standard GDS class."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].screened"
    value: "no"
    work: "Filer answered no to the screening question."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].pct_c"
    value: "100.00"
    work: "100 percent expressed as cents."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].pct_bad"
    value: "no"
    work: "100 is not more than 100."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].over_half"
    value: "yes"
    work: "100% is more than 50%."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].listed_low"
    value: "no"
    work: "Not listed property."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].basis"
    value: "36124.00"
    work: "36,124 x 100%."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].is2025"
    value: "yes"
    work: "Placed in service in 2025."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].on_19"
    value: "yes"
    work: "2025 property that is not listed property."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].on_17"
    value: "no"
    work: "Placed in service in 2025."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].on_26_2025"
    value: "no"
    work: "Not listed property."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].year"
    value: "1"
    work: "2025 - 2025 + 1."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].last"
    value: "16"
    work: "15-year recovery period plus the partial final year."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].done"
    value: "no"
    work: "Year 1 is not past the last year (16)."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].qconv"
    value: "mq2"
    work: "Placed in service in the second quarter."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].s179_bad"
    value: "no"
    work: "3,189 is not more than 36,124, and use is over 50%."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].after179"
    value: "32935.00"
    work: "36,124 - 3,189."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].bonus_mixed"
    value: "no"
    work: "Same choice for all property in the class."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].bonus_full"
    value: "32935.00"
    work: "32,935 x 100%."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].bonus_forty"
    value: "13174.00"
    work: "32,935 x 40%."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].bonus_fullcase"
    value: "13174.00"
    work: "Not acquired after January 19, 2025, so 40% applies."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].bonus"
    value: "0.00"
    work: "Special allowance for the class is none (election out)."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].ub"
    value: "32935.00"
    work: "36,124 - 3,189 - 0."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].col19c"
    value: "32935.00"
    work: "Equals ub."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].rate_hy"
    value: "5.00%"
    work: "1.50 / 15 = 10%, x 0.5."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].rate_mq"
    value: "6.25%"
    work: "10% x 0.625 (second quarter)."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].macrs_hy"
    value: "1646.75"
    work: "32,935 x 5.00%."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].macrs_mq"
    value: "2058.44"
    work: "32,935 x 6.25%."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].macrs2025"
    value: "1646.75"
    work: "Mid-quarter does not apply, so the half-year amount is used."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].mqbase"
    value: "32935.00"
    work: "After section 179, before the special allowance."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].mq_q4_2025"
    value: "0.00"
    work: "Second-quarter property."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].ub_prior_a"
    value: "36124.00"
    work: "36,124 - 0 prior section 179."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].ub_prior"
    value: "36124.00"
    work: "36,124 - 0 special allowance claimed."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].rate_prior"
    value: "8.75%"
    work: "Year 1, 15-year, mq1: 10% x 0.875."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].macrs_prior_live"
    value: "3160.85"
    work: "36,124 x 8.75%."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].dep_2025"
    value: "1646.75"
    work: "Equals macrs2025."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].bonus_2025"
    value: "0.00"
    work: "No special allowance."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].s179_2025"
    value: "3189.00"
    work: "Elected section 179 cost."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].mq_q4"
    value: "0.00"
    work: "Second-quarter property."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].mq_total"
    value: "32935.00"
    work: "Equals mqbase."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].cost179"
    value: "36124.00"
    work: "Business cost of section 179 property."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].cost179_2025"
    value: "36124.00"
    work: "Used more than 50% in the business."
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].dep_prior"
    value: "0.00"
    work: "Not placed in service before 2025."
```
```

### classm.asset.3

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].period"
    value: "y7"
    work: "Pub. 946 Table B-2 asset class 40.1 has a 14-year class life; 10 or more but less than 16 gives 7-year property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].outside"
    value: "no"
    work: "Class 40.1 is ordinary 7-year GDS property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].screened"
    value: "no"
    work: "No special situation applies and the class is in scope"
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
    value: "22713.00"
    work: "22,713.00 x 100%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].is2025"
    value: "yes"
    work: "Placed in service y2025"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].on_19"
    value: "yes"
    work: "2025 property that is not listed property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].on_17"
    value: "no"
    work: "Not placed in service before 2025"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].on_26_2025"
    value: "no"
    work: "Not listed property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].year"
    value: "1"
    work: "2025 - 2025 + 1"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].last"
    value: "8"
    work: "7-year property recovers over 8 tax years"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].done"
    value: "no"
    work: "Year 1 is not after year 8"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].qconv"
    value: "mq1"
    work: "Placed in service in Q1"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].s179_bad"
    value: "no"
    work: "7,925 is not more than 22,713, and business use is over 50%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].after179"
    value: "14788.00"
    work: "22,713.00 - 7,925.00"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_mixed"
    value: "no"
    work: "The choice is the same for the whole class"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_full"
    value: "14788.00"
    work: "14,788.00 x 100%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_forty"
    value: "5915.20"
    work: "14,788.00 x 40%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_fullcase"
    value: "14788.00"
    work: "Acquired after Jan 19, 2025, so 100%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus"
    value: "5915.20"
    work: "40% allowance elected for this class"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].ub"
    value: "8872.80"
    work: "14,788.00 - 5,915.20"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].col19c"
    value: "8872.80"
    work: "Basis after section 179 and the special allowance"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].rate_hy"
    value: "14.29%"
    work: "7-year property, half-year convention, year 1"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].rate_mq"
    value: "25.00%"
    work: "7-year property, mid-quarter Q1, year 1"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs_hy"
    value: "1267.92"
    work: "8,872.80 x 14.29%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs_mq"
    value: "2218.20"
    work: "8,872.80 x 25.00%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs2025"
    value: "1267.92"
    work: "Mid-quarter test is no, so half-year convention applies"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].mqbase"
    value: "14788.00"
    work: "After section 179, before the special allowance"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].mq_q4_2025"
    value: "0.00"
    work: "Placed in service in Q1, not Q4"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].ub_prior_a"
    value: "22713.00"
    work: "22,713.00 - 0.00 prior section 179"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].ub_prior"
    value: "22713.00"
    work: "22,713.00 - 0.00 special allowance"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].rate_prior"
    value: "14.29%"
    work: "7-year property, half-year convention, year 1"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs_prior_live"
    value: "3245.69"
    work: "22,713.00 x 14.29%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].dep_2025"
    value: "1267.92"
    work: "On line 19"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_2025"
    value: "5915.20"
    work: "On line 14"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].s179_2025"
    value: "7925.00"
    work: "On line 6, column (c)"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].mq_q4"
    value: "0.00"
    work: "Not placed in service in Q4"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].mq_total"
    value: "14788.00"
    work: "mqbase for 2025 property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].cost179"
    value: "22713.00"
    work: "Business cost of 2025 property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].cost179_2025"
    value: "22713.00"
    work: "Business use is over 50%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].dep_prior"
    value: "0.00"
    work: "Not reported on line 17"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].period"
    value: "y5"
    work: "Pub. 946 asset class 36.0 has a 6-year class life; more than 4 but less than 10 gives 5-year property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].outside"
    value: "no"
    work: "Class 36.0 is ordinary 5-year GDS property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].screened"
    value: "no"
    work: "No special situation applies and the class is in scope"
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
    work: "Not listed property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].basis"
    value: "5620.00"
    work: "5,620.00 x 100%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].is2025"
    value: "yes"
    work: "Placed in service y2025"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].on_19"
    value: "yes"
    work: "2025 property that is not listed property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].on_17"
    value: "no"
    work: "Not placed in service before 2025"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].on_26_2025"
    value: "no"
    work: "Not listed property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].year"
    value: "1"
    work: "2025 - 2025 + 1"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].last"
    value: "6"
    work: "5-year property recovers over 6 tax years"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].done"
    value: "no"
    work: "Year 1 is not after year 6"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].qconv"
    value: "mq4"
    work: "Placed in service in Q4"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].s179_bad"
    value: "no"
    work: "5,620 is not more than 5,620, and business use is over 50%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].after179"
    value: "0.00"
    work: "5,620.00 - 5,620.00"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].bonus_mixed"
    value: "no"
    work: "The choice is the same for the whole class"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].bonus_full"
    value: "0.00"
    work: "0.00 x 100%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].bonus_forty"
    value: "0.00"
    work: "0.00 x 40%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].bonus_fullcase"
    value: "0.00"
    work: "Acquired after Jan 19, 2025, so 100% of 0.00"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].bonus"
    value: "0.00"
    work: "Elected out (none) for this class"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].ub"
    value: "0.00"
    work: "0.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].col19c"
    value: "0.00"
    work: "Basis after section 179 and the special allowance"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].rate_hy"
    value: "20.00%"
    work: "5-year property, half-year convention, year 1"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].rate_mq"
    value: "5.00%"
    work: "5-year property, mid-quarter Q4, year 1"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].macrs_hy"
    value: "0.00"
    work: "0.00 x 20.00%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].macrs_mq"
    value: "0.00"
    work: "0.00 x 5.00%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].macrs2025"
    value: "0.00"
    work: "Mid-quarter test is no, so half-year convention applies"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].mqbase"
    value: "0.00"
    work: "5,620.00 - 5,620.00 section 179"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].mq_q4_2025"
    value: "0.00"
    work: "Q4 property with a basis of 0.00"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].ub_prior_a"
    value: "5620.00"
    work: "5,620.00 - 0.00 prior section 179"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].ub_prior"
    value: "5620.00"
    work: "5,620.00 - 0.00 special allowance"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].rate_prior"
    value: "15.00%"
    work: "5-year property, mid-quarter Q3 (mq3), year 1"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].macrs_prior_live"
    value: "843.00"
    work: "5,620.00 x 15.00%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].dep_2025"
    value: "0.00"
    work: "On line 19"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].bonus_2025"
    value: "0.00"
    work: "No special allowance"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].s179_2025"
    value: "5620.00"
    work: "On line 6, column (c)"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].mq_q4"
    value: "0.00"
    work: "mq_q4_2025"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].mq_total"
    value: "0.00"
    work: "mqbase"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].cost179"
    value: "5620.00"
    work: "Business cost of 2025 property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].cost179_2025"
    value: "5620.00"
    work: "Business use is over 50%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].dep_prior"
    value: "0.00"
    work: "Not reported on line 17"
```
```

### classm.asset.4

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].period"
    value: "y15"
    work: "Asset class 00.4 has a class life of 22 years; 20 or more but less than 25 is 15-year property (class life recalled, not in the given text)"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].outside"
    value: "no"
    work: "Class 00.4 is a GDS MACRS class handled by this computation"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].screened"
    value: "no"
    work: "Filer answered no to the screening question"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].pct_c"
    value: "100.00"
    work: "Business use 100%, recorded as 100.00"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].pct_bad"
    value: "no"
    work: "100 is not more than 100"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].over_half"
    value: "yes"
    work: "100% > 50%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].listed_low"
    value: "no"
    work: "Not listed property, and the percentage is not over 100"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].basis"
    value: "100.00"
    work: "$100.00 x 100% = $100.00"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].is2025"
    value: "no"
    work: "Placed in service in 2019"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].on_19"
    value: "no"
    work: "Not placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].on_17"
    value: "yes"
    work: "Placed in service before 2025, not listed property: line 17"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].on_26_2025"
    value: "no"
    work: "Not listed property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].year"
    value: "7"
    work: "2025 - 2019 + 1 = 7"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].last"
    value: "16"
    work: "15-year recovery period with a first-year convention spans 16 tax years"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].done"
    value: "no"
    work: "Recovery year 7 is not past the last year, 16"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].qconv"
    value: "mq3"
    work: "Third quarter maps to mq3"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].s179_bad"
    value: "no"
    work: "Section 179 elected $0 is not more than cost; use is over 50%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].after179"
    value: "100.00"
    work: "$100.00 - $0.00 = $100.00"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_mixed"
    value: "no"
    work: "Filer says the choice is the same for the whole class"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_full"
    value: "0.00"
    work: "Special allowance for this class is none"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_forty"
    value: "0.00"
    work: "Special allowance for this class is none"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_fullcase"
    value: "0.00"
    work: "No allowance claimed (none)"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].ub"
    value: "100.00"
    work: "$100.00 - $0.00 section 179 - $0.00 allowance = $100.00"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].rate_hy"
    value: "5.00%"
    work: "15-year 150DB HY, year 1: 10% x 0.5 = 5.00%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].rate_mq"
    value: "3.75%"
    work: "15-year 150DB MQ, 3rd quarter, year 1: 10% x 0.375 = 3.75%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs_hy"
    value: "5.00"
    work: "$100.00 x 5.00% = $5.00"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs_mq"
    value: "3.75"
    work: "$100.00 x 3.75% = $3.75"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].mqbase"
    value: "100.00"
    work: "Basis after section 179, before the special allowance = $100.00"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].mq_q4_2025"
    value: "0.00"
    work: "Not placed in service in October to December 2025"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].ub_prior_a"
    value: "100.00"
    work: "$100.00 - $0.00 section 179 = $100.00"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].ub_prior"
    value: "0.00"
    work: "$100.00 - $100.00 special allowance claimed = $0.00"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].rate_prior"
    value: "5.90%"
    work: "15-year MQ Q3, year 7: switch to straight line; unrecovered 56.83% / 9.625 years remaining = 5.90%"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs_prior_live"
    value: "0.00"
    work: "$0.00 x 5.90% = $0.00"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs_prior"
    value: "0.00"
    work: "Recovery period not ended; use $0.00"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].dep_2025"
    value: "0.00"
    work: "Not 2025 property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus_2025"
    value: "0.00"
    work: "Not 2025 property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].s179_2025"
    value: "0.00"
    work: "Not 2025 property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].mq_q4"
    value: "0.00"
    work: "Not 2025 property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].mq_total"
    value: "0.00"
    work: "Not 2025 property"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].cost179"
    value: "0.00"
    work: "Not placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].cost179_2025"
    value: "0.00"
    work: "Not placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].dep_prior"
    value: "0.00"
    work: "Line 17 amount = macrs_prior = $0.00"
```
```
