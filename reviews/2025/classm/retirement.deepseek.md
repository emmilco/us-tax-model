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
| subject sha256 | 923b5f567ff0cb14238e4936411c45fc789fee82e9cb8ffb14bddd00c1642c01 |
| cases | 5 |
| worked target scope | printed IRS lines |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1099r | 2025 (calendar-year form) | 5, 7 | cited pages | 97b0b54ae7c95303418077d54e349c0106cbbd5c4b5695ef684c23c39a5fda3f | 5, 7 | af300d066f4492afc97aa90824bfc681581f64482976e6d6a705e7e94b0e4e67 |
| i1040gi | 2025; printed date 2026-02-25 | 26, 27, 28, 29, 30, 31 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 26, 27, 28, 30, 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i5329 | 2025 | 1, 3, 5 | cited pages | bc85a048e4293ab244d68023ac7bb45333ceede0763b3b1cb3430eb4829a18bf | 1, 3, 5 | e46adbf118d780a00b73957b6ef4c6e436e651f6f076a36fa9b6717bd138ee5d |
| f8880 | 2025; created 2025-11-04 | 1, 2 | whole document | e8b37e5065850674d94eecd145d787e1789924b0c2b09bf3693992c45ba9dc94 | 2 | e082ccb481b2d0e872449d7728c290669213b8d16d4c94f281c1bb70aeaed575 |

## Lines

### case classm.retirement.1 — prompt sha256 5c7f160f456bf0e3610189121bbd10bcaf52a6364adf748bdcb3b09ed1bf74d1; branches: retirement.special:false, retirement.annuity:false, retirement.annuity:true, retirement.used_last_year:false, retirement.used_last_year:true, retirement.joint_life:false, retirement.joint_life:true, retirement.is_ira:false, retirement.is_ira:true, retirement.roth:false, retirement.direct:false, retirement.bad_code:false, retirement.rolled#1, retirement.has_rollover:false, retirement.has_rollover:true, retirement.smw_shown:false, retirement.smw_shown:true, retirement.smw4_table1#1, retirement.smw4_table1#4, retirement.smw4_table2#0, retirement.smw4_table2#4, retirement.smw4_new#0, retirement.smw4_new#1, retirement.smw4#0, retirement.smw4#1, retirement.smw8:left, retirement.smw8:right, retirement.smw9:floor, retirement.smw9:positive, retirement.cost_left:false, retirement.cost_left:true, retirement.annuity_with_cost:false, retirement.annuity_with_cost:true, retirement.annuity_rollover:false, retirement.annuity_taxable#0, retirement.annuity_taxable#1, retirement.ira_taxable#1, retirement.ira_not_rolled:floor, retirement.ira_not_rolled:positive, retirement.plan_simple:floor, retirement.plan_simple:positive, retirement.plan_taxable#0, retirement.plan_taxable#1, retirement.taxable#0, retirement.taxable#1, retirement.show_a:true, retirement.amount_a#0, retirement.sav_military:false, retirement.sav_404k:false, retirement.sav_inherited:false, retirement.sav_excluded:false, retirement.sav_gross:floor, retirement.sav_gross:positive, retirement.sav_amount#1, retirement.early:false, retirement.early:true, retirement.early_screen:false, retirement.code_screen:false, retirement.screen_refused:false, retirement.has_exception:false, retirement.has_exception:true, retirement.wrong_kind:false, retirement.l1#0, retirement.l1#1, retirement.exc_capped:left, retirement.exc_capped:right, retirement.l2#0, retirement.l2#1, retirement.is_e05:false, retirement.l2_e05#1, retirement.is_e09:false, retirement.l2_e09#1, retirement.is_e19:false, retirement.l2_e19#1, retirement.is_e22:false, retirement.is_e22:true, retirement.l2_e22#0, retirement.l2_e22#1, retirement.is_e23:false, retirement.l2_e23#1, retirement.is_s:false, retirement.l1_s#1, retirement.l2_s#1

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

### case classm.retirement.2 — prompt sha256 951de37dbe484966a1a982bf0831a25da9e2b4edebc1a5bfde73e185d08621f6; branches: retirement.special:false, retirement.annuity:false, retirement.annuity:true, retirement.used_last_year:false, retirement.joint_life:false, retirement.is_ira:false, retirement.roth:false, retirement.direct:false, retirement.bad_code:false, retirement.rolled#1, retirement.has_rollover:false, retirement.smw_shown:false, retirement.smw_shown:true, retirement.smw4_table1#2, retirement.smw4_table1#4, retirement.smw4_table2#1, retirement.smw4_table2#4, retirement.smw4_new#1, retirement.smw4#1, retirement.smw8:left, retirement.smw9:positive, retirement.cost_left:false, retirement.cost_left:true, retirement.annuity_with_cost:false, retirement.annuity_with_cost:true, retirement.annuity_rollover:false, retirement.annuity_taxable#0, retirement.annuity_taxable#1, retirement.ira_taxable#1, retirement.ira_not_rolled:positive, retirement.plan_simple:positive, retirement.plan_taxable#0, retirement.plan_taxable#1, retirement.taxable#1, retirement.show_a:false, retirement.show_a:true, retirement.amount_a#0, retirement.amount_a#1, retirement.sav_military:false, retirement.sav_military:true, retirement.sav_404k:false, retirement.sav_inherited:false, retirement.sav_excluded:false, retirement.sav_excluded:true, retirement.sav_gross:positive, retirement.sav_amount#0, retirement.sav_amount#1, retirement.early:false, retirement.early_screen:false, retirement.code_screen:false, retirement.screen_refused:false, retirement.has_exception:false, retirement.wrong_kind:false, retirement.l1#1, retirement.exc_capped:left, retirement.l2#1, retirement.is_e05:false, retirement.l2_e05#1, retirement.is_e09:false, retirement.l2_e09#1, retirement.is_e19:false, retirement.l2_e19#1, retirement.is_e22:false, retirement.l2_e22#1, retirement.is_e23:false, retirement.l2_e23#1, retirement.is_s:false, retirement.l1_s#1, retirement.l2_s#1

### classm.retirement.2 — person[taxpayer].retirement[r2].smw1 — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **AGREE**

Value: $5,091.00

### classm.retirement.2 — person[taxpayer].retirement[r2].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $20,379.00

### classm.retirement.2 — person[taxpayer].retirement[r2].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last
Status: **AGREE**

Value: $78.38

### classm.retirement.2 — person[taxpayer].retirement[r2].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $940.56

### classm.retirement.2 — person[taxpayer].retirement[r2].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — person[taxpayer].retirement[r2].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $20,379.00

### classm.retirement.2 — person[taxpayer].retirement[r2].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $940.56

### classm.retirement.2 — person[taxpayer].retirement[r2].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $4,150.44

### classm.retirement.2 — person[taxpayer].retirement[r2].smw10 — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **AGREE**

Value: $940.56

### classm.retirement.2 — person[taxpayer].retirement[r2].smw11 — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **AGREE**

Value: $19,438.44

### case classm.retirement.3 — prompt sha256 e8781c6723ad672a493449a1c9f219109df967071b017da65418d144c87a8941; branches: retirement.special:false, retirement.annuity:false, retirement.annuity:true, retirement.used_last_year:false, retirement.used_last_year:true, retirement.joint_life:false, retirement.joint_life:true, retirement.is_ira:false, retirement.is_ira:true, retirement.roth:false, retirement.roth:true, retirement.direct:false, retirement.bad_code:false, retirement.rolled#1, retirement.has_rollover:false, retirement.smw_shown:false, retirement.smw_shown:true, retirement.smw4_table1#3, retirement.smw4_table1#4, retirement.smw4_table2#1, retirement.smw4_table2#3, retirement.smw4_new#0, retirement.smw4_new#1, retirement.smw4#0, retirement.smw4#1, retirement.smw8:left, retirement.smw9:positive, retirement.cost_left:false, retirement.cost_left:true, retirement.annuity_with_cost:false, retirement.annuity_with_cost:true, retirement.annuity_rollover:false, retirement.annuity_taxable#0, retirement.annuity_taxable#1, retirement.ira_taxable#0, retirement.ira_taxable#1, retirement.ira_not_rolled:positive, retirement.plan_simple:positive, retirement.plan_taxable#0, retirement.plan_taxable#1, retirement.taxable#0, retirement.taxable#1, retirement.show_a:true, retirement.amount_a#0, retirement.sav_military:false, retirement.sav_404k:false, retirement.sav_inherited:false, retirement.sav_excluded:false, retirement.sav_gross:positive, retirement.sav_amount#1, retirement.early:false, retirement.early_screen:false, retirement.code_screen:false, retirement.screen_refused:false, retirement.has_exception:false, retirement.wrong_kind:false, retirement.l1#1, retirement.exc_capped:left, retirement.l2#1, retirement.is_e05:false, retirement.l2_e05#1, retirement.is_e09:false, retirement.l2_e09#1, retirement.is_e19:false, retirement.l2_e19#1, retirement.is_e22:false, retirement.l2_e22#1, retirement.is_e23:false, retirement.l2_e23#1, retirement.is_s:false, retirement.l1_s#1, retirement.l2_s#1

### classm.retirement.3 — person[taxpayer].retirement[r1].smw1 — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **AGREE**

Value: $15,200.00

### classm.retirement.3 — person[taxpayer].retirement[r1].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $58,010.00

### classm.retirement.3 — person[taxpayer].retirement[r1].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last
Status: **AGREE**

Value: $276.24

### classm.retirement.3 — person[taxpayer].retirement[r1].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $3,314.88

### classm.retirement.3 — person[taxpayer].retirement[r1].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $18,614.00

### classm.retirement.3 — person[taxpayer].retirement[r1].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $39,396.00

### classm.retirement.3 — person[taxpayer].retirement[r1].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $3,314.88

### classm.retirement.3 — person[taxpayer].retirement[r1].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $11,885.12

### classm.retirement.3 — person[taxpayer].retirement[r1].smw10 — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **AGREE**

Value: $21,928.88

### classm.retirement.3 — person[taxpayer].retirement[r1].smw11 — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **AGREE**

Value: $36,081.12

### case classm.retirement.4 — prompt sha256 a340aa16ce2f6c701d2cbb70df321a6f3848370a425f2232e4acf4b276e1b5e6; branches: retirement.special:false, retirement.annuity:false, retirement.annuity:true, retirement.used_last_year:false, retirement.used_last_year:true, retirement.joint_life:false, retirement.is_ira:false, retirement.roth:false, retirement.direct:false, retirement.bad_code:false, retirement.rolled#1, retirement.has_rollover:false, retirement.smw_shown:false, retirement.smw_shown:true, retirement.smw4_table1#0, retirement.smw4_table1#1, retirement.smw4_table2#1, retirement.smw4_table2#2, retirement.smw4_new#1, retirement.smw4#0, retirement.smw4#1, retirement.smw8:left, retirement.smw9:positive, retirement.cost_left:false, retirement.cost_left:true, retirement.annuity_with_cost:false, retirement.annuity_with_cost:true, retirement.annuity_rollover:false, retirement.annuity_taxable#0, retirement.annuity_taxable#1, retirement.ira_taxable#1, retirement.ira_not_rolled:positive, retirement.plan_simple:positive, retirement.plan_taxable#0, retirement.plan_taxable#1, retirement.taxable#1, retirement.show_a:false, retirement.show_a:true, retirement.amount_a#0, retirement.amount_a#1, retirement.sav_military:false, retirement.sav_404k:false, retirement.sav_inherited:false, retirement.sav_excluded:false, retirement.sav_gross:positive, retirement.sav_amount#1, retirement.early:false, retirement.early_screen:false, retirement.code_screen:false, retirement.screen_refused:false, retirement.has_exception:false, retirement.wrong_kind:false, retirement.l1#1, retirement.exc_capped:left, retirement.l2#1, retirement.is_e05:false, retirement.l2_e05#1, retirement.is_e09:false, retirement.l2_e09#1, retirement.is_e19:false, retirement.l2_e19#1, retirement.is_e22:false, retirement.l2_e22#1, retirement.is_e23:false, retirement.l2_e23#1, retirement.is_s:false, retirement.l1_s#1, retirement.l2_s#1

### classm.retirement.4 — person[taxpayer].retirement[r1].smw1 — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **AGREE**

Value: $59,417.00

### classm.retirement.4 — person[taxpayer].retirement[r1].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $193,265.00

### classm.retirement.4 — person[taxpayer].retirement[r1].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last
Status: **AGREE**

Value: $623.44

### classm.retirement.4 — person[taxpayer].retirement[r1].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $7,481.28

### classm.retirement.4 — person[taxpayer].retirement[r1].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $5,744.00

### classm.retirement.4 — person[taxpayer].retirement[r1].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $187,521.00

### classm.retirement.4 — person[taxpayer].retirement[r1].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $7,481.28

### classm.retirement.4 — person[taxpayer].retirement[r1].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $51,935.72

### classm.retirement.4 — person[taxpayer].retirement[r1].smw10 — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **AGREE**

Value: $13,225.28

### classm.retirement.4 — person[taxpayer].retirement[r1].smw11 — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **AGREE**

Value: $180,039.72

### case classm.retirement.5 — prompt sha256 d34fd9249f685dc8f570bf339739d2fbdec45aad4fdca12a7f45478da03c6f12; branches: retirement.special:false, retirement.annuity:false, retirement.annuity:true, retirement.used_last_year:false, retirement.used_last_year:true, retirement.joint_life:false, retirement.joint_life:true, retirement.is_ira:false, retirement.is_ira:true, retirement.roth:false, retirement.direct:false, retirement.bad_code:false, retirement.rolled#1, retirement.has_rollover:false, retirement.smw_shown:false, retirement.smw_shown:true, retirement.smw4_table1#1, retirement.smw4_table1#4, retirement.smw4_table2#4, retirement.smw4_new#0, retirement.smw4_new#1, retirement.smw4#0, retirement.smw4#1, retirement.smw8:left, retirement.smw9:positive, retirement.cost_left:false, retirement.cost_left:true, retirement.annuity_with_cost:false, retirement.annuity_with_cost:true, retirement.annuity_rollover:false, retirement.annuity_taxable#0, retirement.annuity_taxable#1, retirement.ira_taxable#1, retirement.ira_not_rolled:positive, retirement.plan_simple:positive, retirement.plan_taxable#0, retirement.plan_taxable#1, retirement.taxable#0, retirement.taxable#1, retirement.show_a:false, retirement.show_a:true, retirement.amount_a#0, retirement.amount_a#1, retirement.sav_military:false, retirement.sav_404k:false, retirement.sav_inherited:false, retirement.sav_inherited:true, retirement.sav_excluded:false, retirement.sav_excluded:true, retirement.sav_gross:positive, retirement.sav_amount#0, retirement.sav_amount#1, retirement.early:false, retirement.early_screen:false, retirement.code_screen:false, retirement.screen_refused:false, retirement.has_exception:false, retirement.wrong_kind:false, retirement.l1#1, retirement.exc_capped:left, retirement.l2#1, retirement.is_e05:false, retirement.l2_e05#1, retirement.is_e09:false, retirement.l2_e09#1, retirement.is_e19:false, retirement.l2_e19#1, retirement.is_e22:false, retirement.l2_e22#1, retirement.is_e23:false, retirement.l2_e23#1, retirement.is_s:false, retirement.l1_s#1, retirement.l2_s#1

### classm.retirement.5 — person[taxpayer].retirement[r1].smw1 — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **AGREE**

Value: $28,870.00

### classm.retirement.5 — person[taxpayer].retirement[r1].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $40,538.00

### classm.retirement.5 — person[taxpayer].retirement[r1].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last
Status: **AGREE**

Value: $253.36

### classm.retirement.5 — person[taxpayer].retirement[r1].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $3,040.32

### classm.retirement.5 — person[taxpayer].retirement[r1].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $28,247.00

### classm.retirement.5 — person[taxpayer].retirement[r1].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $12,291.00

### classm.retirement.5 — person[taxpayer].retirement[r1].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $3,040.32

### classm.retirement.5 — person[taxpayer].retirement[r1].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $25,829.68

### classm.retirement.5 — person[taxpayer].retirement[r1].smw10 — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **AGREE**

Value: $31,287.32

### classm.retirement.5 — person[taxpayer].retirement[r1].smw11 — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **AGREE**

Value: $9,250.68

## Raw responses

### classm.retirement.1

```yaml
lines:
  - printed: "person[taxpayer].retirement[r1].smw1"
    value: "0.00"
    work: "Form 1099-R box 1 gross distribution."
  - printed: "person[taxpayer].retirement[r1].smw2"
    value: "6276.00"
    work: "Cost in plan at annuity starting date."
  - printed: "person[taxpayer].retirement[r1].smw4"
    value: "892.00"
    work: "Worksheet completed last year, so use last year's line 4."
  - printed: "person[taxpayer].retirement[r1].smw5"
    value: "10704.00"
    work: "892.00 x 12 months = 10,704.00."
  - printed: "person[taxpayer].retirement[r1].smw6"
    value: "4043.00"
    work: "Amount recovered tax free in years after 1986 from last year's line 10."
  - printed: "person[taxpayer].retirement[r1].smw7"
    value: "2233.00"
    work: "6,276.00 - 4,043.00 = 2,233.00."
  - printed: "person[taxpayer].retirement[r1].smw8"
    value: "2233.00"
    work: "Smaller of line 5 10,704.00 or line 7 2,233.00."
  - printed: "person[taxpayer].retirement[r1].smw9"
    value: "0.00"
    work: "0.00 - 2,233.00 = -2,233.00, but not less than zero."
  - printed: "person[taxpayer].retirement[r1].smw10"
    value: "6276.00"
    work: "4,043.00 + 2,233.00 = 6,276.00."
  - printed: "person[taxpayer].retirement[r1].smw11"
    value: "0.00"
    work: "6,276.00 - 6,276.00 = 0.00."
```

### classm.retirement.2

```yaml
lines:
  - printed: "person[taxpayer].retirement[r2].smw1"
    value: "5091.00"
    work: "Form 1099-R box 1 total pension payments."
  - printed: "person[taxpayer].retirement[r2].smw2"
    value: "20379.00"
    work: "Cost in plan at annuity starting date."
  - printed: "person[taxpayer].retirement[r2].smw4"
    value: "78.38"
    work: "20,379.00 / 260 (age 65, Table 1) = 78.38."
  - printed: "person[taxpayer].retirement[r2].smw5"
    value: "940.56"
    work: "78.38 x 12 months = 940.56."
  - printed: "person[taxpayer].retirement[r2].smw6"
    value: "0.00"
    work: "No amount recovered tax free in years after 1986."
  - printed: "person[taxpayer].retirement[r2].smw7"
    value: "20379.00"
    work: "20,379.00 - 0.00 = 20,379.00."
  - printed: "person[taxpayer].retirement[r2].smw8"
    value: "940.56"
    work: "Smaller of line 5 (940.56) or line 7 (20,379.00)."
  - printed: "person[taxpayer].retirement[r2].smw9"
    value: "4150.44"
    work: "5,091.00 - 940.56 = 4,150.44, not below zero."
  - printed: "person[taxpayer].retirement[r2].smw10"
    value: "940.56"
    work: "0.00 + 940.56 = 940.56."
  - printed: "person[taxpayer].retirement[r2].smw11"
    value: "19438.44"
    work: "20,379.00 - 940.56 = 19,438.44."
```

### classm.retirement.3

```yaml
lines:
  - printed: "person[taxpayer].retirement[r1].smw1"
    value: "15200.00"
    work: "Form 1099-R box 1 total pension or annuity payments = 15,200.00."
  - printed: "person[taxpayer].retirement[r1].smw2"
    value: "58010.00"
    work: "Cost in the plan at the annuity starting date = 58,010.00."
  - printed: "person[taxpayer].retirement[r1].smw4"
    value: "276.24"
    work: "58,010.00 / 210 = 276.2381..., rounded to 276.24."
  - printed: "person[taxpayer].retirement[r1].smw5"
    value: "3314.88"
    work: "276.24 x 12 months = 3,314.88."
  - printed: "person[taxpayer].retirement[r1].smw6"
    value: "18614.00"
    work: "Amount recovered tax free in years after 1986 = 18,614.00."
  - printed: "person[taxpayer].retirement[r1].smw7"
    value: "39396.00"
    work: "58,010.00 - 18,614.00 = 39,396.00."
  - printed: "person[taxpayer].retirement[r1].smw8"
    value: "3314.88"
    work: "Smaller of line 5 (3,314.88) or line 7 (39,396.00) = 3,314.88."
  - printed: "person[taxpayer].retirement[r1].smw9"
    value: "11885.12"
    work: "15,200.00 - 3,314.88 = 11,885.12, not less than zero."
  - printed: "person[taxpayer].retirement[r1].smw10"
    value: "21928.88"
    work: "18,614.00 + 3,314.88 = 21,928.88."
  - printed: "person[taxpayer].retirement[r1].smw11"
    value: "36081.12"
    work: "58,010.00 - 21,928.88 = 36,081.12."
```

### classm.retirement.4

```yaml
lines:
  - printed: "person[taxpayer].retirement[r1].smw1"
    value: "59417.00"
    work: "Form 1099-R box 1 gross distribution"
  - printed: "person[taxpayer].retirement[r1].smw2"
    value: "193265.00"
    work: "Cost in plan at annuity starting date"
  - printed: "person[taxpayer].retirement[r1].smw4"
    value: "623.44"
    work: "Age 59, after 11/18/1996: Table 1 factor 310; 193265 / 310 = 623.4355 -> 623.44"
  - printed: "person[taxpayer].retirement[r1].smw5"
    value: "7481.28"
    work: "623.44 x 12 months = 7481.28"
  - printed: "person[taxpayer].retirement[r1].smw6"
    value: "5744.00"
    work: "Amount recovered tax free in years after 1986"
  - printed: "person[taxpayer].retirement[r1].smw7"
    value: "187521.00"
    work: "193265.00 - 5744.00 = 187521.00"
  - printed: "person[taxpayer].retirement[r1].smw8"
    value: "7481.28"
    work: "Smaller of line 5 (7481.28) or line 7 (187521.00)"
  - printed: "person[taxpayer].retirement[r1].smw9"
    value: "51935.72"
    work: "59417.00 - 7481.28 = 51935.72"
  - printed: "person[taxpayer].retirement[r1].smw10"
    value: "13225.28"
    work: "5744.00 + 7481.28 = 13225.28"
  - printed: "person[taxpayer].retirement[r1].smw11"
    value: "180039.72"
    work: "193265.00 - 13225.28 = 180039.72"
```

### classm.retirement.5

```yaml
lines:
  - printed: "person[taxpayer].retirement[r1].smw1"
    value: "28870.00"
    work: "Form 1099-R box 1 total pension/annuity payments"
  - printed: "person[taxpayer].retirement[r1].smw2"
    value: "40538.00"
    work: "Cost in plan at annuity starting date"
  - printed: "person[taxpayer].retirement[r1].smw4"
    value: "253.36"
    work: "Table 1 age 72 gives 160; 40538 / 160 = 253.36"
  - printed: "person[taxpayer].retirement[r1].smw5"
    value: "3040.32"
    work: "253.36 * 12 months = 3040.32"
  - printed: "person[taxpayer].retirement[r1].smw6"
    value: "28247.00"
    work: "Amount recovered tax free in years after 1986"
  - printed: "person[taxpayer].retirement[r1].smw7"
    value: "12291.00"
    work: "40538.00 - 28247.00 = 12291.00"
  - printed: "person[taxpayer].retirement[r1].smw8"
    value: "3040.32"
    work: "smaller of 3040.32 and 12291.00 is 3040.32"
  - printed: "person[taxpayer].retirement[r1].smw9"
    value: "25829.68"
    work: "28870.00 - 3040.32 = 25829.68"
  - printed: "person[taxpayer].retirement[r1].smw10"
    value: "31287.32"
    work: "28247.00 + 3040.32 = 31287.32"
  - printed: "person[taxpayer].retirement[r1].smw11"
    value: "9250.68"
    work: "40538.00 - 31287.32 = 9250.68"
```
