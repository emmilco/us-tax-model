# Render comparison — ftc

The rendered English of every printed line of `Foreign tax credit — election without Form 1116` (`rendered/2025/ftc.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | bc33c9c64dd7a2b0d9557552783b91f451dcff0159e52f4bd6c1f3eb8bb69170 |
| lines judged | 11 |
| match / mismatch / unclear / missing | 9 / 0 / 2 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1116 | 2025; printed date 2025-12-23 | 1, 2 | cited pages | ca3e843c3bead1e7991566852707530b6bb7c2fd6008c1dbda0ac0bbd40c48ff | 1, 2 | 4e9025bfc8a73bcfd687c7f45cb1a037cd39e7445319bbc71c748e12db68a46a |

## Lines

### taxes — Total creditable foreign taxes after required reductions; generally Form 1099-INT box 6 an
Status: **MATCH**

Model: The text asks for 'your total creditable foreign taxes', reduced 'by any amount you would have entered on line 12 of Form 1116', and lists Forms 1099-INT and 1099-DIV as qualified payee statements. The specific box numbers (box 6, box 7) do not appear in the given text, but they are only guidance and do not change the input.

### all_passive — Was all foreign-source gross income passive category income under the small-tax election r
Status: **MATCH**

Model: This matches the condition 'All of your foreign source gross income was "passive category income"', which for this purpose also includes high-taxed income and certain export financing interest.

### statements — Were all foreign income and taxes reported on qualified payee statements?
Status: **MATCH**

Model: This matches the condition 'All the income and any foreign taxes paid on it were reported to you on a qualified payee statement.'

### eligible — Have creditability, holding-period, related-payment and required foreign-tax reduction rul
Status: **MATCH**

Model: The text says you must still apply 'the general rules for determining whether a tax is creditable' and 'reduce the taxes available for credit by any amount you would have entered on line 12'. Holding-period and related-payment rules are among the Foreign Taxes Not Eligible items the text cites.

### elect — Elect the credit without Form 1116, with no carryover to or from this election year?
Status: **MATCH**

Model: The credit is described as an election, and with it you 'can't carry over to or from any other year any foreign taxes paid or accrued in a tax year to which the election applies'.

### limit — Year parameter ftc.limit
Status: **MATCH**

Model: The text says 'aren't more than $300 ($600 if married filing a joint return)'. Only MFJ gets $600, so $300 for single, MFS, HOH and QSS is consistent.

### zero — Year parameter sales.zero
Status: **MATCH**

Model: This is a $0 constant used when there are no foreign taxes, so no credit arises. It is consistent with the text.

### has_tax — Positive foreign taxes
Status: **MATCH**

Model: This tests whether the foreign taxes exceed zero. It is a simple predicate on the input and does not conflict with the text.

### needs1116 — Fails a condition of the election
Status: **MATCH**

Model: The election 'is available only if you meet all of the following conditions': passive income, qualified payee statements, and taxes not over $300/$600. The creditability and reduction rules still apply, and the filer must actually elect. Failing any of these is correctly treated as needing Form 1116. The estate/trust exclusion is outside the individual scope.

### limited — Smaller of ftc.taxes, f1040.line16
Status: **UNCLEAR**

Restated: Enter the smaller of helper "Total creditable foreign taxes after required reductions; generally Form 1099-INT box 6 and Form 1099-DIV box 7" or f1040 line 16.

Model: The text says to enter 'the smaller of (a) your total foreign tax, or (b) your regular tax. See the instructions for line 20, later, for how to figure your regular tax.' Those line 20 instructions are not provided, so it cannot be confirmed that Form 1040 line 16 equals 'regular tax' for this purpose.

Ruling: representation; project retained. Regular tax for the election is "your total U.S. income tax against which the credit is allowed (regular tax liability, as defined in section 26(b)(1))", excluding the net investment income tax (i1116 p. 25, line 20), which on the return in this slice is Form 1040 line 16: the additional line-16 taxes are refused by `scope.other_line16` and the net investment income and additional Medicare taxes sit on Schedule 2, after line 16. No change to the data.

### credit — Credit is the smaller of creditable foreign tax and regular income tax; zero if no foreign
Status: **UNCLEAR**

Restated: Choose — [helper "Positive foreign taxes" = true → helper "Smaller of ftc.taxes, f1040.line16"] [helper "Positive foreign taxes" = false → helper "Year parameter sales.zero"]

Model: The structure (smaller of foreign tax or regular tax, zero if no foreign tax, refusal to Form 1116 when the election fails) is consistent with the text. However, it depends on the 'limited' operand, whose definition of regular tax is in line 20 instructions that are not provided.

Ruling: representation; project retained. Regular tax for the election is "your total U.S. income tax against which the credit is allowed (regular tax liability, as defined in section 26(b)(1))", excluding the net investment income tax (i1116 p. 25, line 20), which on the return in this slice is Form 1040 line 16: the additional line-16 taxes are refused by `scope.other_line16` and the net investment income and additional Medicare taxes sit on Schedule 2, after line 16. No change to the data.

## Raw response

```yaml
```yaml
lines:
  - key: "taxes"
    status: MATCH
    reason: "The text asks for 'your total creditable foreign taxes', reduced 'by any amount you would have entered on line 12 of Form 1116', and lists Forms 1099-INT and 1099-DIV as qualified payee statements. The specific box numbers (box 6, box 7) do not appear in the given text, but they are only guidance and do not change the input."
  - key: "all_passive"
    status: MATCH
    reason: "This matches the condition 'All of your foreign source gross income was \"passive category income\"', which for this purpose also includes high-taxed income and certain export financing interest."
  - key: "statements"
    status: MATCH
    reason: "This matches the condition 'All the income and any foreign taxes paid on it were reported to you on a qualified payee statement.'"
  - key: "eligible"
    status: MATCH
    reason: "The text says you must still apply 'the general rules for determining whether a tax is creditable' and 'reduce the taxes available for credit by any amount you would have entered on line 12'. Holding-period and related-payment rules are among the Foreign Taxes Not Eligible items the text cites."
  - key: "elect"
    status: MATCH
    reason: "The credit is described as an election, and with it you 'can't carry over to or from any other year any foreign taxes paid or accrued in a tax year to which the election applies'."
  - key: "limit"
    status: MATCH
    reason: "The text says 'aren't more than $300 ($600 if married filing a joint return)'. Only MFJ gets $600, so $300 for single, MFS, HOH and QSS is consistent."
  - key: "zero"
    status: MATCH
    reason: "This is a $0 constant used when there are no foreign taxes, so no credit arises. It is consistent with the text."
  - key: "has_tax"
    status: MATCH
    reason: "This tests whether the foreign taxes exceed zero. It is a simple predicate on the input and does not conflict with the text."
  - key: "needs1116"
    status: MATCH
    reason: "The election 'is available only if you meet all of the following conditions': passive income, qualified payee statements, and taxes not over $300/$600. The creditability and reduction rules still apply, and the filer must actually elect. Failing any of these is correctly treated as needing Form 1116. The estate/trust exclusion is outside the individual scope."
  - key: "limited"
    status: UNCLEAR
    reason: "The text says to enter 'the smaller of (a) your total foreign tax, or (b) your regular tax. See the instructions for line 20, later, for how to figure your regular tax.' Those line 20 instructions are not provided, so it cannot be confirmed that Form 1040 line 16 equals 'regular tax' for this purpose."
  - key: "credit"
    status: UNCLEAR
    reason: "The structure (smaller of foreign tax or regular tax, zero if no foreign tax, refusal to Form 1116 when the election fails) is consistent with the text. However, it depends on the 'limited' operand, whose definition of regular tax is in line 20 instructions that are not provided."
```
```
