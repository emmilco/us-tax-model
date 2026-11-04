# Render comparison — scope

The rendered English of every printed line of `Proof-of-concept scope screening` (`rendered/2025/scope.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| line-scoped reviews | 1 (latest 2026-11-04); see Line-scoped reviews |
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

Model: This is a filer-answered scope screen, and its refusal names the excluded Schedule 1 items. The parts the text covers agree with the Schedule SE instructions: ministers, members of a religious order who haven't taken a vow of poverty and Christian Science practitioners, and church employee income as wages from 'a church or qualified church-controlled organization that has a certificate in effect electing an exemption from employer social security and Medicare taxes.'

### credits — Do you want to claim any credit other than the foreign tax credit claimed without Form 111
Status: **MATCH**

Model: This is a scope screen whose refusal names the excluded forms (Schedule 3 lines 6a to 6z; Form 1040 lines 30 and 31). That fits Form 1040 line 30 'Refundable adoption credit from Form 8839' and line 31 'Amount from Schedule 3, line 15', and the instructions' cross-reference of Form 8978 amounts to Schedule 3 line 6l.

### other_income — Any nonresident alien status (you or your spouse, for any part of 2025) or other income or
Status: **MATCH**

Model: The screen's items agree with the text given. Form 1040 lines 1b–1d and 1f–1h are household wages, tips, Medicaid waiver payments, adoption benefits, Form 8919 wages and other earned income. Pub. 575 covers the spread-out qualified disaster recovery distributions and their repayment on Form 8915-F, the i8606 says to 'Include on line 1 any repayment of a qualified reservist distribution,' and the i1040gi covers nonresident alien status; nothing in the text contradicts the restatement.
Reviewed in: pass 54def64fdc69

### other_line16 — Any additional Form 1040 line 16 tax or filing, including filing Form 8814 (even with no t
Status: **MATCH**

Model: The Form 8615 conditions match the instructions: 'more than $2,700 of unearned income,' required to file, under 18 or age 18 or a full-time student 'at least age 19 but under age 24' without earned income over half of support, a parent alive, and no joint return. The other items also match the text: Forms 8814 and 4972 are line 16 checkboxes, Schedule J is optional ('if you choose'), Form 8978 is mentioned, and the i8960 says CFC/PFIC ownership can make line 13 MAGI differ from AGI.
Reviewed in: pass 54def64fdc69

### ready — All declared scope screens passed
Status: **MATCH**

Model: Ready is simply true once no refusal applies, and each refusal names the gate it excludes (Schedule 1 items, other credits, other income, other line 16 tax, MFS). The MFS exclusions it cites, such as a spouse who itemizes and credits a separate return can't take, agree with the i1040gi Married Filing Separately text.
Reviewed in: pass 54def64fdc69

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| schedule1 | 772b4e76d3435af117a95432e12f98302e3021075b03d072701112816772039d |
| credits | ef3fa66779cb958c56f925af035a3c57fe54cc99d2f0d9a04ab3e4f3d3941c5f |
| other_income | 20e46c38b1f4243b4d02903fa3ab2cc85af8d85911a3bcc30473c4cabbd14995 |
| other_line16 | 2a67ba6cf0bbb33800ca2c3d778da9b1179df09525343535d68a812044d20240 |
| ready | 81eb33d4431975801caf0e8acb233c20a64df0f69acaca886fe62d4e6a16c784 |
| (rest of the document) | 9a25da53ed2fbd2a45701244528c1eac2209891e67bfcf91f6753aa6e83ec08d |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass 54def64fdc69

| field | value |
| --- | --- |
| date | 2026-11-04 |
| review scope | lines other_income, other_line16, ready |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 54def64fdc6913ac80baecdb131dbfafa66ac67f290ee571c9b6f2850f9d0607 |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 0c038d71681d95ff020dafdf85ddad6cbb20d79691d7c721fcfa11a5bc758260 |
| receipt | .transcription/scope.render.lines-12f0328e6e48 |
| lines judged | 3 |
| match / mismatch / unclear / missing | 3 / 0 / 0 / 0 |
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
```yaml
lines:
  - key: "other_income"
    status: MATCH
    reason: "The screen's items agree with the text given. Form 1040 lines 1b–1d and 1f–1h are household wages, tips, Medicaid waiver payments, adoption benefits, Form 8919 wages and other earned income. Pub. 575 covers the spread-out qualified disaster recovery distributions and their repayment on Form 8915-F, the i8606 says to 'Include on line 1 any repayment of a qualified reservist distribution,' and the i1040gi covers nonresident alien status; nothing in the text contradicts the restatement."
  - key: "other_line16"
    status: MATCH
    reason: "The Form 8615 conditions match the instructions: 'more than $2,700 of unearned income,' required to file, under 18 or age 18 or a full-time student 'at least age 19 but under age 24' without earned income over half of support, a parent alive, and no joint return. The other items also match the text: Forms 8814 and 4972 are line 16 checkboxes, Schedule J is optional ('if you choose'), Form 8978 is mentioned, and the i8960 says CFC/PFIC ownership can make line 13 MAGI differ from AGI."
  - key: "ready"
    status: MATCH
    reason: "Ready is simply true once no refusal applies, and each refusal names the gate it excludes (Schedule 1 items, other credits, other income, other line 16 tax, MFS). The MFS exclusions it cites, such as a spouse who itemizes and credits a separate return can't take, agree with the i1040gi Married Filing Separately text."
```
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
