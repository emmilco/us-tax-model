# Render comparison — ftc

The rendered English of every printed line of `Foreign tax credit — election without Form 1116` (`rendered/2025/ftc.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-24 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | bef79e64075d92093eba14ae0a4bffe7871cce47a5d27ee09d0a7de176090b77 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | f2625c069fc948f264f0e0b8b8d13ccdb2d8070bade81d24bde08b944d0282e8 |
| lines judged | 11 |
| match / mismatch / unclear / missing | 8 / 2 / 1 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1116 | 2025; printed date 2025-12-23 | 1, 2, 25 | cited pages | ca3e843c3bead1e7991566852707530b6bb7c2fd6008c1dbda0ac0bbd40c48ff | 1, 2, 25 | 4e9025bfc8a73bcfd687c7f45cb1a037cd39e7445319bbc71c748e12db68a46a |

## Lines

### taxes — Total creditable foreign taxes after required reductions; generally Form 1099-INT box 6 an
Status: **UNCLEAR**

Restated: Input — Total creditable foreign taxes after required reductions; generally Form 1099-INT box 6 and Form 1099-DIV box 7

Model: The IRS text requires total creditable foreign taxes after reductions and lists Form 1099-INT and Form 1099-DIV as qualified payee statements, but it does not specify box 6 or box 7.

Ruling: representation; source-context limitation; archived f1099int (2025) PDF p.2 box6 and f1099div (2025) PDF p.2 box7 are labeled Foreign tax paid. The input still asks for total creditable taxes after required reductions; the box hints do not replace creditability or reduction tests. i1116 pp.1–2 identifies those forms as qualified payee statements but the prompt omits their box layouts; this adjudication supplies those archived sources. No model-error credit or new arithmetic assertion is claimed.

### all_passive — Was all foreign-source gross income passive category income under the small-tax election r
Status: **MATCH**

Model: The IRS election requires all foreign-source gross income to be passive category income under the election rules.

### statements — Were all foreign income and taxes reported on qualified payee statements?
Status: **MATCH**

Model: The IRS election requires all income and any foreign taxes paid on it to be reported on a qualified payee statement.

### eligible — Have creditability, holding-period, related-payment and required foreign-tax reduction rul
Status: **MATCH**

Model: The IRS says the electing filer must still apply the general creditability rules and reduce taxes by the line 12 amount, which covers these requirements.

### elect — Elect the credit without Form 1116, with no carryover to or from this election year?
Status: **MATCH**

Model: The IRS election rules disallow carryovers to or from the election year, so electing with no such carryover is consistent.

### limit — Year parameter ftc.limit
Status: **MATCH**

Model: The IRS threshold is $300, or $600 for married filing jointly, which matches the listed amounts.

### zero — Year parameter sales.zero
Status: **MATCH**

Model: A zero credit when there are no positive foreign taxes matches the smaller-of rule; zero foreign tax yields zero.

### has_tax — Positive foreign taxes
Status: **MATCH**

Model: The credit election only matters when there are positive foreign taxes; with none, the credit is zero.

### needs1116 — Fails a condition of the election
Status: **MATCH**

Model: The gate matches the election conditions and the $300/$600 limit, and it names Form 1116 for excluded cases.

### limited — Smaller of ftc.taxes, f1040.line16
Status: **MISMATCH**

Restated: Enter the smaller of helper "Total creditable foreign taxes after required reductions; generally Form 1099-INT box 6 and Form 1099-DIV box 7" or f1040 line 16.

Model: IRS line 20 regular tax is Form 1040 line 16 plus Schedule 2 (Form 1040), Part I, line 1z, less any tax included on line 16 from Form 4972; this uses only f1040 line 16.

Ruling: scope/representation on supported completed individual returns; i1116 (2025) pp.1–2 requires the smaller of foreign tax and regular tax, with p.25 Line20 defining regular tax as Form1040 line16 plus Schedule2 PartI line1z less Form4972 tax, with Form8978 adjustments. s2.other explicitly excludes advance-credit repayments and every other unsupported Schedule2 tax and is enforced at s2.line3/line21. scope.other_line16 excludes Forms4972/8978 and is enforced at f1040.line16. Thus the additional terms are zero on supported completed returns; Form1040 line16 is the regular-tax amount in this slice. Stand-alone excluded cases are not claimed equivalent. The reviewer correctly identifies the full IRS rule; its reduction here depends on those declared refusals, not model noise.

### credit — Credit is the smaller of creditable foreign tax and regular income tax; zero if no foreign
Status: **MISMATCH**

Restated: Choose — [helper "Positive foreign taxes" = true → helper "Smaller of ftc.taxes, f1040.line16"] [helper "Positive foreign taxes" = false → helper "Year parameter sales.zero"]

Model: The smaller-of rule is right, but the computation uses limited, which omits the Schedule 2 Part I line 1z addition and Form 4972 subtraction required for regular tax.

Ruling: scope/representation on supported completed individual returns; i1116 (2025) pp.1–2 requires the smaller of foreign tax and regular tax, with p.25 Line20 defining regular tax as Form1040 line16 plus Schedule2 PartI line1z less Form4972 tax, with Form8978 adjustments. s2.other explicitly excludes advance-credit repayments and every other unsupported Schedule2 tax and is enforced at s2.line3/line21. scope.other_line16 excludes Forms4972/8978 and is enforced at f1040.line16. Thus the additional terms are zero on supported completed returns; Form1040 line16 is the regular-tax amount in this slice. Stand-alone excluded cases are not claimed equivalent. The reviewer correctly identifies the full IRS rule; its reduction here depends on those declared refusals, not model noise.

## Raw response

```yaml
lines:
  - key: "taxes"
    status: UNCLEAR
    reason: 'The IRS text requires total creditable foreign taxes after reductions and lists Form 1099-INT and Form 1099-DIV as qualified payee statements, but it does not specify box 6 or box 7.'
  - key: "all_passive"
    status: MATCH
    reason: 'The IRS election requires all foreign-source gross income to be passive category income under the election rules.'
  - key: "statements"
    status: MATCH
    reason: 'The IRS election requires all income and any foreign taxes paid on it to be reported on a qualified payee statement.'
  - key: "eligible"
    status: MATCH
    reason: 'The IRS says the electing filer must still apply the general creditability rules and reduce taxes by the line 12 amount, which covers these requirements.'
  - key: "elect"
    status: MATCH
    reason: 'The IRS election rules disallow carryovers to or from the election year, so electing with no such carryover is consistent.'
  - key: "limit"
    status: MATCH
    reason: 'The IRS threshold is $300, or $600 for married filing jointly, which matches the listed amounts.'
  - key: "zero"
    status: MATCH
    reason: 'A zero credit when there are no positive foreign taxes matches the smaller-of rule; zero foreign tax yields zero.'
  - key: "has_tax"
    status: MATCH
    reason: 'The credit election only matters when there are positive foreign taxes; with none, the credit is zero.'
  - key: "needs1116"
    status: MATCH
    reason: 'The gate matches the election conditions and the $300/$600 limit, and it names Form 1116 for excluded cases.'
  - key: "limited"
    status: MISMATCH
    reason: 'IRS line 20 regular tax is Form 1040 line 16 plus Schedule 2 (Form 1040), Part I, line 1z, less any tax included on line 16 from Form 4972; this uses only f1040 line 16.'
  - key: "credit"
    status: MISMATCH
    reason: 'The smaller-of rule is right, but the computation uses limited, which omits the Schedule 2 Part I line 1z addition and Form 4972 subtraction required for regular tax.'
```
