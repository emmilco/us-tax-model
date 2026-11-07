# Render comparison — ftc

The rendered English of every printed line of `Foreign tax credit — election without Form 1116` (`rendered/2025/ftc.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-07 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | cfd909726dcd469225fc75f7c70dfad7a37fad2d07b726335d8a9e1d2c991cc7 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 4ab0d98d84d1d29aa033d90f9e85564a3cac750859c5e3545999da0491d9e188 |
| lines judged | 17 |
| match / mismatch / unclear / missing | 15 / 2 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1116 | 2025; printed date 2025-12-23 | 1, 2, 25 | cited pages | ca3e843c3bead1e7991566852707530b6bb7c2fd6008c1dbda0ac0bbd40c48ff | 1, 2, 25 | 4e9025bfc8a73bcfd687c7f45cb1a037cd39e7445319bbc71c748e12db68a46a |

## Lines

### taxes — Total creditable foreign taxes after required reductions; generally Form 1099-INT box 6 an
Status: **MATCH**

Model: The IRS text refers to total creditable foreign taxes after required reductions and to qualified payee statements; the filer-supplied amount is consistent.

### all_passive — Was all foreign-source gross income passive category income under the small-tax election r
Status: **MATCH**

Model: The IRS election requires all foreign-source gross income to be passive category income; the helper asks that condition.

### statements — Were all foreign income and taxes reported on qualified payee statements?
Status: **MATCH**

Model: The IRS election requires all income and any foreign taxes to be reported on a qualified payee statement; the helper asks that condition.

### eligible — Have creditability, holding-period, related-payment and required foreign-tax reduction rul
Status: **MATCH**

Model: The IRS text requires applying creditability rules and reducing taxes by the line 12 amount; the helper tracks those requirements.

### elect — Elect the credit without Form 1116, with no carryover to or from this election year?
Status: **MISMATCH**

Restated: Input — Elect the credit without Form 1116, with no carryover to or from this election year?

Model: IRS says: "You can’t carry over to or from any other year any foreign taxes paid or accrued in a tax year to which the election applies (but carryovers to and from other years are unaffected)." The restatement's "no carryover to or from this election year" is broader/different.

Ruling: model error; project retained. i1116 p. 2, "You can’t carry over to or from any other year any foreign taxes paid or accrued in a tax year to which the election applies (but carryovers to and from other years are unaffected)". The question's "with no carryover to or from this election year" states exactly that consequence: no carryover of this year's taxes to or from other years; carryovers between other years are not touched by the wording. Unchanged by the gate round, which only asks the question after foreign tax above zero.

### limit — Year parameter ftc.limit
Status: **MATCH**

Model: The IRS text sets $300, or $600 for married filing jointly; other filing statuses are correctly $300.

### zero — Year parameter sales.zero
Status: **MATCH**

Model: A zero amount is used only when there is no foreign tax, consistent with no foreign tax credit.

### has_tax — Positive foreign taxes
Status: **MATCH**

Model: The election and credit apply only when there is positive foreign tax; the helper tests taxes > $0.

### no — Year parameter ftc.no (false)
Status: **MATCH**

Model: This false default is used only when there is no foreign tax, so the election conditions are not applied.

### all_passive_if_tax — Whether all foreign-source gross income was passive category income, asked only with forei
Status: **MATCH**

Model: The passive-income condition is asked only when positive foreign tax exists; false without foreign tax is consistent because the election is inapplicable.

### statements_if_tax — Whether all foreign income and taxes were reported on qualified payee statements, asked on
Status: **MATCH**

Model: The qualified-statement condition is asked only when positive foreign tax exists; false without foreign tax is consistent because the election is inapplicable.

### eligible_if_tax — Whether the creditability, holding-period, related-payment and reduction rules are met, as
Status: **MATCH**

Model: The eligibility condition is asked only when positive foreign tax exists; false without foreign tax is consistent because the election is inapplicable.

### elect_if_tax — Whether the election without Form 1116 is made, asked only with foreign tax (false without
Status: **MATCH**

Model: The election question is asked only when positive foreign tax exists; false without foreign tax is consistent because the election is inapplicable.

### needs1116 — Fails a condition of the election
Status: **MATCH**

Model: The helper triggers Form 1116 when positive foreign tax exceeds the limit or any election condition/election itself is absent, matching the IRS conditions.

### regular_tax — Regular tax for the limit (Form 1040 line 16 plus Schedule 2 line 1z)
Status: **MISMATCH**

Restated: Add f1040 line 16 and s2 line 1z.

Model: IRS says: "Enter the total of Form 1040, 1040-SR, or 1040-NR, line 16, and Schedule 2 (Form 1040), Part I, line 1z, less any tax included on line 16 from Form 4972." The restatement omits the Form 4972 subtraction.

Ruling: scope; as the prior ruling and the Claude ruling of this round. i1116 p. 25, Line 20, "less any tax included on line 16 from Form 4972": Form 4972 tax is refused by scope.other_line16, so there is nothing to subtract on any return the tool completes.

### limited — Smaller of ftc.taxes, ftc.regular_tax
Status: **MATCH**

Model: The IRS election uses the smaller of total foreign tax and regular tax; the helper does that.

### credit — Credit is the smaller of creditable foreign tax and regular income tax; zero if no foreign
Status: **MATCH**

Model: The credit is the smaller of creditable foreign tax and regular tax, and zero when there is no foreign tax; the refusal correctly sends election failures to Form 1116.

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| taxes | e6d588a93b1ac6228df4a292cd466cb7ac8f603a98696488172beaf7a68c206f |
| all_passive | e2f969fdb75a96cd6ab0bf2e64c8779c9492eff9ab622ef594f4aeae757074d9 |
| statements | 13e2d9df332aed24bbee5ced09955425f5ded1ba51316a040eaaa097f1b1208b |
| eligible | 95155ec3ba732e5389fb3b04b77f0689a110d034d5580dd7fb6c71b14a1de5e3 |
| elect | 64f163b8eb270cad4bdb1d626aae9fb4f495c4b05d3619ba5850d464cdeca9ea |
| limit | 7861aa365730f3bb92cc3ff5d8db0fc99202ac69261abff8af27c50e712014da |
| zero | 30aa8978e16f8afbd14b9a2dfdb3b46389696ea81c185d9b916e716410069191 |
| has_tax | 13175e5b5bbd7aab5933429df51d4c3d417c686be59f875c66605982b570e27b |
| no | 2533a78fa5244d11b339dafa15b212c92a4fa6cc6efe2cdbebfb4595cb511a00 |
| all_passive_if_tax | c5dbf8770c3fde7ee327b5ab335778b055583e0b6bd88b5fdfac9c8264b7b63f |
| statements_if_tax | 2df197ed0b0e20a036e358bb449125ede470b0d9c6c3540e8aefeea084bf8950 |
| eligible_if_tax | 2af50f8e33c2f255a2a1aa14ffef9de06fe21c76978ce14de637dcac04184d91 |
| elect_if_tax | b5d2972bb75489d29a50cdfd0a174e9e53248ee5877b732d17cb4e279ce6d138 |
| needs1116 | 2e3b3732b2b08383984b0930b9c0d4f0174b78a54bfe6429fe75fc5e299036f8 |
| regular_tax | 9708e41122ecdaf9ac692bbfdc199dc4e05b00233f3861a7c8094d89caed5945 |
| limited | da26157cf0aea3df3f30f29dbbf26a300f25e0742ff83e73e16494997e9764e9 |
| credit | 720a4f71d3098a07cda22166ba3f07f4d14d93e9d80a30d570260029e2f88cdc |
| (rest of the document) | 8987249afe36e362d3bf00fb617ecae69dc7aac9d4ee3abd263aeae4d097b5db |

## Raw response

```yaml
lines:
  - key: "taxes"
    status: MATCH
    reason: "The IRS text refers to total creditable foreign taxes after required reductions and to qualified payee statements; the filer-supplied amount is consistent."
  - key: "all_passive"
    status: MATCH
    reason: "The IRS election requires all foreign-source gross income to be passive category income; the helper asks that condition."
  - key: "statements"
    status: MATCH
    reason: "The IRS election requires all income and any foreign taxes to be reported on a qualified payee statement; the helper asks that condition."
  - key: "eligible"
    status: MATCH
    reason: "The IRS text requires applying creditability rules and reducing taxes by the line 12 amount; the helper tracks those requirements."
  - key: "elect"
    status: MISMATCH
    reason: "IRS says: \"You can’t carry over to or from any other year any foreign taxes paid or accrued in a tax year to which the election applies (but carryovers to and from other years are unaffected).\" The restatement's \"no carryover to or from this election year\" is broader/different."
  - key: "limit"
    status: MATCH
    reason: "The IRS text sets $300, or $600 for married filing jointly; other filing statuses are correctly $300."
  - key: "zero"
    status: MATCH
    reason: "A zero amount is used only when there is no foreign tax, consistent with no foreign tax credit."
  - key: "has_tax"
    status: MATCH
    reason: "The election and credit apply only when there is positive foreign tax; the helper tests taxes > $0."
  - key: "no"
    status: MATCH
    reason: "This false default is used only when there is no foreign tax, so the election conditions are not applied."
  - key: "all_passive_if_tax"
    status: MATCH
    reason: "The passive-income condition is asked only when positive foreign tax exists; false without foreign tax is consistent because the election is inapplicable."
  - key: "statements_if_tax"
    status: MATCH
    reason: "The qualified-statement condition is asked only when positive foreign tax exists; false without foreign tax is consistent because the election is inapplicable."
  - key: "eligible_if_tax"
    status: MATCH
    reason: "The eligibility condition is asked only when positive foreign tax exists; false without foreign tax is consistent because the election is inapplicable."
  - key: "elect_if_tax"
    status: MATCH
    reason: "The election question is asked only when positive foreign tax exists; false without foreign tax is consistent because the election is inapplicable."
  - key: "needs1116"
    status: MATCH
    reason: "The helper triggers Form 1116 when positive foreign tax exceeds the limit or any election condition/election itself is absent, matching the IRS conditions."
  - key: "regular_tax"
    status: MISMATCH
    reason: "IRS says: \"Enter the total of Form 1040, 1040-SR, or 1040-NR, line 16, and Schedule 2 (Form 1040), Part I, line 1z, less any tax included on line 16 from Form 4972.\" The restatement omits the Form 4972 subtraction."
  - key: "limited"
    status: MATCH
    reason: "The IRS election uses the smaller of total foreign tax and regular tax; the helper does that."
  - key: "credit"
    status: MATCH
    reason: "The credit is the smaller of creditable foreign tax and regular tax, and zero when there is no foreign tax; the refusal correctly sends election failures to Form 1116."
```
