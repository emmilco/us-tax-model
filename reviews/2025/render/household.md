# Render comparison — household

The rendered English of every printed line of `Household facts for dependents and head of household` (`rendered/2025/household.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 457c251b718bcf0e111c6f805cf345c5d5225a246076344461d7ed1893c3469f |
| lines judged | 10 |
| match / mismatch / unclear / missing | 9 / 0 / 1 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 14, 18, 19 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 18, 19 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### taxpayer_tin — Do you have an SSN or ITIN issued on or before the due date of your return, or have you ap
Status: **MATCH**

Model: This matches the filer's part of Step 5 question 1: 'have either an SSN or ITIN issued on or before the due date of your 2025 return (including extensions)? (Answer "Yes" if you are applying for an ITIN...).' The IRS question also covers 'your spouse if filing a joint return', but this helper is limited by its label to the filer.

### taxpayer_work_ssn — Do you have an SSN valid for employment issued before the due date of your return?
Status: **MATCH**

Model: This matches the filer's part of Step 3 question 4: 'SSNs valid for employment and issued before the due date of your 2025 return (including extensions).' The spouse and child parts of that question are outside this filer-only helper.

### home_cost — Did you pay over half the cost of keeping up your home for 2025?
Status: **MATCH**

Model: Test 2 reads 'You paid over half the cost of keeping up a home in which you lived', and the restatement asks the same thing for 2025.

### unmarried — Were you unmarried, or considered unmarried under the head of household rules, at the end 
Status: **MATCH**

Model: This follows 'Check the "Head of household" box only if you are unmarried (or considered unmarried)'. The conditions for being considered unmarried are left to the filer's answer.

### test1_persons — Number of parents who qualify you under Test 1
Status: **MATCH**

Model: Test 1 needs a parent 'whom you can claim as a dependent, except under a multiple support agreement', whose main home for all of 2025 you paid over half the cost of keeping up. Counting the dependent entries flagged by a per-person Test 1 helper with that meaning, and testing for any, is consistent with the text.

### test2_persons — Number of persons who qualify you under Test 2
Status: **UNCLEAR**

Restated: Add dependent.one over every confirmed dependent entry for which helper "A Test 2 person who lived with you more than half the year (the home-cost condition of Test 2 is tested on the household form)" = true, within the current person when parent-bound. An unanswered roster is unknown.

Model: Test 2 also counts persons who are not your dependents: 'Your unmarried qualifying child who isn't your dependent' and items 3 and 4. The restatement counts only 'confirmed dependent entries', and the text given does not say whether the roster includes these non-dependent qualifying children. The per-person helper's handling of the 'Exception to time lived with you' and the exclusions a–c is also not shown.

Ruling: representation; project retained. "Confirmed entry" is the renderer's wording for every person listed, not for dependents only; `dependent.hoh_test2` counts a claimed dependent who lived with the filer more than half the year and is not a household-member-only dependent, or an unmarried qualifying child who lived with the filer more than half the year whether or not a dependent (i1040gi p. 14, Test 2, items 1 and 2). Items 3 and 4 and exclusions (a) and (c) are the divorced-parent and multiple-support rules, which are refused. No change to the data.

### test1_met — Test 1 met
Status: **MATCH**

Model: Test 1 applies when at least one parent meets it, which is a count greater than zero.

### test2_met — Test 2 met, having paid over half the cost of keeping up your own home
Status: **MATCH**

Model: Test 2 reads 'You paid over half the cost of keeping up a home in which you lived and in which one of the following also lived for more than half of the year'. The restatement combines the home-cost answer with at least one qualifying Test 2 person.

### hoh_eligible — Unmarried or considered unmarried, and Test 1 or Test 2 applies
Status: **MATCH**

Model: This mirrors 'Check the "Head of household" box only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies.'

### hoh_fails — Head of household checked without meeting its tests
Status: **MATCH**

Model: This flags a return where Head of household is checked although the condition for checking it ('only if you are unmarried ... and either Test 1 or Test 2 applies') is not met, which follows directly from that sentence.

## Raw response

```yaml
```yaml
lines:
  - key: "taxpayer_tin"
    status: MATCH
    reason: "This matches the filer's part of Step 5 question 1: 'have either an SSN or ITIN issued on or before the due date of your 2025 return (including extensions)? (Answer \"Yes\" if you are applying for an ITIN...).' The IRS question also covers 'your spouse if filing a joint return', but this helper is limited by its label to the filer."
  - key: "taxpayer_work_ssn"
    status: MATCH
    reason: "This matches the filer's part of Step 3 question 4: 'SSNs valid for employment and issued before the due date of your 2025 return (including extensions).' The spouse and child parts of that question are outside this filer-only helper."
  - key: "home_cost"
    status: MATCH
    reason: "Test 2 reads 'You paid over half the cost of keeping up a home in which you lived', and the restatement asks the same thing for 2025."
  - key: "unmarried"
    status: MATCH
    reason: "This follows 'Check the \"Head of household\" box only if you are unmarried (or considered unmarried)'. The conditions for being considered unmarried are left to the filer's answer."
  - key: "test1_persons"
    status: MATCH
    reason: "Test 1 needs a parent 'whom you can claim as a dependent, except under a multiple support agreement', whose main home for all of 2025 you paid over half the cost of keeping up. Counting the dependent entries flagged by a per-person Test 1 helper with that meaning, and testing for any, is consistent with the text."
  - key: "test2_persons"
    status: UNCLEAR
    reason: "Test 2 also counts persons who are not your dependents: 'Your unmarried qualifying child who isn't your dependent' and items 3 and 4. The restatement counts only 'confirmed dependent entries', and the text given does not say whether the roster includes these non-dependent qualifying children. The per-person helper's handling of the 'Exception to time lived with you' and the exclusions a–c is also not shown."
  - key: "test1_met"
    status: MATCH
    reason: "Test 1 applies when at least one parent meets it, which is a count greater than zero."
  - key: "test2_met"
    status: MATCH
    reason: "Test 2 reads 'You paid over half the cost of keeping up a home in which you lived and in which one of the following also lived for more than half of the year'. The restatement combines the home-cost answer with at least one qualifying Test 2 person."
  - key: "hoh_eligible"
    status: MATCH
    reason: "This mirrors 'Check the \"Head of household\" box only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies.'"
  - key: "hoh_fails"
    status: MATCH
    reason: "This flags a return where Head of household is checked although the condition for checking it ('only if you are unmarried ... and either Test 1 or Test 2 applies') is not met, which follows directly from that sentence."
```
```
