# Render comparison — ftc

The rendered English of every printed line of `Foreign tax credit — election without Form 1116` (`rendered/2025/ftc.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-29 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | cb129f0bcc6df88e7398c5b7b0f6c44964d74b70f14c58a1efdd52072374da46 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 17f3d1a3eea40bb2e48f2d73de633a45e20dad7dfa14a54063fb5b1efad5f6ba |
| lines judged | 12 |
| match / mismatch / unclear / missing | 11 / 1 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1116 | 2025; printed date 2025-12-23 | 1, 2, 25 | cited pages | ca3e843c3bead1e7991566852707530b6bb7c2fd6008c1dbda0ac0bbd40c48ff | 1, 2, 25 | 4e9025bfc8a73bcfd687c7f45cb1a037cd39e7445319bbc71c748e12db68a46a |

## Lines

### taxes — Total creditable foreign taxes after required reductions; generally Form 1099-INT box 6 an
Status: **MATCH**

Model: The election test uses "Your total creditable foreign taxes", reduced by "any amount you would have entered on line 12 of Form 1116", as reported on payee statements such as Form 1099-DIV and 1099-INT. The specific box numbers in the label are not in the text given, but the word "generally" makes them informational and they do not change the computation.

### all_passive — Was all foreign-source gross income passive category income under the small-tax election r
Status: **MATCH**

Model: This restates the condition "All of your foreign source gross income was 'passive category income'", which for this purpose includes high-taxed income and certain export financing interest.

### statements — Were all foreign income and taxes reported on qualified payee statements?
Status: **MATCH**

Model: This restates the condition "All the income and any foreign taxes paid on it were reported to you on a qualified payee statement."

### eligible — Have creditability, holding-period, related-payment and required foreign-tax reduction rul
Status: **MATCH**

Model: The text says you must still apply "the general rules for determining whether a tax is creditable", which include the holding-period and related-payment items under Foreign Taxes Not Eligible for a Credit. It also says you must still reduce taxes by the line 12 amount.

### elect — Elect the credit without Form 1116, with no carryover to or from this election year?
Status: **MATCH**

Model: The election is optional ("You may be able to claim"). If made, "You can't carry over to or from any other year any foreign taxes paid or accrued in a tax year to which the election applies."

### limit — Year parameter ftc.limit
Status: **MATCH**

Model: The text sets the threshold at "$300 ($600 if married filing a joint return)", so $300 for every other filing status is consistent.

### zero — Year parameter sales.zero
Status: **MATCH**

Model: This is a $0 constant used for the credit when there is no foreign tax. That is consistent with a credit computed as the smaller of total foreign tax and regular tax.

### has_tax — Positive foreign taxes
Status: **MATCH**

Model: This is a positivity test on total creditable foreign taxes. The text does not require a separate computation for it.

### needs1116 — Fails a condition of the election
Status: **MATCH**

Model: The election requires all of the conditions and taxes that "aren't more than $300 ($600 ...)". Failing any condition, exceeding the limit, or not electing sends the filer to Form 1116 ("File Form 1116 ... if the election, earlier, doesn't apply").

### regular_tax — Regular tax for the limit (Form 1040 line 16 plus Schedule 2 line 1z)
Status: **MISMATCH**

Restated: Add f1040 line 16 and s2 line 1z.

Model: The line 20 instructions define regular tax for individuals as "the total of Form 1040 ... line 16, and Schedule 2 (Form 1040), Part I, line 1z, less any tax included on line 16 from Form 4972". The restatement omits the Form 4972 subtraction. It also omits the Form 8978 line 14 adjustment and the rule "If ... the amount of your tax is zero or less, enter -0-".

Ruling: scope; screens scope.other_line16 and scope.credits. i1116 p. 25, Line 20, "Individuals. Enter the total of Form 1040, 1040-SR, or 1040-NR, line 16, and Schedule 2 (Form 1040), Part I, line 1z, less any tax included on line 16 from Form 4972." and "If you file Form 8978, Partner’s Additional Reporting Year Tax, you will need to increase or decrease the amount you report on Form 1116, line 20 ... If, after your adjustment, the amount of your tax is zero or less, enter -0- on Form 1116, line 20." The restatement is the BUG-0190 fix (round-1 F1): ftc.regular_tax = f1040.line16 + s2.line1z. The three omitted terms are refused. Form 4972: scope.other_line16 ("... including filing Form 8814 (even with no tax), Form 4972, Form 8615, a section 962 election, Form 8621, a Form 8978 amount ...") refuses f1040.line16 and scope.ready, so no Form 4972 tax is in line 16 and nothing is subtracted. Form 8978: a positive amount is in line 16 and refused by the same screen; a negative one goes to Schedule 3 Part I and is refused by scope.credits ("... any other amount for Schedule 3 Part I (for example a Form 8978 adjustment)", at f1040 lines 29 and 30). The zero floor applies only "after your adjustment"; without one, line 16 and line 1z are both NonNegDollars, so their sum is never below zero. The fix uses line 1z, not line 3, which agrees with the page (line 3 adds the alternative minimum tax, section 26(b)(2)). Regression stage18.ftc_limit_with_repayment evaluates to ftc.regular_tax $375.00, ftc.credit $200.00 and Form 1040 line 22 $175.00, the round-1 source values. No new error found.

### limited — Smaller of ftc.taxes, ftc.regular_tax
Status: **MATCH**

Model: This follows "enter ... the smaller of (a) your total foreign tax, or (b) your regular tax." Any error in the regular-tax operand belongs to the regular_tax line.

### credit — Credit is the smaller of creditable foreign tax and regular income tax; zero if no foreign
Status: **MATCH**

Model: The credit is the smaller of foreign tax and regular tax, which equals zero when there is no foreign tax. The refusal properly excludes cases where the election is unavailable or not chosen and sends them to Form 1116.

## Raw response

```yaml
```yaml
lines:
  - key: "taxes"
    status: MATCH
    reason: "The election test uses \"Your total creditable foreign taxes\", reduced by \"any amount you would have entered on line 12 of Form 1116\", as reported on payee statements such as Form 1099-DIV and 1099-INT. The specific box numbers in the label are not in the text given, but the word \"generally\" makes them informational and they do not change the computation."
  - key: "all_passive"
    status: MATCH
    reason: "This restates the condition \"All of your foreign source gross income was 'passive category income'\", which for this purpose includes high-taxed income and certain export financing interest."
  - key: "statements"
    status: MATCH
    reason: "This restates the condition \"All the income and any foreign taxes paid on it were reported to you on a qualified payee statement.\""
  - key: "eligible"
    status: MATCH
    reason: "The text says you must still apply \"the general rules for determining whether a tax is creditable\", which include the holding-period and related-payment items under Foreign Taxes Not Eligible for a Credit. It also says you must still reduce taxes by the line 12 amount."
  - key: "elect"
    status: MATCH
    reason: "The election is optional (\"You may be able to claim\"). If made, \"You can't carry over to or from any other year any foreign taxes paid or accrued in a tax year to which the election applies.\""
  - key: "limit"
    status: MATCH
    reason: "The text sets the threshold at \"$300 ($600 if married filing a joint return)\", so $300 for every other filing status is consistent."
  - key: "zero"
    status: MATCH
    reason: "This is a $0 constant used for the credit when there is no foreign tax. That is consistent with a credit computed as the smaller of total foreign tax and regular tax."
  - key: "has_tax"
    status: MATCH
    reason: "This is a positivity test on total creditable foreign taxes. The text does not require a separate computation for it."
  - key: "needs1116"
    status: MATCH
    reason: "The election requires all of the conditions and taxes that \"aren't more than $300 ($600 ...)\". Failing any condition, exceeding the limit, or not electing sends the filer to Form 1116 (\"File Form 1116 ... if the election, earlier, doesn't apply\")."
  - key: "regular_tax"
    status: MISMATCH
    reason: "The line 20 instructions define regular tax for individuals as \"the total of Form 1040 ... line 16, and Schedule 2 (Form 1040), Part I, line 1z, less any tax included on line 16 from Form 4972\". The restatement omits the Form 4972 subtraction. It also omits the Form 8978 line 14 adjustment and the rule \"If ... the amount of your tax is zero or less, enter -0-\"."
  - key: "limited"
    status: MATCH
    reason: "This follows \"enter ... the smaller of (a) your total foreign tax, or (b) your regular tax.\" Any error in the regular-tax operand belongs to the regular_tax line."
  - key: "credit"
    status: MATCH
    reason: "The credit is the smaller of foreign tax and regular tax, which equals zero when there is no foreign tax. The refusal properly excludes cases where the election is unavailable or not chosen and sends them to Form 1116."
```
```
