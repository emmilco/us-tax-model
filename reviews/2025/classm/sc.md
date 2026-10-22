# Class M hand-work — sc

`Schedule C (Form 1040) — Profit or Loss From Business, one per business` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-21 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| subject sha256 | 1044cc4d28f7e00532ffdf3afb6eb0078c69f310eccb8649ad7a2aebae9d259e |
| cases | 4 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sc | 2025 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sse | 2025; created 2025-05-07 | 1, 2 | whole document | d214b41a4e42da1953a1ee216b6f9d263be284a90cf9f7f28dcb87cd0e9913e6 | - | fbeaf5e9b8509f8fe754b52a6b5a643934ae2ff1a6f76e6e69af8be42fcd2cdd |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| p946 | For use in preparing 2025 returns | 17, 18, 19, 34 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 18, 19, 34 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |
| f4562 | 2025; created 2025-10-09 | 1, 2, 3 | whole document | 71e2ace527072aaa7293e77897bb4ab8e473fa9c47b6b1ccb977fdc58a93bc2d | - | a1330c49d931e7ecdc867aef2d9e01390fc7b4d7e9321943a21ed0f8e883ed18 |
| i4562 | 2025 | 4, 5, 9, 10, 13, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 5, 9, 10, 13, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| f7206 | 2025; created 2025-10-02 | 1 | whole document | 1f54af11e092a24258ac71f29d2bcfeeda1d6100ca332357d4569eea889e1dbb | - | e3b265efad583dd859c584d4e7e8a17d7b6e927878922ab5f020e2ff79a18d87 |
| i1040gi | 2025; printed date 2026-02-25 | 94, 95, 104, 108 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 95, 104 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i8995 | 2025; printed date 2026-01-26 | 2, 4, 6 | cited pages | 96284eaad2fe5ec324de9fd4335cea9ea3260e66ff1d8b1725c1cff7fbe1ddc2 | 2, 4, 6 | 6671a64ba0011f89e03eb5985954073dcd984b3f346495182916b0ecaa42ec1a |
| i7206 | 2025 | 1, 2 | whole document | 88aebffe01e22b57dadeb703483459075718cb0b2514fe8f00185975cfbeef3a | 1, 2 | 5bfa308e7e4634d4a0162d76b4af6a4182b8539a390109360875303222231cfe |

## Lines

### case classm.sc.1 — prompt sha256 5df2c6158d7e0e7e0e52c500065a4b96d90bc2836d0f5417424d1cf168bcdc58; branches: sc.rrta:false, sc.statutory:false, sc.passive:true, sc.spouse_owned:false, sc.method_other:false, sc.special:false, sc.screened:false, sc.ho_uses:false, sc.ho_uses:true, sc.ho_other:false, sc.ho_screened:false, sc.ho_multi:false, sc.ho_over:false, sc.ho_over:true, sc.ho_line4#0, sc.ho_line4#1, sc.ho_unlimited:false, sc.ho_unlimited:true, sc.ho_no179:true, sc.ho_limited:left, sc.ho_limited:right, sc.ho_pre179_floor:floor, sc.ho_pre179_floor:positive, sc.ho_both_limits:false, sc.ho_line5_lim#0, sc.ho_line5#0, sc.ho_line5#1, sc.line30#0, sc.line30#1, sc.loss:false, sc.loss:true, sc.at_risk:true, sc.not_at_risk:false, sc.result#0, sc.result#1, sc.inventory_other:false, sc.s179_allowed#0, sc.profit_pos:floor, sc.profit_pos:positive, sc.hi_uses:false, sc.hi_screen:false, sc.hi_screened:false, sc.f7206_has:false, sc.f7206_has:true, sc.f7206_line7#0, sc.f7206_line7#1, sc.f7206_line8:floor, sc.f7206_line8:positive, sc.f7206_line9#0, sc.f7206_line9#1, sc.f7206_line10:floor, sc.f7206_line10:positive, sc.f7206_min:left, sc.f7206_line14#1, sc.qbi_has:false, sc.qbi_has:true, sc.qbi_se#0, sc.qbi_se#1, sc.qbi_plan#0, sc.qbi_plan#1, sc.tips_ot:false

### classm.sc.1 — person[taxpayer].sc[biz_a].rrta — This business's owner has railroad retirement compensation
Status: **AGREE**

Value: no

### classm.sc.1 — person[taxpayer].sc[biz_a].screened — Something on this Schedule C is outside this tool
Status: **AGREE**

Value: no

### classm.sc.1 — person[taxpayer].sc[biz_a].line3 — Subtract line 2 from line 1
Status: **AGREE**

Value: $188,155.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line4 — Cost of goods sold (from line 42)
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line5 — Gross profit. Subtract line 4 from line 3
Status: **AGREE**

Value: $188,155.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line7 — Gross income. Add lines 5 and 6
Status: **AGREE**

Value: $188,155.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line9 — Car and truck expenses
Status: **AGREE**

Value: $19,703.70

### classm.sc.1 — person[taxpayer].sc[biz_a].line12 — Depletion
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line13 — Depreciation and section 179 expense deduction (not included in Part III)
Status: **AGREE**

Value: $2,536.10

### classm.sc.1 — person[taxpayer].sc[biz_a].line20a — Rent or lease: vehicles, machinery, and equipment
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].meals_50_ded — 50% of the meals subject to the 50% limit
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].meals_80_ded — 80% of the meals under the hours of service limits
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line24b — Deductible meals
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line27a — Energy efficient commercial buildings deduction (attach Form 7205)
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line27b — Other expenses (from line 48)
Status: **AGREE**

Value: $12,210.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line28 — Total expenses before expenses for business use of home. Add lines 8 through 27b
Status: **AGREE**

Value: $64,607.80

### classm.sc.1 — person[taxpayer].sc[biz_a].line29 — Tentative profit or (loss). Subtract line 28 from line 7
Status: **AGREE**

Value: $123,547.20

### classm.sc.1 — person[taxpayer].sc[biz_a].line28_pre179 — Line 28 without the section 179 expense deduction
Status: **AGREE**

Value: $64,607.80

### classm.sc.1 — person[taxpayer].sc[biz_a].line29_pre179 — Line 29 without the section 179 expense deduction
Status: **AGREE**

Value: $123,547.20

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_screened — The home office deduction is outside the simplified method this tool covers
Status: **AGREE**

Value: no

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_multi — This person claims the business use of the home for more than one business
Status: **AGREE**

Value: no

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_over — More than 300 square feet
Status: **AGREE**

Value: no

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_line4_actual — Line 2 (the square feet used) times line 3c
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_line4_cap — 300 square feet times line 3c
Status: **AGREE**

Value: $1,500.00

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_line4 — Multiply line 2 by line 3c
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_line1 — Gross income limitation (Schedule C, line 29)
Status: **AGREE**

Value: $123,547.20

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_room — Line 29 without the section 179 deduction, less the most section 179 deduction t
Status: **AGREE**

Value: $123,547.20

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_unlimited — Line 4 is not more than the smallest line 29 any section 179 allocation could gi
Status: **AGREE**

Value: yes

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_s179_max — The most section 179 deduction this business could take, its 2025 elections plus
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_no179 — No section 179 deduction is possible for this business (no 2025 election and no 
Status: **AGREE**

Value: yes

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_limited — The smaller of line 1 or line 4, with no section 179 election (line 1 is line 29
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_pre179_floor — Line 29 without the section 179 deduction, if zero or less zero
Status: **AGREE**

Value: $123,547.20

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_both_limits — The gross income limitation could bind together with the section 179 business in
Status: **AGREE**

Value: no

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_both — Line 5 when both income limits could bind
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_line5_lim — Line 5 when line 4 is more than the room left by the section 179 elections
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_line5 — Allowable expenses using the simplified method. Enter the smaller of line 1 or l
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line30 — Expenses for business use of your home
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line31 — Net profit or (loss). Subtract line 30 from line 29
Status: **AGREE**

Value: $123,547.20

### classm.sc.1 — person[taxpayer].sc[biz_a].line31_pre179 — Line 31 without the section 179 expense deduction
Status: **AGREE**

Value: $123,547.20

### classm.sc.1 — person[taxpayer].sc[biz_a].loss — Line 31 is a loss
Status: **AGREE**

Value: no

### classm.sc.1 — person[taxpayer].sc[biz_a].not_at_risk — Some investment is not at risk (box 32b)
Status: **AGREE**

Value: no

### classm.sc.1 — person[taxpayer].sc[biz_a].loss_allowed — The loss on line 31 when all investment is at risk
Status: **DISAGREE**

Project: $123,547.20
Model: $0.00
Work: No loss

Ruling: helper of a branch this entry does not take; project retained. The loss line of a business with a profit, the Form 7206 lines of a business under which no plan is established, and the Pub. 946 two-limit helpers of a home office whose line 5 takes another branch are figured by the project but read by no line this entry reaches; the printed lines they would feed (line 31, Form 7206 lines 4 to 14 of the plan's business, line 30) agree. The model entered zero or its own figure for an unused helper. Dropped from the fixture as not evidence. [dropped]

### classm.sc.1 — person[taxpayer].sc[biz_a].result — The amount for Schedule 1, line 3 and Schedule SE, line 2
Status: **AGREE**

Value: $123,547.20

### classm.sc.1 — person[taxpayer].sc[biz_a].line40 — Add lines 35 through 39
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line42 — Cost of goods sold. Subtract line 41 from line 40
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f6 — Section 179 elected on property other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f14 — Special allowance on property other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f17 — MACRS on earlier property other than listed property
Status: **AGREE**

Value: $2,536.10

### classm.sc.1 — person[taxpayer].sc[biz_a].f19_y3 — MACRS on 2025 property of period y3 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f19_y5 — MACRS on 2025 property of period y5 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f19_y7 — MACRS on 2025 property of period y7 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f19_y10 — MACRS on 2025 property of period y10 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f19_y15 — MACRS on 2025 property of period y15 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f19_y20 — MACRS on 2025 property of period y20 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f19_y15sl — MACRS on 2025 property of period y15sl other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f25_assets — Special allowance on listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f25_veh — Special allowance on vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f25 — Line 25 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f26_assets — Column (h) of listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f26_veh — Column (h) of vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f26h — Column (h), line 26, for this business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f28 — Line 28 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f29_assets — Section 179 elected on listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f29_veh — Section 179 on vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f29 — Line 29 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].s179_elected — Section 179 elected for this business's 2025 property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].dep_other — Depreciation other than the section 179 deduction (Form 4562 lines 14, 17, 19 an
Status: **AGREE**

Value: $2,536.10

### classm.sc.1 — person[taxpayer].sc[biz_a].s179_return — The return's section 179 deduction, for its only Schedule C
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].s179_allowed — Section 179 expense deduction for this business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].mq_q4_a — mq_q4 of this business's property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].mq_q4_v — mq_q4 of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].mq_q4 — mq_q4 of this business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].mq_total_a — mq_total of this business's property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].mq_total_v — mq_total of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].mq_total — mq_total of this business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].cost179_a — cost179 of this business's property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].cost179_v — cost179 of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].cost179 — cost179 of this business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].veh_lease — Business part of vehicle lease payments
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].profit_pos — Net profit of this business (zero for a loss)
Status: **AGREE**

Value: $123,547.20

### classm.sc.1 — person[taxpayer].sc[biz_a].hi_screened — This health insurance deduction is outside this tool
Status: **AGREE**

Value: no

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_line2 — Qualified long-term care insurance (the smaller of payments or the age limit, fo
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_line3 — Add lines 1 and 2
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_line4 — Net profit from the trade or business under which the insurance plan is establis
Status: **AGREE**

Value: $123,547.20

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_line5 — Total of all net profits from Schedule C, line 31
Status: **AGREE**

Value: $123,547.20

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_has — Line 4 is more than zero
Status: **AGREE**

Value: yes

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_line7_pos — Schedule 1, line 15 (this person's), times line 4 divided by line 5
Status: **AGREE**

Value: $6,574.20

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_line7 — Multiply Schedule 1 (Form 1040), line 15, deductible part of self-employment tax
Status: **AGREE**

Value: $6,574.20

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_line8 — Subtract line 7 from line 4
Status: **AGREE**

Value: $116,973.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_line9_pos — This person's SEP or SIMPLE deduction times line 4 divided by line 5
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_line9 — Schedule 1, line 16, attributable to the same trade or business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_line10 — Subtract line 9 from line 8
Status: **AGREE**

Value: $116,973.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_line13 — Subtract line 12 from line 10
Status: **AGREE**

Value: $116,973.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_min — The smaller of line 3 or line 13
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_line14 — Self-employed health insurance deduction
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].qbi_has — This business has a net profit
Status: **AGREE**

Value: yes

### classm.sc.1 — person[taxpayer].sc[biz_a].qbi_se_pos — This person's deductible part of self-employment tax attributable to this busine
Status: **AGREE**

Value: $6,574.20

### classm.sc.1 — person[taxpayer].sc[biz_a].qbi_se — Deductible part of self-employment tax attributable to this business
Status: **AGREE**

Value: $6,574.20

### classm.sc.1 — person[taxpayer].sc[biz_a].qbi_plan_pos — This person's SEP or SIMPLE deduction attributable to this business (by share of
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].qbi_plan — SEP or SIMPLE deduction attributable to this business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].qbi_ded — Deductions attributable to this business: self-employment tax, retirement plan a
Status: **AGREE**

Value: $6,574.20

### classm.sc.1 — person[taxpayer].sc[biz_a].qbi — Qualified business income or (loss) of this business
Status: **AGREE**

Value: $116,973.00

### classm.sc.1 — person[taxpayer].sc[biz_b].rrta — This business's owner has railroad retirement compensation
Status: **AGREE**

Value: no

### classm.sc.1 — person[taxpayer].sc[biz_b].screened — Something on this Schedule C is outside this tool
Status: **AGREE**

Value: no

### classm.sc.1 — person[taxpayer].sc[biz_b].line3 — Subtract line 2 from line 1
Status: **AGREE**

Value: $11,971.00

### classm.sc.1 — person[taxpayer].sc[biz_b].line4 — Cost of goods sold (from line 42)
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].line5 — Gross profit. Subtract line 4 from line 3
Status: **AGREE**

Value: $11,971.00

### classm.sc.1 — person[taxpayer].sc[biz_b].line7 — Gross income. Add lines 5 and 6
Status: **AGREE**

Value: $11,971.00

### classm.sc.1 — person[taxpayer].sc[biz_b].line9 — Car and truck expenses
Status: **AGREE**

Value: $7,914.20

### classm.sc.1 — person[taxpayer].sc[biz_b].line12 — Depletion
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].line13 — Depreciation and section 179 expense deduction (not included in Part III)
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].line20a — Rent or lease: vehicles, machinery, and equipment
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].meals_50_ded — 50% of the meals subject to the 50% limit
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].meals_80_ded — 80% of the meals under the hours of service limits
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].line24b — Deductible meals
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].line27a — Energy efficient commercial buildings deduction (attach Form 7205)
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].line27b — Other expenses (from line 48)
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].line28 — Total expenses before expenses for business use of home. Add lines 8 through 27b
Status: **AGREE**

Value: $42,462.20

### classm.sc.1 — person[taxpayer].sc[biz_b].line29 — Tentative profit or (loss). Subtract line 28 from line 7
Status: **AGREE**

Value: $-30,491.20

### classm.sc.1 — person[taxpayer].sc[biz_b].line28_pre179 — Line 28 without the section 179 expense deduction
Status: **AGREE**

Value: $42,462.20

### classm.sc.1 — person[taxpayer].sc[biz_b].line29_pre179 — Line 29 without the section 179 expense deduction
Status: **AGREE**

Value: $-30,491.20

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_screened — The home office deduction is outside the simplified method this tool covers
Status: **AGREE**

Value: no

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_multi — This person claims the business use of the home for more than one business
Status: **AGREE**

Value: no

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_over — More than 300 square feet
Status: **AGREE**

Value: yes

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_line4_actual — Line 2 (the square feet used) times line 3c
Status: **AGREE**

Value: $1,695.00

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_line4_cap — 300 square feet times line 3c
Status: **AGREE**

Value: $1,500.00

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_line4 — Multiply line 2 by line 3c
Status: **AGREE**

Value: $1,500.00

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_line1 — Gross income limitation (Schedule C, line 29)
Status: **AGREE**

Value: $-30,491.20

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_room — Line 29 without the section 179 deduction, less the most section 179 deduction t
Status: **AGREE**

Value: $-30,491.20

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_unlimited — Line 4 is not more than the smallest line 29 any section 179 allocation could gi
Status: **AGREE**

Value: no

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_s179_max — The most section 179 deduction this business could take, its 2025 elections plus
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_no179 — No section 179 deduction is possible for this business (no 2025 election and no 
Status: **AGREE**

Value: yes

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_limited — The smaller of line 1 or line 4, with no section 179 election (line 1 is line 29
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_pre179_floor — Line 29 without the section 179 deduction, if zero or less zero
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_both_limits — The gross income limitation could bind together with the section 179 business in
Status: **AGREE**

Value: no

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_both — Line 5 when both income limits could bind
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_line5_lim — Line 5 when line 4 is more than the room left by the section 179 elections
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_line5 — Allowable expenses using the simplified method. Enter the smaller of line 1 or l
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].line30 — Expenses for business use of your home
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].line31 — Net profit or (loss). Subtract line 30 from line 29
Status: **AGREE**

Value: $-30,491.20

### classm.sc.1 — person[taxpayer].sc[biz_b].line31_pre179 — Line 31 without the section 179 expense deduction
Status: **AGREE**

Value: $-30,491.20

### classm.sc.1 — person[taxpayer].sc[biz_b].loss — Line 31 is a loss
Status: **AGREE**

Value: yes

### classm.sc.1 — person[taxpayer].sc[biz_b].not_at_risk — Some investment is not at risk (box 32b)
Status: **AGREE**

Value: no

### classm.sc.1 — person[taxpayer].sc[biz_b].loss_allowed — The loss on line 31 when all investment is at risk
Status: **AGREE**

Value: $-30,491.20

### classm.sc.1 — person[taxpayer].sc[biz_b].result — The amount for Schedule 1, line 3 and Schedule SE, line 2
Status: **AGREE**

Value: $-30,491.20

### classm.sc.1 — person[taxpayer].sc[biz_b].line40 — Add lines 35 through 39
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].line42 — Cost of goods sold. Subtract line 41 from line 40
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f6 — Section 179 elected on property other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f14 — Special allowance on property other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f17 — MACRS on earlier property other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f19_y3 — MACRS on 2025 property of period y3 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f19_y5 — MACRS on 2025 property of period y5 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f19_y7 — MACRS on 2025 property of period y7 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f19_y10 — MACRS on 2025 property of period y10 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f19_y15 — MACRS on 2025 property of period y15 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f19_y20 — MACRS on 2025 property of period y20 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f19_y15sl — MACRS on 2025 property of period y15sl other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f25_assets — Special allowance on listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f25_veh — Special allowance on vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f25 — Line 25 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f26_assets — Column (h) of listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f26_veh — Column (h) of vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f26h — Column (h), line 26, for this business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f28 — Line 28 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f29_assets — Section 179 elected on listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f29_veh — Section 179 on vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f29 — Line 29 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].s179_elected — Section 179 elected for this business's 2025 property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].dep_other — Depreciation other than the section 179 deduction (Form 4562 lines 14, 17, 19 an
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].s179_return — The return's section 179 deduction, for its only Schedule C
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].s179_allowed — Section 179 expense deduction for this business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].mq_q4_a — mq_q4 of this business's property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].mq_q4_v — mq_q4 of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].mq_q4 — mq_q4 of this business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].mq_total_a — mq_total of this business's property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].mq_total_v — mq_total of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].mq_total — mq_total of this business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].cost179_a — cost179 of this business's property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].cost179_v — cost179 of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].cost179 — cost179 of this business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].veh_lease — Business part of vehicle lease payments
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].profit_pos — Net profit of this business (zero for a loss)
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].hi_screened — This health insurance deduction is outside this tool
Status: **AGREE**

Value: no

### classm.sc.1 — person[taxpayer].sc[biz_b].f7206_line2 — Qualified long-term care insurance (the smaller of payments or the age limit, fo
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f7206_line3 — Add lines 1 and 2
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f7206_line4 — Net profit from the trade or business under which the insurance plan is establis
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f7206_line5 — Total of all net profits from Schedule C, line 31
Status: **AGREE**

Value: $123,547.20

### classm.sc.1 — person[taxpayer].sc[biz_b].f7206_has — Line 4 is more than zero
Status: **AGREE**

Value: no

### classm.sc.1 — person[taxpayer].sc[biz_b].f7206_line7_pos — Schedule 1, line 15 (this person's), times line 4 divided by line 5
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f7206_line7 — Multiply Schedule 1 (Form 1040), line 15, deductible part of self-employment tax
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f7206_line8 — Subtract line 7 from line 4
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f7206_line9_pos — This person's SEP or SIMPLE deduction times line 4 divided by line 5
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f7206_line9 — Schedule 1, line 16, attributable to the same trade or business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f7206_line10 — Subtract line 9 from line 8
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f7206_line13 — Subtract line 12 from line 10
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f7206_min — The smaller of line 3 or line 13
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f7206_line14 — Self-employed health insurance deduction
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].qbi_has — This business has a net profit
Status: **AGREE**

Value: no

### classm.sc.1 — person[taxpayer].sc[biz_b].qbi_se_pos — This person's deductible part of self-employment tax attributable to this busine
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].qbi_se — Deductible part of self-employment tax attributable to this business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].qbi_plan_pos — This person's SEP or SIMPLE deduction attributable to this business (by share of
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].qbi_plan — SEP or SIMPLE deduction attributable to this business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].qbi_ded — Deductions attributable to this business: self-employment tax, retirement plan a
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].qbi — Qualified business income or (loss) of this business
Status: **AGREE**

Value: $-30,491.20

### case classm.sc.2 — prompt sha256 6191810d27b0fe6990e70247ba833e92cea36f4b801102dcf54e355d430c3339; branches: sc.rrta:false, sc.statutory:false, sc.passive:true, sc.spouse_owned:false, sc.method_other:false, sc.special:false, sc.screened:false, sc.ho_uses:false, sc.ho_other:false, sc.ho_screened:false, sc.ho_multi:false, sc.ho_over:false, sc.ho_line4#0, sc.ho_unlimited:true, sc.ho_no179:false, sc.ho_no179:true, sc.ho_limited:left, sc.ho_pre179_floor:positive, sc.ho_both_limits:false, sc.ho_line5_lim#0, sc.ho_line5_lim#1, sc.ho_line5#0, sc.line30#1, sc.loss:false, sc.at_risk:true, sc.not_at_risk:false, sc.result#0, sc.inventory_other:false, sc.s179_allowed#0, sc.profit_pos:positive, sc.hi_uses:false, sc.hi_uses:true, sc.hi_screen:false, sc.hi_screened:false, sc.f7206_has:true, sc.f7206_line7#0, sc.f7206_line8:positive, sc.f7206_line9#0, sc.f7206_line10:positive, sc.f7206_min:left, sc.f7206_line14#0, sc.f7206_line14#1, sc.qbi_has:true, sc.qbi_se#0, sc.qbi_plan#0, sc.tips_ot:false

### classm.sc.2 — person[taxpayer].sc[biz_a].rrta — This business's owner has railroad retirement compensation
Status: **AGREE**

Value: no

### classm.sc.2 — person[taxpayer].sc[biz_a].screened — Something on this Schedule C is outside this tool
Status: **AGREE**

Value: no

### classm.sc.2 — person[taxpayer].sc[biz_a].line3 — Subtract line 2 from line 1
Status: **AGREE**

Value: $120,791.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line4 — Cost of goods sold (from line 42)
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line5 — Gross profit. Subtract line 4 from line 3
Status: **AGREE**

Value: $120,791.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line7 — Gross income. Add lines 5 and 6
Status: **AGREE**

Value: $120,791.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line9 — Car and truck expenses
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line12 — Depletion
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line13 — Depreciation and section 179 expense deduction (not included in Part III)
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line20a — Rent or lease: vehicles, machinery, and equipment
Status: **AGREE**

Value: $5,873.00

### classm.sc.2 — person[taxpayer].sc[biz_a].meals_50_ded — 50% of the meals subject to the 50% limit
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].meals_80_ded — 80% of the meals under the hours of service limits
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line24b — Deductible meals
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line27a — Energy efficient commercial buildings deduction (attach Form 7205)
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line27b — Other expenses (from line 48)
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line28 — Total expenses before expenses for business use of home. Add lines 8 through 27b
Status: **AGREE**

Value: $22,409.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line29 — Tentative profit or (loss). Subtract line 28 from line 7
Status: **AGREE**

Value: $98,382.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line28_pre179 — Line 28 without the section 179 expense deduction
Status: **AGREE**

Value: $22,409.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line29_pre179 — Line 29 without the section 179 expense deduction
Status: **AGREE**

Value: $98,382.00

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_screened — The home office deduction is outside the simplified method this tool covers
Status: **AGREE**

Value: no

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_multi — This person claims the business use of the home for more than one business
Status: **AGREE**

Value: no

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_over — More than 300 square feet
Status: **AGREE**

Value: no

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_line4_actual — Line 2 (the square feet used) times line 3c
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_line4_cap — 300 square feet times line 3c
Status: **DISAGREE**

Project: $1,500.00
Model: $0.00
Work: No simplified method used

Ruling: helper of a branch this entry does not take; project retained. The business claims no home office (sc.ho_uses is false), so sc.ho_line4_cap, 300 square feet times $5, is figured but read by no line this entry reaches (sc.line30 is zero, and lines 30 and 31 agree); the model entered zero for an unused helper. Dropped from the fixture as not evidence. [dropped]

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_line4 — Multiply line 2 by line 3c
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_line1 — Gross income limitation (Schedule C, line 29)
Status: **AGREE**

Value: $98,382.00

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_room — Line 29 without the section 179 deduction, less the most section 179 deduction t
Status: **AGREE**

Value: $98,382.00

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_unlimited — Line 4 is not more than the smallest line 29 any section 179 allocation could gi
Status: **AGREE**

Value: yes

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_s179_max — The most section 179 deduction this business could take, its 2025 elections plus
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_no179 — No section 179 deduction is possible for this business (no 2025 election and no 
Status: **AGREE**

Value: yes

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_limited — The smaller of line 1 or line 4, with no section 179 election (line 1 is line 29
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_pre179_floor — Line 29 without the section 179 deduction, if zero or less zero
Status: **AGREE**

Value: $98,382.00

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_both_limits — The gross income limitation could bind together with the section 179 business in
Status: **AGREE**

Value: no

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_both — Line 5 when both income limits could bind
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_line5_lim — Line 5 when line 4 is more than the room left by the section 179 elections
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_line5 — Allowable expenses using the simplified method. Enter the smaller of line 1 or l
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line30 — Expenses for business use of your home
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line31 — Net profit or (loss). Subtract line 30 from line 29
Status: **AGREE**

Value: $98,382.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line31_pre179 — Line 31 without the section 179 expense deduction
Status: **AGREE**

Value: $98,382.00

### classm.sc.2 — person[taxpayer].sc[biz_a].loss — Line 31 is a loss
Status: **AGREE**

Value: no

### classm.sc.2 — person[taxpayer].sc[biz_a].not_at_risk — Some investment is not at risk (box 32b)
Status: **AGREE**

Value: no

### classm.sc.2 — person[taxpayer].sc[biz_a].loss_allowed — The loss on line 31 when all investment is at risk
Status: **DISAGREE**

Project: $98,382.00
Model: $0.00
Work: No loss

Ruling: helper of a branch this entry does not take; project retained. The loss line of a business with a profit, the Form 7206 lines of a business under which no plan is established, and the Pub. 946 two-limit helpers of a home office whose line 5 takes another branch are figured by the project but read by no line this entry reaches; the printed lines they would feed (line 31, Form 7206 lines 4 to 14 of the plan's business, line 30) agree. The model entered zero or its own figure for an unused helper. Dropped from the fixture as not evidence. [dropped]

### classm.sc.2 — person[taxpayer].sc[biz_a].result — The amount for Schedule 1, line 3 and Schedule SE, line 2
Status: **AGREE**

Value: $98,382.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line40 — Add lines 35 through 39
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line42 — Cost of goods sold. Subtract line 41 from line 40
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f6 — Section 179 elected on property other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f14 — Special allowance on property other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f17 — MACRS on earlier property other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f19_y3 — MACRS on 2025 property of period y3 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f19_y5 — MACRS on 2025 property of period y5 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f19_y7 — MACRS on 2025 property of period y7 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f19_y10 — MACRS on 2025 property of period y10 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f19_y15 — MACRS on 2025 property of period y15 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f19_y20 — MACRS on 2025 property of period y20 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f19_y15sl — MACRS on 2025 property of period y15sl other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f25_assets — Special allowance on listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f25_veh — Special allowance on vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f25 — Line 25 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f26_assets — Column (h) of listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f26_veh — Column (h) of vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f26h — Column (h), line 26, for this business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f28 — Line 28 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f29_assets — Section 179 elected on listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f29_veh — Section 179 on vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f29 — Line 29 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].s179_elected — Section 179 elected for this business's 2025 property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].dep_other — Depreciation other than the section 179 deduction (Form 4562 lines 14, 17, 19 an
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].s179_return — The return's section 179 deduction, for its only Schedule C
Status: **DISAGREE**

Project: $2,527.00
Model: $0.00
Work: Return has two Schedules C, not one

Ruling: helper of a branch this entry does not take; project retained. sc.s179_return (Form 4562 line 12 of the return, for its only Schedule C) is read by line 12 only when the return's deduction differs from the 2025 elections (s179.differs); here it does not (sc.s179_allowed takes sc.s179_elected, branch sc.s179_allowed#0), so the copy of $2,527.00 is figured but unused, and sc.s179_allowed of both businesses agrees ($0.00 and $2,527.00). The model entered zero because the return has two Schedules C. Dropped from the fixture as not evidence. [dropped]

### classm.sc.2 — person[taxpayer].sc[biz_a].s179_allowed — Section 179 expense deduction for this business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].mq_q4_a — mq_q4 of this business's property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].mq_q4_v — mq_q4 of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].mq_q4 — mq_q4 of this business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].mq_total_a — mq_total of this business's property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].mq_total_v — mq_total of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].mq_total — mq_total of this business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].cost179_a — cost179 of this business's property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].cost179_v — cost179 of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].cost179 — cost179 of this business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].veh_lease — Business part of vehicle lease payments
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].profit_pos — Net profit of this business (zero for a loss)
Status: **AGREE**

Value: $98,382.00

### classm.sc.2 — person[taxpayer].sc[biz_a].hi_screened — This health insurance deduction is outside this tool
Status: **AGREE**

Value: no

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_line2 — Qualified long-term care insurance (the smaller of payments or the age limit, fo
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_line3 — Add lines 1 and 2
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_line4 — Net profit from the trade or business under which the insurance plan is establis
Status: **AGREE**

Value: $98,382.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_line5 — Total of all net profits from Schedule C, line 31
Status: **AGREE**

Value: $170,500.18

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_has — Line 4 is more than zero
Status: **AGREE**

Value: yes

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_line7_pos — Schedule 1, line 15 (this person's), times line 4 divided by line 5
Status: **AGREE**

Value: $6,519.52

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_line7 — Multiply Schedule 1 (Form 1040), line 15, deductible part of self-employment tax
Status: **AGREE**

Value: $6,519.52

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_line8 — Subtract line 7 from line 4
Status: **AGREE**

Value: $91,862.48

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_line9_pos — This person's SEP or SIMPLE deduction times line 4 divided by line 5
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_line9 — Schedule 1, line 16, attributable to the same trade or business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_line10 — Subtract line 9 from line 8
Status: **AGREE**

Value: $91,862.48

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_line13 — Subtract line 12 from line 10
Status: **AGREE**

Value: $91,862.48

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_min — The smaller of line 3 or line 13
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_line14 — Self-employed health insurance deduction
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].qbi_has — This business has a net profit
Status: **AGREE**

Value: yes

### classm.sc.2 — person[taxpayer].sc[biz_a].qbi_se_pos — This person's deductible part of self-employment tax attributable to this busine
Status: **AGREE**

Value: $6,519.52

### classm.sc.2 — person[taxpayer].sc[biz_a].qbi_se — Deductible part of self-employment tax attributable to this business
Status: **AGREE**

Value: $6,519.52

### classm.sc.2 — person[taxpayer].sc[biz_a].qbi_plan_pos — This person's SEP or SIMPLE deduction attributable to this business (by share of
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].qbi_plan — SEP or SIMPLE deduction attributable to this business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].qbi_ded — Deductions attributable to this business: self-employment tax, retirement plan a
Status: **AGREE**

Value: $6,519.52

### classm.sc.2 — person[taxpayer].sc[biz_a].qbi — Qualified business income or (loss) of this business
Status: **AGREE**

Value: $91,862.48

### classm.sc.2 — person[taxpayer].sc[biz_b].rrta — This business's owner has railroad retirement compensation
Status: **AGREE**

Value: no

### classm.sc.2 — person[taxpayer].sc[biz_b].screened — Something on this Schedule C is outside this tool
Status: **AGREE**

Value: no

### classm.sc.2 — person[taxpayer].sc[biz_b].line3 — Subtract line 2 from line 1
Status: **AGREE**

Value: $165,450.00

### classm.sc.2 — person[taxpayer].sc[biz_b].line4 — Cost of goods sold (from line 42)
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].line5 — Gross profit. Subtract line 4 from line 3
Status: **AGREE**

Value: $165,450.00

### classm.sc.2 — person[taxpayer].sc[biz_b].line7 — Gross income. Add lines 5 and 6
Status: **AGREE**

Value: $165,450.00

### classm.sc.2 — person[taxpayer].sc[biz_b].line9 — Car and truck expenses
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].line12 — Depletion
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].line13 — Depreciation and section 179 expense deduction (not included in Part III)
Status: **AGREE**

Value: $17,264.82

### classm.sc.2 — person[taxpayer].sc[biz_b].line20a — Rent or lease: vehicles, machinery, and equipment
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].meals_50_ded — 50% of the meals subject to the 50% limit
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].meals_80_ded — 80% of the meals under the hours of service limits
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].line24b — Deductible meals
Status: **AGREE**

Value: $25,846.00

### classm.sc.2 — person[taxpayer].sc[biz_b].line27a — Energy efficient commercial buildings deduction (attach Form 7205)
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].line27b — Other expenses (from line 48)
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].line28 — Total expenses before expenses for business use of home. Add lines 8 through 27b
Status: **AGREE**

Value: $93,331.82

### classm.sc.2 — person[taxpayer].sc[biz_b].line29 — Tentative profit or (loss). Subtract line 28 from line 7
Status: **AGREE**

Value: $72,118.18

### classm.sc.2 — person[taxpayer].sc[biz_b].line28_pre179 — Line 28 without the section 179 expense deduction
Status: **AGREE**

Value: $90,804.82

### classm.sc.2 — person[taxpayer].sc[biz_b].line29_pre179 — Line 29 without the section 179 expense deduction
Status: **AGREE**

Value: $74,645.18

### classm.sc.2 — person[taxpayer].sc[biz_b].ho_screened — The home office deduction is outside the simplified method this tool covers
Status: **AGREE**

Value: no

### classm.sc.2 — person[taxpayer].sc[biz_b].ho_multi — This person claims the business use of the home for more than one business
Status: **AGREE**

Value: no

### classm.sc.2 — person[taxpayer].sc[biz_b].ho_over — More than 300 square feet
Status: **AGREE**

Value: no

### classm.sc.2 — person[taxpayer].sc[biz_b].ho_line4_actual — Line 2 (the square feet used) times line 3c
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].ho_line4_cap — 300 square feet times line 3c
Status: **DISAGREE**

Project: $1,500.00
Model: $0.00
Work: No simplified method used

Ruling: helper of a branch this entry does not take; project retained. The business claims no home office (sc.ho_uses is false), so sc.ho_line4_cap, 300 square feet times $5, is figured but read by no line this entry reaches (sc.line30 is zero); the model entered zero for an unused helper. Dropped from the fixture as not evidence. [dropped]

### classm.sc.2 — person[taxpayer].sc[biz_b].ho_line4 — Multiply line 2 by line 3c
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].ho_line1 — Gross income limitation (Schedule C, line 29)
Status: **AGREE**

Value: $72,118.18

### classm.sc.2 — person[taxpayer].sc[biz_b].ho_room — Line 29 without the section 179 deduction, less the most section 179 deduction t
Status: **AGREE**

Value: $72,118.18

### classm.sc.2 — person[taxpayer].sc[biz_b].ho_unlimited — Line 4 is not more than the smallest line 29 any section 179 allocation could gi
Status: **AGREE**

Value: yes

### classm.sc.2 — person[taxpayer].sc[biz_b].ho_s179_max — The most section 179 deduction this business could take, its 2025 elections plus
Status: **AGREE**

Value: $2,527.00

### classm.sc.2 — person[taxpayer].sc[biz_b].ho_no179 — No section 179 deduction is possible for this business (no 2025 election and no 
Status: **AGREE**

Value: no

### classm.sc.2 — person[taxpayer].sc[biz_b].ho_limited — The smaller of line 1 or line 4, with no section 179 election (line 1 is line 29
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].ho_pre179_floor — Line 29 without the section 179 deduction, if zero or less zero
Status: **AGREE**

Value: $74,645.18

### classm.sc.2 — person[taxpayer].sc[biz_b].ho_both_limits — The gross income limitation could bind together with the section 179 business in
Status: **AGREE**

Value: no

### classm.sc.2 — person[taxpayer].sc[biz_b].ho_both — Line 5 when both income limits could bind
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].ho_line5_lim — Line 5 when line 4 is more than the room left by the section 179 elections
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].ho_line5 — Allowable expenses using the simplified method. Enter the smaller of line 1 or l
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].line30 — Expenses for business use of your home
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].line31 — Net profit or (loss). Subtract line 30 from line 29
Status: **AGREE**

Value: $72,118.18

### classm.sc.2 — person[taxpayer].sc[biz_b].line31_pre179 — Line 31 without the section 179 expense deduction
Status: **AGREE**

Value: $74,645.18

### classm.sc.2 — person[taxpayer].sc[biz_b].loss — Line 31 is a loss
Status: **AGREE**

Value: no

### classm.sc.2 — person[taxpayer].sc[biz_b].not_at_risk — Some investment is not at risk (box 32b)
Status: **AGREE**

Value: no

### classm.sc.2 — person[taxpayer].sc[biz_b].loss_allowed — The loss on line 31 when all investment is at risk
Status: **DISAGREE**

Project: $72,118.18
Model: $0.00
Work: No loss

Ruling: helper of a branch this entry does not take; project retained. The loss line of a business with a profit, the Form 7206 lines of a business under which no plan is established, and the Pub. 946 two-limit helpers of a home office whose line 5 takes another branch are figured by the project but read by no line this entry reaches; the printed lines they would feed (line 31, Form 7206 lines 4 to 14 of the plan's business, line 30) agree. The model entered zero or its own figure for an unused helper. Dropped from the fixture as not evidence. [dropped]

### classm.sc.2 — person[taxpayer].sc[biz_b].result — The amount for Schedule 1, line 3 and Schedule SE, line 2
Status: **AGREE**

Value: $72,118.18

### classm.sc.2 — person[taxpayer].sc[biz_b].line40 — Add lines 35 through 39
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].line42 — Cost of goods sold. Subtract line 41 from line 40
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f6 — Section 179 elected on property other than listed property
Status: **AGREE**

Value: $2,527.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f14 — Special allowance on property other than listed property
Status: **AGREE**

Value: $13,709.60

### classm.sc.2 — person[taxpayer].sc[biz_b].f17 — MACRS on earlier property other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f19_y3 — MACRS on 2025 property of period y3 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f19_y5 — MACRS on 2025 property of period y5 other than listed property
Status: **AGREE**

Value: $1,028.22

### classm.sc.2 — person[taxpayer].sc[biz_b].f19_y7 — MACRS on 2025 property of period y7 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f19_y10 — MACRS on 2025 property of period y10 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f19_y15 — MACRS on 2025 property of period y15 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f19_y20 — MACRS on 2025 property of period y20 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f19_y15sl — MACRS on 2025 property of period y15sl other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f25_assets — Special allowance on listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f25_veh — Special allowance on vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f25 — Line 25 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f26_assets — Column (h) of listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f26_veh — Column (h) of vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f26h — Column (h), line 26, for this business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f28 — Line 28 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f29_assets — Section 179 elected on listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f29_veh — Section 179 on vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f29 — Line 29 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].s179_elected — Section 179 elected for this business's 2025 property
Status: **AGREE**

Value: $2,527.00

### classm.sc.2 — person[taxpayer].sc[biz_b].dep_other — Depreciation other than the section 179 deduction (Form 4562 lines 14, 17, 19 an
Status: **AGREE**

Value: $14,737.82

### classm.sc.2 — person[taxpayer].sc[biz_b].s179_return — The return's section 179 deduction, for its only Schedule C
Status: **DISAGREE**

Project: $2,527.00
Model: $0.00
Work: Return has two Schedules C, not one

Ruling: helper of a branch this entry does not take; project retained. sc.s179_return (Form 4562 line 12 of the return, for its only Schedule C) is read by line 12 only when the return's deduction differs from the 2025 elections (s179.differs); here it does not (sc.s179_allowed takes sc.s179_elected, branch sc.s179_allowed#0), so the copy of $2,527.00 is figured but unused, and sc.s179_allowed of both businesses agrees ($0.00 and $2,527.00). The model entered zero because the return has two Schedules C. Dropped from the fixture as not evidence. [dropped]

### classm.sc.2 — person[taxpayer].sc[biz_b].s179_allowed — Section 179 expense deduction for this business
Status: **AGREE**

Value: $2,527.00

### classm.sc.2 — person[taxpayer].sc[biz_b].mq_q4_a — mq_q4 of this business's property
Status: **AGREE**

Value: $34,274.00

### classm.sc.2 — person[taxpayer].sc[biz_b].mq_q4_v — mq_q4 of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].mq_q4 — mq_q4 of this business
Status: **AGREE**

Value: $34,274.00

### classm.sc.2 — person[taxpayer].sc[biz_b].mq_total_a — mq_total of this business's property
Status: **AGREE**

Value: $34,274.00

### classm.sc.2 — person[taxpayer].sc[biz_b].mq_total_v — mq_total of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].mq_total — mq_total of this business
Status: **AGREE**

Value: $34,274.00

### classm.sc.2 — person[taxpayer].sc[biz_b].cost179_a — cost179 of this business's property
Status: **AGREE**

Value: $36,801.00

### classm.sc.2 — person[taxpayer].sc[biz_b].cost179_v — cost179 of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].cost179 — cost179 of this business
Status: **AGREE**

Value: $36,801.00

### classm.sc.2 — person[taxpayer].sc[biz_b].veh_lease — Business part of vehicle lease payments
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].profit_pos — Net profit of this business (zero for a loss)
Status: **AGREE**

Value: $72,118.18

### classm.sc.2 — person[taxpayer].sc[biz_b].hi_screened — This health insurance deduction is outside this tool
Status: **AGREE**

Value: no

### classm.sc.2 — person[taxpayer].sc[biz_b].f7206_line2 — Qualified long-term care insurance (the smaller of payments or the age limit, fo
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f7206_line3 — Add lines 1 and 2
Status: **AGREE**

Value: $7,387.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f7206_line4 — Net profit from the trade or business under which the insurance plan is establis
Status: **AGREE**

Value: $72,118.18

### classm.sc.2 — person[taxpayer].sc[biz_b].f7206_line5 — Total of all net profits from Schedule C, line 31
Status: **AGREE**

Value: $170,500.18

### classm.sc.2 — person[taxpayer].sc[biz_b].f7206_has — Line 4 is more than zero
Status: **AGREE**

Value: yes

### classm.sc.2 — person[taxpayer].sc[biz_b].f7206_line7_pos — Schedule 1, line 15 (this person's), times line 4 divided by line 5
Status: **AGREE**

Value: $4,779.09

### classm.sc.2 — person[taxpayer].sc[biz_b].f7206_line7 — Multiply Schedule 1 (Form 1040), line 15, deductible part of self-employment tax
Status: **AGREE**

Value: $4,779.09

### classm.sc.2 — person[taxpayer].sc[biz_b].f7206_line8 — Subtract line 7 from line 4
Status: **AGREE**

Value: $67,339.09

### classm.sc.2 — person[taxpayer].sc[biz_b].f7206_line9_pos — This person's SEP or SIMPLE deduction times line 4 divided by line 5
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f7206_line9 — Schedule 1, line 16, attributable to the same trade or business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f7206_line10 — Subtract line 9 from line 8
Status: **AGREE**

Value: $67,339.09

### classm.sc.2 — person[taxpayer].sc[biz_b].f7206_line13 — Subtract line 12 from line 10
Status: **AGREE**

Value: $67,339.09

### classm.sc.2 — person[taxpayer].sc[biz_b].f7206_min — The smaller of line 3 or line 13
Status: **AGREE**

Value: $7,387.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f7206_line14 — Self-employed health insurance deduction
Status: **AGREE**

Value: $7,387.00

### classm.sc.2 — person[taxpayer].sc[biz_b].qbi_has — This business has a net profit
Status: **AGREE**

Value: yes

### classm.sc.2 — person[taxpayer].sc[biz_b].qbi_se_pos — This person's deductible part of self-employment tax attributable to this busine
Status: **AGREE**

Value: $4,779.09

### classm.sc.2 — person[taxpayer].sc[biz_b].qbi_se — Deductible part of self-employment tax attributable to this business
Status: **AGREE**

Value: $4,779.09

### classm.sc.2 — person[taxpayer].sc[biz_b].qbi_plan_pos — This person's SEP or SIMPLE deduction attributable to this business (by share of
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].qbi_plan — SEP or SIMPLE deduction attributable to this business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].qbi_ded — Deductions attributable to this business: self-employment tax, retirement plan a
Status: **AGREE**

Value: $12,166.09

### classm.sc.2 — person[taxpayer].sc[biz_b].qbi — Qualified business income or (loss) of this business
Status: **AGREE**

Value: $59,952.09

### case classm.sc.3 — prompt sha256 6fc8c41533f93f131d6a421f1f2283b0efbcf4a5678965c1fd6ff208ea5f82b9; branches: sc.rrta:false, sc.statutory:false, sc.passive:true, sc.spouse_owned:false, sc.method_other:false, sc.special:false, sc.screened:false, sc.ho_uses:true, sc.ho_other:false, sc.ho_screened:false, sc.ho_multi:false, sc.ho_over:true, sc.ho_line4#1, sc.ho_unlimited:true, sc.ho_no179:false, sc.ho_limited:left, sc.ho_pre179_floor:positive, sc.ho_both_limits:false, sc.ho_line5_lim#1, sc.ho_line5#0, sc.line30#0, sc.loss:false, sc.at_risk:true, sc.not_at_risk:false, sc.result#0, sc.inventory_other:false, sc.s179_allowed#1, sc.profit_pos:positive, sc.hi_uses:false, sc.hi_screen:false, sc.hi_screened:false, sc.f7206_has:true, sc.f7206_line7#0, sc.f7206_line8:positive, sc.f7206_line9#0, sc.f7206_line10:positive, sc.f7206_min:left, sc.f7206_line14#1, sc.qbi_has:true, sc.qbi_se#0, sc.qbi_plan#0, sc.tips_ot:false

### classm.sc.3 — person[taxpayer].sc[biz_a].rrta — This business's owner has railroad retirement compensation
Status: **AGREE**

Value: no

### classm.sc.3 — person[taxpayer].sc[biz_a].screened — Something on this Schedule C is outside this tool
Status: **AGREE**

Value: no

### classm.sc.3 — person[taxpayer].sc[biz_a].line3 — Subtract line 2 from line 1
Status: **AGREE**

Value: $179,494.00

### classm.sc.3 — person[taxpayer].sc[biz_a].line4 — Cost of goods sold (from line 42)
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].line5 — Gross profit. Subtract line 4 from line 3
Status: **AGREE**

Value: $179,494.00

### classm.sc.3 — person[taxpayer].sc[biz_a].line7 — Gross income. Add lines 5 and 6
Status: **AGREE**

Value: $182,172.00

### classm.sc.3 — person[taxpayer].sc[biz_a].line9 — Car and truck expenses
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].line12 — Depletion
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].line13 — Depreciation and section 179 expense deduction (not included in Part III)
Status: **AGREE**

Value: $2,712.80

### classm.sc.3 — person[taxpayer].sc[biz_a].line20a — Rent or lease: vehicles, machinery, and equipment
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].meals_50_ded — 50% of the meals subject to the 50% limit
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].meals_80_ded — 80% of the meals under the hours of service limits
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].line24b — Deductible meals
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].line27a — Energy efficient commercial buildings deduction (attach Form 7205)
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].line27b — Other expenses (from line 48)
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].line28 — Total expenses before expenses for business use of home. Add lines 8 through 27b
Status: **AGREE**

Value: $126,902.80

### classm.sc.3 — person[taxpayer].sc[biz_a].line29 — Tentative profit or (loss). Subtract line 28 from line 7
Status: **AGREE**

Value: $55,269.20

### classm.sc.3 — person[taxpayer].sc[biz_a].line28_pre179 — Line 28 without the section 179 expense deduction
Status: **AGREE**

Value: $125,579.80

### classm.sc.3 — person[taxpayer].sc[biz_a].line29_pre179 — Line 29 without the section 179 expense deduction
Status: **AGREE**

Value: $56,592.20

### classm.sc.3 — person[taxpayer].sc[biz_a].ho_screened — The home office deduction is outside the simplified method this tool covers
Status: **AGREE**

Value: no

### classm.sc.3 — person[taxpayer].sc[biz_a].ho_multi — This person claims the business use of the home for more than one business
Status: **AGREE**

Value: no

### classm.sc.3 — person[taxpayer].sc[biz_a].ho_over — More than 300 square feet
Status: **AGREE**

Value: yes

### classm.sc.3 — person[taxpayer].sc[biz_a].ho_line4_actual — Line 2 (the square feet used) times line 3c
Status: **AGREE**

Value: $2,245.00

### classm.sc.3 — person[taxpayer].sc[biz_a].ho_line4_cap — 300 square feet times line 3c
Status: **AGREE**

Value: $1,500.00

### classm.sc.3 — person[taxpayer].sc[biz_a].ho_line4 — Multiply line 2 by line 3c
Status: **AGREE**

Value: $1,500.00

### classm.sc.3 — person[taxpayer].sc[biz_a].ho_line1 — Gross income limitation (Schedule C, line 29)
Status: **AGREE**

Value: $55,269.20

### classm.sc.3 — person[taxpayer].sc[biz_a].ho_room — Line 29 without the section 179 deduction, less the most section 179 deduction t
Status: **AGREE**

Value: $55,269.20

### classm.sc.3 — person[taxpayer].sc[biz_a].ho_unlimited — Line 4 is not more than the smallest line 29 any section 179 allocation could gi
Status: **AGREE**

Value: yes

### classm.sc.3 — person[taxpayer].sc[biz_a].ho_s179_max — The most section 179 deduction this business could take, its 2025 elections plus
Status: **AGREE**

Value: $1,323.00

### classm.sc.3 — person[taxpayer].sc[biz_a].ho_no179 — No section 179 deduction is possible for this business (no 2025 election and no 
Status: **AGREE**

Value: no

### classm.sc.3 — person[taxpayer].sc[biz_a].ho_limited — The smaller of line 1 or line 4, with no section 179 election (line 1 is line 29
Status: **AGREE**

Value: $1,500.00

### classm.sc.3 — person[taxpayer].sc[biz_a].ho_pre179_floor — Line 29 without the section 179 deduction, if zero or less zero
Status: **AGREE**

Value: $56,592.20

### classm.sc.3 — person[taxpayer].sc[biz_a].ho_both_limits — The gross income limitation could bind together with the section 179 business in
Status: **AGREE**

Value: no

### classm.sc.3 — person[taxpayer].sc[biz_a].ho_both — Line 5 when both income limits could bind
Status: **DISAGREE**

Project: $0.00
Model: $1,500.00
Work: Smaller of line 4 or the remaining income; line 4 governs

Ruling: helper of a branch this entry does not take; project retained. The loss line of a business with a profit, the Form 7206 lines of a business under which no plan is established, and the Pub. 946 two-limit helpers of a home office whose line 5 takes another branch are figured by the project but read by no line this entry reaches; the printed lines they would feed (line 31, Form 7206 lines 4 to 14 of the plan's business, line 30) agree. The model entered zero or its own figure for an unused helper. Dropped from the fixture as not evidence. [dropped]

### classm.sc.3 — person[taxpayer].sc[biz_a].ho_line5_lim — Line 5 when line 4 is more than the room left by the section 179 elections
Status: **DISAGREE**

Project: $0.00
Model: $1,500.00
Work: Smaller of 55,269.20 or 1,500.00

Ruling: helper of a branch this entry does not take; project retained. Line 4 ($1,500.00, 300 square feet times $5) is not more than the room left by section 179 (line 29 before section 179, $56,592.20, less the $1,323.00 carryover, $55,269.20), so sc.ho_unlimited is true and line 5 is line 4 (i1040sc p. 12; Pub. 946 p. 19); sc.ho_line5_lim is not read. With a carryover (sc.ho_no179 false) the project's unused helper copies sc.ho_both ($0.00); the model figured the smaller of line 1 or line 4. Lines 5, 30 and 31 agree ($1,500.00, $1,500.00, $53,769.20). Dropped from the fixture as not evidence. [dropped]

### classm.sc.3 — person[taxpayer].sc[biz_a].ho_line5 — Allowable expenses using the simplified method. Enter the smaller of line 1 or l
Status: **AGREE**

Value: $1,500.00

### classm.sc.3 — person[taxpayer].sc[biz_a].line30 — Expenses for business use of your home
Status: **AGREE**

Value: $1,500.00

### classm.sc.3 — person[taxpayer].sc[biz_a].line31 — Net profit or (loss). Subtract line 30 from line 29
Status: **AGREE**

Value: $53,769.20

### classm.sc.3 — person[taxpayer].sc[biz_a].line31_pre179 — Line 31 without the section 179 expense deduction
Status: **AGREE**

Value: $55,092.20

### classm.sc.3 — person[taxpayer].sc[biz_a].loss — Line 31 is a loss
Status: **AGREE**

Value: no

### classm.sc.3 — person[taxpayer].sc[biz_a].not_at_risk — Some investment is not at risk (box 32b)
Status: **AGREE**

Value: no

### classm.sc.3 — person[taxpayer].sc[biz_a].loss_allowed — The loss on line 31 when all investment is at risk
Status: **AGREE**

Value: $53,769.20

### classm.sc.3 — person[taxpayer].sc[biz_a].result — The amount for Schedule 1, line 3 and Schedule SE, line 2
Status: **AGREE**

Value: $53,769.20

### classm.sc.3 — person[taxpayer].sc[biz_a].line40 — Add lines 35 through 39
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].line42 — Cost of goods sold. Subtract line 41 from line 40
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f6 — Section 179 elected on property other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f14 — Special allowance on property other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f17 — MACRS on earlier property other than listed property
Status: **AGREE**

Value: $1,389.80

### classm.sc.3 — person[taxpayer].sc[biz_a].f19_y3 — MACRS on 2025 property of period y3 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f19_y5 — MACRS on 2025 property of period y5 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f19_y7 — MACRS on 2025 property of period y7 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f19_y10 — MACRS on 2025 property of period y10 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f19_y15 — MACRS on 2025 property of period y15 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f19_y20 — MACRS on 2025 property of period y20 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f19_y15sl — MACRS on 2025 property of period y15sl other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f25_assets — Special allowance on listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f25_veh — Special allowance on vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f25 — Line 25 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f26_assets — Column (h) of listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f26_veh — Column (h) of vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f26h — Column (h), line 26, for this business
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f28 — Line 28 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f29_assets — Section 179 elected on listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f29_veh — Section 179 on vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f29 — Line 29 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].s179_elected — Section 179 elected for this business's 2025 property
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].dep_other — Depreciation other than the section 179 deduction (Form 4562 lines 14, 17, 19 an
Status: **AGREE**

Value: $1,389.80

### classm.sc.3 — person[taxpayer].sc[biz_a].s179_return — The return's section 179 deduction, for its only Schedule C
Status: **AGREE**

Value: $1,323.00

### classm.sc.3 — person[taxpayer].sc[biz_a].s179_allowed — Section 179 expense deduction for this business
Status: **AGREE**

Value: $1,323.00

### classm.sc.3 — person[taxpayer].sc[biz_a].mq_q4_a — mq_q4 of this business's property
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].mq_q4_v — mq_q4 of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].mq_q4 — mq_q4 of this business
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].mq_total_a — mq_total of this business's property
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].mq_total_v — mq_total of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].mq_total — mq_total of this business
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].cost179_a — cost179 of this business's property
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].cost179_v — cost179 of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].cost179 — cost179 of this business
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].veh_lease — Business part of vehicle lease payments
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].profit_pos — Net profit of this business (zero for a loss)
Status: **AGREE**

Value: $53,769.20

### classm.sc.3 — person[taxpayer].sc[biz_a].hi_screened — This health insurance deduction is outside this tool
Status: **AGREE**

Value: no

### classm.sc.3 — person[taxpayer].sc[biz_a].f7206_line2 — Qualified long-term care insurance (the smaller of payments or the age limit, fo
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f7206_line3 — Add lines 1 and 2
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f7206_line4 — Net profit from the trade or business under which the insurance plan is establis
Status: **DISAGREE**

Project: $53,769.20
Model: $0.00
Work: No plan established under this business

Ruling: helper of a branch this entry does not take; project retained. No health insurance plan is established under this business (sc.hi_uses is false, sc.f7206_line1 zero), so Form 7206 line 14 takes zero (branch sc.f7206_line14#1) and agrees ($0.00); the project figures lines 4 to 13 from the business's profit regardless, read by no line this entry reaches. The model entered zero for the unused lines. Dropped from the fixture as not evidence. [dropped]

### classm.sc.3 — person[taxpayer].sc[biz_a].f7206_line5 — Total of all net profits from Schedule C, line 31
Status: **AGREE**

Value: $53,769.20

### classm.sc.3 — person[taxpayer].sc[biz_a].f7206_has — Line 4 is more than zero
Status: **DISAGREE**

Project: yes
Model: no
Work: Line 4 is 0

Ruling: helper of a branch this entry does not take; project retained. No health insurance plan is established under this business (sc.hi_uses is false, sc.f7206_line1 zero), so Form 7206 line 14 takes zero (branch sc.f7206_line14#1) and agrees ($0.00); the project figures lines 4 to 13 from the business's profit regardless, read by no line this entry reaches. The model entered zero for the unused lines. Dropped from the fixture as not evidence. [dropped]

### classm.sc.3 — person[taxpayer].sc[biz_a].f7206_line7_pos — Schedule 1, line 15 (this person's), times line 4 divided by line 5
Status: **DISAGREE**

Project: $720.01
Model: $0.00
Work: Line 4 is 0

Ruling: helper of a branch this entry does not take; project retained. No health insurance plan is established under this business (sc.hi_uses is false, sc.f7206_line1 zero), so Form 7206 line 14 takes zero (branch sc.f7206_line14#1) and agrees ($0.00); the project figures lines 4 to 13 from the business's profit regardless, read by no line this entry reaches. The model entered zero for the unused lines. Dropped from the fixture as not evidence. [dropped]

### classm.sc.3 — person[taxpayer].sc[biz_a].f7206_line7 — Multiply Schedule 1 (Form 1040), line 15, deductible part of self-employment tax
Status: **DISAGREE**

Project: $720.01
Model: $0.00
Work: Line 4 is 0

Ruling: helper of a branch this entry does not take; project retained. No health insurance plan is established under this business (sc.hi_uses is false, sc.f7206_line1 zero), so Form 7206 line 14 takes zero (branch sc.f7206_line14#1) and agrees ($0.00); the project figures lines 4 to 13 from the business's profit regardless, read by no line this entry reaches. The model entered zero for the unused lines. Dropped from the fixture as not evidence. [dropped]

### classm.sc.3 — person[taxpayer].sc[biz_a].f7206_line8 — Subtract line 7 from line 4
Status: **DISAGREE**

Project: $53,049.19
Model: $0.00
Work: 0 - 0

Ruling: helper of a branch this entry does not take; project retained. No health insurance plan is established under this business (sc.hi_uses is false, sc.f7206_line1 zero), so Form 7206 line 14 takes zero (branch sc.f7206_line14#1) and agrees ($0.00); the project figures lines 4 to 13 from the business's profit regardless, read by no line this entry reaches. The model entered zero for the unused lines. Dropped from the fixture as not evidence. [dropped]

### classm.sc.3 — person[taxpayer].sc[biz_a].f7206_line9_pos — This person's SEP or SIMPLE deduction times line 4 divided by line 5
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f7206_line9 — Schedule 1, line 16, attributable to the same trade or business
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f7206_line10 — Subtract line 9 from line 8
Status: **DISAGREE**

Project: $53,049.19
Model: $0.00
Work: 0 - 0

Ruling: helper of a branch this entry does not take; project retained. No health insurance plan is established under this business (sc.hi_uses is false, sc.f7206_line1 zero), so Form 7206 line 14 takes zero (branch sc.f7206_line14#1) and agrees ($0.00); the project figures lines 4 to 13 from the business's profit regardless, read by no line this entry reaches. The model entered zero for the unused lines. Dropped from the fixture as not evidence. [dropped]

### classm.sc.3 — person[taxpayer].sc[biz_a].f7206_line13 — Subtract line 12 from line 10
Status: **DISAGREE**

Project: $53,049.19
Model: $0.00
Work: 0 - 0

Ruling: helper of a branch this entry does not take; project retained. No health insurance plan is established under this business (sc.hi_uses is false, sc.f7206_line1 zero), so Form 7206 line 14 takes zero (branch sc.f7206_line14#1) and agrees ($0.00); the project figures lines 4 to 13 from the business's profit regardless, read by no line this entry reaches. The model entered zero for the unused lines. Dropped from the fixture as not evidence. [dropped]

### classm.sc.3 — person[taxpayer].sc[biz_a].f7206_min — The smaller of line 3 or line 13
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f7206_line14 — Self-employed health insurance deduction
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].qbi_has — This business has a net profit
Status: **AGREE**

Value: yes

### classm.sc.3 — person[taxpayer].sc[biz_a].qbi_se_pos — This person's deductible part of self-employment tax attributable to this busine
Status: **AGREE**

Value: $720.01

### classm.sc.3 — person[taxpayer].sc[biz_a].qbi_se — Deductible part of self-employment tax attributable to this business
Status: **AGREE**

Value: $720.01

### classm.sc.3 — person[taxpayer].sc[biz_a].qbi_plan_pos — This person's SEP or SIMPLE deduction attributable to this business (by share of
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].qbi_plan — SEP or SIMPLE deduction attributable to this business
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].qbi_ded — Deductions attributable to this business: self-employment tax, retirement plan a
Status: **AGREE**

Value: $720.01

### classm.sc.3 — person[taxpayer].sc[biz_a].qbi — Qualified business income or (loss) of this business
Status: **AGREE**

Value: $53,049.19

### case classm.sc.4 — prompt sha256 4c88f3a7e9d67382cf7b6cb8613c1c2255392ef9b8c5fc0019270fc885bb19a0; branches: sc.rrta:false, sc.statutory:false, sc.passive:true, sc.spouse_owned:false, sc.method_other:false, sc.special:false, sc.screened:false, sc.ho_uses:false, sc.ho_other:false, sc.ho_screened:false, sc.ho_multi:false, sc.ho_over:false, sc.ho_line4#0, sc.ho_unlimited:false, sc.ho_unlimited:true, sc.ho_no179:true, sc.ho_limited:left, sc.ho_pre179_floor:floor, sc.ho_pre179_floor:positive, sc.ho_both_limits:false, sc.ho_line5_lim#0, sc.ho_line5#0, sc.ho_line5#1, sc.line30#1, sc.loss:false, sc.loss:true, sc.at_risk:true, sc.not_at_risk:false, sc.result#0, sc.result#1, sc.inventory_other:false, sc.s179_allowed#0, sc.profit_pos:floor, sc.profit_pos:positive, sc.hi_uses:false, sc.hi_uses:true, sc.hi_screen:false, sc.hi_screened:false, sc.f7206_has:false, sc.f7206_has:true, sc.f7206_line7#0, sc.f7206_line7#1, sc.f7206_line8:floor, sc.f7206_line8:positive, sc.f7206_line9#0, sc.f7206_line9#1, sc.f7206_line10:floor, sc.f7206_line10:positive, sc.f7206_min:left, sc.f7206_min:right, sc.f7206_line14#0, sc.f7206_line14#1, sc.qbi_has:false, sc.qbi_has:true, sc.qbi_se#0, sc.qbi_se#1, sc.qbi_plan#0, sc.qbi_plan#1, sc.tips_ot:false

### classm.sc.4 — person[taxpayer].sc[biz_a].rrta — This business's owner has railroad retirement compensation
Status: **AGREE**

Value: no

### classm.sc.4 — person[taxpayer].sc[biz_a].screened — Something on this Schedule C is outside this tool
Status: **AGREE**

Value: no

### classm.sc.4 — person[taxpayer].sc[biz_a].line3 — Subtract line 2 from line 1
Status: **AGREE**

Value: $26,838.00

### classm.sc.4 — person[taxpayer].sc[biz_a].line4 — Cost of goods sold (from line 42)
Status: **AGREE**

Value: $33,384.00

### classm.sc.4 — person[taxpayer].sc[biz_a].line5 — Gross profit. Subtract line 4 from line 3
Status: **AGREE**

Value: $-6,546.00

### classm.sc.4 — person[taxpayer].sc[biz_a].line7 — Gross income. Add lines 5 and 6
Status: **AGREE**

Value: $-6,546.00

### classm.sc.4 — person[taxpayer].sc[biz_a].line9 — Car and truck expenses
Status: **AGREE**

Value: $1,621.90

### classm.sc.4 — person[taxpayer].sc[biz_a].line12 — Depletion
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].line13 — Depreciation and section 179 expense deduction (not included in Part III)
Status: **AGREE**

Value: $6,883.21

### classm.sc.4 — person[taxpayer].sc[biz_a].line20a — Rent or lease: vehicles, machinery, and equipment
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].meals_50_ded — 50% of the meals subject to the 50% limit
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].meals_80_ded — 80% of the meals under the hours of service limits
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].line24b — Deductible meals
Status: **AGREE**

Value: $22,259.00

### classm.sc.4 — person[taxpayer].sc[biz_a].line27a — Energy efficient commercial buildings deduction (attach Form 7205)
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].line27b — Other expenses (from line 48)
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].line28 — Total expenses before expenses for business use of home. Add lines 8 through 27b
Status: **AGREE**

Value: $40,991.11

### classm.sc.4 — person[taxpayer].sc[biz_a].line29 — Tentative profit or (loss). Subtract line 28 from line 7
Status: **AGREE**

Value: $-47,537.11

### classm.sc.4 — person[taxpayer].sc[biz_a].line28_pre179 — Line 28 without the section 179 expense deduction
Status: **AGREE**

Value: $40,991.11

### classm.sc.4 — person[taxpayer].sc[biz_a].line29_pre179 — Line 29 without the section 179 expense deduction
Status: **AGREE**

Value: $-47,537.11

### classm.sc.4 — person[taxpayer].sc[biz_a].ho_screened — The home office deduction is outside the simplified method this tool covers
Status: **AGREE**

Value: no

### classm.sc.4 — person[taxpayer].sc[biz_a].ho_multi — This person claims the business use of the home for more than one business
Status: **AGREE**

Value: no

### classm.sc.4 — person[taxpayer].sc[biz_a].ho_over — More than 300 square feet
Status: **AGREE**

Value: no

### classm.sc.4 — person[taxpayer].sc[biz_a].ho_line4_actual — Line 2 (the square feet used) times line 3c
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].ho_line4_cap — 300 square feet times line 3c
Status: **AGREE**

Value: $1,500.00

### classm.sc.4 — person[taxpayer].sc[biz_a].ho_line4 — Multiply line 2 by line 3c
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].ho_line1 — Gross income limitation (Schedule C, line 29)
Status: **AGREE**

Value: $-47,537.11

### classm.sc.4 — person[taxpayer].sc[biz_a].ho_room — Line 29 without the section 179 deduction, less the most section 179 deduction t
Status: **AGREE**

Value: $-47,537.11

### classm.sc.4 — person[taxpayer].sc[biz_a].ho_unlimited — Line 4 is not more than the smallest line 29 any section 179 allocation could gi
Status: **AGREE**

Value: no

### classm.sc.4 — person[taxpayer].sc[biz_a].ho_s179_max — The most section 179 deduction this business could take, its 2025 elections plus
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].ho_no179 — No section 179 deduction is possible for this business (no 2025 election and no 
Status: **AGREE**

Value: yes

### classm.sc.4 — person[taxpayer].sc[biz_a].ho_limited — The smaller of line 1 or line 4, with no section 179 election (line 1 is line 29
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].ho_pre179_floor — Line 29 without the section 179 deduction, if zero or less zero
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].ho_both_limits — The gross income limitation could bind together with the section 179 business in
Status: **AGREE**

Value: no

### classm.sc.4 — person[taxpayer].sc[biz_a].ho_both — Line 5 when both income limits could bind
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].ho_line5_lim — Line 5 when line 4 is more than the room left by the section 179 elections
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].ho_line5 — Allowable expenses using the simplified method. Enter the smaller of line 1 or l
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].line30 — Expenses for business use of your home
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].line31 — Net profit or (loss). Subtract line 30 from line 29
Status: **AGREE**

Value: $-47,537.11

### classm.sc.4 — person[taxpayer].sc[biz_a].line31_pre179 — Line 31 without the section 179 expense deduction
Status: **AGREE**

Value: $-47,537.11

### classm.sc.4 — person[taxpayer].sc[biz_a].loss — Line 31 is a loss
Status: **AGREE**

Value: yes

### classm.sc.4 — person[taxpayer].sc[biz_a].not_at_risk — Some investment is not at risk (box 32b)
Status: **AGREE**

Value: no

### classm.sc.4 — person[taxpayer].sc[biz_a].loss_allowed — The loss on line 31 when all investment is at risk
Status: **AGREE**

Value: $-47,537.11

### classm.sc.4 — person[taxpayer].sc[biz_a].result — The amount for Schedule 1, line 3 and Schedule SE, line 2
Status: **AGREE**

Value: $-47,537.11

### classm.sc.4 — person[taxpayer].sc[biz_a].line40 — Add lines 35 through 39
Status: **AGREE**

Value: $44,746.00

### classm.sc.4 — person[taxpayer].sc[biz_a].line42 — Cost of goods sold. Subtract line 41 from line 40
Status: **AGREE**

Value: $33,384.00

### classm.sc.4 — person[taxpayer].sc[biz_a].f6 — Section 179 elected on property other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].f14 — Special allowance on property other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].f17 — MACRS on earlier property other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].f19_y3 — MACRS on 2025 property of period y3 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].f19_y5 — MACRS on 2025 property of period y5 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].f19_y7 — MACRS on 2025 property of period y7 other than listed property
Status: **AGREE**

Value: $6,883.21

### classm.sc.4 — person[taxpayer].sc[biz_a].f19_y10 — MACRS on 2025 property of period y10 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].f19_y15 — MACRS on 2025 property of period y15 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].f19_y20 — MACRS on 2025 property of period y20 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].f19_y15sl — MACRS on 2025 property of period y15sl other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].f25_assets — Special allowance on listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].f25_veh — Special allowance on vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].f25 — Line 25 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].f26_assets — Column (h) of listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].f26_veh — Column (h) of vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].f26h — Column (h), line 26, for this business
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].f28 — Line 28 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].f29_assets — Section 179 elected on listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].f29_veh — Section 179 on vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].f29 — Line 29 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].s179_elected — Section 179 elected for this business's 2025 property
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].dep_other — Depreciation other than the section 179 deduction (Form 4562 lines 14, 17, 19 an
Status: **AGREE**

Value: $6,883.21

### classm.sc.4 — person[taxpayer].sc[biz_a].s179_return — The return's section 179 deduction, for its only Schedule C
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].s179_allowed — Section 179 expense deduction for this business
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].mq_q4_a — mq_q4 of this business's property
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].mq_q4_v — mq_q4 of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].mq_q4 — mq_q4 of this business
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].mq_total_a — mq_total of this business's property
Status: **AGREE**

Value: $48,168.00

### classm.sc.4 — person[taxpayer].sc[biz_a].mq_total_v — mq_total of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].mq_total — mq_total of this business
Status: **AGREE**

Value: $48,168.00

### classm.sc.4 — person[taxpayer].sc[biz_a].cost179_a — cost179 of this business's property
Status: **AGREE**

Value: $48,168.00

### classm.sc.4 — person[taxpayer].sc[biz_a].cost179_v — cost179 of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].cost179 — cost179 of this business
Status: **AGREE**

Value: $48,168.00

### classm.sc.4 — person[taxpayer].sc[biz_a].veh_lease — Business part of vehicle lease payments
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].profit_pos — Net profit of this business (zero for a loss)
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].hi_screened — This health insurance deduction is outside this tool
Status: **AGREE**

Value: no

### classm.sc.4 — person[taxpayer].sc[biz_a].f7206_line2 — Qualified long-term care insurance (the smaller of payments or the age limit, fo
Status: **AGREE**

Value: $4,810.00

### classm.sc.4 — person[taxpayer].sc[biz_a].f7206_line3 — Add lines 1 and 2
Status: **AGREE**

Value: $4,810.00

### classm.sc.4 — person[taxpayer].sc[biz_a].f7206_line4 — Net profit from the trade or business under which the insurance plan is establis
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].f7206_line5 — Total of all net profits from Schedule C, line 31
Status: **AGREE**

Value: $47,327.50

### classm.sc.4 — person[taxpayer].sc[biz_a].f7206_has — Line 4 is more than zero
Status: **AGREE**

Value: no

### classm.sc.4 — person[taxpayer].sc[biz_a].f7206_line7_pos — Schedule 1, line 15 (this person's), times line 4 divided by line 5
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].f7206_line7 — Multiply Schedule 1 (Form 1040), line 15, deductible part of self-employment tax
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].f7206_line8 — Subtract line 7 from line 4
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].f7206_line9_pos — This person's SEP or SIMPLE deduction times line 4 divided by line 5
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].f7206_line9 — Schedule 1, line 16, attributable to the same trade or business
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].f7206_line10 — Subtract line 9 from line 8
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].f7206_line13 — Subtract line 12 from line 10
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].f7206_min — The smaller of line 3 or line 13
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].f7206_line14 — Self-employed health insurance deduction
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].qbi_has — This business has a net profit
Status: **AGREE**

Value: no

### classm.sc.4 — person[taxpayer].sc[biz_a].qbi_se_pos — This person's deductible part of self-employment tax attributable to this busine
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].qbi_se — Deductible part of self-employment tax attributable to this business
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].qbi_plan_pos — This person's SEP or SIMPLE deduction attributable to this business (by share of
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].qbi_plan — SEP or SIMPLE deduction attributable to this business
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].qbi_ded — Deductions attributable to this business: self-employment tax, retirement plan a
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_a].qbi — Qualified business income or (loss) of this business
Status: **AGREE**

Value: $-47,537.11

### classm.sc.4 — person[taxpayer].sc[biz_b].rrta — This business's owner has railroad retirement compensation
Status: **AGREE**

Value: no

### classm.sc.4 — person[taxpayer].sc[biz_b].screened — Something on this Schedule C is outside this tool
Status: **AGREE**

Value: no

### classm.sc.4 — person[taxpayer].sc[biz_b].line3 — Subtract line 2 from line 1
Status: **AGREE**

Value: $151,388.00

### classm.sc.4 — person[taxpayer].sc[biz_b].line4 — Cost of goods sold (from line 42)
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].line5 — Gross profit. Subtract line 4 from line 3
Status: **AGREE**

Value: $151,388.00

### classm.sc.4 — person[taxpayer].sc[biz_b].line7 — Gross income. Add lines 5 and 6
Status: **AGREE**

Value: $154,119.00

### classm.sc.4 — person[taxpayer].sc[biz_b].line9 — Car and truck expenses
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].line12 — Depletion
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].line13 — Depreciation and section 179 expense deduction (not included in Part III)
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].line20a — Rent or lease: vehicles, machinery, and equipment
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].meals_50_ded — 50% of the meals subject to the 50% limit
Status: **AGREE**

Value: $209.50

### classm.sc.4 — person[taxpayer].sc[biz_b].meals_80_ded — 80% of the meals under the hours of service limits
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].line24b — Deductible meals
Status: **AGREE**

Value: $209.50

### classm.sc.4 — person[taxpayer].sc[biz_b].line27a — Energy efficient commercial buildings deduction (attach Form 7205)
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].line27b — Other expenses (from line 48)
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].line28 — Total expenses before expenses for business use of home. Add lines 8 through 27b
Status: **AGREE**

Value: $106,791.50

### classm.sc.4 — person[taxpayer].sc[biz_b].line29 — Tentative profit or (loss). Subtract line 28 from line 7
Status: **AGREE**

Value: $47,327.50

### classm.sc.4 — person[taxpayer].sc[biz_b].line28_pre179 — Line 28 without the section 179 expense deduction
Status: **AGREE**

Value: $106,791.50

### classm.sc.4 — person[taxpayer].sc[biz_b].line29_pre179 — Line 29 without the section 179 expense deduction
Status: **AGREE**

Value: $47,327.50

### classm.sc.4 — person[taxpayer].sc[biz_b].ho_screened — The home office deduction is outside the simplified method this tool covers
Status: **AGREE**

Value: no

### classm.sc.4 — person[taxpayer].sc[biz_b].ho_multi — This person claims the business use of the home for more than one business
Status: **AGREE**

Value: no

### classm.sc.4 — person[taxpayer].sc[biz_b].ho_over — More than 300 square feet
Status: **AGREE**

Value: no

### classm.sc.4 — person[taxpayer].sc[biz_b].ho_line4_actual — Line 2 (the square feet used) times line 3c
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].ho_line4_cap — 300 square feet times line 3c
Status: **AGREE**

Value: $1,500.00

### classm.sc.4 — person[taxpayer].sc[biz_b].ho_line4 — Multiply line 2 by line 3c
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].ho_line1 — Gross income limitation (Schedule C, line 29)
Status: **AGREE**

Value: $47,327.50

### classm.sc.4 — person[taxpayer].sc[biz_b].ho_room — Line 29 without the section 179 deduction, less the most section 179 deduction t
Status: **AGREE**

Value: $47,327.50

### classm.sc.4 — person[taxpayer].sc[biz_b].ho_unlimited — Line 4 is not more than the smallest line 29 any section 179 allocation could gi
Status: **AGREE**

Value: yes

### classm.sc.4 — person[taxpayer].sc[biz_b].ho_s179_max — The most section 179 deduction this business could take, its 2025 elections plus
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].ho_no179 — No section 179 deduction is possible for this business (no 2025 election and no 
Status: **AGREE**

Value: yes

### classm.sc.4 — person[taxpayer].sc[biz_b].ho_limited — The smaller of line 1 or line 4, with no section 179 election (line 1 is line 29
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].ho_pre179_floor — Line 29 without the section 179 deduction, if zero or less zero
Status: **AGREE**

Value: $47,327.50

### classm.sc.4 — person[taxpayer].sc[biz_b].ho_both_limits — The gross income limitation could bind together with the section 179 business in
Status: **AGREE**

Value: no

### classm.sc.4 — person[taxpayer].sc[biz_b].ho_both — Line 5 when both income limits could bind
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].ho_line5_lim — Line 5 when line 4 is more than the room left by the section 179 elections
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].ho_line5 — Allowable expenses using the simplified method. Enter the smaller of line 1 or l
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].line30 — Expenses for business use of your home
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].line31 — Net profit or (loss). Subtract line 30 from line 29
Status: **AGREE**

Value: $47,327.50

### classm.sc.4 — person[taxpayer].sc[biz_b].line31_pre179 — Line 31 without the section 179 expense deduction
Status: **AGREE**

Value: $47,327.50

### classm.sc.4 — person[taxpayer].sc[biz_b].loss — Line 31 is a loss
Status: **AGREE**

Value: no

### classm.sc.4 — person[taxpayer].sc[biz_b].not_at_risk — Some investment is not at risk (box 32b)
Status: **AGREE**

Value: no

### classm.sc.4 — person[taxpayer].sc[biz_b].loss_allowed — The loss on line 31 when all investment is at risk
Status: **DISAGREE**

Project: $47,327.50
Model: $0.00
Work: No loss

Ruling: helper of a branch this entry does not take; project retained. The loss line of a business with a profit, the Form 7206 lines of a business under which no plan is established, and the Pub. 946 two-limit helpers of a home office whose line 5 takes another branch are figured by the project but read by no line this entry reaches; the printed lines they would feed (line 31, Form 7206 lines 4 to 14 of the plan's business, line 30) agree. The model entered zero or its own figure for an unused helper. Dropped from the fixture as not evidence. [dropped]

### classm.sc.4 — person[taxpayer].sc[biz_b].result — The amount for Schedule 1, line 3 and Schedule SE, line 2
Status: **AGREE**

Value: $47,327.50

### classm.sc.4 — person[taxpayer].sc[biz_b].line40 — Add lines 35 through 39
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].line42 — Cost of goods sold. Subtract line 41 from line 40
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].f6 — Section 179 elected on property other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].f14 — Special allowance on property other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].f17 — MACRS on earlier property other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].f19_y3 — MACRS on 2025 property of period y3 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].f19_y5 — MACRS on 2025 property of period y5 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].f19_y7 — MACRS on 2025 property of period y7 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].f19_y10 — MACRS on 2025 property of period y10 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].f19_y15 — MACRS on 2025 property of period y15 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].f19_y20 — MACRS on 2025 property of period y20 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].f19_y15sl — MACRS on 2025 property of period y15sl other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].f25_assets — Special allowance on listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].f25_veh — Special allowance on vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].f25 — Line 25 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].f26_assets — Column (h) of listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].f26_veh — Column (h) of vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].f26h — Column (h), line 26, for this business
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].f28 — Line 28 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].f29_assets — Section 179 elected on listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].f29_veh — Section 179 on vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].f29 — Line 29 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].s179_elected — Section 179 elected for this business's 2025 property
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].dep_other — Depreciation other than the section 179 deduction (Form 4562 lines 14, 17, 19 an
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].s179_return — The return's section 179 deduction, for its only Schedule C
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].s179_allowed — Section 179 expense deduction for this business
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].mq_q4_a — mq_q4 of this business's property
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].mq_q4_v — mq_q4 of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].mq_q4 — mq_q4 of this business
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].mq_total_a — mq_total of this business's property
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].mq_total_v — mq_total of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].mq_total — mq_total of this business
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].cost179_a — cost179 of this business's property
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].cost179_v — cost179 of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].cost179 — cost179 of this business
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].veh_lease — Business part of vehicle lease payments
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].profit_pos — Net profit of this business (zero for a loss)
Status: **AGREE**

Value: $47,327.50

### classm.sc.4 — person[taxpayer].sc[biz_b].hi_screened — This health insurance deduction is outside this tool
Status: **AGREE**

Value: no

### classm.sc.4 — person[taxpayer].sc[biz_b].f7206_line2 — Qualified long-term care insurance (the smaller of payments or the age limit, fo
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].f7206_line3 — Add lines 1 and 2
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].f7206_line4 — Net profit from the trade or business under which the insurance plan is establis
Status: **AGREE**

Value: $47,327.50

### classm.sc.4 — person[taxpayer].sc[biz_b].f7206_line5 — Total of all net profits from Schedule C, line 31
Status: **AGREE**

Value: $47,327.50

### classm.sc.4 — person[taxpayer].sc[biz_b].f7206_has — Line 4 is more than zero
Status: **AGREE**

Value: yes

### classm.sc.4 — person[taxpayer].sc[biz_b].f7206_line7_pos — Schedule 1, line 15 (this person's), times line 4 divided by line 5
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].f7206_line7 — Multiply Schedule 1 (Form 1040), line 15, deductible part of self-employment tax
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].f7206_line8 — Subtract line 7 from line 4
Status: **AGREE**

Value: $47,327.50

### classm.sc.4 — person[taxpayer].sc[biz_b].f7206_line9_pos — This person's SEP or SIMPLE deduction times line 4 divided by line 5
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].f7206_line9 — Schedule 1, line 16, attributable to the same trade or business
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].f7206_line10 — Subtract line 9 from line 8
Status: **AGREE**

Value: $47,327.50

### classm.sc.4 — person[taxpayer].sc[biz_b].f7206_line13 — Subtract line 12 from line 10
Status: **AGREE**

Value: $47,327.50

### classm.sc.4 — person[taxpayer].sc[biz_b].f7206_min — The smaller of line 3 or line 13
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].f7206_line14 — Self-employed health insurance deduction
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].qbi_has — This business has a net profit
Status: **AGREE**

Value: yes

### classm.sc.4 — person[taxpayer].sc[biz_b].qbi_se_pos — This person's deductible part of self-employment tax attributable to this busine
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].qbi_se — Deductible part of self-employment tax attributable to this business
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].qbi_plan_pos — This person's SEP or SIMPLE deduction attributable to this business (by share of
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].qbi_plan — SEP or SIMPLE deduction attributable to this business
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].qbi_ded — Deductions attributable to this business: self-employment tax, retirement plan a
Status: **AGREE**

Value: $0.00

### classm.sc.4 — person[taxpayer].sc[biz_b].qbi — Qualified business income or (loss) of this business
Status: **AGREE**

Value: $47,327.50

## Raw responses

### classm.sc.1

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].rrta"
    value: "no"
    work: "No railroad retirement compensation or CT-2"
  - printed: "person[taxpayer].sc[biz_a].screened"
    value: "no"
    work: "Not statutory employee; materially participates; not jointly owned; cash/accrual; no special items"
  - printed: "person[taxpayer].sc[biz_a].line3"
    value: "188155.00"
    work: "188,155.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].line4"
    value: "0.00"
    work: "From line 42"
  - printed: "person[taxpayer].sc[biz_a].line5"
    value: "188155.00"
    work: "188,155.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].line7"
    value: "188155.00"
    work: "188,155.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_a].line9"
    value: "19703.70"
    work: "Vehicle car_1 car and truck expenses"
  - printed: "person[taxpayer].sc[biz_a].line12"
    value: "0.00"
    work: "No depletion"
  - printed: "person[taxpayer].sc[biz_a].line13"
    value: "2536.10"
    work: "s179 0.00 + depreciation 2,536.10 (F4562 line 17)"
  - printed: "person[taxpayer].sc[biz_a].line20a"
    value: "0.00"
    work: "Machinery rent 0.00 + vehicle lease 0.00"
  - printed: "person[taxpayer].sc[biz_a].meals_50_ded"
    value: "0.00"
    work: "0.00 x 50%"
  - printed: "person[taxpayer].sc[biz_a].meals_80_ded"
    value: "0.00"
    work: "0.00 x 80%"
  - printed: "person[taxpayer].sc[biz_a].line24b"
    value: "0.00"
    work: "0.00 + 0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_a].line27a"
    value: "0.00"
    work: "No Form 7205"
  - printed: "person[taxpayer].sc[biz_a].line27b"
    value: "12210.00"
    work: "Line 48 total other expenses"
  - printed: "person[taxpayer].sc[biz_a].line28"
    value: "64607.80"
    work: "19,703.70 + 2,536.10 + 28,564.00 + 1,594.00 + 12,210.00"
  - printed: "person[taxpayer].sc[biz_a].line29"
    value: "123547.20"
    work: "188,155.00 - 64,607.80"
  - printed: "person[taxpayer].sc[biz_a].line28_pre179"
    value: "64607.80"
    work: "Line 28 - s179 0.00"
  - printed: "person[taxpayer].sc[biz_a].line29_pre179"
    value: "123547.20"
    work: "188,155.00 - 64,607.80"
  - printed: "person[taxpayer].sc[biz_a].ho_screened"
    value: "no"
    work: "No home office claimed; no special conditions"
  - printed: "person[taxpayer].sc[biz_a].ho_multi"
    value: "no"
    work: "Count of home-use Schedules C is 1"
  - printed: "person[taxpayer].sc[biz_a].ho_over"
    value: "no"
    work: "0 sq ft is not over 300"
  - printed: "person[taxpayer].sc[biz_a].ho_line4_actual"
    value: "0.00"
    work: "0 x $5.00"
  - printed: "person[taxpayer].sc[biz_a].ho_line4_cap"
    value: "1500.00"
    work: "300 x $5.00"
  - printed: "person[taxpayer].sc[biz_a].ho_line4"
    value: "0.00"
    work: "Not over 300 sq ft, so actual 0.00"
  - printed: "person[taxpayer].sc[biz_a].ho_line1"
    value: "123547.20"
    work: "Schedule C line 29"
  - printed: "person[taxpayer].sc[biz_a].ho_room"
    value: "123547.20"
    work: "123,547.20 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].ho_unlimited"
    value: "yes"
    work: "0.00 <= 123,547.20"
  - printed: "person[taxpayer].sc[biz_a].ho_s179_max"
    value: "0.00"
    work: "Elected 0.00 + carryover 0.00"
  - printed: "person[taxpayer].sc[biz_a].ho_no179"
    value: "yes"
    work: "No election and no carryover"
  - printed: "person[taxpayer].sc[biz_a].ho_limited"
    value: "0.00"
    work: "Smaller of 123,547.20 or 0.00"
  - printed: "person[taxpayer].sc[biz_a].ho_pre179_floor"
    value: "123547.20"
    work: "Line 29 pre-179 is positive"
  - printed: "person[taxpayer].sc[biz_a].ho_both_limits"
    value: "no"
    work: "No section 179 possible"
  - printed: "person[taxpayer].sc[biz_a].ho_both"
    value: "0.00"
    work: "Not applicable"
  - printed: "person[taxpayer].sc[biz_a].ho_line5_lim"
    value: "0.00"
    work: "Smaller of room 123,547.20 or line 4 0.00"
  - printed: "person[taxpayer].sc[biz_a].ho_line5"
    value: "0.00"
    work: "Smaller of line 1 or line 4 = 0.00"
  - printed: "person[taxpayer].sc[biz_a].line30"
    value: "0.00"
    work: "No home office deduction"
  - printed: "person[taxpayer].sc[biz_a].line31"
    value: "123547.20"
    work: "123,547.20 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].line31_pre179"
    value: "123547.20"
    work: "123,547.20 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].loss"
    value: "no"
    work: "Line 31 is a profit"
  - printed: "person[taxpayer].sc[biz_a].not_at_risk"
    value: "no"
    work: "Box 32a is checked (all investment at risk)"
  - printed: "person[taxpayer].sc[biz_a].loss_allowed"
    value: "0.00"
    work: "No loss"
  - printed: "person[taxpayer].sc[biz_a].result"
    value: "123547.20"
    work: "Line 31 profit"
  - printed: "person[taxpayer].sc[biz_a].line40"
    value: "0.00"
    work: "Lines 35-39 all 0.00"
  - printed: "person[taxpayer].sc[biz_a].line42"
    value: "0.00"
    work: "0.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].f6"
    value: "0.00"
    work: "Sum of non-listed s179 elected"
  - printed: "person[taxpayer].sc[biz_a].f14"
    value: "0.00"
    work: "Sum of non-listed special allowance"
  - printed: "person[taxpayer].sc[biz_a].f17"
    value: "2536.10"
    work: "item_1 0.00 + item_2 2,536.10"
  - printed: "person[taxpayer].sc[biz_a].f19_y3"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f19_y5"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f19_y7"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f19_y10"
    value: "0.00"
    work: "MACRS 2025 amounts are 0.00"
  - printed: "person[taxpayer].sc[biz_a].f19_y15"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f19_y20"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f19_y15sl"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f25_assets"
    value: "0.00"
    work: "No listed assets"
  - printed: "person[taxpayer].sc[biz_a].f25_veh"
    value: "0.00"
    work: "car_1 0.00"
  - printed: "person[taxpayer].sc[biz_a].f25"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_a].f26_assets"
    value: "0.00"
    work: "Assets are not listed property"
  - printed: "person[taxpayer].sc[biz_a].f26_veh"
    value: "0.00"
    work: "car_1 0.00"
  - printed: "person[taxpayer].sc[biz_a].f26h"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_a].f28"
    value: "0.00"
    work: "Line 25 + line 26 column (h)"
  - printed: "person[taxpayer].sc[biz_a].f29_assets"
    value: "0.00"
    work: "No listed assets"
  - printed: "person[taxpayer].sc[biz_a].f29_veh"
    value: "0.00"
    work: "car_1 0.00"
  - printed: "person[taxpayer].sc[biz_a].f29"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_a].s179_elected"
    value: "0.00"
    work: "f6 0.00 + f29 0.00"
  - printed: "person[taxpayer].sc[biz_a].dep_other"
    value: "2536.10"
    work: "14: 0.00 + 17: 2,536.10 + 19: 0.00 + 21: 0.00"
  - printed: "person[taxpayer].sc[biz_a].s179_return"
    value: "0.00"
    work: "Form 4562 line 12 is 0.00"
  - printed: "person[taxpayer].sc[biz_a].s179_allowed"
    value: "0.00"
    work: "Summary line 12 is 0.00"
  - printed: "person[taxpayer].sc[biz_a].mq_q4_a"
    value: "0.00"
    work: "Sum of asset Q4 basis"
  - printed: "person[taxpayer].sc[biz_a].mq_q4_v"
    value: "0.00"
    work: "Vehicle Q4 basis"
  - printed: "person[taxpayer].sc[biz_a].mq_q4"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_a].mq_total_a"
    value: "0.00"
    work: "Sum of asset basis"
  - printed: "person[taxpayer].sc[biz_a].mq_total_v"
    value: "0.00"
    work: "Vehicle basis"
  - printed: "person[taxpayer].sc[biz_a].mq_total"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_a].cost179_a"
    value: "0.00"
    work: "Sum of asset s179 cost"
  - printed: "person[taxpayer].sc[biz_a].cost179_v"
    value: "0.00"
    work: "Vehicle s179 cost"
  - printed: "person[taxpayer].sc[biz_a].cost179"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_a].veh_lease"
    value: "0.00"
    work: "car_1 lease 0.00"
  - printed: "person[taxpayer].sc[biz_a].profit_pos"
    value: "123547.20"
    work: "Line 31 is positive"
  - printed: "person[taxpayer].sc[biz_a].hi_screened"
    value: "no"
    work: "No health insurance plan and no exceptions"
  - printed: "person[taxpayer].sc[biz_a].f7206_line2"
    value: "0.00"
    work: "No long-term care insurance"
  - printed: "person[taxpayer].sc[biz_a].f7206_line3"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_a].f7206_line4"
    value: "123547.20"
    work: "Net profit of this business"
  - printed: "person[taxpayer].sc[biz_a].f7206_line5"
    value: "123547.20"
    work: "Given total of net profits"
  - printed: "person[taxpayer].sc[biz_a].f7206_has"
    value: "yes"
    work: "123,547.20 > 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line7_pos"
    value: "6574.20"
    work: "6,574.20 x 123,547.20 / 123,547.20"
  - printed: "person[taxpayer].sc[biz_a].f7206_line7"
    value: "6574.20"
    work: "Line 4 is more than zero"
  - printed: "person[taxpayer].sc[biz_a].f7206_line8"
    value: "116973.00"
    work: "123,547.20 - 6,574.20"
  - printed: "person[taxpayer].sc[biz_a].f7206_line9_pos"
    value: "0.00"
    work: "0.00 x ratio"
  - printed: "person[taxpayer].sc[biz_a].f7206_line9"
    value: "0.00"
    work: "Schedule 1 line 16 is 0.00"
  - printed: "person[taxpayer].sc[biz_a].f7206_line10"
    value: "116973.00"
    work: "116,973.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].f7206_line13"
    value: "116973.00"
    work: "116,973.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].f7206_min"
    value: "0.00"
    work: "Smaller of 0.00 or 116,973.00"
  - printed: "person[taxpayer].sc[biz_a].f7206_line14"
    value: "0.00"
    work: "No health insurance"
  - printed: "person[taxpayer].sc[biz_a].qbi_has"
    value: "yes"
    work: "Net profit is 123,547.20"
  - printed: "person[taxpayer].sc[biz_a].qbi_se_pos"
    value: "6574.20"
    work: "6,574.20 x 123,547.20 / 123,547.20"
  - printed: "person[taxpayer].sc[biz_a].qbi_se"
    value: "6574.20"
    work: "Profit business"
  - printed: "person[taxpayer].sc[biz_a].qbi_plan_pos"
    value: "0.00"
    work: "0.00 x ratio"
  - printed: "person[taxpayer].sc[biz_a].qbi_plan"
    value: "0.00"
    work: "Schedule 1 line 16 is 0.00"
  - printed: "person[taxpayer].sc[biz_a].qbi_ded"
    value: "6574.20"
    work: "6,574.20 + 0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_a].qbi"
    value: "116973.00"
    work: "123,547.20 - 6,574.20"
  - printed: "person[taxpayer].sc[biz_b].rrta"
    value: "no"
    work: "No railroad retirement compensation or CT-2"
  - printed: "person[taxpayer].sc[biz_b].screened"
    value: "no"
    work: "All screening answers are no; materially participates"
  - printed: "person[taxpayer].sc[biz_b].line3"
    value: "11971.00"
    work: "11,971.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_b].line4"
    value: "0.00"
    work: "From line 42"
  - printed: "person[taxpayer].sc[biz_b].line5"
    value: "11971.00"
    work: "11,971.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_b].line7"
    value: "11971.00"
    work: "11,971.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_b].line9"
    value: "7914.20"
    work: "Vehicle car_1 car and truck expenses"
  - printed: "person[taxpayer].sc[biz_b].line12"
    value: "0.00"
    work: "No depletion"
  - printed: "person[taxpayer].sc[biz_b].line13"
    value: "0.00"
    work: "No depreciation or s179"
  - printed: "person[taxpayer].sc[biz_b].line20a"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_b].meals_50_ded"
    value: "0.00"
    work: "0.00 x 50%"
  - printed: "person[taxpayer].sc[biz_b].meals_80_ded"
    value: "0.00"
    work: "0.00 x 80%"
  - printed: "person[taxpayer].sc[biz_b].line24b"
    value: "0.00"
    work: "0.00 + 0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_b].line27a"
    value: "0.00"
    work: "No Form 7205"
  - printed: "person[taxpayer].sc[biz_b].line27b"
    value: "0.00"
    work: "Line 48 total is 0.00"
  - printed: "person[taxpayer].sc[biz_b].line28"
    value: "42462.20"
    work: "7,914.20 + 21,214.00 + 13,334.00"
  - printed: "person[taxpayer].sc[biz_b].line29"
    value: "-30491.20"
    work: "11,971.00 - 42,462.20"
  - printed: "person[taxpayer].sc[biz_b].line28_pre179"
    value: "42462.20"
    work: "Line 28 - s179 0.00"
  - printed: "person[taxpayer].sc[biz_b].line29_pre179"
    value: "-30491.20"
    work: "11,971.00 - 42,462.20"
  - printed: "person[taxpayer].sc[biz_b].ho_screened"
    value: "no"
    work: "Simplified method; no listed exceptions apply"
  - printed: "person[taxpayer].sc[biz_b].ho_multi"
    value: "no"
    work: "Count of home-use Schedules C is 1"
  - printed: "person[taxpayer].sc[biz_b].ho_over"
    value: "yes"
    work: "339 > 300 sq ft"
  - printed: "person[taxpayer].sc[biz_b].ho_line4_actual"
    value: "1695.00"
    work: "339 x $5.00"
  - printed: "person[taxpayer].sc[biz_b].ho_line4_cap"
    value: "1500.00"
    work: "300 x $5.00"
  - printed: "person[taxpayer].sc[biz_b].ho_line4"
    value: "1500.00"
    work: "Line 2 is limited to 300 sq ft"
  - printed: "person[taxpayer].sc[biz_b].ho_line1"
    value: "-30491.20"
    work: "Schedule C line 29"
  - printed: "person[taxpayer].sc[biz_b].ho_room"
    value: "-30491.20"
    work: "-30,491.20 - 0.00"
  - printed: "person[taxpayer].sc[biz_b].ho_unlimited"
    value: "no"
    work: "1,500.00 > -30,491.20"
  - printed: "person[taxpayer].sc[biz_b].ho_s179_max"
    value: "0.00"
    work: "Elected 0.00 + carryover 0.00"
  - printed: "person[taxpayer].sc[biz_b].ho_no179"
    value: "yes"
    work: "No election and no carryover"
  - printed: "person[taxpayer].sc[biz_b].ho_limited"
    value: "0.00"
    work: "Smaller is -30,491.20; zero or less so -0-"
  - printed: "person[taxpayer].sc[biz_b].ho_pre179_floor"
    value: "0.00"
    work: "-30,491.20 is zero or less, so -0-"
  - printed: "person[taxpayer].sc[biz_b].ho_both_limits"
    value: "no"
    work: "No section 179 possible"
  - printed: "person[taxpayer].sc[biz_b].ho_both"
    value: "0.00"
    work: "Not applicable"
  - printed: "person[taxpayer].sc[biz_b].ho_line5_lim"
    value: "0.00"
    work: "Room is negative, so -0-"
  - printed: "person[taxpayer].sc[biz_b].ho_line5"
    value: "0.00"
    work: "Smaller of -30,491.20 or 1,500.00; zero or less so -0-"
  - printed: "person[taxpayer].sc[biz_b].line30"
    value: "0.00"
    work: "From simplified worksheet line 5"
  - printed: "person[taxpayer].sc[biz_b].line31"
    value: "-30491.20"
    work: "-30,491.20 - 0.00"
  - printed: "person[taxpayer].sc[biz_b].line31_pre179"
    value: "-30491.20"
    work: "-30,491.20 - 0.00"
  - printed: "person[taxpayer].sc[biz_b].loss"
    value: "yes"
    work: "Line 31 is negative"
  - printed: "person[taxpayer].sc[biz_b].not_at_risk"
    value: "no"
    work: "Box 32a is checked (all investment at risk)"
  - printed: "person[taxpayer].sc[biz_b].loss_allowed"
    value: "-30491.20"
    work: "All at risk and line G yes, so the full loss is allowed"
  - printed: "person[taxpayer].sc[biz_b].result"
    value: "-30491.20"
    work: "Line 31 loss allowed"
  - printed: "person[taxpayer].sc[biz_b].line40"
    value: "0.00"
    work: "Lines 35-39 all 0.00"
  - printed: "person[taxpayer].sc[biz_b].line42"
    value: "0.00"
    work: "0.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_b].f6"
    value: "0.00"
    work: "No assets"
  - printed: "person[taxpayer].sc[biz_b].f14"
    value: "0.00"
    work: "No assets"
  - printed: "person[taxpayer].sc[biz_b].f17"
    value: "0.00"
    work: "No assets"
  - printed: "person[taxpayer].sc[biz_b].f19_y3"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f19_y5"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f19_y7"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f19_y10"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f19_y15"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f19_y20"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f19_y15sl"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f25_assets"
    value: "0.00"
    work: "No assets"
  - printed: "person[taxpayer].sc[biz_b].f25_veh"
    value: "0.00"
    work: "car_1 0.00"
  - printed: "person[taxpayer].sc[biz_b].f25"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_b].f26_assets"
    value: "0.00"
    work: "No assets"
  - printed: "person[taxpayer].sc[biz_b].f26_veh"
    value: "0.00"
    work: "car_1 0.00"
  - printed: "person[taxpayer].sc[biz_b].f26h"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_b].f28"
    value: "0.00"
    work: "Line 25 + line 26 column (h)"
  - printed: "person[taxpayer].sc[biz_b].f29_assets"
    value: "0.00"
    work: "No assets"
  - printed: "person[taxpayer].sc[biz_b].f29_veh"
    value: "0.00"
    work: "car_1 0.00"
  - printed: "person[taxpayer].sc[biz_b].f29"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_b].s179_elected"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_b].dep_other"
    value: "0.00"
    work: "No depreciation"
  - printed: "person[taxpayer].sc[biz_b].s179_return"
    value: "0.00"
    work: "Form 4562 line 12 is 0.00"
  - printed: "person[taxpayer].sc[biz_b].s179_allowed"
    value: "0.00"
    work: "Summary line 12 is 0.00"
  - printed: "person[taxpayer].sc[biz_b].mq_q4_a"
    value: "0.00"
    work: "No assets"
  - printed: "person[taxpayer].sc[biz_b].mq_q4_v"
    value: "0.00"
    work: "car_1 0.00"
  - printed: "person[taxpayer].sc[biz_b].mq_q4"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_b].mq_total_a"
    value: "0.00"
    work: "No assets"
  - printed: "person[taxpayer].sc[biz_b].mq_total_v"
    value: "0.00"
    work: "car_1 0.00"
  - printed: "person[taxpayer].sc[biz_b].mq_total"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_b].cost179_a"
    value: "0.00"
    work: "No assets"
  - printed: "person[taxpayer].sc[biz_b].cost179_v"
    value: "0.00"
    work: "car_1 0.00"
  - printed: "person[taxpayer].sc[biz_b].cost179"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_b].veh_lease"
    value: "0.00"
    work: "car_1 lease 0.00"
  - printed: "person[taxpayer].sc[biz_b].profit_pos"
    value: "0.00"
    work: "Line 31 is a loss"
  - printed: "person[taxpayer].sc[biz_b].hi_screened"
    value: "no"
    work: "No health insurance plan and no exceptions"
  - printed: "person[taxpayer].sc[biz_b].f7206_line2"
    value: "0.00"
    work: "No long-term care insurance"
  - printed: "person[taxpayer].sc[biz_b].f7206_line3"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_b].f7206_line4"
    value: "0.00"
    work: "No net profit"
  - printed: "person[taxpayer].sc[biz_b].f7206_line5"
    value: "123547.20"
    work: "Given total of net profits"
  - printed: "person[taxpayer].sc[biz_b].f7206_has"
    value: "no"
    work: "Line 4 is 0.00"
  - printed: "person[taxpayer].sc[biz_b].f7206_line7_pos"
    value: "0.00"
    work: "6,574.20 x 0.00 / 123,547.20"
  - printed: "person[taxpayer].sc[biz_b].f7206_line7"
    value: "0.00"
    work: "Line 4 is not more than zero"
  - printed: "person[taxpayer].sc[biz_b].f7206_line8"
    value: "0.00"
    work: "0.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_b].f7206_line9_pos"
    value: "0.00"
    work: "0.00 x 0"
  - printed: "person[taxpayer].sc[biz_b].f7206_line9"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f7206_line10"
    value: "0.00"
    work: "0.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_b].f7206_line13"
    value: "0.00"
    work: "0.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_b].f7206_min"
    value: "0.00"
    work: "Smaller of 0.00 or 0.00"
  - printed: "person[taxpayer].sc[biz_b].f7206_line14"
    value: "0.00"
    work: "No health insurance"
  - printed: "person[taxpayer].sc[biz_b].qbi_has"
    value: "no"
    work: "Line 31 is a loss"
  - printed: "person[taxpayer].sc[biz_b].qbi_se_pos"
    value: "0.00"
    work: "6,574.20 x 0.00 / 123,547.20"
  - printed: "person[taxpayer].sc[biz_b].qbi_se"
    value: "0.00"
    work: "No net profit"
  - printed: "person[taxpayer].sc[biz_b].qbi_plan_pos"
    value: "0.00"
    work: "0.00"
  - printed: "person[taxpayer].sc[biz_b].qbi_plan"
    value: "0.00"
    work: "No net profit"
  - printed: "person[taxpayer].sc[biz_b].qbi_ded"
    value: "0.00"
    work: "0.00 + 0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_b].qbi"
    value: "-30491.20"
    work: "-30,491.20 - 0.00"
```
```

### classm.sc.2

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].rrta"
    value: "no"
    work: "No railroad retirement compensation reported"
  - printed: "person[taxpayer].sc[biz_a].screened"
    value: "no"
    work: "All screening questions answered no"
  - printed: "person[taxpayer].sc[biz_a].line3"
    value: "120791.00"
    work: "120,791.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].line4"
    value: "0.00"
    work: "From line 42"
  - printed: "person[taxpayer].sc[biz_a].line5"
    value: "120791.00"
    work: "120,791.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].line7"
    value: "120791.00"
    work: "120,791.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_a].line9"
    value: "0.00"
    work: "No car or truck expenses"
  - printed: "person[taxpayer].sc[biz_a].line12"
    value: "0.00"
    work: "No depletion"
  - printed: "person[taxpayer].sc[biz_a].line13"
    value: "0.00"
    work: "No assets for this business"
  - printed: "person[taxpayer].sc[biz_a].line20a"
    value: "5873.00"
    work: "Machinery, equipment and vehicle rent 5,873.00 + vehicle lease 0.00"
  - printed: "person[taxpayer].sc[biz_a].meals_50_ded"
    value: "0.00"
    work: "50% x 0.00"
  - printed: "person[taxpayer].sc[biz_a].meals_80_ded"
    value: "0.00"
    work: "80% x 0.00"
  - printed: "person[taxpayer].sc[biz_a].line24b"
    value: "0.00"
    work: "0 + 0 + 0"
  - printed: "person[taxpayer].sc[biz_a].line27a"
    value: "0.00"
    work: "No Form 7205"
  - printed: "person[taxpayer].sc[biz_a].line27b"
    value: "0.00"
    work: "Line 48 = 0.00"
  - printed: "person[taxpayer].sc[biz_a].line28"
    value: "22409.00"
    work: "10,450 (20b) + 6,086 (24a) + 5,873 (20a)"
  - printed: "person[taxpayer].sc[biz_a].line29"
    value: "98382.00"
    work: "120,791.00 - 22,409.00"
  - printed: "person[taxpayer].sc[biz_a].line28_pre179"
    value: "22409.00"
    work: "22,409.00 - 0.00 section 179"
  - printed: "person[taxpayer].sc[biz_a].line29_pre179"
    value: "98382.00"
    work: "120,791.00 - 22,409.00"
  - printed: "person[taxpayer].sc[biz_a].ho_screened"
    value: "no"
    work: "No home office claimed"
  - printed: "person[taxpayer].sc[biz_a].ho_multi"
    value: "no"
    work: "0 Schedules C claim home use"
  - printed: "person[taxpayer].sc[biz_a].ho_over"
    value: "no"
    work: "0 square feet is not more than 300"
  - printed: "person[taxpayer].sc[biz_a].ho_line4_actual"
    value: "0.00"
    work: "0 sq ft x rate"
  - printed: "person[taxpayer].sc[biz_a].ho_line4_cap"
    value: "0.00"
    work: "No simplified method used"
  - printed: "person[taxpayer].sc[biz_a].ho_line4"
    value: "0.00"
    work: "0 x 3c"
  - printed: "person[taxpayer].sc[biz_a].ho_line1"
    value: "98382.00"
    work: "Schedule C line 29"
  - printed: "person[taxpayer].sc[biz_a].ho_room"
    value: "98382.00"
    work: "98,382.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].ho_unlimited"
    value: "yes"
    work: "0 <= 98,382.00"
  - printed: "person[taxpayer].sc[biz_a].ho_s179_max"
    value: "0.00"
    work: "Elected 0 + carryover 0"
  - printed: "person[taxpayer].sc[biz_a].ho_no179"
    value: "yes"
    work: "No election and no carryover"
  - printed: "person[taxpayer].sc[biz_a].ho_limited"
    value: "0.00"
    work: "Smaller of 98,382 or 0"
  - printed: "person[taxpayer].sc[biz_a].ho_pre179_floor"
    value: "98382.00"
    work: "98,382.00, which is positive"
  - printed: "person[taxpayer].sc[biz_a].ho_both_limits"
    value: "no"
    work: "Line 4 is 0"
  - printed: "person[taxpayer].sc[biz_a].ho_both"
    value: "0.00"
    work: "Not applicable"
  - printed: "person[taxpayer].sc[biz_a].ho_line5_lim"
    value: "0.00"
    work: "Not applicable"
  - printed: "person[taxpayer].sc[biz_a].ho_line5"
    value: "0.00"
    work: "Smaller of line 1 or 0"
  - printed: "person[taxpayer].sc[biz_a].line30"
    value: "0.00"
    work: "No home office"
  - printed: "person[taxpayer].sc[biz_a].line31"
    value: "98382.00"
    work: "98,382.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].line31_pre179"
    value: "98382.00"
    work: "98,382.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].loss"
    value: "no"
    work: "Line 31 is a profit"
  - printed: "person[taxpayer].sc[biz_a].not_at_risk"
    value: "no"
    work: "All investment is at risk"
  - printed: "person[taxpayer].sc[biz_a].loss_allowed"
    value: "0.00"
    work: "No loss"
  - printed: "person[taxpayer].sc[biz_a].result"
    value: "98382.00"
    work: "Line 31 profit"
  - printed: "person[taxpayer].sc[biz_a].line40"
    value: "0.00"
    work: "Lines 35-39 are all 0"
  - printed: "person[taxpayer].sc[biz_a].line42"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].sc[biz_a].f6"
    value: "0.00"
    work: "No assets"
  - printed: "person[taxpayer].sc[biz_a].f14"
    value: "0.00"
    work: "No assets"
  - printed: "person[taxpayer].sc[biz_a].f17"
    value: "0.00"
    work: "No assets"
  - printed: "person[taxpayer].sc[biz_a].f19_y3"
    value: "0.00"
    work: "No assets"
  - printed: "person[taxpayer].sc[biz_a].f19_y5"
    value: "0.00"
    work: "No assets"
  - printed: "person[taxpayer].sc[biz_a].f19_y7"
    value: "0.00"
    work: "No assets"
  - printed: "person[taxpayer].sc[biz_a].f19_y10"
    value: "0.00"
    work: "No assets"
  - printed: "person[taxpayer].sc[biz_a].f19_y15"
    value: "0.00"
    work: "No assets"
  - printed: "person[taxpayer].sc[biz_a].f19_y20"
    value: "0.00"
    work: "No assets"
  - printed: "person[taxpayer].sc[biz_a].f19_y15sl"
    value: "0.00"
    work: "No assets"
  - printed: "person[taxpayer].sc[biz_a].f25_assets"
    value: "0.00"
    work: "No listed property"
  - printed: "person[taxpayer].sc[biz_a].f25_veh"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_a].f25"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].f26_assets"
    value: "0.00"
    work: "No listed property"
  - printed: "person[taxpayer].sc[biz_a].f26_veh"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_a].f26h"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].f28"
    value: "0.00"
    work: "Lines 25 through 27, column (h)"
  - printed: "person[taxpayer].sc[biz_a].f29_assets"
    value: "0.00"
    work: "No listed property"
  - printed: "person[taxpayer].sc[biz_a].f29_veh"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_a].f29"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].s179_elected"
    value: "0.00"
    work: "f6 + f29 = 0"
  - printed: "person[taxpayer].sc[biz_a].dep_other"
    value: "0.00"
    work: "Lines 14, 17, 19 and 21 are 0"
  - printed: "person[taxpayer].sc[biz_a].s179_return"
    value: "0.00"
    work: "Return has two Schedules C, not one"
  - printed: "person[taxpayer].sc[biz_a].s179_allowed"
    value: "0.00"
    work: "Deduction equals amount elected (0)"
  - printed: "person[taxpayer].sc[biz_a].mq_q4_a"
    value: "0.00"
    work: "No assets"
  - printed: "person[taxpayer].sc[biz_a].mq_q4_v"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_a].mq_q4"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].mq_total_a"
    value: "0.00"
    work: "No assets"
  - printed: "person[taxpayer].sc[biz_a].mq_total_v"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_a].mq_total"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].cost179_a"
    value: "0.00"
    work: "No assets"
  - printed: "person[taxpayer].sc[biz_a].cost179_v"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_a].cost179"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].veh_lease"
    value: "0.00"
    work: "No vehicles entered"
  - printed: "person[taxpayer].sc[biz_a].profit_pos"
    value: "98382.00"
    work: "Line 31 profit"
  - printed: "person[taxpayer].sc[biz_a].hi_screened"
    value: "no"
    work: "No health insurance screening items apply"
  - printed: "person[taxpayer].sc[biz_a].f7206_line2"
    value: "0.00"
    work: "No long-term care insurance"
  - printed: "person[taxpayer].sc[biz_a].f7206_line3"
    value: "0.00"
    work: "No plan under this business"
  - printed: "person[taxpayer].sc[biz_a].f7206_line4"
    value: "98382.00"
    work: "Net profit of this business"
  - printed: "person[taxpayer].sc[biz_a].f7206_line5"
    value: "170500.18"
    work: "Total net profits (given)"
  - printed: "person[taxpayer].sc[biz_a].f7206_has"
    value: "yes"
    work: "98,382.00 > 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line7_pos"
    value: "6519.52"
    work: "11,298.61 x 98,382.00 / 170,500.18"
  - printed: "person[taxpayer].sc[biz_a].f7206_line7"
    value: "6519.52"
    work: "Equals line7_pos"
  - printed: "person[taxpayer].sc[biz_a].f7206_line8"
    value: "91862.48"
    work: "98,382.00 - 6,519.52"
  - printed: "person[taxpayer].sc[biz_a].f7206_line9_pos"
    value: "0.00"
    work: "Schedule 1 line 16 = 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line9"
    value: "0.00"
    work: "0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line10"
    value: "91862.48"
    work: "91,862.48 - 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line13"
    value: "91862.48"
    work: "91,862.48 - 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_min"
    value: "0.00"
    work: "Smaller of 0 or 91,862.48"
  - printed: "person[taxpayer].sc[biz_a].f7206_line14"
    value: "0.00"
    work: "No plan established under this business"
  - printed: "person[taxpayer].sc[biz_a].qbi_has"
    value: "yes"
    work: "Net profit 98,382.00"
  - printed: "person[taxpayer].sc[biz_a].qbi_se_pos"
    value: "6519.52"
    work: "11,298.61 x 98,382.00 / 170,500.18"
  - printed: "person[taxpayer].sc[biz_a].qbi_se"
    value: "6519.52"
    work: "Equals qbi_se_pos"
  - printed: "person[taxpayer].sc[biz_a].qbi_plan_pos"
    value: "0.00"
    work: "Schedule 1 line 16 = 0"
  - printed: "person[taxpayer].sc[biz_a].qbi_plan"
    value: "0.00"
    work: "0"
  - printed: "person[taxpayer].sc[biz_a].qbi_ded"
    value: "6519.52"
    work: "6,519.52 + 0 + 0"
  - printed: "person[taxpayer].sc[biz_a].qbi"
    value: "91862.48"
    work: "98,382.00 - 6,519.52"
  - printed: "person[taxpayer].sc[biz_b].rrta"
    value: "no"
    work: "No railroad retirement compensation reported"
  - printed: "person[taxpayer].sc[biz_b].screened"
    value: "no"
    work: "All screening questions answered no"
  - printed: "person[taxpayer].sc[biz_b].line3"
    value: "165450.00"
    work: "165,450.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_b].line4"
    value: "0.00"
    work: "From line 42"
  - printed: "person[taxpayer].sc[biz_b].line5"
    value: "165450.00"
    work: "165,450.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_b].line7"
    value: "165450.00"
    work: "165,450.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_b].line9"
    value: "0.00"
    work: "No car or truck expenses"
  - printed: "person[taxpayer].sc[biz_b].line12"
    value: "0.00"
    work: "No depletion"
  - printed: "person[taxpayer].sc[biz_b].line13"
    value: "17264.82"
    work: "2,527.00 + 13,709.60 + 1,028.22"
  - printed: "person[taxpayer].sc[biz_b].line20a"
    value: "0.00"
    work: "No rent or lease of vehicles, machinery or equipment"
  - printed: "person[taxpayer].sc[biz_b].meals_50_ded"
    value: "0.00"
    work: "50% x 0.00"
  - printed: "person[taxpayer].sc[biz_b].meals_80_ded"
    value: "0.00"
    work: "80% x 0.00"
  - printed: "person[taxpayer].sc[biz_b].line24b"
    value: "25846.00"
    work: "0 + 0 + 25,846.00 deducted in full"
  - printed: "person[taxpayer].sc[biz_b].line27a"
    value: "0.00"
    work: "No Form 7205"
  - printed: "person[taxpayer].sc[biz_b].line27b"
    value: "0.00"
    work: "Line 48 = 0.00"
  - printed: "person[taxpayer].sc[biz_b].line28"
    value: "93331.82"
    work: "17,264.82 + 24,869 + 6,470 + 25,846 + 18,882"
  - printed: "person[taxpayer].sc[biz_b].line29"
    value: "72118.18"
    work: "165,450.00 - 93,331.82"
  - printed: "person[taxpayer].sc[biz_b].line28_pre179"
    value: "90804.82"
    work: "93,331.82 - 2,527.00"
  - printed: "person[taxpayer].sc[biz_b].line29_pre179"
    value: "74645.18"
    work: "165,450.00 - 90,804.82"
  - printed: "person[taxpayer].sc[biz_b].ho_screened"
    value: "no"
    work: "No home office claimed"
  - printed: "person[taxpayer].sc[biz_b].ho_multi"
    value: "no"
    work: "0 Schedules C claim home use"
  - printed: "person[taxpayer].sc[biz_b].ho_over"
    value: "no"
    work: "0 square feet is not more than 300"
  - printed: "person[taxpayer].sc[biz_b].ho_line4_actual"
    value: "0.00"
    work: "0 sq ft x rate"
  - printed: "person[taxpayer].sc[biz_b].ho_line4_cap"
    value: "0.00"
    work: "No simplified method used"
  - printed: "person[taxpayer].sc[biz_b].ho_line4"
    value: "0.00"
    work: "0 x 3c"
  - printed: "person[taxpayer].sc[biz_b].ho_line1"
    value: "72118.18"
    work: "Schedule C line 29"
  - printed: "person[taxpayer].sc[biz_b].ho_room"
    value: "72118.18"
    work: "74,645.18 - 2,527.00"
  - printed: "person[taxpayer].sc[biz_b].ho_unlimited"
    value: "yes"
    work: "0 <= 72,118.18"
  - printed: "person[taxpayer].sc[biz_b].ho_s179_max"
    value: "2527.00"
    work: "Elected 2,527.00 + carryover 0"
  - printed: "person[taxpayer].sc[biz_b].ho_no179"
    value: "no"
    work: "Section 179 elected"
  - printed: "person[taxpayer].sc[biz_b].ho_limited"
    value: "0.00"
    work: "Smaller of 74,645.18 or 0"
  - printed: "person[taxpayer].sc[biz_b].ho_pre179_floor"
    value: "74645.18"
    work: "74,645.18, which is positive"
  - printed: "person[taxpayer].sc[biz_b].ho_both_limits"
    value: "no"
    work: "Line 4 is 0"
  - printed: "person[taxpayer].sc[biz_b].ho_both"
    value: "0.00"
    work: "Not applicable"
  - printed: "person[taxpayer].sc[biz_b].ho_line5_lim"
    value: "0.00"
    work: "Not applicable"
  - printed: "person[taxpayer].sc[biz_b].ho_line5"
    value: "0.00"
    work: "Smaller of line 1 or 0"
  - printed: "person[taxpayer].sc[biz_b].line30"
    value: "0.00"
    work: "No home office"
  - printed: "person[taxpayer].sc[biz_b].line31"
    value: "72118.18"
    work: "72,118.18 - 0.00"
  - printed: "person[taxpayer].sc[biz_b].line31_pre179"
    value: "74645.18"
    work: "74,645.18 - 0.00"
  - printed: "person[taxpayer].sc[biz_b].loss"
    value: "no"
    work: "Line 31 is a profit"
  - printed: "person[taxpayer].sc[biz_b].not_at_risk"
    value: "no"
    work: "All investment is at risk"
  - printed: "person[taxpayer].sc[biz_b].loss_allowed"
    value: "0.00"
    work: "No loss"
  - printed: "person[taxpayer].sc[biz_b].result"
    value: "72118.18"
    work: "Line 31 profit"
  - printed: "person[taxpayer].sc[biz_b].line40"
    value: "0.00"
    work: "Lines 35-39 are all 0"
  - printed: "person[taxpayer].sc[biz_b].line42"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].sc[biz_b].f6"
    value: "2527.00"
    work: "item_1, not listed property"
  - printed: "person[taxpayer].sc[biz_b].f14"
    value: "13709.60"
    work: "item_1 special allowance"
  - printed: "person[taxpayer].sc[biz_b].f17"
    value: "0.00"
    work: "item_1 MACRS on earlier property = 0"
  - printed: "person[taxpayer].sc[biz_b].f19_y3"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f19_y5"
    value: "1028.22"
    work: "item_1, 5-year property"
  - printed: "person[taxpayer].sc[biz_b].f19_y7"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f19_y10"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f19_y15"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f19_y20"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f19_y15sl"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f25_assets"
    value: "0.00"
    work: "No listed property"
  - printed: "person[taxpayer].sc[biz_b].f25_veh"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_b].f25"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_b].f26_assets"
    value: "0.00"
    work: "Asset is not listed property"
  - printed: "person[taxpayer].sc[biz_b].f26_veh"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_b].f26h"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_b].f28"
    value: "0.00"
    work: "Lines 25 through 27, column (h)"
  - printed: "person[taxpayer].sc[biz_b].f29_assets"
    value: "0.00"
    work: "No listed property"
  - printed: "person[taxpayer].sc[biz_b].f29_veh"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_b].f29"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_b].s179_elected"
    value: "2527.00"
    work: "f6 2,527.00 + f29 0"
  - printed: "person[taxpayer].sc[biz_b].dep_other"
    value: "14737.82"
    work: "13,709.60 + 0 + 1,028.22 + 0"
  - printed: "person[taxpayer].sc[biz_b].s179_return"
    value: "0.00"
    work: "Return has two Schedules C, not one"
  - printed: "person[taxpayer].sc[biz_b].s179_allowed"
    value: "2527.00"
    work: "Deduction equals amount elected; line 12 = 2,527.00"
  - printed: "person[taxpayer].sc[biz_b].mq_q4_a"
    value: "34274.00"
    work: "item_1 fourth-quarter basis"
  - printed: "person[taxpayer].sc[biz_b].mq_q4_v"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_b].mq_q4"
    value: "34274.00"
    work: "34,274.00 + 0"
  - printed: "person[taxpayer].sc[biz_b].mq_total_a"
    value: "34274.00"
    work: "item_1 basis for all of 2025"
  - printed: "person[taxpayer].sc[biz_b].mq_total_v"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_b].mq_total"
    value: "34274.00"
    work: "34,274.00 + 0"
  - printed: "person[taxpayer].sc[biz_b].cost179_a"
    value: "36801.00"
    work: "item_1 section 179 cost"
  - printed: "person[taxpayer].sc[biz_b].cost179_v"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_b].cost179"
    value: "36801.00"
    work: "36,801.00 + 0"
  - printed: "person[taxpayer].sc[biz_b].veh_lease"
    value: "0.00"
    work: "No vehicles entered"
  - printed: "person[taxpayer].sc[biz_b].profit_pos"
    value: "72118.18"
    work: "Line 31 profit"
  - printed: "person[taxpayer].sc[biz_b].hi_screened"
    value: "no"
    work: "No health insurance screening items apply"
  - printed: "person[taxpayer].sc[biz_b].f7206_line2"
    value: "0.00"
    work: "No long-term care insurance"
  - printed: "person[taxpayer].sc[biz_b].f7206_line3"
    value: "7387.00"
    work: "7,387.00 + 0"
  - printed: "person[taxpayer].sc[biz_b].f7206_line4"
    value: "72118.18"
    work: "Net profit of this business"
  - printed: "person[taxpayer].sc[biz_b].f7206_line5"
    value: "170500.18"
    work: "Total net profits (given)"
  - printed: "person[taxpayer].sc[biz_b].f7206_has"
    value: "yes"
    work: "72,118.18 > 0"
  - printed: "person[taxpayer].sc[biz_b].f7206_line7_pos"
    value: "4779.09"
    work: "11,298.61 x 72,118.18 / 170,500.18"
  - printed: "person[taxpayer].sc[biz_b].f7206_line7"
    value: "4779.09"
    work: "Equals line7_pos"
  - printed: "person[taxpayer].sc[biz_b].f7206_line8"
    value: "67339.09"
    work: "72,118.18 - 4,779.09"
  - printed: "person[taxpayer].sc[biz_b].f7206_line9_pos"
    value: "0.00"
    work: "Schedule 1 line 16 = 0"
  - printed: "person[taxpayer].sc[biz_b].f7206_line9"
    value: "0.00"
    work: "0"
  - printed: "person[taxpayer].sc[biz_b].f7206_line10"
    value: "67339.09"
    work: "67,339.09 - 0"
  - printed: "person[taxpayer].sc[biz_b].f7206_line13"
    value: "67339.09"
    work: "67,339.09 - 0"
  - printed: "person[taxpayer].sc[biz_b].f7206_min"
    value: "7387.00"
    work: "Smaller of 7,387.00 or 67,339.09"
  - printed: "person[taxpayer].sc[biz_b].f7206_line14"
    value: "7387.00"
    work: "Line 14 = smaller of line 3 or line 13"
  - printed: "person[taxpayer].sc[biz_b].qbi_has"
    value: "yes"
    work: "Net profit 72,118.18"
  - printed: "person[taxpayer].sc[biz_b].qbi_se_pos"
    value: "4779.09"
    work: "11,298.61 x 72,118.18 / 170,500.18"
  - printed: "person[taxpayer].sc[biz_b].qbi_se"
    value: "4779.09"
    work: "Equals qbi_se_pos"
  - printed: "person[taxpayer].sc[biz_b].qbi_plan_pos"
    value: "0.00"
    work: "Schedule 1 line 16 = 0"
  - printed: "person[taxpayer].sc[biz_b].qbi_plan"
    value: "0.00"
    work: "0"
  - printed: "person[taxpayer].sc[biz_b].qbi_ded"
    value: "12166.09"
    work: "4,779.09 + 0 + 7,387.00"
  - printed: "person[taxpayer].sc[biz_b].qbi"
    value: "59952.09"
    work: "72,118.18 - 12,166.09"
```
```

### classm.sc.3

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].rrta"
    value: "no"
    work: "Given: no railroad retirement compensation or CT-2"
  - printed: "person[taxpayer].sc[biz_a].screened"
    value: "no"
    work: "All screening questions answered no"
  - printed: "person[taxpayer].sc[biz_a].line3"
    value: "179494.00"
    work: "179,494.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].line4"
    value: "0.00"
    work: "From line 42"
  - printed: "person[taxpayer].sc[biz_a].line5"
    value: "179494.00"
    work: "179,494.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].line7"
    value: "182172.00"
    work: "179,494.00 + 2,678.00"
  - printed: "person[taxpayer].sc[biz_a].line9"
    value: "0.00"
    work: "No car or truck expenses given"
  - printed: "person[taxpayer].sc[biz_a].line12"
    value: "0.00"
    work: "No depletion"
  - printed: "person[taxpayer].sc[biz_a].line13"
    value: "2712.80"
    work: "Other depreciation 1,389.80 + section 179 deduction 1,323.00"
  - printed: "person[taxpayer].sc[biz_a].line20a"
    value: "0.00"
    work: "0.00 equipment rent + 0.00 vehicle lease"
  - printed: "person[taxpayer].sc[biz_a].meals_50_ded"
    value: "0.00"
    work: "50% x 0.00"
  - printed: "person[taxpayer].sc[biz_a].meals_80_ded"
    value: "0.00"
    work: "80% x 0.00"
  - printed: "person[taxpayer].sc[biz_a].line24b"
    value: "0.00"
    work: "0 + 0 + 0"
  - printed: "person[taxpayer].sc[biz_a].line27a"
    value: "0.00"
    work: "No Form 7205"
  - printed: "person[taxpayer].sc[biz_a].line27b"
    value: "0.00"
    work: "Line 48 is 0.00"
  - printed: "person[taxpayer].sc[biz_a].line28"
    value: "126902.80"
    work: "29,484 + 14,941 + 16,968 + 2,797 + 30,000 + 30,000 + 2,712.80"
  - printed: "person[taxpayer].sc[biz_a].line29"
    value: "55269.20"
    work: "182,172.00 - 126,902.80"
  - printed: "person[taxpayer].sc[biz_a].line28_pre179"
    value: "125579.80"
    work: "126,902.80 - 1,323.00"
  - printed: "person[taxpayer].sc[biz_a].line29_pre179"
    value: "56592.20"
    work: "182,172.00 - 125,579.80"
  - printed: "person[taxpayer].sc[biz_a].ho_screened"
    value: "no"
    work: "No special home-use circumstances apply"
  - printed: "person[taxpayer].sc[biz_a].ho_multi"
    value: "no"
    work: "Only 1 Schedule C claims home use"
  - printed: "person[taxpayer].sc[biz_a].ho_over"
    value: "yes"
    work: "449 > 300 square feet"
  - printed: "person[taxpayer].sc[biz_a].ho_line4_actual"
    value: "2245.00"
    work: "449 x $5.00"
  - printed: "person[taxpayer].sc[biz_a].ho_line4_cap"
    value: "1500.00"
    work: "300 x $5.00"
  - printed: "person[taxpayer].sc[biz_a].ho_line4"
    value: "1500.00"
    work: "Line 2 limited to 300; 300 x 5.00"
  - printed: "person[taxpayer].sc[biz_a].ho_line1"
    value: "55269.20"
    work: "Schedule C line 29"
  - printed: "person[taxpayer].sc[biz_a].ho_room"
    value: "55269.20"
    work: "56,592.20 - 1,323.00"
  - printed: "person[taxpayer].sc[biz_a].ho_unlimited"
    value: "yes"
    work: "1,500.00 <= 55,269.20"
  - printed: "person[taxpayer].sc[biz_a].ho_s179_max"
    value: "1323.00"
    work: "0.00 elected + 1,323.00 carryover"
  - printed: "person[taxpayer].sc[biz_a].ho_no179"
    value: "no"
    work: "Carryover of 1,323.00 exists"
  - printed: "person[taxpayer].sc[biz_a].ho_limited"
    value: "1500.00"
    work: "Smaller of 56,592.20 or 1,500.00"
  - printed: "person[taxpayer].sc[biz_a].ho_pre179_floor"
    value: "56592.20"
    work: "56,592.20 is positive"
  - printed: "person[taxpayer].sc[biz_a].ho_both_limits"
    value: "no"
    work: "Line 4 fits within the room left after maximum section 179"
  - printed: "person[taxpayer].sc[biz_a].ho_both"
    value: "1500.00"
    work: "Smaller of line 4 or the remaining income; line 4 governs"
  - printed: "person[taxpayer].sc[biz_a].ho_line5_lim"
    value: "1500.00"
    work: "Smaller of 55,269.20 or 1,500.00"
  - printed: "person[taxpayer].sc[biz_a].ho_line5"
    value: "1500.00"
    work: "Smaller of 55,269.20 or 1,500.00"
  - printed: "person[taxpayer].sc[biz_a].line30"
    value: "1500.00"
    work: "Simplified Method Worksheet line 5"
  - printed: "person[taxpayer].sc[biz_a].line31"
    value: "53769.20"
    work: "55,269.20 - 1,500.00"
  - printed: "person[taxpayer].sc[biz_a].line31_pre179"
    value: "55092.20"
    work: "56,592.20 - 1,500.00"
  - printed: "person[taxpayer].sc[biz_a].loss"
    value: "no"
    work: "Line 31 is a profit"
  - printed: "person[taxpayer].sc[biz_a].not_at_risk"
    value: "no"
    work: "All investment is at risk"
  - printed: "person[taxpayer].sc[biz_a].loss_allowed"
    value: "53769.20"
    work: "Line 31 amount; all investment is at risk"
  - printed: "person[taxpayer].sc[biz_a].result"
    value: "53769.20"
    work: "Line 31 profit"
  - printed: "person[taxpayer].sc[biz_a].line40"
    value: "0.00"
    work: "Lines 35-39 are all 0"
  - printed: "person[taxpayer].sc[biz_a].line42"
    value: "0.00"
    work: "0.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].f6"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_a].f14"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_a].f17"
    value: "1389.80"
    work: "1,389.63 + 0.17"
  - printed: "person[taxpayer].sc[biz_a].f19_y3"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f19_y5"
    value: "0.00"
    work: "item_2: 0.00"
  - printed: "person[taxpayer].sc[biz_a].f19_y7"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f19_y10"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f19_y15"
    value: "0.00"
    work: "item_1: 0.00"
  - printed: "person[taxpayer].sc[biz_a].f19_y20"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f19_y15sl"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f25_assets"
    value: "0.00"
    work: "No listed property"
  - printed: "person[taxpayer].sc[biz_a].f25_veh"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_a].f25"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].f26_assets"
    value: "0.00"
    work: "No listed property"
  - printed: "person[taxpayer].sc[biz_a].f26_veh"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_a].f26h"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].f28"
    value: "0.00"
    work: "Lines 25-27 column (h) = 0"
  - printed: "person[taxpayer].sc[biz_a].f29_assets"
    value: "0.00"
    work: "No listed property"
  - printed: "person[taxpayer].sc[biz_a].f29_veh"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_a].f29"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].s179_elected"
    value: "0.00"
    work: "f6 0 + f29 0"
  - printed: "person[taxpayer].sc[biz_a].dep_other"
    value: "1389.80"
    work: "Line 14 0 + line 17 1,389.80 + line 19 0 + line 21 0"
  - printed: "person[taxpayer].sc[biz_a].s179_return"
    value: "1323.00"
    work: "Form 4562 Summary line 12"
  - printed: "person[taxpayer].sc[biz_a].s179_allowed"
    value: "1323.00"
    work: "Only Schedule C; return line 12"
  - printed: "person[taxpayer].sc[biz_a].mq_q4_a"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].mq_q4_v"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_a].mq_q4"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].mq_total_a"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].mq_total_v"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_a].mq_total"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].cost179_a"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].cost179_v"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_a].cost179"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].veh_lease"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_a].profit_pos"
    value: "53769.20"
    work: "Line 31 positive"
  - printed: "person[taxpayer].sc[biz_a].hi_screened"
    value: "no"
    work: "No health insurance plan under this business"
  - printed: "person[taxpayer].sc[biz_a].f7206_line2"
    value: "0.00"
    work: "No long-term care insurance"
  - printed: "person[taxpayer].sc[biz_a].f7206_line3"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line4"
    value: "0.00"
    work: "No plan established under this business"
  - printed: "person[taxpayer].sc[biz_a].f7206_line5"
    value: "53769.20"
    work: "Given total of net profits"
  - printed: "person[taxpayer].sc[biz_a].f7206_has"
    value: "no"
    work: "Line 4 is 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line7_pos"
    value: "0.00"
    work: "Line 4 is 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line7"
    value: "0.00"
    work: "Line 4 is 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line8"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line9_pos"
    value: "0.00"
    work: "Schedule 1 line 16 is 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line9"
    value: "0.00"
    work: "0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line10"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line13"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_min"
    value: "0.00"
    work: "Smaller of 0 or 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line14"
    value: "0.00"
    work: "No health insurance deduction"
  - printed: "person[taxpayer].sc[biz_a].qbi_has"
    value: "yes"
    work: "Line 31 is 53,769.20 > 0"
  - printed: "person[taxpayer].sc[biz_a].qbi_se_pos"
    value: "720.01"
    work: "720.01 x 53,769.20 / 53,769.20"
  - printed: "person[taxpayer].sc[biz_a].qbi_se"
    value: "720.01"
    work: "Profit share applies"
  - printed: "person[taxpayer].sc[biz_a].qbi_plan_pos"
    value: "0.00"
    work: "0 x share"
  - printed: "person[taxpayer].sc[biz_a].qbi_plan"
    value: "0.00"
    work: "0"
  - printed: "person[taxpayer].sc[biz_a].qbi_ded"
    value: "720.01"
    work: "720.01 + 0 + 0"
  - printed: "person[taxpayer].sc[biz_a].qbi"
    value: "53049.19"
    work: "53,769.20 - 720.01"
```
```

### classm.sc.4

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].rrta"
    value: "no"
    work: "No railroad retirement compensation or CT-2 reported"
  - printed: "person[taxpayer].sc[biz_a].screened"
    value: "no"
    work: "All screening questions are answered no"
  - printed: "person[taxpayer].sc[biz_a].line3"
    value: "26838.00"
    work: "26,838.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].line4"
    value: "33384.00"
    work: "From line 42"
  - printed: "person[taxpayer].sc[biz_a].line5"
    value: "-6546.00"
    work: "26,838.00 - 33,384.00"
  - printed: "person[taxpayer].sc[biz_a].line7"
    value: "-6546.00"
    work: "-6,546.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_a].line9"
    value: "1621.90"
    work: "Vehicle car_1 expenses"
  - printed: "person[taxpayer].sc[biz_a].line12"
    value: "0.00"
    work: "No depletion"
  - printed: "person[taxpayer].sc[biz_a].line13"
    value: "6883.21"
    work: "Section 179 of 0 + other depreciation of 6,883.21 + listed property of 0"
  - printed: "person[taxpayer].sc[biz_a].line20a"
    value: "0.00"
    work: "Equipment rent of 0 + vehicle lease of 0"
  - printed: "person[taxpayer].sc[biz_a].meals_50_ded"
    value: "0.00"
    work: "50% x 0"
  - printed: "person[taxpayer].sc[biz_a].meals_80_ded"
    value: "0.00"
    work: "80% x 0"
  - printed: "person[taxpayer].sc[biz_a].line24b"
    value: "22259.00"
    work: "0 + 0 + 22,259 (deducted in full)"
  - printed: "person[taxpayer].sc[biz_a].line27a"
    value: "0.00"
    work: "No Form 7205"
  - printed: "person[taxpayer].sc[biz_a].line27b"
    value: "0.00"
    work: "Line 48 is 0"
  - printed: "person[taxpayer].sc[biz_a].line28"
    value: "40991.11"
    work: "1,621.90 + 6,883.21 + 10,227 + 22,259"
  - printed: "person[taxpayer].sc[biz_a].line29"
    value: "-47537.11"
    work: "-6,546.00 - 40,991.11"
  - printed: "person[taxpayer].sc[biz_a].line28_pre179"
    value: "40991.11"
    work: "Line 28 less section 179 of 0"
  - printed: "person[taxpayer].sc[biz_a].line29_pre179"
    value: "-47537.11"
    work: "-6,546.00 - 40,991.11"
  - printed: "person[taxpayer].sc[biz_a].ho_screened"
    value: "no"
    work: "No home office special cases"
  - printed: "person[taxpayer].sc[biz_a].ho_multi"
    value: "no"
    work: "0 Schedules C claim home use"
  - printed: "person[taxpayer].sc[biz_a].ho_over"
    value: "no"
    work: "0 sq ft is not over 300"
  - printed: "person[taxpayer].sc[biz_a].ho_line4_actual"
    value: "0.00"
    work: "0 x 5.00"
  - printed: "person[taxpayer].sc[biz_a].ho_line4_cap"
    value: "1500.00"
    work: "300 x 5.00"
  - printed: "person[taxpayer].sc[biz_a].ho_line4"
    value: "0.00"
    work: "0 sq ft x 5.00"
  - printed: "person[taxpayer].sc[biz_a].ho_line1"
    value: "-47537.11"
    work: "Schedule C line 29"
  - printed: "person[taxpayer].sc[biz_a].ho_room"
    value: "-47537.11"
    work: "-47,537.11 - 0"
  - printed: "person[taxpayer].sc[biz_a].ho_unlimited"
    value: "no"
    work: "0 is more than -47,537.11"
  - printed: "person[taxpayer].sc[biz_a].ho_s179_max"
    value: "0.00"
    work: "Elected 0 + carryover 0"
  - printed: "person[taxpayer].sc[biz_a].ho_no179"
    value: "yes"
    work: "No election and no carryover"
  - printed: "person[taxpayer].sc[biz_a].ho_limited"
    value: "0.00"
    work: "Smaller of -47,537.11 or 0; if zero or less, enter 0"
  - printed: "person[taxpayer].sc[biz_a].ho_pre179_floor"
    value: "0.00"
    work: "-47,537.11 is less than zero, so 0"
  - printed: "person[taxpayer].sc[biz_a].ho_both_limits"
    value: "no"
    work: "No section 179 is possible"
  - printed: "person[taxpayer].sc[biz_a].ho_both"
    value: "0.00"
    work: "Not applicable"
  - printed: "person[taxpayer].sc[biz_a].ho_line5_lim"
    value: "0.00"
    work: "Not applicable"
  - printed: "person[taxpayer].sc[biz_a].ho_line5"
    value: "0.00"
    work: "Smaller of line 1 or line 4; if zero or less, enter 0"
  - printed: "person[taxpayer].sc[biz_a].line30"
    value: "0.00"
    work: "No home office claimed"
  - printed: "person[taxpayer].sc[biz_a].line31"
    value: "-47537.11"
    work: "-47,537.11 - 0"
  - printed: "person[taxpayer].sc[biz_a].line31_pre179"
    value: "-47537.11"
    work: "Line 29 before 179, less line 30"
  - printed: "person[taxpayer].sc[biz_a].loss"
    value: "yes"
    work: "Line 31 is below 0"
  - printed: "person[taxpayer].sc[biz_a].not_at_risk"
    value: "no"
    work: "All investment is at risk (32a)"
  - printed: "person[taxpayer].sc[biz_a].loss_allowed"
    value: "-47537.11"
    work: "32a checked and material participation, so the loss is not reduced"
  - printed: "person[taxpayer].sc[biz_a].result"
    value: "-47537.11"
    work: "Loss allowed"
  - printed: "person[taxpayer].sc[biz_a].line40"
    value: "44746.00"
    work: "0 + 44,746 + 0 + 0 + 0"
  - printed: "person[taxpayer].sc[biz_a].line42"
    value: "33384.00"
    work: "44,746 - 11,362"
  - printed: "person[taxpayer].sc[biz_a].f6"
    value: "0.00"
    work: "No section 179 elected"
  - printed: "person[taxpayer].sc[biz_a].f14"
    value: "0.00"
    work: "No special allowance"
  - printed: "person[taxpayer].sc[biz_a].f17"
    value: "0.00"
    work: "No pre-2025 MACRS"
  - printed: "person[taxpayer].sc[biz_a].f19_y3"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f19_y5"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f19_y7"
    value: "6883.21"
    work: "item_1, 7-year property"
  - printed: "person[taxpayer].sc[biz_a].f19_y10"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f19_y15"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f19_y20"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f19_y15sl"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f25_assets"
    value: "0.00"
    work: "No listed property"
  - printed: "person[taxpayer].sc[biz_a].f25_veh"
    value: "0.00"
    work: "Vehicle special allowance is 0"
  - printed: "person[taxpayer].sc[biz_a].f25"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].f26_assets"
    value: "0.00"
    work: "item_1 is not listed property"
  - printed: "person[taxpayer].sc[biz_a].f26_veh"
    value: "0.00"
    work: "Vehicle column (h) is 0"
  - printed: "person[taxpayer].sc[biz_a].f26h"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].f28"
    value: "0.00"
    work: "Line 25 + line 26 column (h)"
  - printed: "person[taxpayer].sc[biz_a].f29_assets"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f29_veh"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f29"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].s179_elected"
    value: "0.00"
    work: "f6 + f29 = 0"
  - printed: "person[taxpayer].sc[biz_a].dep_other"
    value: "6883.21"
    work: "0 + 0 + 6,883.21 + 0"
  - printed: "person[taxpayer].sc[biz_a].s179_return"
    value: "0.00"
    work: "Form 4562 line 12 is 0"
  - printed: "person[taxpayer].sc[biz_a].s179_allowed"
    value: "0.00"
    work: "Nothing elected and the return total is 0"
  - printed: "person[taxpayer].sc[biz_a].mq_q4_a"
    value: "0.00"
    work: "item_1 fourth-quarter basis"
  - printed: "person[taxpayer].sc[biz_a].mq_q4_v"
    value: "0.00"
    work: "Vehicle fourth-quarter basis"
  - printed: "person[taxpayer].sc[biz_a].mq_q4"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].mq_total_a"
    value: "48168.00"
    work: "item_1"
  - printed: "person[taxpayer].sc[biz_a].mq_total_v"
    value: "0.00"
    work: "Vehicle"
  - printed: "person[taxpayer].sc[biz_a].mq_total"
    value: "48168.00"
    work: "48,168 + 0"
  - printed: "person[taxpayer].sc[biz_a].cost179_a"
    value: "48168.00"
    work: "item_1"
  - printed: "person[taxpayer].sc[biz_a].cost179_v"
    value: "0.00"
    work: "Vehicle"
  - printed: "person[taxpayer].sc[biz_a].cost179"
    value: "48168.00"
    work: "48,168 + 0"
  - printed: "person[taxpayer].sc[biz_a].veh_lease"
    value: "0.00"
    work: "car_1 lease is 0"
  - printed: "person[taxpayer].sc[biz_a].profit_pos"
    value: "0.00"
    work: "Loss, so 0"
  - printed: "person[taxpayer].sc[biz_a].hi_screened"
    value: "no"
    work: "No special cases"
  - printed: "person[taxpayer].sc[biz_a].f7206_line2"
    value: "4810.00"
    work: "Long-term care, smaller of (a) or (b)"
  - printed: "person[taxpayer].sc[biz_a].f7206_line3"
    value: "4810.00"
    work: "0 + 4,810"
  - printed: "person[taxpayer].sc[biz_a].f7206_line4"
    value: "0.00"
    work: "Business has a loss"
  - printed: "person[taxpayer].sc[biz_a].f7206_line5"
    value: "47327.50"
    work: "Given total of net profits"
  - printed: "person[taxpayer].sc[biz_a].f7206_has"
    value: "no"
    work: "Line 4 is 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line7_pos"
    value: "0.00"
    work: "0 x 0 / 47,327.50"
  - printed: "person[taxpayer].sc[biz_a].f7206_line7"
    value: "0.00"
    work: "Line 4 is 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line8"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line9_pos"
    value: "0.00"
    work: "0 x share"
  - printed: "person[taxpayer].sc[biz_a].f7206_line9"
    value: "0.00"
    work: "Line 4 is 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line10"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line13"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_min"
    value: "0.00"
    work: "Smaller of 4,810 or 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line14"
    value: "0.00"
    work: "Smaller of line 3 or line 13"
  - printed: "person[taxpayer].sc[biz_a].qbi_has"
    value: "no"
    work: "Net loss"
  - printed: "person[taxpayer].sc[biz_a].qbi_se_pos"
    value: "0.00"
    work: "SE deduction of 0 x share"
  - printed: "person[taxpayer].sc[biz_a].qbi_se"
    value: "0.00"
    work: "No profit"
  - printed: "person[taxpayer].sc[biz_a].qbi_plan_pos"
    value: "0.00"
    work: "0 x share"
  - printed: "person[taxpayer].sc[biz_a].qbi_plan"
    value: "0.00"
    work: "No profit"
  - printed: "person[taxpayer].sc[biz_a].qbi_ded"
    value: "0.00"
    work: "0 + 0 + 0"
  - printed: "person[taxpayer].sc[biz_a].qbi"
    value: "-47537.11"
    work: "-47,537.11 - 0"
  - printed: "person[taxpayer].sc[biz_b].rrta"
    value: "no"
    work: "No railroad retirement compensation"
  - printed: "person[taxpayer].sc[biz_b].screened"
    value: "no"
    work: "All screening questions are answered no"
  - printed: "person[taxpayer].sc[biz_b].line3"
    value: "151388.00"
    work: "151,388 - 0"
  - printed: "person[taxpayer].sc[biz_b].line4"
    value: "0.00"
    work: "Line 42"
  - printed: "person[taxpayer].sc[biz_b].line5"
    value: "151388.00"
    work: "151,388 - 0"
  - printed: "person[taxpayer].sc[biz_b].line7"
    value: "154119.00"
    work: "151,388 + 2,731"
  - printed: "person[taxpayer].sc[biz_b].line9"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_b].line12"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].line13"
    value: "0.00"
    work: "No assets"
  - printed: "person[taxpayer].sc[biz_b].line20a"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_b].meals_50_ded"
    value: "209.50"
    work: "50% x 419"
  - printed: "person[taxpayer].sc[biz_b].meals_80_ded"
    value: "0.00"
    work: "80% x 0"
  - printed: "person[taxpayer].sc[biz_b].line24b"
    value: "209.50"
    work: "209.50 + 0 + 0"
  - printed: "person[taxpayer].sc[biz_b].line27a"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].line27b"
    value: "0.00"
    work: "Line 48 is 0"
  - printed: "person[taxpayer].sc[biz_b].line28"
    value: "106791.50"
    work: "30,000 + 20,232 + 30,000 + 209.50 + 26,350"
  - printed: "person[taxpayer].sc[biz_b].line29"
    value: "47327.50"
    work: "154,119 - 106,791.50"
  - printed: "person[taxpayer].sc[biz_b].line28_pre179"
    value: "106791.50"
    work: "No section 179"
  - printed: "person[taxpayer].sc[biz_b].line29_pre179"
    value: "47327.50"
    work: "154,119 - 106,791.50"
  - printed: "person[taxpayer].sc[biz_b].ho_screened"
    value: "no"
    work: "No special cases"
  - printed: "person[taxpayer].sc[biz_b].ho_multi"
    value: "no"
    work: "Count is 0"
  - printed: "person[taxpayer].sc[biz_b].ho_over"
    value: "no"
    work: "0 sq ft"
  - printed: "person[taxpayer].sc[biz_b].ho_line4_actual"
    value: "0.00"
    work: "0 x 5.00"
  - printed: "person[taxpayer].sc[biz_b].ho_line4_cap"
    value: "1500.00"
    work: "300 x 5.00"
  - printed: "person[taxpayer].sc[biz_b].ho_line4"
    value: "0.00"
    work: "0 x 5.00"
  - printed: "person[taxpayer].sc[biz_b].ho_line1"
    value: "47327.50"
    work: "Line 29"
  - printed: "person[taxpayer].sc[biz_b].ho_room"
    value: "47327.50"
    work: "47,327.50 - 0"
  - printed: "person[taxpayer].sc[biz_b].ho_unlimited"
    value: "yes"
    work: "0 <= 47,327.50"
  - printed: "person[taxpayer].sc[biz_b].ho_s179_max"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_b].ho_no179"
    value: "yes"
    work: "No election and no carryover"
  - printed: "person[taxpayer].sc[biz_b].ho_limited"
    value: "0.00"
    work: "Smaller of 47,327.50 or 0"
  - printed: "person[taxpayer].sc[biz_b].ho_pre179_floor"
    value: "47327.50"
    work: "Positive"
  - printed: "person[taxpayer].sc[biz_b].ho_both_limits"
    value: "no"
    work: "No section 179 is possible"
  - printed: "person[taxpayer].sc[biz_b].ho_both"
    value: "0.00"
    work: "Not applicable"
  - printed: "person[taxpayer].sc[biz_b].ho_line5_lim"
    value: "0.00"
    work: "Not applicable"
  - printed: "person[taxpayer].sc[biz_b].ho_line5"
    value: "0.00"
    work: "Smaller of 47,327.50 or 0"
  - printed: "person[taxpayer].sc[biz_b].line30"
    value: "0.00"
    work: "No home office claimed"
  - printed: "person[taxpayer].sc[biz_b].line31"
    value: "47327.50"
    work: "47,327.50 - 0"
  - printed: "person[taxpayer].sc[biz_b].line31_pre179"
    value: "47327.50"
    work: "47,327.50 - 0"
  - printed: "person[taxpayer].sc[biz_b].loss"
    value: "no"
    work: "Profit"
  - printed: "person[taxpayer].sc[biz_b].not_at_risk"
    value: "no"
    work: "All investment is at risk"
  - printed: "person[taxpayer].sc[biz_b].loss_allowed"
    value: "0.00"
    work: "No loss"
  - printed: "person[taxpayer].sc[biz_b].result"
    value: "47327.50"
    work: "Line 31 profit"
  - printed: "person[taxpayer].sc[biz_b].line40"
    value: "0.00"
    work: "All are 0"
  - printed: "person[taxpayer].sc[biz_b].line42"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].sc[biz_b].f6"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f14"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f17"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f19_y3"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f19_y5"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f19_y7"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f19_y10"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f19_y15"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f19_y20"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f19_y15sl"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f25_assets"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f25_veh"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f25"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_b].f26_assets"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f26_veh"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f26h"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_b].f28"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_b].f29_assets"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f29_veh"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f29"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_b].s179_elected"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_b].dep_other"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].s179_return"
    value: "0.00"
    work: "Form 4562 line 12 is 0"
  - printed: "person[taxpayer].sc[biz_b].s179_allowed"
    value: "0.00"
    work: "None elected"
  - printed: "person[taxpayer].sc[biz_b].mq_q4_a"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].mq_q4_v"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].mq_q4"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_b].mq_total_a"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].mq_total_v"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].mq_total"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_b].cost179_a"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].cost179_v"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].cost179"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_b].veh_lease"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].profit_pos"
    value: "47327.50"
    work: "Line 31 profit"
  - printed: "person[taxpayer].sc[biz_b].hi_screened"
    value: "no"
    work: "No special cases"
  - printed: "person[taxpayer].sc[biz_b].f7206_line2"
    value: "0.00"
    work: "No long-term care entry"
  - printed: "person[taxpayer].sc[biz_b].f7206_line3"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_b].f7206_line4"
    value: "47327.50"
    work: "Net profit of this business"
  - printed: "person[taxpayer].sc[biz_b].f7206_line5"
    value: "47327.50"
    work: "Given total"
  - printed: "person[taxpayer].sc[biz_b].f7206_has"
    value: "yes"
    work: "47,327.50 > 0"
  - printed: "person[taxpayer].sc[biz_b].f7206_line7_pos"
    value: "0.00"
    work: "0 x 47,327.50 / 47,327.50"
  - printed: "person[taxpayer].sc[biz_b].f7206_line7"
    value: "0.00"
    work: "Schedule 1 line 15 is 0"
  - printed: "person[taxpayer].sc[biz_b].f7206_line8"
    value: "47327.50"
    work: "47,327.50 - 0"
  - printed: "person[taxpayer].sc[biz_b].f7206_line9_pos"
    value: "0.00"
    work: "0 x 1"
  - printed: "person[taxpayer].sc[biz_b].f7206_line9"
    value: "0.00"
    work: "Schedule 1 line 16 is 0"
  - printed: "person[taxpayer].sc[biz_b].f7206_line10"
    value: "47327.50"
    work: "47,327.50 - 0"
  - printed: "person[taxpayer].sc[biz_b].f7206_line13"
    value: "47327.50"
    work: "47,327.50 - 0"
  - printed: "person[taxpayer].sc[biz_b].f7206_min"
    value: "0.00"
    work: "Smaller of 0 or 47,327.50"
  - printed: "person[taxpayer].sc[biz_b].f7206_line14"
    value: "0.00"
    work: "No health plan established under this business"
  - printed: "person[taxpayer].sc[biz_b].qbi_has"
    value: "yes"
    work: "Net profit"
  - printed: "person[taxpayer].sc[biz_b].qbi_se_pos"
    value: "0.00"
    work: "0 x 47,327.50 / 47,327.50"
  - printed: "person[taxpayer].sc[biz_b].qbi_se"
    value: "0.00"
    work: "From qbi_se_pos"
  - printed: "person[taxpayer].sc[biz_b].qbi_plan_pos"
    value: "0.00"
    work: "0 x share"
  - printed: "person[taxpayer].sc[biz_b].qbi_plan"
    value: "0.00"
    work: "From qbi_plan_pos"
  - printed: "person[taxpayer].sc[biz_b].qbi_ded"
    value: "0.00"
    work: "0 + 0 + 0"
  - printed: "person[taxpayer].sc[biz_b].qbi"
    value: "47327.50"
    work: "47,327.50 - 0"
```
```
