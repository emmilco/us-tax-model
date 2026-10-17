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
| iw2w3 | 2025; printed date 2025-02-19 | 12, 13, 18 | cited pages | 27ad850a44d58d9186afcccb33b8a32f4747911e2b1b3138de515f44d4de33f3 | 12, 13, 18 | 041478fca3ac83c1ab32e205578acf77d55143fd6c318cda2fbe6e33bf77e593 |
| i1040gi | 2025; printed date 2026-02-25 | 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 117 | 816ff8c5ed82d0349bfa79ae008e9b4492c04005a8702145dcd8cd0139eacc47 |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | d0173256c777b69a079b5239cb98fe29d3353314f410cdc88356a94a2182d702 |
| f8959 | 2025; created 2025-04-30 | 1 | whole document | 92ba0b667ac9963d648a57a3f08893be1a57e5540a4957668fabdc79a5c12af9 | - | cfcb0cc50de26876183ca7956c570cc3d19f0401875794de2f0c86a5cf87d60c |
| i8959 | 2025; printed date 2025-08-07 | 1, 2, 3, 4 | whole document | 0ec9603864196115a05c89675c3cf1ea20ce0384fb59e2195b2dbd8c65d3e85d | 1, 2, 3, 4 | 926d666edb486650f74da8863ef35ce5a9fe82c240719196138fdc8d40bf40df |

## Lines

### rrta — Do any wage statements report railroad retirement compensation or taxes (W-2 box 14)?
Status: **MATCH**

Model: W-2 instructions say RRTA compensation and Tier 1/Tier 2 taxes are reported in box 14, so asking about box 14 identifies the RRTA case. The program then refuses that case.

### employers — Total w2.one for this person
Status: **UNCLEAR**

Restated: Add w2.one over every confirmed w2 entry, within the current person when parent-bound. An unanswered roster is unknown.

Model: The IRS test is whether you 'had more than one employer.' The program counts W-2 entries per person instead. The text given does not say each employer issues exactly one W-2, so a count of W-2s may not equal a count of employers.

Ruling: representation; project retained. The W-2 collection is keyed by employer, and repeated forms from one employer are consolidated into one entry ("Keyed by employer within person; consolidate repeated forms for the same employer explicitly", forms/2025/w2.yaml collection note), so the count of entries is the count of employers that "had more than one employer for 2025" (i1040gi p. 117) asks for. No change to the data.

### overcount — Number of employers that withheld more than the limit
Status: **MATCH**

Model: This counts W-2s where the employer withheld more than $10,918.20, matching 'if any one employer withheld more than $10,918.20,' figured per person.

### over — Any employer withheld more than the limit
Status: **MATCH**

Model: A count above zero means 'any one employer withheld more than $10,918.20.'

### wages — Total w2.wages for this person
Status: **UNCLEAR**

Restated: Add w2.wages over every confirmed w2 entry, within the current person when parent-bound. An unanswered roster is unknown.

Model: The IRS condition is 'total wages of more than $176,100,' figured separately per person. The text does not say which W-2 box supplies 'wages' (box 1 or box 3), and the restatement's w2.wages does not identify the box either.

Ruling: representation; project retained. The $176,100 test is on social security wages, the wage base above which no social security tax is withheld (i1040gi p. 117, line 11; $10,918.20 is 6.2% of $176,100), so `w2.wages` sums Form W-2 box 3 (social security wages) and box 7 (social security tips), the amounts the tax was withheld on. No change to the data.

### withheld — Total w2.box4 for this person
Status: **MATCH**

Model: The instructions say box 4 shows the employee social security tax withheld. Summing box 4 per person gives the 'amount withheld' compared against $10,918.20, with the RRTA Tier 1 portion excluded by refusal.

### eligible — More than one employer and total social security wages over $176,100
Status: **MATCH**

Model: This matches 'had more than one employer for 2025 and total wages of more than $176,100,' given the employers and wages lines it relies on.

### excess — Withholding above $10,918.20, if any
Status: **MATCH**

Model: This matches 'a credit on this line for the amount withheld in excess of $10,918.20,' floored at zero.

### zero — No excess credit
Status: **MATCH**

Model: A constant zero for the ineligible branch; no credit applies when the condition is not met.

### credit — Excess social security tax withheld, figured separately for this person
Status: **MATCH**

Model: The credit is the excess when the person qualifies and zero otherwise. The refusals name the excluded cases: RRTA ('You can't claim a refund for excess tier 2 RRTA tax on Form 1040... use Form 843') and over-withholding by one employer ('you can't claim the excess on your return... file a claim for refund using Form 843').

## Raw response

```yaml
```yaml
lines:
  - key: "rrta"
    status: MATCH
    reason: "W-2 instructions say RRTA compensation and Tier 1/Tier 2 taxes are reported in box 14, so asking about box 14 identifies the RRTA case. The program then refuses that case."
  - key: "employers"
    status: UNCLEAR
    reason: "The IRS test is whether you 'had more than one employer.' The program counts W-2 entries per person instead. The text given does not say each employer issues exactly one W-2, so a count of W-2s may not equal a count of employers."
  - key: "overcount"
    status: MATCH
    reason: "This counts W-2s where the employer withheld more than $10,918.20, matching 'if any one employer withheld more than $10,918.20,' figured per person."
  - key: "over"
    status: MATCH
    reason: "A count above zero means 'any one employer withheld more than $10,918.20.'"
  - key: "wages"
    status: UNCLEAR
    reason: "The IRS condition is 'total wages of more than $176,100,' figured separately per person. The text does not say which W-2 box supplies 'wages' (box 1 or box 3), and the restatement's w2.wages does not identify the box either."
  - key: "withheld"
    status: MATCH
    reason: "The instructions say box 4 shows the employee social security tax withheld. Summing box 4 per person gives the 'amount withheld' compared against $10,918.20, with the RRTA Tier 1 portion excluded by refusal."
  - key: "eligible"
    status: MATCH
    reason: "This matches 'had more than one employer for 2025 and total wages of more than $176,100,' given the employers and wages lines it relies on."
  - key: "excess"
    status: MATCH
    reason: "This matches 'a credit on this line for the amount withheld in excess of $10,918.20,' floored at zero."
  - key: "zero"
    status: MATCH
    reason: "A constant zero for the ineligible branch; no credit applies when the condition is not met."
  - key: "credit"
    status: MATCH
    reason: "The credit is the excess when the person qualifies and zero otherwise. The refusals name the excluded cases: RRTA ('You can't claim a refund for excess tier 2 RRTA tax on Form 1040... use Form 843') and over-withholding by one employer ('you can't claim the excess on your return... file a claim for refund using Form 843')."
```
```
