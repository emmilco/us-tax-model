# Render comparison — scope

The rendered English of every printed line of `Proof-of-concept scope screening` (`rendered/2025/scope.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| line-scoped reviews | 1 (latest 2026-11-06); see Line-scoped reviews |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 5e735001c1608662a8cbbee87dd33ceb151e1cd9d0919b4eb053769866368d75 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | f6cd527e2ad6b29f35be673c35a7f8fd5621c88f6e48db75ac01c4a4efb247cf |
| lines judged | 5 |
| match / mismatch / unclear / missing | 5 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040gi | 2025; printed date 2026-02-25 | 14, 36, 43 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 36, 43 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i1040sse | 2025 | 1, 2, 3, 4, 5 | whole document | bd4768e77e9087e707701447574c3fd8b1b6ac8deca77fcf2e1bce4c50b7db28 | 1, 2, 3, 4, 5 | 6cb68f929e214450ea7ffa33648d5602e2431f38e91c7a6c83dfbee0ab23f08c |
| p575 | None | 35 | pages named by another document's citation | 4d6ee3802a2906a4633dcfc104aa33bb3d9ddedebddc9eadbd0393cfdb61e07b | 35 | 3962801dde168fda9f4ee239245d9746b12e2d60bf358b25186ae4a57aa5b837 |

## Lines

### schedule1 — Any income or adjustment requiring Schedule 1 other than the ones this tool asks about sep
Status: **MATCH**

Model: This is a filer-input scope screen, and its descriptions agree with the text given. The minister and church employee income wording matches i1040sse ('wages you received as an employee ... of a church or qualified church-controlled organization that has a certificate in effect electing an exemption from employer social security and Medicare taxes'), and the refusal names what is excluded.
Reviewed in: pass 14fc9dfc3bd1

### credits — Do you want to claim any credit other than the following, or do you have any other amount
Status: **MATCH**

Model: This is a filer-input scope screen for credits beyond the supported list, and the ready refusal names the excluded forms. Nothing in the text given contradicts the listed credits or the Form 8978 example; i1040gi points a negative Form 8978 line 14 amount to Schedule 3 line 6l.
Reviewed in: pass 14fc9dfc3bd1

### other_income — Any nonresident alien status, or other income or return treatment outside the kinds listed
Status: **MATCH**

Model: This is a filer-input scope screen, and its items agree with the text given. Pub. 575 spreads a 2023 qualified disaster recovery distribution over 2023, 2024 and 2025 and points to Form 8915-F, and i8606 says 'Include on line 1 any repayment of a qualified reservist distribution.' The ready refusal names the exclusion.
Reviewed in: pass 14fc9dfc3bd1

### other_line16 — Any additional Form 1040 line 16 tax or filing, including any of the following?
Status: **MATCH**

Model: The Form 8615 conditions match i1040gi: 'more than $2,700 of unearned income', required to file, under 18 / age 18 / full-time student 'at least age 19 but under age 24', parent alive, no joint return. The CFC/PFIC note matches i8960 line 13, and Schedule J is optional ('if you choose'), as i1040gi says.
Reviewed in: pass 14fc9dfc3bd1

### ready — All declared scope screens passed
Status: **MATCH**

Model: The value is a constant true, gated by refusals for each scope input and for MFS filing status. The MFS reasons are consistent with i1040gi ('can't take the standard deduction if your spouse itemizes', no education credits on a separate return) and with Form 1040 line 6d on MFS spouses who lived apart.
Reviewed in: pass 14fc9dfc3bd1

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| schedule1 | 177e07f9f761177d8d0d74d5818250a1c77e73f8404f01e9518ee809eba51a79 |
| credits | a2d9bcde875f8e0e3d4e7f8168c8af403162435e40d07d93d7049483ce2820e9 |
| other_income | 4215927dad7e61c1fa8e6d761035d1cd44533e7a65f34742a890462f2bc8cc95 |
| other_line16 | 96db9fa19806453b282fdcc893a7acdde1e978926828bcf82d896542ee4d7f89 |
| ready | 4845f0664f62dfdf1869a2dc192ec117e9941384cf0a2a71c04bb65360f317ac |
| (rest of the document) | 9a25da53ed2fbd2a45701244528c1eac2209891e67bfcf91f6753aa6e83ec08d |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass 14fc9dfc3bd1

| field | value |
| --- | --- |
| date | 2026-11-06 |
| review scope | lines schedule1, credits, other_income, other_line16, ready |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 14fc9dfc3bd12eb3c81675b4cf89b3e79580ecfb7a8d1960cb24ee15c5a803b4 |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | c22da569405ab86f393956d521b30522322aa02ca930b255d665ff8785e797b9 |
| receipt | .transcription/scope.render.lines-3f42ec2e2ecc |
| lines judged | 5 |
| match / mismatch / unclear / missing | 5 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040gi | 2025; printed date 2026-02-25 | 14, 36, 43 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 36, 43 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i1040sse | 2025 | 1, 2, 3, 4, 5 | whole document | bd4768e77e9087e707701447574c3fd8b1b6ac8deca77fcf2e1bce4c50b7db28 | 1, 2, 3, 4, 5 | 6cb68f929e214450ea7ffa33648d5602e2431f38e91c7a6c83dfbee0ab23f08c |
| p575 | None | 35 | pages named by another document's citation | 4d6ee3802a2906a4633dcfc104aa33bb3d9ddedebddc9eadbd0393cfdb61e07b | 35 | 3962801dde168fda9f4ee239245d9746b12e2d60bf358b25186ae4a57aa5b837 |
| i8606 | 2025 | 9 | pages named by another document's citation | 242e712835ef634f3af8f1d0f19435b236e9c54b80921d6017c153b3e6c2aec6 | 9 | 805e59f2458d33a3fc0a1d17ebede2ecd59e18d911069bbe84987e53e297ec79 |
| i8960 | 2025; printed date 2026-02-04 | 22 | pages named by another document's citation | fcae098ebc1ad79343de101a66765d3b3597f664dc744de3a7588be123c900a1 | - | d6dc1f475c511790abb02d6d6cfff554a59b40c0da1c56eb2f26af4e3cb7fa51 |

##### Raw response

```yaml
lines:
  - key: "schedule1"
    status: MATCH
    reason: "This is a filer-input scope screen, and its descriptions agree with the text given. The minister and church employee income wording matches i1040sse ('wages you received as an employee ... of a church or qualified church-controlled organization that has a certificate in effect electing an exemption from employer social security and Medicare taxes'), and the refusal names what is excluded."
  - key: "credits"
    status: MATCH
    reason: "This is a filer-input scope screen for credits beyond the supported list, and the ready refusal names the excluded forms. Nothing in the text given contradicts the listed credits or the Form 8978 example; i1040gi points a negative Form 8978 line 14 amount to Schedule 3 line 6l."
  - key: "other_income"
    status: MATCH
    reason: "This is a filer-input scope screen, and its items agree with the text given. Pub. 575 spreads a 2023 qualified disaster recovery distribution over 2023, 2024 and 2025 and points to Form 8915-F, and i8606 says 'Include on line 1 any repayment of a qualified reservist distribution.' The ready refusal names the exclusion."
  - key: "other_line16"
    status: MATCH
    reason: "The Form 8615 conditions match i1040gi: 'more than $2,700 of unearned income', required to file, under 18 / age 18 / full-time student 'at least age 19 but under age 24', parent alive, no joint return. The CFC/PFIC note matches i8960 line 13, and Schedule J is optional ('if you choose'), as i1040gi says."
  - key: "ready"
    status: MATCH
    reason: "The value is a constant true, gated by refusals for each scope input and for MFS filing status. The MFS reasons are consistent with i1040gi ('can't take the standard deduction if your spouse itemizes', no education credits on a separate return) and with Form 1040 line 6d on MFS spouses who lived apart."
```

## Raw response

```yaml
```yaml
lines:
  - key: "schedule1"
    status: MATCH
    reason: "This is a filer-answered scope screen, and its refusal names the excluded Schedule 1 items. The parts the text covers agree with the Schedule SE instructions: ministers, members of a religious order who haven't taken a vow of poverty and Christian Science practitioners, and church employee income as wages from 'a church or qualified church-controlled organization that has a certificate in effect electing an exemption from employer social security and Medicare taxes.'"
  - key: "credits"
    status: MATCH
    reason: "This is a scope screen whose refusal names the excluded forms (Schedule 3 lines 6a to 6z; Form 1040 lines 30 and 31). That fits Form 1040 line 30 'Refundable adoption credit from Form 8839' and line 31 'Amount from Schedule 3, line 15', and the instructions' cross-reference of Form 8978 amounts to Schedule 3 line 6l."
  - key: "other_income"
    status: MATCH
    reason: "The listed lines agree with Form 1040 lines 1b to 1d (household employee wages, tips and Medicaid waiver payments not on a W-2) and 1f to 1h (Form 8839 adoption benefits, Form 8919 wages, other earned income). Dependent care benefits are excluded except the W-2 box 10 amount, and Form 8915-F disaster distribution reporting agrees with Pub. 575. Unsupported cases are refused."
  - key: "other_line16"
    status: MATCH
    reason: "The Form 8615 conditions agree with the instructions: 'more than $2,700 of unearned income', required to file, under 18, age 18 without earned income over half of support, or a full-time student 'at least age 19 but under age 24', a parent alive at the end of 2025, and not filing jointly. Form 8814 and Form 4972 are the line 16 checkboxes, and the screen's list is open-ended ('including'), with a refusal."
  - key: "ready"
    status: MATCH
    reason: "This is a constant 'true' gate whose refusals agree with the screens above. The MFS refusal agrees with the instructions that a separate filer 'can't take the standard deduction if your spouse itemizes deductions' and 'can't take ... the education credits'."
```
```
