# Render comparison — ssb

The rendered English of every printed line of `Social Security Benefits Worksheet—Lines 6a and 6b` (`rendered/2025/ssb.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| line-scoped reviews | 1 (latest 2026-11-04); see Line-scoped reviews |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 3aaeb2737002e5a69c2727d08be1bd797e5d35c387369e52fe26a35aa6b1f1b6 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 1b486e66d1e17c5909dc6d27b0fe20b0bed14846b8af225e05ccf176d48bca71 |
| lines judged | 18 |
| match / mismatch / unclear / missing | 17 / 1 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 31, 32, 43, 93, 94, 95, 96, 97, 98, 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 31, 43, 93, 95, 96, 98, 117 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| p590a | 2025 | 6, 7, 35 | cited pages | be942a345a01a8f875a2a625b400d7760221e1a55a2c85dca5ab75826e6c801a | 6, 7, 35 | cbe3b3b920a64ff514424a52a467ab8efabacfe958197d1ca8aabaee71ca5a3b |
| f8880 | 2025; created 2025-11-04 | 1, 2 | whole document | e8b37e5065850674d94eecd145d787e1789924b0c2b09bf3693992c45ba9dc94 | 2 | e082ccb481b2d0e872449d7728c290669213b8d16d4c94f281c1bb70aeaed575 |
| i8606 | 2025 | 5 | cited pages | 242e712835ef634f3af8f1d0f19435b236e9c54b80921d6017c153b3e6c2aec6 | 5 | 805e59f2458d33a3fc0a1d17ebede2ecd59e18d911069bbe84987e53e297ec79 |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040s8812 | 2025; printed date 2026-01-23 | 8 | cited pages | fd50a5266cc20aa5a31de0535658793f75c7abbb12fd83b65dc5b21c6ede2765 | - | e6ba91f54df679c9c19c23169c369f14bff012ba2fe110c3973bde59676c1d45 |
| f1040s1 | 2025; created 2025-07-25 | 1, 2 | whole document | 30004f72691a7078d8720e432e83110aa2bc3852ce9b45867becdb8c28222956 | - | 2293cadd525c2df84256455db693bbd46b710c62d28a98d503b1a6f8d8aea444 |
| i1040sse | 2025 | 1, 2, 3, 4, 5 | whole document | bd4768e77e9087e707701447574c3fd8b1b6ac8deca77fcf2e1bce4c50b7db28 | 1, 2, 3, 4, 5 | 6cb68f929e214450ea7ffa33648d5602e2431f38e91c7a6c83dfbee0ab23f08c |
| iw2w3 | 2025; printed date 2025-02-19 | 17, 18 | cited pages | 27ad850a44d58d9186afcccb33b8a32f4747911e2b1b3138de515f44d4de33f3 | 17, 18 | 3876738db222e8abe6103f29d8a8654a3139b9896f97e325d50e80b87ed5b26a |
| i1040sc | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sse | 2025; created 2025-05-07 | 1, 2 | whole document | d214b41a4e42da1953a1ee216b6f9d263be284a90cf9f7f28dcb87cd0e9913e6 | - | fbeaf5e9b8509f8fe754b52a6b5a643934ae2ff1a6f76e6e69af8be42fcd2cdd |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| p560 | For use in preparing 2025 returns | 7, 8, 9, 10, 11, 14, 15, 16, 17, 38, 39, 40 | cited pages | 38bbfa2efb2894e2527d66cd3478f33c6ceae4b777f78674c22bec16db9809aa | 7, 8, 9, 10, 11, 14, 15, 16, 17, 38, 40 | 7ef279c8f34addc2ff13420e35fab4a092bf8027f53907c28a5f46d2c21da737 |
| f7206 | 2025; created 2025-10-02 | 1 | whole document | 1f54af11e092a24258ac71f29d2bcfeeda1d6100ca332357d4569eea889e1dbb | - | e3b265efad583dd859c584d4e7e8a17d7b6e927878922ab5f020e2ff79a18d87 |
| i4562 | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 17, 18, 19, 31, 32, 34, 37, 39, 41, 59, 61, 62, 63, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 18, 19, 31, 32, 34, 37, 39, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |
| i7206 | 2025 | 1, 2 | whole document | 88aebffe01e22b57dadeb703483459075718cb0b2514fe8f00185975cfbeef3a | 1, 2 | 5bfa308e7e4634d4a0162d76b4af6a4182b8539a390109360875303222231cfe |
| f4562 | 2025; created 2025-10-09 | 1, 2, 3 | whole document | 71e2ace527072aaa7293e77897bb4ab8e473fa9c47b6b1ccb977fdc58a93bc2d | - | a1330c49d931e7ecdc867aef2d9e01390fc7b4d7e9321943a21ed0f8e883ed18 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |
| p538 | None | 17 | pages named by another document's citation | 4186d7aaa8f711c9a524b87fac1e3df05640b6d66130093b2469480acb06ef6c | 17 | f500211df18a4aafd843e48bbad4b9102c598cf5ccc0fae96c7814a4bef0ae00 |

## Lines

### 1 — Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099
Status: **MATCH**

Model: The IRS line asks for the total box 5 amount from all Forms SSA-1099 and RRB-1099; the restatement uses the same helper.

### 2 — Multiply line 1 by 50% (0.50)
Status: **MATCH**

Model: IRS line 2 multiplies line 1 by 50% (0.50), which is the same as 1/2; the refusals name the publication worksheets and other excluded cases.

### 3 — Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and 8
Status: **MATCH**

Model: IRS line 3 combines Form 1040 lines 1z, 2b, 3b, 4b, 5b, 7a, and 8, exactly as restated.

### 4 — Enter the amount, if any, from Form 1040 or 1040-SR, line 2a
Status: **MATCH**

Model: IRS line 4 enters the amount, if any, from Form 1040 line 2a; the restatement does the same.

### 5 — Combine lines 2, 3, and 4
Status: **MATCH**

Model: IRS line 5 combines lines 2, 3, and 4; the restatement adds those same lines.

### 6 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25
Status: **MATCH**

Model: IRS line 6 totals Schedule 1 lines 11 through 20, 23, and 25; the restatement covers the supported items and refuses the excluded Schedule 1 adjustments (lines 12, 14, and 23).

### 7 — Is the amount on line 6 less than the amount on line 5? If yes, subtract line 6 from line
Status: **MATCH**

Model: IRS line 7 subtracts line 6 from line 5 when line 6 is less, otherwise no benefits are taxable; the restatement's zero-or-less rule gives the same line value.

### 8 — $32,000 if married filing jointly; $25,000 if single, head of household, qualifying surviv
Status: **MATCH**

Model: It uses $32,000 for married filing jointly and $25,000 for single, HOH, QSS, or MFS lived apart all year, and skips lines 8 through 15 for MFS lived with the spouse, matching the worksheet line 8 instructions.
Reviewed in: pass fcd47be8e69f

### 9 — Is the amount on line 8 less than the amount on line 7? If yes, subtract line 8 from line
Status: **MISMATCH**

Restated: Subtract line 8 from line 7. If zero or less, enter -0-.

Model: The IRS line 9 is conditional: “Is the amount on line 8 less than the amount on line 7? No. STOP None of your social security benefits are taxable... Yes. Subtract line 8 from line 7.” The restatement instead always subtracts and floors at zero, omitting the No/STOP condition.

Ruling: representation; i1040gi p. 32, worksheet line 9: "Is the amount on line 8 less than the amount on line 7? No. None of your social security benefits are taxable. Enter -0- on Form 1040 or 1040-SR, line 6b. ... STOP". On the No branch the restatement's floor gives $0, and the round-2 display conditions stop the worksheet there (ssb.past9 is line 9 above zero; ssb.show10_15 hides lines 10 to 15 and ssb.show16_18 hides lines 16 to 18 unless married filing separately and living together, a return refused by s3.mfs), so no amount is shown past the STOP. Project stands.
Reviewed in: pass fcd47be8e69f

### 10 — Enter $12,000 if married filing jointly; $9,000 if single, head of household, qualifying s
Status: **MATCH**

Model: It uses $12,000 for married filing jointly and $9,000 for single, HOH, QSS, or MFS lived apart all year, matching line 10.
Reviewed in: pass fcd47be8e69f

### 11 — Subtract line 10 from line 9. If zero or less, enter -0-
Status: **MATCH**

Model: It says to subtract line 10 from line 9 and enter -0- if zero or less, matching line 11.
Reviewed in: pass fcd47be8e69f

### 12 — Enter the smaller of line 9 or line 10
Status: **MATCH**

Model: It enters the smaller of line 9 or line 10, matching line 12.
Reviewed in: pass fcd47be8e69f

### 13 — Enter one-half of line 12
Status: **MATCH**

Model: It computes one-half of line 12, matching line 13.
Reviewed in: pass fcd47be8e69f

### 14 — Enter the smaller of line 2 or line 13
Status: **MATCH**

Model: It enters the smaller of line 2 or line 13, matching line 14.
Reviewed in: pass fcd47be8e69f

### 15 — Multiply line 11 by 85% (0.85). If line 11 is zero, enter -0-
Status: **MATCH**

Model: It multiplies line 11 by 85% (0.85), matching line 15; omitting the redundant zero instruction does not change the value.
Reviewed in: pass fcd47be8e69f

### 16 — Add lines 14 and 15 (if married filing separately and you lived with your spouse at any ti
Status: **MATCH**

Model: It adds lines 14 and 15 except for MFS lived with the spouse, where it uses line 7 times 85%, matching the line 8 skip instruction and line 16.
Reviewed in: pass fcd47be8e69f

### 17 — Multiply line 1 by 85% (0.85)
Status: **MATCH**

Model: It multiplies line 1 by 85% (0.85), matching line 17.
Reviewed in: pass fcd47be8e69f

### 18 — Taxable social security benefits. Enter the smaller of line 16 or line 17
Status: **MATCH**

Model: It enters the smaller of line 16 or line 17 when benefits exist, and returns no amount ($0) otherwise, consistent with line 18 and the worksheet-not-needed case.
Reviewed in: pass fcd47be8e69f

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| 1 | 76637e5095bbc4d0d073bba07d2128b25ceec89a0f14ae365c41a77daf7a59c3 |
| 2 | 4476a2567813553419a59cc599b4bc876a8fb1a608252175ec6967e3525371c0 |
| 3 | 04a638edf0cfaadaf2e62796865d9920e7b6a2fe2d8f0b64cd604f34f13b8f52 |
| 4 | aa744040bb91dc6c31d93efc105025d1cdcdb1cbd76995d1f6175b0967ff6d95 |
| 5 | 44f9f14f0311182e2b2f3ecbcd93f14c54fd4b5d05dff78bdeeeac9acb468225 |
| 6 | be21631703fce01e8481d78349579ebea19f7d331d228371b8bf34d62f541010 |
| 7 | 152433cd6dd9464b00bf9db4a45eec5b53f906d1652cd5e9bdebeded584f0b4f |
| 8 | a84a9a1898f157e9dd752da10009a3e155ddda71f74e7c5700ff0f1c7beac583 |
| 9 | d92325b7e03e35ddc8cd65ca3ae5c6316f2bb4239b96956a5fdb76aaacb62346 |
| 10 | f513705fe0d2abe0fdfdfd5744357ee9f67949b60c71d65dfa178553feb7fc3e |
| 11 | e493cef3008a752abbfa3f39d5bb2a86be51f5d4a09c598129c363effbe76ec6 |
| 12 | 23a3ed2ef9769c4bd181c1935fe380f7e894df0be969f85535c1b366712efd43 |
| 13 | 3b41141dcf12fe6a46ffd559b888de52cf278553d128a8025534bbf667a4e6dc |
| 14 | 829698b340cb990f8ba20f832f928b48f56c85ca141e11a7d8d2ec7b6eade7ba |
| 15 | 0de672202e97284f3a651f35a5b384206f74b45434a10e0a32b016216f83fd96 |
| 16 | 1c3ed3979220e486ec26775efba103ccec55e418d25353d6114ebc7ab8991619 |
| 17 | d984d8f690104b305a693e51a6e9bc3d73e3d0915ee4f558e1d5b423178653b6 |
| 18 | b53a99500f17b04ec4b1d8ac037fe378519d3996dc11725ae62a32241d20ffb4 |
| (rest of the document) | 142145d6f88cbae0819a2535132ef458f8a2a8752d791971a6ce0ecec72fac7c |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass fcd47be8e69f

| field | value |
| --- | --- |
| date | 2026-11-04 |
| review scope | lines 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | fcd47be8e69f9624fa1cad577d2f5f33d74e583ece00a52ecb3227249fcc4c0e |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 4d78d21dc78432d288d2ebf19e09a9931f07d25669bd931ece3593ef4c4e9b04 |
| receipt | .transcription/ssb.deepseek.render.lines-38ff4c33403d |
| lines judged | 11 |
| match / mismatch / unclear / missing | 10 / 1 / 0 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 31, 32 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

##### Raw response

```yaml
lines:
  - key: "8"
    status: MATCH
    reason: "It uses $32,000 for married filing jointly and $25,000 for single, HOH, QSS, or MFS lived apart all year, and skips lines 8 through 15 for MFS lived with the spouse, matching the worksheet line 8 instructions."
  - key: "9"
    status: MISMATCH
    reason: "The IRS line 9 is conditional: “Is the amount on line 8 less than the amount on line 7? No. STOP None of your social security benefits are taxable... Yes. Subtract line 8 from line 7.” The restatement instead always subtracts and floors at zero, omitting the No/STOP condition."
  - key: "10"
    status: MATCH
    reason: "It uses $12,000 for married filing jointly and $9,000 for single, HOH, QSS, or MFS lived apart all year, matching line 10."
  - key: "11"
    status: MATCH
    reason: "It says to subtract line 10 from line 9 and enter -0- if zero or less, matching line 11."
  - key: "12"
    status: MATCH
    reason: "It enters the smaller of line 9 or line 10, matching line 12."
  - key: "13"
    status: MATCH
    reason: "It computes one-half of line 12, matching line 13."
  - key: "14"
    status: MATCH
    reason: "It enters the smaller of line 2 or line 13, matching line 14."
  - key: "15"
    status: MATCH
    reason: "It multiplies line 11 by 85% (0.85), matching line 15; omitting the redundant zero instruction does not change the value."
  - key: "16"
    status: MATCH
    reason: "It adds lines 14 and 15 except for MFS lived with the spouse, where it uses line 7 times 85%, matching the line 8 skip instruction and line 16."
  - key: "17"
    status: MATCH
    reason: "It multiplies line 1 by 85% (0.85), matching line 17."
  - key: "18"
    status: MATCH
    reason: "It enters the smaller of line 16 or line 17 when benefits exist, and returns no amount ($0) otherwise, consistent with line 18 and the worksheet-not-needed case."
```

## Raw response

```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "The IRS line asks for the total box 5 amount from all Forms SSA-1099 and RRB-1099; the restatement uses the same helper."
  - key: "2"
    status: MATCH
    reason: "IRS line 2 multiplies line 1 by 50% (0.50), which is the same as 1/2; the refusals name the publication worksheets and other excluded cases."
  - key: "3"
    status: MATCH
    reason: "IRS line 3 combines Form 1040 lines 1z, 2b, 3b, 4b, 5b, 7a, and 8, exactly as restated."
  - key: "4"
    status: MATCH
    reason: "IRS line 4 enters the amount, if any, from Form 1040 line 2a; the restatement does the same."
  - key: "5"
    status: MATCH
    reason: "IRS line 5 combines lines 2, 3, and 4; the restatement adds those same lines."
  - key: "6"
    status: MATCH
    reason: "IRS line 6 totals Schedule 1 lines 11 through 20, 23, and 25; the restatement covers the supported items and refuses the excluded Schedule 1 adjustments (lines 12, 14, and 23)."
  - key: "7"
    status: MATCH
    reason: "IRS line 7 subtracts line 6 from line 5 when line 6 is less, otherwise no benefits are taxable; the restatement's zero-or-less rule gives the same line value."
  - key: "8"
    status: MATCH
    reason: "IRS line 8 uses $32,000 for MFJ and $25,000 for single, HOH, QSS, or MFS lived apart all year; MFS lived with spouse skips lines 8 through 15, as restated."
  - key: "9"
    status: MATCH
    reason: "IRS line 9 subtracts line 8 from line 7 when line 8 is less, otherwise no benefits are taxable; the restatement's zero-or-less rule gives the same line value."
  - key: "10"
    status: MATCH
    reason: "IRS line 10 uses $12,000 for MFJ and $9,000 for single, HOH, QSS, or MFS lived apart all year, matching the restatement."
  - key: "11"
    status: MATCH
    reason: "IRS line 11 subtracts line 10 from line 9 and enters -0- if zero or less, exactly as restated."
  - key: "12"
    status: MATCH
    reason: "IRS line 12 enters the smaller of line 9 or line 10, exactly as restated."
  - key: "13"
    status: MATCH
    reason: "IRS line 13 enters one-half of line 12, which is the same as multiplying by 1/2."
  - key: "14"
    status: MATCH
    reason: "IRS line 14 enters the smaller of line 2 or line 13, exactly as restated."
  - key: "15"
    status: MATCH
    reason: "IRS line 15 multiplies line 11 by 85% (0.85); omitting the zero instruction does not change the computed value."
  - key: "16"
    status: MATCH
    reason: "IRS line 16 normally adds lines 14 and 15, but for MFS lived with spouse it uses line 7 times 85%; the restatement captures both branches."
  - key: "17"
    status: MATCH
    reason: "IRS line 17 multiplies line 1 by 85% (0.85), exactly as restated."
  - key: "18"
    status: MATCH
    reason: "IRS line 18 enters the smaller of line 16 or line 17; when there are no benefits the result is zero, matching the restatement's no-amount branch."
```
