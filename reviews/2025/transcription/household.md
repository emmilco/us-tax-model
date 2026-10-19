# Transcription agreement — household

Second transcription of `Household facts for dependents and head of household` by an isolated model (spec 6.5), compared line by line with `forms/2025/household.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-19 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | ba32f76b42c895cbb54a568cbdaa66ec25ad33ee141a26dc6a7036f2982f8853 |
| printed lines compared | 9 |
| agree / disagree / missing | 4 / 5 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i8889 | 2025 | 4, 7 | cited pages | bfbdc8bbe0b85d088325243f176d4c8261b0ca2428f75f4f41e4a339ecb5495c | 4, 7 | 533a42f870f12dc6c1984815eae1a4bf59d6fde28cbc909d9a4e76ff41c6eda7 |
| i1040gi | 2025; printed date 2026-02-25 | 14, 17, 18, 40 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 17, 18, 40 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### household.hsa_both — You and your spouse each have a Form 8889
Status: **DISAGREE**

Project:

```json
{"args": [{"const": 2}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0}, {"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "eq"}
```

Second:

```json
{"args": [{"args": [{"const": 1}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": 1}, {"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": null}], "test": "le"}], "test": "all"}}], "test": "le"}, {"args": [{"const": 1}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": 1}, {"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": null}], "test": "le"}], "test": "all"}}], "test": "le"}], "test": "all"}
```

Second transcription's note: Open: Form 8889 instructions speak of 'both you and your spouse have HSAs' (and, under Specific Instructions, 'if married filing jointly'). Chosen reading: true when both a taxpayer entry and a spouse entry have a Form 8889. Filing status is not tested, because the line 6 spouse rule is not limited to joint filers.

Ruling: representation; project retained. The second counts the taxpayer's and the spouse's entries separately by role; the project counts every person. The roster has one entry for you and, only on a joint return, one for your spouse, and any other roster is refused at Form 1040 line 1a (household.roster_bad), so within scope the counts agree (i8889 p. 4, "If married filing jointly and both you and your spouse have HSAs, complete a separate Form 8889 for each of you").

### household.hsa_split_count — Number of Forms 8889 using the spouse rule of line 6
Status: **AGREE**

### household.hsa_agreed_count — Number of Forms 8889 using an agreed allocation
Status: **AGREE**

### household.hsa_step1_sum — Both spouses Step 1 limits added together
Status: **AGREE**

### household.hsa_share_sum — Both spouses parts of the Step 1 limit added together
Status: **AGREE**

### household.all_work_ssn — You, and your spouse if filing jointly, have SSNs valid for employment
Status: **DISAGREE**

Project:

```json
{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "eq"}
```

Second:

```json
{"args": [{"args": [{"args": [{"const": 1}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 1}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "le"}], "test": "all"}
```

Ruling: representation; project retained. The second counts the taxpayer's and the spouse's entries separately by role; the project counts every person. The roster has one entry for you and, only on a joint return, one for your spouse, and any other roster is refused at Form 1040 line 1a (household.roster_bad), so within scope the counts agree (Form 1040 page 1, name and SSN lines; i1040gi p. 17 and p. 40).

### household.all_tin — You, and your spouse if filing jointly, have an SSN or ITIN
Status: **DISAGREE**

Project:

```json
{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}}], "test": "eq"}
```

Second:

```json
{"args": [{"args": [{"args": [{"const": 1}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "all"}}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 1}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "all"}}], "test": "le"}], "test": "all"}
```

Ruling: representation; project retained. The second counts the taxpayer's and the spouse's entries separately by role; the project counts every person. The roster has one entry for you and, only on a joint return, one for your spouse, and any other roster is refused at Form 1040 line 1a (household.roster_bad), so within scope the counts agree (Form 1040 page 1, name and SSN lines; i1040gi p. 17 and p. 40).

### household.ctc_ssn — Child tax credit identification: you, or your spouse if filing jointly, have an SSN valid 
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "any"}}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"args": [{"args": [{"const": 1}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "all"}}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 1}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "le"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 1}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "le"}, {"args": [{"const": 1}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "all"}}], "test": "le"}], "test": "all"}], "test": "any"}
```

Second transcription's note: Open: 'each other person on the return' could also include dependents. The 'Before you begin' text addresses only the two spouses: one needs a valid SSN, and the other needs an SSN or ITIN. Each dependent's identification is tested separately in Step 3, per child. Chosen reading: only the filer and the spouse are tested here.

Ruling: representation; project retained. The second counts the taxpayer's and the spouse's entries separately by role; the project counts every person. The roster has one entry for you and, only on a joint return, one for your spouse, and any other roster is refused at Form 1040 line 1a (household.roster_bad), so within scope the counts agree (Form 1040 page 1, name and SSN lines; i1040gi p. 17 and p. 40).

### household.taxpayer_work_ssn — Do you have an SSN valid for employment issued before the due date of your return?
Status: **DISAGREE**

Project:

```json
{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}
```

Second:

```json
{"args": [{"const": 1}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "le"}
```

Ruling: representation; project retained. The project tests 0 < count and the second 1 <= count; for a count the two are the same test.

## Raw second transcription

```yaml
```yaml
lines:
  - id: household.h_tp_hsa_count
    printed: "(helper)"
    label: "Number of your entries with at least one Form 8889"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.role, {const: "taxpayer"}]}
          - {op: test, ge: [person.hsa_forms, {param: person.one}]}

  - id: household.h_sp_hsa_count
    printed: "(helper)"
    label: "Number of your spouse's entries with at least one Form 8889"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.role, {const: "spouse"}]}
          - {op: test, ge: [person.hsa_forms, {param: person.one}]}

  - id: household.hsa_both
    printed: "(helper)"
    label: "You and your spouse each have a Form 8889"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, ge: [household.h_tp_hsa_count, {param: person.one}]}
        - {op: test, ge: [household.h_sp_hsa_count, {param: person.one}]}
    note: "Open: Form 8889 instructions speak of 'both you and your spouse have HSAs' (and, under Specific Instructions, 'if married filing jointly'). Chosen reading: true when both a taxpayer entry and a spouse entry have a Form 8889. Filing status is not tested, because the line 6 spouse rule is not limited to joint filers."

  - id: household.hsa_split_count
    printed: "(helper)"
    label: "Number of Forms 8889 using the spouse rule of line 6"
    type: Count
    expr: {op: sum_over, collection: person, field: person.hsa_split}

  - id: household.hsa_agreed_count
    printed: "(helper)"
    label: "Number of Forms 8889 using an agreed allocation"
    type: Count
    expr: {op: sum_over, collection: person, field: person.hsa_agreed}

  - id: household.hsa_step1_sum
    printed: "(helper)"
    label: "Both spouses Step 1 limits added together"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: person.hsa_step1}

  - id: household.hsa_share_sum
    printed: "(helper)"
    label: "Both spouses parts of the Step 1 limit added together"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: person.hsa_share}

  - id: household.h_joint
    printed: "(helper)"
    label: "Filing a joint return (married filing jointly)"
    type: Bool
    expr: {op: test, eq: [f1040.status, {const: "mfj"}]}

  - id: household.h_tp_work_count
    printed: "(helper)"
    label: "Number of your entries with an SSN valid for employment issued before the due date of your return"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.role, {const: "taxpayer"}]}
          - {op: test, eq: [person.work_ssn, {const: true}]}

  - id: household.taxpayer_work_ssn
    printed: "(helper)"
    label: "Do you have an SSN valid for employment issued before the due date of your return?"
    type: Bool
    expr: {op: test, ge: [household.h_tp_work_count, {param: person.one}]}

  - id: household.h_sp_work_count
    printed: "(helper)"
    label: "Number of your spouse's entries with an SSN valid for employment issued before the due date of your return"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.role, {const: "spouse"}]}
          - {op: test, eq: [person.work_ssn, {const: true}]}

  - id: household.h_sp_work_ssn
    printed: "(helper)"
    label: "Your spouse has an SSN valid for employment issued before the due date of your return"
    type: Bool
    expr: {op: test, ge: [household.h_sp_work_count, {param: person.one}]}

  - id: household.h_tp_tin_count
    printed: "(helper)"
    label: "Number of your entries with an SSN or ITIN issued on or before the due date of your return"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.role, {const: "taxpayer"}]}
          - {op: test, eq: [person.tin, {const: true}]}

  - id: household.h_tp_tin
    printed: "(helper)"
    label: "You have an SSN or ITIN issued on or before the due date of your return"
    type: Bool
    expr: {op: test, ge: [household.h_tp_tin_count, {param: person.one}]}

  - id: household.h_sp_tin_count
    printed: "(helper)"
    label: "Number of your spouse's entries with an SSN or ITIN issued on or before the due date of your return"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.role, {const: "spouse"}]}
          - {op: test, eq: [person.tin, {const: true}]}

  - id: household.h_sp_tin
    printed: "(helper)"
    label: "Your spouse has an SSN or ITIN issued on or before the due date of your return"
    type: Bool
    expr: {op: test, ge: [household.h_sp_tin_count, {param: person.one}]}

  - id: household.all_work_ssn
    printed: "(helper)"
    label: "You, and your spouse if filing jointly, have SSNs valid for employment"
    type: Bool
    expr:
      op: test
      all:
        - household.taxpayer_work_ssn
        - {op: test, any: [{op: test, not: household.h_joint}, household.h_sp_work_ssn]}

  - id: household.all_tin
    printed: "(helper)"
    label: "You, and your spouse if filing jointly, have an SSN or ITIN"
    type: Bool
    expr:
      op: test
      all:
        - household.h_tp_tin
        - {op: test, any: [{op: test, not: household.h_joint}, household.h_sp_tin]}

  - id: household.ctc_ssn
    printed: "(helper)"
    label: "Child tax credit identification: you, or your spouse if filing jointly, have an SSN valid for employment, and each other person on the return has an SSN or ITIN"
    type: Bool
    expr:
      op: test
      any:
        - op: test
          all:
            - household.taxpayer_work_ssn
            - {op: test, any: [{op: test, not: household.h_joint}, household.h_sp_tin]}
        - op: test
          all:
            - household.h_joint
            - household.h_sp_work_ssn
            - household.h_tp_tin
    note: "Open: 'each other person on the return' could also include dependents. The 'Before you begin' text addresses only the two spouses: one needs a valid SSN, and the other needs an SSN or ITIN. Each dependent's identification is tested separately in Step 3, per child. Chosen reading: only the filer and the spouse are tested here."
```
```
