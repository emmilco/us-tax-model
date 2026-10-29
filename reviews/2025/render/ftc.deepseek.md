# Render comparison — ftc

The rendered English of every printed line of `Foreign tax credit — election without Form 1116` (`rendered/2025/ftc.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-29 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | cb129f0bcc6df88e7398c5b7b0f6c44964d74b70f14c58a1efdd52072374da46 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
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

Model: The restatement's amount is the total creditable foreign taxes after required reductions, which the IRS text requires; the 1099-INT/DIV references are to qualified payee statements.

### all_passive — Was all foreign-source gross income passive category income under the small-tax election r
Status: **MATCH**

Model: The IRS election requires all foreign source gross income to be passive category income; the helper asks exactly that.

### statements — Were all foreign income and taxes reported on qualified payee statements?
Status: **MATCH**

Model: The IRS election requires all income and any foreign taxes paid on it to be reported on a qualified payee statement; the helper asks that.

### eligible — Have creditability, holding-period, related-payment and required foreign-tax reduction rul
Status: **MATCH**

Model: The IRS text says the general creditable-tax rules and the required line 12 reduction still apply; the helper asks whether those requirements are satisfied.

### elect — Elect the credit without Form 1116, with no carryover to or from this election year?
Status: **MATCH**

Model: The helper captures the election plus the no-carryover rule; unsupported carryover cases are refused to Form 1116.

### limit — Year parameter ftc.limit
Status: **MATCH**

Model: The IRS sets the threshold at $300, or $600 for married filing jointly; the helper uses those amounts for the filing statuses.

### zero — Year parameter sales.zero
Status: **MATCH**

Model: If there are no positive foreign taxes, the smaller-of computation is zero; the helper supplies $0.

### has_tax — Positive foreign taxes
Status: **MATCH**

Model: The helper is true exactly when creditable foreign taxes are positive, which is the condition for using the smaller-of credit computation.

### needs1116 — Fails a condition of the election
Status: **MATCH**

Model: The helper requires positive foreign taxes and fails the election if the limit is exceeded or any of the passive-income, qualified-statement, eligibility, or election conditions is not met; the refusal sends the filer to Form 1116.

### regular_tax — Regular tax for the limit (Form 1040 line 16 plus Schedule 2 line 1z)
Status: **MISMATCH**

Restated: Add f1040 line 16 and s2 line 1z.

Model: IRS line 20 requires Form 1040 line 16 plus Schedule 2 line 1z 'less any tax included on line 16 from Form 4972' (and possible Form 8978 adjustment); the restatement only adds the two lines.

Ruling: scope; screens scope.other_line16 and scope.credits. i1116 p. 25, Line 20, "Individuals. Enter the total of Form 1040, 1040-SR, or 1040-NR, line 16, and Schedule 2 (Form 1040), Part I, line 1z, less any tax included on line 16 from Form 4972." and "If you file Form 8978, Partner’s Additional Reporting Year Tax, you will need to increase or decrease the amount you report on Form 1116, line 20 ... If, after your adjustment, the amount of your tax is zero or less, enter -0- on Form 1116, line 20." The restatement is the BUG-0190 fix (round-1 F1): ftc.regular_tax = f1040.line16 + s2.line1z. The three omitted terms are refused. Form 4972: scope.other_line16 ("... including filing Form 8814 (even with no tax), Form 4972, Form 8615, a section 962 election, Form 8621, a Form 8978 amount ...") refuses f1040.line16 and scope.ready, so no Form 4972 tax is in line 16 and nothing is subtracted. Form 8978: a positive amount is in line 16 and refused by the same screen; a negative one goes to Schedule 3 Part I and is refused by scope.credits ("... any other amount for Schedule 3 Part I (for example a Form 8978 adjustment)", at f1040 lines 29 and 30). The zero floor applies only "after your adjustment"; without one, line 16 and line 1z are both NonNegDollars, so their sum is never below zero. The fix uses line 1z, not line 3, which agrees with the page (line 3 adds the alternative minimum tax, section 26(b)(2)). Regression stage18.ftc_limit_with_repayment evaluates to ftc.regular_tax $375.00, ftc.credit $200.00 and Form 1040 line 22 $175.00, the round-1 source values. No new error found.

### limited — Smaller of ftc.taxes, ftc.regular_tax
Status: **MATCH**

Model: The IRS says to enter the smaller of total foreign tax after required reductions or regular tax; the helper takes the smaller of taxes and regular_tax.

### credit — Credit is the smaller of creditable foreign tax and regular income tax; zero if no foreign
Status: **MATCH**

Model: The IRS says to enter the smaller of total foreign tax or regular tax; the helper does that and uses zero when there is no foreign tax, with the Form 1116 refusal for ineligible cases.

## Raw response

```yaml
lines:
  - key: "taxes"
    status: MATCH
    reason: "The restatement's amount is the total creditable foreign taxes after required reductions, which the IRS text requires; the 1099-INT/DIV references are to qualified payee statements."
  - key: "all_passive"
    status: MATCH
    reason: "The IRS election requires all foreign source gross income to be passive category income; the helper asks exactly that."
  - key: "statements"
    status: MATCH
    reason: "The IRS election requires all income and any foreign taxes paid on it to be reported on a qualified payee statement; the helper asks that."
  - key: "eligible"
    status: MATCH
    reason: "The IRS text says the general creditable-tax rules and the required line 12 reduction still apply; the helper asks whether those requirements are satisfied."
  - key: "elect"
    status: MATCH
    reason: "The helper captures the election plus the no-carryover rule; unsupported carryover cases are refused to Form 1116."
  - key: "limit"
    status: MATCH
    reason: "The IRS sets the threshold at $300, or $600 for married filing jointly; the helper uses those amounts for the filing statuses."
  - key: "zero"
    status: MATCH
    reason: "If there are no positive foreign taxes, the smaller-of computation is zero; the helper supplies $0."
  - key: "has_tax"
    status: MATCH
    reason: "The helper is true exactly when creditable foreign taxes are positive, which is the condition for using the smaller-of credit computation."
  - key: "needs1116"
    status: MATCH
    reason: "The helper requires positive foreign taxes and fails the election if the limit is exceeded or any of the passive-income, qualified-statement, eligibility, or election conditions is not met; the refusal sends the filer to Form 1116."
  - key: "regular_tax"
    status: MISMATCH
    reason: "IRS line 20 requires Form 1040 line 16 plus Schedule 2 line 1z 'less any tax included on line 16 from Form 4972' (and possible Form 8978 adjustment); the restatement only adds the two lines."
  - key: "limited"
    status: MATCH
    reason: "The IRS says to enter the smaller of total foreign tax after required reductions or regular tax; the helper takes the smaller of taxes and regular_tax."
  - key: "credit"
    status: MATCH
    reason: "The IRS says to enter the smaller of total foreign tax or regular tax; the helper does that and uses zero when there is no foreign tax, with the Form 1116 refusal for ineligible cases."
```
