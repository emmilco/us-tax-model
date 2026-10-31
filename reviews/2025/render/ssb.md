# Render comparison — ssb

The rendered English of every printed line of `Social Security Benefits Worksheet—Lines 6a and 6b` (`rendered/2025/ssb.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-30 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | e98d70b19265abbbb6407ca9af5e29f7b5f39ae751f42fb46e96956f8f8baa27 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 3b7a26f23416c32746997c0e197b4897ffd597d473f7e948ae960b63a1049842 |
| lines judged | 18 |
| match / mismatch / unclear / missing | 17 / 1 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 31, 32, 43, 93, 94, 95, 96, 97, 98, 104, 108, 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 31, 43, 93, 95, 96, 98, 104, 117 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| p590a | 2025 | 6, 7, 16, 30, 35 | cited pages | be942a345a01a8f875a2a625b400d7760221e1a55a2c85dca5ab75826e6c801a | 6, 7, 35 | cbe3b3b920a64ff514424a52a467ab8efabacfe958197d1ca8aabaee71ca5a3b |
| f8880 | 2025; created 2025-11-04 | 1, 2 | whole document | e8b37e5065850674d94eecd145d787e1789924b0c2b09bf3693992c45ba9dc94 | 2 | e082ccb481b2d0e872449d7728c290669213b8d16d4c94f281c1bb70aeaed575 |
| i1040sse | 2025 | 1, 2, 3, 4, 5 | whole document | bd4768e77e9087e707701447574c3fd8b1b6ac8deca77fcf2e1bce4c50b7db28 | 1, 2, 3, 4, 5 | 6cb68f929e214450ea7ffa33648d5602e2431f38e91c7a6c83dfbee0ab23f08c |
| p560 | For use in preparing 2025 returns | 7, 8, 9, 10, 11, 14, 15, 16, 17, 38, 39, 40 | cited pages | 38bbfa2efb2894e2527d66cd3478f33c6ceae4b777f78674c22bec16db9809aa | 7, 8, 9, 10, 11, 14, 15, 16, 17, 38, 40 | 7ef279c8f34addc2ff13420e35fab4a092bf8027f53907c28a5f46d2c21da737 |
| iw2w3 | 2025; printed date 2025-02-19 | 17, 18, 20 | cited pages | 27ad850a44d58d9186afcccb33b8a32f4747911e2b1b3138de515f44d4de33f3 | 17, 18, 20 | 3876738db222e8abe6103f29d8a8654a3139b9896f97e325d50e80b87ed5b26a |
| i8606 | 2025 | 5 | cited pages | 242e712835ef634f3af8f1d0f19435b236e9c54b80921d6017c153b3e6c2aec6 | 5 | 805e59f2458d33a3fc0a1d17ebede2ecd59e18d911069bbe84987e53e297ec79 |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040s8812 | 2025; printed date 2026-01-23 | 8 | cited pages | fd50a5266cc20aa5a31de0535658793f75c7abbb12fd83b65dc5b21c6ede2765 | - | e6ba91f54df679c9c19c23169c369f14bff012ba2fe110c3973bde59676c1d45 |
| f1040s1 | 2025; created 2025-07-25 | 1, 2 | whole document | 30004f72691a7078d8720e432e83110aa2bc3852ce9b45867becdb8c28222956 | - | 2293cadd525c2df84256455db693bbd46b710c62d28a98d503b1a6f8d8aea444 |
| i1040sc | 2025 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sse | 2025; created 2025-05-07 | 1, 2 | whole document | d214b41a4e42da1953a1ee216b6f9d263be284a90cf9f7f28dcb87cd0e9913e6 | - | fbeaf5e9b8509f8fe754b52a6b5a643934ae2ff1a6f76e6e69af8be42fcd2cdd |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| f7206 | 2025; created 2025-10-02 | 1 | whole document | 1f54af11e092a24258ac71f29d2bcfeeda1d6100ca332357d4569eea889e1dbb | - | e3b265efad583dd859c584d4e7e8a17d7b6e927878922ab5f020e2ff79a18d87 |
| i4562 | 2025 | 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 17, 18, 19, 34, 37, 39, 41, 59, 61, 62, 63, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 18, 19, 34, 37, 39, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |
| i7206 | 2025 | 1, 2 | whole document | 88aebffe01e22b57dadeb703483459075718cb0b2514fe8f00185975cfbeef3a | 1, 2 | 5bfa308e7e4634d4a0162d76b4af6a4182b8539a390109360875303222231cfe |
| f4562 | 2025; created 2025-10-09 | 1, 2, 3 | whole document | 71e2ace527072aaa7293e77897bb4ab8e473fa9c47b6b1ccb977fdc58a93bc2d | - | a1330c49d931e7ecdc867aef2d9e01390fc7b4d7e9321943a21ed0f8e883ed18 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |

## Lines

### 1 — Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099
Status: **MATCH**

Model: The helper is the total of box 5 of all Forms SSA-1099 and RRB-1099, which is what the worksheet asks for.

### 2 — Multiply line 1 by 50% (0.50)
Status: **MATCH**

Model: One-half equals the printed 50% (0.50). The refusals exclude the Exception cases that use Pub. 915 or Pub. 590-A, the lump-sum election, and excluded terrorist-attack disability payments.

### 3 — Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and 8
Status: **MATCH**

Model: It adds the same Form 1040 lines the worksheet says to combine (1z, 2b, 3b, 4b, 5b, 7a, and 8), and the value type allows a net negative amount.

### 4 — Enter the amount, if any, from Form 1040 or 1040-SR, line 2a
Status: **MATCH**

Model: It enters Form 1040, line 2a, as printed; the amount is zero if there is none.

### 5 — Combine lines 2, 3, and 4
Status: **MATCH**

Model: It adds lines 2, 3, and 4, as the worksheet's 'Combine lines 2, 3, and 4' directs.

### 6 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25
Status: **MISMATCH**

Restated: Add s1 line 11, s1 line 13, s1 line 15, s1 line 16, s1 line 17, s1 line 18, s1 line 19a, helper "Schedule 1, line 20 (IRA deduction) as this worksheet reads it, figured with no one covered by a retirement plan", and s1 line 25.

Model: The IRS total includes the actual Schedule 1 line 20 ('lines 11 through 20, and 23 and 25'), and the IRA worksheet says 'you can deduct a smaller amount and treat the rest as a nondeductible contribution.' The helper always uses the maximum (smallest of the applicable amount, line 10, and line 11), and no shown refusal or link to the deduct-less screen covers that election; the omitted lines 12, 14, and 23 and retirement-plan coverage are properly refused.

Ruling: scope; i1040gi p. 32, worksheet line 6 ("lines 11 through 20, and 23 and 25"); p. 98, IRA Deduction Worksheet line 12: "Or, if you want, you can deduct a smaller amount and treat the rest as a nondeductible contribution (see Form 8606)"; amb.2025.ira_ssb_copy. The copy ssb.ira_line20 is the register's chosen reading of line 20 on the no-coverage path. The election to deduct less is refused for the return by ira.less_gate on s1.line20 (amb.2025.ira_deduct_less): checked on stage16.refuse.ira.deduct_less with $20,000 of benefits, Form 1040 line 24 is refused on ira.less_gate, so the maximum the copy figures never reaches a completed return. Coverage is refused by ira.cov_gate and ssb.pub915, and lines 12, 14 and 23 by scope.schedule1, as the model accepts. Project stands on the English.

### 7 — Is the amount on line 6 less than the amount on line 5? If yes, subtract line 6 from line
Status: **MATCH**

Model: When line 6 is not less than line 5, the -0- result carries through to zero on line 18, matching the IRS instruction to enter -0- on line 6b. Otherwise it subtracts line 6 from line 5 as printed.

### 8 — $32,000 if married filing jointly; $25,000 if single, head of household, qualifying surviv
Status: **MATCH**

Model: It uses $32,000 for married filing jointly and $25,000 for single, head of household, qualifying surviving spouse, or married filing separately and living apart all year. For separate filers who lived together, the zero helper has no effect because line 16 uses line 7 times 85%, matching the skip instruction.

### 9 — Is the amount on line 8 less than the amount on line 7? If yes, subtract line 8 from line
Status: **MATCH**

Model: It subtracts line 8 from line 7 when line 8 is less. When it is not, the -0- result carries through to zero on line 18, matching the IRS stop instruction.

### 10 — Enter $12,000 if married filing jointly; $9,000 if single, head of household, qualifying s
Status: **MATCH**

Model: It uses $12,000 for married filing jointly and $9,000 for the other listed statuses, including married filing separately and living apart all year. The zero for separate filers who lived together reflects the skip of lines 8 through 15.

### 11 — Subtract line 10 from line 9. If zero or less, enter -0-
Status: **MATCH**

Model: It subtracts line 10 from line 9 and enters -0- if zero or less, as printed.

### 12 — Enter the smaller of line 9 or line 10
Status: **MATCH**

Model: It enters the smaller of line 9 or line 10, as printed.

### 13 — Enter one-half of line 12
Status: **MATCH**

Model: Multiplying line 12 by 1/2 is the same as the printed 'Enter one-half of line 12.'

### 14 — Enter the smaller of line 2 or line 13
Status: **MATCH**

Model: It enters the smaller of line 2 or line 13, as printed.

### 15 — Multiply line 11 by 85% (0.85). If line 11 is zero, enter -0-
Status: **MATCH**

Model: It multiplies line 11 by 85%, which also gives zero when line 11 is zero, as printed.

### 16 — Add lines 14 and 15
Status: **MATCH**

Model: It adds lines 14 and 15, except that separate filers who lived with their spouse at any time in 2025 use line 7 times 85%, as the line 8 instruction directs.

### 17 — Multiply line 1 by 85% (0.85)
Status: **MATCH**

Model: It multiplies line 1 by 85% (0.85), as printed.

### 18 — Taxable social security benefits. Enter the smaller of line 16 or line 17
Status: **MATCH**

Model: It enters the smaller of line 16 or line 17, as printed. The zero branch applies only when line 1 is zero, where line 17 would also make the printed result zero.

## Raw response

```yaml
```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "The helper is the total of box 5 of all Forms SSA-1099 and RRB-1099, which is what the worksheet asks for."
  - key: "2"
    status: MATCH
    reason: "One-half equals the printed 50% (0.50). The refusals exclude the Exception cases that use Pub. 915 or Pub. 590-A, the lump-sum election, and excluded terrorist-attack disability payments."
  - key: "3"
    status: MATCH
    reason: "It adds the same Form 1040 lines the worksheet says to combine (1z, 2b, 3b, 4b, 5b, 7a, and 8), and the value type allows a net negative amount."
  - key: "4"
    status: MATCH
    reason: "It enters Form 1040, line 2a, as printed; the amount is zero if there is none."
  - key: "5"
    status: MATCH
    reason: "It adds lines 2, 3, and 4, as the worksheet's 'Combine lines 2, 3, and 4' directs."
  - key: "6"
    status: MISMATCH
    reason: "The IRS total includes the actual Schedule 1 line 20 ('lines 11 through 20, and 23 and 25'), and the IRA worksheet says 'you can deduct a smaller amount and treat the rest as a nondeductible contribution.' The helper always uses the maximum (smallest of the applicable amount, line 10, and line 11), and no shown refusal or link to the deduct-less screen covers that election; the omitted lines 12, 14, and 23 and retirement-plan coverage are properly refused."
  - key: "7"
    status: MATCH
    reason: "When line 6 is not less than line 5, the -0- result carries through to zero on line 18, matching the IRS instruction to enter -0- on line 6b. Otherwise it subtracts line 6 from line 5 as printed."
  - key: "8"
    status: MATCH
    reason: "It uses $32,000 for married filing jointly and $25,000 for single, head of household, qualifying surviving spouse, or married filing separately and living apart all year. For separate filers who lived together, the zero helper has no effect because line 16 uses line 7 times 85%, matching the skip instruction."
  - key: "9"
    status: MATCH
    reason: "It subtracts line 8 from line 7 when line 8 is less. When it is not, the -0- result carries through to zero on line 18, matching the IRS stop instruction."
  - key: "10"
    status: MATCH
    reason: "It uses $12,000 for married filing jointly and $9,000 for the other listed statuses, including married filing separately and living apart all year. The zero for separate filers who lived together reflects the skip of lines 8 through 15."
  - key: "11"
    status: MATCH
    reason: "It subtracts line 10 from line 9 and enters -0- if zero or less, as printed."
  - key: "12"
    status: MATCH
    reason: "It enters the smaller of line 9 or line 10, as printed."
  - key: "13"
    status: MATCH
    reason: "Multiplying line 12 by 1/2 is the same as the printed 'Enter one-half of line 12.'"
  - key: "14"
    status: MATCH
    reason: "It enters the smaller of line 2 or line 13, as printed."
  - key: "15"
    status: MATCH
    reason: "It multiplies line 11 by 85%, which also gives zero when line 11 is zero, as printed."
  - key: "16"
    status: MATCH
    reason: "It adds lines 14 and 15, except that separate filers who lived with their spouse at any time in 2025 use line 7 times 85%, as the line 8 instruction directs."
  - key: "17"
    status: MATCH
    reason: "It multiplies line 1 by 85% (0.85), as printed."
  - key: "18"
    status: MATCH
    reason: "It enters the smaller of line 16 or line 17, as printed. The zero branch applies only when line 1 is zero, where line 17 would also make the printed result zero."
```
```
