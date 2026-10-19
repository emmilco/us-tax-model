# Household facts for dependents and head of household

- Document: `household` (form, tax year 2025)
- Note: Facts about the filer that the dependent tests and the head of household status read. Married filing statuses remain refused elsewhere; "unmarried" here is the instructions' unmarried or considered unmarried at the end of 2025.

## (helper) — `household.taxpayer_tin_count`

- **Authored helper label:** Your entry, if the answer is yes
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "Whose entry is this, yours or your spouse's?" = 'taxpayer' and helper "Do you have an SSN or ITIN issued on or before the due date of your return, or have you applied for an ITIN by then?" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"all":[{"eq":["person.role",{"const":"taxpayer"}],"op":"test"},{"eq":["person.tin",{"const":true}],"op":"test"}],"op":"test"}}`
- Cite: [i1040gi] p. 19, Step 5, question 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.taxpayer_tin`

- **Authored helper label:** Do you have an SSN or ITIN issued on or before the due date of your return, or have you applied for an ITIN by then?
- **Encoded (Bool):** helper "Your entry, if the answer is yes" > 0 (a count)
- Expr: `{"gt":["household.taxpayer_tin_count",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [i1040gi] p. 19, Step 5, question 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.taxpayer_work_ssn_count`

- **Authored helper label:** Your entry, if the answer is yes
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "Whose entry is this, yours or your spouse's?" = 'taxpayer' and helper "Do you have an SSN valid for employment issued before the due date of your return?" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"all":[{"eq":["person.role",{"const":"taxpayer"}],"op":"test"},{"eq":["person.work_ssn",{"const":true}],"op":"test"}],"op":"test"}}`
- Cite: [i1040gi] p. 18, Step 3, question 4 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.taxpayer_work_ssn`

- **Authored helper label:** Do you have an SSN valid for employment issued before the due date of your return?
- **Encoded (Bool):** helper "Your entry, if the answer is yes" > 0 (a count)
- Expr: `{"gt":["household.taxpayer_work_ssn_count",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [i1040gi] p. 18, Step 3, question 4 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.home_cost`

- **Authored helper label:** Did you pay over half the cost of keeping up your home for 2025?
- **Encoded (Bool):** Input — Did you pay over half the cost of keeping up your home for 2025?
- Expr: `{"op":"input","source":"Did you pay over half the cost of keeping up your home for 2025?"}`
- Cite: [i1040gi] p. 14, Head of Household, Test 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.unmarried`

- **Authored helper label:** Were you unmarried, or considered unmarried under the head of household rules, at the end of 2025?
- **Encoded (Bool):** Input — Were you unmarried, or considered unmarried under the head of household rules, at the end of 2025?
- Expr: `{"op":"input","source":"Were you unmarried, or considered unmarried under the head of household rules, at the end of 2025?"}`
- Cite: [i1040gi] p. 14, Head of Household, "You are considered unmarried for this purpose if any of the following applies" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.test1_persons`

- **Authored helper label:** Number of parents who qualify you under Test 1
- **Encoded (Count):** Add dependent.one over every confirmed dependent entry for which helper "Qualifies you for head of household under Test 1 through a parent who does not live with you (a parent who lives with you qualifies you through Test 2)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"dependent","field":"dependent.one","op":"sum_over","where":{"eq":["dependent.hoh_test1",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 14, Head of Household, Test 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.test2_persons`

- **Authored helper label:** Number of persons who qualify you under Test 2
- **Encoded (Count):** Add dependent.one over every confirmed dependent entry for which helper "A Test 2 person who lived with you more than half the year (the home-cost condition of Test 2 is tested on the household form)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"dependent","field":"dependent.one","op":"sum_over","where":{"eq":["dependent.hoh_test2",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 14, Head of Household, Test 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.test1_met`

- **Authored helper label:** Test 1 met
- **Encoded (Bool):** helper "Number of parents who qualify you under Test 1" > 0 (a count)
- Expr: `{"gt":["household.test1_persons",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [i1040gi] p. 14, Head of Household, Test 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.test2_met`

- **Authored helper label:** Test 2 met, having paid over half the cost of keeping up your own home
- **Encoded (Bool):** helper "Did you pay over half the cost of keeping up your home for 2025?" = true and helper "Number of persons who qualify you under Test 2" > 0 (a count)
- Expr: `{"all":[{"eq":["household.home_cost",{"const":true}],"op":"test"},{"gt":["household.test2_persons",{"const":0,"type":"Count"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 14, Head of Household, Test 2, "You paid over half the cost of keeping up a home in which you lived and in which one of the following also lived for more than half of the year" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.hoh_eligible`

- **Authored helper label:** Unmarried or considered unmarried, and Test 1 or Test 2 applies
- **Encoded (Bool):** helper "Were you unmarried, or considered unmarried under the head of household rules, at the end of 2025?" = true and (helper "Test 1 met" = true or helper "Test 2 met, having paid over half the cost of keeping up your own home" = true)
- Expr: `{"all":[{"eq":["household.unmarried",{"const":true}],"op":"test"},{"any":[{"eq":["household.test1_met",{"const":true}],"op":"test"},{"eq":["household.test2_met",{"const":true}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 14, Head of Household, "Check the box only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `household.hoh_fails`

- **Authored helper label:** Head of household checked without meeting its tests
- **Encoded (Bool):** f1040 line Filing Status = 'hoh' and helper "Unmarried or considered unmarried, and Test 1 or Test 2 applies" = false
- Expr: `{"all":[{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},{"eq":["household.hoh_eligible",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 14, Head of Household (2025; printed date 2026-02-25; sha256 482e9c48)
