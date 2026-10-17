# Render comparison — household

The rendered English of every printed line of `Household facts for dependents and head of household` (`rendered/2025/household.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | df1a895aa3c3335ce7255aa04ba225f7bd269d251216e841f8d6e3cd966838cf |
| lines judged | 10 |
| match / mismatch / unclear / missing | 9 / 1 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 14, 18, 19 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 18, 19 | 816ff8c5ed82d0349bfa79ae008e9b4492c04005a8702145dcd8cd0139eacc47 |

## Lines

### taxpayer_tin — Do you have an SSN or ITIN issued on or before the due date of your return, or have you ap
Status: **MATCH**

Model: Restates the filer's part of Step 5 question 1: 'Did you ... have either an SSN or ITIN issued on or before the due date of your 2025 return (including extensions)? (Answer "Yes" if you are applying for an ITIN ...)'. The spouse's part ('and your spouse if filing a joint return') is outside this filer-only input.

### taxpayer_work_ssn — Do you have an SSN valid for employment issued before the due date of your return?
Status: **MATCH**

Model: Restates the filer's part of Step 3 question 4: 'Did you ... have SSNs valid for employment and issued before the due date of your 2025 return (including extensions)?'. The spouse and child parts are outside this filer-only input.

### home_cost — Did you pay over half the cost of keeping up your home for 2025?
Status: **MATCH**

Model: Matches the Test 2 condition 'You paid over half the cost of keeping up a home in which you lived'. The program uses this input only for Test 2. Test 1's parent-home cost is carried in the per-parent Test 1 helper.

### unmarried — Were you unmarried, or considered unmarried under the head of household rules, at the end 
Status: **MATCH**

Model: Matches 'Check the "Head of household" box only if you are unmarried (or considered unmarried)'. The text lists the 'considered unmarried' cases.

### test1_persons — Number of parents who qualify you under Test 1
Status: **MATCH**

Model: Counts confirmed dependents flagged as Test 1 parents. Test 1 requires 'your parent whom you can claim as a dependent' whose main home you kept up, so restricting the count to dependent entries is consistent. The per-entry helper is defined elsewhere and is not judged here.

### test2_persons — Number of persons who qualify you under Test 2
Status: **MISMATCH**

Restated: Add dependent.one over every confirmed dependent entry for which helper "A Test 2 person who lived with you more than half the year (the home-cost condition of Test 2 is tested on the household form)" = true, within the current person when parent-bound. An unanswered roster is unknown.

Model: Counts only confirmed dependent entries. Test 2 also covers non-dependents: '2. Your unmarried qualifying child who isn't your dependent', '3. Your married qualifying child who isn't your dependent only because you can be claimed as a dependent on someone else's 2025 return', and '4. Your qualifying child who ... isn't your dependent because of the rule for Children of divorced or separated parents'. No refusal names these excluded cases.

Ruling: representation; project retained. "Confirmed entry" is the renderer's wording for every person listed, not for dependents only; `dependent.hoh_test2` counts a claimed dependent who lived with the filer more than half the year and is not a household-member-only dependent, or an unmarried qualifying child who lived with the filer more than half the year whether or not a dependent (i1040gi p. 14, Test 2, items 1 and 2). Items 3 and 4 and exclusions (a) and (c) are the divorced-parent and multiple-support rules, which are refused. No change to the data.

### test1_met — Test 1 met
Status: **MATCH**

Model: Test 1 applies when at least one parent qualifies, so a count greater than zero is correct.

### test2_met — Test 2 met, having paid over half the cost of keeping up your own home
Status: **MATCH**

Model: Matches 'You paid over half the cost of keeping up a home in which you lived and in which one of the following also lived for more than half of the year'. Both the home-cost condition and a qualifying person are required.

### hoh_eligible — Unmarried or considered unmarried, and Test 1 or Test 2 applies
Status: **MATCH**

Model: Matches 'Check the "Head of household" box only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies.'

### hoh_fails — Head of household checked without meeting its tests
Status: **MATCH**

Model: Flags a return that checks 'Head of household (HOH)' when the 'only if' conditions for that box are not met. This is consistent with the instruction text.

## Raw response

```yaml
```yaml
lines:
  - key: "taxpayer_tin"
    status: MATCH
    reason: "Restates the filer's part of Step 5 question 1: 'Did you ... have either an SSN or ITIN issued on or before the due date of your 2025 return (including extensions)? (Answer \"Yes\" if you are applying for an ITIN ...)'. The spouse's part ('and your spouse if filing a joint return') is outside this filer-only input."
  - key: "taxpayer_work_ssn"
    status: MATCH
    reason: "Restates the filer's part of Step 3 question 4: 'Did you ... have SSNs valid for employment and issued before the due date of your 2025 return (including extensions)?'. The spouse and child parts are outside this filer-only input."
  - key: "home_cost"
    status: MATCH
    reason: "Matches the Test 2 condition 'You paid over half the cost of keeping up a home in which you lived'. The program uses this input only for Test 2. Test 1's parent-home cost is carried in the per-parent Test 1 helper."
  - key: "unmarried"
    status: MATCH
    reason: "Matches 'Check the \"Head of household\" box only if you are unmarried (or considered unmarried)'. The text lists the 'considered unmarried' cases."
  - key: "test1_persons"
    status: MATCH
    reason: "Counts confirmed dependents flagged as Test 1 parents. Test 1 requires 'your parent whom you can claim as a dependent' whose main home you kept up, so restricting the count to dependent entries is consistent. The per-entry helper is defined elsewhere and is not judged here."
  - key: "test2_persons"
    status: MISMATCH
    reason: "Counts only confirmed dependent entries. Test 2 also covers non-dependents: '2. Your unmarried qualifying child who isn't your dependent', '3. Your married qualifying child who isn't your dependent only because you can be claimed as a dependent on someone else's 2025 return', and '4. Your qualifying child who ... isn't your dependent because of the rule for Children of divorced or separated parents'. No refusal names these excluded cases."
  - key: "test1_met"
    status: MATCH
    reason: "Test 1 applies when at least one parent qualifies, so a count greater than zero is correct."
  - key: "test2_met"
    status: MATCH
    reason: "Matches 'You paid over half the cost of keeping up a home in which you lived and in which one of the following also lived for more than half of the year'. Both the home-cost condition and a qualifying person are required."
  - key: "hoh_eligible"
    status: MATCH
    reason: "Matches 'Check the \"Head of household\" box only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies.'"
  - key: "hoh_fails"
    status: MATCH
    reason: "Flags a return that checks 'Head of household (HOH)' when the 'only if' conditions for that box are not met. This is consistent with the instruction text."
```
```
