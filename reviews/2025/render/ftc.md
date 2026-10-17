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
| i1116 | 2025; printed date 2025-12-23 | 1, 2 | cited pages | ca3e843c3bead1e7991566852707530b6bb7c2fd6008c1dbda0ac0bbd40c48ff | 1, 2 | cd35caf7283cb41a304b322a1438a3c7c78d3d692012065b8f15e84dd6340afa |

## Lines

### taxes — Total creditable foreign taxes after required reductions; generally Form 1099-INT box 6 an
Status: **MATCH**

Model: The text conditions the election on 'Your total creditable foreign taxes' after the required line 12 reduction. The given pages list Form 1099-INT and 1099-DIV as qualified payee statements but do not name box 6 or box 7; the label hedges this with 'generally'.

### all_passive — Was all foreign-source gross income passive category income under the small-tax election r
Status: **MATCH**

Model: Matches the condition 'All of your foreign source gross income was "passive category income"', which for this purpose includes high-taxed income and certain export financing interest.

### statements — Were all foreign income and taxes reported on qualified payee statements?
Status: **MATCH**

Model: Matches the condition 'All the income and any foreign taxes paid on it were reported to you on a qualified payee statement.'

### eligible — Have creditability, holding-period, related-payment and required foreign-tax reduction rul
Status: **MATCH**

Model: The text says you are 'still required to take into account the general rules for determining whether a tax is creditable' and must 'reduce the taxes available for credit by any amount you would have entered on line 12'. Holding-period and related-payment rules appear among the 'Foreign Taxes Not Eligible for a Credit' items.

### elect — Elect the credit without Form 1116, with no carryover to or from this election year?
Status: **MATCH**

Model: The election is optional, and if made 'You can't carry over to or from any other year any foreign taxes paid or accrued in a tax year to which the election applies'. This matches the restatement.

### limit — Year parameter ftc.limit
Status: **MATCH**

Model: The text says '$300 ($600 if married filing a joint return)'. All other filing statuses therefore get $300, as the restatement has it.

### zero — Year parameter sales.zero
Status: **MATCH**

Model: This is a constant $0, used as the credit when there is no foreign tax, which is consistent with the text.

### has_tax — Positive foreign taxes
Status: **MATCH**

Model: This tests whether total creditable foreign taxes are positive. It is a simple gate consistent with the text.

### needs1116 — Fails a condition of the election
Status: **MATCH**

Model: This fails the election if taxes are more than the limit ('aren't more than $300 ($600 ...)'), if income is not all passive, if it was not all reported on qualified payee statements, if the creditability or reduction rules are not met, or if the filer does not elect. Estates and trusts are outside an individual program.

### limited — Smaller of ftc.taxes, f1040.line16
Status: **UNCLEAR**

Restated: Enter the smaller of helper "Total creditable foreign taxes after required reductions; generally Form 1099-INT box 6 and Form 1099-DIV box 7" or f1040 line 16.

Model: The text says to enter 'the smaller of (a) your total foreign tax, or (b) your regular tax. See the instructions for line 20, later, for how to figure your regular tax.' The line 20 instructions are not in the pages given, so it cannot be confirmed that regular tax equals f1040 line 16.

Ruling: representation; project retained. Regular tax for the election is "your total U.S. income tax against which the credit is allowed (regular tax liability, as defined in section 26(b)(1))", excluding the net investment income tax (i1116 p. 25, line 20), which on the return in this slice is Form 1040 line 16: the additional line-16 taxes are refused by `scope.other_line16` and the net investment income and additional Medicare taxes sit on Schedule 2, after line 16. No change to the data.

### credit — Credit is the smaller of creditable foreign tax and regular income tax; zero if no foreign
Status: **UNCLEAR**

Restated: Choose — [helper "Positive foreign taxes" = true → helper "Smaller of ftc.taxes, f1040.line16"] [helper "Positive foreign taxes" = false → helper "Year parameter sales.zero"]

Model: The structure matches the text: the smaller of total foreign tax or regular tax, zero when there is no tax, and a refusal when the election conditions fail. However, it depends on 'regular tax', which the text defines only by reference to the line 20 instructions, and those are not provided.

Ruling: representation; project retained. Regular tax for the election is "your total U.S. income tax against which the credit is allowed (regular tax liability, as defined in section 26(b)(1))", excluding the net investment income tax (i1116 p. 25, line 20), which on the return in this slice is Form 1040 line 16: the additional line-16 taxes are refused by `scope.other_line16` and the net investment income and additional Medicare taxes sit on Schedule 2, after line 16. No change to the data.

## Raw response

```yaml
```yaml
lines:
  - key: "taxes"
    status: MATCH
    reason: "The text conditions the election on 'Your total creditable foreign taxes' after the required line 12 reduction. The given pages list Form 1099-INT and 1099-DIV as qualified payee statements but do not name box 6 or box 7; the label hedges this with 'generally'."
  - key: "all_passive"
    status: MATCH
    reason: "Matches the condition 'All of your foreign source gross income was \"passive category income\"', which for this purpose includes high-taxed income and certain export financing interest."
  - key: "statements"
    status: MATCH
    reason: "Matches the condition 'All the income and any foreign taxes paid on it were reported to you on a qualified payee statement.'"
  - key: "eligible"
    status: MATCH
    reason: "The text says you are 'still required to take into account the general rules for determining whether a tax is creditable' and must 'reduce the taxes available for credit by any amount you would have entered on line 12'. Holding-period and related-payment rules appear among the 'Foreign Taxes Not Eligible for a Credit' items."
  - key: "elect"
    status: MATCH
    reason: "The election is optional, and if made 'You can't carry over to or from any other year any foreign taxes paid or accrued in a tax year to which the election applies'. This matches the restatement."
  - key: "limit"
    status: MATCH
    reason: "The text says '$300 ($600 if married filing a joint return)'. All other filing statuses therefore get $300, as the restatement has it."
  - key: "zero"
    status: MATCH
    reason: "This is a constant $0, used as the credit when there is no foreign tax, which is consistent with the text."
  - key: "has_tax"
    status: MATCH
    reason: "This tests whether total creditable foreign taxes are positive. It is a simple gate consistent with the text."
  - key: "needs1116"
    status: MATCH
    reason: "This fails the election if taxes are more than the limit ('aren't more than $300 ($600 ...)'), if income is not all passive, if it was not all reported on qualified payee statements, if the creditability or reduction rules are not met, or if the filer does not elect. Estates and trusts are outside an individual program."
  - key: "limited"
    status: UNCLEAR
    reason: "The text says to enter 'the smaller of (a) your total foreign tax, or (b) your regular tax. See the instructions for line 20, later, for how to figure your regular tax.' The line 20 instructions are not in the pages given, so it cannot be confirmed that regular tax equals f1040 line 16."
  - key: "credit"
    status: UNCLEAR
    reason: "The structure matches the text: the smaller of total foreign tax or regular tax, zero when there is no tax, and a refusal when the election conditions fail. However, it depends on 'regular tax', which the text defines only by reference to the line 20 instructions, and those are not provided."
```
```
