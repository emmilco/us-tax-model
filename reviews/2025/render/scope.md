# Render comparison — scope

The rendered English of every printed line of `Proof-of-concept scope screening` (`rendered/2025/scope.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | b72cbe9671315aa9ccfcaecb5ff3037a401bd380df19fd10eb8975655bb4ef09 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | c0c4f10962168d8e302931bd58e6a8d0aa229a203ae2aa516501c95e6a37af96 |
| lines judged | 5 |
| match / mismatch / unclear / missing | 5 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040gi | 2025; printed date 2026-02-25 | 14, 36, 43 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 36, 43 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i1040sse | 2025 | 1, 2, 3, 4, 5 | whole document | bd4768e77e9087e707701447574c3fd8b1b6ac8deca77fcf2e1bce4c50b7db28 | 1, 2, 3, 4, 5 | 6cb68f929e214450ea7ffa33648d5602e2431f38e91c7a6c83dfbee0ab23f08c |

## Lines

### schedule1 — Any income or adjustment requiring Schedule 1 other than the ones this tool asks about sep
Status: **MATCH**

Model: This is a yes/no scope screen whose computation is just its own label. Its descriptions agree with the Schedule SE instructions: church employee income is wages from 'a church or qualified church-controlled organization that has a certificate in effect electing an exemption from employer social security and Medicare taxes', and clergy are 'a minister, member of a religious order who hasn't taken a vow of poverty, or Christian Science practitioner'.

### credits — Do you want to claim any credit other than the foreign tax credit claimed without Form 111
Status: **MATCH**

Model: This is a yes/no scope screen whose computation is just its own label. Its Form 8978 example agrees with the Form 1040 instructions, which send a negative 'amount on Form 8978, line 14' to 'the instructions for Schedule 3, line 6l'. The refusal names the credits it leaves out.

### other_income — Any nonresident alien status (you or your spouse, for any part of 2025) or other income or
Status: **MATCH**

Model: This is a yes/no scope screen whose computation is just its own label. Its references agree with Form 1040: lines 1b–1d and 1f–1h are household wages, tips not on line 1a, Medicaid waiver payments, adoption benefits, Form 8919 wages and other earned income, and line 1e covers taxable dependent care benefits from Form 2441.

### other_line16 — Any additional Form 1040 line 16 tax or filing, including filing Form 8814 (even with no t
Status: **MATCH**

Model: This is a yes/no scope screen. Its Form 8615 conditions match the instructions: more than $2,700 of unearned income, required to file, at least one parent alive at the end of 2025, no joint return, and under 18; or 18; or a full-time student 'at least age 19 but under age 24', with earned income not more than half of support in the last two cases. Forms 8814 and 4972 match the line 16 checkboxes.

### ready — All declared scope screens passed
Status: **MATCH**

Model: This is a constant 'true' gated by refusals that name each excluded case. The married-filing-separately refusal agrees with the instructions, which say a separate filer 'can't take the standard deduction if your spouse itemizes deductions' and can't take the education credits or certain deductions.

## Raw response

```yaml
```yaml
lines:
  - key: "schedule1"
    status: MATCH
    reason: "This is a yes/no scope screen whose computation is just its own label. Its descriptions agree with the Schedule SE instructions: church employee income is wages from 'a church or qualified church-controlled organization that has a certificate in effect electing an exemption from employer social security and Medicare taxes', and clergy are 'a minister, member of a religious order who hasn't taken a vow of poverty, or Christian Science practitioner'."
  - key: "credits"
    status: MATCH
    reason: "This is a yes/no scope screen whose computation is just its own label. Its Form 8978 example agrees with the Form 1040 instructions, which send a negative 'amount on Form 8978, line 14' to 'the instructions for Schedule 3, line 6l'. The refusal names the credits it leaves out."
  - key: "other_income"
    status: MATCH
    reason: "This is a yes/no scope screen whose computation is just its own label. Its references agree with Form 1040: lines 1b–1d and 1f–1h are household wages, tips not on line 1a, Medicaid waiver payments, adoption benefits, Form 8919 wages and other earned income, and line 1e covers taxable dependent care benefits from Form 2441."
  - key: "other_line16"
    status: MATCH
    reason: "This is a yes/no scope screen. Its Form 8615 conditions match the instructions: more than $2,700 of unearned income, required to file, at least one parent alive at the end of 2025, no joint return, and under 18; or 18; or a full-time student 'at least age 19 but under age 24', with earned income not more than half of support in the last two cases. Forms 8814 and 4972 match the line 16 checkboxes."
  - key: "ready"
    status: MATCH
    reason: "This is a constant 'true' gated by refusals that name each excluded case. The married-filing-separately refusal agrees with the instructions, which say a separate filer 'can't take the standard deduction if your spouse itemizes deductions' and can't take the education credits or certain deductions."
```
```
