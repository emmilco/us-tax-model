# Review record ff9b06acdd6a — transcription s1

One pass of a review, stored once (tools/transcription/review_store.py); the form's index says which lines it still judges.

```json
{
 "family": "claude",
 "form": "s1",
 "kind": "transcription",
 "policies": {
  "comparison policy": "checked-expression-types-v2",
  "input context policy": "required-review-interfaces-v2",
  "prompt policy": "source-only-computation-v3+lines-v3",
  "type validation policy": "project-expression-types-v3"
 },
 "prompt_sha256": "ba12f0138895c09b584a5d1c04c6cb50c14ba74a690c9fafdcea6bae7fc2ff1a",
 "response_sha256": "c547f720031adb4461315a1287bd0f48b79a11dce7574a7303a97fb553403c4c",
 "scope": [
  "9"
 ],
 "subjects": {
  "9": "459883f981a0746432add8ea69b959e17c4c0999ecbd7a02871b7fc2df51cffa"
 }
}
```

<!-- part block -->
#### Pass ba12f0138895

| field | value |
| --- | --- |
| date | 2026-11-24 |
| review scope | lines 9 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | ba12f0138895c09b584a5d1c04c6cb50c14ba74a690c9fafdcea6bae7fc2ff1a |
| prompt policy | source-only-computation-v3+lines-v3 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 4b739cf0f83a3c44e3c4e0ea06a9b8a0288f75985c00f5ffca93dc9691efcc1b |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | c600021112ed903c10129bd4000e38beb4c23d75bd498fc037b1041c940a4a6f |
| receipt | .transcription/s1.lines-19581e27de7c |
| printed lines compared | 1 |
| agree / disagree / missing | 0 / 1 / 0 |
| extra printed lines in second | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040s1 | 2025; created 2025-07-25 | 1, 2 | whole document | 30004f72691a7078d8720e432e83110aa2bc3852ce9b45867becdb8c28222956 | - | 2293cadd525c2df84256455db693bbd46b710c62d28a98d503b1a6f8d8aea444 |
| i1040gi | 2025; printed date 2026-02-25 | 91, 92 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 91, 92 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| p525 | 2025 | 4, 33 | cited pages | 7df495537860edb313c70301e591c2a0775567fab771e3d5f9bbb0cbccb69182 | 4, 33 | 27f9e8c0836aae6360658725d1b0db69ecaf91bfa77998e1637b51f92b18df65 |
| rr-2025-4 | Rev. Rul. 2025-4 (IRB 2025-7); not year-specific; effective for payments made on or after January 1, 2025, with 2025 a transition period for reporting | 27, 32 | pages named by another document's citation | a684c9ce673a677027737d3c1c78e24dddb1556fff2ca5bf6dd6dc812f427729 | - | 4233122a946ea3d6cd361f346161d519a2b38d24c27217f96555d2df37a5d4e8 |

##### Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form, inputs and named lines: clcw.prior_11, clcw.prior_14, clcw.prior_sd15, clcw.prior_sd21, clcw.prior_sd7, clcw.spouse_screen | clcw |
| named form, inputs and named lines: clcw_next_year.final_return | clcw_next_year |
| named form, inputs and named lines: f1040.digital_assets, f1040.estimated_any, f1040.line16, f1040.line1a, f1040.line1d, f1040.line1h, f1040.line25b, f1040.line25c, f1040.line25c_other, f1040.line26, f1040.line35a, f1040.line36, f1040.line3a, f1040.status, f1040.tax_exempt_any, f1040.tax_exempt_interest, f1040.withheld_other_any | f1040 |
| named form, inputs and named lines: household.community_property, household.considered_unmarried, household.cp_married, household.cp_retirement, household.credit_disallowed, household.ever_married, household.home_cost, household.married_dec31, household.mfs_living, household.no, household.qss_eligible, household.rdp, household.spouse_cp_domicile, household.spouse_died_this_year | household |
| named form, inputs and named lines: refund.any, refund.box8, refund.exc_tax, refund.exc_who, refund.itemized, refund.line17_prior_year, refund.line5d_prior_year, refund.line5e_prior_year, refund.mfs_spouse_itemized, refund.other_year, refund.paid_other_time, refund.received, refund.sales, refund.spouse_blind, refund.spouse_born, refund.status, refund.two_itemized, refund.two_returns, refund.you_blind, refund.you_born | refund |
| named form, inputs and named lines: s2.amt_boat, s2.amt_business, s2.amt_pab, s2.credit_recapture, s2.household_employee, s2.household_help, s2.hsa_testing, s2.iso, s2.iso_vested, s2.lookback, s2.mortgage_subsidy, s2.options_any, s2.other_tax, s2.w2_marks | s2 |
| named form, inputs and named lines: sche.accrual, sche.grouped, sche.qbi_business, sche.re_pro | sche |
| named form, inputs and named lines: sd.business_property, sd.carryover, sd.casualty, sd.condemned, sd.distributions, sd.f2439, sd.home_sale, sd.installment, sd.like_kind, sd.qof, sd.route_each, sd.sec1256, sd.small_business_stock, sd.sold_other, sd.special_any, sd.trader_election | sd |
| named line | eic, f1116, f4952, ftc, k1p, k1s, qdcg, s3, s8812 |
| named lines: f8889.line16 | f8889 |
| shared page | oi8z, person, rec, sa, scope |

##### Raw second transcription

```yaml
```yaml
lines:
  - id: s1.h_line9_additions
    printed: "(helper)"
    label: "Lines 8a, 8b, 8c, 8e, 8f, 8g, 8h, 8i, 8j, 8k, 8r, 8v and 8z added (line 8a entered as a negative number)"
    type: Dollars
    expr:
      op: sum
      of:
        - s1.line8a
        - s1.line8b
        - s1.line8c
        - s1.line8e
        - s1.line8f
        - s1.line8g
        - s1.line8h
        - s1.line8i
        - s1.line8j
        - s1.line8k
        - s1.line8r
        - s1.line8v
        - s1.line8z
    note: "Instructions say line 8a is entered in the preprinted parentheses as a negative number. Its interface type is Dollars, so it is read as already negative and is added here. Lines 8d, 8l, 8m, 8n, 8o, 8p, 8q, 8t and 8u have no interface line in this slice, so they are left out of the total. Those situations are outside the tool's scope."
  - id: s1.line9
    printed: "9"
    label: "Total other income. Add lines 8a through 8z"
    type: Dollars
    expr:
      op: subtract
      from: s1.h_line9_additions
      take: s1.line8s
    note: "Line 8s is printed in parentheses and is entered as a negative number. Its interface type is NonNegDollars, so it is read as the positive amount of nontaxable Medicaid waiver payments. 'Adding' the negative entry is therefore written as subtracting s1.line8s."
```
```
<!-- part section 9 -->
9 — Total other income. Add lines 8a through 8z
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "8a"}, {"line": "8b"}, {"line": "8c"}, {"line": "8e"}, {"line": "8f"}, {"line": "8g"}, {"line": "8h"}, {"line": "8i"}, {"line": "8j"}, {"line": "8k"}, {"line": "8r"}, {"line": "8v"}, {"line": "8z"}, {"from": {"const": 0}, "op": "subtract", "take": {"line": "8s"}}], "op": "sum"}
```

Second:

```json
{"from": {"of": [{"line": "8a"}, {"line": "8b"}, {"line": "8c"}, {"line": "8e"}, {"line": "8f"}, {"line": "8g"}, {"line": "8h"}, {"line": "8i"}, {"line": "8j"}, {"line": "8k"}, {"line": "8r"}, {"line": "8v"}, {"line": "8z"}], "op": "sum"}, "op": "subtract", "take": {"line": "8s"}}
```

Second transcription's note: Line 8s is printed in parentheses and is entered as a negative number. Its interface type is NonNegDollars, so it is read as the positive amount of nontaxable Medicaid waiver payments. 'Adding' the negative entry is therefore written as subtracting s1.line8s.

Ruling: open
Reviewed in: pass ba12f0138895

<!-- end -->
