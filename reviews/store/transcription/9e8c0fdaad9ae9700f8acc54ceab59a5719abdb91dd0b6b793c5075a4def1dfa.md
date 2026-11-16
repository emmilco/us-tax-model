# Review record 9e8c0fdaad9a — transcription household

One pass of a review, stored once (tools/transcription/review_store.py); the form's index says which lines it still judges.

```json
{
 "family": "claude",
 "form": "household",
 "kind": "transcription",
 "policies": {
  "comparison policy": "checked-expression-types-v2",
  "input context policy": "required-review-interfaces-v2",
  "prompt policy": "source-only-computation-v3+lines-v3",
  "type validation policy": "project-expression-types-v3"
 },
 "prompt_sha256": "b0a9e2ada8710f7099f22921ec01f55da736c3cb0fece113f179a17e0bbdf442",
 "response_sha256": "3b2ee8513b016220aa0ae777a4bfbe932387595201360f47218f0c3c2cffd09b",
 "scope": [
  "household.filing_status_conflict",
  "household.mfs",
  "household.mfs_apart_all_year",
  "household.mfs_apart_last6",
  "household.mfs_community_property"
 ],
 "subjects": {
  "household.filing_status_conflict": "c20f956d22dccd614e1d5ac766e3267b84b02b72154f1fe9624ea9469c34c315",
  "household.mfs": "176699ddce9a83f1c9416ba78656a2b56ac77d598593dc578bb1ded5ce97b640",
  "household.mfs_apart_all_year": "da52f9a1821e39b91e804f3aa457836970061d10c66846a048b8e0000e687b3c",
  "household.mfs_apart_last6": "a5dddebeca49eee99f2000ef1909058390d0ddd5a00d6ad3ba35c13571c86a95",
  "household.mfs_community_property": "0f1c67a4ce5098eff5c11bcc60478ea07274f28266b249b77afc59af38b2cf40"
 }
}
```

<!-- part block -->
#### Pass b0a9e2ada871

| field | value |
| --- | --- |
| date | 2026-11-15 |
| review scope | lines household.filing_status_conflict, household.mfs, household.mfs_apart_all_year, household.mfs_apart_last6, household.mfs_community_property |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | b0a9e2ada8710f7099f22921ec01f55da736c3cb0fece113f179a17e0bbdf442 |
| prompt policy | source-only-computation-v3+lines-v3 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | d89ed7dc5c7f44d14b51607cb28e91c3ed9e4bf162d003775273e20c08a7447d |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 6315fc0ef176ca9697ff774da90ac32e32342375daa1699e8aeb8c7874e54dfc |
| receipt | .transcription/household.lines-ce94e78ba6d9 |
| printed lines compared | 5 |
| agree / disagree / missing | 1 / 4 / 0 |
| extra printed lines in second | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 13, 14, 15, 23, 31, 32, 39, 41, 43, 44, 97 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 13, 14, 15, 23, 31, 39, 41, 43, 44 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| p501 | 2025 returns; PDF created 2026-02-04 | 6 | cited pages | 6aca9108a08fb6d4725c630023df5e17084d92135c6607cd7c536e8e0c67f19b | 6 | 2e0a281a7d3f73f1334d5f59a39a9fe4c393fd10dd6e6c6b1b8639c5ef038671 |
| i8889 | 2025 | 4 | pages named by another document's citation | bfbdc8bbe0b85d088325243f176d4c8261b0ca2428f75f4f41e4a339ecb5495c | 4 | 533a42f870f12dc6c1984815eae1a4bf59d6fde28cbc909d9a4e76ff41c6eda7 |

##### Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, qdcg_amount, se, tax_on_amount, tcw |
| named form | interest |
| named form, inputs and named lines: clcw.prior_11, clcw.prior_14, clcw.prior_sd15, clcw.prior_sd21, clcw.prior_sd7, clcw.spouse_screen | clcw |
| named form, inputs and named lines: clcw_next_year.final_return | clcw_next_year |
| named form, inputs and named lines: f2441.benefits, f2441.care, f2441.care_other, f2441.employer_care, f2441.line13, f2441.line14, f2441.mfs_spouse_deemed, f2441.mfs_spouse_earned, f2441.nondependent, f2441.other_care_expenses, f2441.plan_max, f2441.plans_differ, f2441.prior_year, f2441.spouse_died, f2441.student, f2441.unable | f2441 |
| named form, inputs and named lines: f8959.line24, f8959.territory_w2 | f8959 |
| named form, inputs and named lines: s3.adoption, s3.adoption_any, s3.adoption_earlier, s3.adoption_final, s3.adoption_stepchild, s3.adoption_us, s3.credit_bond, s3.disability_retired, s3.elderly_credit, s3.ev, s3.ev_bought, s3.ev_credit, s3.ev_dealer, s3.ev_equipment, s3.farmland, s3.farmland_deferral, s3.foreign_any, s3.kerosene, s3.kerosene_credit, s3.line10, s3.line2, s3.mcc, s3.prior_amt, s3.prior_amt_deferral, s3.prior_forms, s3.prior_other_forms, s3.repaid_income, s3.section960c, s3.section965, s3.virgin_islands | s3 |
| named form, inputs and named lines: s8812.combat_pay, s8812.puerto_rico | s8812 |
| named form, inputs and named lines: sb.account_any, sb.asset_any, sb.bond_special, sb.bonds_any, sb.company_any, sb.fbar_required, sb.form5471, sb.form8938, sb.line7a, sb.line8, sb.nominee, sb.ordinary_dividends, sb.territory_any, sb.trust_any | sb |
| named line | f8960, rec, refund, s2 |
| shared page | dependent, eic, f1040, f5695, f8889, ira, person, retirement, s1, sa, sales, scope, sd, ssb |

##### Raw second transcription

```yaml
```yaml
lines:
  - id: household.mfs
    printed: "(helper)"
    label: "Married filing separately: you are married at the end of 2025 and file a separate return"
    type: Bool
    expr:
      op: test
      eq: [f1040.status, {const: "mfs"}]
  - id: household.mfs_apart_all_year
    printed: "(helper)"
    label: "Married filing separately and you lived apart from your spouse for all of 2025"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [household.mfs, {const: true}]}
        - {op: test, eq: [household.mfs_living, {const: "apart_all_year"}]}
  - id: household.mfs_apart_last6
    printed: "(helper)"
    label: "Married filing separately and you lived apart from your spouse for the last 6 months of 2025"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [household.mfs, {const: true}]}
        - op: test
          any:
            - {op: test, eq: [household.mfs_living, {const: "apart_last6"}]}
            - {op: test, eq: [household.mfs_living, {const: "apart_all_year"}]}
    note: "Open: whether this interface means only the enum value apart_last6 (lived together only before July 1) or the IRS condition 'lived apart from your spouse for the last 6 months of 2025'. Chose the IRS condition, which a filer who lived apart all year also meets, so both apart_last6 and apart_all_year count."
  - id: household.mfs_community_property
    printed: "(helper)"
    label: "Married filing separately and you lived in a community property state in 2025 (different rules apply; see Pub. 555)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [household.mfs, {const: true}]}
        - {op: test, eq: [household.community_property, {const: true}]}
    note: "Read from 'If you are married and file a separate return ... Different rules apply to people in community property states; see Pub. 555.' The registered domestic partner rule (household.rdp) is not tied to MFS status and is not included."
  - id: household.h_single_conflict
    printed: "(helper)"
    label: "Single checked, but you were married on December 31, 2025, or your spouse died in 2025 (considered married for the whole year)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [f1040.status, {const: "single"}]}
        - op: test
          any:
            - {op: test, eq: [household.married_dec31, {const: true}]}
            - {op: test, eq: [household.spouse_died_this_year, {const: true}]}
  - id: household.h_mfj_conflict
    printed: "(helper)"
    label: "Married filing jointly checked, but you were not married at the end of 2025 and your spouse did not die in 2025"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [f1040.status, {const: "mfj"}]}
        - {op: test, eq: [household.married_dec31, {const: false}]}
        - {op: test, eq: [household.spouse_died_this_year, {const: false}]}
  - id: household.h_mfs_conflict
    printed: "(helper)"
    label: "Married filing separately checked, but you were not married at the end of 2025"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [household.mfs, {const: true}]}
        - {op: test, eq: [household.married_dec31, {const: false}]}
    note: "Follows the Form 1040 instruction 'Check the Married filing separately box ... if you are married at the end of 2025'. Pub. 501 treats a filer whose spouse died in 2025 as married for the whole year, but no supplied input is asked of an MFS filer about a spouse's death, so that case is not excepted here."
  - id: household.h_hoh_conflict
    printed: "(helper)"
    label: "Head of household checked, but you are not unmarried or considered unmarried, or you did not pay over half the cost of keeping up your home"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [f1040.status, {const: "hoh"}]}
        - op: test
          any:
            - {op: test, eq: [household.home_cost, {const: false}]}
            - {op: test, eq: [household.spouse_died_this_year, {const: true}]}
            - op: test
              all:
                - {op: test, eq: [household.married_dec31, {const: true}]}
                - {op: test, eq: [household.considered_unmarried, {const: false}]}
    note: "Both Test 1 and Test 2 require paying over half the cost of keeping up a home. household.home_cost asks about 'your home', so it is used for both tests. The qualifying-person part of Tests 1 and 2 is evaluated per dependent elsewhere and is not checked here."
  - id: household.h_qss_conflict
    printed: "(helper)"
    label: "Qualifying surviving spouse checked, but not all five tests apply"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [f1040.status, {const: "qss"}]}
        - {op: test, eq: [household.qss_eligible, {const: false}]}
  - id: household.filing_status_conflict
    printed: "(helper)"
    label: "The filing status checked conflicts with your answers about marital status and household"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [household.h_single_conflict, {const: true}]}
        - {op: test, eq: [household.h_mfj_conflict, {const: true}]}
        - {op: test, eq: [household.h_mfs_conflict, {const: true}]}
        - {op: test, eq: [household.h_hoh_conflict, {const: true}]}
        - {op: test, eq: [household.h_qss_conflict, {const: true}]}
    note: "Open: the pages do not define this interface. Read it as the checked filing status (f1040.status) being inconsistent with the Form 1040 and Pub. 501 filing-status conditions, as far as the supplied household inputs can test them."
```
```
<!-- part section household.filing_status_conflict -->
household.filing_status_conflict — The filing status conflicts with the marriage facts entered
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "household.no"}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"alternatives": [{"guard": {"args": [{"const": false}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"input": "household.ever_married"}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}}], "op": "choose"}], "test": "eq"}, "then": {"param": "household.no"}}, {"guard": {"args": [{"const": true}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"input": "household.ever_married"}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}}], "op": "choose"}], "test": "eq"}, "then": {"input": "household.married_dec31"}}], "op": "choose"}], "test": "eq"}, "then": {"args": [{"const": false}, {"alternatives": [{"guard": {"args": [{"const": false}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"input": "household.ever_married"}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}}], "op": "choose"}], "test": "eq"}, "then": {"param": "household.no"}}, {"guard": {"args": [{"const": true}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"input": "household.ever_married"}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}}], "op": "choose"}], "test": "eq"}, "then": {"input": "household.spouse_died_this_year"}}], "op": "choose"}], "test": "eq"}}, {"guard": {"args": [{"const": true}, {"alternatives": [{"guard": {"args": [{"const": false}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"input": "household.ever_married"}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}}], "op": "choose"}], "test": "eq"}, "then": {"param": "household.no"}}, {"guard": {"args": [{"const": true}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"input": "household.ever_married"}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}}], "op": "choose"}], "test": "eq"}, "then": {"input": "household.married_dec31"}}], "op": "choose"}], "test": "eq"}, "then": {"param": "household.no"}}], "op": "choose"}}, {"guard": {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"input": "household.ever_married"}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}}], "op": "choose"}], "test": "eq"}, "then": {"param": "household.no"}}, {"guard": {"args": [{"const": true}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"input": "household.ever_married"}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}}], "op": "choose"}], "test": "eq"}, "then": {"input": "household.married_dec31"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"args": [{"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "household.considered_unmarried"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.married_dec31"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"input": "household.home_cost"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.spouse_died_this_year"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": true}, {"input": "household.married_dec31"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.spouse_died_this_year"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "household.married_dec31"}], "test": "eq"}, {"args": [{"const": false}, {"input": "household.spouse_died_this_year"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "household.married_dec31"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "household.qss_eligible"}], "test": "eq"}], "test": "all"}], "test": "any"}
```

Second transcription's note: Open: the pages do not define this interface. Read it as the checked filing status (f1040.status) being inconsistent with the Form 1040 and Pub. 501 filing-status conditions, as far as the supplied household inputs can test them.

Ruling: open
Reviewed in: pass b0a9e2ada871

<!-- part section household.mfs -->
household.mfs — Filing status married filing separately
Status: **AGREE**
Reviewed in: pass b0a9e2ada871

<!-- part section household.mfs_apart_all_year -->
household.mfs_apart_all_year — Married filing separately, and you lived apart from your spouse for all of 2025
Status: **DISAGREE**

Project:

```json
{"args": [{"const": "apart_all_year"}, {"alternatives": [{"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"input": "household.mfs_living"}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "household.mfs_living_else"}}], "op": "choose"}], "test": "eq"}
```

Second:

```json
{"args": [{"args": [{"const": "apart_all_year"}, {"input": "household.mfs_living"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}
```

Ruling: open
Reviewed in: pass b0a9e2ada871

<!-- part section household.mfs_apart_last6 -->
household.mfs_apart_last6 — Married filing separately, and your spouse did not live with you at any time in the last 6
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": "apart_all_year"}, {"alternatives": [{"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"input": "household.mfs_living"}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "household.mfs_living_else"}}], "op": "choose"}], "test": "eq"}, {"args": [{"const": "apart_last6"}, {"alternatives": [{"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"input": "household.mfs_living"}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"param": "household.mfs_living_else"}}], "op": "choose"}], "test": "eq"}], "test": "any"}
```

Second:

```json
{"args": [{"args": [{"args": [{"const": "apart_all_year"}, {"input": "household.mfs_living"}], "test": "eq"}, {"args": [{"const": "apart_last6"}, {"input": "household.mfs_living"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}
```

Second transcription's note: Open: whether this interface means only the enum value apart_last6 (lived together only before July 1) or the IRS condition 'lived apart from your spouse for the last 6 months of 2025'. Chose the IRS condition, which a filer who lived apart all year also meets, so both apart_last6 and apart_all_year count.

Ruling: open
Reviewed in: pass b0a9e2ada871

<!-- part section household.mfs_community_property -->
household.mfs_community_property — Married filing separately, and you lived in a community property state at some time in 202
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "household.no"}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"input": "household.community_property"}}], "op": "choose"}
```

Second:

```json
{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.community_property"}], "test": "eq"}], "test": "all"}
```

Second transcription's note: Read from 'If you are married and file a separate return ... Different rules apply to people in community property states; see Pub. 555.' The registered domestic partner rule (household.rdp) is not tied to MFS status and is not included.

Ruling: open
Reviewed in: pass b0a9e2ada871

<!-- end -->
