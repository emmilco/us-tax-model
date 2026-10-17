# Render comparison — person

The rendered English of every printed line of `Excess Social Security credit — separately per person` (`rendered/2025/person.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 48cf2713a0cd541cbfb439190e53b4aa7488d5d7407a44a9722d88dad3d4eb57 |
| lines judged | 10 |
| match / mismatch / unclear / missing | 9 / 0 / 1 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 |
| --- | --- | --- | --- | --- |
| iw2w3 | 2025; printed date 2025-02-19 | 12, 13, 18 | cited pages | 27ad850a44d58d9186afcccb33b8a32f4747911e2b1b3138de515f44d4de33f3 |
| i1040gi | 2025; printed date 2026-02-25 | 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 |
| f8959 | 2025; created 2025-04-30 | 1 | whole document | 92ba0b667ac9963d648a57a3f08893be1a57e5540a4957668fabdc79a5c12af9 |
| i8959 | 2025; printed date 2025-08-07 | 1, 2, 3, 4 | whole document | 0ec9603864196115a05c89675c3cf1ea20ce0384fb59e2195b2dbd8c65d3e85d |

## Lines

### rrta — Do any wage statements report railroad retirement compensation or taxes (W-2 box 14)?
Status: **MATCH**

Model: The W-2/W-3 instructions say railroad employers 'Use Form W-2, box 14, to report total RRTA compensation, Tier 1, Tier 2, Medicare...' for employees covered by RRTA. A yes/no input on box 14 RRTA reporting identifies that case.

### employers — Total w2.one for this person
Status: **UNCLEAR**

Restated: Add w2.one over every confirmed w2 entry, within the current person when parent-bound. An unanswered roster is unknown.

Model: The IRS condition is 'had more than one employer for 2025', but the program counts confirmed W-2 entries. The text given does not say that each W-2 entry is a distinct employer, so it cannot confirm the count when one employer issues more than one W-2.

Ruling: representation; project retained. The W-2 collection is keyed by employer, and repeated forms from one employer are consolidated into one entry ("Keyed by employer within person; consolidate repeated forms for the same employer explicitly", forms/2025/w2.yaml collection note), so the count of entries is the count of employers that "had more than one employer for 2025" (i1040gi p. 117) asks for. No change to the data.

### overcount — Total w2.one for this person
Status: **MATCH**

Model: This counts the cases the text describes: 'if any one employer withheld more than $10,918.20'. The threshold matches. It inherits the same W-2-entry-versus-employer caveat as the employers line.

### over — Any employer withheld more than the limit
Status: **MATCH**

Model: A count above zero means 'any one employer withheld more than $10,918.20', which is the condition the text uses to bar the credit.

### wages — Total w2.wages for this person
Status: **MATCH**

Model: The text tests 'total wages of more than $176,100', figured separately per person. Adding each person's W-2 wages gives that total.

### withheld — Total w2.box4 for this person
Status: **MATCH**

Model: Box 4 is 'Social security tax withheld'. The credit is for 'the amount withheld in excess of $10,918.20'. Tier 1 RRTA withholding is left out, and the RRTA refusal covers that case.

### eligible — More than one employer and total social security wages over $176,100
Status: **MATCH**

Model: This matches 'had more than one employer for 2025 and total wages of more than $176,100'. It depends on the employers line, which is UNCLEAR.

### excess — Withholding above $10,918.20, if any
Status: **MATCH**

Model: This matches 'You can take a credit on this line for the amount withheld in excess of $10,918.20'. Flooring the result at zero is consistent with that.

### zero — No excess credit
Status: **MATCH**

Model: A zero value for the case where the eligibility condition is not met is consistent with the text, which allows a credit only when that condition holds.

### credit — Excess social security tax withheld, figured separately for this person
Status: **MATCH**

Model: The excess is credited only when eligible and is 'Figure[d] ... separately for you and your spouse'. The refusals name the excluded cases the text describes: the Tier 1 RRTA path, Tier 2 via Form 843, and 'if any one employer withheld more than $10,918.20, you can't claim the excess ... file a claim for refund using Form 843'.

## Raw response

```yaml
```yaml
lines:
  - key: "rrta"
    status: MATCH
    reason: "The W-2/W-3 instructions say railroad employers 'Use Form W-2, box 14, to report total RRTA compensation, Tier 1, Tier 2, Medicare...' for employees covered by RRTA. A yes/no input on box 14 RRTA reporting identifies that case."
  - key: "employers"
    status: UNCLEAR
    reason: "The IRS condition is 'had more than one employer for 2025', but the program counts confirmed W-2 entries. The text given does not say that each W-2 entry is a distinct employer, so it cannot confirm the count when one employer issues more than one W-2."
  - key: "overcount"
    status: MATCH
    reason: "This counts the cases the text describes: 'if any one employer withheld more than $10,918.20'. The threshold matches. It inherits the same W-2-entry-versus-employer caveat as the employers line."
  - key: "over"
    status: MATCH
    reason: "A count above zero means 'any one employer withheld more than $10,918.20', which is the condition the text uses to bar the credit."
  - key: "wages"
    status: MATCH
    reason: "The text tests 'total wages of more than $176,100', figured separately per person. Adding each person's W-2 wages gives that total."
  - key: "withheld"
    status: MATCH
    reason: "Box 4 is 'Social security tax withheld'. The credit is for 'the amount withheld in excess of $10,918.20'. Tier 1 RRTA withholding is left out, and the RRTA refusal covers that case."
  - key: "eligible"
    status: MATCH
    reason: "This matches 'had more than one employer for 2025 and total wages of more than $176,100'. It depends on the employers line, which is UNCLEAR."
  - key: "excess"
    status: MATCH
    reason: "This matches 'You can take a credit on this line for the amount withheld in excess of $10,918.20'. Flooring the result at zero is consistent with that."
  - key: "zero"
    status: MATCH
    reason: "A zero value for the case where the eligibility condition is not met is consistent with the text, which allows a credit only when that condition holds."
  - key: "credit"
    status: MATCH
    reason: "The excess is credited only when eligible and is 'Figure[d] ... separately for you and your spouse'. The refusals name the excluded cases the text describes: the Tier 1 RRTA path, Tier 2 via Form 843, and 'if any one employer withheld more than $10,918.20, you can't claim the excess ... file a claim for refund using Form 843'."
```
```
