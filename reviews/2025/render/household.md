# Render comparison — household

The rendered English of every printed line of `Household facts for dependents and head of household` (`rendered/2025/household.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-19 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 945fa693bd212101627e7aef9616e2035b6a380cf63a650767e73ec0b617df9b |
| subject sha256 | e0df7702060c20acc80f02f5843f03660a80f27edad5ca2ff095dd0f9150daeb |
| lines judged | 28 |
| match / mismatch / unclear / missing | 26 / 2 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i8889 | 2025 | 4, 7 | cited pages | bfbdc8bbe0b85d088325243f176d4c8261b0ca2428f75f4f41e4a339ecb5495c | 4, 7 | 533a42f870f12dc6c1984815eae1a4bf59d6fde28cbc909d9a4e76ff41c6eda7 |
| i1040gi | 2025; printed date 2026-02-25 | 14, 17, 18, 40 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 17, 18, 40 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### persons — Number of people on the return (you, and your spouse if filing jointly)
Status: **MATCH**

Model: This counts every person entry. roster_ok limits the roster to you, plus your spouse only when filing jointly, which matches the IRS phrase "you, and your spouse if filing jointly".

### taxpayers — Number of entries for you
Status: **MATCH**

Model: This is a bookkeeping count of entries marked as yours. No IRS line conflicts with it, and it is what roster_ok needs to check that there is exactly one taxpayer.

### spouses — Number of entries for your spouse
Status: **MATCH**

Model: This is a bookkeeping count of entries marked as your spouse's. It lets roster_ok confirm that a spouse is on the return only for the "Married filing jointly" status.

### roster_ok — One entry for you, and one for your spouse exactly when filing jointly
Status: **MATCH**

Model: Form 1040 names the spouse as a joint filer only on a joint return ("If joint return, spouse's first name"). So the check is right: one taxpayer, plus one spouse if MFJ and none otherwise.

### roster_bad — The people entered do not match the filing status
Status: **MATCH**

Model: This is simply the negation of roster_ok.

### hsa_people — Number of people on the return with a Form 8889
Status: **MATCH**

Model: The Form 8889 instructions say "If married filing jointly and both you and your spouse have HSAs, complete a separate Form 8889 for each of you". Counting the people who have at least one Form 8889 fits that.

### hsa_both — You and your spouse each have a Form 8889
Status: **MATCH**

Model: A count of 2 means both spouses have a Form 8889, which is what "Combine the amounts on line 13 of both Forms 8889" assumes.

### hsa_split_count — Number of Forms 8889 using the spouse rule of line 6
Status: **MATCH**

Model: This adds up each person's flag for using the line 6 spouse rule ("Spouses who have separate HSAs and had family coverage... use the following rules to figure the amount on line 6"). That is consistent with the label.

### hsa_agreed_count — Number of Forms 8889 using an agreed allocation
Status: **MATCH**

Model: This counts the Forms 8889 that use the line 6 option "unless you both agree on a different allocation (such as allocating nothing to one spouse)". That is consistent with the label.

### hsa_step1_sum — Both spouses Step 1 limits added together
Status: **MATCH**

Model: This adds each spouse's refigured limit from line 6 Step 1 ("Refigure the contribution limit that would have been entered on line 5..."), as the label says.

### hsa_share_sum — Both spouses parts of the Step 1 limit added together
Status: **MATCH**

Model: This adds each spouse's share from line 6 Step 2 ("Divide the refigured contribution limit from Step 1 equally between you and your spouse, unless you both agree on a different allocation"), as the label says.

### work_ssn_count — Number of people on the return with an SSN valid for employment
Status: **MATCH**

Model: This counts people with an SSN "valid for employment and issued before the due date of your return (including extensions)", which is the IRS definition of a valid SSN.

### any_work_ssn — You, or your spouse if filing jointly, have an SSN valid for employment
Status: **MATCH**

Model: Requiring at least one valid SSN matches "If you are filing a joint return, only one spouse is required to have a valid SSN to be eligible for the CTC and ACTC."

### all_work_ssn — You, and your spouse if filing jointly, have SSNs valid for employment
Status: **MATCH**

Model: Requiring everyone on the return to have a valid SSN matches the EIC test "Do you, and your spouse if filing a joint return, have a social security number... that allows you to work".

### tin_count — Number of people on the return with an SSN or ITIN
Status: **MISMATCH**

Restated: Add person.one over every confirmed person entry for which helper "Do you have an SSN or ITIN issued on or before the due date of your return, or have you applied for an ITIN by then?" = true, within the current person when parent-bound. An unanswered roster is unknown.

Model: The per-person test counts someone who has only applied for an ITIN by the due date. For you and your spouse, the IRS text requires an issued number: "you, and your spouse if filing jointly, must have either an SSN or ITIN issued on or before the due date of your 2025 return". The "applying for an ITIN" allowance appears only for the child, in Step 3.

Ruling: project retained; the question is now split. Step 5, question 1 (the credit for other dependents) asks whether you, and your spouse if filing jointly, have an SSN or ITIN issued on or before the due date and adds '(Answer "Yes" if you are applying for an ITIN on or before the return due date (including extensions).)' (i1040gi p. 19). person.tin now asks only for an issued number and person.itin_applied for an application; this count, for the credit for other dependents, accepts either.

### all_tin — You, and your spouse if filing jointly, have an SSN or ITIN
Status: **MATCH**

Model: Requiring everyone on the return to qualify follows "you, and your spouse if filing jointly, must have either an SSN or ITIN". The extra allowance for an ITIN application comes in through tin_count.

### id_count — Number of people on the return with an SSN valid for employment or an SSN or ITIN
Status: **MISMATCH**

Restated: Add person.one over every confirmed person entry for which (helper "Do you have an SSN valid for employment issued before the due date of your return?" = true or helper "Do you have an SSN or ITIN issued on or before the due date of your return, or have you applied for an ITIN by then?" = true), within the current person when parent-bound. An unanswered roster is unknown.

Model: The second test counts someone who has only applied for an ITIN. For the spouse without a valid SSN, the IRS text says "The other spouse must have either an SSN or ITIN, and it must have been issued on or before the due date of the return".

Ruling: second transcription right; data fixed. For the child tax credit 'The other spouse must have either an SSN or ITIN, and it must have been issued on or before the due date of the return' (i1040gi p. 17, Before you begin); the count now reads person.tin, which asks only for an issued number, and no longer an application for an ITIN (person.itin_applied). BUG-0049.

### ctc_ssn — Child tax credit identification: you, or your spouse if filing jointly, have an SSN valid 
Status: **MATCH**

Model: The structure matches "only one spouse is required to have a valid SSN... The other spouse must have either an SSN or ITIN": at least one valid SSN, and everyone else has an SSN or ITIN. The extra allowance for an ITIN application comes in through id_count.

### taxpayer_work_ssn_count — Your entry, if the answer is yes
Status: **MATCH**

Model: This counts your own entry when it has an SSN valid for employment issued before the due date, which is the IRS valid-SSN test applied to you.

### taxpayer_work_ssn — Do you have an SSN valid for employment issued before the due date of your return?
Status: **MATCH**

Model: A count above zero means you have a valid SSN, matching "you must have a valid SSN, which means it must be valid for employment and issued before the due date of your return".

### home_cost — Did you pay over half the cost of keeping up your home for 2025?
Status: **MATCH**

Model: This is an input. It is used only for Test 2: "You paid over half the cost of keeping up a home in which you lived".

### unmarried — Were you unmarried, or considered unmarried under the head of household rules, at the end 
Status: **MATCH**

Model: This is an input. It matches "Check the 'Head of household' box only if you are unmarried (or considered unmarried)", and the instructions list the cases that count as considered unmarried.

### test1_persons — Number of parents who qualify you under Test 1
Status: **MATCH**

Model: Test 1 covers a parent's home that you paid over half the cost of keeping up, where the parent is your dependent other than under a multiple support agreement. The text says "Your parent didn't have to live with you." A parent who lives with you all year and meets Test 1 also meets Test 2, so sending that parent to Test 2 does not change the result.

### test2_persons — Number of persons who qualify you under Test 2
Status: **MATCH**

Model: This counts persons who qualify under Test 2 and "also lived for more than half of the year". The home-cost condition is tested separately in test2_met.

### test1_met — Test 1 met
Status: **MATCH**

Model: Test 1 is met if at least one parent qualifies.

### test2_met — Test 2 met, having paid over half the cost of keeping up your own home
Status: **MATCH**

Model: This matches Test 2: "You paid over half the cost of keeping up a home in which you lived and in which one of the following also lived for more than half of the year".

### hoh_eligible — Unmarried or considered unmarried, and Test 1 or Test 2 applies
Status: **MATCH**

Model: This matches "Check the 'Head of household' box only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies."

### hoh_fails — Head of household checked without meeting its tests
Status: **MATCH**

Model: This flags a return where Head of household is checked but hoh_eligible is false, which is the case the IRS text rules out.

## Raw response

```yaml
```yaml
lines:
  - key: "persons"
    status: MATCH
    reason: "This counts every person entry. roster_ok limits the roster to you, plus your spouse only when filing jointly, which matches the IRS phrase \"you, and your spouse if filing jointly\"."
  - key: "taxpayers"
    status: MATCH
    reason: "This is a bookkeeping count of entries marked as yours. No IRS line conflicts with it, and it is what roster_ok needs to check that there is exactly one taxpayer."
  - key: "spouses"
    status: MATCH
    reason: "This is a bookkeeping count of entries marked as your spouse's. It lets roster_ok confirm that a spouse is on the return only for the \"Married filing jointly\" status."
  - key: "roster_ok"
    status: MATCH
    reason: "Form 1040 names the spouse as a joint filer only on a joint return (\"If joint return, spouse's first name\"). So the check is right: one taxpayer, plus one spouse if MFJ and none otherwise."
  - key: "roster_bad"
    status: MATCH
    reason: "This is simply the negation of roster_ok."
  - key: "hsa_people"
    status: MATCH
    reason: "The Form 8889 instructions say \"If married filing jointly and both you and your spouse have HSAs, complete a separate Form 8889 for each of you\". Counting the people who have at least one Form 8889 fits that."
  - key: "hsa_both"
    status: MATCH
    reason: "A count of 2 means both spouses have a Form 8889, which is what \"Combine the amounts on line 13 of both Forms 8889\" assumes."
  - key: "hsa_split_count"
    status: MATCH
    reason: "This adds up each person's flag for using the line 6 spouse rule (\"Spouses who have separate HSAs and had family coverage... use the following rules to figure the amount on line 6\"). That is consistent with the label."
  - key: "hsa_agreed_count"
    status: MATCH
    reason: "This counts the Forms 8889 that use the line 6 option \"unless you both agree on a different allocation (such as allocating nothing to one spouse)\". That is consistent with the label."
  - key: "hsa_step1_sum"
    status: MATCH
    reason: "This adds each spouse's refigured limit from line 6 Step 1 (\"Refigure the contribution limit that would have been entered on line 5...\"), as the label says."
  - key: "hsa_share_sum"
    status: MATCH
    reason: "This adds each spouse's share from line 6 Step 2 (\"Divide the refigured contribution limit from Step 1 equally between you and your spouse, unless you both agree on a different allocation\"), as the label says."
  - key: "work_ssn_count"
    status: MATCH
    reason: "This counts people with an SSN \"valid for employment and issued before the due date of your return (including extensions)\", which is the IRS definition of a valid SSN."
  - key: "any_work_ssn"
    status: MATCH
    reason: "Requiring at least one valid SSN matches \"If you are filing a joint return, only one spouse is required to have a valid SSN to be eligible for the CTC and ACTC.\""
  - key: "all_work_ssn"
    status: MATCH
    reason: "Requiring everyone on the return to have a valid SSN matches the EIC test \"Do you, and your spouse if filing a joint return, have a social security number... that allows you to work\"."
  - key: "tin_count"
    status: MISMATCH
    reason: "The per-person test counts someone who has only applied for an ITIN by the due date. For you and your spouse, the IRS text requires an issued number: \"you, and your spouse if filing jointly, must have either an SSN or ITIN issued on or before the due date of your 2025 return\". The \"applying for an ITIN\" allowance appears only for the child, in Step 3."
  - key: "all_tin"
    status: MATCH
    reason: "Requiring everyone on the return to qualify follows \"you, and your spouse if filing jointly, must have either an SSN or ITIN\". The extra allowance for an ITIN application comes in through tin_count."
  - key: "id_count"
    status: MISMATCH
    reason: "The second test counts someone who has only applied for an ITIN. For the spouse without a valid SSN, the IRS text says \"The other spouse must have either an SSN or ITIN, and it must have been issued on or before the due date of the return\"."
  - key: "ctc_ssn"
    status: MATCH
    reason: "The structure matches \"only one spouse is required to have a valid SSN... The other spouse must have either an SSN or ITIN\": at least one valid SSN, and everyone else has an SSN or ITIN. The extra allowance for an ITIN application comes in through id_count."
  - key: "taxpayer_work_ssn_count"
    status: MATCH
    reason: "This counts your own entry when it has an SSN valid for employment issued before the due date, which is the IRS valid-SSN test applied to you."
  - key: "taxpayer_work_ssn"
    status: MATCH
    reason: "A count above zero means you have a valid SSN, matching \"you must have a valid SSN, which means it must be valid for employment and issued before the due date of your return\"."
  - key: "home_cost"
    status: MATCH
    reason: "This is an input. It is used only for Test 2: \"You paid over half the cost of keeping up a home in which you lived\"."
  - key: "unmarried"
    status: MATCH
    reason: "This is an input. It matches \"Check the 'Head of household' box only if you are unmarried (or considered unmarried)\", and the instructions list the cases that count as considered unmarried."
  - key: "test1_persons"
    status: MATCH
    reason: "Test 1 covers a parent's home that you paid over half the cost of keeping up, where the parent is your dependent other than under a multiple support agreement. The text says \"Your parent didn't have to live with you.\" A parent who lives with you all year and meets Test 1 also meets Test 2, so sending that parent to Test 2 does not change the result."
  - key: "test2_persons"
    status: MATCH
    reason: "This counts persons who qualify under Test 2 and \"also lived for more than half of the year\". The home-cost condition is tested separately in test2_met."
  - key: "test1_met"
    status: MATCH
    reason: "Test 1 is met if at least one parent qualifies."
  - key: "test2_met"
    status: MATCH
    reason: "This matches Test 2: \"You paid over half the cost of keeping up a home in which you lived and in which one of the following also lived for more than half of the year\"."
  - key: "hoh_eligible"
    status: MATCH
    reason: "This matches \"Check the 'Head of household' box only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies.\""
  - key: "hoh_fails"
    status: MATCH
    reason: "This flags a return where Head of household is checked but hoh_eligible is false, which is the case the IRS text rules out."
```
```
