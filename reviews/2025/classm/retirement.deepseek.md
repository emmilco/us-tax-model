# Class M hand-work — retirement

`Form 1099-R distributions (IRAs, pensions and annuities)` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.deepseek.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-29 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt policy | worked-values-request-bound-v2 |
| system sha256 | 18ff9cfe094eedd0548bba02012b0ebf2a58d0606e834e3633432585b4192cb7 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | bab37e774cf6e78d4acf71f846c6754e4fcac86c1cc607a649ffb269ad60ab8c |
| cases | 6 |
| worked target scope | printed IRS lines |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1099r | 2025 (calendar-year form) | 5, 7 | cited pages | 97b0b54ae7c95303418077d54e349c0106cbbd5c4b5695ef684c23c39a5fda3f | 5, 7 | af300d066f4492afc97aa90824bfc681581f64482976e6d6a705e7e94b0e4e67 |
| i1040gi | 2025; printed date 2026-02-25 | 26, 27, 28, 29, 30, 31 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 26, 27, 28, 30, 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i5329 | 2025 | 1, 3, 5 | cited pages | bc85a048e4293ab244d68023ac7bb45333ceede0763b3b1cb3430eb4829a18bf | 1, 3, 5 | e46adbf118d780a00b73957b6ef4c6e436e651f6f076a36fa9b6717bd138ee5d |
| f8880 | 2025; created 2025-11-04 | 1, 2 | whole document | e8b37e5065850674d94eecd145d787e1789924b0c2b09bf3693992c45ba9dc94 | 2 | e082ccb481b2d0e872449d7728c290669213b8d16d4c94f281c1bb70aeaed575 |

## Lines

### case classm.retirement.1 — prompt sha256 1d8a445839943786a3c79fdd3361a2c58b5e070d30a334656bf2d78453b50b85; branches: retirement.special:false, retirement.annuity:false, retirement.annuity:true, retirement.used_last_year:false, retirement.used_last_year:true, retirement.joint_life:false, retirement.joint_life:true, retirement.is_ira:false, retirement.is_ira:true, retirement.roth:false, retirement.direct:false, retirement.bad_code:false, retirement.rolled#1, retirement.has_rollover:false, retirement.has_rollover:true, retirement.smw4_table1#1, retirement.smw4_table1#4, retirement.smw4_table2#0, retirement.smw4_table2#4, retirement.smw4_new#0, retirement.smw4_new#1, retirement.smw4#0, retirement.smw4#1, retirement.smw8:left, retirement.smw8:right, retirement.smw9:floor, retirement.smw9:positive, retirement.cost_left:false, retirement.cost_left:true, retirement.annuity_with_cost:false, retirement.annuity_with_cost:true, retirement.annuity_rollover:false, retirement.annuity_taxable#0, retirement.annuity_taxable#1, retirement.ira_taxable#1, retirement.ira_not_rolled:floor, retirement.ira_not_rolled:positive, retirement.plan_simple:floor, retirement.plan_simple:positive, retirement.plan_taxable#0, retirement.plan_taxable#1, retirement.taxable#0, retirement.taxable#1, retirement.show_a:true, retirement.amount_a#0, retirement.sav_military:false, retirement.sav_404k:false, retirement.sav_inherited:false, retirement.sav_excluded:false, retirement.sav_gross:floor, retirement.sav_gross:positive, retirement.sav_amount#1, retirement.early:false, retirement.early:true, retirement.early_screen:false, retirement.code_screen:false, retirement.screen_refused:false, retirement.has_exception:false, retirement.has_exception:true, retirement.wrong_kind:false, retirement.l1#0, retirement.l1#1, retirement.exc_capped:left, retirement.exc_capped:right, retirement.l2#0, retirement.l2#1, retirement.is_e05:false, retirement.l2_e05#1, retirement.is_e09:false, retirement.l2_e09#1, retirement.is_e19:false, retirement.l2_e19#1, retirement.is_e22:false, retirement.is_e22:true, retirement.l2_e22#0, retirement.l2_e22#1, retirement.is_e23:false, retirement.l2_e23#1, retirement.is_s:false, retirement.l1_s#1, retirement.l2_s#1

### classm.retirement.1 — person[taxpayer].retirement[r1].smw1 — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — person[taxpayer].retirement[r1].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $6,276.00

### classm.retirement.1 — person[taxpayer].retirement[r1].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last
Status: **AGREE**

Value: $892.00

### classm.retirement.1 — person[taxpayer].retirement[r1].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $10,704.00

### classm.retirement.1 — person[taxpayer].retirement[r1].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $4,043.00

### classm.retirement.1 — person[taxpayer].retirement[r1].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $2,233.00

### classm.retirement.1 — person[taxpayer].retirement[r1].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $2,233.00

### classm.retirement.1 — person[taxpayer].retirement[r1].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — person[taxpayer].retirement[r1].smw10 — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **AGREE**

Value: $6,276.00

### classm.retirement.1 — person[taxpayer].retirement[r1].smw11 — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — person[taxpayer].retirement[r2].smw1 — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **AGREE**

Value: $28,224.00

### classm.retirement.1 — person[taxpayer].retirement[r2].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — person[taxpayer].retirement[r2].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — person[taxpayer].retirement[r2].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — person[taxpayer].retirement[r2].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — person[taxpayer].retirement[r2].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — person[taxpayer].retirement[r2].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — person[taxpayer].retirement[r2].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $28,224.00

### classm.retirement.1 — person[taxpayer].retirement[r2].smw10 — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — person[taxpayer].retirement[r2].smw11 — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **AGREE**

Value: $0.00

### case classm.retirement.2 — prompt sha256 16265d5053532888d3bcd8763e98d8e3248737646749f34e903762f9ebc8bb90; branches: retirement.special:false, retirement.annuity:false, retirement.used_last_year:false, retirement.used_last_year:true, retirement.joint_life:false, retirement.joint_life:true, retirement.is_ira:true, retirement.roth:false, retirement.roth:true, retirement.direct:false, retirement.bad_code:false, retirement.rolled#1, retirement.has_rollover:false, retirement.smw4_table1#1, retirement.smw4_table1#2, retirement.smw4_table2#1, retirement.smw4_table2#2, retirement.smw4_new#0, retirement.smw4_new#1, retirement.smw4#0, retirement.smw4#1, retirement.smw8:left, retirement.smw9:floor, retirement.smw9:positive, retirement.cost_left:false, retirement.annuity_with_cost:false, retirement.annuity_rollover:false, retirement.annuity_taxable#1, retirement.ira_taxable#0, retirement.ira_taxable#1, retirement.ira_not_rolled:floor, retirement.ira_not_rolled:positive, retirement.plan_simple:floor, retirement.plan_simple:positive, retirement.plan_taxable#1, retirement.taxable#0, retirement.show_a:false, retirement.show_a:true, retirement.amount_a#0, retirement.amount_a#1, retirement.sav_military:false, retirement.sav_404k:false, retirement.sav_inherited:false, retirement.sav_inherited:true, retirement.sav_excluded:false, retirement.sav_excluded:true, retirement.sav_gross:floor, retirement.sav_gross:positive, retirement.sav_amount#0, retirement.sav_amount#1, retirement.early:false, retirement.early:true, retirement.early_screen:false, retirement.code_screen:false, retirement.screen_refused:false, retirement.has_exception:false, retirement.wrong_kind:false, retirement.l1#0, retirement.l1#1, retirement.exc_capped:left, retirement.l2#1, retirement.is_e05:false, retirement.l2_e05#1, retirement.is_e09:false, retirement.l2_e09#1, retirement.is_e19:false, retirement.l2_e19#1, retirement.is_e22:false, retirement.l2_e22#1, retirement.is_e23:false, retirement.l2_e23#1, retirement.is_s:false, retirement.l1_s#1, retirement.l2_s#1

### classm.retirement.2 — person[taxpayer].retirement[r1].smw1 — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — person[taxpayer].retirement[r1].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — person[taxpayer].retirement[r1].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — person[taxpayer].retirement[r1].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — person[taxpayer].retirement[r1].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — person[taxpayer].retirement[r1].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — person[taxpayer].retirement[r1].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — person[taxpayer].retirement[r1].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — person[taxpayer].retirement[r1].smw10 — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — person[taxpayer].retirement[r1].smw11 — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — person[taxpayer].retirement[r2].smw1 — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **AGREE**

Value: $36,791.00

### classm.retirement.2 — person[taxpayer].retirement[r2].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — person[taxpayer].retirement[r2].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — person[taxpayer].retirement[r2].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — person[taxpayer].retirement[r2].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — person[taxpayer].retirement[r2].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — person[taxpayer].retirement[r2].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — person[taxpayer].retirement[r2].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $36,791.00

### classm.retirement.2 — person[taxpayer].retirement[r2].smw10 — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — person[taxpayer].retirement[r2].smw11 — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **AGREE**

Value: $0.00

### case classm.retirement.3 — prompt sha256 ca1de3903391b2f048d052f5ce7956ff560a1eaa61751982fc367ce94f1b7197; branches: retirement.special:false, retirement.annuity:false, retirement.used_last_year:true, retirement.joint_life:true, retirement.is_ira:true, retirement.roth:false, retirement.direct:false, retirement.bad_code:false, retirement.rolled#1, retirement.has_rollover:false, retirement.smw4_table1#4, retirement.smw4_table2#1, retirement.smw4_new#0, retirement.smw4#0, retirement.smw8:left, retirement.smw9:positive, retirement.cost_left:false, retirement.annuity_with_cost:false, retirement.annuity_rollover:false, retirement.annuity_taxable#1, retirement.ira_taxable#1, retirement.ira_not_rolled:positive, retirement.plan_simple:positive, retirement.plan_taxable#1, retirement.taxable#0, retirement.show_a:false, retirement.amount_a#1, retirement.sav_military:false, retirement.sav_404k:false, retirement.sav_inherited:false, retirement.sav_excluded:false, retirement.sav_gross:positive, retirement.sav_amount#1, retirement.early:true, retirement.early_screen:false, retirement.code_screen:false, retirement.screen_refused:false, retirement.has_exception:true, retirement.wrong_kind:false, retirement.l1#0, retirement.exc_capped:left, retirement.l2#0, retirement.is_e05:false, retirement.l2_e05#1, retirement.is_e09:false, retirement.l2_e09#1, retirement.is_e19:true, retirement.l2_e19#0, retirement.is_e22:false, retirement.l2_e22#1, retirement.is_e23:false, retirement.l2_e23#1, retirement.is_s:true, retirement.l1_s#0, retirement.l2_s#0

### classm.retirement.3 — person[taxpayer].retirement[r1].smw1 — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **AGREE**

Value: $11,843.00

### classm.retirement.3 — person[taxpayer].retirement[r1].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $0.00

### classm.retirement.3 — person[taxpayer].retirement[r1].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last
Status: **AGREE**

Value: $0.00

### classm.retirement.3 — person[taxpayer].retirement[r1].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $0.00

### classm.retirement.3 — person[taxpayer].retirement[r1].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $0.00

### classm.retirement.3 — person[taxpayer].retirement[r1].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $0.00

### classm.retirement.3 — person[taxpayer].retirement[r1].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $0.00

### classm.retirement.3 — person[taxpayer].retirement[r1].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $11,843.00

### classm.retirement.3 — person[taxpayer].retirement[r1].smw10 — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **AGREE**

Value: $0.00

### classm.retirement.3 — person[taxpayer].retirement[r1].smw11 — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **AGREE**

Value: $0.00

### case classm.retirement.4 — prompt sha256 16e6243fad015d4e0f21dd9f04dcce9a326bbc2d14f5bf39d95f27c9f00db437; branches: retirement.special:false, retirement.annuity:false, retirement.used_last_year:true, retirement.joint_life:false, retirement.is_ira:false, retirement.is_ira:true, retirement.roth:false, retirement.direct:false, retirement.direct:true, retirement.bad_code:false, retirement.rolled#0, retirement.rolled#1, retirement.has_rollover:false, retirement.has_rollover:true, retirement.smw4_table1#0, retirement.smw4_table1#3, retirement.smw4_table2#1, retirement.smw4_table2#3, retirement.smw4_new#1, retirement.smw4#0, retirement.smw8:left, retirement.smw9:positive, retirement.cost_left:false, retirement.annuity_with_cost:false, retirement.annuity_rollover:false, retirement.annuity_taxable#1, retirement.ira_taxable#1, retirement.ira_not_rolled:floor, retirement.ira_not_rolled:positive, retirement.plan_simple:floor, retirement.plan_simple:positive, retirement.plan_taxable#1, retirement.taxable#0, retirement.taxable#1, retirement.show_a:false, retirement.show_a:true, retirement.amount_a#0, retirement.amount_a#1, retirement.sav_military:false, retirement.sav_404k:false, retirement.sav_inherited:false, retirement.sav_excluded:false, retirement.sav_gross:floor, retirement.sav_gross:positive, retirement.sav_amount#1, retirement.early:false, retirement.early_screen:false, retirement.code_screen:false, retirement.screen_refused:false, retirement.has_exception:false, retirement.wrong_kind:false, retirement.l1#1, retirement.exc_capped:left, retirement.l2#1, retirement.is_e05:false, retirement.l2_e05#1, retirement.is_e09:false, retirement.l2_e09#1, retirement.is_e19:false, retirement.l2_e19#1, retirement.is_e22:false, retirement.l2_e22#1, retirement.is_e23:false, retirement.l2_e23#1, retirement.is_s:false, retirement.l1_s#1, retirement.l2_s#1

### classm.retirement.4 — person[taxpayer].retirement[r1].smw1 — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **AGREE**

Value: $10,905.00

### classm.retirement.4 — person[taxpayer].retirement[r1].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $0.00

### classm.retirement.4 — person[taxpayer].retirement[r1].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last
Status: **AGREE**

Value: $0.00

### classm.retirement.4 — person[taxpayer].retirement[r1].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $0.00

### classm.retirement.4 — person[taxpayer].retirement[r1].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $0.00

### classm.retirement.4 — person[taxpayer].retirement[r1].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $0.00

### classm.retirement.4 — person[taxpayer].retirement[r1].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $0.00

### classm.retirement.4 — person[taxpayer].retirement[r1].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $10,905.00

### classm.retirement.4 — person[taxpayer].retirement[r1].smw10 — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **AGREE**

Value: $0.00

### classm.retirement.4 — person[taxpayer].retirement[r1].smw11 — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **AGREE**

Value: $0.00

### classm.retirement.4 — person[taxpayer].retirement[r2].smw1 — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **AGREE**

Value: $37,628.00

### classm.retirement.4 — person[taxpayer].retirement[r2].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $0.00

### classm.retirement.4 — person[taxpayer].retirement[r2].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last
Status: **AGREE**

Value: $0.00

### classm.retirement.4 — person[taxpayer].retirement[r2].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $0.00

### classm.retirement.4 — person[taxpayer].retirement[r2].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $0.00

### classm.retirement.4 — person[taxpayer].retirement[r2].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $0.00

### classm.retirement.4 — person[taxpayer].retirement[r2].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $0.00

### classm.retirement.4 — person[taxpayer].retirement[r2].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $37,628.00

### classm.retirement.4 — person[taxpayer].retirement[r2].smw10 — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **AGREE**

Value: $0.00

### classm.retirement.4 — person[taxpayer].retirement[r2].smw11 — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **AGREE**

Value: $0.00

### case classm.retirement.5 — prompt sha256 2ab2507d280b5ff266b233f86ea1300266a3cf86f460512973c6a8fba785e866; branches: retirement.special:false, retirement.annuity:false, retirement.used_last_year:false, retirement.joint_life:true, retirement.is_ira:true, retirement.roth:false, retirement.direct:false, retirement.bad_code:false, retirement.rolled#1, retirement.has_rollover:false, retirement.smw4_table1#0, retirement.smw4_table2#4, retirement.smw4_new#0, retirement.smw4#1, retirement.smw8:left, retirement.smw9:floor, retirement.cost_left:false, retirement.annuity_with_cost:false, retirement.annuity_rollover:false, retirement.annuity_taxable#1, retirement.ira_taxable#1, retirement.ira_not_rolled:floor, retirement.plan_simple:floor, retirement.plan_taxable#1, retirement.taxable#0, retirement.show_a:false, retirement.amount_a#1, retirement.sav_military:false, retirement.sav_404k:false, retirement.sav_inherited:false, retirement.sav_excluded:false, retirement.sav_gross:floor, retirement.sav_amount#1, retirement.early:true, retirement.early_screen:false, retirement.code_screen:false, retirement.screen_refused:false, retirement.has_exception:true, retirement.wrong_kind:false, retirement.l1#0, retirement.exc_capped:right, retirement.l2#0, retirement.is_e05:false, retirement.l2_e05#1, retirement.is_e09:false, retirement.l2_e09#1, retirement.is_e19:false, retirement.l2_e19#1, retirement.is_e22:false, retirement.l2_e22#1, retirement.is_e23:true, retirement.l2_e23#0, retirement.is_s:false, retirement.l1_s#1, retirement.l2_s#1

### classm.retirement.5 — person[taxpayer].retirement[r1].smw1 — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **AGREE**

Value: $0.00

### classm.retirement.5 — person[taxpayer].retirement[r1].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $0.00

### classm.retirement.5 — person[taxpayer].retirement[r1].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last
Status: **AGREE**

Value: $0.00

### classm.retirement.5 — person[taxpayer].retirement[r1].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $0.00

### classm.retirement.5 — person[taxpayer].retirement[r1].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $0.00

### classm.retirement.5 — person[taxpayer].retirement[r1].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $0.00

### classm.retirement.5 — person[taxpayer].retirement[r1].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $0.00

### classm.retirement.5 — person[taxpayer].retirement[r1].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $0.00

### classm.retirement.5 — person[taxpayer].retirement[r1].smw10 — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **AGREE**

Value: $0.00

### classm.retirement.5 — person[taxpayer].retirement[r1].smw11 — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **AGREE**

Value: $0.00

### case classm.retirement.6 — prompt sha256 89c3762a68e020a3d65d7e08100a76e960ed5c8226311d824f6779459557e88d; branches: retirement.special:false, retirement.annuity:false, retirement.used_last_year:true, retirement.joint_life:false, retirement.joint_life:true, retirement.is_ira:false, retirement.is_ira:true, retirement.roth:false, retirement.direct:false, retirement.bad_code:false, retirement.rolled#1, retirement.has_rollover:false, retirement.smw4_table1#0, retirement.smw4_table1#4, retirement.smw4_table2#2, retirement.smw4_table2#4, retirement.smw4_new#0, retirement.smw4_new#1, retirement.smw4#0, retirement.smw8:left, retirement.smw9:positive, retirement.cost_left:false, retirement.annuity_with_cost:false, retirement.annuity_rollover:false, retirement.annuity_taxable#1, retirement.ira_taxable#1, retirement.ira_not_rolled:positive, retirement.plan_simple:positive, retirement.plan_taxable#1, retirement.taxable#0, retirement.taxable#1, retirement.show_a:false, retirement.amount_a#1, retirement.sav_military:false, retirement.sav_military:true, retirement.sav_404k:false, retirement.sav_inherited:false, retirement.sav_excluded:false, retirement.sav_excluded:true, retirement.sav_gross:positive, retirement.sav_amount#0, retirement.sav_amount#1, retirement.early:false, retirement.early_screen:false, retirement.code_screen:false, retirement.screen_refused:false, retirement.has_exception:false, retirement.wrong_kind:false, retirement.l1#1, retirement.exc_capped:left, retirement.l2#1, retirement.is_e05:false, retirement.l2_e05#1, retirement.is_e09:false, retirement.l2_e09#1, retirement.is_e19:false, retirement.l2_e19#1, retirement.is_e22:false, retirement.l2_e22#1, retirement.is_e23:false, retirement.l2_e23#1, retirement.is_s:false, retirement.l1_s#1, retirement.l2_s#1

### classm.retirement.6 — person[taxpayer].retirement[r1].smw1 — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **AGREE**

Value: $1,173.00

### classm.retirement.6 — person[taxpayer].retirement[r1].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $0.00

### classm.retirement.6 — person[taxpayer].retirement[r1].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last
Status: **AGREE**

Value: $0.00

### classm.retirement.6 — person[taxpayer].retirement[r1].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $0.00

### classm.retirement.6 — person[taxpayer].retirement[r1].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $0.00

### classm.retirement.6 — person[taxpayer].retirement[r1].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $0.00

### classm.retirement.6 — person[taxpayer].retirement[r1].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $0.00

### classm.retirement.6 — person[taxpayer].retirement[r1].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $1,173.00

### classm.retirement.6 — person[taxpayer].retirement[r1].smw10 — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **AGREE**

Value: $0.00

### classm.retirement.6 — person[taxpayer].retirement[r1].smw11 — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **AGREE**

Value: $0.00

### classm.retirement.6 — person[taxpayer].retirement[r2].smw1 — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **AGREE**

Value: $28,849.00

### classm.retirement.6 — person[taxpayer].retirement[r2].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $0.00

### classm.retirement.6 — person[taxpayer].retirement[r2].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last
Status: **AGREE**

Value: $0.00

### classm.retirement.6 — person[taxpayer].retirement[r2].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $0.00

### classm.retirement.6 — person[taxpayer].retirement[r2].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $0.00

### classm.retirement.6 — person[taxpayer].retirement[r2].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $0.00

### classm.retirement.6 — person[taxpayer].retirement[r2].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $0.00

### classm.retirement.6 — person[taxpayer].retirement[r2].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $28,849.00

### classm.retirement.6 — person[taxpayer].retirement[r2].smw10 — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **AGREE**

Value: $0.00

### classm.retirement.6 — person[taxpayer].retirement[r2].smw11 — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **AGREE**

Value: $0.00

## Raw responses

### classm.retirement.1

```yaml
lines:
  - printed: "person[taxpayer].retirement[r1].smw1"
    value: "0.00"
    work: "Box 1 gross distribution = $0.00"
  - printed: "person[taxpayer].retirement[r1].smw2"
    value: "6276.00"
    work: "Cost in plan at annuity starting date = $6,276.00"
  - printed: "person[taxpayer].retirement[r1].smw4"
    value: "892.00"
    work: "Completed worksheet last year; use last year's line 4 = $892.00"
  - printed: "person[taxpayer].retirement[r1].smw5"
    value: "10704.00"
    work: "$892.00 x 12 months = $10,704.00"
  - printed: "person[taxpayer].retirement[r1].smw6"
    value: "4043.00"
    work: "Last year's line 10 recovered tax free = $4,043.00"
  - printed: "person[taxpayer].retirement[r1].smw7"
    value: "2233.00"
    work: "$6,276.00 - $4,043.00 = $2,233.00"
  - printed: "person[taxpayer].retirement[r1].smw8"
    value: "2233.00"
    work: "Smaller of $10,704.00 or $2,233.00 = $2,233.00"
  - printed: "person[taxpayer].retirement[r1].smw9"
    value: "0.00"
    work: "$0.00 - $2,233.00 = -$2,233.00; not less than zero = $0.00"
  - printed: "person[taxpayer].retirement[r1].smw10"
    value: "6276.00"
    work: "$4,043.00 + $2,233.00 = $6,276.00"
  - printed: "person[taxpayer].retirement[r1].smw11"
    value: "0.00"
    work: "$6,276.00 - $6,276.00 = $0.00"
  - printed: "person[taxpayer].retirement[r2].smw1"
    value: "28224.00"
    work: "Box 1 gross distribution = $28,224.00"
  - printed: "person[taxpayer].retirement[r2].smw2"
    value: "0.00"
    work: "Cost in plan at annuity starting date = $0.00"
  - printed: "person[taxpayer].retirement[r2].smw4"
    value: "0.00"
    work: "$0.00 / 310 (Table 1 age 56-60, post-11/18/1996) = $0.00"
  - printed: "person[taxpayer].retirement[r2].smw5"
    value: "0.00"
    work: "$0.00 x 12 months = $0.00"
  - printed: "person[taxpayer].retirement[r2].smw6"
    value: "0.00"
    work: "Recovered tax free in years after 1986 = $0.00"
  - printed: "person[taxpayer].retirement[r2].smw7"
    value: "0.00"
    work: "$0.00 - $0.00 = $0.00"
  - printed: "person[taxpayer].retirement[r2].smw8"
    value: "0.00"
    work: "Smaller of $0.00 or $0.00 = $0.00"
  - printed: "person[taxpayer].retirement[r2].smw9"
    value: "28224.00"
    work: "$28,224.00 - $0.00 = $28,224.00"
  - printed: "person[taxpayer].retirement[r2].smw10"
    value: "0.00"
    work: "$0.00 + $0.00 = $0.00"
  - printed: "person[taxpayer].retirement[r2].smw11"
    value: "0.00"
    work: "$0.00 - $0.00 = $0.00"
```

### classm.retirement.2

```yaml
lines:
  - printed: "person[taxpayer].retirement[r1].smw1"
    value: "0.00"
    work: "Form 1099-R box 1 gross distribution is $0.00."
  - printed: "person[taxpayer].retirement[r1].smw2"
    value: "0.00"
    work: "Cost in plan at annuity starting date is $0.00."
  - printed: "person[taxpayer].retirement[r1].smw4"
    value: "0.00"
    work: "No prior-year worksheet; age 57 Table 1 factor 310; 0.00 / 310 = 0.00."
  - printed: "person[taxpayer].retirement[r1].smw5"
    value: "0.00"
    work: "0.00 x 12 months = 0.00."
  - printed: "person[taxpayer].retirement[r1].smw6"
    value: "0.00"
    work: "Amount recovered tax free in years after 1986 is $0.00."
  - printed: "person[taxpayer].retirement[r1].smw7"
    value: "0.00"
    work: "Line 2 0.00 - line 6 0.00 = 0.00."
  - printed: "person[taxpayer].retirement[r1].smw8"
    value: "0.00"
    work: "Smaller of line 5 0.00 or line 7 0.00 = 0.00."
  - printed: "person[taxpayer].retirement[r1].smw9"
    value: "0.00"
    work: "Line 1 0.00 - line 8 0.00 = 0.00, not less than zero."
  - printed: "person[taxpayer].retirement[r1].smw10"
    value: "0.00"
    work: "Line 6 0.00 + line 8 0.00 = 0.00."
  - printed: "person[taxpayer].retirement[r1].smw11"
    value: "0.00"
    work: "Line 2 0.00 - line 10 0.00 = 0.00."
  - printed: "person[taxpayer].retirement[r2].smw1"
    value: "36791.00"
    work: "Form 1099-R box 1 gross distribution is $36,791.00."
  - printed: "person[taxpayer].retirement[r2].smw2"
    value: "0.00"
    work: "Cost in plan at annuity starting date is $0.00."
  - printed: "person[taxpayer].retirement[r2].smw4"
    value: "0.00"
    work: "Completed last year; use last year's line 4 of $0.00."
  - printed: "person[taxpayer].retirement[r2].smw5"
    value: "0.00"
    work: "0.00 x 12 months = 0.00."
  - printed: "person[taxpayer].retirement[r2].smw6"
    value: "0.00"
    work: "Prior-year line 10 amount recovered tax free is $0.00."
  - printed: "person[taxpayer].retirement[r2].smw7"
    value: "0.00"
    work: "Line 2 0.00 - line 6 0.00 = 0.00."
  - printed: "person[taxpayer].retirement[r2].smw8"
    value: "0.00"
    work: "Smaller of line 5 0.00 or line 7 0.00 = 0.00."
  - printed: "person[taxpayer].retirement[r2].smw9"
    value: "36791.00"
    work: "Line 1 36,791.00 - line 8 0.00 = 36,791.00."
  - printed: "person[taxpayer].retirement[r2].smw10"
    value: "0.00"
    work: "Line 6 0.00 + line 8 0.00 = 0.00."
  - printed: "person[taxpayer].retirement[r2].smw11"
    value: "0.00"
    work: "Line 2 0.00 - line 10 0.00 = 0.00."
```

### classm.retirement.3

```yaml
lines:
  - printed: "person[taxpayer].retirement[r1].smw1"
    value: "11843.00"
    work: "Form 1099-R box 1 = $11,843.00"
  - printed: "person[taxpayer].retirement[r1].smw2"
    value: "0.00"
    work: "Cost in plan at annuity starting date = $0.00"
  - printed: "person[taxpayer].retirement[r1].smw4"
    value: "0.00"
    work: "Completed last year; line 4 = last year's line 4 = $0.00"
  - printed: "person[taxpayer].retirement[r1].smw5"
    value: "0.00"
    work: "$0.00 x 12 months = $0.00"
  - printed: "person[taxpayer].retirement[r1].smw6"
    value: "0.00"
    work: "Amount recovered tax free in years after 1986 = $0.00"
  - printed: "person[taxpayer].retirement[r1].smw7"
    value: "0.00"
    work: "$0.00 - $0.00 = $0.00"
  - printed: "person[taxpayer].retirement[r1].smw8"
    value: "0.00"
    work: "Smaller of line 5 ($0.00) or line 7 ($0.00) = $0.00"
  - printed: "person[taxpayer].retirement[r1].smw9"
    value: "11843.00"
    work: "$11,843.00 - $0.00 = $11,843.00"
  - printed: "person[taxpayer].retirement[r1].smw10"
    value: "0.00"
    work: "$0.00 + $0.00 = $0.00"
  - printed: "person[taxpayer].retirement[r1].smw11"
    value: "0.00"
    work: "$0.00 - $0.00 = $0.00"
```

### classm.retirement.4

```yaml
lines:
  - printed: "person[taxpayer].retirement[r1].smw1"
    value: "10905.00"
    work: "Form 1099-R box 1"
  - printed: "person[taxpayer].retirement[r1].smw2"
    value: "0.00"
    work: "Given cost in plan at annuity starting date"
  - printed: "person[taxpayer].retirement[r1].smw4"
    value: "0.00"
    work: "Completed worksheet last year; use last year's line 4 = 0"
  - printed: "person[taxpayer].retirement[r1].smw5"
    value: "0.00"
    work: "Line 4 0 x 12 months = 0"
  - printed: "person[taxpayer].retirement[r1].smw6"
    value: "0.00"
    work: "Last year's line 10 = 0"
  - printed: "person[taxpayer].retirement[r1].smw7"
    value: "0.00"
    work: "Line 2 0 - line 6 0 = 0"
  - printed: "person[taxpayer].retirement[r1].smw8"
    value: "0.00"
    work: "Smaller of line 5 0 or line 7 0 = 0"
  - printed: "person[taxpayer].retirement[r1].smw9"
    value: "10905.00"
    work: "Line 1 10905 - line 8 0 = 10905"
  - printed: "person[taxpayer].retirement[r1].smw10"
    value: "0.00"
    work: "Line 6 0 + line 8 0 = 0"
  - printed: "person[taxpayer].retirement[r1].smw11"
    value: "0.00"
    work: "Line 2 0 - line 10 0 = 0"
  - printed: "person[taxpayer].retirement[r2].smw1"
    value: "37628.00"
    work: "Form 1099-R box 1"
  - printed: "person[taxpayer].retirement[r2].smw2"
    value: "0.00"
    work: "Given cost in plan at annuity starting date"
  - printed: "person[taxpayer].retirement[r2].smw4"
    value: "0.00"
    work: "Completed worksheet last year; use last year's line 4 = 0"
  - printed: "person[taxpayer].retirement[r2].smw5"
    value: "0.00"
    work: "Line 4 0 x 12 months = 0"
  - printed: "person[taxpayer].retirement[r2].smw6"
    value: "0.00"
    work: "Last year's line 10 = 0"
  - printed: "person[taxpayer].retirement[r2].smw7"
    value: "0.00"
    work: "Line 2 0 - line 6 0 = 0"
  - printed: "person[taxpayer].retirement[r2].smw8"
    value: "0.00"
    work: "Smaller of line 5 0 or line 7 0 = 0"
  - printed: "person[taxpayer].retirement[r2].smw9"
    value: "37628.00"
    work: "Line 1 37628 - line 8 0 = 37628"
  - printed: "person[taxpayer].retirement[r2].smw10"
    value: "0.00"
    work: "Line 6 0 + line 8 0 = 0"
  - printed: "person[taxpayer].retirement[r2].smw11"
    value: "0.00"
    work: "Line 2 0 - line 10 0 = 0"
```

### classm.retirement.5

```yaml
lines:
  - printed: "person[taxpayer].retirement[r1].smw1"
    value: "0.00"
    work: "Form 1099-R box 1 is $0.00."
  - printed: "person[taxpayer].retirement[r1].smw2"
    value: "0.00"
    work: "Cost in plan at annuity starting date is $0.00."
  - printed: "person[taxpayer].retirement[r1].smw4"
    value: "0.00"
    work: "Line 2 $0.00 ÷ Table 2 number 210 = $0.00."
  - printed: "person[taxpayer].retirement[r1].smw5"
    value: "0.00"
    work: "Line 4 $0.00 × 12 months = $0.00."
  - printed: "person[taxpayer].retirement[r1].smw6"
    value: "0.00"
    work: "Amount recovered tax free in years after 1986 is $0.00."
  - printed: "person[taxpayer].retirement[r1].smw7"
    value: "0.00"
    work: "Line 2 $0.00 − line 6 $0.00 = $0.00."
  - printed: "person[taxpayer].retirement[r1].smw8"
    value: "0.00"
    work: "Smaller of line 5 $0.00 or line 7 $0.00 = $0.00."
  - printed: "person[taxpayer].retirement[r1].smw9"
    value: "0.00"
    work: "Line 1 $0.00 − line 8 $0.00 = $0.00; not less than zero."
  - printed: "person[taxpayer].retirement[r1].smw10"
    value: "0.00"
    work: "Line 6 $0.00 + line 8 $0.00 = $0.00."
  - printed: "person[taxpayer].retirement[r1].smw11"
    value: "0.00"
    work: "Line 2 $0.00 − line 10 $0.00 = $0.00."
```

### classm.retirement.6

```yaml
lines:
  - printed: "person[taxpayer].retirement[r1].smw1"
    value: "1173.00"
    work: "Form 1099-R box 1 total pension/annuity payments = 1,173.00"
  - printed: "person[taxpayer].retirement[r1].smw2"
    value: "0.00"
    work: "Cost in plan at annuity starting date = 0.00"
  - printed: "person[taxpayer].retirement[r1].smw4"
    value: "0.00"
    work: "Completed last year, so use prior-year line 4 = 0.00"
  - printed: "person[taxpayer].retirement[r1].smw5"
    value: "0.00"
    work: "0.00 × 12 months = 0.00"
  - printed: "person[taxpayer].retirement[r1].smw6"
    value: "0.00"
    work: "Recovered tax free in years after 1986 = 0.00"
  - printed: "person[taxpayer].retirement[r1].smw7"
    value: "0.00"
    work: "Line 2 0.00 − line 6 0.00 = 0.00"
  - printed: "person[taxpayer].retirement[r1].smw8"
    value: "0.00"
    work: "Smaller of line 5 0.00 or line 7 0.00 = 0.00"
  - printed: "person[taxpayer].retirement[r1].smw9"
    value: "1173.00"
    work: "Line 1 1,173.00 − line 8 0.00 = 1,173.00, not less than zero"
  - printed: "person[taxpayer].retirement[r1].smw10"
    value: "0.00"
    work: "Line 6 0.00 + line 8 0.00 = 0.00"
  - printed: "person[taxpayer].retirement[r1].smw11"
    value: "0.00"
    work: "Line 2 0.00 − line 10 0.00 = 0.00"
  - printed: "person[taxpayer].retirement[r2].smw1"
    value: "28849.00"
    work: "Form 1099-R box 1 total pension/annuity payments = 28,849.00"
  - printed: "person[taxpayer].retirement[r2].smw2"
    value: "0.00"
    work: "Cost in plan at annuity starting date = 0.00"
  - printed: "person[taxpayer].retirement[r2].smw4"
    value: "0.00"
    work: "Completed last year, so use prior-year line 4 = 0.00"
  - printed: "person[taxpayer].retirement[r2].smw5"
    value: "0.00"
    work: "0.00 × 12 months = 0.00"
  - printed: "person[taxpayer].retirement[r2].smw6"
    value: "0.00"
    work: "Recovered tax free in years after 1986 = 0.00"
  - printed: "person[taxpayer].retirement[r2].smw7"
    value: "0.00"
    work: "Line 2 0.00 − line 6 0.00 = 0.00"
  - printed: "person[taxpayer].retirement[r2].smw8"
    value: "0.00"
    work: "Smaller of line 5 0.00 or line 7 0.00 = 0.00"
  - printed: "person[taxpayer].retirement[r2].smw9"
    value: "28849.00"
    work: "Line 1 28,849.00 − line 8 0.00 = 28,849.00, not less than zero"
  - printed: "person[taxpayer].retirement[r2].smw10"
    value: "0.00"
    work: "Line 6 0.00 + line 8 0.00 = 0.00"
  - printed: "person[taxpayer].retirement[r2].smw11"
    value: "0.00"
    work: "Line 2 0.00 − line 10 0.00 = 0.00"
```
