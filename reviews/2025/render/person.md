# Render comparison — person

The rendered English of every printed line of `Excess Social Security credit — separately per person` (`rendered/2025/person.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | ce904f54eedc7d650f1c9efe47506c6b12b586a55d2ca10449a5c11372423ebb |
| lines judged | 10 |
| match / mismatch / unclear / missing | 8 / 0 / 2 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| iw2w3 | 2025; printed date 2025-02-19 | 12, 13, 18 | cited pages | 27ad850a44d58d9186afcccb33b8a32f4747911e2b1b3138de515f44d4de33f3 | 12, 13, 18 | 3876738db222e8abe6103f29d8a8654a3139b9896f97e325d50e80b87ed5b26a |
| i1040gi | 2025; printed date 2026-02-25 | 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 117 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| f8959 | 2025; created 2025-04-30 | 1 | whole document | 92ba0b667ac9963d648a57a3f08893be1a57e5540a4957668fabdc79a5c12af9 | - | cfcb0cc50de26876183ca7956c570cc3d19f0401875794de2f0c86a5cf87d60c |
| i8959 | 2025; printed date 2025-08-07 | 1, 2, 3, 4 | whole document | 0ec9603864196115a05c89675c3cf1ea20ce0384fb59e2195b2dbd8c65d3e85d | 1, 2, 3, 4 | 926d666edb486650f74da8863ef35ce5a9fe82c240719196138fdc8d40bf40df |

## Lines

### rrta — Do any wage statements report railroad retirement compensation or taxes (W-2 box 14)?
Status: **MATCH**

Model: The W-2/W-3 instructions say railroad employers 'Use Form W-2, box 14, to report total RRTA compensation, Tier 1, Tier 2...'. A yes/no input on whether box 14 reports RRTA amounts is a fair gate for the RRTA refusal on the credit line.

### employers — Total w2.one for this person
Status: **UNCLEAR**

Restated: Add w2.one over every confirmed w2 entry, within the current person when parent-bound. An unanswered roster is unknown.

Model: The line 11 test is 'had more than one employer for 2025', but the program counts W-2 entries. The text does not say whether each W-2 is a distinct employer, so two W-2s from one employer could be miscounted.

Ruling: representation; project retained. The W-2 collection is keyed by employer, and repeated forms from one employer are consolidated into one entry ("Keyed by employer within person; consolidate repeated forms for the same employer explicitly", forms/2025/w2.yaml collection note), so the count of entries is the count of employers that "had more than one employer for 2025" (i1040gi p. 117) asks for. No change to the data.

### overcount — Number of employers that withheld more than the limit
Status: **MATCH**

Model: This tracks 'if any one employer withheld more than $10,918.20, you can't claim the excess on your return,' counted per person. The helper's label matches the IRS condition, though it is evaluated per W-2 entry rather than per distinct employer.

### over — Any employer withheld more than the limit
Status: **MATCH**

Model: A count above zero means at least one employer withheld more than $10,918.20, which is the IRS condition 'if any one employer withheld more than $10,918.20.'

### wages — Total w2.wages for this person
Status: **UNCLEAR**

Restated: Add w2.wages over every confirmed w2 entry, within the current person when parent-bound. An unanswered roster is unknown.

Model: The IRS text says only 'total wages of more than $176,100' and does not say which W-2 box is meant. The field w2.wages is not defined (box 1 vs. box 3/7), so the operand cannot be confirmed.

Ruling: representation; project retained. The $176,100 test is on social security wages, the wage base above which no social security tax is withheld (i1040gi p. 117, line 11; $10,918.20 is 6.2% of $176,100), so `w2.wages` sums Form W-2 box 3 (social security wages) and box 7 (social security tips), the amounts the tax was withheld on. No change to the data.

### withheld — Total w2.box4 for this person
Status: **MATCH**

Model: Summing W-2 box 4 ('Social security tax withheld') per person matches 'too much social security ... tax may have been withheld' and 'Figure this amount separately for you and your spouse.' The tier 1 RRTA portion is excluded by the RRTA refusal.

### eligible — More than one employer and total social security wages over $176,100
Status: **MATCH**

Model: This mirrors 'had more than one employer for 2025 and total wages of more than $176,100,' with both comparisons strict as in the text. It inherits the open questions on the employers and wages operands.

### excess — Withholding above $10,918.20, if any
Status: **MATCH**

Model: This matches 'You can take a credit on this line for the amount withheld in excess of $10,918.20', floored at zero.

### zero — No excess credit
Status: **MATCH**

Model: This is a constant zero used when the eligibility conditions in the line 11 instructions are not met.

### credit — Excess social security tax withheld, figured separately for this person
Status: **MATCH**

Model: The credit is the excess when the filer has more than one employer and wages above $176,100, and zero otherwise, figured 'separately for you and your spouse.' The refusals correctly exclude the cases the text routes elsewhere: 'If the employer doesn't adjust the overcollection, you can file a claim for refund using Form 843' and 'You can't claim a refund for excess tier 2 RRTA tax on Form 1040 ... Instead, use Form 843.'

## Raw response

```yaml
lines:
  - key: "rrta"
    status: MATCH
    reason: "The W-2/W-3 instructions say railroad employers 'Use Form W-2, box 14, to report total RRTA compensation, Tier 1, Tier 2...'. A yes/no input on whether box 14 reports RRTA amounts is a fair gate for the RRTA refusal on the credit line."
  - key: "employers"
    status: UNCLEAR
    reason: "The line 11 test is 'had more than one employer for 2025', but the program counts W-2 entries. The text does not say whether each W-2 is a distinct employer, so two W-2s from one employer could be miscounted."
  - key: "overcount"
    status: MATCH
    reason: "This tracks 'if any one employer withheld more than $10,918.20, you can't claim the excess on your return,' counted per person. The helper's label matches the IRS condition, though it is evaluated per W-2 entry rather than per distinct employer."
  - key: "over"
    status: MATCH
    reason: "A count above zero means at least one employer withheld more than $10,918.20, which is the IRS condition 'if any one employer withheld more than $10,918.20.'"
  - key: "wages"
    status: UNCLEAR
    reason: "The IRS text says only 'total wages of more than $176,100' and does not say which W-2 box is meant. The field w2.wages is not defined (box 1 vs. box 3/7), so the operand cannot be confirmed."
  - key: "withheld"
    status: MATCH
    reason: "Summing W-2 box 4 ('Social security tax withheld') per person matches 'too much social security ... tax may have been withheld' and 'Figure this amount separately for you and your spouse.' The tier 1 RRTA portion is excluded by the RRTA refusal."
  - key: "eligible"
    status: MATCH
    reason: "This mirrors 'had more than one employer for 2025 and total wages of more than $176,100,' with both comparisons strict as in the text. It inherits the open questions on the employers and wages operands."
  - key: "excess"
    status: MATCH
    reason: "This matches 'You can take a credit on this line for the amount withheld in excess of $10,918.20', floored at zero."
  - key: "zero"
    status: MATCH
    reason: "This is a constant zero used when the eligibility conditions in the line 11 instructions are not met."
  - key: "credit"
    status: MATCH
    reason: "The credit is the excess when the filer has more than one employer and wages above $176,100, and zero otherwise, figured 'separately for you and your spouse.' The refusals correctly exclude the cases the text routes elsewhere: 'If the employer doesn't adjust the overcollection, you can file a claim for refund using Form 843' and 'You can't claim a refund for excess tier 2 RRTA tax on Form 1040 ... Instead, use Form 843.'"
```
