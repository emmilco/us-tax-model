# Render comparison — household

The rendered English of every printed line of `Household facts for dependents and head of household` (`rendered/2025/household.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 1bde484c7b4e81fae422ea586e5c942bef39e9f6f161d59868e54d049e6ad36d |
| lines judged | 11 |
| match / mismatch / unclear / missing | 9 / 1 / 1 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 |
| --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 14, 17, 18, 19 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 |

## Lines

### taxpayer_age — Your age at the end of 2025
Status: **MATCH**

Model: This is a plain input of the filer's age at the end of 2025. The text uses that age when it compares it with a child's age ("Under age 19 at the end of 2025 and younger than you").

### taxpayer_tin — Do you have an SSN or ITIN issued on or before the due date of your return, or have you ap
Status: **MATCH**

Model: This matches Step 5, question 1: "have either an SSN or ITIN issued on or before the due date of your 2025 return (including extensions)? (Answer 'Yes' if you are applying for an ITIN on or before the return due date...)". The helper covers only the filer, not a spouse, and its label says so.

### taxpayer_work_ssn — Do you have an SSN valid for employment issued before the due date of your return?
Status: **MATCH**

Model: This matches Step 3, question 4 for the filer: "SSNs valid for employment and issued before the due date of your 2025 return (including extensions)".

### home_cost — Did you pay over half the cost of keeping up your home for 2025?
Status: **MATCH**

Model: This is a plain input matching Test 2's "You paid over half the cost of keeping up a home in which you lived".

### unmarried — Were you unmarried, or considered unmarried under the head of household rules, at the end 
Status: **MATCH**

Model: This is a plain input matching "if you are unmarried (or considered unmarried)". The text lists the ways to be considered unmarried, and the filer applies them.

### test1_persons — Number of parents who qualify you under Test 1
Status: **UNCLEAR**

Restated: Add dependent.one over every confirmed dependent entry for which helper "Qualifies you for head of household under Test 1 (a parent whose main home you kept up)" = true, within the current person when parent-bound. An unanswered roster is unknown.

Model: Counting over dependent entries fits Test 1, which requires "your parent whom you can claim as a dependent". But the per-entry helper it counts isn't defined in the glossary. So I can't confirm it requires "main home for all of 2025", that you paid over half the cost of that home, and the exclusion "except under a multiple support agreement".

Ruling: representation; project retained. The per-dependent `dependent.hoh_test1` requires the parent to be claimed as a dependent and the filer to have paid over half the cost of the parent's main home for all of 2025 (`dependent.parent_home_paid`, whose question says so); a multiple support agreement is refused (`dependent.qualifying_relative` refuses on `dependent.multiple_support`). The dependent worksheet has its own logs. No change to the data.

### test2_persons — Number of persons who qualify you under Test 2
Status: **MISMATCH**

Restated: Add dependent.one over every confirmed dependent entry for which helper "Qualifies you for head of household under Test 2 (lived with you more than half the year)" = true, within the current person when parent-bound. An unanswered roster is unknown.

Model: It counts only confirmed dependent entries, but Test 2 also covers people who aren't your dependents: "2. Your unmarried qualifying child who isn't your dependent", plus items 3 and 4. The restatement also doesn't show the exclusions a–c (divorced-parent rule, "lived with you for all of 2025" only, multiple support agreement) or the "more than half of the year" condition.

Ruling: representation; project retained. "Confirmed entry" is the renderer's wording for every person listed, not for dependents only; `dependent.hoh_test2` counts a claimed dependent who lived with the filer more than half the year and is not a household-member-only dependent, or an unmarried qualifying child who lived with the filer more than half the year whether or not a dependent (i1040gi p. 14, Test 2, items 1 and 2). Items 3 and 4 and exclusions (a) and (c) are the divorced-parent and multiple-support rules, which are refused. No change to the data.

### test1_met — Test 1 met
Status: **MATCH**

Model: Test 1 applies when at least one parent qualifies, which is the same as a count above zero.

### test2_met — Test 2 met, having paid over half the cost of keeping up your own home
Status: **MATCH**

Model: This matches Test 2: "You paid over half the cost of keeping up a home in which you lived and in which one of the following also lived". It requires both the cost condition and at least one qualifying person, though it is only as accurate as the test2_persons count it uses.

### hoh_eligible — Unmarried or considered unmarried, and Test 1 or Test 2 applies
Status: **MATCH**

Model: This matches "Check the 'Head of household' box only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies."

### hoh_fails — Head of household checked without meeting its tests
Status: **MATCH**

Model: This flags Head of household being checked when the "only if" condition for that box isn't met, which is what the text describes.

## Raw response

```yaml
```yaml
lines:
  - key: "taxpayer_age"
    status: MATCH
    reason: "This is a plain input of the filer's age at the end of 2025. The text uses that age when it compares it with a child's age (\"Under age 19 at the end of 2025 and younger than you\")."
  - key: "taxpayer_tin"
    status: MATCH
    reason: "This matches Step 5, question 1: \"have either an SSN or ITIN issued on or before the due date of your 2025 return (including extensions)? (Answer 'Yes' if you are applying for an ITIN on or before the return due date...)\". The helper covers only the filer, not a spouse, and its label says so."
  - key: "taxpayer_work_ssn"
    status: MATCH
    reason: "This matches Step 3, question 4 for the filer: \"SSNs valid for employment and issued before the due date of your 2025 return (including extensions)\"."
  - key: "home_cost"
    status: MATCH
    reason: "This is a plain input matching Test 2's \"You paid over half the cost of keeping up a home in which you lived\"."
  - key: "unmarried"
    status: MATCH
    reason: "This is a plain input matching \"if you are unmarried (or considered unmarried)\". The text lists the ways to be considered unmarried, and the filer applies them."
  - key: "test1_persons"
    status: UNCLEAR
    reason: "Counting over dependent entries fits Test 1, which requires \"your parent whom you can claim as a dependent\". But the per-entry helper it counts isn't defined in the glossary. So I can't confirm it requires \"main home for all of 2025\", that you paid over half the cost of that home, and the exclusion \"except under a multiple support agreement\"."
  - key: "test2_persons"
    status: MISMATCH
    reason: "It counts only confirmed dependent entries, but Test 2 also covers people who aren't your dependents: \"2. Your unmarried qualifying child who isn't your dependent\", plus items 3 and 4. The restatement also doesn't show the exclusions a–c (divorced-parent rule, \"lived with you for all of 2025\" only, multiple support agreement) or the \"more than half of the year\" condition."
  - key: "test1_met"
    status: MATCH
    reason: "Test 1 applies when at least one parent qualifies, which is the same as a count above zero."
  - key: "test2_met"
    status: MATCH
    reason: "This matches Test 2: \"You paid over half the cost of keeping up a home in which you lived and in which one of the following also lived\". It requires both the cost condition and at least one qualifying person, though it is only as accurate as the test2_persons count it uses."
  - key: "hoh_eligible"
    status: MATCH
    reason: "This matches \"Check the 'Head of household' box only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies.\""
  - key: "hoh_fails"
    status: MATCH
    reason: "This flags Head of household being checked when the \"only if\" condition for that box isn't met, which is what the text describes."
```
```
