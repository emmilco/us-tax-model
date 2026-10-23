# Transcription agreement — household

Second transcription of `Household facts for dependents and head of household` by an isolated model (spec 6.5), compared line by line with `forms/2025/household.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 9e59b0e080fa5b3c1296608d4050c60221e916b47ee3a942f06a4c69e8bdf8d4 |
| subject sha256 | a6e69d16188a6c51f5482550733f0a1b3d89e34205791b5ee6bf8160ff2a6481 |
| printed lines compared | 9 |
| agree / disagree / missing | 5 / 4 / 0 |
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
{"args": [{"param": "hsa.two"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": 0}, {"collection": "f8889", "field": "f8889.one", "op": "sum_over", "where": null}], "test": "lt"}}], "test": "le"}
```

Second transcription's note: i8889 says that if married filing jointly and both spouses have HSAs, a separate Form 8889 is completed for each. Only the filers on the return are entered, so 'both' is read as two person entries, each with at least one Form 8889.

Ruling: representation; project retained. The second tests at least two person entries with a Form 8889; the project exactly two. The roster has one entry for you and, only on a joint return, one for your spouse, and any other roster is refused at Form 1040 line 1a (household.roster_bad), so within scope the counts agree (i8889 p. 4, 'If married filing jointly and both you and your spouse have HSAs, complete a separate Form 8889 for each of you').

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
{"args": [{"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "person.eic_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "person.eic_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "all"}
```

Second transcription's note: EIC Step 1 question 2 asks about 'you, and your spouse if filing a joint return'. The spouse's entry is therefore tested only when the filing status is married filing jointly.

Ruling: representation; project retained. The second counts the taxpayer's and the spouse's entries separately by role and tests the spouse only on a joint return; the project counts every person on the return against the roster. The roster has one entry for you and, only on a joint return, one for your spouse (household.roster_bad refuses any other at Form 1040 line 1a), so within scope the two agree (i1040gi p. 40, Step 1, question 2, 'Do you, and your spouse if filing a joint return, have a social security number ... that allows you to work and is valid for EIC purposes'; p. 44, 'For the EIC, a valid SSN is a number issued by the Social Security Administration unless "Not Valid for Employment" is printed on the social security card and the number was issued solely to allow the recipient of the SSN to apply for or receive a federally funded benefit').

### household.all_tin — You, and your spouse if filing jointly, have an SSN or ITIN, or have applied for an ITIN
Status: **DISAGREE**

Project:

```json
{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "eq"}
```

Second:

```json
{"args": [{"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "person.tin"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "person.tin"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "all"}
```

Second transcription's note: Step 5 question 1 says to answer 'Yes' if you are applying for an ITIN on or before the return due date. A pending ITIN application is therefore counted here.

Ruling: representation; project retained. The second counts the taxpayer's and the spouse's entries separately by role and tests the spouse only on a joint return; the project counts every person on the return against the roster. The roster has one entry for you and, only on a joint return, one for your spouse (household.roster_bad refuses any other at Form 1040 line 1a), so within scope the two agree (i1040gi p. 17, Before you begin, 'If you want to claim the credit for other dependents, you, and your spouse if filing jointly, must have either an SSN or ITIN'; p. 19, Step 5, question 1, an ITIN application by the due date counts on both sides).

### household.ctc_ssn — Child tax credit identification: you, or your spouse if filing jointly, have an SSN valid 
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "any"}}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "lt"}], "test": "any"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "person.tin"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "person.tin"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "all"}
```

Second transcription's note: The line 19 text says only one spouse on a joint return needs a valid SSN. The other spouse 'must have either an SSN or ITIN, and it must have been issued on or before the due date', and no allowance is made for a pending ITIN application, so person.tin alone is used. 'Each other person on the return' is read as the filers only; each child's own SSN is tested per dependent in Step 3.

Ruling: representation; project retained. The second counts the taxpayer's and the spouse's entries separately by role and tests the spouse only on a joint return; the project counts every person on the return against the roster. The roster has one entry for you and, only on a joint return, one for your spouse (household.roster_bad refuses any other at Form 1040 line 1a), so within scope the two agree (i1040gi p. 17, Before you begin, 'If you are filing a joint return, only one spouse is required to have a valid SSN to be eligible for the CTC and ACTC. The other spouse must have either an SSN or ITIN').

### household.taxpayer_work_ssn — Do you have an SSN valid for employment issued before the due date of your return?
Status: **AGREE**

## Raw second transcription

```yaml
```yaml
lines:
  - id: household.h_hsa_persons
    printed: "(helper)"
    label: "Number of persons on the return with a Form 8889"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where: {op: test, gt: [person.hsa_forms, {const: 0}]}

  - id: household.hsa_both
    printed: "(helper)"
    label: "You and your spouse each have a Form 8889"
    type: Bool
    expr: {op: test, ge: [household.h_hsa_persons, {param: hsa.two}]}
    note: "i8889 says that if married filing jointly and both spouses have HSAs, a separate Form 8889 is completed for each. Only the filers on the return are entered, so 'both' is read as two person entries, each with at least one Form 8889."

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

  - id: household.h_eic_missing_you
    printed: "(helper)"
    label: "Your entry, if you do not have an SSN valid for the EIC"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.role, {const: "taxpayer"}]}
          - {op: test, eq: [person.eic_ssn, {const: false}]}

  - id: household.h_eic_missing_spouse
    printed: "(helper)"
    label: "Your spouse's entry, if your spouse does not have an SSN valid for the EIC"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.role, {const: "spouse"}]}
          - {op: test, eq: [person.eic_ssn, {const: false}]}

  - id: household.all_eic_ssn
    printed: "(helper)"
    label: "You, and your spouse if filing jointly, have SSNs valid for the EIC"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [household.h_eic_missing_you, {const: 0}]}
        - op: test
          any:
            - {op: test, ne: [f1040.status, {const: "mfj"}]}
            - {op: test, eq: [household.h_eic_missing_spouse, {const: 0}]}
    note: "EIC Step 1 question 2 asks about 'you, and your spouse if filing a joint return'. The spouse's entry is therefore tested only when the filing status is married filing jointly."

  - id: household.h_tin_missing_you
    printed: "(helper)"
    label: "Your entry, if you have neither an SSN or ITIN nor an ITIN application"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.role, {const: "taxpayer"}]}
          - {op: test, eq: [person.tin, {const: false}]}
          - {op: test, eq: [person.itin_applied, {const: false}]}

  - id: household.h_tin_missing_spouse
    printed: "(helper)"
    label: "Your spouse's entry, if your spouse has neither an SSN or ITIN nor an ITIN application"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.role, {const: "spouse"}]}
          - {op: test, eq: [person.tin, {const: false}]}
          - {op: test, eq: [person.itin_applied, {const: false}]}

  - id: household.all_tin
    printed: "(helper)"
    label: "You, and your spouse if filing jointly, have an SSN or ITIN, or have applied for an ITIN"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [household.h_tin_missing_you, {const: 0}]}
        - op: test
          any:
            - {op: test, ne: [f1040.status, {const: "mfj"}]}
            - {op: test, eq: [household.h_tin_missing_spouse, {const: 0}]}
    note: "Step 5 question 1 says to answer 'Yes' if you are applying for an ITIN on or before the return due date. A pending ITIN application is therefore counted here."

  - id: household.h_work_you
    printed: "(helper)"
    label: "Your entry, if you have an SSN valid for employment issued before the due date of your return"
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

  - id: household.h_work_spouse
    printed: "(helper)"
    label: "Your spouse's entry, if your spouse has an SSN valid for employment issued before the due date of your return"
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

  - id: household.h_issued_missing_you
    printed: "(helper)"
    label: "Your entry, if you have no SSN or ITIN issued on or before the due date of your return"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.role, {const: "taxpayer"}]}
          - {op: test, eq: [person.tin, {const: false}]}

  - id: household.h_issued_missing_spouse
    printed: "(helper)"
    label: "Your spouse's entry, if your spouse has no SSN or ITIN issued on or before the due date of your return"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.role, {const: "spouse"}]}
          - {op: test, eq: [person.tin, {const: false}]}

  - id: household.ctc_ssn
    printed: "(helper)"
    label: "Child tax credit identification: you, or your spouse if filing jointly, have an SSN valid for employment, and each other person on the return has an SSN or ITIN"
    type: Bool
    expr:
      op: test
      all:
        - op: test
          any:
            - {op: test, gt: [household.h_work_you, {const: 0}]}
            - op: test
              all:
                - {op: test, eq: [f1040.status, {const: "mfj"}]}
                - {op: test, gt: [household.h_work_spouse, {const: 0}]}
        - {op: test, eq: [household.h_issued_missing_you, {const: 0}]}
        - op: test
          any:
            - {op: test, ne: [f1040.status, {const: "mfj"}]}
            - {op: test, eq: [household.h_issued_missing_spouse, {const: 0}]}
    note: "The line 19 text says only one spouse on a joint return needs a valid SSN. The other spouse 'must have either an SSN or ITIN, and it must have been issued on or before the due date', and no allowance is made for a pending ITIN application, so person.tin alone is used. 'Each other person on the return' is read as the filers only; each child's own SSN is tested per dependent in Step 3."

  - id: household.taxpayer_work_ssn
    printed: "(helper)"
    label: "Do you have an SSN valid for employment issued before the due date of your return?"
    type: Bool
    expr: {op: test, gt: [household.h_work_you, {const: 0}]}
```
```
