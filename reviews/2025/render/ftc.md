# Render comparison — ftc

The rendered English of every printed line of `Foreign tax credit — election without Form 1116` (`rendered/2025/ftc.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 5219c0fc677afb9c255b1f1c10c74e40160ec8d398c5d5c5b0f7c0faa01df0fc |
| lines judged | 11 |
| match / mismatch / unclear / missing | 9 / 0 / 2 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 |
| --- | --- | --- | --- | --- |
| i1116 | 2025; printed date 2025-12-23 | 1, 2 | cited pages | ca3e843c3bead1e7991566852707530b6bb7c2fd6008c1dbda0ac0bbd40c48ff |

## Lines

### taxes — Total creditable foreign taxes after required reductions; generally Form 1099-INT box 6 an
Status: **MATCH**

Model: The text tests 'total creditable foreign taxes', which must be reduced 'by any amount you would have entered on line 12 of Form 1116'. The input asks for that reduced total. The 1099 box numbers are only a 'generally' hint, and they do not change the value.

### all_passive — Was all foreign-source gross income passive category income under the small-tax election r
Status: **MATCH**

Model: The text requires 'All of your foreign source gross income was "passive category income"', widened for this election to include high-taxed income and certain export financing interest. The input refers to those election-specific rules.

### statements — Were all foreign income and taxes reported on qualified payee statements?
Status: **MATCH**

Model: The text requires 'All the income and any foreign taxes paid on it were reported to you on a qualified payee statement'. The input asks exactly that.

### eligible — Have creditability, holding-period, related-payment and required foreign-tax reduction rul
Status: **MATCH**

Model: The text says the filer must still apply 'the general rules for determining whether a tax is creditable', including the holding-period and related-payment items listed under Foreign Taxes Not Eligible. The filer must also 'reduce the taxes available for credit by any amount you would have entered on line 12'. The input covers these.

### elect — Elect the credit without Form 1116, with no carryover to or from this election year?
Status: **MATCH**

Model: The text says that under the election 'You can't carry over to or from any other year any foreign taxes paid or accrued in a tax year to which the election applies'. The input asks for the election on those terms.

### limit — Year parameter ftc.limit
Status: **MATCH**

Model: The text sets the threshold at 'aren't more than $300 ($600 if married filing a joint return)'. That gives $600 for mfj and $300 for every other filing status, which is what the restatement uses.

### zero — Year parameter sales.zero
Status: **MATCH**

Model: This is a $0 constant used as the credit when there is no foreign tax. That is consistent with the text: with no foreign tax, the smaller of foreign tax and regular tax is $0.

### has_tax — Positive foreign taxes
Status: **MATCH**

Model: It tests whether total creditable foreign taxes exceed $0. That is a reasonable gate, and nothing in the text conflicts with it.

### needs1116 — Fails a condition of the election
Status: **MATCH**

Model: It flags a failure of any listed condition: the passive-income condition, the qualified payee statement condition, taxes 'aren't more than $300 ($600 ...)', the creditability and reduction rules, or not making the election. The text's exclusion of estates and trusts is not tested, but this is an individual Form 1040 context.

### limited — Smaller of ftc.taxes, f1040.line16
Status: **UNCLEAR**

Restated: Enter the smaller of helper "Total creditable foreign taxes after required reductions; generally Form 1099-INT box 6 and Form 1099-DIV box 7" or f1040 line 16.

Model: The text says to enter 'the smaller of (a) your total foreign tax, or (b) your regular tax. See the instructions for line 20, later, for how to figure your regular tax.' The line 20 instructions are not in the pages given, so it cannot be confirmed that regular tax equals Form 1040 line 16.

Ruling: representation; project retained. Regular tax for the election is "your total U.S. income tax against which the credit is allowed (regular tax liability, as defined in section 26(b)(1))", excluding the net investment income tax (i1116 p. 25, line 20), which on the return in this slice is Form 1040 line 16: the additional line-16 taxes are refused by `scope.other_line16` and the net investment income and additional Medicare taxes sit on Schedule 2, after line 16. No change to the data.

### credit — Credit is the smaller of creditable foreign tax and regular income tax; zero if no foreign
Status: **UNCLEAR**

Restated: Choose — [helper "Positive foreign taxes" = true → helper "Smaller of ftc.taxes, f1040.line16"] [helper "Positive foreign taxes" = false → helper "Year parameter sales.zero"]

Model: The structure matches the text: credit is the smaller of foreign tax and regular tax, and Form 1116 is required when the election is unavailable or not chosen. However, the value depends on 'regular tax' as defined in the line 20 instructions, which are not provided.

Ruling: representation; project retained. Regular tax for the election is "your total U.S. income tax against which the credit is allowed (regular tax liability, as defined in section 26(b)(1))", excluding the net investment income tax (i1116 p. 25, line 20), which on the return in this slice is Form 1040 line 16: the additional line-16 taxes are refused by `scope.other_line16` and the net investment income and additional Medicare taxes sit on Schedule 2, after line 16. No change to the data.

## Raw response

```yaml
```yaml
lines:
  - key: "taxes"
    status: MATCH
    reason: "The text tests 'total creditable foreign taxes', which must be reduced 'by any amount you would have entered on line 12 of Form 1116'. The input asks for that reduced total. The 1099 box numbers are only a 'generally' hint, and they do not change the value."
  - key: "all_passive"
    status: MATCH
    reason: "The text requires 'All of your foreign source gross income was \"passive category income\"', widened for this election to include high-taxed income and certain export financing interest. The input refers to those election-specific rules."
  - key: "statements"
    status: MATCH
    reason: "The text requires 'All the income and any foreign taxes paid on it were reported to you on a qualified payee statement'. The input asks exactly that."
  - key: "eligible"
    status: MATCH
    reason: "The text says the filer must still apply 'the general rules for determining whether a tax is creditable', including the holding-period and related-payment items listed under Foreign Taxes Not Eligible. The filer must also 'reduce the taxes available for credit by any amount you would have entered on line 12'. The input covers these."
  - key: "elect"
    status: MATCH
    reason: "The text says that under the election 'You can't carry over to or from any other year any foreign taxes paid or accrued in a tax year to which the election applies'. The input asks for the election on those terms."
  - key: "limit"
    status: MATCH
    reason: "The text sets the threshold at 'aren't more than $300 ($600 if married filing a joint return)'. That gives $600 for mfj and $300 for every other filing status, which is what the restatement uses."
  - key: "zero"
    status: MATCH
    reason: "This is a $0 constant used as the credit when there is no foreign tax. That is consistent with the text: with no foreign tax, the smaller of foreign tax and regular tax is $0."
  - key: "has_tax"
    status: MATCH
    reason: "It tests whether total creditable foreign taxes exceed $0. That is a reasonable gate, and nothing in the text conflicts with it."
  - key: "needs1116"
    status: MATCH
    reason: "It flags a failure of any listed condition: the passive-income condition, the qualified payee statement condition, taxes 'aren't more than $300 ($600 ...)', the creditability and reduction rules, or not making the election. The text's exclusion of estates and trusts is not tested, but this is an individual Form 1040 context."
  - key: "limited"
    status: UNCLEAR
    reason: "The text says to enter 'the smaller of (a) your total foreign tax, or (b) your regular tax. See the instructions for line 20, later, for how to figure your regular tax.' The line 20 instructions are not in the pages given, so it cannot be confirmed that regular tax equals Form 1040 line 16."
  - key: "credit"
    status: UNCLEAR
    reason: "The structure matches the text: credit is the smaller of foreign tax and regular tax, and Form 1116 is required when the election is unavailable or not chosen. However, the value depends on 'regular tax' as defined in the line 20 instructions, which are not provided."
```
```
