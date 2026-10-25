# Transcription agreement — household

Second transcription of `Household facts for dependents and head of household` by an isolated model (spec 6.5), compared line by line with `forms/2025/household.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 479f494c36f6eed441324caca9dae480294eb74a2ba2e0490f2a80dfd799cc65 |
| prompt policy | source-only-computation-v2 |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | a6e69d16188a6c51f5482550733f0a1b3d89e34205791b5ee6bf8160ff2a6481 |
| printed lines compared | 9 |
| agree / disagree / missing | 4 / 5 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040gi | 2025; printed date 2026-02-25 | 14, 17, 18, 19, 23, 39, 40, 41, 43, 44, 66 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 17, 18, 19, 23, 39, 40, 41, 43, 44, 66 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i8889 | 2025 | 4, 7 | cited pages | bfbdc8bbe0b85d088325243f176d4c8261b0ca2428f75f4f41e4a339ecb5495c | 4, 7 | 533a42f870f12dc6c1984815eae1a4bf59d6fde28cbc909d9a4e76ff41c6eda7 |
| i1040s8812 | 2025; printed date 2026-01-23 | 2 | pages named by another document's citation | fd50a5266cc20aa5a31de0535658793f75c7abbb12fd83b65dc5b21c6ede2765 | 2 | e6ba91f54df679c9c19c23169c369f14bff012ba2fe110c3973bde59676c1d45 |

## Lines

### household.hsa_both — You and your spouse each have a Form 8889
Status: **DISAGREE**

Project:

```json
{"args": [{"const": 2}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0}, {"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "eq"}
```

Second:

```json
{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0}, {"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": null}], "test": "lt"}}, {"param": "hsa.two"}], "test": "eq"}
```

Second transcription's note: Read i8889: If both you and your spouse have HSAs; counted persons with at least one HSA/Form 8889 entry.

Ruling: open

### household.hsa_split_count — Number of Forms 8889 using the spouse rule of line 6
Status: **AGREE**

### household.hsa_agreed_count — Number of Forms 8889 using an agreed allocation
Status: **AGREE**

### household.hsa_step1_sum — Both spouses Step 1 limits added together
Status: **AGREE**

### household.hsa_share_sum — Both spouses parts of the Step 1 limit added together
Status: **AGREE**

### household.all_eic_ssn — You, and your spouse if filing jointly, have SSNs valid for the EIC
Status: **DISAGREE**

Project:

```json
{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.eic_ssn"}], "test": "eq"}}], "test": "eq"}
```

Second:

```json
{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "person.eic_ssn"}], "test": "eq"}}, {"const": 0}], "test": "le"}
```

Second transcription's note: Compared the count of persons whose eic_ssn is false to zero.

Ruling: open

### household.all_tin — You, and your spouse if filing jointly, have an SSN or ITIN, or have applied for an ITIN
Status: **DISAGREE**

Project:

```json
{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "eq"}
```

Second:

```json
{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "ne"}], "test": "all"}}, {"const": 0}], "test": "le"}
```

Second transcription's note: Compared the count of persons with neither tin nor itin_applied to zero.

Ruling: open

### household.ctc_ssn — Child tax credit identification: you, or your spouse if filing jointly, have an SSN valid 
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "any"}}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "ne"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "lt"}], "test": "all"}
```

Second transcription's note: At least one person has an SSN valid for employment, and everyone has an SSN/ITIN or has applied.

Ruling: open

### household.taxpayer_work_ssn — Do you have an SSN valid for employment issued before the due date of your return?
Status: **DISAGREE**

Project:

```json
{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}
```

Second:

```json
{"args": [{"const": 1}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "eq"}
```

Ruling: open

## Raw second transcription

```yaml
lines:
  - id: household.hsa_both
    printed: "(helper)"
    label: "Both the taxpayer and spouse have an HSA (Form 8889) for 2025"
    type: Bool
    expr: {op: test, eq: ["household.h_hsa_person_count", {param: hsa.two}]}
    note: "Read i8889: If both you and your spouse have HSAs; counted persons with at least one HSA/Form 8889 entry."
  - id: household.hsa_split_count
    printed: "(helper)"
    label: "Number of spouses subject to equal allocation of the family HSA contribution limit"
    type: Count
    expr: {op: sum_over, collection: person, field: person.hsa_split}
    note: "Summed the per-person split indicators used for Form 8889 line 6."
  - id: household.hsa_agreed_count
    printed: "(helper)"
    label: "Number of spouses with an agreed different HSA allocation"
    type: Count
    expr: {op: sum_over, collection: person, field: person.hsa_agreed}
  - id: household.hsa_step1_sum
    printed: "(helper)"
    label: "Total family HSA contribution limit before allocation"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: person.hsa_step1}
  - id: household.hsa_share_sum
    printed: "(helper)"
    label: "Total HSA contribution limit allocated to the persons on this return"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: person.hsa_share}
  - id: household.all_eic_ssn
    printed: "(helper)"
    label: "All persons on the return have an SSN valid for the EIC"
    type: Bool
    expr: {op: test, eq: ["household.h_eic_ssn_bad", {param: hsa.no_months}]}
    note: "Compared the count of persons whose eic_ssn is false to zero."
  - id: household.all_tin
    printed: "(helper)"
    label: "All persons on the return have an SSN or ITIN issued or applied for"
    type: Bool
    expr: {op: test, eq: ["household.h_tin_bad", {param: hsa.no_months}]}
    note: "Compared the count of persons with neither tin nor itin_applied to zero."
  - id: household.ctc_ssn
    printed: "(helper)"
    label: "Household meets the SSN/ITIN gate for the child tax credit"
    type: Bool
    expr:
      op: test
      all:
        - op: test
          gt: ["household.h_work_ssn_count", {param: hsa.no_months}]
        - op: test
          eq: ["household.all_tin", {const: true}]
    note: "At least one person has an SSN valid for employment, and everyone has an SSN/ITIN or has applied."
  - id: household.taxpayer_work_ssn
    printed: "(helper)"
    label: "The taxpayer has an SSN valid for employment"
    type: Bool
    expr: {op: test, eq: ["household.h_taxpayer_work_count", {param: person.one}]}
  - id: household.h_hsa_person_count
    printed: "(helper)"
    label: "Number of persons on the return with at least one HSA/Form 8889"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        gt: ["person.hsa_forms", {param: hsa.no_months}]
  - id: household.h_eic_ssn_bad
    printed: "(helper)"
    label: "Number of persons on the return without an SSN valid for the EIC"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        eq: ["person.eic_ssn", {const: false}]
  - id: household.h_tin_bad
    printed: "(helper)"
    label: "Number of persons on the return with neither an SSN/ITIN nor an application"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        not:
          op: test
          any:
            - op: test
              eq: ["person.tin", {const: true}]
            - op: test
              eq: ["person.itin_applied", {const: true}]
  - id: household.h_work_ssn_count
    printed: "(helper)"
    label: "Number of persons on the return with an SSN valid for employment"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        eq: ["person.work_ssn", {const: true}]
  - id: household.h_taxpayer_work_count
    printed: "(helper)"
    label: "Number of taxpayer entries with an SSN valid for employment"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - op: test
            eq: ["person.role", {const: "taxpayer"}]
          - op: test
            eq: ["person.work_ssn", {const: true}]
```
