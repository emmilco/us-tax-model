# Review record aaddf62deaef — transcription f1116

One pass of a review, stored once (tools/transcription/review_store.py); the form's index says which lines it still judges.

```json
{
 "family": "claude",
 "form": "f1116",
 "kind": "transcription",
 "policies": {
  "comparison policy": "checked-expression-types-v2",
  "input context policy": "required-review-interfaces-v2",
  "prompt policy": "source-only-computation-v3+lines-v3",
  "type validation policy": "project-expression-types-v3"
 },
 "prompt_sha256": "b869f9ba945dcc2030246efb14b3585c129cd895c297eb3b38ccfb8127022ecd",
 "response_sha256": "6c4ca3b59c4de78cf7b68c9eb8bc8d063e62ca8fd73672fb5a0b5591010b78a0",
 "scope": [
  "18",
  "35"
 ],
 "subjects": {
  "18": "07b7a1056818cf504ee86764fa1ac3655f76ac39132f1da5571cd4ca5dbee7f3",
  "35": "61fe46681d26bf592e746e67f7cedeb48620d42ce362679997ec6bebe6a22a54"
 }
}
```

<!-- part block -->
#### Pass b869f9ba945d

| field | value |
| --- | --- |
| date | 2026-11-22 |
| review scope | lines 18, 35 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | b869f9ba945dcc2030246efb14b3585c129cd895c297eb3b38ccfb8127022ecd |
| prompt policy | source-only-computation-v3+lines-v3 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | fail |
| required input context sha256 | d533dedbf650e8ab2042e4475c3a6096b746f532173951f540cbf3aabcc36ca8 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | ddf0e9634feb2650775052f7eba54846d4b457e0e7486431320b73dffb04821f |
| receipt | .transcription/f1116.lines-1ac38fadf0ae |
| printed lines compared | 2 |
| agree / disagree / missing | 2 / 0 / 0 |
| extra printed lines in second | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1116 | 2025; created 2025-09-16 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision) | 1, 2 | whole document | 35fb2ea431123e1b99d31ebffd382e3452d1d1c9a2ca56f5c1e658cf2d2c4e20 | - | 47a5c4ac2284a31b7c1c9d473905bf2e1d6ac3e68875543a6e19bc9224861b76 |
| i1116 | 2025; printed date 2025-12-23 | 2, 9, 11, 17, 18, 19, 20, 21, 23, 24 | cited pages | ca3e843c3bead1e7991566852707530b6bb7c2fd6008c1dbda0ac0bbd40c48ff | 2, 9, 11, 17, 19, 20, 21, 24 | 4e9025bfc8a73bcfd687c7f45cb1a037cd39e7445319bbc71c748e12db68a46a |
| p514 | 2025 (Publication 514 (2025), Catalog Number 15018A, Jan 30, 2026) | 27, 37, 39 | cited pages | db756c91fb3988617c583cbb077c6390dd7e235736f6df0ab2b2a63568f934ba | 27, 37, 39 | 8ba7d10e464cb1323987bc176a435020718ff8bc7d1b9407fdc32f24a86c6e6a |
| cfr-26-1-904-4 | 26 CFR Ch. I (4-1-25 Edition), section 1.904-4 (GovInfo, GPO) | 3, 4 | cited pages | 8e53df6404606a73b955b1d3af6a8e427db995546f51466975de1020d5557850 | 3, 4 | cb3ffa1c80dfe882de47403ff42d30e2a32a63039fe0a990cee47f4061163b26 |
| i1116sb | Rev. December 2022 (printed 'Instructions for Schedule B (Form 1116) (Rev. 12-2022)', Dec 29, 2022); current irs-pdf edition, not year-specific; the IRS had posted no 2025 edition | 1, 2, 3, 4 | whole document | 90f1313e93bf416f2ee96a62d18d70f06016968268aca1055653869475205766 | 1, 2, 3 | 4f7920df06efd2f3f67a5f5f7b3a83f7307e81fb9342cd91461ba433b47486fd |
| i1040gi | 2025; printed date 2026-02-25 | 80 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

##### Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form | interest |
| named form, inputs and named lines: clcw.prior_11, clcw.prior_14, clcw.prior_sd15, clcw.prior_sd21, clcw.prior_sd7, clcw.spouse_screen | clcw |
| named form, inputs and named lines: clcw_next_year.final_return | clcw_next_year |
| named form, inputs and named lines: div.any, div.basis_reconciled, div.box10, div.box12, div.box13, div.box2b, div.box2c, div.box2d, div.box2e, div.box2f, div.box3, div.box9, div.other_boxes | div |
| named form, inputs and named lines: f1040.digital_assets, f1040.estimated_any, f1040.gate.qdcg_applies, f1040.gate.sdtw, f1040.line11b, f1040.line14, f1040.line25b, f1040.line25c_other, f1040.line26, f1040.line2b, f1040.line35a, f1040.line36, f1040.line3a, f1040.line3b, f1040.status, f1040.tax_exempt_any, f1040.tax_exempt_interest, f1040.withheld_other_any | f1040 |
| named form, inputs and named lines: f4952.alternative_allocation, f4952.carryover, f4952.has_interest, f4952.line1, f4952.line4e, f4952.line4g, f4952.prior_7, f4952.unsupported | f4952 |
| named form, inputs and named lines: household.community_property, household.considered_unmarried, household.cp_married, household.credit_disallowed, household.ever_married, household.home_cost, household.married_dec31, household.mfs_living, household.qss_eligible, household.rdp, household.spouse_cp_domicile, household.spouse_died_this_year | household |
| named form, inputs and named lines: qbi.carryforward, qbi.coop_patron, qbi.dividends, qbi.prior_form, qbi.reit_loss, qbi.suspended | qbi |
| named form, inputs and named lines: s1.alaska_any, s1.alaska_dividend, s1.alimony, s1.alimony_any, s1.alimony_paid, s1.alimony_received, s1.alimony_unsupported, s1.cod_amount, s1.cod_any, s1.cod_bankrupt, s1.cod_business, s1.cod_gift, s1.cod_interest, s1.cod_joint_other, s1.cod_not_liable, s1.cod_price_cut, s1.cod_property, s1.cod_stockholder, s1.cod_student_home, s1.digital_amount, s1.digital_income, s1.gambling_pro, s1.gambling_winnings, s1.has_sc, s1.hobby_any, s1.hobby_income, s1.inmate_wages, s1.jury_any, s1.jury_pay, s1.jury_to_employer, s1.line21, s1.ltc_payout, s1.nol_amount, s1.nol_before_limit_date, s1.nol_ebl, s1.nol_not_married, s1.nol_was_joint, s1.nqdc_pension, s1.olympic, s1.options_amount, s1.prizes, s1.scholarship_any, s1.scholarship_taxable, s1.stock_options, s1.uc_any, s1.uc_paid, s1.uc_repaid, s1.uc_unsupported, s1.winnings_any | s1 |
| named form, inputs and named lines: s1a.carloan, s1a.line30, s1a.line37, s1a.overtime, s1a.tips | s1a |
| named form, inputs and named lines: s2.amt_boat, s2.amt_business, s2.amt_pab, s2.credit_recapture, s2.household_employee, s2.household_help, s2.hsa_testing, s2.iso, s2.iso_vested, s2.line1z, s2.lookback, s2.mortgage_subsidy, s2.options_any, s2.other_tax, s2.w2_marks | s2 |
| named form, inputs and named lines: s3.adoption, s3.adoption_any, s3.adoption_earlier, s3.adoption_final, s3.adoption_stepchild, s3.adoption_us, s3.credit_bond, s3.disability_retired, s3.elderly_credit, s3.ev, s3.ev_bought, s3.ev_credit, s3.ev_dealer, s3.ev_equipment, s3.farmland, s3.farmland_deferral, s3.foreign_any, s3.kerosene, s3.kerosene_credit, s3.line1, s3.line10, s3.mcc, s3.prior_amt, s3.prior_amt_deferral, s3.prior_forms, s3.prior_other_forms, s3.repaid_income, s3.section960c, s3.section965, s3.virgin_islands | s3 |
| named form, inputs and named lines: sa.bond_premium, sa.charity_limited, sa.debt_instrument_loss, sa.dependent, sa.elect_itemize, sa.estate_tax_income, sa.excluded_income, sa.foreign_tax_deduct, sa.gambling_losses, sa.gift_carryover, sa.gifts, sa.home_other, sa.home_owner, sa.impairment_work, sa.itemizes, sa.line1, sa.line11, sa.line5a, sa.line5a_total, sa.line5b, sa.line5c, sa.line5e, sa.line8e, sa.line9, sa.medical_any, sa.medical_premiums, sa.mortgage_interest, sa.mortgage_other_use, sa.mortgage_over_limit, sa.mortgage_over_limit_mfs, sa.mortgage_unreported, sa.pension_unrecovered, sa.personal_property_tax_any, sa.property_tax_leave_out, sa.property_tax_other_any, sa.sales_tax_wish, sa.spouse_extra, sa.spouse_itemizes, sa.state_tax_any, sa.state_tax_other, sa.state_tax_other_any | sa |
| named form, inputs and named lines: sb.account_any, sb.asset_any, sb.bond_special, sb.bonds_any, sb.company_any, sb.fbar_required, sb.form5471, sb.form8938, sb.line3, sb.line4, sb.line6, sb.line7a, sb.line8, sb.nominee, sb.ordinary_dividends, sb.territory_any, sb.trust_any | sb |
| named form, inputs and named lines: scope.adoption_benefits, scope.archer_msa, scope.armed_forces, scope.artist_official, scope.attorney_fees, scope.business_before, scope.care_benefits_other, scope.cfc, scope.chapter11, scope.church_exempt_wages, scope.clergy, scope.contractor_pay, scope.disaster_distribution, scope.education_recapture, scope.excess_deferral, scope.f8615, scope.f8814, scope.f8978, scope.farm, scope.foreign_shares, scope.household_pay, scope.income_averaging, scope.k1, scope.medicaid_waiver, scope.military_move, scope.nol, scope.noncitizen, scope.nonresident, scope.passive, scope.pay_no_w2, scope.performer_expenses, scope.pfic, scope.recovery, scope.reforestation, scope.religious_work, scope.rent_personal, scope.rental, scope.reservist_expenses, scope.reservist_repaid, scope.se_plan_other, scope.strike_pay, scope.tips_unreported, scope.treaty, scope.unearned_2700, scope.w2_marks, scope.wages_no_form | scope |
| named form, inputs and named lines: sd.business_property, sd.carryover, sd.casualty, sd.condemned, sd.distributions, sd.f2439, sd.installment, sd.like_kind, sd.line22, sd.qof, sd.route_each, sd.sec1256, sd.small_business_stock, sd.sold_other, sd.trader_election | sd |
| named form, inputs and named lines: sdtw.line18, sdtw.line22, sdtw.line27, sdtw.line30, sdtw.line36, sdtw.line40, sdtw.line43, sdtw.line45, sdtw.line46 | sdtw |
| named line | refund |
| shared page | f1116col, f1116sb, f1116sbyr, ftc |
| worksheet | qdcg |

##### Raw second transcription

```yaml
```yaml
lines:
  - id: f1116.h_ti_base
    printed: "(helper)"
    label: "Form 1040, 1040-SR, or 1040-NR, line 11b, minus Form 1040, 1040-SR, or 1040-NR, line 14"
    type: Dollars
    expr: {op: subtract, from: f1040.line11b, take: f1040.line14}

  - id: f1116.h_l18_sum
    printed: "(helper)"
    label: "The sum of (i) line 11b minus line 14 and (ii) Schedule 1-A (Form 1040), line 37"
    type: Dollars
    expr: {op: sum, of: [f1116.h_ti_base, s1a.line37]}

  - id: f1116.h_line17_positive
    printed: "(helper)"
    label: "Line 17 is more than zero (if the result is zero or less, skip line 18 and enter -0- on line 19)"
    type: Bool
    expr: {op: test, gt: [f1116.line17, {const: 0}]}

  - id: f1116.h_qdcg_ws_needed
    printed: "(helper)"
    label: "You completed the Qualified Dividends and Capital Gain Tax Worksheet, line 5 of it is greater than zero, and line 23 of it is less than line 24"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [f1040.gate.qdcg_applies, {const: true}]}
        - {op: test, gt: [qdcg.line5, {const: 0}]}
        - {op: test, lt: [qdcg.line23, qdcg.line24]}

  - id: f1116.h_sdtw_ws_needed
    printed: "(helper)"
    label: "You figured your tax using the Schedule D Tax Worksheet, line 18 of it is greater than zero, and line 45 of it is less than line 46"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [f1040.gate.sdtw, {const: true}]}
        - {op: test, gt: [sdtw.line18, {const: 0}]}
        - {op: test, lt: [sdtw.line45, sdtw.line46]}

  - id: f1116.h_exc_ceiling
    printed: "(helper)"
    label: "Adjustment exception ceiling: $394,600 if married filing jointly or qualifying surviving spouse; $197,300 if married filing separately, single, or head of household"
    type: NonNegDollars
    expr: {op: param, ref: f1116.exception_ceiling}

  - id: f1116.h_exc_qd_limit
    printed: "(helper)"
    label: "Adjustment exception limit on foreign source qualified dividends plus foreign source net capital gain ($20,000)"
    type: NonNegDollars
    expr: {op: param, ref: f1116.exception_qd_limit}

  - id: f1116.h_foreign_div
    printed: "(helper)"
    label: "Foreign source dividends reported in the columns of this Form 1116 (an upper bound on foreign source qualified dividends)"
    type: NonNegDollars
    expr: {op: sum_over, collection: f1116col, field: f1116col.div_income_if_div}
    note: "The adjustment exception tests foreign source qualified dividends, which no supplied line gives. The total foreign dividends of the columns is used as an upper bound: when it is under $20,000, the qualified part is too. When it is not, the exception is treated as not shown and line 18 refuses. Foreign capital gains are refused through f1116.foreign_gain, so foreign net capital gain is zero here."

  - id: f1116.h_exc_income
    printed: "(helper)"
    label: "Line 5 of the Qualified Dividends and Capital Gain Tax Worksheet (or line 18 of the Schedule D Tax Worksheet) doesn't exceed the adjustment exception amount for your filing status"
    type: Bool
    expr:
      op: test
      any:
        - op: test
          all:
            - {op: test, eq: [f1040.gate.qdcg_applies, {const: true}]}
            - {op: test, le: [qdcg.line5, f1116.h_exc_ceiling]}
        - op: test
          all:
            - {op: test, eq: [f1040.gate.sdtw, {const: true}]}
            - {op: test, le: [sdtw.line18, f1116.h_exc_ceiling]}

  - id: f1116.h_exc_div
    printed: "(helper)"
    label: "The amount of your foreign source net capital gain plus your foreign source qualified dividends is less than $20,000"
    type: Bool
    expr: {op: test, lt: [f1116.h_foreign_div, f1116.h_exc_qd_limit]}

  - id: f1116.h_l18_ws_unsupported
    printed: "(helper)"
    label: "You must use the Worksheet for Line 18 (worldwide qualified dividends and capital gains) and you don't qualify for the adjustment exception"
    type: Bool
    expr:
      op: test
      all:
        - op: test
          any:
            - {op: test, eq: [f1116.h_qdcg_ws_needed, {const: true}]}
            - {op: test, eq: [f1116.h_sdtw_ws_needed, {const: true}]}
        - op: test
          not:
            op: test
            all:
              - {op: test, eq: [f1116.h_exc_income, {const: true}]}
              - {op: test, eq: [f1116.h_exc_div, {const: true}]}
    note: "The Worksheet for Line 18 multiplies worksheet amounts by 0.4595 and 0.5946. No year parameter supplies these rates, so the worksheet is not computed, and line 18 refuses when the worksheet is required. When the exception is met, the instructions say the election must be made if line 1a was left unadjusted. This reading assumes line 1a (reviewed separately) is left unadjusted in that case, so line 18 is taxable income."

  - id: f1116.line18
    printed: "18"
    label: "Individuals: Enter the sum of (i) Form 1040, 1040-SR, or 1040-NR, line 11b, minus Form 1040, 1040-SR, or 1040-NR, line 14, and (ii) Schedule 1-A (Form 1040), line 37. Estates and trusts: Enter your taxable income without the deduction for your exemption. (All filers: If the result is zero or less, enter -0- on line 18.)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: f1116.h_l18_sum, take: {const: 0}}
    refuses: [f1116.foreign_gain, f1116.h_l18_ws_unsupported]
    shown_when: f1116.h_line17_positive
    note: "Line 17 says to skip line 18 when line 17 is zero or less, so the line is shown only when line 17 is positive. Only the individual case is encoded. The worksheet case (qualified dividends or capital gains adjustments without the adjustment exception) is refused, not computed."

  - id: f1116.line35
    printed: "35"
    label: "Subtract line 34 from line 33. This is your foreign tax credit. Enter here and on Schedule 3 (Form 1040), line 1; Form 1041, Schedule G, line 2a; or Form 990-T, Part III, line 1a"
    type: Dollars
    expr: {op: subtract, from: f1116.line33, take: f1116.line34}
```
```
<!-- part section 18 -->
18 — Individuals, the sum of (i) Form 1040 line 11b minus line 14 and (ii) Schedule 1-A line 37
Status: **AGREE**
Reviewed in: pass b869f9ba945d

<!-- part section 35 -->
35 — Subtract line 34 from line 33. This is your foreign tax credit
Status: **AGREE**
Reviewed in: pass b869f9ba945d

<!-- part gate 18 -->
| 18 | f1116.foreign_gain, f1116.h_l18_ws_unsupported | f1116.foreign_gain, f1116.h_l18_ws_unsupported |
<!-- end -->
