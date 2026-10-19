# Render comparison — person

The rendered English of every printed line of `Excess Social Security credit — separately per person` (`rendered/2025/person.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-19 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | faae7e4b11d5dab3f25e8fb2ccf4535dcd251fa25c534e92b46ffe0c898bea58 |
| lines judged | 10 |
| match / mismatch / unclear / missing | 10 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040gi | 2025; printed date 2026-02-25 | 18, 19, 41, 93, 104, 108, 110, 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 18, 19, 41, 93, 104, 110, 117 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i8889 | 2025 | 3, 4, 7 | cited pages | bfbdc8bbe0b85d088325243f176d4c8261b0ca2428f75f4f41e4a339ecb5495c | 3, 4, 7 | 533a42f870f12dc6c1984815eae1a4bf59d6fde28cbc909d9a4e76ff41c6eda7 |
| iw2w3 | 2025; printed date 2025-02-19 | 12, 13, 18 | cited pages | 27ad850a44d58d9186afcccb33b8a32f4747911e2b1b3138de515f44d4de33f3 | 12, 13, 18 | 3876738db222e8abe6103f29d8a8654a3139b9896f97e325d50e80b87ed5b26a |
| f8959 | 2025; created 2025-04-30 | 1 | whole document | 92ba0b667ac9963d648a57a3f08893be1a57e5540a4957668fabdc79a5c12af9 | - | cfcb0cc50de26876183ca7956c570cc3d19f0401875794de2f0c86a5cf87d60c |
| i8959 | 2025; printed date 2025-08-07 | 1, 2, 3, 4 | whole document | 0ec9603864196115a05c89675c3cf1ea20ce0384fb59e2195b2dbd8c65d3e85d | 1, 2, 3, 4 | 926d666edb486650f74da8863ef35ce5a9fe82c240719196138fdc8d40bf40df |

## Lines

### rrta — Do any wage statements report railroad retirement compensation or taxes (W-2 box 14), or d
Status: **MATCH**

Model: The line 11 text covers 'social security or tier 1 railroad retirement (RRTA) tax' and says excess tier 2 RRTA tax goes on Form 843. The W-2/W-3 instructions put RRTA compensation and taxes in W-2 box 14, and the 8959 instructions name Form CT-2 for employee representatives, so this input properly gates the RRTA path the program declines.

### employers — Total w2.one for this person
Status: **MATCH**

Model: The text conditions the credit on having 'more than one employer for 2025' and says to figure it 'separately for you and your spouse'. A per-person count of W-2 entries matches this if each entry is a distinct employer; the text does not cover one employer issuing several W-2s.

### overcount — Number of employers that withheld more than the limit
Status: **MATCH**

Model: This counts, per person, the employers whose withholding exceeds $10,918.20, which serves the text's rule 'if any one employer withheld more than $10,918.20, you can't claim the excess on your return.' Like 'employers', it treats each W-2 entry as one employer.

### over — Any employer withheld more than the limit
Status: **MATCH**

Model: This is true when at least one employer withheld more than $10,918.20, which is the condition under which the text says 'you can't claim the excess on your return' and points to Form 843.

### wages — Total w2.wages for this person
Status: **MATCH**

Model: The text tests 'total wages of more than $176,100', figured separately per person. A per-person sum of W-2 wages is that total.

### withheld — Total w2.box4 for this person
Status: **MATCH**

Model: The credit is 'the amount withheld in excess of $10,918.20', and the W-2/W-3 instructions say box 4 is 'Social security tax withheld'. A per-person sum of box 4 is the total social security tax withheld; RRTA is refused separately.

### eligible — More than one employer and total social security wages over $176,100
Status: **MATCH**

Model: This matches the text's condition 'had more than one employer for 2025 and total wages of more than $176,100'.

### excess — Withholding above $10,918.20, if any
Status: **MATCH**

Model: The text allows 'a credit on this line for the amount withheld in excess of $10,918.20'. Total withheld minus $10,918.20, floored at zero, computes that.

### zero — No excess credit
Status: **MATCH**

Model: This is a constant $0 used as the credit when the eligibility conditions are not met, which agrees with the text that the credit applies only to filers meeting them.

### credit — Excess social security tax withheld, figured separately for this person
Status: **MATCH**

Model: The line gives the per-person excess when eligible and $0 otherwise, as the text requires ('Figure this amount separately for you and your spouse'). The refusals properly exclude the RRTA cases (tier 2 'use Form 843') and the case where 'any one employer withheld more than $10,918.20' ('The employer should adjust the tax... file a claim for refund using Form 843').

## Raw response

```yaml
```yaml
lines:
  - key: "rrta"
    status: MATCH
    reason: "The line 11 text covers 'social security or tier 1 railroad retirement (RRTA) tax' and says excess tier 2 RRTA tax goes on Form 843. The W-2/W-3 instructions put RRTA compensation and taxes in W-2 box 14, and the 8959 instructions name Form CT-2 for employee representatives, so this input properly gates the RRTA path the program declines."
  - key: "employers"
    status: MATCH
    reason: "The text conditions the credit on having 'more than one employer for 2025' and says to figure it 'separately for you and your spouse'. A per-person count of W-2 entries matches this if each entry is a distinct employer; the text does not cover one employer issuing several W-2s."
  - key: "overcount"
    status: MATCH
    reason: "This counts, per person, the employers whose withholding exceeds $10,918.20, which serves the text's rule 'if any one employer withheld more than $10,918.20, you can't claim the excess on your return.' Like 'employers', it treats each W-2 entry as one employer."
  - key: "over"
    status: MATCH
    reason: "This is true when at least one employer withheld more than $10,918.20, which is the condition under which the text says 'you can't claim the excess on your return' and points to Form 843."
  - key: "wages"
    status: MATCH
    reason: "The text tests 'total wages of more than $176,100', figured separately per person. A per-person sum of W-2 wages is that total."
  - key: "withheld"
    status: MATCH
    reason: "The credit is 'the amount withheld in excess of $10,918.20', and the W-2/W-3 instructions say box 4 is 'Social security tax withheld'. A per-person sum of box 4 is the total social security tax withheld; RRTA is refused separately."
  - key: "eligible"
    status: MATCH
    reason: "This matches the text's condition 'had more than one employer for 2025 and total wages of more than $176,100'."
  - key: "excess"
    status: MATCH
    reason: "The text allows 'a credit on this line for the amount withheld in excess of $10,918.20'. Total withheld minus $10,918.20, floored at zero, computes that."
  - key: "zero"
    status: MATCH
    reason: "This is a constant $0 used as the credit when the eligibility conditions are not met, which agrees with the text that the credit applies only to filers meeting them."
  - key: "credit"
    status: MATCH
    reason: "The line gives the per-person excess when eligible and $0 otherwise, as the text requires ('Figure this amount separately for you and your spouse'). The refusals properly exclude the RRTA cases (tier 2 'use Form 843') and the case where 'any one employer withheld more than $10,918.20' ('The employer should adjust the tax... file a claim for refund using Form 843')."
```
```
