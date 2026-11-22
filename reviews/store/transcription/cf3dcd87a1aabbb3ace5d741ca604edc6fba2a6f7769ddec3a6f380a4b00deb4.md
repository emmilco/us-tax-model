# Review record cf3dcd87a1aa — transcription f8960

One pass of a review, stored once (tools/transcription/review_store.py); the form's index says which lines it still judges.

```json
{
 "family": "claude",
 "form": "f8960",
 "kind": "transcription",
 "policies": {
  "comparison policy": "checked-expression-types-v2",
  "input context policy": "required-review-interfaces-v2",
  "prompt policy": "source-only-computation-v3+lines-v3",
  "type validation policy": "project-expression-types-v3"
 },
 "prompt_sha256": "f5f7ddb78b28cd8f2323277dd25df9f41fa5b28e46f677870edfbaf63b7c0e9e",
 "response_sha256": "ce6304bd7198b4e47768c4a94b4fb4ca365c176aab1c87c6f91817d8a2307294",
 "scope": [
  "1"
 ],
 "subjects": {
  "1": "d4beae0540543cc005a990471b90b0a0eda8b862a951d89eb070149a981feacb"
 }
}
```

<!-- part block -->
#### Pass f5f7ddb78b28

| field | value |
| --- | --- |
| date | 2026-11-16 |
| review scope | lines 1 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | f5f7ddb78b28cd8f2323277dd25df9f41fa5b28e46f677870edfbaf63b7c0e9e |
| prompt policy | source-only-computation-v3+lines-v3 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 2f481a0e9f12b8780c5e925c82f49a7a9af4a8017c0529dc1f4142bcd1417c1e |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | b3b97a56827216c9d71b8b0af05ba1bf3f7234eec154f96d08b5198cd7535984 |
| receipt | .transcription/f8960.lines-6b86b273ff34 |
| printed lines compared | 1 |
| agree / disagree / missing | 1 / 0 / 0 |
| extra printed lines in second | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f8960 | 2025; created 2025-08-19 | 1 | whole document | 76d992342a282067460ae60eaf8bda63925b514b721a6e8763f1174abedb59e9 | - | 35521c3ad7dfcd341a9de35529db4ea02c74bde6b9659da0d9388cfa46f9e4cb |
| i8960 | 2025; printed date 2026-02-04 | 3, 7, 9, 13, 14, 15, 17, 18 | cited pages | fcae098ebc1ad79343de101a66765d3b3597f664dc744de3a7588be123c900a1 | 3, 7, 9, 13, 17, 18 | d6dc1f475c511790abb02d6d6cfff554a59b40c0da1c56eb2f26af4e3cb7fa51 |
| i1099div | January 2024 (continuous-use instructions) | 1, 2, 3, 4, 5 | whole document | c0f334a4f8c8032dfce868bbfad5bf4cba1d48c9f2226d42d736b69ae784bcf3 | 1, 2, 3, 4, 5 | d9599f4871f4d473ff9c582e205b5e9385bd865210e9c2af4c4aede3a33af4f3 |
| i1040gi | 2025; printed date 2026-02-25 | 90 | pages named by another document's citation | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

##### Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form, inputs and named lines: clcw.prior_11, clcw.prior_14, clcw.prior_sd15, clcw.prior_sd21, clcw.prior_sd7, clcw.spouse_screen | clcw |
| named form, inputs and named lines: clcw_next_year.final_return | clcw_next_year |
| named form, inputs and named lines: div.any, div.basis_reconciled, div.box10, div.box12, div.box13, div.box2b, div.box2c, div.box2d, div.box2e, div.box2f, div.box3, div.box9, div.other_boxes | div |
| named form, inputs and named lines: f1040.digital_assets, f1040.estimated_any, f1040.line25b, f1040.line25c_other, f1040.line26, f1040.line2b, f1040.line35a, f1040.line36, f1040.line3a, f1040.line3b, f1040.line7a, f1040.status, f1040.tax_exempt_any, f1040.tax_exempt_interest, f1040.withheld_other_any | f1040 |
| named form, inputs and named lines: f4952.alternative_allocation, f4952.carryover, f4952.has_interest, f4952.line1, f4952.line4g, f4952.line8, f4952.prior_7, f4952.unsupported | f4952 |
| named form, inputs and named lines: household.community_property, household.considered_unmarried, household.cp_married, household.credit_disallowed, household.ever_married, household.home_cost, household.married_dec31, household.mfs_living, household.no, household.qss_eligible, household.rdp, household.spouse_cp_domicile, household.spouse_died_this_year | household |
| named form, inputs and named lines: qbi.carryforward, qbi.coop_patron, qbi.dividends, qbi.prior_form, qbi.reit_loss, qbi.suspended | qbi |
| named form, inputs and named lines: sa.bond_premium, sa.charity_limited, sa.debt_instrument_loss, sa.dependent, sa.elect_itemize, sa.estate_tax_income, sa.excluded_income, sa.foreign_tax_deduct, sa.gambling_losses, sa.gift_carryover, sa.gifts, sa.home_other, sa.home_owner, sa.impairment_work, sa.line1, sa.line11, sa.line17, sa.line5a, sa.line5b, sa.line5c, sa.line5d, sa.line5e, sa.line9, sa.medical_any, sa.medical_premiums, sa.mortgage_interest, sa.mortgage_other_use, sa.mortgage_over_limit, sa.mortgage_over_limit_mfs, sa.mortgage_unreported, sa.pension_unrecovered, sa.personal_property_tax_any, sa.property_tax_leave_out, sa.property_tax_other_any, sa.sales_tax_wish, sa.spouse_extra, sa.spouse_itemizes, sa.state_tax_any, sa.state_tax_other, sa.state_tax_other_any | sa |
| named form, inputs and named lines: sche.accrual, sche.grouped, sche.qbi_business, sche.re_pro | sche |
| named form, inputs and named lines: scope.adoption_benefits, scope.archer_msa, scope.armed_forces, scope.artist_official, scope.attorney_fees, scope.business_before, scope.care_benefits_other, scope.cfc, scope.chapter11, scope.church_exempt_wages, scope.clergy, scope.contractor_pay, scope.disaster_distribution, scope.education_recapture, scope.excess_deferral, scope.f8615, scope.f8814, scope.f8978, scope.farm, scope.foreign_shares, scope.household_pay, scope.income_averaging, scope.k1, scope.medicaid_waiver, scope.military_move, scope.nol, scope.noncitizen, scope.nonresident, scope.passive, scope.pay_no_w2, scope.performer_expenses, scope.pfic, scope.recovery, scope.reforestation, scope.religious_work, scope.rent_personal, scope.rental, scope.reservist_expenses, scope.reservist_repaid, scope.se_plan_other, scope.strike_pay, scope.tips_unreported, scope.treaty, scope.unearned_2700, scope.w2_marks, scope.wages_no_form | scope |
| named form, inputs and named lines: sd.business_property, sd.carryover, sd.casualty, sd.condemned, sd.distributions, sd.f2439, sd.installment, sd.like_kind, sd.qof, sd.route_each, sd.sec1256, sd.small_business_stock, sd.sold_other, sd.trader_election | sd |
| named line | f5329, interest, k1p, k1s, rec, sb |
| shared page | refund, s1 |

##### Raw second transcription

```yaml
lines:
  - id: f8960.line1
    printed: "1"
    label: "Taxable interest (see instructions)"
    type: Dollars
    expr: {op: copy, from: f1040.line2b}
    refuses: [f8960.election_6013g]
    note: "The Line 1 instructions say to enter taxable interest from Form 1040 or 1040-SR, line 2b. Adjustments for interest earned in a non-section 1411 trade or business, and for self-charged interest, go on line 7, not here, so line 1 copies line 2b unchanged. One point was open. The instructions refer to the rules for dual-status filers and for section 6013(g)/(h) elections. If such an election is made but not applied for NIIT, each spouse figures NII separately, so this line would not be the joint line 2b. I read that as outside what this line computes and list f8960.election_6013g under refuses rather than adding an input for a separately figured interest amount."
```
<!-- part section 1 -->
1 — Taxable interest (Form 1040 line 2b)
Status: **AGREE**
Reviewed in: pass f5f7ddb78b28

<!-- part gate 1 -->
| 1 | f8960.election_6013g | f8960.election_6013g |
<!-- end -->
