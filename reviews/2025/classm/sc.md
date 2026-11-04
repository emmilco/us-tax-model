# Class M hand-work — sc

`Schedule C (Form 1040) — Profit or Loss From Business, one per business` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt policy | worked-values-request-bound-v2 |
| system sha256 | 18ff9cfe094eedd0548bba02012b0ebf2a58d0606e834e3633432585b4192cb7 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 1044cc4d28f7e00532ffdf3afb6eb0078c69f310eccb8649ad7a2aebae9d259e |
| cases | 2 |
| worked target scope | printed IRS lines |

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
| p538 | None | 17 | pages named by another document's citation | 4186d7aaa8f711c9a524b87fac1e3df05640b6d66130093b2469480acb06ef6c | 17 | f500211df18a4aafd843e48bbad4b9102c598cf5ccc0fae96c7814a4bef0ae00 |
| p463 | For use in preparing 2025 returns | 12 | pages named by another document's citation | 153efad2a94bcccadf643b0f28f913d74b7d70b727f73eca540a2ce4d32bbfda | 12 | a0b14576fdb49a7ba3e7a90092c1b8f6b8ba33889c8c35da5629156346581326 |
| i7206 | 2025 | 1, 2 | whole document | 88aebffe01e22b57dadeb703483459075718cb0b2514fe8f00185975cfbeef3a | 1, 2 | 5bfa308e7e4634d4a0162d76b4af6a4182b8539a390109360875303222231cfe |
| f8995 | 2025; created 2025-09-12 | 1 | whole document | 49922587df3bd093e24470f5b42d0e3382ef8f5210b3cedccb02ccb864f2f65a | - | 8e2e78d7610e1d45e93c10c8b03f9026d46a1166678c6ed93f852569c382f346 |

## Lines

### case classm.sc.1 — prompt sha256 c01c6156292e4f9e2484c832686757e69da26337104cc481098845c6ae681582; branches: sc.rrta:false, sc.statutory:false, sc.passive:true, sc.spouse_owned:false, sc.method_other:false, sc.special:false, sc.screened:false, sc.ho_uses:false, sc.ho_uses:true, sc.ho_other:false, sc.ho_screened:false, sc.ho_multi:false, sc.ho_over:false, sc.ho_line4#0, sc.ho_unlimited:false, sc.ho_unlimited:true, sc.ho_no179:true, sc.ho_limited:left, sc.ho_limited:right, sc.ho_pre179_floor:floor, sc.ho_pre179_floor:positive, sc.ho_both_limits:false, sc.ho_line5_lim#0, sc.ho_line5#0, sc.ho_line5#1, sc.line30#0, sc.line30#1, sc.loss:false, sc.loss:true, sc.at_risk:true, sc.not_at_risk:false, sc.result#0, sc.result#1, sc.inventory_other:false, sc.s179_allowed#0, sc.profit_pos:floor, sc.profit_pos:positive, sc.hi_uses:false, sc.hi_uses:true, sc.hi_screen:false, sc.hi_screened:false, sc.f7206_has:false, sc.f7206_has:true, sc.f7206_line7#0, sc.f7206_line7#1, sc.f7206_line8:floor, sc.f7206_line8:positive, sc.f7206_line9#0, sc.f7206_line9#1, sc.f7206_line10:floor, sc.f7206_line10:positive, sc.f7206_min:left, sc.f7206_min:right, sc.f7206_line14#0, sc.f7206_line14#1, sc.qbi_has:false, sc.qbi_has:true, sc.qbi_se#0, sc.qbi_se#1, sc.qbi_plan#0, sc.qbi_plan#1, sc.tips_ot:false

### classm.sc.1 — person[taxpayer].sc[biz_a].line3 — Subtract line 2 from line 1
Status: **AGREE**

Value: $218,989.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line4 — Cost of goods sold (from line 42)
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line5 — Gross profit. Subtract line 4 from line 3
Status: **AGREE**

Value: $218,989.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line7 — Gross income. Add lines 5 and 6
Status: **AGREE**

Value: $218,989.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line9 — Car and truck expenses
Status: **AGREE**

Value: $3,919.68

### classm.sc.1 — person[taxpayer].sc[biz_a].line12 — Depletion
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line13 — Depreciation and section 179 expense deduction (not included in Part III)
Status: **AGREE**

Value: $2,074.40

### classm.sc.1 — person[taxpayer].sc[biz_a].line20a — Rent or lease: vehicles, machinery, and equipment
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line24b — Deductible meals
Status: **AGREE**

Value: $42,368.40

### classm.sc.1 — person[taxpayer].sc[biz_a].line27a — Energy efficient commercial buildings deduction (attach Form 7205)
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line27b — Other expenses (from line 48)
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line28 — Total expenses before expenses for business use of home. Add lines 8 through 27b
Status: **AGREE**

Value: $91,226.48

### classm.sc.1 — person[taxpayer].sc[biz_a].line29 — Tentative profit or (loss). Subtract line 28 from line 7
Status: **AGREE**

Value: $127,762.52

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_line4 — Multiply line 2 by line 3c
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_line1 — Gross income limitation (Schedule C, line 29)
Status: **AGREE**

Value: $127,762.52

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_line5 — Allowable expenses using the simplified method. Enter the smaller of line 1 or l
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line30 — Expenses for business use of your home
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line31 — Net profit or (loss). Subtract line 30 from line 29
Status: **AGREE**

Value: $127,762.52

### classm.sc.1 — person[taxpayer].sc[biz_a].line40 — Add lines 35 through 39
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line42 — Cost of goods sold. Subtract line 41 from line 40
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].s179_allowed — Section 179 expense deduction for this business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_line2 — Qualified long-term care insurance (the smaller of payments or the age limit, fo
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_line3 — Add lines 1 and 2
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_line4 — Net profit from the trade or business under which the insurance plan is establis
Status: **AGREE**

Value: $127,762.52

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_line5 — Total of all net profits from Schedule C, line 31
Status: **AGREE**

Value: $127,762.52

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_line7 — Multiply Schedule 1 (Form 1040), line 15, deductible part of self-employment tax
Status: **AGREE**

Value: $4,577.39

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_line8 — Subtract line 7 from line 4
Status: **AGREE**

Value: $123,185.13

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_line9 — Schedule 1, line 16, attributable to the same trade or business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_line10 — Subtract line 9 from line 8
Status: **AGREE**

Value: $123,185.13

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_line13 — Subtract line 12 from line 10
Status: **AGREE**

Value: $123,185.13

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_line14 — Self-employed health insurance deduction
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].qbi — Qualified business income or (loss) of this business
Status: **AGREE**

Value: $123,185.13

### classm.sc.1 — person[taxpayer].sc[biz_b].line3 — Subtract line 2 from line 1
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].line4 — Cost of goods sold (from line 42)
Status: **AGREE**

Value: $18,584.00

### classm.sc.1 — person[taxpayer].sc[biz_b].line5 — Gross profit. Subtract line 4 from line 3
Status: **AGREE**

Value: $-18,584.00

### classm.sc.1 — person[taxpayer].sc[biz_b].line7 — Gross income. Add lines 5 and 6
Status: **AGREE**

Value: $-18,584.00

### classm.sc.1 — person[taxpayer].sc[biz_b].line9 — Car and truck expenses
Status: **AGREE**

Value: $31,243.80

### classm.sc.1 — person[taxpayer].sc[biz_b].line12 — Depletion
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].line13 — Depreciation and section 179 expense deduction (not included in Part III)
Status: **AGREE**

Value: $336.08

### classm.sc.1 — person[taxpayer].sc[biz_b].line20a — Rent or lease: vehicles, machinery, and equipment
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

Value: $44,386.88

### classm.sc.1 — person[taxpayer].sc[biz_b].line29 — Tentative profit or (loss). Subtract line 28 from line 7
Status: **AGREE**

Value: $-62,970.88

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_line4 — Multiply line 2 by line 3c
Status: **AGREE**

Value: $975.00

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_line1 — Gross income limitation (Schedule C, line 29)
Status: **AGREE**

Value: $-62,970.88

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_line5 — Allowable expenses using the simplified method. Enter the smaller of line 1 or l
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].line30 — Expenses for business use of your home
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].line31 — Net profit or (loss). Subtract line 30 from line 29
Status: **AGREE**

Value: $-62,970.88

### classm.sc.1 — person[taxpayer].sc[biz_b].line40 — Add lines 35 through 39
Status: **AGREE**

Value: $31,735.00

### classm.sc.1 — person[taxpayer].sc[biz_b].line42 — Cost of goods sold. Subtract line 41 from line 40
Status: **AGREE**

Value: $18,584.00

### classm.sc.1 — person[taxpayer].sc[biz_b].s179_allowed — Section 179 expense deduction for this business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f7206_line2 — Qualified long-term care insurance (the smaller of payments or the age limit, fo
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f7206_line3 — Add lines 1 and 2
Status: **AGREE**

Value: $5,518.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f7206_line4 — Net profit from the trade or business under which the insurance plan is establis
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f7206_line5 — Total of all net profits from Schedule C, line 31
Status: **AGREE**

Value: $127,762.52

### classm.sc.1 — person[taxpayer].sc[biz_b].f7206_line7 — Multiply Schedule 1 (Form 1040), line 15, deductible part of self-employment tax
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f7206_line8 — Subtract line 7 from line 4
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

### classm.sc.1 — person[taxpayer].sc[biz_b].f7206_line14 — Self-employed health insurance deduction
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].qbi — Qualified business income or (loss) of this business
Status: **AGREE**

Value: $-62,970.88

### case classm.sc.2 — prompt sha256 aae029103684f8d5c5680e6186877daf9c74b44b6909702d1115cc64fe5b95c0; branches: sc.rrta:false, sc.statutory:false, sc.passive:true, sc.spouse_owned:false, sc.method_other:false, sc.special:false, sc.screened:false, sc.ho_uses:true, sc.ho_other:false, sc.ho_screened:false, sc.ho_multi:false, sc.ho_over:true, sc.ho_line4#1, sc.ho_unlimited:true, sc.ho_no179:false, sc.ho_limited:left, sc.ho_pre179_floor:positive, sc.ho_both_limits:false, sc.ho_line5_lim#1, sc.ho_line5#0, sc.line30#0, sc.loss:false, sc.result#0, sc.inventory_other:false, sc.s179_allowed#0, sc.profit_pos:positive, sc.hi_uses:false, sc.hi_screen:false, sc.hi_screened:false, sc.f7206_has:true, sc.f7206_line7#0, sc.f7206_line8:positive, sc.f7206_line9#0, sc.f7206_line10:positive, sc.f7206_min:left, sc.f7206_line14#1, sc.qbi_has:true, sc.qbi_se#0, sc.qbi_plan#0

### classm.sc.2 — person[taxpayer].sc[biz_a].line3 — Subtract line 2 from line 1
Status: **AGREE**

Value: $250,000.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line4 — Cost of goods sold (from line 42)
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line5 — Gross profit. Subtract line 4 from line 3
Status: **AGREE**

Value: $250,000.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line7 — Gross income. Add lines 5 and 6
Status: **AGREE**

Value: $250,000.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line9 — Car and truck expenses
Status: **AGREE**

Value: $8,845.01

### classm.sc.2 — person[taxpayer].sc[biz_a].line12 — Depletion
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line13 — Depreciation and section 179 expense deduction (not included in Part III)
Status: **AGREE**

Value: $23,918.50

### classm.sc.2 — person[taxpayer].sc[biz_a].line20a — Rent or lease: vehicles, machinery, and equipment
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

Value: $140,617.51

### classm.sc.2 — person[taxpayer].sc[biz_a].line29 — Tentative profit or (loss). Subtract line 28 from line 7
Status: **AGREE**

Value: $109,382.49

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_line4 — Multiply line 2 by line 3c
Status: **AGREE**

Value: $1,500.00

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_line1 — Gross income limitation (Schedule C, line 29)
Status: **AGREE**

Value: $109,382.49

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_line5 — Allowable expenses using the simplified method. Enter the smaller of line 1 or l
Status: **AGREE**

Value: $1,500.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line30 — Expenses for business use of your home
Status: **AGREE**

Value: $1,500.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line31 — Net profit or (loss). Subtract line 30 from line 29
Status: **AGREE**

Value: $107,882.49

### classm.sc.2 — person[taxpayer].sc[biz_a].line40 — Add lines 35 through 39
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line42 — Cost of goods sold. Subtract line 41 from line 40
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].s179_allowed — Section 179 expense deduction for this business
Status: **AGREE**

Value: $2,733.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_line2 — Qualified long-term care insurance (the smaller of payments or the age limit, fo
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_line3 — Add lines 1 and 2
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_line4 — Net profit from the trade or business under which the insurance plan is establis
Status: **AGREE**

Value: $107,882.49

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_line5 — Total of all net profits from Schedule C, line 31
Status: **AGREE**

Value: $107,882.49

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_line7 — Multiply Schedule 1 (Form 1040), line 15, deductible part of self-employment tax
Status: **AGREE**

Value: $7,621.66

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_line8 — Subtract line 7 from line 4
Status: **AGREE**

Value: $100,260.83

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_line9 — Schedule 1, line 16, attributable to the same trade or business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_line10 — Subtract line 9 from line 8
Status: **AGREE**

Value: $100,260.83

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_line13 — Subtract line 12 from line 10
Status: **AGREE**

Value: $100,260.83

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_line14 — Self-employed health insurance deduction
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].qbi — Qualified business income or (loss) of this business
Status: **AGREE**

Value: $100,260.83

## Raw responses

### classm.sc.1

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].line3"
    value: "218989.00"
    work: "218,989.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].line4"
    value: "0.00"
    work: "From line 42"
  - printed: "person[taxpayer].sc[biz_a].line5"
    value: "218989.00"
    work: "218,989.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].line7"
    value: "218989.00"
    work: "218,989.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_a].line9"
    value: "3919.68"
    work: "car_1 car and truck expenses"
  - printed: "person[taxpayer].sc[biz_a].line12"
    value: "0.00"
    work: "No depletion"
  - printed: "person[taxpayer].sc[biz_a].line13"
    value: "2074.40"
    work: "Vehicle depreciation col (h) 2,074.40 + section 179 0.00"
  - printed: "person[taxpayer].sc[biz_a].line20a"
    value: "0.00"
    work: "No equipment or vehicle rent"
  - printed: "person[taxpayer].sc[biz_a].line24b"
    value: "42368.40"
    work: "50% x 0 + 80% x 22,568 = 18,054.40; plus 24,314.00 deducted in full"
  - printed: "person[taxpayer].sc[biz_a].line27a"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].line27b"
    value: "0.00"
    work: "Line 48 = 0"
  - printed: "person[taxpayer].sc[biz_a].line28"
    value: "91226.48"
    work: "9,574 + 3,919.68 + 2,074.40 + 10,504 + 22,786 + 42,368.40"
  - printed: "person[taxpayer].sc[biz_a].line29"
    value: "127762.52"
    work: "218,989.00 - 91,226.48"
  - printed: "person[taxpayer].sc[biz_a].ho_line4"
    value: "0.00"
    work: "0 sq ft x $5"
  - printed: "person[taxpayer].sc[biz_a].ho_line1"
    value: "127762.52"
    work: "Schedule C line 29"
  - printed: "person[taxpayer].sc[biz_a].ho_line5"
    value: "0.00"
    work: "Smaller of 127,762.52 or 0"
  - printed: "person[taxpayer].sc[biz_a].line30"
    value: "0.00"
    work: "No home office claimed"
  - printed: "person[taxpayer].sc[biz_a].line31"
    value: "127762.52"
    work: "127,762.52 - 0"
  - printed: "person[taxpayer].sc[biz_a].line40"
    value: "0.00"
    work: "Lines 35 through 39 are all 0"
  - printed: "person[taxpayer].sc[biz_a].line42"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].sc[biz_a].s179_allowed"
    value: "0.00"
    work: "Form 4562 summary line 12 = 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line2"
    value: "0.00"
    work: "No long-term care insurance"
  - printed: "person[taxpayer].sc[biz_a].f7206_line3"
    value: "0.00"
    work: "0 + 0; no health plan under this business"
  - printed: "person[taxpayer].sc[biz_a].f7206_line4"
    value: "127762.52"
    work: "Net profit, line 31"
  - printed: "person[taxpayer].sc[biz_a].f7206_line5"
    value: "127762.52"
    work: "Given total of net profits"
  - printed: "person[taxpayer].sc[biz_a].f7206_line7"
    value: "4577.39"
    work: "4,577.39 x (127,762.52 / 127,762.52 = 1.0)"
  - printed: "person[taxpayer].sc[biz_a].f7206_line8"
    value: "123185.13"
    work: "127,762.52 - 4,577.39"
  - printed: "person[taxpayer].sc[biz_a].f7206_line9"
    value: "0.00"
    work: "Schedule 1 line 16 = 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line10"
    value: "123185.13"
    work: "123,185.13 - 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line13"
    value: "123185.13"
    work: "123,185.13 - 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line14"
    value: "0.00"
    work: "Smaller of 0 or 123,185.13"
  - printed: "person[taxpayer].sc[biz_a].qbi"
    value: "123185.13"
    work: "127,762.52 - SE deduction share 4,577.39 - SEHI 0 - plan 0"
  - printed: "person[taxpayer].sc[biz_b].line3"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].sc[biz_b].line4"
    value: "18584.00"
    work: "From line 42"
  - printed: "person[taxpayer].sc[biz_b].line5"
    value: "-18584.00"
    work: "0 - 18,584"
  - printed: "person[taxpayer].sc[biz_b].line7"
    value: "-18584.00"
    work: "-18,584 + 0"
  - printed: "person[taxpayer].sc[biz_b].line9"
    value: "31243.80"
    work: "17,927.00 + 13,316.80"
  - printed: "person[taxpayer].sc[biz_b].line12"
    value: "0.00"
    work: "No depletion"
  - printed: "person[taxpayer].sc[biz_b].line13"
    value: "336.08"
    work: "MACRS on 7-year 2025 property 336.08 + section 179 0 + vehicles 0"
  - printed: "person[taxpayer].sc[biz_b].line20a"
    value: "0.00"
    work: "No equipment or vehicle rent"
  - printed: "person[taxpayer].sc[biz_b].line24b"
    value: "0.00"
    work: "No meals"
  - printed: "person[taxpayer].sc[biz_b].line27a"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].line27b"
    value: "0.00"
    work: "Line 48 = 0"
  - printed: "person[taxpayer].sc[biz_b].line28"
    value: "44386.88"
    work: "31,243.80 + 336.08 + 4,239 + 8,568"
  - printed: "person[taxpayer].sc[biz_b].line29"
    value: "-62970.88"
    work: "-18,584 - 44,386.88"
  - printed: "person[taxpayer].sc[biz_b].ho_line4"
    value: "975.00"
    work: "195 sq ft x $5.00"
  - printed: "person[taxpayer].sc[biz_b].ho_line1"
    value: "-62970.88"
    work: "Schedule C line 29"
  - printed: "person[taxpayer].sc[biz_b].ho_line5"
    value: "0.00"
    work: "Smaller is -62,970.88; zero or less, so enter -0-"
  - printed: "person[taxpayer].sc[biz_b].line30"
    value: "0.00"
    work: "Simplified worksheet line 5"
  - printed: "person[taxpayer].sc[biz_b].line31"
    value: "-62970.88"
    work: "-62,970.88 - 0; all investment at risk (32a), material participation"
  - printed: "person[taxpayer].sc[biz_b].line40"
    value: "31735.00"
    work: "0 + 31,735 + 0 + 0 + 0"
  - printed: "person[taxpayer].sc[biz_b].line42"
    value: "18584.00"
    work: "31,735 - 13,151"
  - printed: "person[taxpayer].sc[biz_b].s179_allowed"
    value: "0.00"
    work: "Form 4562 summary line 12 = 0"
  - printed: "person[taxpayer].sc[biz_b].f7206_line2"
    value: "0.00"
    work: "No long-term care insurance"
  - printed: "person[taxpayer].sc[biz_b].f7206_line3"
    value: "5518.00"
    work: "5,518 + 0"
  - printed: "person[taxpayer].sc[biz_b].f7206_line4"
    value: "0.00"
    work: "Business has a loss, so no net profit"
  - printed: "person[taxpayer].sc[biz_b].f7206_line5"
    value: "127762.52"
    work: "Given total of net profits"
  - printed: "person[taxpayer].sc[biz_b].f7206_line7"
    value: "0.00"
    work: "4,577.39 x (0 / 127,762.52 = 0)"
  - printed: "person[taxpayer].sc[biz_b].f7206_line8"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].sc[biz_b].f7206_line9"
    value: "0.00"
    work: "Schedule 1 line 16 = 0"
  - printed: "person[taxpayer].sc[biz_b].f7206_line10"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].sc[biz_b].f7206_line13"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].sc[biz_b].f7206_line14"
    value: "0.00"
    work: "Smaller of 5,518 or 0"
  - printed: "person[taxpayer].sc[biz_b].qbi"
    value: "-62970.88"
    work: "-62,970.88 - SE deduction share 0 - SEHI 0"
```
```

### classm.sc.2

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].line3"
    value: "250000.00"
    work: "Line 1 250,000.00 - line 2 0.00"
  - printed: "person[taxpayer].sc[biz_a].line4"
    value: "0.00"
    work: "From line 42"
  - printed: "person[taxpayer].sc[biz_a].line5"
    value: "250000.00"
    work: "Line 3 250,000.00 - line 4 0.00"
  - printed: "person[taxpayer].sc[biz_a].line7"
    value: "250000.00"
    work: "Line 5 250,000.00 + line 6 0.00"
  - printed: "person[taxpayer].sc[biz_a].line9"
    value: "8845.01"
    work: "Car_1 5,320.58 + car_2 3,524.43"
  - printed: "person[taxpayer].sc[biz_a].line12"
    value: "0.00"
    work: "No depletion"
  - printed: "person[taxpayer].sc[biz_a].line13"
    value: "23918.50"
    work: "4562 line 22: s179 2,733.00 + line 19 MACRS 6,536.10 + line 21/28 listed (575.74 + 14,073.66)"
  - printed: "person[taxpayer].sc[biz_a].line20a"
    value: "0.00"
    work: "No equipment or vehicle rent"
  - printed: "person[taxpayer].sc[biz_a].line24b"
    value: "0.00"
    work: "No meals"
  - printed: "person[taxpayer].sc[biz_a].line27a"
    value: "0.00"
    work: "No Form 7205"
  - printed: "person[taxpayer].sc[biz_a].line27b"
    value: "0.00"
    work: "Line 48 is 0"
  - printed: "person[taxpayer].sc[biz_a].line28"
    value: "140617.51"
    work: "8,845.01 + 30,000 + 23,918.50 + 29,987 + 20,082 + 13,258 + 14,527"
  - printed: "person[taxpayer].sc[biz_a].line29"
    value: "109382.49"
    work: "Line 7 250,000.00 - line 28 140,617.51"
  - printed: "person[taxpayer].sc[biz_a].ho_line4"
    value: "1500.00"
    work: "Line 2 min(365, 300) = 300 x line 3c $5.00"
  - printed: "person[taxpayer].sc[biz_a].ho_line1"
    value: "109382.49"
    work: "Schedule C line 29; no home gains or losses"
  - printed: "person[taxpayer].sc[biz_a].ho_line5"
    value: "1500.00"
    work: "Smaller of 109,382.49 or 1,500.00"
  - printed: "person[taxpayer].sc[biz_a].line30"
    value: "1500.00"
    work: "Simplified worksheet line 5"
  - printed: "person[taxpayer].sc[biz_a].line31"
    value: "107882.49"
    work: "Line 29 109,382.49 - line 30 1,500.00"
  - printed: "person[taxpayer].sc[biz_a].line40"
    value: "0.00"
    work: "Lines 35-39 are all 0"
  - printed: "person[taxpayer].sc[biz_a].line42"
    value: "0.00"
    work: "Line 40 0 - line 41 0"
  - printed: "person[taxpayer].sc[biz_a].s179_allowed"
    value: "2733.00"
    work: "Summary 4562 line 12 is 2,733.00; one business"
  - printed: "person[taxpayer].sc[biz_a].f7206_line2"
    value: "0.00"
    work: "No long-term care insurance"
  - printed: "person[taxpayer].sc[biz_a].f7206_line3"
    value: "0.00"
    work: "Line 1 0 + line 2 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line4"
    value: "107882.49"
    work: "Schedule C line 31 net profit"
  - printed: "person[taxpayer].sc[biz_a].f7206_line5"
    value: "107882.49"
    work: "Given total of net profits"
  - printed: "person[taxpayer].sc[biz_a].f7206_line7"
    value: "7621.66"
    work: "7,621.66 x (107,882.49 / 107,882.49 = 1.0)"
  - printed: "person[taxpayer].sc[biz_a].f7206_line8"
    value: "100260.83"
    work: "107,882.49 - 7,621.66"
  - printed: "person[taxpayer].sc[biz_a].f7206_line9"
    value: "0.00"
    work: "Schedule 1 line 16 is 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line10"
    value: "100260.83"
    work: "Line 8 - line 9"
  - printed: "person[taxpayer].sc[biz_a].f7206_line13"
    value: "100260.83"
    work: "Line 10 - line 12 (0)"
  - printed: "person[taxpayer].sc[biz_a].f7206_line14"
    value: "0.00"
    work: "Smaller of line 3 (0) or line 13"
  - printed: "person[taxpayer].sc[biz_a].qbi"
    value: "100260.83"
    work: "107,882.49 - SE tax deduction 7,621.66 - SEP 0 - SEHI 0"
```
```
