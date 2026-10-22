# Class M hand-work — scveh

`Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-21 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| subject sha256 | 5b6187c11081f200dec0dba9db43047edab438841af52ee92553fb9ae48af033 |
| cases | 6 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sc | 2025 | 6, 7, 8, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 6, 7, 8, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| i4562 | 2025 | 4, 5, 6, 7, 9, 10, 11, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 5, 6, 7, 9, 10, 11, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |
| p946 | For use in preparing 2025 returns | 34, 37, 41, 59, 61, 62, 63 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 34, 37, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

## Lines

### case classm.scveh.1 — prompt sha256 53d4f1ee3e164993c8f06bd31e0be4c358604f76887c942bc85e0131dd6a2a31; branches: scveh.owned:false, scveh.owned:true, scveh.no_miles:false, scveh.over_half:true, scveh.smr_ok:true, scveh.smr_bad:false, scveh.line9#1, scveh.is_actual_owned:false, scveh.is_actual_owned:true, scveh.is_actual_leased:false, scveh.is_actual_leased:true, scveh.line20a#0, scveh.line20a#1, scveh.low_use:false, scveh.screen:false, scveh.screened:false, scveh.passenger:false, scveh.passenger:true, scveh.suv:false, scveh.is2025:false, scveh.is2025:true, scveh.is2019:false, scveh.is2019:true, scveh.s179_bad:false, scveh.after_jan19:false, scveh.after_jan19:true, scveh.bonus_same:true, scveh.bonus_mixed:false, scveh.claims_bonus:false, scveh.claims_bonus:true, scveh.lim_2025#0, scveh.lim_2025#1, scveh.line7#0, scveh.line7#1, scveh.line10#0, scveh.line10#1, scveh.line10_2025#0, scveh.line10_2025#1, scveh.s179_line10:left, scveh.line11:positive, scveh.line14#0, scveh.line14#1, scveh.line15:positive, scveh.bonus_fullcase#0, scveh.bonus_fullcase#1, scveh.bonus_2025#1, scveh.bonus_2025#2, scveh.line16#0, scveh.line16#1, scveh.bonus_allowed:left, scveh.line17:positive, scveh.line18:positive, scveh.line19#0, scveh.line19#1, scveh.line19_earlier#0, scveh.line19_earlier#1, scveh.line19_2025#1, scveh.line20:left, scveh.line20:right, scveh.b100:positive, scveh.d1:right, scveh.d2:left, scveh.d2:right, scveh.d3:left, scveh.d3:right, scveh.d4:left, scveh.d4:right, scveh.d5:left, scveh.d5:right, scveh.d6:right, scveh.unrecovered:positive, scveh.post_amount:right, scveh.too_old:false, scveh.bonus_v#0, scveh.bonus_v#1, scveh.macrs_pass#0, scveh.macrs_pass#1, scveh.macrs_heavy#0, scveh.macrs_heavy#1, scveh.macrs_v#0, scveh.macrs_v#1, scveh.bonus#0, scveh.bonus#1, scveh.macrs#0, scveh.macrs#1, scveh.s179_2025#0, scveh.s179_2025#1, scveh.mq_q4#0, scveh.mq_q4#1, scveh.mq_total#0, scveh.mq_total#1, scveh.cost179#0, scveh.cost179#1, scveh.q4_basis#0, scveh.q4_basis#3, scveh.mq_q4_o#0, scveh.mq_q4_o#1, scveh.mq_total_o#0, scveh.mq_total_o#1, scveh.cost179_o#0, scveh.cost179_o#1

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].bm_c — Business miles, as cents
Status: **DISAGREE**

Project: $233.98
Model: $23,398.00
Work: Business miles 23,398

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].cm_c — Commuting miles, as cents
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].om_c — Other miles, as cents
Status: **DISAGREE**

Project: $9.21
Model: $921.00
Work: Other miles 921

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].nonbusiness_c — Commuting and other miles, as cents
Status: **DISAGREE**

Project: $9.21
Model: $921.00
Work: 0 + 921

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].total_c — Total miles, as cents
Status: **DISAGREE**

Project: $243.19
Model: $24,319.00
Work: 23,398 + 921

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].no_miles — Actual expenses claimed for a vehicle with no miles
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].smr_bad — The standard mileage rate is not available for this vehicle
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].smr_amount — Business miles times the standard mileage rate
Status: **AGREE**

Value: $16,378.60

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line9_standard — Standard mileage amount plus parking fees and tolls
Status: **AGREE**

Value: $16,378.60

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].operating_business — The business portion of the operating expenses
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line9_actual — Business portion of the operating expenses plus parking fees and tolls
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].is_actual_owned — Owned and on actual expenses
Status: **AGREE**

Value: yes

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].is_actual_leased — Leased and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].lease_business — The business portion of the lease payments
Status: **AGREE**

Value: $5,538.97

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].low_use — Business use is 50% or less
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].screened — This vehicle's depreciation is outside this tool
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].year — Year of recovery in 2025
Status: **AGREE**

Value: 1

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].is2025 — Placed in service in 2025
Status: **AGREE**

Value: yes

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].is2019 — Placed in service in 2019 (2025 is after the recovery period)
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].bus_cost — Business/investment cost (cost times business use)
Status: **DISAGREE**

Project: $47,144.27
Model: $47,144.29
Work: 49,000 x 23,398 / 24,319 (line 13)

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].s179_bad — The section 179 election is more than the business cost, or than the SUV limit
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_mixed — The special allowance choice differs within the 5-year class
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].claims_bonus — A special allowance is claimed
Status: **AGREE**

Value: yes

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].lim_first_bonus — First-year limit with the special allowance
Status: **AGREE**

Value: $20,200.00

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].lim_first_none — First-year limit without the special allowance
Status: **AGREE**

Value: $12,200.00

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].lim_2025 — Limit for a 2025 vehicle
Status: **AGREE**

Value: $20,200.00

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].lim_prior — Limit for the vehicle's 2025 year of recovery
Status: **DISAGREE**

Project: $20,200.00
Model: $12,200.00
Work: Table 2 row for 2025, year 1 = $12,200

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. For a 2025 vehicle line 7 reads lim_2025 (agreeing), not lim_prior; lim_prior is the table's year-1 cell with the special allowance, $20,200 (Pub. 946 p. 59). Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **AGREE**

Value: $20,200.00

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **AGREE**

Value: $19,434.99

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_ok — Section 179 elected for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line10_2025 — Section 179 for a 2025 vehicle: not more than line 9 for a passenger automobile
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].s179_line10 — The section 179 election, not more than line 9
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line11 — Subtract line 10 from line 9
Status: **AGREE**

Value: $19,434.99

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **DISAGREE**

Project: $47,144.27
Model: $47,144.29
Work: 47,144.29 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_full — 100% special allowance
Status: **DISAGREE**

Project: $47,144.27
Model: $47,144.29
Work: 100% x 47,144.29

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_forty — 40% special allowance
Status: **DISAGREE**

Project: $18,857.71
Model: $18,857.72
Work: 40% x 47,144.29

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **DISAGREE**

Project: $47,144.27
Model: $47,144.29
Work: Acquired after Jan 19, 2025, so 100%

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_2025 — Special allowance for a 2025 vehicle
Status: **DISAGREE**

Project: $18,857.71
Model: $18,857.72
Work: Filer elected 40%

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line16 — Special depreciation allowance
Status: **DISAGREE**

Project: $18,857.71
Model: $18,857.72
Work: Special allowance for a 2025 vehicle

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **DISAGREE**

Project: $18,857.71
Model: $18,857.72
Work: Smaller of 18,857.72 or 19,434.99

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **DISAGREE**

Project: $577.28
Model: $577.27
Work: 19,434.99 - 18,857.72

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line18 — Basis for depreciation (line 15 less line 16)
Status: **DISAGREE**

Project: $28,286.56
Model: $28,286.57
Work: 47,144.29 - 18,857.72

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq4

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].rate_hy — MACRS rate, half-year convention
Status: **AGREE**

Value: 20%

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].rate_mq — MACRS rate, mid-quarter convention
Status: **AGREE**

Value: 5%

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].rate_prior — MACRS rate for the 2025 year of recovery
Status: **AGREE**

Value: 5%

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line19_hy — Line 18 times the half-year rate
Status: **AGREE**

Value: $5,657.31

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line19_mq — Line 18 times the mid-quarter rate
Status: **AGREE**

Value: $1,414.33

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line19_prior — Line 18 times the rate for the 2025 year of recovery
Status: **AGREE**

Value: $1,414.33

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $1,414.33

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line19_earlier — Line 19 for a vehicle placed in service before 2025 (zero after the recovery per
Status: **DISAGREE**

Project: $1,414.33
Model: $0.00
Work: Not placed in service before 2025

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. For a 2025 vehicle line 19 is line19_2025 (agreeing). Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line19_2025 — Line 19 for a 2025 vehicle, half-year or mid-quarter
Status: **AGREE**

Value: $1,414.33

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **DISAGREE**

Project: $577.28
Model: $577.27
Work: Lesser of 577.27 or 1,414.33

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].b100 — Cost less the section 179 deduction (as if used 100% for business)
Status: **AGREE**

Value: $49,000.00

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].r1 — MACRS rate for year 1
Status: **AGREE**

Value: 5%

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].t1 — Year 1 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $2,450.00

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].l1 — Year 1 limit (no special allowance)
Status: **AGREE**

Value: $12,200.00

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].t1s — Year 1 section 179 deduction plus MACRS amount
Status: **AGREE**

Value: $2,450.00

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].d1 — Year 1 deduction allowable at 100% business use (the lesser of the limit or the 
Status: **AGREE**

Value: $2,450.00

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].r2 — MACRS rate for year 2
Status: **AGREE**

Value: 38%

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].t2 — Year 2 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $18,620.00

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].r3 — MACRS rate for year 3
Status: **AGREE**

Value: 22.8%

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].t3 — Year 3 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $11,172.00

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].r4 — MACRS rate for year 4
Status: **AGREE**

Value: 13.68%

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].t4 — Year 4 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $6,703.20

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].r5 — MACRS rate for year 5
Status: **AGREE**

Value: 10.94%

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].t5 — Year 5 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $5,360.60

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].r6 — MACRS rate for year 6
Status: **AGREE**

Value: 9.58%

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].t6 — Year 6 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $4,694.20

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].too_old — Placed in service before 2019
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_v — Special allowance for this vehicle (line 25)
Status: **DISAGREE**

Project: $18,857.71
Model: $18,857.72
Work: Allowed special allowance

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_pass — Column (h) for a passenger automobile
Status: **DISAGREE**

Project: $577.28
Model: $577.27
Work: Line 20

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_heavy — Column (h) for a vehicle not subject to the limits
Status: **AGREE**

Value: $1,414.33

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_v — Column (h)
Status: **DISAGREE**

Project: $577.28
Model: $577.27
Work: Subject to the passenger automobile limits

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].bonus — Line 25: special allowance of this vehicle
Status: **DISAGREE**

Project: $18,857.71
Model: $18,857.72
Work: Owned, actual expenses

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].macrs — Column (h): depreciation of this vehicle
Status: **DISAGREE**

Project: $577.28
Model: $577.27
Work: Owned, actual expenses

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].s179_2025 — Column (i): elected section 179 cost of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **DISAGREE**

Project: $47,144.27
Model: $47,144.29
Work: Q4 2025 business basis less 0 section 179

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **DISAGREE**

Project: $47,144.27
Model: $47,144.29
Work: 2025 business basis

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **DISAGREE**

Project: $47,144.27
Model: $47,144.29
Work: Business cost of listed property placed in service 2025

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_o — Special allowance (owned, actual expenses)
Status: **DISAGREE**

Project: $18,857.71
Model: $18,857.72
Work: Owned, actual expenses

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_o — Depreciation (owned, actual expenses)
Status: **DISAGREE**

Project: $577.28
Model: $577.27
Work: Owned, actual expenses

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_o — Section 179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].q4_basis — Basis for the mid-quarter test when placed in service October to December
Status: **DISAGREE**

Project: $47,144.27
Model: $47,144.29
Work: Placed in service in Q4

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_o — mq_q4 (owned, actual expenses)
Status: **DISAGREE**

Project: $47,144.27
Model: $47,144.29
Work: Owned, actual expenses

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_a2 — mq_q4 of a 2025 vehicle
Status: **DISAGREE**

Project: $47,144.27
Model: $47,144.29
Work: 2025 vehicle

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].mq_total_o — mq_total (owned, actual expenses)
Status: **DISAGREE**

Project: $47,144.27
Model: $47,144.29
Work: Owned, actual expenses

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].mq_total_a2 — mq_total of a 2025 vehicle
Status: **DISAGREE**

Project: $47,144.27
Model: $47,144.29
Work: 2025 vehicle

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].cost179_o — cost179 (owned, actual expenses)
Status: **DISAGREE**

Project: $47,144.27
Model: $47,144.29
Work: Owned, actual expenses

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].cost179_a2 — cost179 of a 2025 vehicle
Status: **DISAGREE**

Project: $47,144.27
Model: $47,144.29
Work: 2025 vehicle

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].bm_c — Business miles, as cents
Status: **DISAGREE**

Project: $123.06
Model: $12,306.00
Work: Business miles 12,306

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].cm_c — Commuting miles, as cents
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].om_c — Other miles, as cents
Status: **DISAGREE**

Project: $79.64
Model: $7,964.00
Work: Other miles 7,964

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].nonbusiness_c — Commuting and other miles, as cents
Status: **DISAGREE**

Project: $79.64
Model: $7,964.00
Work: 0 + 7,964

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].total_c — Total miles, as cents
Status: **DISAGREE**

Project: $202.70
Model: $20,270.00
Work: 12,306 + 7,964

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].no_miles — Actual expenses claimed for a vehicle with no miles
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].smr_bad — The standard mileage rate is not available for this vehicle
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].smr_amount — Business miles times the standard mileage rate
Status: **AGREE**

Value: $8,614.20

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line9_standard — Standard mileage amount plus parking fees and tolls
Status: **AGREE**

Value: $9,614.20

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].operating_business — The business portion of the operating expenses
Status: **AGREE**

Value: $6,071.04

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line9_actual — Business portion of the operating expenses plus parking fees and tolls
Status: **AGREE**

Value: $7,071.04

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $7,071.04

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].is_actual_owned — Owned and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].is_actual_leased — Leased and on actual expenses
Status: **AGREE**

Value: yes

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].lease_business — The business portion of the lease payments
Status: **AGREE**

Value: $1,761.21

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $1,761.21

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].low_use — Business use is 50% or less
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].screened — This vehicle's depreciation is outside this tool
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].year — Year of recovery in 2025
Status: **AGREE**

Value: 7

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].is2025 — Placed in service in 2025
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].is2019 — Placed in service in 2019 (2025 is after the recovery period)
Status: **AGREE**

Value: yes

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].bus_cost — Business/investment cost (cost times business use)
Status: **DISAGREE**

Project: $6,673.89
Model: $6,673.90
Work: 10,993 x 12,306 / 20,270

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].s179_bad — The section 179 election is more than the business cost, or than the SUV limit
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_mixed — The special allowance choice differs within the 5-year class
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].claims_bonus — A special allowance is claimed
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].lim_first_bonus — First-year limit with the special allowance
Status: **DISAGREE**

Project: $5,760.00
Model: $20,200.00
Work: Table 2 footnote

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Here the vehicle's key gives the project's value: line 7 reads lim_2025 only for a 2025 vehicle and lim_prior otherwise, and the project looks every limit up by the year actually placed in service and its year of recovery; the model read the 2025 column. Pub. 946 p. 59 table, checked: 1st year 2025 $20,200 (footnote 1: $12,200 without the special allowance), 2nd year 2024 $19,800, 4th and later year 2021 $5,860, 2020 and 2019 $5,760, footnote 6 (2019 without the special allowance) $10,100; the project's tables carry these values. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].lim_first_none — First-year limit without the special allowance
Status: **DISAGREE**

Project: $10,100.00
Model: $12,200.00
Work: Table 2: 2025, year 1

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Here the vehicle's key gives the project's value: line 7 reads lim_2025 only for a 2025 vehicle and lim_prior otherwise, and the project looks every limit up by the year actually placed in service and its year of recovery; the model read the 2025 column. Pub. 946 p. 59 table, checked: 1st year 2025 $20,200 (footnote 1: $12,200 without the special allowance), 2nd year 2024 $19,800, 4th and later year 2021 $5,860, 2020 and 2019 $5,760, footnote 6 (2019 without the special allowance) $10,100; the project's tables carry these values. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].lim_2025 — Limit for a 2025 vehicle
Status: **DISAGREE**

Project: $10,100.00
Model: $12,200.00
Work: No special allowance claimed

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Here the vehicle's key gives the project's value: line 7 reads lim_2025 only for a 2025 vehicle and lim_prior otherwise, and the project looks every limit up by the year actually placed in service and its year of recovery; the model read the 2025 column. Pub. 946 p. 59 table, checked: 1st year 2025 $20,200 (footnote 1: $12,200 without the special allowance), 2nd year 2024 $19,800, 4th and later year 2021 $5,860, 2020 and 2019 $5,760, footnote 6 (2019 without the special allowance) $10,100; the project's tables carry these values. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].lim_prior — Limit for the vehicle's 2025 year of recovery
Status: **AGREE**

Value: $5,760.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **AGREE**

Value: $5,760.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **AGREE**

Value: $3,496.92

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].s179_2025_ok — Section 179 elected for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line10_2025 — Section 179 for a 2025 vehicle: not more than line 9 for a passenger automobile
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].s179_line10 — The section 179 election, not more than line 9
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line11 — Subtract line 10 from line 9
Status: **AGREE**

Value: $3,496.92

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **DISAGREE**

Project: $6,673.89
Model: $6,673.90
Work: 6,673.90 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_full — 100% special allowance
Status: **DISAGREE**

Project: $6,673.89
Model: $6,673.90
Work: 100% x 6,673.90

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_forty — 40% special allowance
Status: **AGREE**

Value: $2,669.56

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **DISAGREE**

Project: $6,673.89
Model: $6,673.90
Work: Marked acquired after Jan 19, 2025

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_2025 — Special allowance for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line16 — Special depreciation allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **AGREE**

Value: $3,496.92

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line18 — Basis for depreciation (line 15 less line 16)
Status: **DISAGREE**

Project: $6,673.89
Model: $6,673.90
Work: 6,673.90 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].qconv — Mid-quarter convention for that quarter
Status: **DISAGREE**

Project: mq1
Model: mq4
Work: Convention used is mq4

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The quarter given for this entry is January to March, so the table gives mq1; the model copied the prior-year convention (mq4). The vehicle was placed in service in 2019 and is leased, so no 2025 mid-quarter rate is read. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line19_earlier — Line 19 for a vehicle placed in service before 2025 (zero after the recovery per
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].b100 — Cost less the section 179 deduction (as if used 100% for business)
Status: **AGREE**

Value: $10,993.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].r1 — MACRS rate for year 1
Status: **AGREE**

Value: 5%

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].t1 — Year 1 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $549.65

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].l1 — Year 1 limit (no special allowance)
Status: **AGREE**

Value: $10,100.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].t1s — Year 1 section 179 deduction plus MACRS amount
Status: **AGREE**

Value: $549.65

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].d1 — Year 1 deduction allowable at 100% business use (the lesser of the limit or the 
Status: **AGREE**

Value: $549.65

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].r2 — MACRS rate for year 2
Status: **AGREE**

Value: 38%

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].t2 — Year 2 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $4,177.34

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].l2 — Year 2 limit
Status: **AGREE**

Value: $16,100.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].d2 — Year 2 deduction allowable at 100% business use
Status: **AGREE**

Value: $4,177.34

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].r3 — MACRS rate for year 3
Status: **AGREE**

Value: 22.8%

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].t3 — Year 3 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $2,506.40

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].l3 — Year 3 limit
Status: **AGREE**

Value: $9,700.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].d3 — Year 3 deduction allowable at 100% business use
Status: **AGREE**

Value: $2,506.40

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].r4 — MACRS rate for year 4
Status: **AGREE**

Value: 13.68%

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].t4 — Year 4 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $1,503.84

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].l4 — Year 4 limit
Status: **AGREE**

Value: $5,760.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].d4 — Year 4 deduction allowable at 100% business use
Status: **AGREE**

Value: $1,503.84

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].r5 — MACRS rate for year 5
Status: **AGREE**

Value: 10.94%

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].t5 — Year 5 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $1,202.63

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].l5 — Year 5 limit
Status: **AGREE**

Value: $5,760.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].d5 — Year 5 deduction allowable at 100% business use
Status: **AGREE**

Value: $1,202.63

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].r6 — MACRS rate for year 6
Status: **AGREE**

Value: 9.58%

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].t6 — Year 6 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $1,053.13

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].l6 — Year 6 limit
Status: **AGREE**

Value: $5,760.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].d6 — Year 6 deduction allowable at 100% business use
Status: **AGREE**

Value: $1,053.13

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].d_total — Deductions allowable during the recovery period at 100% business use
Status: **AGREE**

Value: $10,992.99

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].unrecovered — Unrecovered basis at the end of the recovery period
Status: **AGREE**

Value: $0.01

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].post_amount — The lesser of the limit or the unrecovered basis
Status: **AGREE**

Value: $0.01

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].post — 2025 deduction after the recovery period (times the business use percentage)
Status: **AGREE**

Value: $0.01

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].too_old — Placed in service before 2019
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_v — Special allowance for this vehicle (line 25)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].macrs_pass — Column (h) for a passenger automobile
Status: **AGREE**

Value: $0.01

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].macrs_heavy — Column (h) for a vehicle not subject to the limits
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].macrs_v — Column (h)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].bonus — Line 25: special allowance of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].macrs — Column (h): depreciation of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].s179_2025 — Column (i): elected section 179 cost of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_o — Special allowance (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].macrs_o — Depreciation (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].s179_2025_o — Section 179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].q4_basis — Basis for the mid-quarter test when placed in service October to December
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].mq_q4_o — mq_q4 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].mq_q4_a2 — mq_q4 of a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].mq_total_o — mq_total (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].mq_total_a2 — mq_total of a 2025 vehicle
Status: **DISAGREE**

Project: $6,673.89
Model: $0.00
Work: Not a 2025 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The _o line reads the _a2 copy only for a 2025 vehicle; for this earlier vehicle the _o line and the result are zero (agreeing). Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].cost179_o — cost179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].cost179_a2 — cost179 of a 2025 vehicle
Status: **DISAGREE**

Project: $6,673.89
Model: $0.00
Work: Not a 2025 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The _o line reads the _a2 copy only for a 2025 vehicle; for this earlier vehicle the _o line and the result are zero (agreeing). Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].bm_c — Business miles, as cents
Status: **DISAGREE**

Project: $299.99
Model: $29,999.00
Work: Business miles 29,999

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].cm_c — Commuting miles, as cents
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].om_c — Other miles, as cents
Status: **DISAGREE**

Project: $17.09
Model: $1,709.00
Work: Other miles 1,709

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].nonbusiness_c — Commuting and other miles, as cents
Status: **DISAGREE**

Project: $17.09
Model: $1,709.00
Work: 0 + 1,709

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].total_c — Total miles, as cents
Status: **DISAGREE**

Project: $317.08
Model: $31,708.00
Work: 29,999 + 1,709

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].no_miles — Actual expenses claimed for a vehicle with no miles
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].smr_bad — The standard mileage rate is not available for this vehicle
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].smr_amount — Business miles times the standard mileage rate
Status: **AGREE**

Value: $20,999.30

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line9_standard — Standard mileage amount plus parking fees and tolls
Status: **AGREE**

Value: $20,999.30

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].operating_business — The business portion of the operating expenses
Status: **AGREE**

Value: $673.62

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line9_actual — Business portion of the operating expenses plus parking fees and tolls
Status: **AGREE**

Value: $673.62

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $673.62

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].is_actual_owned — Owned and on actual expenses
Status: **AGREE**

Value: yes

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].is_actual_leased — Leased and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].lease_business — The business portion of the lease payments
Status: **AGREE**

Value: $6,957.63

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].low_use — Business use is 50% or less
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].screened — This vehicle's depreciation is outside this tool
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].year — Year of recovery in 2025
Status: **AGREE**

Value: 5

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].is2025 — Placed in service in 2025
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].is2019 — Placed in service in 2019 (2025 is after the recovery period)
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].bus_cost — Business/investment cost (cost times business use)
Status: **AGREE**

Value: $70,806.27

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].s179_bad — The section 179 election is more than the business cost, or than the SUV limit
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_mixed — The special allowance choice differs within the 5-year class
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].claims_bonus — A special allowance is claimed
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].lim_first_bonus — First-year limit with the special allowance
Status: **DISAGREE**

Project: $5,860.00
Model: $20,200.00
Work: Table 2 footnote

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Here the vehicle's key gives the project's value: line 7 reads lim_2025 only for a 2025 vehicle and lim_prior otherwise, and the project looks every limit up by the year actually placed in service and its year of recovery; the model read the 2025 column. Pub. 946 p. 59 table, checked: 1st year 2025 $20,200 (footnote 1: $12,200 without the special allowance), 2nd year 2024 $19,800, 4th and later year 2021 $5,860, 2020 and 2019 $5,760, footnote 6 (2019 without the special allowance) $10,100; the project's tables carry these values. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].lim_prior — Limit for the vehicle's 2025 year of recovery
Status: **AGREE**

Value: $5,860.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **AGREE**

Value: $5,860.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **AGREE**

Value: $5,544.16

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].s179_2025_ok — Section 179 elected for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line10_2025 — Section 179 for a 2025 vehicle: not more than line 9 for a passenger automobile
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].s179_line10 — The section 179 election, not more than line 9
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line11 — Subtract line 10 from line 9
Status: **AGREE**

Value: $5,544.16

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **AGREE**

Value: $70,806.27

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_full — 100% special allowance
Status: **AGREE**

Value: $70,806.27

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_forty — 40% special allowance
Status: **AGREE**

Value: $28,322.51

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **AGREE**

Value: $28,322.51

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_2025 — Special allowance for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line16 — Special depreciation allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **AGREE**

Value: $5,544.16

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line18 — Basis for depreciation (line 15 less line 16)
Status: **AGREE**

Value: $70,806.27

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq4

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].rate_hy — MACRS rate, half-year convention
Status: **AGREE**

Value: 11.52%

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].rate_mq — MACRS rate, mid-quarter convention
Status: **AGREE**

Value: 10.94%

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].rate_prior — MACRS rate for the 2025 year of recovery
Status: **AGREE**

Value: 10.94%

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line19_hy — Line 18 times the half-year rate
Status: **AGREE**

Value: $8,156.88

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line19_mq — Line 18 times the mid-quarter rate
Status: **AGREE**

Value: $7,746.21

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line19_prior — Line 18 times the rate for the 2025 year of recovery
Status: **AGREE**

Value: $7,746.21

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $7,746.21

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line19_earlier — Line 19 for a vehicle placed in service before 2025 (zero after the recovery per
Status: **AGREE**

Value: $7,746.21

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line19_2025 — Line 19 for a 2025 vehicle, half-year or mid-quarter
Status: **AGREE**

Value: $7,746.21

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

Value: $5,544.16

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].b100 — Cost less the section 179 deduction (as if used 100% for business)
Status: **AGREE**

Value: $74,840.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].r1 — MACRS rate for year 1
Status: **AGREE**

Value: 5%

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].t1 — Year 1 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $3,742.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].t1s — Year 1 section 179 deduction plus MACRS amount
Status: **AGREE**

Value: $3,742.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].r2 — MACRS rate for year 2
Status: **AGREE**

Value: 38%

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].t2 — Year 2 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $28,439.20

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].l2 — Year 2 limit
Status: **AGREE**

Value: $16,400.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].d2 — Year 2 deduction allowable at 100% business use
Status: **AGREE**

Value: $16,400.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].r3 — MACRS rate for year 3
Status: **AGREE**

Value: 22.8%

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].t3 — Year 3 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $17,063.52

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].l3 — Year 3 limit
Status: **AGREE**

Value: $9,800.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].d3 — Year 3 deduction allowable at 100% business use
Status: **AGREE**

Value: $9,800.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].r4 — MACRS rate for year 4
Status: **AGREE**

Value: 13.68%

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].t4 — Year 4 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $10,238.11

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].l4 — Year 4 limit
Status: **AGREE**

Value: $5,860.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].d4 — Year 4 deduction allowable at 100% business use
Status: **AGREE**

Value: $5,860.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].r5 — MACRS rate for year 5
Status: **AGREE**

Value: 10.94%

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].t5 — Year 5 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $8,187.50

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].l5 — Year 5 limit
Status: **AGREE**

Value: $5,860.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].d5 — Year 5 deduction allowable at 100% business use
Status: **AGREE**

Value: $5,860.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].r6 — MACRS rate for year 6
Status: **AGREE**

Value: 9.58%

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].t6 — Year 6 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $7,169.67

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].too_old — Placed in service before 2019
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_v — Special allowance for this vehicle (line 25)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].macrs_pass — Column (h) for a passenger automobile
Status: **AGREE**

Value: $5,544.16

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].macrs_heavy — Column (h) for a vehicle not subject to the limits
Status: **AGREE**

Value: $7,746.21

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].macrs_v — Column (h)
Status: **AGREE**

Value: $7,746.21

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].bonus — Line 25: special allowance of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].macrs — Column (h): depreciation of this vehicle
Status: **AGREE**

Value: $7,746.21

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].s179_2025 — Column (i): elected section 179 cost of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_o — Special allowance (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].macrs_o — Depreciation (owned, actual expenses)
Status: **AGREE**

Value: $7,746.21

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].s179_2025_o — Section 179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].q4_basis — Basis for the mid-quarter test when placed in service October to December
Status: **AGREE**

Value: $70,806.27

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].mq_q4_o — mq_q4 (owned, actual expenses)
Status: **DISAGREE**

Project: $0.00
Model: $70,806.27
Work: Owned, actual expenses

Ruling: model error; project retained. For an owned vehicle on actual expenses placed in service in 2021, the mid-quarter test basis is zero: Pub. 946 p. 34, the mid-quarter convention compares 'the total depreciable bases of MACRS property you placed in service during the last 3 months of the tax year' with 'all MACRS property you placed in service during the entire year'; a 2021 vehicle is not property placed in service in 2025. The project's mq_q4_o chooses zero when is2025 is false; the model entered the vehicle's business cost $70,806.27. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].mq_q4_a2 — mq_q4 of a 2025 vehicle
Status: **DISAGREE**

Project: $70,806.27
Model: $0.00
Work: Not a 2025 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The _o line reads the _a2 copy only for a 2025 vehicle; for this earlier vehicle the _o line and the result are zero (agreeing). Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].mq_total_o — mq_total (owned, actual expenses)
Status: **DISAGREE**

Project: $0.00
Model: $70,806.27
Work: Owned, actual expenses

Ruling: model error; project retained. The mid-quarter test's total basis counts only MACRS property placed in service during 2025 (Pub. 946 p. 34, 'all MACRS property you placed in service during the entire year'); this vehicle was placed in service in 2021, so its contribution is zero, as the project has. The model entered $70,806.27. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].mq_total_a2 — mq_total of a 2025 vehicle
Status: **DISAGREE**

Project: $70,806.27
Model: $0.00
Work: Not a 2025 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The _o line reads the _a2 copy only for a 2025 vehicle; for this earlier vehicle the _o line and the result are zero (agreeing). Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].cost179_o — cost179 (owned, actual expenses)
Status: **DISAGREE**

Project: $0.00
Model: $70,806.27
Work: Owned, actual expenses

Ruling: model error; project retained. This line feeds Form 4562 line 2, 'the total cost of all section 179 property you placed in service during the tax year' (i4562 p. 4, Line 2, including listed property from Part V); a vehicle placed in service in 2021 contributes zero, as the project has. The model entered its business cost $70,806.27. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].cost179_a2 — cost179 of a 2025 vehicle
Status: **DISAGREE**

Project: $70,806.27
Model: $0.00
Work: Not a 2025 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The _o line reads the _a2 copy only for a 2025 vehicle; for this earlier vehicle the _o line and the result are zero (agreeing). Not evidence. [dropped]

### case classm.scveh.2 — prompt sha256 7643574474f5500ccaacf9423d3e802fa4c01f495f450812897717d7dc40169b; branches: scveh.owned:true, scveh.no_miles:false, scveh.over_half:true, scveh.smr_ok:true, scveh.smr_bad:false, scveh.line9#1, scveh.is_actual_owned:true, scveh.is_actual_leased:false, scveh.line20a#1, scveh.low_use:false, scveh.screen:false, scveh.screened:false, scveh.passenger:true, scveh.suv:false, scveh.is2025:false, scveh.is2025:true, scveh.is2019:false, scveh.is2019:true, scveh.s179_bad:false, scveh.after_jan19:true, scveh.bonus_same:true, scveh.bonus_mixed:false, scveh.claims_bonus:false, scveh.claims_bonus:true, scveh.lim_2025#0, scveh.lim_2025#1, scveh.line7#0, scveh.line7#1, scveh.line10#0, scveh.line10#1, scveh.line10_2025#0, scveh.s179_line10:left, scveh.line11:positive, scveh.line14#0, scveh.line14#1, scveh.line15:positive, scveh.bonus_fullcase#0, scveh.bonus_2025#0, scveh.bonus_2025#2, scveh.line16#0, scveh.line16#1, scveh.bonus_allowed:left, scveh.bonus_allowed:right, scveh.line17:floor, scveh.line17:positive, scveh.line18:floor, scveh.line18:positive, scveh.line19#0, scveh.line19#1, scveh.line19_earlier#0, scveh.line19_earlier#1, scveh.line19_2025#0, scveh.line20:left, scveh.line20:right, scveh.b100:positive, scveh.d1:right, scveh.d2:right, scveh.d3:right, scveh.d4:right, scveh.d5:right, scveh.d6:right, scveh.unrecovered:floor, scveh.post_amount:right, scveh.too_old:false, scveh.bonus_v#0, scveh.macrs_pass#0, scveh.macrs_pass#1, scveh.macrs_heavy#0, scveh.macrs_heavy#1, scveh.macrs_v#0, scveh.bonus#0, scveh.macrs#0, scveh.s179_2025#0, scveh.mq_q4#0, scveh.mq_total#0, scveh.cost179#0, scveh.q4_basis#1, scveh.q4_basis#2, scveh.mq_q4_o#0, scveh.mq_q4_o#1, scveh.mq_total_o#0, scveh.mq_total_o#1, scveh.cost179_o#0, scveh.cost179_o#1

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].bm_c — Business miles, as cents
Status: **DISAGREE**

Project: $259.42
Model: $25,942.00
Work: Business miles 25,942

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].cm_c — Commuting miles, as cents
Status: **DISAGREE**

Project: $8.61
Model: $861.00
Work: Commuting miles 861

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].om_c — Other miles, as cents
Status: **DISAGREE**

Project: $17.90
Model: $1,790.00
Work: Other miles 1,790

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].nonbusiness_c — Commuting and other miles, as cents
Status: **DISAGREE**

Project: $26.51
Model: $2,651.00
Work: 861 + 1,790

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].total_c — Total miles, as cents
Status: **DISAGREE**

Project: $285.93
Model: $28,593.00
Work: 25,942 + 2,651

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].no_miles — Actual expenses claimed for a vehicle with no miles
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].smr_bad — The standard mileage rate is not available for this vehicle
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].smr_amount — Business miles times the standard mileage rate
Status: **AGREE**

Value: $18,159.40

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line9_standard — Standard mileage amount plus parking fees and tolls
Status: **AGREE**

Value: $18,159.40

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].operating_business — The business portion of the operating expenses
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line9_actual — Business portion of the operating expenses plus parking fees and tolls
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].is_actual_owned — Owned and on actual expenses
Status: **AGREE**

Value: yes

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].is_actual_leased — Leased and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].lease_business — The business portion of the lease payments
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].low_use — Business use is 50% or less
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].screened — This vehicle's depreciation is outside this tool
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].year — Year of recovery in 2025
Status: **AGREE**

Value: 7

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].is2025 — Placed in service in 2025
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].is2019 — Placed in service in 2019 (2025 is after the recovery period)
Status: **AGREE**

Value: yes

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].bus_cost — Business/investment cost (cost times business use)
Status: **AGREE**

Value: $14,313.33

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].s179_bad — The section 179 election is more than the business cost, or than the SUV limit
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_mixed — The special allowance choice differs within the 5-year class
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].claims_bonus — A special allowance is claimed
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].lim_first_bonus — First-year limit with the special allowance
Status: **DISAGREE**

Project: $5,760.00
Model: $20,200.00
Work: Table 2 footnote: 2025 limit with special allowance

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Here the vehicle's key gives the project's value: line 7 reads lim_2025 only for a 2025 vehicle and lim_prior otherwise, and the project looks every limit up by the year actually placed in service and its year of recovery; the model read the 2025 column. Pub. 946 p. 59 table, checked: 1st year 2025 $20,200 (footnote 1: $12,200 without the special allowance), 2nd year 2024 $19,800, 4th and later year 2021 $5,860, 2020 and 2019 $5,760, footnote 6 (2019 without the special allowance) $10,100; the project's tables carry these values. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].lim_first_none — First-year limit without the special allowance
Status: **DISAGREE**

Project: $10,100.00
Model: $12,200.00
Work: Table 2: 2025 year 1 limit

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Here the vehicle's key gives the project's value: line 7 reads lim_2025 only for a 2025 vehicle and lim_prior otherwise, and the project looks every limit up by the year actually placed in service and its year of recovery; the model read the 2025 column. Pub. 946 p. 59 table, checked: 1st year 2025 $20,200 (footnote 1: $12,200 without the special allowance), 2nd year 2024 $19,800, 4th and later year 2021 $5,860, 2020 and 2019 $5,760, footnote 6 (2019 without the special allowance) $10,100; the project's tables carry these values. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].lim_2025 — Limit for a 2025 vehicle
Status: **DISAGREE**

Project: $10,100.00
Model: $12,200.00
Work: No special allowance claimed

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Here the vehicle's key gives the project's value: line 7 reads lim_2025 only for a 2025 vehicle and lim_prior otherwise, and the project looks every limit up by the year actually placed in service and its year of recovery; the model read the 2025 column. Pub. 946 p. 59 table, checked: 1st year 2025 $20,200 (footnote 1: $12,200 without the special allowance), 2nd year 2024 $19,800, 4th and later year 2021 $5,860, 2020 and 2019 $5,760, footnote 6 (2019 without the special allowance) $10,100; the project's tables carry these values. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].lim_prior — Limit for the vehicle's 2025 year of recovery
Status: **AGREE**

Value: $5,760.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **AGREE**

Value: $5,760.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **AGREE**

Value: $5,225.96

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_ok — Section 179 elected for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line10_2025 — Section 179 for a 2025 vehicle: not more than line 9 for a passenger automobile
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].s179_line10 — The section 179 election, not more than line 9
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line11 — Subtract line 10 from line 9
Status: **AGREE**

Value: $5,225.96

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **AGREE**

Value: $14,313.33

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_full — 100% special allowance
Status: **AGREE**

Value: $14,313.33

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_forty — 40% special allowance
Status: **AGREE**

Value: $5,725.33

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **AGREE**

Value: $14,313.33

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_2025 — Special allowance for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line16 — Special depreciation allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **AGREE**

Value: $5,225.96

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line18 — Basis for depreciation (line 15 less line 16)
Status: **AGREE**

Value: $14,313.33

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq3

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line19_earlier — Line 19 for a vehicle placed in service before 2025 (zero after the recovery per
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].b100 — Cost less the section 179 deduction (as if used 100% for business)
Status: **AGREE**

Value: $15,776.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].r1 — MACRS rate for year 1
Status: **AGREE**

Value: 35%

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].t1 — Year 1 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $5,521.60

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].l1 — Year 1 limit (no special allowance)
Status: **AGREE**

Value: $10,100.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].t1s — Year 1 section 179 deduction plus MACRS amount
Status: **AGREE**

Value: $5,521.60

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].d1 — Year 1 deduction allowable at 100% business use (the lesser of the limit or the 
Status: **AGREE**

Value: $5,521.60

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].r2 — MACRS rate for year 2
Status: **AGREE**

Value: 26%

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].t2 — Year 2 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $4,101.76

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].l2 — Year 2 limit
Status: **AGREE**

Value: $16,100.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].d2 — Year 2 deduction allowable at 100% business use
Status: **AGREE**

Value: $4,101.76

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].r3 — MACRS rate for year 3
Status: **AGREE**

Value: 15.6%

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].t3 — Year 3 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $2,461.06

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].l3 — Year 3 limit
Status: **AGREE**

Value: $9,700.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].d3 — Year 3 deduction allowable at 100% business use
Status: **AGREE**

Value: $2,461.06

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].r4 — MACRS rate for year 4
Status: **AGREE**

Value: 11.01%

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].t4 — Year 4 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $1,736.94

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].l4 — Year 4 limit
Status: **AGREE**

Value: $5,760.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].d4 — Year 4 deduction allowable at 100% business use
Status: **AGREE**

Value: $1,736.94

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].r5 — MACRS rate for year 5
Status: **AGREE**

Value: 11.01%

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].t5 — Year 5 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $1,736.94

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].l5 — Year 5 limit
Status: **AGREE**

Value: $5,760.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].d5 — Year 5 deduction allowable at 100% business use
Status: **AGREE**

Value: $1,736.94

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].r6 — MACRS rate for year 6
Status: **AGREE**

Value: 1.38%

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].t6 — Year 6 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $217.71

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].l6 — Year 6 limit
Status: **AGREE**

Value: $5,760.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].d6 — Year 6 deduction allowable at 100% business use
Status: **AGREE**

Value: $217.71

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].d_total — Deductions allowable during the recovery period at 100% business use
Status: **AGREE**

Value: $15,776.01

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].unrecovered — Unrecovered basis at the end of the recovery period
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].post_amount — The lesser of the limit or the unrecovered basis
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].post — 2025 deduction after the recovery period (times the business use percentage)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].too_old — Placed in service before 2019
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_v — Special allowance for this vehicle (line 25)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_pass — Column (h) for a passenger automobile
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_heavy — Column (h) for a vehicle not subject to the limits
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_v — Column (h)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].bonus — Line 25: special allowance of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].macrs — Column (h): depreciation of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].s179_2025 — Column (i): elected section 179 cost of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_o — Special allowance (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_o — Depreciation (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_o — Section 179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].q4_basis — Basis for the mid-quarter test when placed in service October to December
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_o — mq_q4 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_a2 — mq_q4 of a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].mq_total_o — mq_total (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].mq_total_a2 — mq_total of a 2025 vehicle
Status: **AGREE**

Value: $14,313.33

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].cost179_o — cost179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].cost179_a2 — cost179 of a 2025 vehicle
Status: **AGREE**

Value: $14,313.33

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].bm_c — Business miles, as cents
Status: **DISAGREE**

Project: $124.62
Model: $12,462.00
Work: Business miles 12,462

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].cm_c — Commuting miles, as cents
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].om_c — Other miles, as cents
Status: **DISAGREE**

Project: $9.37
Model: $937.00
Work: Other miles 937

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].nonbusiness_c — Commuting and other miles, as cents
Status: **DISAGREE**

Project: $9.37
Model: $937.00
Work: 0 + 937

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].total_c — Total miles, as cents
Status: **DISAGREE**

Project: $133.99
Model: $13,399.00
Work: 12,462 + 937

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].no_miles — Actual expenses claimed for a vehicle with no miles
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].smr_bad — The standard mileage rate is not available for this vehicle
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].smr_amount — Business miles times the standard mileage rate
Status: **AGREE**

Value: $8,723.40

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line9_standard — Standard mileage amount plus parking fees and tolls
Status: **AGREE**

Value: $8,723.40

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].operating_business — The business portion of the operating expenses
Status: **AGREE**

Value: $1,506.71

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line9_actual — Business portion of the operating expenses plus parking fees and tolls
Status: **AGREE**

Value: $1,506.71

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $1,506.71

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].is_actual_owned — Owned and on actual expenses
Status: **AGREE**

Value: yes

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].is_actual_leased — Leased and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].lease_business — The business portion of the lease payments
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].low_use — Business use is 50% or less
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].screened — This vehicle's depreciation is outside this tool
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].year — Year of recovery in 2025
Status: **AGREE**

Value: 1

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].is2025 — Placed in service in 2025
Status: **AGREE**

Value: yes

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].is2019 — Placed in service in 2019 (2025 is after the recovery period)
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].bus_cost — Business/investment cost (cost times business use)
Status: **DISAGREE**

Project: $47,544.20
Model: $47,544.22
Work: 51,119 x 12,462/13,399

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].s179_bad — The section 179 election is more than the business cost, or than the SUV limit
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_mixed — The special allowance choice differs within the 5-year class
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].claims_bonus — A special allowance is claimed
Status: **AGREE**

Value: yes

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].lim_first_bonus — First-year limit with the special allowance
Status: **AGREE**

Value: $20,200.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].lim_first_none — First-year limit without the special allowance
Status: **AGREE**

Value: $12,200.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].lim_2025 — Limit for a 2025 vehicle
Status: **AGREE**

Value: $20,200.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].lim_prior — Limit for the vehicle's 2025 year of recovery
Status: **AGREE**

Value: $20,200.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **AGREE**

Value: $20,200.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **DISAGREE**

Project: $18,787.39
Model: $18,787.40
Work: 20,200 x 12,462/13,399

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].s179_2025_ok — Section 179 elected for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line10_2025 — Section 179 for a 2025 vehicle: not more than line 9 for a passenger automobile
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].s179_line10 — The section 179 election, not more than line 9
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line11 — Subtract line 10 from line 9
Status: **DISAGREE**

Project: $18,787.39
Model: $18,787.40
Work: 18,787.40 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **DISAGREE**

Project: $47,544.20
Model: $47,544.22
Work: 47,544.22 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_full — 100% special allowance
Status: **DISAGREE**

Project: $47,544.20
Model: $47,544.22
Work: 47,544.22 x 100%

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_forty — 40% special allowance
Status: **DISAGREE**

Project: $19,017.68
Model: $19,017.69
Work: 47,544.22 x 40%

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **DISAGREE**

Project: $47,544.20
Model: $47,544.22
Work: Acquired after Jan 19, 2025, so 100%

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_2025 — Special allowance for a 2025 vehicle
Status: **DISAGREE**

Project: $47,544.20
Model: $47,544.22
Work: Special allowance claimed (full)

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line16 — Special depreciation allowance
Status: **DISAGREE**

Project: $47,544.20
Model: $47,544.22
Work: Placed in service in 2025

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **DISAGREE**

Project: $18,787.39
Model: $18,787.40
Work: Smaller of 47,544.22 or line 11 of 18,787.40

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line18 — Basis for depreciation (line 15 less line 16)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq2

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].rate_hy — MACRS rate, half-year convention
Status: **AGREE**

Value: 20%

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].rate_mq — MACRS rate, mid-quarter convention
Status: **AGREE**

Value: 25%

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].rate_prior — MACRS rate for the 2025 year of recovery
Status: **AGREE**

Value: 5%

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line19_hy — Line 18 times the half-year rate
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line19_mq — Line 18 times the mid-quarter rate
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line19_prior — Line 18 times the rate for the 2025 year of recovery
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line19_earlier — Line 19 for a vehicle placed in service before 2025 (zero after the recovery per
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line19_2025 — Line 19 for a 2025 vehicle, half-year or mid-quarter
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].b100 — Cost less the section 179 deduction (as if used 100% for business)
Status: **AGREE**

Value: $51,119.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].r1 — MACRS rate for year 1
Status: **AGREE**

Value: 5%

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].t1 — Year 1 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $2,555.95

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].l1 — Year 1 limit (no special allowance)
Status: **AGREE**

Value: $12,200.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].t1s — Year 1 section 179 deduction plus MACRS amount
Status: **AGREE**

Value: $2,555.95

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].d1 — Year 1 deduction allowable at 100% business use (the lesser of the limit or the 
Status: **AGREE**

Value: $2,555.95

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].r2 — MACRS rate for year 2
Status: **AGREE**

Value: 38%

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].t2 — Year 2 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $19,425.22

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].r3 — MACRS rate for year 3
Status: **AGREE**

Value: 22.8%

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].t3 — Year 3 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $11,655.13

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].r4 — MACRS rate for year 4
Status: **AGREE**

Value: 13.68%

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].t4 — Year 4 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $6,993.08

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].r5 — MACRS rate for year 5
Status: **AGREE**

Value: 10.94%

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].t5 — Year 5 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $5,592.42

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].r6 — MACRS rate for year 6
Status: **AGREE**

Value: 9.58%

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].t6 — Year 6 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $4,897.20

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].too_old — Placed in service before 2019
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_v — Special allowance for this vehicle (line 25)
Status: **DISAGREE**

Project: $18,787.39
Model: $18,787.40
Work: bonus_allowed

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].macrs_pass — Column (h) for a passenger automobile
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].macrs_heavy — Column (h) for a vehicle not subject to the limits
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].macrs_v — Column (h)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].bonus — Line 25: special allowance of this vehicle
Status: **DISAGREE**

Project: $18,787.39
Model: $18,787.40
Work: bonus_v

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].macrs — Column (h): depreciation of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].s179_2025 — Column (i): elected section 179 cost of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **DISAGREE**

Project: $47,544.20
Model: $47,544.22
Work: Business cost - section 179 of 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **DISAGREE**

Project: $47,544.20
Model: $47,544.22
Work: Business cost of listed property

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_o — Special allowance (owned, actual expenses)
Status: **DISAGREE**

Project: $18,787.39
Model: $18,787.40
Work: Owned, actual expenses

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].macrs_o — Depreciation (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].s179_2025_o — Section 179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].q4_basis — Basis for the mid-quarter test when placed in service October to December
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].mq_q4_o — mq_q4 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].mq_q4_a2 — mq_q4 of a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].mq_total_o — mq_total (owned, actual expenses)
Status: **DISAGREE**

Project: $47,544.20
Model: $47,544.22
Work: 2025 vehicle

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].mq_total_a2 — mq_total of a 2025 vehicle
Status: **DISAGREE**

Project: $47,544.20
Model: $47,544.22
Work: 47,544.22 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].cost179_o — cost179 (owned, actual expenses)
Status: **DISAGREE**

Project: $47,544.20
Model: $47,544.22
Work: 2025 vehicle

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].cost179_a2 — cost179 of a 2025 vehicle
Status: **DISAGREE**

Project: $47,544.20
Model: $47,544.22
Work: Business cost

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### case classm.scveh.3 — prompt sha256 2d9e57d2b5f65560b5e7ce8a8874b6b64d04e5f443a314467bfbaf90f1ba01ae; branches: scveh.owned:true, scveh.no_miles:false, scveh.over_half:true, scveh.smr_ok:true, scveh.smr_bad:false, scveh.line9#0, scveh.is_actual_owned:false, scveh.is_actual_leased:false, scveh.line20a#1, scveh.low_use:false, scveh.screen:false, scveh.screened:false, scveh.passenger:true, scveh.suv:false, scveh.is2025:false, scveh.is2019:true, scveh.s179_bad:false, scveh.after_jan19:true, scveh.bonus_same:true, scveh.bonus_mixed:false, scveh.claims_bonus:false, scveh.lim_2025#1, scveh.line7#1, scveh.line10#1, scveh.line10_2025#0, scveh.s179_line10:left, scveh.line11:positive, scveh.line14#1, scveh.line15:positive, scveh.bonus_fullcase#0, scveh.bonus_2025#2, scveh.line16#1, scveh.bonus_allowed:left, scveh.line17:positive, scveh.line18:positive, scveh.line19#1, scveh.line19_earlier#1, scveh.line19_2025#0, scveh.line20:right, scveh.b100:positive, scveh.d1:left, scveh.d2:right, scveh.d3:right, scveh.d4:right, scveh.d5:right, scveh.d6:right, scveh.unrecovered:positive, scveh.post_amount:left, scveh.too_old:false, scveh.bonus_v#0, scveh.macrs_pass#1, scveh.macrs_heavy#1, scveh.macrs_v#0, scveh.bonus#1, scveh.macrs#1, scveh.s179_2025#1, scveh.mq_q4#1, scveh.mq_total#1, scveh.cost179#1, scveh.q4_basis#0, scveh.mq_q4_o#1, scveh.mq_total_o#1, scveh.cost179_o#1

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].bm_c — Business miles, as cents
Status: **DISAGREE**

Project: $266.10
Model: $26,610.00
Work: Business miles 26,610

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].cm_c — Commuting miles, as cents
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].om_c — Other miles, as cents
Status: **DISAGREE**

Project: $33.36
Model: $3,336.00
Work: Other miles 3,336

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].nonbusiness_c — Commuting and other miles, as cents
Status: **DISAGREE**

Project: $33.36
Model: $3,336.00
Work: 0 + 3,336

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].total_c — Total miles, as cents
Status: **DISAGREE**

Project: $299.46
Model: $29,946.00
Work: 26,610 + 3,336

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].no_miles — Actual expenses claimed for a vehicle with no miles
Status: **AGREE**

Value: no

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].smr_bad — The standard mileage rate is not available for this vehicle
Status: **AGREE**

Value: no

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].smr_amount — Business miles times the standard mileage rate
Status: **AGREE**

Value: $18,627.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line9_standard — Standard mileage amount plus parking fees and tolls
Status: **AGREE**

Value: $18,627.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].operating_business — The business portion of the operating expenses
Status: **AGREE**

Value: $7,129.23

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line9_actual — Business portion of the operating expenses plus parking fees and tolls
Status: **AGREE**

Value: $7,129.23

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $18,627.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].is_actual_owned — Owned and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].is_actual_leased — Leased and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].lease_business — The business portion of the lease payments
Status: **DISAGREE**

Project: $5,243.62
Model: $5,243.63
Work: 5,901 x 26,610 / 29,946

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].low_use — Business use is 50% or less
Status: **AGREE**

Value: no

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].screened — This vehicle's depreciation is outside this tool
Status: **AGREE**

Value: no

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].year — Year of recovery in 2025
Status: **AGREE**

Value: 7

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].is2025 — Placed in service in 2025
Status: **AGREE**

Value: no

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].is2019 — Placed in service in 2019 (2025 is after the recovery period)
Status: **AGREE**

Value: yes

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].bus_cost — Business/investment cost (cost times business use)
Status: **DISAGREE**

Project: $48,214.49
Model: $48,214.52
Work: Worksheet line 13: 54,259 x 26,610 / 29,946

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].s179_bad — The section 179 election is more than the business cost, or than the SUV limit
Status: **AGREE**

Value: no

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_mixed — The special allowance choice differs within the 5-year class
Status: **AGREE**

Value: no

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].claims_bonus — A special allowance is claimed
Status: **AGREE**

Value: no

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].lim_first_bonus — First-year limit with the special allowance
Status: **DISAGREE**

Project: $5,760.00
Model: $20,200.00
Work: Table 2 footnote: 2025 limit with the special allowance

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Here the vehicle's key gives the project's value: line 7 reads lim_2025 only for a 2025 vehicle and lim_prior otherwise, and the project looks every limit up by the year actually placed in service and its year of recovery; the model read the 2025 column. Pub. 946 p. 59 table, checked: 1st year 2025 $20,200 (footnote 1: $12,200 without the special allowance), 2nd year 2024 $19,800, 4th and later year 2021 $5,860, 2020 and 2019 $5,760, footnote 6 (2019 without the special allowance) $10,100; the project's tables carry these values. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].lim_first_none — First-year limit without the special allowance
Status: **DISAGREE**

Project: $10,100.00
Model: $12,200.00
Work: Table 2: 2025, year 1

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Here the vehicle's key gives the project's value: line 7 reads lim_2025 only for a 2025 vehicle and lim_prior otherwise, and the project looks every limit up by the year actually placed in service and its year of recovery; the model read the 2025 column. Pub. 946 p. 59 table, checked: 1st year 2025 $20,200 (footnote 1: $12,200 without the special allowance), 2nd year 2024 $19,800, 4th and later year 2021 $5,860, 2020 and 2019 $5,760, footnote 6 (2019 without the special allowance) $10,100; the project's tables carry these values. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].lim_2025 — Limit for a 2025 vehicle
Status: **DISAGREE**

Project: $10,100.00
Model: $12,200.00
Work: No special allowance claimed

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Here the vehicle's key gives the project's value: line 7 reads lim_2025 only for a 2025 vehicle and lim_prior otherwise, and the project looks every limit up by the year actually placed in service and its year of recovery; the model read the 2025 column. Pub. 946 p. 59 table, checked: 1st year 2025 $20,200 (footnote 1: $12,200 without the special allowance), 2nd year 2024 $19,800, 4th and later year 2021 $5,860, 2020 and 2019 $5,760, footnote 6 (2019 without the special allowance) $10,100; the project's tables carry these values. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].lim_prior — Limit for the vehicle's 2025 year of recovery
Status: **AGREE**

Value: $5,760.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **AGREE**

Value: $5,760.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **AGREE**

Value: $5,118.33

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_ok — Section 179 elected for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line10_2025 — Section 179 for a 2025 vehicle: not more than line 9 for a passenger automobile
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].s179_line10 — The section 179 election, not more than line 9
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line11 — Subtract line 10 from line 9
Status: **AGREE**

Value: $5,118.33

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $9,850.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **DISAGREE**

Project: $38,364.49
Model: $38,364.52
Work: 48,214.52 - 9,850

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_full — 100% special allowance
Status: **DISAGREE**

Project: $38,364.49
Model: $38,364.52
Work: 38,364.52 x 100%

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_forty — 40% special allowance
Status: **DISAGREE**

Project: $15,345.80
Model: $15,345.81
Work: 38,364.52 x 40%

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **DISAGREE**

Project: $38,364.49
Model: $38,364.52
Work: Acquired after January 19, 2025 = yes, so 100%

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_2025 — Special allowance for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line16 — Special depreciation allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **AGREE**

Value: $5,118.33

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line18 — Basis for depreciation (line 15 less line 16)
Status: **DISAGREE**

Project: $38,364.49
Model: $38,364.52
Work: 38,364.52 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq1

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line19_earlier — Line 19 for a vehicle placed in service before 2025 (zero after the recovery per
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].b100 — Cost less the section 179 deduction (as if used 100% for business)
Status: **AGREE**

Value: $44,409.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].r1 — MACRS rate for year 1
Status: **AGREE**

Value: 20%

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].t1 — Year 1 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $8,881.80

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].l1 — Year 1 limit (no special allowance)
Status: **AGREE**

Value: $10,100.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].t1s — Year 1 section 179 deduction plus MACRS amount
Status: **AGREE**

Value: $18,731.80

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].d1 — Year 1 deduction allowable at 100% business use (the lesser of the limit or the 
Status: **AGREE**

Value: $10,100.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].r2 — MACRS rate for year 2
Status: **AGREE**

Value: 32%

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].t2 — Year 2 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $14,210.88

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].l2 — Year 2 limit
Status: **AGREE**

Value: $16,100.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].d2 — Year 2 deduction allowable at 100% business use
Status: **AGREE**

Value: $14,210.88

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].r3 — MACRS rate for year 3
Status: **AGREE**

Value: 19.2%

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].t3 — Year 3 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $8,526.53

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].l3 — Year 3 limit
Status: **AGREE**

Value: $9,700.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].d3 — Year 3 deduction allowable at 100% business use
Status: **AGREE**

Value: $8,526.53

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].r4 — MACRS rate for year 4
Status: **AGREE**

Value: 11.52%

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].t4 — Year 4 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $5,115.92

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].l4 — Year 4 limit
Status: **AGREE**

Value: $5,760.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].d4 — Year 4 deduction allowable at 100% business use
Status: **AGREE**

Value: $5,115.92

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].r5 — MACRS rate for year 5
Status: **AGREE**

Value: 11.52%

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].t5 — Year 5 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $5,115.92

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].l5 — Year 5 limit
Status: **AGREE**

Value: $5,760.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].d5 — Year 5 deduction allowable at 100% business use
Status: **AGREE**

Value: $5,115.92

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].r6 — MACRS rate for year 6
Status: **AGREE**

Value: 5.76%

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].t6 — Year 6 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $2,557.96

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].l6 — Year 6 limit
Status: **AGREE**

Value: $5,760.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].d6 — Year 6 deduction allowable at 100% business use
Status: **AGREE**

Value: $2,557.96

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].d_total — Deductions allowable during the recovery period at 100% business use
Status: **AGREE**

Value: $45,627.21

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].unrecovered — Unrecovered basis at the end of the recovery period
Status: **AGREE**

Value: $8,631.79

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].post_amount — The lesser of the limit or the unrecovered basis
Status: **AGREE**

Value: $5,760.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].post — 2025 deduction after the recovery period (times the business use percentage)
Status: **AGREE**

Value: $5,118.33

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].too_old — Placed in service before 2019
Status: **AGREE**

Value: no

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_v — Special allowance for this vehicle (line 25)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_pass — Column (h) for a passenger automobile
Status: **AGREE**

Value: $5,118.33

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_heavy — Column (h) for a vehicle not subject to the limits
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_v — Column (h)
Status: **AGREE**

Value: $5,118.33

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].bonus — Line 25: special allowance of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].macrs — Column (h): depreciation of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].s179_2025 — Column (i): elected section 179 cost of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_o — Special allowance (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_o — Depreciation (owned, actual expenses)
Status: **DISAGREE**

Project: $5,118.33
Model: $0.00
Work: Not owned on actual expenses

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. macrs reads macrs_o only for an owned vehicle on actual expenses; this one is leased or on the standard mileage rate, so macrs is zero (agreeing). Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_o — Section 179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].q4_basis — Basis for the mid-quarter test when placed in service October to December
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_o — mq_q4 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_a2 — mq_q4 of a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].mq_total_o — mq_total (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].mq_total_a2 — mq_total of a 2025 vehicle
Status: **DISAGREE**

Project: $38,364.49
Model: $0.00
Work: Not a 2025 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The _o line reads the _a2 copy only for a 2025 vehicle; for this earlier vehicle the _o line and the result are zero (agreeing). Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].cost179_o — cost179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].cost179_a2 — cost179 of a 2025 vehicle
Status: **DISAGREE**

Project: $48,214.49
Model: $0.00
Work: Not a 2025 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The _o line reads the _a2 copy only for a 2025 vehicle; for this earlier vehicle the _o line and the result are zero (agreeing). Not evidence. [dropped]

### case classm.scveh.4 — prompt sha256 8fd2ac6866e1bff68dc356bba8206e9049cd817bbc65095af50e22918dc0fa6d; branches: scveh.owned:true, scveh.no_miles:false, scveh.over_half:true, scveh.smr_ok:true, scveh.smr_bad:false, scveh.line9#1, scveh.is_actual_owned:true, scveh.is_actual_leased:false, scveh.line20a#1, scveh.low_use:false, scveh.screen:false, scveh.screened:false, scveh.passenger:true, scveh.suv:false, scveh.is2025:false, scveh.is2019:false, scveh.s179_bad:false, scveh.after_jan19:true, scveh.bonus_same:true, scveh.bonus_mixed:false, scveh.claims_bonus:false, scveh.lim_2025#1, scveh.line7#1, scveh.line10#1, scveh.line10_2025#0, scveh.s179_line10:left, scveh.line11:positive, scveh.line14#1, scveh.line15:floor, scveh.bonus_fullcase#0, scveh.bonus_2025#2, scveh.line16#1, scveh.bonus_allowed:left, scveh.line17:positive, scveh.line18:floor, scveh.line19#1, scveh.line19_earlier#0, scveh.line19_2025#1, scveh.line20:right, scveh.b100:floor, scveh.d2:right, scveh.too_old:false, scveh.bonus_v#0, scveh.macrs_pass#0, scveh.macrs_heavy#0, scveh.macrs_v#0, scveh.bonus#0, scveh.macrs#0, scveh.s179_2025#0, scveh.mq_q4#0, scveh.mq_total#0, scveh.cost179#0, scveh.q4_basis#3, scveh.mq_q4_o#1, scveh.mq_total_o#1, scveh.cost179_o#1

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].bm_c — Business miles, as cents
Status: **DISAGREE**

Project: $298.86
Model: $29,886.00
Work: Business miles 29,886

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].cm_c — Commuting miles, as cents
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].om_c — Other miles, as cents
Status: **DISAGREE**

Project: $3.91
Model: $391.00
Work: Other miles 391

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].nonbusiness_c — Commuting and other miles, as cents
Status: **DISAGREE**

Project: $3.91
Model: $391.00
Work: 0 + 391

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].total_c — Total miles, as cents
Status: **DISAGREE**

Project: $302.77
Model: $30,277.00
Work: 29,886 + 391

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].no_miles — Actual expenses claimed for a vehicle with no miles
Status: **AGREE**

Value: no

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].smr_bad — The standard mileage rate is not available for this vehicle
Status: **AGREE**

Value: no

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].smr_amount — Business miles times the standard mileage rate
Status: **AGREE**

Value: $20,920.20

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line9_standard — Standard mileage amount plus parking fees and tolls
Status: **AGREE**

Value: $20,920.20

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].operating_business — The business portion of the operating expenses
Status: **AGREE**

Value: $9,706.02

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line9_actual — Business portion of the operating expenses plus parking fees and tolls
Status: **AGREE**

Value: $9,706.02

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $9,706.02

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].is_actual_owned — Owned and on actual expenses
Status: **AGREE**

Value: yes

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].is_actual_leased — Leased and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].lease_business — The business portion of the lease payments
Status: **AGREE**

Value: $5,582.96

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].low_use — Business use is 50% or less
Status: **AGREE**

Value: no

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].screened — This vehicle's depreciation is outside this tool
Status: **AGREE**

Value: no

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].year — Year of recovery in 2025
Status: **AGREE**

Value: 2

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].is2025 — Placed in service in 2025
Status: **AGREE**

Value: no

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].is2019 — Placed in service in 2019 (2025 is after the recovery period)
Status: **AGREE**

Value: no

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].bus_cost — Business/investment cost (cost times business use)
Status: **AGREE**

Value: $7,658.80

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].s179_bad — The section 179 election is more than the business cost, or than the SUV limit
Status: **AGREE**

Value: no

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_mixed — The special allowance choice differs within the 5-year class
Status: **AGREE**

Value: no

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].claims_bonus — A special allowance is claimed
Status: **AGREE**

Value: no

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].lim_first_bonus — First-year limit with the special allowance
Status: **DISAGREE**

Project: $19,800.00
Model: $20,200.00
Work: Table 2 footnote: 2025 first-year limit with special allowance

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Here the vehicle's key gives the project's value: line 7 reads lim_2025 only for a 2025 vehicle and lim_prior otherwise, and the project looks every limit up by the year actually placed in service and its year of recovery; the model read the 2025 column. Pub. 946 p. 59 table, checked: 1st year 2025 $20,200 (footnote 1: $12,200 without the special allowance), 2nd year 2024 $19,800, 4th and later year 2021 $5,860, 2020 and 2019 $5,760, footnote 6 (2019 without the special allowance) $10,100; the project's tables carry these values. Not evidence. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].lim_prior — Limit for the vehicle's 2025 year of recovery
Status: **AGREE**

Value: $19,800.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **AGREE**

Value: $19,800.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **AGREE**

Value: $19,544.30

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_ok — Section 179 elected for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line10_2025 — Section 179 for a 2025 vehicle: not more than line 9 for a passenger automobile
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].s179_line10 — The section 179 election, not more than line 9
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line11 — Subtract line 10 from line 9
Status: **AGREE**

Value: $19,544.30

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $7,759.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_full — 100% special allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_forty — 40% special allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_2025 — Special allowance for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line16 — Special depreciation allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **AGREE**

Value: $19,544.30

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line18 — Basis for depreciation (line 15 less line 16)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq4

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].rate_hy — MACRS rate, half-year convention
Status: **DISAGREE**

Project: 32%
Model: 20%
Work: 5-year 200DB half-year, year 1

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The project keys the rate on the vehicle's actual year of recovery (Pub. 946 Table A-1/A-5); the 2025-vehicle rate and line 19 for a 2025 vehicle are not read for a vehicle placed in service earlier, whose line 19 is line19_prior (agreeing or differing only in cents). Not evidence. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].rate_mq — MACRS rate, mid-quarter convention
Status: **DISAGREE**

Project: 38%
Model: 5%
Work: 5-year 200DB mid-quarter Q4, year 1

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The project keys the rate on the vehicle's actual year of recovery (Pub. 946 Table A-1/A-5); the 2025-vehicle rate and line 19 for a 2025 vehicle are not read for a vehicle placed in service earlier, whose line 19 is line19_prior (agreeing or differing only in cents). Not evidence. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].rate_prior — MACRS rate for the 2025 year of recovery
Status: **AGREE**

Value: 32%

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line19_hy — Line 18 times the half-year rate
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line19_mq — Line 18 times the mid-quarter rate
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line19_prior — Line 18 times the rate for the 2025 year of recovery
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line19_earlier — Line 19 for a vehicle placed in service before 2025 (zero after the recovery per
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line19_2025 — Line 19 for a 2025 vehicle, half-year or mid-quarter
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].b100 — Cost less the section 179 deduction (as if used 100% for business)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].r1 — MACRS rate for year 1
Status: **AGREE**

Value: 20%

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].t1 — Year 1 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].t1s — Year 1 section 179 deduction plus MACRS amount
Status: **AGREE**

Value: $7,759.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].r2 — MACRS rate for year 2
Status: **AGREE**

Value: 32%

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].t2 — Year 2 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].l2 — Year 2 limit
Status: **AGREE**

Value: $19,800.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].d2 — Year 2 deduction allowable at 100% business use
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].r3 — MACRS rate for year 3
Status: **AGREE**

Value: 19.2%

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].t3 — Year 3 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].r4 — MACRS rate for year 4
Status: **AGREE**

Value: 11.52%

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].t4 — Year 4 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].r5 — MACRS rate for year 5
Status: **AGREE**

Value: 11.52%

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].t5 — Year 5 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].r6 — MACRS rate for year 6
Status: **AGREE**

Value: 5.76%

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].t6 — Year 6 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].too_old — Placed in service before 2019
Status: **AGREE**

Value: no

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_v — Special allowance for this vehicle (line 25)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_pass — Column (h) for a passenger automobile
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_heavy — Column (h) for a vehicle not subject to the limits
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_v — Column (h)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].bonus — Line 25: special allowance of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].macrs — Column (h): depreciation of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].s179_2025 — Column (i): elected section 179 cost of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_o — Special allowance (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_o — Depreciation (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_o — Section 179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].q4_basis — Basis for the mid-quarter test when placed in service October to December
Status: **DISAGREE**

Project: $0.00
Model: $7,658.80
Work: Q4: business cost 7,658.80 - 2025 section 179 election 0

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. This 2024 vehicle's q4_basis is not read (mq_q4_o is zero for a vehicle not placed in service in 2025, agreeing). The model's working is also wrong: q4_basis is line 15, which here is zero because the prior section 179 deduction ($7,759) exceeds the business cost ($7,658.80); the model subtracted a 2025 election instead. Not evidence. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_o — mq_q4 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_a2 — mq_q4 of a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].mq_total_o — mq_total (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].mq_total_a2 — mq_total of a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].cost179_o — cost179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].cost179_a2 — cost179 of a 2025 vehicle
Status: **DISAGREE**

Project: $7,658.80
Model: $0.00
Work: Not a 2025 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The _o line reads the _a2 copy only for a 2025 vehicle; for this earlier vehicle the _o line and the result are zero (agreeing). Not evidence. [dropped]

### case classm.scveh.5 — prompt sha256 83b6cfc02cfa956785b5c4e5c0ef7e23662691b6a693cd01a71caa5bed182fc9; branches: scveh.owned:false, scveh.owned:true, scveh.no_miles:false, scveh.over_half:true, scveh.smr_ok:true, scveh.smr_bad:false, scveh.line9#0, scveh.line9#1, scveh.is_actual_owned:false, scveh.is_actual_owned:true, scveh.is_actual_leased:false, scveh.is_actual_leased:true, scveh.line20a#0, scveh.line20a#1, scveh.low_use:false, scveh.screen:false, scveh.screened:false, scveh.passenger:true, scveh.suv:false, scveh.is2025:false, scveh.is2025:true, scveh.is2019:false, scveh.s179_bad:false, scveh.after_jan19:true, scveh.bonus_same:true, scveh.bonus_mixed:false, scveh.claims_bonus:false, scveh.lim_2025#1, scveh.line7#0, scveh.line7#1, scveh.line10#0, scveh.line10#1, scveh.line10_2025#0, scveh.s179_line10:left, scveh.s179_line10:right, scveh.line11:floor, scveh.line11:positive, scveh.line14#0, scveh.line14#1, scveh.line15:positive, scveh.bonus_fullcase#0, scveh.bonus_2025#2, scveh.line16#0, scveh.line16#1, scveh.bonus_allowed:left, scveh.line17:floor, scveh.line17:positive, scveh.line18:positive, scveh.line19#0, scveh.line19#1, scveh.line19_earlier#0, scveh.line19_2025#0, scveh.line20:left, scveh.line20:right, scveh.b100:positive, scveh.d1:right, scveh.d2:left, scveh.d2:right, scveh.d3:right, scveh.d4:right, scveh.d5:right, scveh.d6:right, scveh.too_old:false, scveh.bonus_v#0, scveh.macrs_pass#0, scveh.macrs_heavy#0, scveh.macrs_v#0, scveh.bonus#0, scveh.bonus#1, scveh.macrs#0, scveh.macrs#1, scveh.s179_2025#0, scveh.s179_2025#1, scveh.mq_q4#0, scveh.mq_q4#1, scveh.mq_total#0, scveh.mq_total#1, scveh.cost179#0, scveh.cost179#1, scveh.q4_basis#0, scveh.q4_basis#2, scveh.q4_basis#3, scveh.mq_q4_o#0, scveh.mq_q4_o#1, scveh.mq_total_o#0, scveh.mq_total_o#1, scveh.cost179_o#0, scveh.cost179_o#1

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].bm_c — Business miles, as cents
Status: **DISAGREE**

Project: $133.07
Model: $13,307.00
Work: Business miles 13,307

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].cm_c — Commuting miles, as cents
Status: **DISAGREE**

Project: $29.28
Model: $2,928.00
Work: Commuting miles 2,928

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].om_c — Other miles, as cents
Status: **DISAGREE**

Project: $28.24
Model: $2,824.00
Work: Other miles 2,824

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].nonbusiness_c — Commuting and other miles, as cents
Status: **DISAGREE**

Project: $57.52
Model: $5,752.00
Work: 2928 + 2824

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].total_c — Total miles, as cents
Status: **DISAGREE**

Project: $190.59
Model: $19,059.00
Work: 13307 + 5752

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].no_miles — Actual expenses claimed for a vehicle with no miles
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].smr_bad — The standard mileage rate is not available for this vehicle
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].smr_amount — Business miles times the standard mileage rate
Status: **AGREE**

Value: $9,314.90

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].line9_standard — Standard mileage amount plus parking fees and tolls
Status: **AGREE**

Value: $9,314.90

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].operating_business — The business portion of the operating expenses
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].line9_actual — Business portion of the operating expenses plus parking fees and tolls
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].is_actual_owned — Owned and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].is_actual_leased — Leased and on actual expenses
Status: **AGREE**

Value: yes

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].lease_business — The business portion of the lease payments
Status: **AGREE**

Value: $2,493.27

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $2,493.27

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].low_use — Business use is 50% or less
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].screened — This vehicle's depreciation is outside this tool
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].year — Year of recovery in 2025
Status: **AGREE**

Value: 2

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].is2025 — Placed in service in 2025
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].is2019 — Placed in service in 2019 (2025 is after the recovery period)
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].bus_cost — Business/investment cost (cost times business use)
Status: **DISAGREE**

Project: $54,544.08
Model: $54,544.11
Work: 78121 x 13307/19059

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].s179_bad — The section 179 election is more than the business cost, or than the SUV limit
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_mixed — The special allowance choice differs within the 5-year class
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].claims_bonus — A special allowance is claimed
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].lim_first_bonus — First-year limit with the special allowance
Status: **DISAGREE**

Project: $19,800.00
Model: $20,200.00
Work: Table 2 footnote, 2025 with special allowance

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Here the vehicle's key gives the project's value: line 7 reads lim_2025 only for a 2025 vehicle and lim_prior otherwise, and the project looks every limit up by the year actually placed in service and its year of recovery; the model read the 2025 column. Pub. 946 p. 59 table, checked: 1st year 2025 $20,200 (footnote 1: $12,200 without the special allowance), 2nd year 2024 $19,800, 4th and later year 2021 $5,860, 2020 and 2019 $5,760, footnote 6 (2019 without the special allowance) $10,100; the project's tables carry these values. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].lim_prior — Limit for the vehicle's 2025 year of recovery
Status: **AGREE**

Value: $19,800.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **AGREE**

Value: $19,800.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **DISAGREE**

Project: $13,824.36
Model: $13,824.37
Work: 19800 x 13307/19059

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_ok — Section 179 elected for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].line10_2025 — Section 179 for a 2025 vehicle: not more than line 9 for a passenger automobile
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].s179_line10 — The section 179 election, not more than line 9
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].line11 — Subtract line 10 from line 9
Status: **DISAGREE**

Project: $13,824.36
Model: $13,824.37
Work: 13824.37 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **DISAGREE**

Project: $54,544.08
Model: $54,544.11
Work: 54544.11 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_full — 100% special allowance
Status: **DISAGREE**

Project: $54,544.08
Model: $54,544.11
Work: 54544.11 x 100%

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_forty — 40% special allowance
Status: **DISAGREE**

Project: $21,817.63
Model: $21,817.64
Work: 54544.11 x 40%

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **DISAGREE**

Project: $54,544.08
Model: $54,544.11
Work: Acquired after 1/19/2025, so 100%

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_2025 — Special allowance for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].line16 — Special depreciation allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **DISAGREE**

Project: $13,824.36
Model: $13,824.37
Work: 13824.37 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].line18 — Basis for depreciation (line 15 less line 16)
Status: **DISAGREE**

Project: $54,544.08
Model: $54,544.11
Work: 54544.11 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq4

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].rate_hy — MACRS rate, half-year convention
Status: **DISAGREE**

Project: 32%
Model: 20%
Work: 5-yr 200DB HY, year 1

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The project keys the rate on the vehicle's actual year of recovery (Pub. 946 Table A-1/A-5); the 2025-vehicle rate and line 19 for a 2025 vehicle are not read for a vehicle placed in service earlier, whose line 19 is line19_prior (agreeing or differing only in cents). Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].rate_mq — MACRS rate, mid-quarter convention
Status: **DISAGREE**

Project: 38%
Model: 5%
Work: 5-yr 200DB MQ Q4, year 1

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The project keys the rate on the vehicle's actual year of recovery (Pub. 946 Table A-1/A-5); the 2025-vehicle rate and line 19 for a 2025 vehicle are not read for a vehicle placed in service earlier, whose line 19 is line19_prior (agreeing or differing only in cents). Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].rate_prior — MACRS rate for the 2025 year of recovery
Status: **AGREE**

Value: 32%

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].line19_hy — Line 18 times the half-year rate
Status: **DISAGREE**

Project: $17,454.11
Model: $10,908.82
Work: 54544.11 x 20%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The project keys the rate on the vehicle's actual year of recovery (Pub. 946 Table A-1/A-5); the 2025-vehicle rate and line 19 for a 2025 vehicle are not read for a vehicle placed in service earlier, whose line 19 is line19_prior (agreeing or differing only in cents). Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].line19_mq — Line 18 times the mid-quarter rate
Status: **DISAGREE**

Project: $20,726.75
Model: $2,727.21
Work: 54544.11 x 5%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The project keys the rate on the vehicle's actual year of recovery (Pub. 946 Table A-1/A-5); the 2025-vehicle rate and line 19 for a 2025 vehicle are not read for a vehicle placed in service earlier, whose line 19 is line19_prior (agreeing or differing only in cents). Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].line19_prior — Line 18 times the rate for the 2025 year of recovery
Status: **DISAGREE**

Project: $17,454.11
Model: $17,454.12
Work: 54544.11 x 32%

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **DISAGREE**

Project: $17,454.11
Model: $17,454.12
Work: Placed in service before 2025, so the year-2 rate

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].line19_earlier — Line 19 for a vehicle placed in service before 2025 (zero after the recovery per
Status: **DISAGREE**

Project: $17,454.11
Model: $17,454.12
Work: line19_prior

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].line19_2025 — Line 19 for a 2025 vehicle, half-year or mid-quarter
Status: **DISAGREE**

Project: $17,454.11
Model: $10,908.82
Work: Mid-quarter test no, so HY

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The project keys the rate on the vehicle's actual year of recovery (Pub. 946 Table A-1/A-5); the 2025-vehicle rate and line 19 for a 2025 vehicle are not read for a vehicle placed in service earlier, whose line 19 is line19_prior (agreeing or differing only in cents). Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **DISAGREE**

Project: $13,824.36
Model: $13,824.37
Work: lesser of 13824.37 or 17454.12

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].b100 — Cost less the section 179 deduction (as if used 100% for business)
Status: **AGREE**

Value: $78,121.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].r1 — MACRS rate for year 1
Status: **AGREE**

Value: 20%

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].t1 — Year 1 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $15,624.20

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].t1s — Year 1 section 179 deduction plus MACRS amount
Status: **AGREE**

Value: $15,624.20

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].r2 — MACRS rate for year 2
Status: **AGREE**

Value: 32%

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].t2 — Year 2 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $24,998.72

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].l2 — Year 2 limit
Status: **AGREE**

Value: $19,800.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].d2 — Year 2 deduction allowable at 100% business use
Status: **AGREE**

Value: $19,800.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].r3 — MACRS rate for year 3
Status: **AGREE**

Value: 19.2%

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].t3 — Year 3 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $14,999.23

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].r4 — MACRS rate for year 4
Status: **AGREE**

Value: 11.52%

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].t4 — Year 4 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $8,999.54

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].r5 — MACRS rate for year 5
Status: **AGREE**

Value: 11.52%

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].t5 — Year 5 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $8,999.54

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].r6 — MACRS rate for year 6
Status: **AGREE**

Value: 5.76%

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].t6 — Year 6 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $4,499.77

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].too_old — Placed in service before 2019
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_v — Special allowance for this vehicle (line 25)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_pass — Column (h) for a passenger automobile
Status: **DISAGREE**

Project: $13,824.36
Model: $13,824.37
Work: line 20

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_heavy — Column (h) for a vehicle not subject to the limits
Status: **DISAGREE**

Project: $17,454.11
Model: $17,454.12
Work: line 19

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_v — Column (h)
Status: **DISAGREE**

Project: $13,824.36
Model: $13,824.37
Work: Subject to the passenger automobile limits

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].bonus — Line 25: special allowance of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].macrs — Column (h): depreciation of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].s179_2025 — Column (i): elected section 179 cost of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_o — Special allowance (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_o — Depreciation (owned, actual expenses)
Status: **DISAGREE**

Project: $13,824.36
Model: $0.00
Work: Not owned

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. macrs reads macrs_o only for an owned vehicle on actual expenses; this one is leased or on the standard mileage rate, so macrs is zero (agreeing). Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_o — Section 179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].q4_basis — Basis for the mid-quarter test when placed in service October to December
Status: **DISAGREE**

Project: $54,544.08
Model: $54,544.11
Work: Q4, so 54544.11 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_o — mq_q4 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_a2 — mq_q4 of a 2025 vehicle
Status: **DISAGREE**

Project: $54,544.08
Model: $0.00
Work: Not 2025

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The _o line reads the _a2 copy only for a 2025 vehicle; for this earlier vehicle the _o line and the result are zero (agreeing). Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].mq_total_o — mq_total (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].mq_total_a2 — mq_total of a 2025 vehicle
Status: **DISAGREE**

Project: $54,544.08
Model: $0.00
Work: Not 2025

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The _o line reads the _a2 copy only for a 2025 vehicle; for this earlier vehicle the _o line and the result are zero (agreeing). Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].cost179_o — cost179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].cost179_a2 — cost179 of a 2025 vehicle
Status: **DISAGREE**

Project: $54,544.08
Model: $0.00
Work: Not 2025

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The _o line reads the _a2 copy only for a 2025 vehicle; for this earlier vehicle the _o line and the result are zero (agreeing). Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].bm_c — Business miles, as cents
Status: **DISAGREE**

Project: $292.52
Model: $29,252.00
Work: Business miles 29,252

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].cm_c — Commuting miles, as cents
Status: **DISAGREE**

Project: $7.26
Model: $726.00
Work: Commuting miles 726

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].om_c — Other miles, as cents
Status: **DISAGREE**

Project: $16.99
Model: $1,699.00
Work: Other miles 1,699

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].nonbusiness_c — Commuting and other miles, as cents
Status: **DISAGREE**

Project: $24.25
Model: $2,425.00
Work: 726 + 1699

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].total_c — Total miles, as cents
Status: **DISAGREE**

Project: $316.77
Model: $31,677.00
Work: 29252 + 2425

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].no_miles — Actual expenses claimed for a vehicle with no miles
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].smr_bad — The standard mileage rate is not available for this vehicle
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].smr_amount — Business miles times the standard mileage rate
Status: **AGREE**

Value: $20,476.40

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].line9_standard — Standard mileage amount plus parking fees and tolls
Status: **AGREE**

Value: $20,476.40

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].operating_business — The business portion of the operating expenses
Status: **AGREE**

Value: $2,650.29

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].line9_actual — Business portion of the operating expenses plus parking fees and tolls
Status: **AGREE**

Value: $2,650.29

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $2,650.29

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].is_actual_owned — Owned and on actual expenses
Status: **AGREE**

Value: yes

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].is_actual_leased — Leased and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].lease_business — The business portion of the lease payments
Status: **AGREE**

Value: $961.31

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].low_use — Business use is 50% or less
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].screened — This vehicle's depreciation is outside this tool
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].year — Year of recovery in 2025
Status: **AGREE**

Value: 1

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].is2025 — Placed in service in 2025
Status: **AGREE**

Value: yes

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].is2019 — Placed in service in 2019 (2025 is after the recovery period)
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].bus_cost — Business/investment cost (cost times business use)
Status: **AGREE**

Value: $41,575.39

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].s179_bad — The section 179 election is more than the business cost, or than the SUV limit
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_mixed — The special allowance choice differs within the 5-year class
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].claims_bonus — A special allowance is claimed
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].lim_first_bonus — First-year limit with the special allowance
Status: **AGREE**

Value: $20,200.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].lim_first_none — First-year limit without the special allowance
Status: **AGREE**

Value: $12,200.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].lim_2025 — Limit for a 2025 vehicle
Status: **AGREE**

Value: $12,200.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].lim_prior — Limit for the vehicle's 2025 year of recovery
Status: **DISAGREE**

Project: $20,200.00
Model: $12,200.00
Work: Year 1 of a 2025 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. For a 2025 vehicle line 7 reads lim_2025 (agreeing), not lim_prior; lim_prior is the table's year-1 cell with the special allowance, $20,200 (Pub. 946 p. 59). Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **AGREE**

Value: $12,200.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **AGREE**

Value: $11,266.04

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].s179_2025_ok — Section 179 elected for a 2025 vehicle
Status: **AGREE**

Value: $14,878.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $11,266.04

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].line10_2025 — Section 179 for a 2025 vehicle: not more than line 9 for a passenger automobile
Status: **AGREE**

Value: $11,266.04

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].s179_line10 — The section 179 election, not more than line 9
Status: **AGREE**

Value: $11,266.04

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].line11 — Subtract line 10 from line 9
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $11,266.04

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **AGREE**

Value: $30,309.35

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_full — 100% special allowance
Status: **AGREE**

Value: $30,309.35

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_forty — 40% special allowance
Status: **AGREE**

Value: $12,123.74

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **AGREE**

Value: $30,309.35

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_2025 — Special allowance for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].line16 — Special depreciation allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].line18 — Basis for depreciation (line 15 less line 16)
Status: **AGREE**

Value: $30,309.35

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq3

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].rate_hy — MACRS rate, half-year convention
Status: **AGREE**

Value: 20%

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].rate_mq — MACRS rate, mid-quarter convention
Status: **AGREE**

Value: 15%

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].rate_prior — MACRS rate for the 2025 year of recovery
Status: **AGREE**

Value: 20%

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].line19_hy — Line 18 times the half-year rate
Status: **AGREE**

Value: $6,061.87

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].line19_mq — Line 18 times the mid-quarter rate
Status: **AGREE**

Value: $4,546.40

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].line19_prior — Line 18 times the rate for the 2025 year of recovery
Status: **AGREE**

Value: $6,061.87

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $6,061.87

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].line19_earlier — Line 19 for a vehicle placed in service before 2025 (zero after the recovery per
Status: **AGREE**

Value: $6,061.87

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].line19_2025 — Line 19 for a 2025 vehicle, half-year or mid-quarter
Status: **AGREE**

Value: $6,061.87

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].b100 — Cost less the section 179 deduction (as if used 100% for business)
Status: **DISAGREE**

Project: $45,022.00
Model: $33,755.96
Work: 45022 - 11266.04

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The year 1 to 6 recovery chain (b100, t1 to t6, d1 to d6) feeds only the post-recovery amount of a 2019 vehicle; this vehicle was placed in service in 2025. The model also misread the chain: b100 is cost less the section 179 deduction claimed in the first year (prior_179, given as zero), not the 2025 line 10 amount ($11,266.04), and t1s adds prior_179, so d1 = lesser of $12,200 and $9,004.40 = $9,004.40. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].r1 — MACRS rate for year 1
Status: **AGREE**

Value: 20%

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].t1 — Year 1 MACRS amount as if used 100% for business
Status: **DISAGREE**

Project: $9,004.40
Model: $6,751.19
Work: 33755.96 x 20%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The year 1 to 6 recovery chain (b100, t1 to t6, d1 to d6) feeds only the post-recovery amount of a 2019 vehicle; this vehicle was placed in service in 2025. The model also misread the chain: b100 is cost less the section 179 deduction claimed in the first year (prior_179, given as zero), not the 2025 line 10 amount ($11,266.04), and t1s adds prior_179, so d1 = lesser of $12,200 and $9,004.40 = $9,004.40. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].l1 — Year 1 limit (no special allowance)
Status: **AGREE**

Value: $12,200.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].t1s — Year 1 section 179 deduction plus MACRS amount
Status: **DISAGREE**

Project: $9,004.40
Model: $18,017.23
Work: 11266.04 + 6751.19

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The year 1 to 6 recovery chain (b100, t1 to t6, d1 to d6) feeds only the post-recovery amount of a 2019 vehicle; this vehicle was placed in service in 2025. The model also misread the chain: b100 is cost less the section 179 deduction claimed in the first year (prior_179, given as zero), not the 2025 line 10 amount ($11,266.04), and t1s adds prior_179, so d1 = lesser of $12,200 and $9,004.40 = $9,004.40. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].d1 — Year 1 deduction allowable at 100% business use (the lesser of the limit or the 
Status: **DISAGREE**

Project: $9,004.40
Model: $12,200.00
Work: lesser of 12200 or 18017.23

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The year 1 to 6 recovery chain (b100, t1 to t6, d1 to d6) feeds only the post-recovery amount of a 2019 vehicle; this vehicle was placed in service in 2025. The model also misread the chain: b100 is cost less the section 179 deduction claimed in the first year (prior_179, given as zero), not the 2025 line 10 amount ($11,266.04), and t1s adds prior_179, so d1 = lesser of $12,200 and $9,004.40 = $9,004.40. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].r2 — MACRS rate for year 2
Status: **AGREE**

Value: 32%

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].t2 — Year 2 MACRS amount as if used 100% for business
Status: **DISAGREE**

Project: $14,407.04
Model: $10,801.91
Work: 33755.96 x 32%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The year 1 to 6 recovery chain (b100, t1 to t6, d1 to d6) feeds only the post-recovery amount of a 2019 vehicle; this vehicle was placed in service in 2025. The model also misread the chain: b100 is cost less the section 179 deduction claimed in the first year (prior_179, given as zero), not the 2025 line 10 amount ($11,266.04), and t1s adds prior_179, so d1 = lesser of $12,200 and $9,004.40 = $9,004.40. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].r3 — MACRS rate for year 3
Status: **AGREE**

Value: 19.2%

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].t3 — Year 3 MACRS amount as if used 100% for business
Status: **DISAGREE**

Project: $8,644.22
Model: $6,481.14
Work: 33755.96 x 19.2%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The year 1 to 6 recovery chain (b100, t1 to t6, d1 to d6) feeds only the post-recovery amount of a 2019 vehicle; this vehicle was placed in service in 2025. The model also misread the chain: b100 is cost less the section 179 deduction claimed in the first year (prior_179, given as zero), not the 2025 line 10 amount ($11,266.04), and t1s adds prior_179, so d1 = lesser of $12,200 and $9,004.40 = $9,004.40. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].r4 — MACRS rate for year 4
Status: **AGREE**

Value: 11.52%

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].t4 — Year 4 MACRS amount as if used 100% for business
Status: **DISAGREE**

Project: $5,186.53
Model: $3,888.69
Work: 33755.96 x 11.52%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The year 1 to 6 recovery chain (b100, t1 to t6, d1 to d6) feeds only the post-recovery amount of a 2019 vehicle; this vehicle was placed in service in 2025. The model also misread the chain: b100 is cost less the section 179 deduction claimed in the first year (prior_179, given as zero), not the 2025 line 10 amount ($11,266.04), and t1s adds prior_179, so d1 = lesser of $12,200 and $9,004.40 = $9,004.40. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].r5 — MACRS rate for year 5
Status: **AGREE**

Value: 11.52%

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].t5 — Year 5 MACRS amount as if used 100% for business
Status: **DISAGREE**

Project: $5,186.53
Model: $3,888.69
Work: 33755.96 x 11.52%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The year 1 to 6 recovery chain (b100, t1 to t6, d1 to d6) feeds only the post-recovery amount of a 2019 vehicle; this vehicle was placed in service in 2025. The model also misread the chain: b100 is cost less the section 179 deduction claimed in the first year (prior_179, given as zero), not the 2025 line 10 amount ($11,266.04), and t1s adds prior_179, so d1 = lesser of $12,200 and $9,004.40 = $9,004.40. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].r6 — MACRS rate for year 6
Status: **AGREE**

Value: 5.76%

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].t6 — Year 6 MACRS amount as if used 100% for business
Status: **DISAGREE**

Project: $2,593.27
Model: $1,944.34
Work: 33755.96 x 5.76%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The year 1 to 6 recovery chain (b100, t1 to t6, d1 to d6) feeds only the post-recovery amount of a 2019 vehicle; this vehicle was placed in service in 2025. The model also misread the chain: b100 is cost less the section 179 deduction claimed in the first year (prior_179, given as zero), not the 2025 line 10 amount ($11,266.04), and t1s adds prior_179, so d1 = lesser of $12,200 and $9,004.40 = $9,004.40. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].too_old — Placed in service before 2019
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_v — Special allowance for this vehicle (line 25)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].macrs_pass — Column (h) for a passenger automobile
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].macrs_heavy — Column (h) for a vehicle not subject to the limits
Status: **AGREE**

Value: $6,061.87

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].macrs_v — Column (h)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].bonus — Line 25: special allowance of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].macrs — Column (h): depreciation of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].s179_2025 — Column (i): elected section 179 cost of this vehicle
Status: **AGREE**

Value: $11,266.04

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **AGREE**

Value: $30,309.35

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **AGREE**

Value: $41,575.39

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_o — Special allowance (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].macrs_o — Depreciation (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].s179_2025_o — Section 179 (owned, actual expenses)
Status: **AGREE**

Value: $11,266.04

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].q4_basis — Basis for the mid-quarter test when placed in service October to December
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].mq_q4_o — mq_q4 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].mq_q4_a2 — mq_q4 of a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].mq_total_o — mq_total (owned, actual expenses)
Status: **AGREE**

Value: $30,309.35

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].mq_total_a2 — mq_total of a 2025 vehicle
Status: **AGREE**

Value: $30,309.35

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].cost179_o — cost179 (owned, actual expenses)
Status: **AGREE**

Value: $41,575.39

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_2].cost179_a2 — cost179 of a 2025 vehicle
Status: **AGREE**

Value: $41,575.39

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].bm_c — Business miles, as cents
Status: **DISAGREE**

Project: $207.67
Model: $20,767.00
Work: Business miles 20,767

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].cm_c — Commuting miles, as cents
Status: **DISAGREE**

Project: $32.86
Model: $3,286.00
Work: Commuting miles 3,286

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].om_c — Other miles, as cents
Status: **DISAGREE**

Project: $30.77
Model: $3,077.00
Work: Other miles 3,077

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].nonbusiness_c — Commuting and other miles, as cents
Status: **DISAGREE**

Project: $63.63
Model: $6,363.00
Work: 3286 + 3077

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].total_c — Total miles, as cents
Status: **DISAGREE**

Project: $271.30
Model: $27,130.00
Work: 20767 + 6363

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].no_miles — Actual expenses claimed for a vehicle with no miles
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].smr_bad — The standard mileage rate is not available for this vehicle
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].smr_amount — Business miles times the standard mileage rate
Status: **AGREE**

Value: $14,536.90

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line9_standard — Standard mileage amount plus parking fees and tolls
Status: **AGREE**

Value: $14,536.90

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].operating_business — The business portion of the operating expenses
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line9_actual — Business portion of the operating expenses plus parking fees and tolls
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $14,536.90

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].is_actual_owned — Owned and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].is_actual_leased — Leased and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].lease_business — The business portion of the lease payments
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].low_use — Business use is 50% or less
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].screened — This vehicle's depreciation is outside this tool
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].year — Year of recovery in 2025
Status: **AGREE**

Value: 6

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].is2025 — Placed in service in 2025
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].is2019 — Placed in service in 2019 (2025 is after the recovery period)
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].bus_cost — Business/investment cost (cost times business use)
Status: **DISAGREE**

Project: $28,476.75
Model: $28,476.74
Work: 37202 x 20767/27130

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].s179_bad — The section 179 election is more than the business cost, or than the SUV limit
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_mixed — The special allowance choice differs within the 5-year class
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].claims_bonus — A special allowance is claimed
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].lim_first_bonus — First-year limit with the special allowance
Status: **DISAGREE**

Project: $5,760.00
Model: $20,200.00
Work: Table 2 footnote

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Here the vehicle's key gives the project's value: line 7 reads lim_2025 only for a 2025 vehicle and lim_prior otherwise, and the project looks every limit up by the year actually placed in service and its year of recovery; the model read the 2025 column. Pub. 946 p. 59 table, checked: 1st year 2025 $20,200 (footnote 1: $12,200 without the special allowance), 2nd year 2024 $19,800, 4th and later year 2021 $5,860, 2020 and 2019 $5,760, footnote 6 (2019 without the special allowance) $10,100; the project's tables carry these values. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].lim_prior — Limit for the vehicle's 2025 year of recovery
Status: **AGREE**

Value: $5,760.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **AGREE**

Value: $5,760.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **DISAGREE**

Project: $4,409.07
Model: $4,409.06
Work: 5760 x 20767/27130

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].s179_2025_ok — Section 179 elected for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line10_2025 — Section 179 for a 2025 vehicle: not more than line 9 for a passenger automobile
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].s179_line10 — The section 179 election, not more than line 9
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line11 — Subtract line 10 from line 9
Status: **DISAGREE**

Project: $4,409.07
Model: $4,409.06
Work: 4409.06 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **DISAGREE**

Project: $28,476.75
Model: $28,476.74
Work: 28476.74 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_full — 100% special allowance
Status: **DISAGREE**

Project: $28,476.75
Model: $28,476.74
Work: x 100%

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_forty — 40% special allowance
Status: **AGREE**

Value: $11,390.70

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **DISAGREE**

Project: $28,476.75
Model: $28,476.74
Work: Acquired after 1/19/2025

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_2025 — Special allowance for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line16 — Special depreciation allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **DISAGREE**

Project: $4,409.07
Model: $4,409.06
Work: 4409.06 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line18 — Basis for depreciation (line 15 less line 16)
Status: **DISAGREE**

Project: $28,476.75
Model: $28,476.74
Work: 28476.74 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq4

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].rate_hy — MACRS rate, half-year convention
Status: **DISAGREE**

Project: 5.76%
Model: 20%
Work: HY, year 1

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The project keys the rate on the vehicle's actual year of recovery (Pub. 946 Table A-1/A-5); the 2025-vehicle rate and line 19 for a 2025 vehicle are not read for a vehicle placed in service earlier, whose line 19 is line19_prior (agreeing or differing only in cents). Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].rate_mq — MACRS rate, mid-quarter convention
Status: **DISAGREE**

Project: 9.58%
Model: 5%
Work: MQ Q4, year 1

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The project keys the rate on the vehicle's actual year of recovery (Pub. 946 Table A-1/A-5); the 2025-vehicle rate and line 19 for a 2025 vehicle are not read for a vehicle placed in service earlier, whose line 19 is line19_prior (agreeing or differing only in cents). Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].rate_prior — MACRS rate for the 2025 year of recovery
Status: **AGREE**

Value: 4.26%

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line19_hy — Line 18 times the half-year rate
Status: **DISAGREE**

Project: $1,640.26
Model: $5,695.35
Work: 28476.74 x 20%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The project keys the rate on the vehicle's actual year of recovery (Pub. 946 Table A-1/A-5); the 2025-vehicle rate and line 19 for a 2025 vehicle are not read for a vehicle placed in service earlier, whose line 19 is line19_prior (agreeing or differing only in cents). Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line19_mq — Line 18 times the mid-quarter rate
Status: **DISAGREE**

Project: $2,728.07
Model: $1,423.84
Work: 28476.74 x 5%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The project keys the rate on the vehicle's actual year of recovery (Pub. 946 Table A-1/A-5); the 2025-vehicle rate and line 19 for a 2025 vehicle are not read for a vehicle placed in service earlier, whose line 19 is line19_prior (agreeing or differing only in cents). Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line19_prior — Line 18 times the rate for the 2025 year of recovery
Status: **AGREE**

Value: $1,213.11

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $1,213.11

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line19_earlier — Line 19 for a vehicle placed in service before 2025 (zero after the recovery per
Status: **AGREE**

Value: $1,213.11

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line19_2025 — Line 19 for a 2025 vehicle, half-year or mid-quarter
Status: **DISAGREE**

Project: $1,640.26
Model: $5,695.35
Work: HY

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The project keys the rate on the vehicle's actual year of recovery (Pub. 946 Table A-1/A-5); the 2025-vehicle rate and line 19 for a 2025 vehicle are not read for a vehicle placed in service earlier, whose line 19 is line19_prior (agreeing or differing only in cents). Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

Value: $1,213.11

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].b100 — Cost less the section 179 deduction (as if used 100% for business)
Status: **AGREE**

Value: $37,202.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].r1 — MACRS rate for year 1
Status: **AGREE**

Value: 25%

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].t1 — Year 1 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $9,300.50

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].t1s — Year 1 section 179 deduction plus MACRS amount
Status: **AGREE**

Value: $9,300.50

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].r2 — MACRS rate for year 2
Status: **AGREE**

Value: 30%

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].t2 — Year 2 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $11,160.60

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].l2 — Year 2 limit
Status: **AGREE**

Value: $16,100.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].d2 — Year 2 deduction allowable at 100% business use
Status: **AGREE**

Value: $11,160.60

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].r3 — MACRS rate for year 3
Status: **AGREE**

Value: 18%

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].t3 — Year 3 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $6,696.36

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].l3 — Year 3 limit
Status: **AGREE**

Value: $9,700.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].d3 — Year 3 deduction allowable at 100% business use
Status: **AGREE**

Value: $6,696.36

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].r4 — MACRS rate for year 4
Status: **AGREE**

Value: 11.37%

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].t4 — Year 4 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $4,229.87

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].l4 — Year 4 limit
Status: **AGREE**

Value: $5,760.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].d4 — Year 4 deduction allowable at 100% business use
Status: **AGREE**

Value: $4,229.87

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].r5 — MACRS rate for year 5
Status: **AGREE**

Value: 11.37%

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].t5 — Year 5 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $4,229.87

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].l5 — Year 5 limit
Status: **AGREE**

Value: $5,760.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].d5 — Year 5 deduction allowable at 100% business use
Status: **AGREE**

Value: $4,229.87

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].r6 — MACRS rate for year 6
Status: **AGREE**

Value: 4.26%

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].t6 — Year 6 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $1,584.81

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].l6 — Year 6 limit
Status: **AGREE**

Value: $5,760.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].d6 — Year 6 deduction allowable at 100% business use
Status: **AGREE**

Value: $1,584.81

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].too_old — Placed in service before 2019
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_v — Special allowance for this vehicle (line 25)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].macrs_pass — Column (h) for a passenger automobile
Status: **AGREE**

Value: $1,213.11

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].macrs_heavy — Column (h) for a vehicle not subject to the limits
Status: **AGREE**

Value: $1,213.11

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].macrs_v — Column (h)
Status: **AGREE**

Value: $1,213.11

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].bonus — Line 25: special allowance of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].macrs — Column (h): depreciation of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].s179_2025 — Column (i): elected section 179 cost of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_o — Special allowance (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].macrs_o — Depreciation (owned, actual expenses)
Status: **DISAGREE**

Project: $1,213.11
Model: $0.00
Work: Not actual-owned

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. macrs reads macrs_o only for an owned vehicle on actual expenses; this one is leased or on the standard mileage rate, so macrs is zero (agreeing). Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].s179_2025_o — Section 179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].q4_basis — Basis for the mid-quarter test when placed in service October to December
Status: **DISAGREE**

Project: $28,476.75
Model: $28,476.74
Work: Q4, so 28476.74 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].mq_q4_o — mq_q4 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].mq_q4_a2 — mq_q4 of a 2025 vehicle
Status: **DISAGREE**

Project: $28,476.75
Model: $0.00
Work: Not 2025

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The _o line reads the _a2 copy only for a 2025 vehicle; for this earlier vehicle the _o line and the result are zero (agreeing). Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].mq_total_o — mq_total (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].mq_total_a2 — mq_total of a 2025 vehicle
Status: **DISAGREE**

Project: $28,476.75
Model: $0.00
Work: Not 2025

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The _o line reads the _a2 copy only for a 2025 vehicle; for this earlier vehicle the _o line and the result are zero (agreeing). Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].cost179_o — cost179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].cost179_a2 — cost179 of a 2025 vehicle
Status: **DISAGREE**

Project: $28,476.75
Model: $0.00
Work: Not 2025

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The _o line reads the _a2 copy only for a 2025 vehicle; for this earlier vehicle the _o line and the result are zero (agreeing). Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].bm_c — Business miles, as cents
Status: **DISAGREE**

Project: $155.46
Model: $15,546.00
Work: Business miles 15,546

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].cm_c — Commuting miles, as cents
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].om_c — Other miles, as cents
Status: **DISAGREE**

Project: $37.99
Model: $3,799.00
Work: Other miles 3,799

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].nonbusiness_c — Commuting and other miles, as cents
Status: **DISAGREE**

Project: $37.99
Model: $3,799.00
Work: 0 + 3799

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].total_c — Total miles, as cents
Status: **DISAGREE**

Project: $193.45
Model: $19,345.00
Work: 15546 + 3799

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].no_miles — Actual expenses claimed for a vehicle with no miles
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].smr_bad — The standard mileage rate is not available for this vehicle
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].smr_amount — Business miles times the standard mileage rate
Status: **AGREE**

Value: $10,882.20

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line9_standard — Standard mileage amount plus parking fees and tolls
Status: **AGREE**

Value: $10,882.20

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].operating_business — The business portion of the operating expenses
Status: **AGREE**

Value: $1,342.04

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line9_actual — Business portion of the operating expenses plus parking fees and tolls
Status: **AGREE**

Value: $1,342.04

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $10,882.20

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].is_actual_owned — Owned and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].is_actual_leased — Leased and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].lease_business — The business portion of the lease payments
Status: **AGREE**

Value: $1,407.14

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].low_use — Business use is 50% or less
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].screened — This vehicle's depreciation is outside this tool
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].year — Year of recovery in 2025
Status: **AGREE**

Value: 2

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].is2025 — Placed in service in 2025
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].is2019 — Placed in service in 2019 (2025 is after the recovery period)
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].bus_cost — Business/investment cost (cost times business use)
Status: **DISAGREE**

Project: $56,442.18
Model: $56,442.15
Work: 70235 x 15546/19345

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].s179_bad — The section 179 election is more than the business cost, or than the SUV limit
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_mixed — The special allowance choice differs within the 5-year class
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].claims_bonus — A special allowance is claimed
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].lim_first_bonus — First-year limit with the special allowance
Status: **DISAGREE**

Project: $19,800.00
Model: $20,200.00
Work: Table 2 footnote

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Here the vehicle's key gives the project's value: line 7 reads lim_2025 only for a 2025 vehicle and lim_prior otherwise, and the project looks every limit up by the year actually placed in service and its year of recovery; the model read the 2025 column. Pub. 946 p. 59 table, checked: 1st year 2025 $20,200 (footnote 1: $12,200 without the special allowance), 2nd year 2024 $19,800, 4th and later year 2021 $5,860, 2020 and 2019 $5,760, footnote 6 (2019 without the special allowance) $10,100; the project's tables carry these values. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].lim_prior — Limit for the vehicle's 2025 year of recovery
Status: **AGREE**

Value: $19,800.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **AGREE**

Value: $19,800.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **DISAGREE**

Project: $15,911.66
Model: $15,911.65
Work: 19800 x 15546/19345

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].s179_2025_ok — Section 179 elected for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line10_2025 — Section 179 for a 2025 vehicle: not more than line 9 for a passenger automobile
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].s179_line10 — The section 179 election, not more than line 9
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line11 — Subtract line 10 from line 9
Status: **DISAGREE**

Project: $15,911.66
Model: $15,911.65
Work: 15911.65 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **DISAGREE**

Project: $56,442.18
Model: $56,442.15
Work: 56442.15 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_full — 100% special allowance
Status: **DISAGREE**

Project: $56,442.18
Model: $56,442.15
Work: x 100%

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_forty — 40% special allowance
Status: **DISAGREE**

Project: $22,576.87
Model: $22,576.86
Work: x 40%

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **DISAGREE**

Project: $56,442.18
Model: $56,442.15
Work: Acquired after 1/19/2025

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_2025 — Special allowance for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line16 — Special depreciation allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **DISAGREE**

Project: $15,911.66
Model: $15,911.65
Work: 15911.65 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line18 — Basis for depreciation (line 15 less line 16)
Status: **DISAGREE**

Project: $56,442.18
Model: $56,442.15
Work: 56442.15 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq1

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].rate_hy — MACRS rate, half-year convention
Status: **DISAGREE**

Project: 32%
Model: 20%
Work: HY, year 1

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The project keys the rate on the vehicle's actual year of recovery (Pub. 946 Table A-1/A-5); the 2025-vehicle rate and line 19 for a 2025 vehicle are not read for a vehicle placed in service earlier, whose line 19 is line19_prior (agreeing or differing only in cents). Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].rate_mq — MACRS rate, mid-quarter convention
Status: **DISAGREE**

Project: 26%
Model: 35%
Work: MQ Q1, year 1

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The project keys the rate on the vehicle's actual year of recovery (Pub. 946 Table A-1/A-5); the 2025-vehicle rate and line 19 for a 2025 vehicle are not read for a vehicle placed in service earlier, whose line 19 is line19_prior (agreeing or differing only in cents). Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].rate_prior — MACRS rate for the 2025 year of recovery
Status: **AGREE**

Value: 34%

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line19_hy — Line 18 times the half-year rate
Status: **DISAGREE**

Project: $18,061.50
Model: $11,288.43
Work: 56442.15 x 20%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The project keys the rate on the vehicle's actual year of recovery (Pub. 946 Table A-1/A-5); the 2025-vehicle rate and line 19 for a 2025 vehicle are not read for a vehicle placed in service earlier, whose line 19 is line19_prior (agreeing or differing only in cents). Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line19_mq — Line 18 times the mid-quarter rate
Status: **DISAGREE**

Project: $14,674.97
Model: $19,754.75
Work: 56442.15 x 35%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The project keys the rate on the vehicle's actual year of recovery (Pub. 946 Table A-1/A-5); the 2025-vehicle rate and line 19 for a 2025 vehicle are not read for a vehicle placed in service earlier, whose line 19 is line19_prior (agreeing or differing only in cents). Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line19_prior — Line 18 times the rate for the 2025 year of recovery
Status: **DISAGREE**

Project: $19,190.34
Model: $19,190.33
Work: 56442.15 x 34%

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **DISAGREE**

Project: $19,190.34
Model: $19,190.33
Work: Placed in service before 2025

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line19_earlier — Line 19 for a vehicle placed in service before 2025 (zero after the recovery per
Status: **DISAGREE**

Project: $19,190.34
Model: $19,190.33
Work: line19_prior

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line19_2025 — Line 19 for a 2025 vehicle, half-year or mid-quarter
Status: **DISAGREE**

Project: $18,061.50
Model: $11,288.43
Work: HY

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The project keys the rate on the vehicle's actual year of recovery (Pub. 946 Table A-1/A-5); the 2025-vehicle rate and line 19 for a 2025 vehicle are not read for a vehicle placed in service earlier, whose line 19 is line19_prior (agreeing or differing only in cents). Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **DISAGREE**

Project: $15,911.66
Model: $15,911.65
Work: lesser of 15911.65 or 19190.33

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].b100 — Cost less the section 179 deduction (as if used 100% for business)
Status: **AGREE**

Value: $70,235.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].r1 — MACRS rate for year 1
Status: **AGREE**

Value: 15%

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].t1 — Year 1 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $10,535.25

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].t1s — Year 1 section 179 deduction plus MACRS amount
Status: **AGREE**

Value: $10,535.25

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].r2 — MACRS rate for year 2
Status: **AGREE**

Value: 34%

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].t2 — Year 2 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $23,879.90

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].l2 — Year 2 limit
Status: **AGREE**

Value: $19,800.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].d2 — Year 2 deduction allowable at 100% business use
Status: **AGREE**

Value: $19,800.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].r3 — MACRS rate for year 3
Status: **AGREE**

Value: 20.4%

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].t3 — Year 3 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $14,327.94

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].r4 — MACRS rate for year 4
Status: **AGREE**

Value: 12.24%

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].t4 — Year 4 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $8,596.76

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].r5 — MACRS rate for year 5
Status: **AGREE**

Value: 11.3%

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].t5 — Year 5 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $7,936.56

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].r6 — MACRS rate for year 6
Status: **AGREE**

Value: 7.06%

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].t6 — Year 6 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $4,958.59

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].too_old — Placed in service before 2019
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_v — Special allowance for this vehicle (line 25)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].macrs_pass — Column (h) for a passenger automobile
Status: **DISAGREE**

Project: $15,911.66
Model: $15,911.65
Work: line 20

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].macrs_heavy — Column (h) for a vehicle not subject to the limits
Status: **DISAGREE**

Project: $19,190.34
Model: $19,190.33
Work: line 19

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].macrs_v — Column (h)
Status: **DISAGREE**

Project: $15,911.66
Model: $15,911.65
Work: Subject to the limits

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].bonus — Line 25: special allowance of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].macrs — Column (h): depreciation of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].s179_2025 — Column (i): elected section 179 cost of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_o — Special allowance (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].macrs_o — Depreciation (owned, actual expenses)
Status: **DISAGREE**

Project: $15,911.66
Model: $0.00
Work: Not actual-owned

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. macrs reads macrs_o only for an owned vehicle on actual expenses; this one is leased or on the standard mileage rate, so macrs is zero (agreeing). Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].s179_2025_o — Section 179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].q4_basis — Basis for the mid-quarter test when placed in service October to December
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].mq_q4_o — mq_q4 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].mq_q4_a2 — mq_q4 of a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].mq_total_o — mq_total (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].mq_total_a2 — mq_total of a 2025 vehicle
Status: **DISAGREE**

Project: $56,442.18
Model: $0.00
Work: Not 2025

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The _o line reads the _a2 copy only for a 2025 vehicle; for this earlier vehicle the _o line and the result are zero (agreeing). Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].cost179_o — cost179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].cost179_a2 — cost179 of a 2025 vehicle
Status: **DISAGREE**

Project: $56,442.18
Model: $0.00
Work: Not 2025

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The _o line reads the _a2 copy only for a 2025 vehicle; for this earlier vehicle the _o line and the result are zero (agreeing). Not evidence. [dropped]

### case classm.scveh.6 — prompt sha256 134a4c33a26ba19d9723069c6bb422218d928a38b97e3b80f59994cc5ee42ba7; branches: scveh.owned:true, scveh.no_miles:false, scveh.over_half:true, scveh.smr_ok:true, scveh.smr_bad:false, scveh.line9#0, scveh.line9#1, scveh.is_actual_owned:false, scveh.is_actual_owned:true, scveh.is_actual_leased:false, scveh.line20a#1, scveh.low_use:false, scveh.screen:false, scveh.screened:false, scveh.passenger:false, scveh.passenger:true, scveh.suv:false, scveh.is2025:false, scveh.is2019:false, scveh.is2019:true, scveh.s179_bad:false, scveh.after_jan19:true, scveh.bonus_same:true, scveh.bonus_mixed:false, scveh.claims_bonus:false, scveh.lim_2025#1, scveh.line7#1, scveh.line10#1, scveh.line10_2025#0, scveh.line10_2025#1, scveh.s179_line10:left, scveh.line11:positive, scveh.line14#1, scveh.line15:positive, scveh.bonus_fullcase#0, scveh.bonus_2025#2, scveh.line16#1, scveh.bonus_allowed:left, scveh.line17:positive, scveh.line18:positive, scveh.line19#1, scveh.line19_earlier#0, scveh.line19_earlier#1, scveh.line19_2025#1, scveh.line20:right, scveh.b100:positive, scveh.d1:right, scveh.d2:left, scveh.d2:right, scveh.d3:left, scveh.d3:right, scveh.d4:left, scveh.d4:right, scveh.d5:left, scveh.d5:right, scveh.d6:left, scveh.unrecovered:positive, scveh.post_amount:left, scveh.too_old:false, scveh.bonus_v#0, scveh.bonus_v#1, scveh.macrs_pass#0, scveh.macrs_pass#1, scveh.macrs_heavy#0, scveh.macrs_heavy#1, scveh.macrs_v#0, scveh.macrs_v#1, scveh.bonus#0, scveh.bonus#1, scveh.macrs#0, scveh.macrs#1, scveh.s179_2025#0, scveh.s179_2025#1, scveh.mq_q4#0, scveh.mq_q4#1, scveh.mq_total#0, scveh.mq_total#1, scveh.cost179#0, scveh.cost179#1, scveh.q4_basis#2, scveh.q4_basis#3, scveh.mq_q4_o#1, scveh.mq_total_o#1, scveh.cost179_o#1

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].bm_c — Business miles, as cents
Status: **DISAGREE**

Project: $186.74
Model: $18,674.00
Work: Business miles 18,674

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].cm_c — Commuting miles, as cents
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].om_c — Other miles, as cents
Status: **DISAGREE**

Project: $31.32
Model: $3,132.00
Work: Other miles 3,132

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].nonbusiness_c — Commuting and other miles, as cents
Status: **DISAGREE**

Project: $31.32
Model: $3,132.00
Work: 0 + 3,132

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].total_c — Total miles, as cents
Status: **DISAGREE**

Project: $218.06
Model: $21,806.00
Work: 18,674 + 3,132

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].no_miles — Actual expenses claimed for a vehicle with no miles
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].smr_bad — The standard mileage rate is not available for this vehicle
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].smr_amount — Business miles times the standard mileage rate
Status: **AGREE**

Value: $13,071.80

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line9_standard — Standard mileage amount plus parking fees and tolls
Status: **AGREE**

Value: $13,071.80

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].operating_business — The business portion of the operating expenses
Status: **AGREE**

Value: $8,563.70

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line9_actual — Business portion of the operating expenses plus parking fees and tolls
Status: **AGREE**

Value: $8,563.70

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $13,071.80

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].is_actual_owned — Owned and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].is_actual_leased — Leased and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].lease_business — The business portion of the lease payments
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].low_use — Business use is 50% or less
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].screened — This vehicle's depreciation is outside this tool
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].year — Year of recovery in 2025
Status: **AGREE**

Value: 7

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].is2025 — Placed in service in 2025
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].is2019 — Placed in service in 2019 (2025 is after the recovery period)
Status: **AGREE**

Value: yes

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].bus_cost — Business/investment cost (cost times business use)
Status: **DISAGREE**

Project: $56,076.82
Model: $56,076.81
Work: 65,482 x 18,674/21,806

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].s179_bad — The section 179 election is more than the business cost, or than the SUV limit
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_mixed — The special allowance choice differs within the 5-year class
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].claims_bonus — A special allowance is claimed
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].lim_first_bonus — First-year limit with the special allowance
Status: **DISAGREE**

Project: $5,760.00
Model: $20,200.00
Work: Table 2 footnote: 2025 limit with special allowance

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Here the vehicle's key gives the project's value: line 7 reads lim_2025 only for a 2025 vehicle and lim_prior otherwise, and the project looks every limit up by the year actually placed in service and its year of recovery; the model read the 2025 column. Pub. 946 p. 59 table, checked: 1st year 2025 $20,200 (footnote 1: $12,200 without the special allowance), 2nd year 2024 $19,800, 4th and later year 2021 $5,860, 2020 and 2019 $5,760, footnote 6 (2019 without the special allowance) $10,100; the project's tables carry these values. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].lim_first_none — First-year limit without the special allowance
Status: **DISAGREE**

Project: $10,100.00
Model: $12,200.00
Work: Table 2: 2025 year 1 limit

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Here the vehicle's key gives the project's value: line 7 reads lim_2025 only for a 2025 vehicle and lim_prior otherwise, and the project looks every limit up by the year actually placed in service and its year of recovery; the model read the 2025 column. Pub. 946 p. 59 table, checked: 1st year 2025 $20,200 (footnote 1: $12,200 without the special allowance), 2nd year 2024 $19,800, 4th and later year 2021 $5,860, 2020 and 2019 $5,760, footnote 6 (2019 without the special allowance) $10,100; the project's tables carry these values. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].lim_2025 — Limit for a 2025 vehicle
Status: **DISAGREE**

Project: $10,100.00
Model: $12,200.00
Work: No special allowance claimed

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Here the vehicle's key gives the project's value: line 7 reads lim_2025 only for a 2025 vehicle and lim_prior otherwise, and the project looks every limit up by the year actually placed in service and its year of recovery; the model read the 2025 column. Pub. 946 p. 59 table, checked: 1st year 2025 $20,200 (footnote 1: $12,200 without the special allowance), 2nd year 2024 $19,800, 4th and later year 2021 $5,860, 2020 and 2019 $5,760, footnote 6 (2019 without the special allowance) $10,100; the project's tables carry these values. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].lim_prior — Limit for the vehicle's 2025 year of recovery
Status: **AGREE**

Value: $5,760.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **AGREE**

Value: $5,760.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **AGREE**

Value: $4,932.69

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_ok — Section 179 elected for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line10_2025 — Section 179 for a 2025 vehicle: not more than line 9 for a passenger automobile
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].s179_line10 — The section 179 election, not more than line 9
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line11 — Subtract line 10 from line 9
Status: **AGREE**

Value: $4,932.69

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $1,714.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **DISAGREE**

Project: $54,362.82
Model: $54,362.81
Work: 56,076.81 - 1,714

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_full — 100% special allowance
Status: **DISAGREE**

Project: $54,362.82
Model: $54,362.81
Work: 54,362.81 x 100%

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_forty — 40% special allowance
Status: **DISAGREE**

Project: $21,745.13
Model: $21,745.12
Work: 54,362.81 x 40%

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **DISAGREE**

Project: $54,362.82
Model: $54,362.81
Work: Acquired after Jan 19, 2025, so 100%

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_2025 — Special allowance for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line16 — Special depreciation allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **AGREE**

Value: $4,932.69

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line18 — Basis for depreciation (line 15 less line 16)
Status: **DISAGREE**

Project: $54,362.82
Model: $54,362.81
Work: 54,362.81 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq4

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line19_earlier — Line 19 for a vehicle placed in service before 2025 (zero after the recovery per
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].b100 — Cost less the section 179 deduction (as if used 100% for business)
Status: **AGREE**

Value: $63,768.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].r1 — MACRS rate for year 1
Status: **AGREE**

Value: 5%

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].t1 — Year 1 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $3,188.40

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].l1 — Year 1 limit (no special allowance)
Status: **AGREE**

Value: $10,100.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].t1s — Year 1 section 179 deduction plus MACRS amount
Status: **AGREE**

Value: $4,902.40

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].d1 — Year 1 deduction allowable at 100% business use (the lesser of the limit or the 
Status: **AGREE**

Value: $4,902.40

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].r2 — MACRS rate for year 2
Status: **AGREE**

Value: 38%

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].t2 — Year 2 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $24,231.84

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].l2 — Year 2 limit
Status: **AGREE**

Value: $16,100.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].d2 — Year 2 deduction allowable at 100% business use
Status: **AGREE**

Value: $16,100.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].r3 — MACRS rate for year 3
Status: **AGREE**

Value: 22.8%

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].t3 — Year 3 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $14,539.10

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].l3 — Year 3 limit
Status: **AGREE**

Value: $9,700.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].d3 — Year 3 deduction allowable at 100% business use
Status: **AGREE**

Value: $9,700.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].r4 — MACRS rate for year 4
Status: **AGREE**

Value: 13.68%

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].t4 — Year 4 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $8,723.46

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].l4 — Year 4 limit
Status: **AGREE**

Value: $5,760.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].d4 — Year 4 deduction allowable at 100% business use
Status: **AGREE**

Value: $5,760.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].r5 — MACRS rate for year 5
Status: **AGREE**

Value: 10.94%

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].t5 — Year 5 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $6,976.22

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].l5 — Year 5 limit
Status: **AGREE**

Value: $5,760.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].d5 — Year 5 deduction allowable at 100% business use
Status: **AGREE**

Value: $5,760.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].r6 — MACRS rate for year 6
Status: **AGREE**

Value: 9.58%

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].t6 — Year 6 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $6,108.97

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].l6 — Year 6 limit
Status: **AGREE**

Value: $5,760.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].d6 — Year 6 deduction allowable at 100% business use
Status: **AGREE**

Value: $5,760.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].d_total — Deductions allowable during the recovery period at 100% business use
Status: **AGREE**

Value: $47,982.40

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].unrecovered — Unrecovered basis at the end of the recovery period
Status: **AGREE**

Value: $17,499.60

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].post_amount — The lesser of the limit or the unrecovered basis
Status: **AGREE**

Value: $5,760.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].post — 2025 deduction after the recovery period (times the business use percentage)
Status: **AGREE**

Value: $4,932.69

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].too_old — Placed in service before 2019
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_v — Special allowance for this vehicle (line 25)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_pass — Column (h) for a passenger automobile
Status: **AGREE**

Value: $4,932.69

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_heavy — Column (h) for a vehicle not subject to the limits
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_v — Column (h)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].bonus — Line 25: special allowance of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].macrs — Column (h): depreciation of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].s179_2025 — Column (i): elected section 179 cost of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_o — Special allowance (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_o — Depreciation (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_o — Section 179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].q4_basis — Basis for the mid-quarter test when placed in service October to December
Status: **DISAGREE**

Project: $54,362.82
Model: $54,362.81
Work: Q4: line 15 basis after section 179

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_o — mq_q4 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_a2 — mq_q4 of a 2025 vehicle
Status: **DISAGREE**

Project: $54,362.82
Model: $0.00
Work: Not a 2025 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The _o line reads the _a2 copy only for a 2025 vehicle; for this earlier vehicle the _o line and the result are zero (agreeing). Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].mq_total_o — mq_total (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].mq_total_a2 — mq_total of a 2025 vehicle
Status: **DISAGREE**

Project: $54,362.82
Model: $0.00
Work: Not a 2025 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The _o line reads the _a2 copy only for a 2025 vehicle; for this earlier vehicle the _o line and the result are zero (agreeing). Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].cost179_o — cost179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].cost179_a2 — cost179 of a 2025 vehicle
Status: **DISAGREE**

Project: $56,076.82
Model: $0.00
Work: Not a 2025 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The _o line reads the _a2 copy only for a 2025 vehicle; for this earlier vehicle the _o line and the result are zero (agreeing). Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].bm_c — Business miles, as cents
Status: **DISAGREE**

Project: $225.72
Model: $22,572.00
Work: Business miles 22,572

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].cm_c — Commuting miles, as cents
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].om_c — Other miles, as cents
Status: **DISAGREE**

Project: $27.34
Model: $2,734.00
Work: Other miles 2,734

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].nonbusiness_c — Commuting and other miles, as cents
Status: **DISAGREE**

Project: $27.34
Model: $2,734.00
Work: 0 + 2,734

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].total_c — Total miles, as cents
Status: **DISAGREE**

Project: $253.06
Model: $25,306.00
Work: 22,572 + 2,734

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].no_miles — Actual expenses claimed for a vehicle with no miles
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].smr_bad — The standard mileage rate is not available for this vehicle
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].smr_amount — Business miles times the standard mileage rate
Status: **AGREE**

Value: $15,800.40

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line9_standard — Standard mileage amount plus parking fees and tolls
Status: **AGREE**

Value: $15,800.40

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].operating_business — The business portion of the operating expenses
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line9_actual — Business portion of the operating expenses plus parking fees and tolls
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].is_actual_owned — Owned and on actual expenses
Status: **AGREE**

Value: yes

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].is_actual_leased — Leased and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].lease_business — The business portion of the lease payments
Status: **AGREE**

Value: $7,012.61

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].low_use — Business use is 50% or less
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].screened — This vehicle's depreciation is outside this tool
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].year — Year of recovery in 2025
Status: **AGREE**

Value: 5

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].is2025 — Placed in service in 2025
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].is2019 — Placed in service in 2019 (2025 is after the recovery period)
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].bus_cost — Business/investment cost (cost times business use)
Status: **DISAGREE**

Project: $42,373.55
Model: $42,373.56
Work: 47,506 x 22,572/25,306

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].s179_bad — The section 179 election is more than the business cost, or than the SUV limit
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_mixed — The special allowance choice differs within the 5-year class
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].claims_bonus — A special allowance is claimed
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].lim_first_bonus — First-year limit with the special allowance
Status: **DISAGREE**

Project: $5,860.00
Model: $20,200.00
Work: Table 2 footnote: 2025 limit with special allowance

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Here the vehicle's key gives the project's value: line 7 reads lim_2025 only for a 2025 vehicle and lim_prior otherwise, and the project looks every limit up by the year actually placed in service and its year of recovery; the model read the 2025 column. Pub. 946 p. 59 table, checked: 1st year 2025 $20,200 (footnote 1: $12,200 without the special allowance), 2nd year 2024 $19,800, 4th and later year 2021 $5,860, 2020 and 2019 $5,760, footnote 6 (2019 without the special allowance) $10,100; the project's tables carry these values. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].lim_prior — Limit for the vehicle's 2025 year of recovery
Status: **AGREE**

Value: $5,860.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **AGREE**

Value: $5,860.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **AGREE**

Value: $5,226.90

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].s179_2025_ok — Section 179 elected for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line10_2025 — Section 179 for a 2025 vehicle: not more than line 9 for a passenger automobile
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].s179_line10 — The section 179 election, not more than line 9
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line11 — Subtract line 10 from line 9
Status: **AGREE**

Value: $5,226.90

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **DISAGREE**

Project: $42,373.55
Model: $42,373.56
Work: 42,373.56 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_full — 100% special allowance
Status: **DISAGREE**

Project: $42,373.55
Model: $42,373.56
Work: 42,373.56 x 100%

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_forty — 40% special allowance
Status: **AGREE**

Value: $16,949.42

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **DISAGREE**

Project: $42,373.55
Model: $42,373.56
Work: Acquired after Jan 19, 2025, so 100%

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_2025 — Special allowance for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line16 — Special depreciation allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **AGREE**

Value: $5,226.90

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line18 — Basis for depreciation (line 15 less line 16)
Status: **DISAGREE**

Project: $42,373.55
Model: $42,373.56
Work: 42,373.56 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025.vehicle_business_pct in ambiguities/2025.yaml); the model multiplied by the exact fraction, a difference of a few cents. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq3

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].rate_hy — MACRS rate, half-year convention
Status: **DISAGREE**

Project: 11.52%
Model: 20%
Work: 5-year HY, year 1

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The project keys the rate on the vehicle's actual year of recovery (Pub. 946 Table A-1/A-5); the 2025-vehicle rate and line 19 for a 2025 vehicle are not read for a vehicle placed in service earlier, whose line 19 is line19_prior (agreeing or differing only in cents). Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].rate_mq — MACRS rate, mid-quarter convention
Status: **DISAGREE**

Project: 11.3%
Model: 15%
Work: 5-year mid-quarter Q3, year 1

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The project keys the rate on the vehicle's actual year of recovery (Pub. 946 Table A-1/A-5); the 2025-vehicle rate and line 19 for a 2025 vehicle are not read for a vehicle placed in service earlier, whose line 19 is line19_prior (agreeing or differing only in cents). Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].rate_prior — MACRS rate for the 2025 year of recovery
Status: **AGREE**

Value: 11.52%

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line19_hy — Line 18 times the half-year rate
Status: **DISAGREE**

Project: $4,881.43
Model: $8,474.71
Work: 42,373.56 x 20%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The project keys the rate on the vehicle's actual year of recovery (Pub. 946 Table A-1/A-5); the 2025-vehicle rate and line 19 for a 2025 vehicle are not read for a vehicle placed in service earlier, whose line 19 is line19_prior (agreeing or differing only in cents). Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line19_mq — Line 18 times the mid-quarter rate
Status: **DISAGREE**

Project: $4,788.21
Model: $6,356.03
Work: 42,373.56 x 15%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The project keys the rate on the vehicle's actual year of recovery (Pub. 946 Table A-1/A-5); the 2025-vehicle rate and line 19 for a 2025 vehicle are not read for a vehicle placed in service earlier, whose line 19 is line19_prior (agreeing or differing only in cents). Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line19_prior — Line 18 times the rate for the 2025 year of recovery
Status: **AGREE**

Value: $4,881.43

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $4,881.43

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line19_earlier — Line 19 for a vehicle placed in service before 2025 (zero after the recovery per
Status: **AGREE**

Value: $4,881.43

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line19_2025 — Line 19 for a 2025 vehicle, half-year or mid-quarter
Status: **DISAGREE**

Project: $4,788.21
Model: $6,356.03
Work: Mid-quarter test is met, so the MQ amount

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The project keys the rate on the vehicle's actual year of recovery (Pub. 946 Table A-1/A-5); the 2025-vehicle rate and line 19 for a 2025 vehicle are not read for a vehicle placed in service earlier, whose line 19 is line19_prior (agreeing or differing only in cents). Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

Value: $4,881.43

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].b100 — Cost less the section 179 deduction (as if used 100% for business)
Status: **AGREE**

Value: $47,506.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].r1 — MACRS rate for year 1
Status: **AGREE**

Value: 20%

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].t1 — Year 1 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $9,501.20

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].t1s — Year 1 section 179 deduction plus MACRS amount
Status: **AGREE**

Value: $9,501.20

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].r2 — MACRS rate for year 2
Status: **AGREE**

Value: 32%

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].t2 — Year 2 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $15,201.92

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].l2 — Year 2 limit
Status: **AGREE**

Value: $16,400.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].d2 — Year 2 deduction allowable at 100% business use
Status: **AGREE**

Value: $15,201.92

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].r3 — MACRS rate for year 3
Status: **AGREE**

Value: 19.2%

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].t3 — Year 3 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $9,121.15

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].l3 — Year 3 limit
Status: **AGREE**

Value: $9,800.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].d3 — Year 3 deduction allowable at 100% business use
Status: **AGREE**

Value: $9,121.15

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].r4 — MACRS rate for year 4
Status: **AGREE**

Value: 11.52%

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].t4 — Year 4 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $5,472.69

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].l4 — Year 4 limit
Status: **AGREE**

Value: $5,860.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].d4 — Year 4 deduction allowable at 100% business use
Status: **AGREE**

Value: $5,472.69

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].r5 — MACRS rate for year 5
Status: **AGREE**

Value: 11.52%

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].t5 — Year 5 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $5,472.69

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].l5 — Year 5 limit
Status: **AGREE**

Value: $5,860.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].d5 — Year 5 deduction allowable at 100% business use
Status: **AGREE**

Value: $5,472.69

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].r6 — MACRS rate for year 6
Status: **AGREE**

Value: 5.76%

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].t6 — Year 6 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $2,736.35

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].too_old — Placed in service before 2019
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_v — Special allowance for this vehicle (line 25)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].macrs_pass — Column (h) for a passenger automobile
Status: **AGREE**

Value: $4,881.43

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].macrs_heavy — Column (h) for a vehicle not subject to the limits
Status: **AGREE**

Value: $4,881.43

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].macrs_v — Column (h)
Status: **AGREE**

Value: $4,881.43

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].bonus — Line 25: special allowance of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].macrs — Column (h): depreciation of this vehicle
Status: **AGREE**

Value: $4,881.43

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].s179_2025 — Column (i): elected section 179 cost of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_o — Special allowance (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].macrs_o — Depreciation (owned, actual expenses)
Status: **AGREE**

Value: $4,881.43

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].s179_2025_o — Section 179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].q4_basis — Basis for the mid-quarter test when placed in service October to December
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].mq_q4_o — mq_q4 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].mq_q4_a2 — mq_q4 of a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].mq_total_o — mq_total (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].mq_total_a2 — mq_total of a 2025 vehicle
Status: **DISAGREE**

Project: $42,373.55
Model: $0.00
Work: Not a 2025 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The _o line reads the _a2 copy only for a 2025 vehicle; for this earlier vehicle the _o line and the result are zero (agreeing). Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].cost179_o — cost179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].cost179_a2 — cost179 of a 2025 vehicle
Status: **DISAGREE**

Project: $42,373.55
Model: $0.00
Work: Not a 2025 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. The _o line reads the _a2 copy only for a 2025 vehicle; for this earlier vehicle the _o line and the result are zero (agreeing). Not evidence. [dropped]

## Raw responses

### classm.scveh.1

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bm_c"
    value: "23398.00"
    work: "Business miles 23,398"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cm_c"
    value: "0.00"
    work: "Commuting miles 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].om_c"
    value: "921.00"
    work: "Other miles 921"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].nonbusiness_c"
    value: "921.00"
    work: "0 + 921"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].total_c"
    value: "24319.00"
    work: "23,398 + 921"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].no_miles"
    value: "no"
    work: "Total miles are 24,319, not zero"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].over_half"
    value: "yes"
    work: "23,398 / 24,319 = 96.21%, more than 50%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].smr_bad"
    value: "no"
    work: "Filer answered that the standard mileage rate may be used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].smr_amount"
    value: "16378.60"
    work: "23,398 x 0.70"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9_standard"
    value: "16378.60"
    work: "16,378.60 + 0 parking and tolls"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].operating_business"
    value: "0.00"
    work: "0 x 96.21%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9_actual"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9"
    value: "0.00"
    work: "Actual expenses method, so the line 9 actual amount is used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is_actual_owned"
    value: "yes"
    work: "Owned, actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is_actual_leased"
    value: "no"
    work: "Vehicle is owned, not leased"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lease_business"
    value: "5538.97"
    work: "5,757 x 23,398 / 24,319"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20a"
    value: "0.00"
    work: "Not leased, so nothing goes on line 20a"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].low_use"
    value: "no"
    work: "Business use is 96.21%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].screened"
    value: "no"
    work: "None of the screens apply and business use is over 50%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].year"
    value: "1"
    work: "Placed in service 2025, so 2025 is year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is2025"
    value: "yes"
    work: "y2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is2019"
    value: "no"
    work: "y2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bus_cost"
    value: "47144.29"
    work: "49,000 x 23,398 / 24,319 (line 13)"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_bad"
    value: "no"
    work: "Section 179 elected is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_mixed"
    value: "no"
    work: "Same choice applies to all 5-year property"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].claims_bonus"
    value: "yes"
    work: "Filer chose the 40% special allowance"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lim_first_bonus"
    value: "20200.00"
    work: "Table 2 footnote: $20,200 for 2025 with special allowance"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lim_first_none"
    value: "12200.00"
    work: "Table 2: 2025, year 1 = $12,200"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lim_2025"
    value: "20200.00"
    work: "Special allowance claimed"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lim_prior"
    value: "12200.00"
    work: "Table 2 row for 2025, year 1 = $12,200"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line7"
    value: "20200.00"
    work: "2025 vehicle, so the lim_2025 amount is used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9w"
    value: "19434.99"
    work: "20,200 x 23,398 / 24,319"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_ok"
    value: "0.00"
    work: "Elected 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line10"
    value: "0.00"
    work: "0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line10_2025"
    value: "0.00"
    work: "Smaller of 0 or 19,434.99"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_line10"
    value: "0.00"
    work: "Smaller of 0 or line 9"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line11"
    value: "19434.99"
    work: "19,434.99 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line14"
    value: "0.00"
    work: "No section 179 deduction claimed"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line15"
    value: "47144.29"
    work: "47,144.29 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_full"
    value: "47144.29"
    work: "100% x 47,144.29"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_forty"
    value: "18857.72"
    work: "40% x 47,144.29"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_fullcase"
    value: "47144.29"
    work: "Acquired after Jan 19, 2025, so 100%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_2025"
    value: "18857.72"
    work: "Filer elected 40%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line16"
    value: "18857.72"
    work: "Special allowance for a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_allowed"
    value: "18857.72"
    work: "Smaller of 18,857.72 or 19,434.99"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line17"
    value: "577.27"
    work: "19,434.99 - 18,857.72"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line18"
    value: "28286.57"
    work: "47,144.29 - 18,857.72"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].qconv"
    value: "mq4"
    work: "Mid-quarter convention applies; placed in service in Q4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].rate_hy"
    value: "20.00%"
    work: "5-yr 200DB HY, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].rate_mq"
    value: "5.00%"
    work: "40% x 12.5% (Q4), year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].rate_prior"
    value: "5.00%"
    work: "mq4, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_hy"
    value: "5657.31"
    work: "28,286.57 x 20%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_mq"
    value: "1414.33"
    work: "28,286.57 x 5%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_prior"
    value: "1414.33"
    work: "28,286.57 x 5%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19"
    value: "1414.33"
    work: "Mid-quarter convention applies"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_earlier"
    value: "0.00"
    work: "Not placed in service before 2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_2025"
    value: "1414.33"
    work: "MQ amount"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20"
    value: "577.27"
    work: "Lesser of 577.27 or 1,414.33"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].b100"
    value: "49000.00"
    work: "49,000 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r1"
    value: "5.00%"
    work: "mq4 year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t1"
    value: "2450.00"
    work: "49,000 x 5%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].l1"
    value: "12200.00"
    work: "Table 2: 2025, year 1, no special allowance"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t1s"
    value: "2450.00"
    work: "0 + 2,450"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].d1"
    value: "2450.00"
    work: "Lesser of 12,200 or 2,450"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r2"
    value: "38.00%"
    work: "mq4 year 2: 95% x 40%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t2"
    value: "18620.00"
    work: "49,000 x 38%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r3"
    value: "22.80%"
    work: "mq4 year 3"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t3"
    value: "11172.00"
    work: "49,000 x 22.8%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r4"
    value: "13.68%"
    work: "mq4 year 4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t4"
    value: "6703.20"
    work: "49,000 x 13.68%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r5"
    value: "10.94%"
    work: "mq4 year 5 (switch to SL)"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t5"
    value: "5360.60"
    work: "49,000 x 10.94%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r6"
    value: "9.58%"
    work: "mq4 year 6"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t6"
    value: "4694.20"
    work: "49,000 x 9.58%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].too_old"
    value: "no"
    work: "Placed in service 2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_v"
    value: "18857.72"
    work: "Allowed special allowance"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_pass"
    value: "577.27"
    work: "Line 20"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_heavy"
    value: "1414.33"
    work: "Line 19"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_v"
    value: "577.27"
    work: "Subject to the passenger automobile limits"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus"
    value: "18857.72"
    work: "Owned, actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs"
    value: "577.27"
    work: "Owned, actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_2025"
    value: "0.00"
    work: "None elected"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_q4"
    value: "47144.29"
    work: "Q4 2025 business basis less 0 section 179"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_total"
    value: "47144.29"
    work: "2025 business basis"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cost179"
    value: "47144.29"
    work: "Business cost of listed property placed in service 2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_o"
    value: "18857.72"
    work: "Owned, actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_o"
    value: "577.27"
    work: "Owned, actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_o"
    value: "0.00"
    work: "0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].q4_basis"
    value: "47144.29"
    work: "Placed in service in Q4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_o"
    value: "47144.29"
    work: "Owned, actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_a2"
    value: "47144.29"
    work: "2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_total_o"
    value: "47144.29"
    work: "Owned, actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_total_a2"
    value: "47144.29"
    work: "2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cost179_o"
    value: "47144.29"
    work: "Owned, actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cost179_a2"
    value: "47144.29"
    work: "2025 vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bm_c"
    value: "12306.00"
    work: "Business miles 12,306"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].cm_c"
    value: "0.00"
    work: "Commuting miles 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].om_c"
    value: "7964.00"
    work: "Other miles 7,964"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].nonbusiness_c"
    value: "7964.00"
    work: "0 + 7,964"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].total_c"
    value: "20270.00"
    work: "12,306 + 7,964"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].no_miles"
    value: "no"
    work: "Total miles are 20,270, not zero"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].over_half"
    value: "yes"
    work: "12,306 / 20,270 = 60.71%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].smr_bad"
    value: "no"
    work: "Filer answered that the standard mileage rate may be used"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].smr_amount"
    value: "8614.20"
    work: "12,306 x 0.70"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line9_standard"
    value: "9614.20"
    work: "8,614.20 + 1,000"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].operating_business"
    value: "6071.04"
    work: "10,000 x 12,306 / 20,270"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line9_actual"
    value: "7071.04"
    work: "6,071.04 + 1,000"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line9"
    value: "7071.04"
    work: "Actual expenses method"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].is_actual_owned"
    value: "no"
    work: "Vehicle is leased"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].is_actual_leased"
    value: "yes"
    work: "Leased, actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].lease_business"
    value: "1761.21"
    work: "2,901 x 12,306 / 20,270"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line20a"
    value: "1761.21"
    work: "Leased, actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].low_use"
    value: "no"
    work: "Business use is 60.71%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].screened"
    value: "no"
    work: "No screen applies"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].year"
    value: "7"
    work: "2025 - 2019 + 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].is2025"
    value: "no"
    work: "y2019"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].is2019"
    value: "yes"
    work: "y2019"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bus_cost"
    value: "6673.90"
    work: "10,993 x 12,306 / 20,270"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].s179_bad"
    value: "no"
    work: "Section 179 elected is 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_mixed"
    value: "no"
    work: "Same choice applies to all 5-year property"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].claims_bonus"
    value: "no"
    work: "Special allowance choice is none"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].lim_first_bonus"
    value: "20200.00"
    work: "Table 2 footnote"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].lim_first_none"
    value: "12200.00"
    work: "Table 2: 2025, year 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].lim_2025"
    value: "12200.00"
    work: "No special allowance claimed"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].lim_prior"
    value: "5760.00"
    work: "Table 2: 2019, 4 or more years = $5,760"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line7"
    value: "5760.00"
    work: "Prior-year vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line9w"
    value: "3496.92"
    work: "5,760 x 12,306 / 20,270"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].s179_2025_ok"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line10"
    value: "0.00"
    work: "Not the year placed in service"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line10_2025"
    value: "0.00"
    work: "0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].s179_line10"
    value: "0.00"
    work: "0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line11"
    value: "3496.92"
    work: "3,496.92 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line14"
    value: "0.00"
    work: "No section 179 deduction claimed"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line15"
    value: "6673.90"
    work: "6,673.90 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_full"
    value: "6673.90"
    work: "100% x 6,673.90"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_forty"
    value: "2669.56"
    work: "40% x 6,673.90"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_fullcase"
    value: "6673.90"
    work: "Marked acquired after Jan 19, 2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_2025"
    value: "0.00"
    work: "None claimed; not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line16"
    value: "0.00"
    work: "Not the year placed in service"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_allowed"
    value: "0.00"
    work: "0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line17"
    value: "3496.92"
    work: "3,496.92 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line18"
    value: "6673.90"
    work: "6,673.90 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].qconv"
    value: "mq4"
    work: "Convention used is mq4"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line19"
    value: "0.00"
    work: "Year 7 is after the 5-year recovery period"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line19_earlier"
    value: "0.00"
    work: "After the recovery period"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line20"
    value: "0.00"
    work: "Lesser of 3,496.92 or 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].b100"
    value: "10993.00"
    work: "10,993 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].r1"
    value: "5.00%"
    work: "mq4 year 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].t1"
    value: "549.65"
    work: "10,993 x 5%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].l1"
    value: "10100.00"
    work: "2019, year 1, no special allowance"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].t1s"
    value: "549.65"
    work: "0 + 549.65"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].d1"
    value: "549.65"
    work: "Lesser of 10,100 or 549.65"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].r2"
    value: "38.00%"
    work: "mq4 year 2"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].t2"
    value: "4177.34"
    work: "10,993 x 38%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].l2"
    value: "16100.00"
    work: "2019, year 2"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].d2"
    value: "4177.34"
    work: "Lesser of 16,100 or 4,177.34"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].r3"
    value: "22.80%"
    work: "mq4 year 3"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].t3"
    value: "2506.40"
    work: "10,993 x 22.8%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].l3"
    value: "9700.00"
    work: "2019, year 3"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].d3"
    value: "2506.40"
    work: "Lesser of 9,700 or 2,506.40"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].r4"
    value: "13.68%"
    work: "mq4 year 4"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].t4"
    value: "1503.84"
    work: "10,993 x 13.68%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].l4"
    value: "5760.00"
    work: "2019, 4th year"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].d4"
    value: "1503.84"
    work: "Lesser of 5,760 or 1,503.84"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].r5"
    value: "10.94%"
    work: "mq4 year 5"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].t5"
    value: "1202.63"
    work: "10,993 x 10.94%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].l5"
    value: "5760.00"
    work: "2019, later year"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].d5"
    value: "1202.63"
    work: "Lesser of 5,760 or 1,202.63"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].r6"
    value: "9.58%"
    work: "mq4 year 6"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].t6"
    value: "1053.13"
    work: "10,993 x 9.58%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].l6"
    value: "5760.00"
    work: "2019, later year"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].d6"
    value: "1053.13"
    work: "Lesser of 5,760 or 1,053.13"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].d_total"
    value: "10992.99"
    work: "Sum of d1 through d6"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].unrecovered"
    value: "0.01"
    work: "10,993 - 10,992.99"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].post_amount"
    value: "0.01"
    work: "Lesser of 5,760 or 0.01"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].post"
    value: "0.01"
    work: "0.01 x 60.71%, rounded"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].too_old"
    value: "no"
    work: "2019 is not before 2019"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_v"
    value: "0.00"
    work: "No special allowance"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].macrs_pass"
    value: "0.01"
    work: "Unrecovered-basis amount after the recovery period"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].macrs_heavy"
    value: "0.00"
    work: "No deduction after the recovery period for non-limited property"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].macrs_v"
    value: "0.00"
    work: "Not subject to the passenger automobile limits"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus"
    value: "0.00"
    work: "Leased, so no depreciation"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].macrs"
    value: "0.00"
    work: "Leased, so no depreciation"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].s179_2025"
    value: "0.00"
    work: "Leased"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].mq_q4"
    value: "0.00"
    work: "Leased and not placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].mq_total"
    value: "0.00"
    work: "Leased and not placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].cost179"
    value: "0.00"
    work: "Leased and not placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_o"
    value: "0.00"
    work: "Not owned"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].macrs_o"
    value: "0.00"
    work: "Not owned"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].s179_2025_o"
    value: "0.00"
    work: "Not owned"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].q4_basis"
    value: "0.00"
    work: "Placed in service in Q1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].mq_q4_o"
    value: "0.00"
    work: "Not owned"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].mq_q4_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].mq_total_o"
    value: "0.00"
    work: "Not owned"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].mq_total_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].cost179_o"
    value: "0.00"
    work: "Not owned"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].cost179_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bm_c"
    value: "29999.00"
    work: "Business miles 29,999"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].cm_c"
    value: "0.00"
    work: "Commuting miles 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].om_c"
    value: "1709.00"
    work: "Other miles 1,709"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].nonbusiness_c"
    value: "1709.00"
    work: "0 + 1,709"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].total_c"
    value: "31708.00"
    work: "29,999 + 1,709"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].no_miles"
    value: "no"
    work: "Total miles are 31,708, not zero"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].over_half"
    value: "yes"
    work: "29,999 / 31,708 = 94.61%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].smr_bad"
    value: "no"
    work: "Filer answered that the standard mileage rate may be used"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].smr_amount"
    value: "20999.30"
    work: "29,999 x 0.70"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line9_standard"
    value: "20999.30"
    work: "20,999.30 + 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].operating_business"
    value: "673.62"
    work: "712 x 29,999 / 31,708"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line9_actual"
    value: "673.62"
    work: "673.62 + 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line9"
    value: "673.62"
    work: "Actual expenses method"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].is_actual_owned"
    value: "yes"
    work: "Owned, actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].is_actual_leased"
    value: "no"
    work: "Vehicle is owned"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].lease_business"
    value: "6957.63"
    work: "7,354 x 29,999 / 31,708"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line20a"
    value: "0.00"
    work: "Not leased"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].low_use"
    value: "no"
    work: "Business use is 94.61%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].screened"
    value: "no"
    work: "No screen applies"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].year"
    value: "5"
    work: "2025 - 2021 + 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].is2025"
    value: "no"
    work: "y2021"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].is2019"
    value: "no"
    work: "y2021"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bus_cost"
    value: "70806.27"
    work: "74,840 x 29,999 / 31,708"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].s179_bad"
    value: "no"
    work: "Section 179 elected is 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_mixed"
    value: "no"
    work: "Same choice applies to all 5-year property"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].claims_bonus"
    value: "no"
    work: "Special allowance choice is none"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].lim_first_bonus"
    value: "20200.00"
    work: "Table 2 footnote"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].lim_prior"
    value: "5860.00"
    work: "Table 2: 2021, 4 or more years = $5,860"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line7"
    value: "5860.00"
    work: "Prior-year vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line9w"
    value: "5544.16"
    work: "5,860 x 29,999 / 31,708"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].s179_2025_ok"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line10"
    value: "0.00"
    work: "Not the year placed in service"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line10_2025"
    value: "0.00"
    work: "0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].s179_line10"
    value: "0.00"
    work: "0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line11"
    value: "5544.16"
    work: "5,544.16 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line14"
    value: "0.00"
    work: "No section 179 deduction claimed"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line15"
    value: "70806.27"
    work: "70,806.27 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_full"
    value: "70806.27"
    work: "100% x 70,806.27"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_forty"
    value: "28322.51"
    work: "40% x 70,806.27"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_fullcase"
    value: "28322.51"
    work: "Not acquired after Jan 19, 2025, so 40%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_2025"
    value: "0.00"
    work: "Not a 2025 vehicle; none claimed"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line16"
    value: "0.00"
    work: "Not the year placed in service"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_allowed"
    value: "0.00"
    work: "0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line17"
    value: "5544.16"
    work: "5,544.16 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line18"
    value: "70806.27"
    work: "70,806.27 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].qconv"
    value: "mq4"
    work: "Convention used is mq4"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].rate_hy"
    value: "11.52%"
    work: "5-yr HY, year 5"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].rate_mq"
    value: "10.94%"
    work: "5-yr mq4, year 5"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].rate_prior"
    value: "10.94%"
    work: "mq4, year 5"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line19_hy"
    value: "8156.88"
    work: "70,806.27 x 11.52%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line19_mq"
    value: "7746.21"
    work: "70,806.27 x 10.94%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line19_prior"
    value: "7746.21"
    work: "70,806.27 x 10.94%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line19"
    value: "7746.21"
    work: "Prior-year rate"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line19_earlier"
    value: "7746.21"
    work: "Within the recovery period"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line19_2025"
    value: "7746.21"
    work: "MQ amount"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line20"
    value: "5544.16"
    work: "Lesser of 5,544.16 or 7,746.21"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].b100"
    value: "74840.00"
    work: "74,840 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].r1"
    value: "5.00%"
    work: "mq4 year 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].t1"
    value: "3742.00"
    work: "74,840 x 5%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].t1s"
    value: "3742.00"
    work: "0 + 3,742"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].r2"
    value: "38.00%"
    work: "mq4 year 2"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].t2"
    value: "28439.20"
    work: "74,840 x 38%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].l2"
    value: "16400.00"
    work: "2021, year 2"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].d2"
    value: "16400.00"
    work: "Lesser of 16,400 or 28,439.20"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].r3"
    value: "22.80%"
    work: "mq4 year 3"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].t3"
    value: "17063.52"
    work: "74,840 x 22.8%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].l3"
    value: "9800.00"
    work: "2021, year 3"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].d3"
    value: "9800.00"
    work: "Lesser of 9,800 or 17,063.52"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].r4"
    value: "13.68%"
    work: "mq4 year 4"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].t4"
    value: "10238.11"
    work: "74,840 x 13.68%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].l4"
    value: "5860.00"
    work: "2021, 4th year"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].d4"
    value: "5860.00"
    work: "Lesser of 5,860 or 10,238.11"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].r5"
    value: "10.94%"
    work: "mq4 year 5"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].t5"
    value: "8187.50"
    work: "74,840 x 10.94%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].l5"
    value: "5860.00"
    work: "2021, later year"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].d5"
    value: "5860.00"
    work: "Lesser of 5,860 or 8,187.50"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].r6"
    value: "9.58%"
    work: "mq4 year 6"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].t6"
    value: "7169.67"
    work: "74,840 x 9.58%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].too_old"
    value: "no"
    work: "Placed in service 2021"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_v"
    value: "0.00"
    work: "No special allowance"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].macrs_pass"
    value: "5544.16"
    work: "Line 20"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].macrs_heavy"
    value: "7746.21"
    work: "Line 19"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].macrs_v"
    value: "7746.21"
    work: "Not subject to the passenger automobile limits"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus"
    value: "0.00"
    work: "No special allowance"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].macrs"
    value: "7746.21"
    work: "Owned, actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].s179_2025"
    value: "0.00"
    work: "None elected"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].mq_q4"
    value: "0.00"
    work: "Not placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].mq_total"
    value: "0.00"
    work: "Not placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].cost179"
    value: "0.00"
    work: "Not placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_o"
    value: "0.00"
    work: "0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].macrs_o"
    value: "7746.21"
    work: "Owned, actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].s179_2025_o"
    value: "0.00"
    work: "0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].q4_basis"
    value: "70806.27"
    work: "Quarter marked q4; business basis less 0 section 179"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].mq_q4_o"
    value: "70806.27"
    work: "Owned, actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].mq_q4_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].mq_total_o"
    value: "70806.27"
    work: "Owned, actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].mq_total_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].cost179_o"
    value: "70806.27"
    work: "Owned, actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].cost179_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
```
```

### classm.scveh.2

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bm_c"
    value: "25942.00"
    work: "Business miles 25,942"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cm_c"
    value: "861.00"
    work: "Commuting miles 861"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].om_c"
    value: "1790.00"
    work: "Other miles 1,790"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].nonbusiness_c"
    value: "2651.00"
    work: "861 + 1,790"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].total_c"
    value: "28593.00"
    work: "25,942 + 2,651"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].no_miles"
    value: "no"
    work: "Total miles are more than 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].over_half"
    value: "yes"
    work: "25,942/28,593 = 90.73% > 50%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].smr_bad"
    value: "no"
    work: "Filer says the standard mileage rate may be used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].smr_amount"
    value: "18159.40"
    work: "25,942 x 0.70"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9_standard"
    value: "18159.40"
    work: "18,159.40 + 0 parking/tolls"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].operating_business"
    value: "0.00"
    work: "0 x 90.73%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9_actual"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9"
    value: "0.00"
    work: "Actual expenses method"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is_actual_owned"
    value: "yes"
    work: "Owned; actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is_actual_leased"
    value: "no"
    work: "Owned, not leased"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lease_business"
    value: "0.00"
    work: "No lease payments"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20a"
    value: "0.00"
    work: "Not leased"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].low_use"
    value: "no"
    work: "Business use is 90.73%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].screened"
    value: "no"
    work: "No screening condition applies"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].year"
    value: "7"
    work: "2019 is year 1, so 2025 is year 7"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is2025"
    value: "no"
    work: "Placed in service in 2019"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is2019"
    value: "yes"
    work: "Year placed in service is y2019"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bus_cost"
    value: "14313.33"
    work: "15,776 x 25,942/28,593"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_bad"
    value: "no"
    work: "Section 179 elected is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_mixed"
    value: "no"
    work: "Same choice for all 5-year property"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].claims_bonus"
    value: "no"
    work: "Special allowance is none"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lim_first_bonus"
    value: "20200.00"
    work: "Table 2 footnote: 2025 limit with special allowance"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lim_first_none"
    value: "12200.00"
    work: "Table 2: 2025 year 1 limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lim_2025"
    value: "12200.00"
    work: "No special allowance claimed"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lim_prior"
    value: "5760.00"
    work: "2019 vehicle, 4th and later year limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line7"
    value: "5760.00"
    work: "Limit for year 7 of a 2019 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9w"
    value: "5225.96"
    work: "5,760 x 25,942/28,593"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_ok"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line10"
    value: "0.00"
    work: "Not the year placed in service"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line10_2025"
    value: "0.00"
    work: "Section 179 elected is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_line10"
    value: "0.00"
    work: "Smaller of 0 or line 9"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line11"
    value: "5225.96"
    work: "5,225.96 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line14"
    value: "0.00"
    work: "No section 179 deduction in 2019"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line15"
    value: "14313.33"
    work: "14,313.33 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_full"
    value: "14313.33"
    work: "14,313.33 x 100%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_forty"
    value: "5725.33"
    work: "14,313.33 x 40%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_fullcase"
    value: "14313.33"
    work: "Acquired after Jan 19, 2025, so 100%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_2025"
    value: "0.00"
    work: "Special allowance not claimed"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line16"
    value: "0.00"
    work: "Not the year placed in service"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_allowed"
    value: "0.00"
    work: "Smaller of 0 or line 11"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line17"
    value: "5225.96"
    work: "5,225.96 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line18"
    value: "14313.33"
    work: "14,313.33 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].qconv"
    value: "mq3"
    work: "Placed in service in quarter 3"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19"
    value: "0.00"
    work: "Year 7 is after the 5-year recovery period"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_earlier"
    value: "0.00"
    work: "After the recovery period"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20"
    value: "0.00"
    work: "Lesser of 5,225.96 or 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].b100"
    value: "15776.00"
    work: "15,776 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r1"
    value: "35.00%"
    work: "5-year 200DB, mid-quarter Q1, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t1"
    value: "5521.60"
    work: "15,776 x 35%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].l1"
    value: "10100.00"
    work: "2019 year 1 limit without special allowance"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t1s"
    value: "5521.60"
    work: "0 + 5,521.60"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].d1"
    value: "5521.60"
    work: "Lesser of 10,100 or 5,521.60"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r2"
    value: "26.00%"
    work: "Mid-quarter Q1, year 2"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t2"
    value: "4101.76"
    work: "15,776 x 26%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].l2"
    value: "16100.00"
    work: "2019 vehicle, year 2"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].d2"
    value: "4101.76"
    work: "Lesser of the limit or the amount"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r3"
    value: "15.60%"
    work: "Mid-quarter Q1, year 3"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t3"
    value: "2461.06"
    work: "15,776 x 15.60%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].l3"
    value: "9700.00"
    work: "2019 vehicle, year 3"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].d3"
    value: "2461.06"
    work: "Lesser of the limit or the amount"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r4"
    value: "11.01%"
    work: "Mid-quarter Q1, year 4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t4"
    value: "1736.94"
    work: "15,776 x 11.01%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].l4"
    value: "5760.00"
    work: "2019 vehicle, 4th and later years"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].d4"
    value: "1736.94"
    work: "Lesser of the limit or the amount"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r5"
    value: "11.01%"
    work: "Mid-quarter Q1, year 5"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t5"
    value: "1736.94"
    work: "15,776 x 11.01%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].l5"
    value: "5760.00"
    work: "2019 vehicle, 4th and later years"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].d5"
    value: "1736.94"
    work: "Lesser of the limit or the amount"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r6"
    value: "1.38%"
    work: "Mid-quarter Q1, year 6"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t6"
    value: "217.71"
    work: "15,776 x 1.38%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].l6"
    value: "5760.00"
    work: "2019 vehicle, 4th and later years"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].d6"
    value: "217.71"
    work: "Lesser of the limit or the amount"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].d_total"
    value: "15776.01"
    work: "Sum of d1 through d6"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].unrecovered"
    value: "0.00"
    work: "15,776 - 15,776.01, which is less than zero, so 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].post_amount"
    value: "0.00"
    work: "Lesser of 5,760 or 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].post"
    value: "0.00"
    work: "0 x 90.73%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].too_old"
    value: "no"
    work: "Placed in service in 2019"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_v"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_pass"
    value: "0.00"
    work: "Post-recovery amount is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_heavy"
    value: "0.00"
    work: "Recovery period has ended"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_v"
    value: "0.00"
    work: "Passenger automobile"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus"
    value: "0.00"
    work: "bonus_v"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs"
    value: "0.00"
    work: "macrs_v"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_2025"
    value: "0.00"
    work: "No section 179 election"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_q4"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_total"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cost179"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_o"
    value: "0.00"
    work: "bonus"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_o"
    value: "0.00"
    work: "macrs"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_o"
    value: "0.00"
    work: "s179_2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].q4_basis"
    value: "0.00"
    work: "Placed in service in Q3, not Q4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_o"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_a2"
    value: "0.00"
    work: "q4_basis is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_total_o"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_total_a2"
    value: "14313.33"
    work: "Business cost 14,313.33 - section 179 of 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cost179_o"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cost179_a2"
    value: "14313.33"
    work: "Business cost"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bm_c"
    value: "12462.00"
    work: "Business miles 12,462"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].cm_c"
    value: "0.00"
    work: "Commuting miles 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].om_c"
    value: "937.00"
    work: "Other miles 937"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].nonbusiness_c"
    value: "937.00"
    work: "0 + 937"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].total_c"
    value: "13399.00"
    work: "12,462 + 937"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].no_miles"
    value: "no"
    work: "Total miles are more than 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].over_half"
    value: "yes"
    work: "12,462/13,399 = 93.01% > 50%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].smr_bad"
    value: "no"
    work: "Filer says the standard mileage rate may be used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].smr_amount"
    value: "8723.40"
    work: "12,462 x 0.70"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9_standard"
    value: "8723.40"
    work: "8,723.40 + 0 parking/tolls"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].operating_business"
    value: "1506.71"
    work: "1,620 x 12,462/13,399"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9_actual"
    value: "1506.71"
    work: "1,506.71 + 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9"
    value: "1506.71"
    work: "Actual expenses method"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].is_actual_owned"
    value: "yes"
    work: "Owned; actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].is_actual_leased"
    value: "no"
    work: "Owned, not leased"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].lease_business"
    value: "0.00"
    work: "No lease payments"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line20a"
    value: "0.00"
    work: "Not leased"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].low_use"
    value: "no"
    work: "Business use is 93.01%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].screened"
    value: "no"
    work: "No screening condition applies"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].year"
    value: "1"
    work: "Placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].is2025"
    value: "yes"
    work: "Year placed in service is y2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].is2019"
    value: "no"
    work: "Placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bus_cost"
    value: "47544.22"
    work: "51,119 x 12,462/13,399"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].s179_bad"
    value: "no"
    work: "Section 179 elected is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_mixed"
    value: "no"
    work: "Same choice for all 5-year property"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].claims_bonus"
    value: "yes"
    work: "Special allowance is full"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].lim_first_bonus"
    value: "20200.00"
    work: "Table 2 footnote: 2025 limit with special allowance"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].lim_first_none"
    value: "12200.00"
    work: "Table 2: 2025 year 1 limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].lim_2025"
    value: "20200.00"
    work: "Special allowance claimed"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].lim_prior"
    value: "20200.00"
    work: "Year 1 of a 2025 vehicle with special allowance"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line7"
    value: "20200.00"
    work: "lim_2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9w"
    value: "18787.40"
    work: "20,200 x 12,462/13,399"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].s179_2025_ok"
    value: "0.00"
    work: "Section 179 elected is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line10"
    value: "0.00"
    work: "Smaller of 0 or line 9"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line10_2025"
    value: "0.00"
    work: "Smaller of 0 or line 9"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].s179_line10"
    value: "0.00"
    work: "Smaller of 0 or line 9"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line11"
    value: "18787.40"
    work: "18,787.40 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line14"
    value: "0.00"
    work: "No section 179 deduction"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line15"
    value: "47544.22"
    work: "47,544.22 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_full"
    value: "47544.22"
    work: "47,544.22 x 100%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_forty"
    value: "19017.69"
    work: "47,544.22 x 40%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_fullcase"
    value: "47544.22"
    work: "Acquired after Jan 19, 2025, so 100%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_2025"
    value: "47544.22"
    work: "Special allowance claimed (full)"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line16"
    value: "47544.22"
    work: "Placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_allowed"
    value: "18787.40"
    work: "Smaller of 47,544.22 or line 11 of 18,787.40"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line17"
    value: "0.00"
    work: "18,787.40 - 47,544.22, which is less than zero, so 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line18"
    value: "0.00"
    work: "47,544.22 - 47,544.22"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].qconv"
    value: "mq2"
    work: "Placed in service in quarter 2"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].rate_hy"
    value: "20.00%"
    work: "5-year 200DB half-year, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].rate_mq"
    value: "25.00%"
    work: "5-year 200DB mid-quarter Q2, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].rate_prior"
    value: "5.00%"
    work: "Given convention mq4, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19_hy"
    value: "0.00"
    work: "0 x 20%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19_mq"
    value: "0.00"
    work: "0 x 25%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19_prior"
    value: "0.00"
    work: "0 x 5%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19"
    value: "0.00"
    work: "Line 18 is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19_earlier"
    value: "0.00"
    work: "Not placed in service before 2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19_2025"
    value: "0.00"
    work: "Mid-quarter test is no, so half-year: 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line20"
    value: "0.00"
    work: "Lesser of 0 or 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].b100"
    value: "51119.00"
    work: "51,119 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r1"
    value: "5.00%"
    work: "Mid-quarter Q4 (given), year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t1"
    value: "2555.95"
    work: "51,119 x 5%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].l1"
    value: "12200.00"
    work: "2025 year 1 limit without special allowance"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t1s"
    value: "2555.95"
    work: "0 + 2,555.95"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].d1"
    value: "2555.95"
    work: "Lesser of 12,200 or 2,555.95"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r2"
    value: "38.00%"
    work: "Mid-quarter Q4, year 2"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t2"
    value: "19425.22"
    work: "51,119 x 38%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r3"
    value: "22.80%"
    work: "Mid-quarter Q4, year 3"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t3"
    value: "11655.13"
    work: "51,119 x 22.80%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r4"
    value: "13.68%"
    work: "Mid-quarter Q4, year 4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t4"
    value: "6993.08"
    work: "51,119 x 13.68%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r5"
    value: "10.94%"
    work: "Mid-quarter Q4, year 5"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t5"
    value: "5592.42"
    work: "51,119 x 10.94%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r6"
    value: "9.58%"
    work: "Mid-quarter Q4, year 6"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t6"
    value: "4897.20"
    work: "51,119 x 9.58%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].too_old"
    value: "no"
    work: "Placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_v"
    value: "18787.40"
    work: "bonus_allowed"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].macrs_pass"
    value: "0.00"
    work: "Line 20"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].macrs_heavy"
    value: "0.00"
    work: "line19_2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].macrs_v"
    value: "0.00"
    work: "Passenger automobile"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus"
    value: "18787.40"
    work: "bonus_v"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].macrs"
    value: "0.00"
    work: "macrs_v"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].s179_2025"
    value: "0.00"
    work: "No section 179 election"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_q4"
    value: "0.00"
    work: "Placed in service in Q2"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_total"
    value: "47544.22"
    work: "Business cost - section 179 of 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].cost179"
    value: "47544.22"
    work: "Business cost of listed property"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_o"
    value: "18787.40"
    work: "Owned, actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].macrs_o"
    value: "0.00"
    work: "Owned, actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].s179_2025_o"
    value: "0.00"
    work: "Owned, actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].q4_basis"
    value: "0.00"
    work: "Placed in service in Q2, not Q4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_q4_o"
    value: "0.00"
    work: "q4_basis is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_q4_a2"
    value: "0.00"
    work: "q4_basis is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_total_o"
    value: "47544.22"
    work: "2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_total_a2"
    value: "47544.22"
    work: "47,544.22 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].cost179_o"
    value: "47544.22"
    work: "2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].cost179_a2"
    value: "47544.22"
    work: "Business cost"
```
```

### classm.scveh.3

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bm_c"
    value: "26610.00"
    work: "Business miles 26,610"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cm_c"
    value: "0.00"
    work: "Commuting miles 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].om_c"
    value: "3336.00"
    work: "Other miles 3,336"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].nonbusiness_c"
    value: "3336.00"
    work: "0 + 3,336"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].total_c"
    value: "29946.00"
    work: "26,610 + 3,336"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].no_miles"
    value: "no"
    work: "Standard mileage rate is used and miles are reported"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].over_half"
    value: "yes"
    work: "26,610 / 29,946 = 88.86%, which is more than 50%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].smr_bad"
    value: "no"
    work: "Filer says the standard mileage rate may be used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].smr_amount"
    value: "18627.00"
    work: "26,610 x 0.70"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9_standard"
    value: "18627.00"
    work: "18,627.00 + 0 parking and tolls"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].operating_business"
    value: "7129.23"
    work: "8,023 x 26,610 / 29,946"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9_actual"
    value: "7129.23"
    work: "7,129.23 + 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9"
    value: "18627.00"
    work: "Standard method chosen, so the standard amount is used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is_actual_owned"
    value: "no"
    work: "Standard mileage rate is used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is_actual_leased"
    value: "no"
    work: "Vehicle is owned and the standard rate is used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lease_business"
    value: "5243.63"
    work: "5,901 x 26,610 / 29,946"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20a"
    value: "0.00"
    work: "Not leased, and with the standard rate no lease payments are deducted"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].low_use"
    value: "no"
    work: "88.86% is more than 50%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].screened"
    value: "no"
    work: "Filer answered no to the screening question"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].year"
    value: "7"
    work: "Placed in service 2019, so 2025 is year 7"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is2025"
    value: "no"
    work: "Placed in service 2019"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is2019"
    value: "yes"
    work: "Placed in service 2019"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bus_cost"
    value: "48214.52"
    work: "Worksheet line 13: 54,259 x 26,610 / 29,946"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_bad"
    value: "no"
    work: "Elected 0, which is not more than the business cost"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_mixed"
    value: "no"
    work: "Choice is the same for all 5-year property"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].claims_bonus"
    value: "no"
    work: "Special allowance = none"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lim_first_bonus"
    value: "20200.00"
    work: "Table 2 footnote: 2025 limit with the special allowance"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lim_first_none"
    value: "12200.00"
    work: "Table 2: 2025, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lim_2025"
    value: "12200.00"
    work: "No special allowance claimed"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lim_prior"
    value: "5760.00"
    work: "Table 2: 2019, 4 or more years"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line7"
    value: "5760.00"
    work: "Prior-year vehicle limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9w"
    value: "5118.33"
    work: "5,760 x 26,610 / 29,946"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_ok"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line10"
    value: "0.00"
    work: "Not the year placed in service"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line10_2025"
    value: "0.00"
    work: "Elected 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_line10"
    value: "0.00"
    work: "Smaller of 0 or 5,118.33"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line11"
    value: "5118.33"
    work: "5,118.33 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line14"
    value: "9850.00"
    work: "Section 179 claimed in 2019, as given"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line15"
    value: "38364.52"
    work: "48,214.52 - 9,850"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_full"
    value: "38364.52"
    work: "38,364.52 x 100%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_forty"
    value: "15345.81"
    work: "38,364.52 x 40%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_fullcase"
    value: "38364.52"
    work: "Acquired after January 19, 2025 = yes, so 100%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_2025"
    value: "0.00"
    work: "No allowance claimed and not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line16"
    value: "0.00"
    work: "Enter -0- if not the year placed in service"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_allowed"
    value: "0.00"
    work: "Smaller of 0 or line 11"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line17"
    value: "5118.33"
    work: "5,118.33 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line18"
    value: "38364.52"
    work: "38,364.52 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].qconv"
    value: "mq1"
    work: "Placed in service in quarter 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19"
    value: "0.00"
    work: "Year 7 is after the 5-year recovery period, so the rate is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_earlier"
    value: "0.00"
    work: "After the recovery period"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20"
    value: "0.00"
    work: "Lesser of 5,118.33 or 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].b100"
    value: "44409.00"
    work: "54,259 - 9,850"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r1"
    value: "20.00%"
    work: "5-year, 200DB, half-year convention, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t1"
    value: "8881.80"
    work: "44,409 x 20%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].l1"
    value: "10100.00"
    work: "2019 first-year limit without the special allowance (footnote 6)"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t1s"
    value: "18731.80"
    work: "9,850 + 8,881.80"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].d1"
    value: "10100.00"
    work: "Lesser of 10,100 or 18,731.80"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r2"
    value: "32.00%"
    work: "HY table, year 2"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t2"
    value: "14210.88"
    work: "44,409 x 32%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].l2"
    value: "16100.00"
    work: "2019, 2nd year"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].d2"
    value: "14210.88"
    work: "Lesser of the limit or the amount"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r3"
    value: "19.20%"
    work: "HY table, year 3"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t3"
    value: "8526.53"
    work: "44,409 x 19.2%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].l3"
    value: "9700.00"
    work: "2019, 3rd year"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].d3"
    value: "8526.53"
    work: "Lesser of the limit or the amount"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r4"
    value: "11.52%"
    work: "HY table, year 4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t4"
    value: "5115.92"
    work: "44,409 x 11.52%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].l4"
    value: "5760.00"
    work: "2019, 4th and later years"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].d4"
    value: "5115.92"
    work: "Lesser of the limit or the amount"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r5"
    value: "11.52%"
    work: "HY table, year 5"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t5"
    value: "5115.92"
    work: "44,409 x 11.52%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].l5"
    value: "5760.00"
    work: "2019, later years"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].d5"
    value: "5115.92"
    work: "Lesser of the limit or the amount"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r6"
    value: "5.76%"
    work: "HY table, year 6"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t6"
    value: "2557.96"
    work: "44,409 x 5.76%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].l6"
    value: "5760.00"
    work: "2019, later years"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].d6"
    value: "2557.96"
    work: "Lesser of the limit or the amount"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].d_total"
    value: "45627.21"
    work: "Sum of d1 through d6"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].unrecovered"
    value: "8631.79"
    work: "54,259 - 45,627.21"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].post_amount"
    value: "5760.00"
    work: "Lesser of 5,760 or 8,631.79"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].post"
    value: "5118.33"
    work: "5,760 x 26,610 / 29,946"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].too_old"
    value: "no"
    work: "Placed in service in 2019, not before"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_v"
    value: "0.00"
    work: "No special allowance"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_pass"
    value: "5118.33"
    work: "Line 20 of 0 + post-recovery 5,118.33"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_heavy"
    value: "0.00"
    work: "No depreciation after the recovery period for a vehicle not subject to the limits"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_v"
    value: "5118.33"
    work: "Subject to the passenger automobile limits"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus"
    value: "0.00"
    work: "Standard mileage rate, so no depreciation is deducted"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs"
    value: "0.00"
    work: "Standard mileage rate, so no depreciation is deducted"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_2025"
    value: "0.00"
    work: "Not a 2025 vehicle; standard rate used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_q4"
    value: "0.00"
    work: "Not placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_total"
    value: "0.00"
    work: "Not placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cost179"
    value: "0.00"
    work: "Not placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_o"
    value: "0.00"
    work: "Not owned on actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_o"
    value: "0.00"
    work: "Not owned on actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_o"
    value: "0.00"
    work: "Not owned on actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].q4_basis"
    value: "0.00"
    work: "Placed in service in quarter 1, not October to December"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_o"
    value: "0.00"
    work: "Not owned on actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_total_o"
    value: "0.00"
    work: "Not owned on actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_total_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cost179_o"
    value: "0.00"
    work: "Not owned on actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cost179_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
```
```

### classm.scveh.4

```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bm_c"
    value: "29886.00"
    work: "Business miles 29,886"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cm_c"
    value: "0.00"
    work: "Commuting miles 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].om_c"
    value: "391.00"
    work: "Other miles 391"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].nonbusiness_c"
    value: "391.00"
    work: "0 + 391"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].total_c"
    value: "30277.00"
    work: "29,886 + 391"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].no_miles"
    value: "no"
    work: "Total miles 30,277 > 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].over_half"
    value: "yes"
    work: "29,886 / 30,277 = 98.71% > 50%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].smr_bad"
    value: "no"
    work: "Filer answered yes, the standard mileage rate may be used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].smr_amount"
    value: "20920.20"
    work: "29,886 x 0.70"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9_standard"
    value: "20920.20"
    work: "20,920.20 + 0 parking and tolls"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].operating_business"
    value: "9706.02"
    work: "9,833 x 29,886 / 30,277"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9_actual"
    value: "9706.02"
    work: "9,706.02 + 0 parking and tolls"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9"
    value: "9706.02"
    work: "Actual expenses chosen"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is_actual_owned"
    value: "yes"
    work: "Owned and actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is_actual_leased"
    value: "no"
    work: "Vehicle is owned"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lease_business"
    value: "5582.96"
    work: "5,656 x 29,886 / 30,277"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20a"
    value: "0.00"
    work: "Not leased, so no line 20a amount"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].low_use"
    value: "no"
    work: "98.71% > 50%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].screened"
    value: "no"
    work: "Filer answered no to the screening question"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].year"
    value: "2"
    work: "Placed in service 2024, so 2025 is recovery year 2"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is2025"
    value: "no"
    work: "Placed in service 2024"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is2019"
    value: "no"
    work: "Placed in service 2024"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bus_cost"
    value: "7658.80"
    work: "Worksheet line 13: 7,759 x 29,886 / 30,277"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_bad"
    value: "no"
    work: "2025 election 0 is not more than 7,658.80 business cost"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_mixed"
    value: "no"
    work: "Choice is the same for all 5-year property"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].claims_bonus"
    value: "no"
    work: "Special allowance = none"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lim_first_bonus"
    value: "20200.00"
    work: "Table 2 footnote: 2025 first-year limit with special allowance"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lim_prior"
    value: "19800.00"
    work: "Table 2: 2024 automobile, year 2 limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line7"
    value: "19800.00"
    work: "Year-2 limit for a 2024 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9w"
    value: "19544.30"
    work: "19,800 x 29,886 / 30,277"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_ok"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line10"
    value: "0.00"
    work: "Enter -0-: 2025 is not the year placed in service"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line10_2025"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_line10"
    value: "0.00"
    work: "Smaller of election 0 or line 9 19,544.30"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line11"
    value: "19544.30"
    work: "19,544.30 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line14"
    value: "7759.00"
    work: "Section 179 claimed in year placed in service"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line15"
    value: "0.00"
    work: "7,658.80 - 7,759 is less than zero, so enter 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_full"
    value: "0.00"
    work: "100% x 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_forty"
    value: "0.00"
    work: "40% x 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_fullcase"
    value: "0.00"
    work: "Line 15 is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_2025"
    value: "0.00"
    work: "Not a 2025 vehicle; no allowance claimed"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line16"
    value: "0.00"
    work: "Enter -0-: not the year placed in service"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_allowed"
    value: "0.00"
    work: "Smaller of 0 or line 11"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line17"
    value: "19544.30"
    work: "19,544.30 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line18"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].qconv"
    value: "mq4"
    work: "Placed in service in the fourth quarter"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].rate_hy"
    value: "20.00%"
    work: "5-year 200DB half-year, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].rate_mq"
    value: "5.00%"
    work: "5-year 200DB mid-quarter Q4, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].rate_prior"
    value: "32.00%"
    work: "5-year 200DB half-year (convention used), year 2"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_hy"
    value: "0.00"
    work: "0 x 20%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_mq"
    value: "0.00"
    work: "0 x 5%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_prior"
    value: "0.00"
    work: "0 x 32%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19"
    value: "0.00"
    work: "Line 18 is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_earlier"
    value: "0.00"
    work: "Prior-year vehicle: 0 x 32%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_2025"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20"
    value: "0.00"
    work: "Lesser of 19,544.30 or 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].b100"
    value: "0.00"
    work: "7,759 - 7,759"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r1"
    value: "20.00%"
    work: "5-year half-year, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t1"
    value: "0.00"
    work: "0 x 20%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t1s"
    value: "7759.00"
    work: "7,759 + 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r2"
    value: "32.00%"
    work: "5-year half-year, year 2"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t2"
    value: "0.00"
    work: "0 x 32%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].l2"
    value: "19800.00"
    work: "2024 vehicle, year 2 limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].d2"
    value: "0.00"
    work: "Lesser of 0 or 19,800"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r3"
    value: "19.20%"
    work: "5-year half-year, year 3"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t3"
    value: "0.00"
    work: "0 x 19.20%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r4"
    value: "11.52%"
    work: "5-year half-year, year 4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t4"
    value: "0.00"
    work: "0 x 11.52%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r5"
    value: "11.52%"
    work: "5-year half-year, year 5"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t5"
    value: "0.00"
    work: "0 x 11.52%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r6"
    value: "5.76%"
    work: "5-year half-year, year 6"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t6"
    value: "0.00"
    work: "0 x 5.76%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].too_old"
    value: "no"
    work: "Placed in service 2024"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_v"
    value: "0.00"
    work: "No special allowance"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_pass"
    value: "0.00"
    work: "Line 20 is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_heavy"
    value: "0.00"
    work: "Line 19 is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_v"
    value: "0.00"
    work: "Passenger automobile, so 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus"
    value: "0.00"
    work: "Line 25 is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs"
    value: "0.00"
    work: "Column (h) is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_2025"
    value: "0.00"
    work: "No 2025 election"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_q4"
    value: "0.00"
    work: "Not placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_total"
    value: "0.00"
    work: "Not placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cost179"
    value: "0.00"
    work: "Not placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_o"
    value: "0.00"
    work: "Owned and actual; allowance 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_o"
    value: "0.00"
    work: "Owned and actual; column (h) 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_o"
    value: "0.00"
    work: "Owned and actual; 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].q4_basis"
    value: "7658.80"
    work: "Q4: business cost 7,658.80 - 2025 section 179 election 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_o"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_total_o"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_total_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cost179_o"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cost179_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
```

### classm.scveh.5

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bm_c"
    value: "13307.00"
    work: "Business miles 13,307"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cm_c"
    value: "2928.00"
    work: "Commuting miles 2,928"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].om_c"
    value: "2824.00"
    work: "Other miles 2,824"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].nonbusiness_c"
    value: "5752.00"
    work: "2928 + 2824"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].total_c"
    value: "19059.00"
    work: "13307 + 5752"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].no_miles"
    value: "no"
    work: "Total miles is more than 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].over_half"
    value: "yes"
    work: "13307/19059 = 69.82% > 50%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].smr_bad"
    value: "no"
    work: "The filer may use the standard mileage rate"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].smr_amount"
    value: "9314.90"
    work: "13307 x 0.70"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9_standard"
    value: "9314.90"
    work: "9314.90 + 0 parking and tolls"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].operating_business"
    value: "0.00"
    work: "0 x 13307/19059"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9_actual"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9"
    value: "0.00"
    work: "Actual expenses method"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is_actual_owned"
    value: "no"
    work: "Vehicle is leased"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is_actual_leased"
    value: "yes"
    work: "Leased, actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lease_business"
    value: "2493.27"
    work: "3571 x 13307/19059"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20a"
    value: "2493.27"
    work: "Leased on actual expenses, business portion of lease"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].low_use"
    value: "no"
    work: "69.82% > 50%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].screened"
    value: "no"
    work: "No screening condition applies"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].year"
    value: "2"
    work: "2025 - 2024 + 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is2025"
    value: "no"
    work: "Placed in service in 2024"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is2019"
    value: "no"
    work: "Placed in service in 2024"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bus_cost"
    value: "54544.11"
    work: "78121 x 13307/19059"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_bad"
    value: "no"
    work: "Section 179 election is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_mixed"
    value: "no"
    work: "Choice is the same for all 5-year property"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].claims_bonus"
    value: "no"
    work: "Special allowance = none"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lim_first_bonus"
    value: "20200.00"
    work: "Table 2 footnote, 2025 with special allowance"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lim_prior"
    value: "19800.00"
    work: "Table 2, placed in service 2024, year 2"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line7"
    value: "19800.00"
    work: "Year-2 limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9w"
    value: "13824.37"
    work: "19800 x 13307/19059"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_ok"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line10"
    value: "0.00"
    work: "Not the year placed in service"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line10_2025"
    value: "0.00"
    work: "Section 179 is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_line10"
    value: "0.00"
    work: "smaller of 0 or line 9"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line11"
    value: "13824.37"
    work: "13824.37 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line14"
    value: "0.00"
    work: "Section 179 in the year placed in service = 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line15"
    value: "54544.11"
    work: "54544.11 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_full"
    value: "54544.11"
    work: "54544.11 x 100%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_forty"
    value: "21817.64"
    work: "54544.11 x 40%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_fullcase"
    value: "54544.11"
    work: "Acquired after 1/19/2025, so 100%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_2025"
    value: "0.00"
    work: "No special allowance claimed"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line16"
    value: "0.00"
    work: "Not the year placed in service"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_allowed"
    value: "0.00"
    work: "smaller of 0 or line 11"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line17"
    value: "13824.37"
    work: "13824.37 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line18"
    value: "54544.11"
    work: "54544.11 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].qconv"
    value: "mq4"
    work: "Placed in service in Q4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].rate_hy"
    value: "20.00%"
    work: "5-yr 200DB HY, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].rate_mq"
    value: "5.00%"
    work: "5-yr 200DB MQ Q4, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].rate_prior"
    value: "32.00%"
    work: "HY, year 2"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_hy"
    value: "10908.82"
    work: "54544.11 x 20%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_mq"
    value: "2727.21"
    work: "54544.11 x 5%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_prior"
    value: "17454.12"
    work: "54544.11 x 32%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19"
    value: "17454.12"
    work: "Placed in service before 2025, so the year-2 rate"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_earlier"
    value: "17454.12"
    work: "line19_prior"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_2025"
    value: "10908.82"
    work: "Mid-quarter test no, so HY"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20"
    value: "13824.37"
    work: "lesser of 13824.37 or 17454.12"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].b100"
    value: "78121.00"
    work: "78121 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r1"
    value: "20.00%"
    work: "HY, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t1"
    value: "15624.20"
    work: "78121 x 20%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t1s"
    value: "15624.20"
    work: "0 + 15624.20"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r2"
    value: "32.00%"
    work: "HY, year 2"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t2"
    value: "24998.72"
    work: "78121 x 32%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].l2"
    value: "19800.00"
    work: "Table 2, 2024, year 2"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].d2"
    value: "19800.00"
    work: "lesser of 19800 or 24998.72"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r3"
    value: "19.20%"
    work: "HY, year 3"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t3"
    value: "14999.23"
    work: "78121 x 19.2%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r4"
    value: "11.52%"
    work: "HY, year 4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t4"
    value: "8999.54"
    work: "78121 x 11.52%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r5"
    value: "11.52%"
    work: "HY, year 5"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t5"
    value: "8999.54"
    work: "78121 x 11.52%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r6"
    value: "5.76%"
    work: "HY, year 6"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t6"
    value: "4499.77"
    work: "78121 x 5.76%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].too_old"
    value: "no"
    work: "Placed in service 2024"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_v"
    value: "0.00"
    work: "line 16 allowed = 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_pass"
    value: "13824.37"
    work: "line 20"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_heavy"
    value: "17454.12"
    work: "line 19"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_v"
    value: "13824.37"
    work: "Subject to the passenger automobile limits"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus"
    value: "0.00"
    work: "Not owned and on actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs"
    value: "0.00"
    work: "Leased, no depreciation"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_2025"
    value: "0.00"
    work: "Leased"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_q4"
    value: "0.00"
    work: "Not owned and on actual expenses / not 2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_total"
    value: "0.00"
    work: "Not 2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cost179"
    value: "0.00"
    work: "Not 2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_o"
    value: "0.00"
    work: "Not owned"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_o"
    value: "0.00"
    work: "Not owned"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_o"
    value: "0.00"
    work: "Not owned"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].q4_basis"
    value: "54544.11"
    work: "Q4, so 54544.11 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_o"
    value: "0.00"
    work: "Not owned"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_a2"
    value: "0.00"
    work: "Not 2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_total_o"
    value: "0.00"
    work: "Not owned"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_total_a2"
    value: "0.00"
    work: "Not 2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cost179_o"
    value: "0.00"
    work: "Not owned"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cost179_a2"
    value: "0.00"
    work: "Not 2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bm_c"
    value: "29252.00"
    work: "Business miles 29,252"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].cm_c"
    value: "726.00"
    work: "Commuting miles 726"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].om_c"
    value: "1699.00"
    work: "Other miles 1,699"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].nonbusiness_c"
    value: "2425.00"
    work: "726 + 1699"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].total_c"
    value: "31677.00"
    work: "29252 + 2425"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].no_miles"
    value: "no"
    work: "Total miles is more than 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].over_half"
    value: "yes"
    work: "29252/31677 = 92.34%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].smr_bad"
    value: "no"
    work: "The standard mileage rate is available"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].smr_amount"
    value: "20476.40"
    work: "29252 x 0.70"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9_standard"
    value: "20476.40"
    work: "20476.40 + 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].operating_business"
    value: "2650.29"
    work: "2870 x 29252/31677"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9_actual"
    value: "2650.29"
    work: "2650.29 + 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9"
    value: "2650.29"
    work: "Actual expenses method"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].is_actual_owned"
    value: "yes"
    work: "Owned, actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].is_actual_leased"
    value: "no"
    work: "Owned"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].lease_business"
    value: "961.31"
    work: "1041 x 29252/31677"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line20a"
    value: "0.00"
    work: "Not leased"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].low_use"
    value: "no"
    work: "92.34% > 50%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].screened"
    value: "no"
    work: "No screening condition applies"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].year"
    value: "1"
    work: "Placed in service 2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].is2025"
    value: "yes"
    work: "Placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].is2019"
    value: "no"
    work: "Placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bus_cost"
    value: "41575.39"
    work: "45022 x 29252/31677"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].s179_bad"
    value: "no"
    work: "14878 <= 41575.39; not an SUV"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_mixed"
    value: "no"
    work: "Same choice for the class"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].claims_bonus"
    value: "no"
    work: "Special allowance = none"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].lim_first_bonus"
    value: "20200.00"
    work: "Table 2 footnote"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].lim_first_none"
    value: "12200.00"
    work: "Table 2, 2025, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].lim_2025"
    value: "12200.00"
    work: "No special allowance"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].lim_prior"
    value: "12200.00"
    work: "Year 1 of a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line7"
    value: "12200.00"
    work: "lim_2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9w"
    value: "11266.04"
    work: "12200 x 29252/31677"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].s179_2025_ok"
    value: "14878.00"
    work: "Election allowed"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line10"
    value: "11266.04"
    work: "smaller of 14878 or 11266.04"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line10_2025"
    value: "11266.04"
    work: "smaller of 14878 or line 9"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].s179_line10"
    value: "11266.04"
    work: "smaller of 14878 or line 9"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line11"
    value: "0.00"
    work: "11266.04 - 11266.04"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line14"
    value: "11266.04"
    work: "Section 179 claimed in 2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line15"
    value: "30309.35"
    work: "41575.39 - 11266.04"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_full"
    value: "30309.35"
    work: "30309.35 x 100%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_forty"
    value: "12123.74"
    work: "30309.35 x 40%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_fullcase"
    value: "30309.35"
    work: "Acquired after 1/19/2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_2025"
    value: "0.00"
    work: "Not claimed"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line16"
    value: "0.00"
    work: "Not claimed"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_allowed"
    value: "0.00"
    work: "smaller of 0 or 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line17"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line18"
    value: "30309.35"
    work: "30309.35 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].qconv"
    value: "mq3"
    work: "Q3"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].rate_hy"
    value: "20.00%"
    work: "HY, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].rate_mq"
    value: "15.00%"
    work: "MQ Q3, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].rate_prior"
    value: "20.00%"
    work: "HY, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19_hy"
    value: "6061.87"
    work: "30309.35 x 20%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19_mq"
    value: "4546.40"
    work: "30309.35 x 15%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19_prior"
    value: "6061.87"
    work: "30309.35 x 20%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19"
    value: "6061.87"
    work: "MQ test no, so HY"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19_earlier"
    value: "6061.87"
    work: "line19_prior"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19_2025"
    value: "6061.87"
    work: "HY"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line20"
    value: "0.00"
    work: "lesser of 0 or 6061.87"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].b100"
    value: "33755.96"
    work: "45022 - 11266.04"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r1"
    value: "20.00%"
    work: "HY, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t1"
    value: "6751.19"
    work: "33755.96 x 20%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].l1"
    value: "12200.00"
    work: "Table 2, 2025, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t1s"
    value: "18017.23"
    work: "11266.04 + 6751.19"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].d1"
    value: "12200.00"
    work: "lesser of 12200 or 18017.23"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r2"
    value: "32.00%"
    work: "HY, year 2"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t2"
    value: "10801.91"
    work: "33755.96 x 32%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r3"
    value: "19.20%"
    work: "HY, year 3"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t3"
    value: "6481.14"
    work: "33755.96 x 19.2%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r4"
    value: "11.52%"
    work: "HY, year 4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t4"
    value: "3888.69"
    work: "33755.96 x 11.52%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r5"
    value: "11.52%"
    work: "HY, year 5"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t5"
    value: "3888.69"
    work: "33755.96 x 11.52%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r6"
    value: "5.76%"
    work: "HY, year 6"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t6"
    value: "1944.34"
    work: "33755.96 x 5.76%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].too_old"
    value: "no"
    work: "Placed in service 2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_v"
    value: "0.00"
    work: "No allowance"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].macrs_pass"
    value: "0.00"
    work: "line 20"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].macrs_heavy"
    value: "6061.87"
    work: "line 19"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].macrs_v"
    value: "0.00"
    work: "Subject to the limits"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus"
    value: "0.00"
    work: "bonus_o"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].macrs"
    value: "0.00"
    work: "macrs_o"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].s179_2025"
    value: "11266.04"
    work: "s179_2025_o"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_q4"
    value: "0.00"
    work: "Q3"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_total"
    value: "30309.35"
    work: "41575.39 - 11266.04"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].cost179"
    value: "41575.39"
    work: "Business cost"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_o"
    value: "0.00"
    work: "bonus_v"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].macrs_o"
    value: "0.00"
    work: "macrs_v"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].s179_2025_o"
    value: "11266.04"
    work: "line 10"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].q4_basis"
    value: "0.00"
    work: "Not Q4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_q4_o"
    value: "0.00"
    work: "Not Q4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_q4_a2"
    value: "0.00"
    work: "Not Q4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_total_o"
    value: "30309.35"
    work: "mq_total_a2"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_total_a2"
    value: "30309.35"
    work: "41575.39 - 11266.04"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].cost179_o"
    value: "41575.39"
    work: "cost179_a2"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].cost179_a2"
    value: "41575.39"
    work: "Business cost"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bm_c"
    value: "20767.00"
    work: "Business miles 20,767"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].cm_c"
    value: "3286.00"
    work: "Commuting miles 3,286"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].om_c"
    value: "3077.00"
    work: "Other miles 3,077"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].nonbusiness_c"
    value: "6363.00"
    work: "3286 + 3077"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].total_c"
    value: "27130.00"
    work: "20767 + 6363"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].no_miles"
    value: "no"
    work: "Standard mileage method; miles > 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].over_half"
    value: "yes"
    work: "20767/27130 = 76.55%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].smr_bad"
    value: "no"
    work: "Standard mileage rate is allowed"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].smr_amount"
    value: "14536.90"
    work: "20767 x 0.70"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line9_standard"
    value: "14536.90"
    work: "14536.90 + 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].operating_business"
    value: "0.00"
    work: "0 x pct"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line9_actual"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line9"
    value: "14536.90"
    work: "Standard mileage method"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].is_actual_owned"
    value: "no"
    work: "Standard mileage method"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].is_actual_leased"
    value: "no"
    work: "Standard mileage method"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].lease_business"
    value: "0.00"
    work: "0 x pct"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line20a"
    value: "0.00"
    work: "Not leased on actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].low_use"
    value: "no"
    work: "76.55% > 50%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].screened"
    value: "no"
    work: "No screening condition applies"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].year"
    value: "6"
    work: "2025 - 2020 + 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].is2025"
    value: "no"
    work: "Placed in service 2020"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].is2019"
    value: "no"
    work: "Placed in service 2020"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bus_cost"
    value: "28476.74"
    work: "37202 x 20767/27130"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].s179_bad"
    value: "no"
    work: "Election is 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_mixed"
    value: "no"
    work: "Same choice"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].claims_bonus"
    value: "no"
    work: "Special allowance = none"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].lim_first_bonus"
    value: "20200.00"
    work: "Table 2 footnote"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].lim_prior"
    value: "5760.00"
    work: "Table 2, 2020, 4 or more years"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line7"
    value: "5760.00"
    work: "lim_prior"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line9w"
    value: "4409.06"
    work: "5760 x 20767/27130"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].s179_2025_ok"
    value: "0.00"
    work: "Not 2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line10"
    value: "0.00"
    work: "Not the year placed in service"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line10_2025"
    value: "0.00"
    work: "Section 179 is 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].s179_line10"
    value: "0.00"
    work: "Section 179 is 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line11"
    value: "4409.06"
    work: "4409.06 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line14"
    value: "0.00"
    work: "Given"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line15"
    value: "28476.74"
    work: "28476.74 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_full"
    value: "28476.74"
    work: "x 100%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_forty"
    value: "11390.70"
    work: "x 40%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_fullcase"
    value: "28476.74"
    work: "Acquired after 1/19/2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_2025"
    value: "0.00"
    work: "Not claimed"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line16"
    value: "0.00"
    work: "Not the year placed in service"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_allowed"
    value: "0.00"
    work: "0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line17"
    value: "4409.06"
    work: "4409.06 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line18"
    value: "28476.74"
    work: "28476.74 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].qconv"
    value: "mq4"
    work: "Q4"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].rate_hy"
    value: "20.00%"
    work: "HY, year 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].rate_mq"
    value: "5.00%"
    work: "MQ Q4, year 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].rate_prior"
    value: "4.26%"
    work: "MQ Q2, year 6"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line19_hy"
    value: "5695.35"
    work: "28476.74 x 20%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line19_mq"
    value: "1423.84"
    work: "28476.74 x 5%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line19_prior"
    value: "1213.11"
    work: "28476.74 x 4.26%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line19"
    value: "1213.11"
    work: "Placed in service before 2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line19_earlier"
    value: "1213.11"
    work: "line19_prior"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line19_2025"
    value: "5695.35"
    work: "HY"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line20"
    value: "1213.11"
    work: "lesser of 4409.06 or 1213.11"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].b100"
    value: "37202.00"
    work: "37202 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].r1"
    value: "25.00%"
    work: "MQ Q2, year 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].t1"
    value: "9300.50"
    work: "37202 x 25%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].t1s"
    value: "9300.50"
    work: "0 + 9300.50"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].r2"
    value: "30.00%"
    work: "MQ Q2, year 2"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].t2"
    value: "11160.60"
    work: "37202 x 30%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].l2"
    value: "16100.00"
    work: "2020, year 2"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].d2"
    value: "11160.60"
    work: "lesser"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].r3"
    value: "18.00%"
    work: "MQ Q2, year 3"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].t3"
    value: "6696.36"
    work: "37202 x 18%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].l3"
    value: "9700.00"
    work: "2020, year 3"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].d3"
    value: "6696.36"
    work: "lesser"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].r4"
    value: "11.37%"
    work: "MQ Q2, year 4"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].t4"
    value: "4229.87"
    work: "37202 x 11.37%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].l4"
    value: "5760.00"
    work: "2020, year 4 or more"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].d4"
    value: "4229.87"
    work: "lesser"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].r5"
    value: "11.37%"
    work: "MQ Q2, year 5"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].t5"
    value: "4229.87"
    work: "37202 x 11.37%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].l5"
    value: "5760.00"
    work: "2020, year 4 or more"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].d5"
    value: "4229.87"
    work: "lesser"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].r6"
    value: "4.26%"
    work: "MQ Q2, year 6"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].t6"
    value: "1584.81"
    work: "37202 x 4.26%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].l6"
    value: "5760.00"
    work: "2020, year 4 or more"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].d6"
    value: "1584.81"
    work: "lesser"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].too_old"
    value: "no"
    work: "Placed in service 2020"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_v"
    value: "0.00"
    work: "No allowance"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].macrs_pass"
    value: "1213.11"
    work: "line 20"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].macrs_heavy"
    value: "1213.11"
    work: "line 19"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].macrs_v"
    value: "1213.11"
    work: "Subject to the limits"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus"
    value: "0.00"
    work: "Standard mileage"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].macrs"
    value: "0.00"
    work: "Standard mileage, no depreciation"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].s179_2025"
    value: "0.00"
    work: "Standard mileage"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].mq_q4"
    value: "0.00"
    work: "Not owned on actual / not 2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].mq_total"
    value: "0.00"
    work: "Not 2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].cost179"
    value: "0.00"
    work: "Not 2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_o"
    value: "0.00"
    work: "Not actual-owned"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].macrs_o"
    value: "0.00"
    work: "Not actual-owned"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].s179_2025_o"
    value: "0.00"
    work: "Not actual-owned"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].q4_basis"
    value: "28476.74"
    work: "Q4, so 28476.74 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].mq_q4_o"
    value: "0.00"
    work: "Not actual-owned"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].mq_q4_a2"
    value: "0.00"
    work: "Not 2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].mq_total_o"
    value: "0.00"
    work: "Not actual-owned"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].mq_total_a2"
    value: "0.00"
    work: "Not 2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].cost179_o"
    value: "0.00"
    work: "Not actual-owned"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].cost179_a2"
    value: "0.00"
    work: "Not 2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bm_c"
    value: "15546.00"
    work: "Business miles 15,546"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].cm_c"
    value: "0.00"
    work: "Commuting miles 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].om_c"
    value: "3799.00"
    work: "Other miles 3,799"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].nonbusiness_c"
    value: "3799.00"
    work: "0 + 3799"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].total_c"
    value: "19345.00"
    work: "15546 + 3799"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].no_miles"
    value: "no"
    work: "Miles > 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].over_half"
    value: "yes"
    work: "15546/19345 = 80.36%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].smr_bad"
    value: "no"
    work: "Standard mileage rate is allowed"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].smr_amount"
    value: "10882.20"
    work: "15546 x 0.70"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line9_standard"
    value: "10882.20"
    work: "10882.20 + 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].operating_business"
    value: "1342.04"
    work: "1670 x 15546/19345"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line9_actual"
    value: "1342.04"
    work: "1342.04 + 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line9"
    value: "10882.20"
    work: "Standard mileage method"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].is_actual_owned"
    value: "no"
    work: "Standard mileage method"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].is_actual_leased"
    value: "no"
    work: "Standard mileage method"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].lease_business"
    value: "1407.14"
    work: "1751 x 15546/19345"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line20a"
    value: "0.00"
    work: "Standard mileage; no lease deduction"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].low_use"
    value: "no"
    work: "80.36% > 50%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].screened"
    value: "no"
    work: "No screening condition applies"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].year"
    value: "2"
    work: "2025 - 2024 + 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].is2025"
    value: "no"
    work: "Placed in service 2024"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].is2019"
    value: "no"
    work: "Placed in service 2024"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bus_cost"
    value: "56442.15"
    work: "70235 x 15546/19345"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].s179_bad"
    value: "no"
    work: "Election is 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_mixed"
    value: "no"
    work: "Same choice"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].claims_bonus"
    value: "no"
    work: "Special allowance = none"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].lim_first_bonus"
    value: "20200.00"
    work: "Table 2 footnote"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].lim_prior"
    value: "19800.00"
    work: "Table 2, 2024, year 2"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line7"
    value: "19800.00"
    work: "lim_prior"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line9w"
    value: "15911.65"
    work: "19800 x 15546/19345"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].s179_2025_ok"
    value: "0.00"
    work: "Not 2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line10"
    value: "0.00"
    work: "Not the year placed in service"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line10_2025"
    value: "0.00"
    work: "Section 179 is 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].s179_line10"
    value: "0.00"
    work: "Section 179 is 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line11"
    value: "15911.65"
    work: "15911.65 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line14"
    value: "0.00"
    work: "Given"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line15"
    value: "56442.15"
    work: "56442.15 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_full"
    value: "56442.15"
    work: "x 100%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_forty"
    value: "22576.86"
    work: "x 40%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_fullcase"
    value: "56442.15"
    work: "Acquired after 1/19/2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_2025"
    value: "0.00"
    work: "Not claimed"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line16"
    value: "0.00"
    work: "Not the year placed in service"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_allowed"
    value: "0.00"
    work: "0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line17"
    value: "15911.65"
    work: "15911.65 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line18"
    value: "56442.15"
    work: "56442.15 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].qconv"
    value: "mq1"
    work: "Q1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].rate_hy"
    value: "20.00%"
    work: "HY, year 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].rate_mq"
    value: "35.00%"
    work: "MQ Q1, year 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].rate_prior"
    value: "34.00%"
    work: "MQ Q3, year 2"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line19_hy"
    value: "11288.43"
    work: "56442.15 x 20%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line19_mq"
    value: "19754.75"
    work: "56442.15 x 35%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line19_prior"
    value: "19190.33"
    work: "56442.15 x 34%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line19"
    value: "19190.33"
    work: "Placed in service before 2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line19_earlier"
    value: "19190.33"
    work: "line19_prior"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line19_2025"
    value: "11288.43"
    work: "HY"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line20"
    value: "15911.65"
    work: "lesser of 15911.65 or 19190.33"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].b100"
    value: "70235.00"
    work: "70235 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].r1"
    value: "15.00%"
    work: "MQ Q3, year 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].t1"
    value: "10535.25"
    work: "70235 x 15%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].t1s"
    value: "10535.25"
    work: "0 + 10535.25"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].r2"
    value: "34.00%"
    work: "MQ Q3, year 2"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].t2"
    value: "23879.90"
    work: "70235 x 34%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].l2"
    value: "19800.00"
    work: "2024, year 2"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].d2"
    value: "19800.00"
    work: "lesser of 19800 or 23879.90"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].r3"
    value: "20.40%"
    work: "MQ Q3, year 3"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].t3"
    value: "14327.94"
    work: "70235 x 20.4%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].r4"
    value: "12.24%"
    work: "MQ Q3, year 4"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].t4"
    value: "8596.76"
    work: "70235 x 12.24%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].r5"
    value: "11.30%"
    work: "MQ Q3, year 5"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].t5"
    value: "7936.56"
    work: "70235 x 11.30%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].r6"
    value: "7.06%"
    work: "MQ Q3, year 6"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].t6"
    value: "4958.59"
    work: "70235 x 7.06%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].too_old"
    value: "no"
    work: "Placed in service 2024"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_v"
    value: "0.00"
    work: "No allowance"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].macrs_pass"
    value: "15911.65"
    work: "line 20"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].macrs_heavy"
    value: "19190.33"
    work: "line 19"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].macrs_v"
    value: "15911.65"
    work: "Subject to the limits"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus"
    value: "0.00"
    work: "Standard mileage"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].macrs"
    value: "0.00"
    work: "Standard mileage, no depreciation"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].s179_2025"
    value: "0.00"
    work: "Standard mileage"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].mq_q4"
    value: "0.00"
    work: "Not 2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].mq_total"
    value: "0.00"
    work: "Not 2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].cost179"
    value: "0.00"
    work: "Not 2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_o"
    value: "0.00"
    work: "Not actual-owned"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].macrs_o"
    value: "0.00"
    work: "Not actual-owned"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].s179_2025_o"
    value: "0.00"
    work: "Not actual-owned"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].q4_basis"
    value: "0.00"
    work: "Q1, not Q4"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].mq_q4_o"
    value: "0.00"
    work: "Not actual-owned"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].mq_q4_a2"
    value: "0.00"
    work: "Not 2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].mq_total_o"
    value: "0.00"
    work: "Not actual-owned"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].mq_total_a2"
    value: "0.00"
    work: "Not 2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].cost179_o"
    value: "0.00"
    work: "Not actual-owned"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].cost179_a2"
    value: "0.00"
    work: "Not 2025"
```
```

### classm.scveh.6

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bm_c"
    value: "18674.00"
    work: "Business miles 18,674"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cm_c"
    value: "0.00"
    work: "Commuting miles 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].om_c"
    value: "3132.00"
    work: "Other miles 3,132"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].nonbusiness_c"
    value: "3132.00"
    work: "0 + 3,132"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].total_c"
    value: "21806.00"
    work: "18,674 + 3,132"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].no_miles"
    value: "no"
    work: "Standard mileage method; total miles are not zero"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].over_half"
    value: "yes"
    work: "18,674 / 21,806 = 85.64% > 50%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].smr_bad"
    value: "no"
    work: "The filer may use the standard mileage rate"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].smr_amount"
    value: "13071.80"
    work: "18,674 x 0.70"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9_standard"
    value: "13071.80"
    work: "13,071.80 + 0 parking and tolls"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].operating_business"
    value: "8563.70"
    work: "10,000 x 18,674/21,806"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9_actual"
    value: "8563.70"
    work: "8,563.70 + 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9"
    value: "13071.80"
    work: "Standard mileage method chosen"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is_actual_owned"
    value: "no"
    work: "Standard mileage method"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is_actual_leased"
    value: "no"
    work: "Owned; standard mileage method"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lease_business"
    value: "0.00"
    work: "0 lease payments x business %"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20a"
    value: "0.00"
    work: "Not leased on actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].low_use"
    value: "no"
    work: "85.64% > 50%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].screened"
    value: "no"
    work: "None of the screens apply"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].year"
    value: "7"
    work: "Placed in service 2019; 2025 is year 7"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is2025"
    value: "no"
    work: "Placed in service 2019"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is2019"
    value: "yes"
    work: "Placed in service 2019"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bus_cost"
    value: "56076.81"
    work: "65,482 x 18,674/21,806"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_bad"
    value: "no"
    work: "Elected section 179 is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_mixed"
    value: "no"
    work: "Same choice for all 5-year property"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].claims_bonus"
    value: "no"
    work: "Special allowance = none"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lim_first_bonus"
    value: "20200.00"
    work: "Table 2 footnote: 2025 limit with special allowance"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lim_first_none"
    value: "12200.00"
    work: "Table 2: 2025 year 1 limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lim_2025"
    value: "12200.00"
    work: "No special allowance claimed"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lim_prior"
    value: "5760.00"
    work: "Table 2: 2019 vehicle, year 4 or more"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line7"
    value: "5760.00"
    work: "Limit for the 2025 year of recovery"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9w"
    value: "4932.69"
    work: "5,760 x 18,674/21,806"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_ok"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line10"
    value: "0.00"
    work: "Not the year placed in service"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line10_2025"
    value: "0.00"
    work: "Smaller of 0 or 4,932.69"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_line10"
    value: "0.00"
    work: "Smaller of election 0 or line 9"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line11"
    value: "4932.69"
    work: "4,932.69 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line14"
    value: "1714.00"
    work: "Section 179 claimed in 2019"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line15"
    value: "54362.81"
    work: "56,076.81 - 1,714"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_full"
    value: "54362.81"
    work: "54,362.81 x 100%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_forty"
    value: "21745.12"
    work: "54,362.81 x 40%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_fullcase"
    value: "54362.81"
    work: "Acquired after Jan 19, 2025, so 100%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_2025"
    value: "0.00"
    work: "No special allowance claimed"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line16"
    value: "0.00"
    work: "Not the year placed in service"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_allowed"
    value: "0.00"
    work: "Smaller of 0 or line 11"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line17"
    value: "4932.69"
    work: "4,932.69 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line18"
    value: "54362.81"
    work: "54,362.81 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].qconv"
    value: "mq4"
    work: "Quarter q4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19"
    value: "0.00"
    work: "2019 vehicle is past the recovery period; no table rate"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_earlier"
    value: "0.00"
    work: "Zero after the recovery period"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20"
    value: "0.00"
    work: "Lesser of 4,932.69 or 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].b100"
    value: "63768.00"
    work: "65,482 - 1,714"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r1"
    value: "5.00%"
    work: "5-year 200DB mid-quarter Q4, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t1"
    value: "3188.40"
    work: "63,768 x 5.00%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].l1"
    value: "10100.00"
    work: "2019 year 1 limit with no special allowance"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t1s"
    value: "4902.40"
    work: "1,714 + 3,188.40"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].d1"
    value: "4902.40"
    work: "Lesser of 10,100 or 4,902.40"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r2"
    value: "38.00%"
    work: "Mid-quarter Q4, year 2"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t2"
    value: "24231.84"
    work: "63,768 x 38%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].l2"
    value: "16100.00"
    work: "2019 year 2 limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].d2"
    value: "16100.00"
    work: "Lesser of 16,100 or 24,231.84"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r3"
    value: "22.80%"
    work: "Mid-quarter Q4, year 3"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t3"
    value: "14539.10"
    work: "63,768 x 22.80%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].l3"
    value: "9700.00"
    work: "2019 year 3 limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].d3"
    value: "9700.00"
    work: "Lesser of 9,700 or 14,539.10"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r4"
    value: "13.68%"
    work: "Mid-quarter Q4, year 4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t4"
    value: "8723.46"
    work: "63,768 x 13.68%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].l4"
    value: "5760.00"
    work: "2019 limit, year 4 or later"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].d4"
    value: "5760.00"
    work: "Lesser of 5,760 or 8,723.46"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r5"
    value: "10.94%"
    work: "Mid-quarter Q4, year 5"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t5"
    value: "6976.22"
    work: "63,768 x 10.94%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].l5"
    value: "5760.00"
    work: "2019 limit, year 4 or later"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].d5"
    value: "5760.00"
    work: "Lesser of 5,760 or 6,976.22"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r6"
    value: "9.58%"
    work: "Mid-quarter Q4, year 6"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t6"
    value: "6108.97"
    work: "63,768 x 9.58%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].l6"
    value: "5760.00"
    work: "2019 limit, year 4 or later"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].d6"
    value: "5760.00"
    work: "Lesser of 5,760 or 6,108.97"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].d_total"
    value: "47982.40"
    work: "4,902.40 + 16,100 + 9,700 + 5,760 x 3"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].unrecovered"
    value: "17499.60"
    work: "65,482 - 47,982.40"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].post_amount"
    value: "5760.00"
    work: "Lesser of 5,760 or 17,499.60"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].post"
    value: "4932.69"
    work: "5,760 x 18,674/21,806"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].too_old"
    value: "no"
    work: "Placed in service 2019"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_v"
    value: "0.00"
    work: "bonus_allowed is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_pass"
    value: "4932.69"
    work: "2019 passenger auto: deduction after the recovery period"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_heavy"
    value: "0.00"
    work: "No deduction after the recovery period for property that is not a passenger auto"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_v"
    value: "0.00"
    work: "Not subject to the auto limits, so the heavy-vehicle column applies"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus"
    value: "0.00"
    work: "Not on actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs"
    value: "0.00"
    work: "Standard mileage rate; no depreciation"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_2025"
    value: "0.00"
    work: "Not on actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_q4"
    value: "0.00"
    work: "Not a 2025 actual-expense vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_total"
    value: "0.00"
    work: "Not a 2025 actual-expense vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cost179"
    value: "0.00"
    work: "Not a 2025 actual-expense vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_o"
    value: "0.00"
    work: "Not owned on actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_o"
    value: "0.00"
    work: "Not owned on actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_o"
    value: "0.00"
    work: "Not owned on actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].q4_basis"
    value: "54362.81"
    work: "Q4: line 15 basis after section 179"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_o"
    value: "0.00"
    work: "Not owned on actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_total_o"
    value: "0.00"
    work: "Not owned on actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_total_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cost179_o"
    value: "0.00"
    work: "Not owned on actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cost179_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bm_c"
    value: "22572.00"
    work: "Business miles 22,572"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].cm_c"
    value: "0.00"
    work: "Commuting miles 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].om_c"
    value: "2734.00"
    work: "Other miles 2,734"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].nonbusiness_c"
    value: "2734.00"
    work: "0 + 2,734"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].total_c"
    value: "25306.00"
    work: "22,572 + 2,734"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].no_miles"
    value: "no"
    work: "Total miles are not zero"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].over_half"
    value: "yes"
    work: "22,572 / 25,306 = 89.20% > 50%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].smr_bad"
    value: "no"
    work: "Actual expenses method; standard rate is available anyway"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].smr_amount"
    value: "15800.40"
    work: "22,572 x 0.70"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9_standard"
    value: "15800.40"
    work: "15,800.40 + 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].operating_business"
    value: "0.00"
    work: "0 x business %"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9_actual"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9"
    value: "0.00"
    work: "Actual expenses method chosen"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].is_actual_owned"
    value: "yes"
    work: "Owned; actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].is_actual_leased"
    value: "no"
    work: "Owned"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].lease_business"
    value: "7012.61"
    work: "7,862 x 22,572/25,306"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line20a"
    value: "0.00"
    work: "Not leased"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].low_use"
    value: "no"
    work: "89.20% > 50%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].screened"
    value: "no"
    work: "None of the screens apply"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].year"
    value: "5"
    work: "Placed in service 2021; 2025 is year 5"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].is2025"
    value: "no"
    work: "Placed in service 2021"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].is2019"
    value: "no"
    work: "Placed in service 2021"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bus_cost"
    value: "42373.56"
    work: "47,506 x 22,572/25,306"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].s179_bad"
    value: "no"
    work: "Elected section 179 is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_mixed"
    value: "no"
    work: "Same choice for all 5-year property"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].claims_bonus"
    value: "no"
    work: "Special allowance = none"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].lim_first_bonus"
    value: "20200.00"
    work: "Table 2 footnote: 2025 limit with special allowance"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].lim_prior"
    value: "5860.00"
    work: "Table 2: 2021 vehicle, year 4 or more"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line7"
    value: "5860.00"
    work: "Limit for year 5"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9w"
    value: "5226.90"
    work: "5,860 x 22,572/25,306"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].s179_2025_ok"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line10"
    value: "0.00"
    work: "Not the year placed in service"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line10_2025"
    value: "0.00"
    work: "Smaller of 0 or line 9"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].s179_line10"
    value: "0.00"
    work: "Smaller of election 0 or line 9"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line11"
    value: "5226.90"
    work: "5,226.90 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line14"
    value: "0.00"
    work: "No section 179 claimed in 2021"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line15"
    value: "42373.56"
    work: "42,373.56 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_full"
    value: "42373.56"
    work: "42,373.56 x 100%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_forty"
    value: "16949.42"
    work: "42,373.56 x 40%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_fullcase"
    value: "42373.56"
    work: "Acquired after Jan 19, 2025, so 100%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_2025"
    value: "0.00"
    work: "No special allowance claimed"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line16"
    value: "0.00"
    work: "Not the year placed in service"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_allowed"
    value: "0.00"
    work: "Smaller of 0 or line 11"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line17"
    value: "5226.90"
    work: "5,226.90 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line18"
    value: "42373.56"
    work: "42,373.56 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].qconv"
    value: "mq3"
    work: "Quarter q3"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].rate_hy"
    value: "20.00%"
    work: "5-year HY, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].rate_mq"
    value: "15.00%"
    work: "5-year mid-quarter Q3, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].rate_prior"
    value: "11.52%"
    work: "5-year HY, year 5"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19_hy"
    value: "8474.71"
    work: "42,373.56 x 20%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19_mq"
    value: "6356.03"
    work: "42,373.56 x 15%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19_prior"
    value: "4881.43"
    work: "42,373.56 x 11.52%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19"
    value: "4881.43"
    work: "Earlier-year vehicle uses line19_prior"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19_earlier"
    value: "4881.43"
    work: "Within the recovery period"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19_2025"
    value: "6356.03"
    work: "Mid-quarter test is met, so the MQ amount"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line20"
    value: "4881.43"
    work: "Lesser of 5,226.90 or 4,881.43"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].b100"
    value: "47506.00"
    work: "47,506 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r1"
    value: "20.00%"
    work: "HY, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t1"
    value: "9501.20"
    work: "47,506 x 20%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t1s"
    value: "9501.20"
    work: "0 + 9,501.20"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r2"
    value: "32.00%"
    work: "HY, year 2"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t2"
    value: "15201.92"
    work: "47,506 x 32%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].l2"
    value: "16400.00"
    work: "2021 year 2 limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].d2"
    value: "15201.92"
    work: "Lesser of 16,400 or 15,201.92"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r3"
    value: "19.20%"
    work: "HY, year 3"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t3"
    value: "9121.15"
    work: "47,506 x 19.20%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].l3"
    value: "9800.00"
    work: "2021 year 3 limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].d3"
    value: "9121.15"
    work: "Lesser of 9,800 or 9,121.15"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r4"
    value: "11.52%"
    work: "HY, year 4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t4"
    value: "5472.69"
    work: "47,506 x 11.52%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].l4"
    value: "5860.00"
    work: "2021 limit, year 4 or later"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].d4"
    value: "5472.69"
    work: "Lesser of 5,860 or 5,472.69"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r5"
    value: "11.52%"
    work: "HY, year 5"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t5"
    value: "5472.69"
    work: "47,506 x 11.52%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].l5"
    value: "5860.00"
    work: "2021 limit, year 4 or later"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].d5"
    value: "5472.69"
    work: "Lesser of 5,860 or 5,472.69"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r6"
    value: "5.76%"
    work: "HY, year 6"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t6"
    value: "2736.35"
    work: "47,506 x 5.76%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].too_old"
    value: "no"
    work: "Placed in service 2021"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_v"
    value: "0.00"
    work: "bonus_allowed is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].macrs_pass"
    value: "4881.43"
    work: "Line 20"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].macrs_heavy"
    value: "4881.43"
    work: "Line 19 with no limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].macrs_v"
    value: "4881.43"
    work: "Subject to the auto limits, so the passenger column"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus"
    value: "0.00"
    work: "bonus_o"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].macrs"
    value: "4881.43"
    work: "macrs_o"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].s179_2025"
    value: "0.00"
    work: "s179_2025_o"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_q4"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_total"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].cost179"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_o"
    value: "0.00"
    work: "Owned on actual expenses: bonus_v 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].macrs_o"
    value: "4881.43"
    work: "Owned on actual expenses: macrs_v"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].s179_2025_o"
    value: "0.00"
    work: "s179_2025_ok is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].q4_basis"
    value: "0.00"
    work: "Placed in service in Q3, not Q4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_q4_o"
    value: "0.00"
    work: "mq_q4_a2 is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_q4_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_total_o"
    value: "0.00"
    work: "mq_total_a2 is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_total_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].cost179_o"
    value: "0.00"
    work: "cost179_a2 is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].cost179_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
```
```
