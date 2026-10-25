# Render comparison — ftc

The rendered English of every printed line of `Foreign tax credit — election without Form 1116` (`rendered/2025/ftc.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-24 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | bef79e64075d92093eba14ae0a4bffe7871cce47a5d27ee09d0a7de176090b77 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | f2625c069fc948f264f0e0b8b8d13ccdb2d8070bade81d24bde08b944d0282e8 |
| lines judged | 11 |
| match / mismatch / unclear / missing | 9 / 2 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1116 | 2025; printed date 2025-12-23 | 1, 2, 25 | cited pages | ca3e843c3bead1e7991566852707530b6bb7c2fd6008c1dbda0ac0bbd40c48ff | 1, 2, 25 | 4e9025bfc8a73bcfd687c7f45cb1a037cd39e7445319bbc71c748e12db68a46a |

## Lines

### taxes — Total creditable foreign taxes after required reductions; generally Form 1099-INT box 6 an
Status: **MATCH**

Model: The text says the election requires that 'Your total creditable foreign taxes aren't more than $300', and that you must still 'reduce the taxes available for credit by any amount you would have entered on line 12'. The input asks for exactly that net amount. The box numbers are not in the text, but the label only offers them as a 'generally' hint, so they do not change the value.

### all_passive — Was all foreign-source gross income passive category income under the small-tax election r
Status: **MATCH**

Model: This matches the condition 'All of your foreign source gross income was "passive category income"'. The phrase 'under the small-tax election rules' covers the text's widened definition, which adds high-taxed income and certain export financing interest.

### statements — Were all foreign income and taxes reported on qualified payee statements?
Status: **MATCH**

Model: This matches the condition 'All the income and any foreign taxes paid on it were reported to you on a qualified payee statement.'

### eligible — Have creditability, holding-period, related-payment and required foreign-tax reduction rul
Status: **MATCH**

Model: The text says you are 'still required to take into account the general rules for determining whether a tax is creditable', which include the holding-period and related-payment items, and to 'reduce the taxes available for credit by any amount you would have entered on line 12'. The input covers all of these.

### elect — Elect the credit without Form 1116, with no carryover to or from this election year?
Status: **MATCH**

Model: The text calls this an election and says 'You can't carry over to or from any other year any foreign taxes paid or accrued in a tax year to which the election applies'. The input asks for that choice and that consequence, and as a yes/no it does not change any computed amount.

### limit — Year parameter ftc.limit
Status: **MATCH**

Model: The text sets the threshold at '$300 ($600 if married filing a joint return)'. Using $300 for every other filing status and $600 for married filing jointly matches.

### zero — Year parameter sales.zero
Status: **MATCH**

Model: A $0 value used when there is no foreign tax is consistent with the text. With no foreign tax there is nothing to credit.

### has_tax — Positive foreign taxes
Status: **MATCH**

Model: This tests whether foreign taxes are positive, which is consistent with the text. The election and credit only matter when there is foreign tax.

### needs1116 — Fails a condition of the election
Status: **MATCH**

Model: Each condition is negated correctly. Taxes over the limit fail 'aren't more than $300 ($600...)'. Non-passive income, missing payee statements, failed creditability or line 12 reduction rules, or not choosing the election all mean Form 1116 is required.

### limited — Smaller of ftc.taxes, f1040.line16
Status: **MISMATCH**

Restated: Enter the smaller of helper "Total creditable foreign taxes after required reductions; generally Form 1099-INT box 6 and Form 1099-DIV box 7" or f1040 line 16.

Model: The text says to enter 'the smaller of (a) your total foreign tax, or (b) your regular tax' and to 'See the instructions for line 20... for how to figure your regular tax'. For individuals, line 20 means 'the total of Form 1040, 1040-SR, or 1040-NR, line 16, and Schedule 2 (Form 1040), Part I, line 1z, less any tax included on line 16 from Form 4972' (adjusted for Form 8978). The program uses Form 1040 line 16 alone: it leaves out Schedule 2 line 1z and does not subtract the Form 4972 tax.

Ruling: scope/representation on supported completed individual returns; i1116 (2025) pp.1–2 requires the smaller of foreign tax and regular tax, with p.25 Line20 defining regular tax as Form1040 line16 plus Schedule2 PartI line1z less Form4972 tax, with Form8978 adjustments. s2.other explicitly excludes advance-credit repayments and every other unsupported Schedule2 tax and is enforced at s2.line3/line21. scope.other_line16 excludes Forms4972/8978 and is enforced at f1040.line16. Thus the additional terms are zero on supported completed returns; Form1040 line16 is the regular-tax amount in this slice. Stand-alone excluded cases are not claimed equivalent. The reviewer correctly identifies the full IRS rule; its reduction here depends on those declared refusals, not model noise.

### credit — Credit is the smaller of creditable foreign tax and regular income tax; zero if no foreign
Status: **MISMATCH**

Restated: Choose — [helper "Positive foreign taxes" = true → helper "Smaller of ftc.taxes, f1040.line16"] [helper "Positive foreign taxes" = false → helper "Year parameter sales.zero"]

Model: The branching and the refusal are right. However, when foreign tax is positive the credit takes the 'limited' value, which measures regular tax as Form 1040 line 16 alone instead of 'the total of Form 1040... line 16, and Schedule 2 (Form 1040), Part I, line 1z, less any tax included on line 16 from Form 4972'. So the credit can differ from 'the smaller of (a) your total foreign tax, or (b) your regular tax.'

Ruling: scope/representation on supported completed individual returns; i1116 (2025) pp.1–2 requires the smaller of foreign tax and regular tax, with p.25 Line20 defining regular tax as Form1040 line16 plus Schedule2 PartI line1z less Form4972 tax, with Form8978 adjustments. s2.other explicitly excludes advance-credit repayments and every other unsupported Schedule2 tax and is enforced at s2.line3/line21. scope.other_line16 excludes Forms4972/8978 and is enforced at f1040.line16. Thus the additional terms are zero on supported completed returns; Form1040 line16 is the regular-tax amount in this slice. Stand-alone excluded cases are not claimed equivalent. The reviewer correctly identifies the full IRS rule; its reduction here depends on those declared refusals, not model noise.

## Raw response

```yaml
```yaml
lines:
  - key: "taxes"
    status: MATCH
    reason: "The text says the election requires that 'Your total creditable foreign taxes aren't more than $300', and that you must still 'reduce the taxes available for credit by any amount you would have entered on line 12'. The input asks for exactly that net amount. The box numbers are not in the text, but the label only offers them as a 'generally' hint, so they do not change the value."
  - key: "all_passive"
    status: MATCH
    reason: "This matches the condition 'All of your foreign source gross income was \"passive category income\"'. The phrase 'under the small-tax election rules' covers the text's widened definition, which adds high-taxed income and certain export financing interest."
  - key: "statements"
    status: MATCH
    reason: "This matches the condition 'All the income and any foreign taxes paid on it were reported to you on a qualified payee statement.'"
  - key: "eligible"
    status: MATCH
    reason: "The text says you are 'still required to take into account the general rules for determining whether a tax is creditable', which include the holding-period and related-payment items, and to 'reduce the taxes available for credit by any amount you would have entered on line 12'. The input covers all of these."
  - key: "elect"
    status: MATCH
    reason: "The text calls this an election and says 'You can't carry over to or from any other year any foreign taxes paid or accrued in a tax year to which the election applies'. The input asks for that choice and that consequence, and as a yes/no it does not change any computed amount."
  - key: "limit"
    status: MATCH
    reason: "The text sets the threshold at '$300 ($600 if married filing a joint return)'. Using $300 for every other filing status and $600 for married filing jointly matches."
  - key: "zero"
    status: MATCH
    reason: "A $0 value used when there is no foreign tax is consistent with the text. With no foreign tax there is nothing to credit."
  - key: "has_tax"
    status: MATCH
    reason: "This tests whether foreign taxes are positive, which is consistent with the text. The election and credit only matter when there is foreign tax."
  - key: "needs1116"
    status: MATCH
    reason: "Each condition is negated correctly. Taxes over the limit fail 'aren't more than $300 ($600...)'. Non-passive income, missing payee statements, failed creditability or line 12 reduction rules, or not choosing the election all mean Form 1116 is required."
  - key: "limited"
    status: MISMATCH
    reason: "The text says to enter 'the smaller of (a) your total foreign tax, or (b) your regular tax' and to 'See the instructions for line 20... for how to figure your regular tax'. For individuals, line 20 means 'the total of Form 1040, 1040-SR, or 1040-NR, line 16, and Schedule 2 (Form 1040), Part I, line 1z, less any tax included on line 16 from Form 4972' (adjusted for Form 8978). The program uses Form 1040 line 16 alone: it leaves out Schedule 2 line 1z and does not subtract the Form 4972 tax."
  - key: "credit"
    status: MISMATCH
    reason: "The branching and the refusal are right. However, when foreign tax is positive the credit takes the 'limited' value, which measures regular tax as Form 1040 line 16 alone instead of 'the total of Form 1040... line 16, and Schedule 2 (Form 1040), Part I, line 1z, less any tax included on line 16 from Form 4972'. So the credit can differ from 'the smaller of (a) your total foreign tax, or (b) your regular tax.'"
```
```
