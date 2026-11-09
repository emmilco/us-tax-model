# Review record 191aa51ffac9 — transcription household.deepseek

One pass of a review, stored once (tools/transcription/review_store.py); the form's index says which lines it still judges.

```json
{
 "family": "deepseek",
 "form": "household",
 "kind": "transcription",
 "policies": {
  "comparison policy": "checked-expression-types-v2",
  "input context policy": "required-review-interfaces-v2",
  "prompt policy": "source-only-computation-v3+lines-v2",
  "type validation policy": "project-expression-types-v3"
 },
 "prompt_sha256": "640c8b7f885232cc9973593a8de6236422b6abaeb5faf27f6686a1905f2c3c91",
 "response_sha256": "500ebc5102d96c6c5a09d7616c41b1a46cc8fd38c77fc40ee1173e3da025c078",
 "scope": [
  "household.hoh_fails",
  "household.qss_fails",
  "household.cp_marriage_ended",
  "household.filing_status_conflict"
 ],
 "subjects": {
  "household.cp_marriage_ended": "a4dd7ded639151d4f130ebbd7925404435613a1b67daf9bec834a91a4e8b05d2",
  "household.filing_status_conflict": "959a2f15e9956ceabebb956ee7da3f4445592fe8ec91d323c61333d89a41e07f",
  "household.hoh_fails": "96f9e45bb7ef3a93a4f8b7b83b29c455ab3d4e320c880494442b0edcd6417f70",
  "household.qss_fails": "49db0cd4d57e1d8f68ff7615a282d68a1900f30e202c0c01e4293d18fbb0dbb1"
 }
}
```

<!-- part block -->
#### Pass 640c8b7f8852

| field | value |
| --- | --- |
| date | 2026-11-07 |
| review scope | lines household.hoh_fails, household.qss_fails, household.cp_marriage_ended, household.filing_status_conflict |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 640c8b7f885232cc9973593a8de6236422b6abaeb5faf27f6686a1905f2c3c91 |
| prompt policy | source-only-computation-v3+lines-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 803c699487320ab901bbe4b49b892f8f0bef6a2ab5ef0584d86dc75fafd55c96 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 877d0d54921e64f9c104d4b53ea77cd4216946a2bb5fddeb853f010608dfdcbd |
| receipt | .transcription/household.deepseek.lines-d801bd4b40fd |
| printed lines compared | 4 |
| agree / disagree / missing | 1 / 3 / 0 |
| extra printed lines in second | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 13, 14, 15, 23, 41 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 13, 14, 15, 23, 41 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| p501 | 2025 returns; PDF created 2026-02-04 | 6, 8, 9, 11 | cited pages | 6aca9108a08fb6d4725c630023df5e17084d92135c6607cd7c536e8e0c67f19b | 6, 8, 11 | 2e0a281a7d3f73f1334d5f59a39a9fe4c393fd10dd6e6c6b1b8639c5ef038671 |
| i8889 | 2025 | 4 | pages named by another document's citation | bfbdc8bbe0b85d088325243f176d4c8261b0ca2428f75f4f41e4a339ecb5495c | 4 | 533a42f870f12dc6c1984815eae1a4bf59d6fde28cbc909d9a4e76ff41c6eda7 |

##### Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form | interest |
| named form, inputs and named lines: sb.fbar_required, sb.form8938, sb.line7a, sb.line8, sb.ordinary_dividends, sb.unsupported | sb |
| named line | f8960, refund |
| shared page | dependent, eic, f1040, f8889, person, s1, s3, scope |

##### Raw second transcription

```yaml
lines:
  - id: household.h_married_or_died
    printed: "(helper)"
    label: "Married at year end or spouse died in 2025"
    type: Bool
    expr:
      op: test
      any:
        - op: test
          eq: ["household.married", {const: true}]
        - op: test
          eq: ["household.spouse_died_2025", {const: true}]

  - id: household.h_hoh_test1_count
    printed: "(helper)"
    label: "Number of dependent entries meeting head of household Test 1"
    type: Count
    expr:
      op: sum_over
      collection: dependent
      field: dependent.one
      where:
        op: test
        eq: ["dependent.hoh_test1", {const: true}]

  - id: household.h_hoh_test2_count
    printed: "(helper)"
    label: "Number of dependent entries meeting head of household Test 2"
    type: Count
    expr:
      op: sum_over
      collection: dependent
      field: dependent.one
      where:
        op: test
        eq: ["dependent.hoh_test2", {const: true}]

  - id: household.h_hoh_eligible
    printed: "(helper)"
    label: "Head of household eligibility from the supplied household and dependent facts"
    type: Bool
    expr:
      op: test
      all:
        - op: test
          eq: ["household.unmarried", {const: true}]
        - op: test
          any:
            - op: test
              gt: ["household.h_hoh_test1_count", {const: 0, type: Count}]
            - op: test
              all:
                - op: test
                  eq: ["household.home_cost", {const: true}]
                - op: test
                  gt: ["household.h_hoh_test2_count", {const: 0, type: Count}]

  - id: household.hoh_fails
    printed: "(helper)"
    label: "Head of household filing status fails the household facts"
    type: Bool
    expr:
      op: test
      all:
        - op: test
          eq: ["f1040.status", {const: "hoh"}]
        - op: test
          not:
            op: test
            eq: ["household.h_hoh_eligible", {const: true}]
    note: "Required interface. Chosen reading: true only when Form 1040 status is head of household and the supplied household facts fail the HOH tests. Test 1 uses the dependent form's HOH Test 1 field, which includes the parent-home cost; Test 2 uses the dependent form's HOH Test 2 field plus household.home_cost. A qualifying child who is not represented in the dependent collection is outside this helper."

  - id: household.qss_fails
    printed: "(helper)"
    label: "Qualifying surviving spouse filing status fails the household facts"
    type: Bool
    expr:
      op: test
      all:
        - op: test
          eq: ["f1040.status", {const: "qss"}]
        - op: test
          any:
            - op: test
              eq: ["household.qss_eligible", {const: false}]
            - op: test
              eq: ["household.spouse_died_2025", {const: true}]
            - op: test
              eq: ["household.married", {const: true}]
    note: "Required interface. Chosen reading: true when QSS is selected and either the all-five-tests QSS question is false, the spouse died in 2025 (which cannot qualify for QSS), or the taxpayer is married at the end of 2025."

  - id: household.cp_marriage_ended
    printed: "(helper)"
    label: "Community-property marriage ended during 2025 by divorce or legal separation"
    type: Bool
    expr:
      op: test
      all:
        - op: test
          eq: ["household.community_property", {const: true}]
        - op: test
          eq: ["household.cp_married", {const: true}]
    note: "Required interface. Chosen reading: true when the taxpayer lived in a community property state in 2025 and answered yes to the community-property marriage question, which describes being married during 2025 before a divorce or legal separation. A 2025 death is not treated here because the separate spouse-died question addresses that situation for filing status."

  - id: household.filing_status_conflict
    printed: "(helper)"
    label: "Selected filing status conflicts with the household facts"
    type: Bool
    expr:
      op: test
      any:
        - op: test
          eq: ["household.hoh_fails", {const: true}]
        - op: test
          eq: ["household.qss_fails", {const: true}]
        - op: test
          all:
            - op: test
              eq: ["f1040.status", {const: "single"}]
            - op: test
              eq: ["household.h_married_or_died", {const: true}]
        - op: test
          all:
            - op: test
              eq: ["f1040.status", {const: "mfj"}]
            - op: test
              not:
                op: test
                eq: ["household.h_married_or_died", {const: true}]
        - op: test
          all:
            - op: test
              eq: ["f1040.status", {const: "mfs"}]
            - op: test
              not:
                op: test
                eq: ["household.h_married_or_died", {const: true}]
    note: "Required interface. Chosen reading: reports a conflict between the selected filing status and the household facts. HOH and QSS conflicts use the specific failure flags; single conflicts with married-at-year-end or spouse-died-in-2025 facts; MFJ and MFS require one of those facts."
```
<!-- part section household.hoh_fails -->
household.hoh_fails — Head of household checked without meeting its tests
Status: **AGREE**
Reviewed in: pass 640c8b7f8852

<!-- part section household.qss_fails -->
household.qss_fails — Qualifying surviving spouse checked without meeting its tests
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "household.qss_eligible"}], "test": "eq"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"args": [{"const": false}, {"input": "household.qss_eligible"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.married"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.spouse_died_2025"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}
```

Second transcription's note: Required interface. Chosen reading: true when QSS is selected and either the all-five-tests QSS question is false, the spouse died in 2025 (which cannot qualify for QSS), or the taxpayer is married at the end of 2025.

Ruling: open
Reviewed in: pass 640c8b7f8852

<!-- part section household.cp_marriage_ended -->
household.cp_marriage_ended — Not filing jointly, and married for part of 2025 while living in a community property stat
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": false}, {"input": "household.married"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.community_property"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.cp_married"}], "test": "eq"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"const": true}, {"input": "household.community_property"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.cp_married"}], "test": "eq"}], "test": "all"}
```

Second transcription's note: Required interface. Chosen reading: true when the taxpayer lived in a community property state in 2025 and answered yes to the community-property marriage question, which describes being married during 2025 before a divorce or legal separation. A 2025 death is not treated here because the separate spouse-died question addresses that situation for filing status.

Ruling: open
Reviewed in: pass 640c8b7f8852

<!-- part section household.filing_status_conflict -->
household.filing_status_conflict — The filing status conflicts with the marriage facts entered
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "household.married"}], "test": "eq"}, {"args": [{"const": false}, {"input": "household.spouse_died_2025"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.married"}], "test": "eq"}], "test": "all"}], "test": "any"}
```

Second:

```json
{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "household.married"}], "test": "ne"}, {"args": [{"const": true}, {"input": "household.spouse_died_2025"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": true}, {"input": "household.married"}], "test": "ne"}, {"args": [{"const": true}, {"input": "household.spouse_died_2025"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"const": false}, {"input": "dependent.married"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.lawful"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.qr_all_year"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.spouse_relative"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "dependent.born_died"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.placed"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.part_year_home"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.absence_no_return"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": true}, {"input": "household.home_cost"}], "test": "ne"}], "test": "any"}, {"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.lawful"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.qr_all_year"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.spouse_relative"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.parent_home_paid"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "all"}, {"args": [{"const": true}, {"input": "household.unmarried"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": false}, {"input": "household.qss_eligible"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.married"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.spouse_died_2025"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": true}, {"input": "household.married"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.spouse_died_2025"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}], "test": "any"}
```

Second transcription's note: Required interface. Chosen reading: reports a conflict between the selected filing status and the household facts. HOH and QSS conflicts use the specific failure flags; single conflicts with married-at-year-end or spouse-died-in-2025 facts; MFJ and MFS require one of those facts.

Ruling: open
Reviewed in: pass 640c8b7f8852

<!-- end -->
