# Render comparison — eic

The rendered English of every printed line of `Earned Income Credit (EIC)—Steps 1 to 6 and Worksheet A—Line 27a` (`rendered/2025/eic.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-30 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 43c83fc71565fa784b6e7ea07a157786768e2aa15a485a7785a3dd3e1d46f985 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 764ca34b318417459289e4b984452237ce694d73411849d80333f18af252ba45 |
| lines judged | 13 |
| match / mismatch / unclear / missing | 13 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 93, 94, 95, 104, 108, 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 40, 41, 42, 43, 44, 45, 93, 95, 104, 117 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040s8812 | 2025; printed date 2026-01-23 | 8 | cited pages | fd50a5266cc20aa5a31de0535658793f75c7abbb12fd83b65dc5b21c6ede2765 | - | e6ba91f54df679c9c19c23169c369f14bff012ba2fe110c3973bde59676c1d45 |
| f1040s8812 | 2025; created 2025-07-30 | 1, 2 | whole document | 9b38295071c42fe489ec8f93e117b31eda11355b5a95e3fe388eeee69601c8c9 | - | 3525d47f51cb713591081610a862cae77eff08a8aa7e2064a96b15cee4fd5cb9 |
| i1040sse | 2025 | 1, 2, 3, 4, 5 | whole document | bd4768e77e9087e707701447574c3fd8b1b6ac8deca77fcf2e1bce4c50b7db28 | 1, 2, 3, 4, 5 | 6cb68f929e214450ea7ffa33648d5602e2431f38e91c7a6c83dfbee0ab23f08c |
| i1040sc | 2025 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sse | 2025; created 2025-05-07 | 1, 2 | whole document | d214b41a4e42da1953a1ee216b6f9d263be284a90cf9f7f28dcb87cd0e9913e6 | - | fbeaf5e9b8509f8fe754b52a6b5a643934ae2ff1a6f76e6e69af8be42fcd2cdd |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| iw2w3 | 2025; printed date 2025-02-19 | 18, 20 | cited pages | 27ad850a44d58d9186afcccb33b8a32f4747911e2b1b3138de515f44d4de33f3 | 18, 20 | 3876738db222e8abe6103f29d8a8654a3139b9896f97e325d50e80b87ed5b26a |
| p560 | For use in preparing 2025 returns | 7, 8, 9, 10, 11, 14, 15, 16, 17, 38, 39, 40 | cited pages | 38bbfa2efb2894e2527d66cd3478f33c6ceae4b777f78674c22bec16db9809aa | 7, 8, 9, 10, 11, 14, 15, 16, 17, 38, 40 | 7ef279c8f34addc2ff13420e35fab4a092bf8027f53907c28a5f46d2c21da737 |
| f8880 | 2025; created 2025-11-04 | 1, 2 | whole document | e8b37e5065850674d94eecd145d787e1789924b0c2b09bf3693992c45ba9dc94 | 2 | e082ccb481b2d0e872449d7728c290669213b8d16d4c94f281c1bb70aeaed575 |
| p590a | 2025 | 30, 35 | cited pages | be942a345a01a8f875a2a625b400d7760221e1a55a2c85dca5ab75826e6c801a | 35 | cbe3b3b920a64ff514424a52a467ab8efabacfe958197d1ca8aabaee71ca5a3b |
| f7206 | 2025; created 2025-10-02 | 1 | whole document | 1f54af11e092a24258ac71f29d2bcfeeda1d6100ca332357d4569eea889e1dbb | - | e3b265efad583dd859c584d4e7e8a17d7b6e927878922ab5f020e2ff79a18d87 |
| i4562 | 2025 | 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 17, 18, 19, 34, 37, 39, 41, 59, 61, 62, 63, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 18, 19, 34, 37, 39, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |
| i7206 | 2025 | 1, 2 | whole document | 88aebffe01e22b57dadeb703483459075718cb0b2514fe8f00185975cfbeef3a | 1, 2 | 5bfa308e7e4634d4a0162d76b4af6a4182b8539a390109360875303222231cfe |
| f4562 | 2025; created 2025-10-09 | 1, 2, 3 | whole document | 71e2ace527072aaa7293e77897bb4ab8e473fa9c47b6b1ccb977fdc58a93bc2d | - | a1330c49d931e7ecdc867aef2d9e01390fc7b4d7e9321943a21ed0f8e883ed18 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |

## Lines

### (Step 5, 1) — Enter the amount from Form 1040 or 1040-SR, line 1z
Status: **MATCH**

Model: IRS Step 5 worksheet line 1 says to enter Form 1040 line 1z; the refusal names the clergy, church employee, and statutory employee cases it excludes.

### (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless chosen as ear
Status: **MATCH**

Model: IRS line 2 is the Medicaid waiver payment addback unless included in earned income; with no such payments it is $0, and the refusal names Medicaid waiver payments.

### (Step 5, 3) — Subtract line 2 from line 1
Status: **MATCH**

Model: IRS line 3 says to subtract line 2 from line 1, which is what the restatement does.

### (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **MATCH**

Model: IRS line 4 is nontaxable combat pay only if elected; with no combat pay it is $0, and the refusal names nontaxable combat pay.

### (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **MATCH**

Model: IRS line 5 says to add lines 3 and 4, which is what the restatement does.

### 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned income
Status: **MATCH**

Model: IRS Worksheet B line 4b combines lines 1e, 2c, 3, and 4a; the restatement adds Step 5 line 5 to the 1e and 2c helper, with statutory employee line 3 refused elsewhere.

### 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero if line 4b
Status: **MATCH**

Model: IRS Worksheet B line 6 enters total earned income from line 4b; subtracting $0 and flooring at zero is equivalent where line 6 is reached because line 4b must be positive.

### 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line 6
Status: **MATCH**

Model: IRS Worksheet A line 1 enters earned income from Step 5; when Worksheet A applies, the restatement uses Step 5 line 5, and the self-employed branch is not reached.

### 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the column for you
Status: **MATCH**

Model: IRS line 2 looks up line 1 in the EIC Table using filing status and the number of qualifying children with valid SSNs; the restatement does that and uses zero below the table start.

### 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **MATCH**

Model: IRS line 3 says to enter the amount from Form 1040 line 11b, exactly as restated.

### 4 — Are the amounts on lines 3 and 1 the same?
Status: **MATCH**

Model: IRS line 4 asks whether lines 3 and 1 are the same; the restatement compares equality.

### 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the column for you
Status: **MATCH**

Model: IRS line 5, when not left blank, looks up line 3 in the EIC Table by filing status and qualifying children; the restatement uses the same table credits.

### 6 (eic.line6) — This is your earned income credit
Status: **MATCH**

Model: IRS line 6 uses line 2 if line 4 is Yes or line 5 is blank, and otherwise the smaller of lines 5 and 2, matching the restatement and helper.

## Raw response

```yaml
lines:
  - key: "(Step 5, 1)"
    status: MATCH
    reason: "IRS Step 5 worksheet line 1 says to enter Form 1040 line 1z; the refusal names the clergy, church employee, and statutory employee cases it excludes."
  - key: "(Step 5, 2)"
    status: MATCH
    reason: "IRS line 2 is the Medicaid waiver payment addback unless included in earned income; with no such payments it is $0, and the refusal names Medicaid waiver payments."
  - key: "(Step 5, 3)"
    status: MATCH
    reason: "IRS line 3 says to subtract line 2 from line 1, which is what the restatement does."
  - key: "(Step 5, 4)"
    status: MATCH
    reason: "IRS line 4 is nontaxable combat pay only if elected; with no combat pay it is $0, and the refusal names nontaxable combat pay."
  - key: "(Step 5, 5)"
    status: MATCH
    reason: "IRS line 5 says to add lines 3 and 4, which is what the restatement does."
  - key: "4b"
    status: MATCH
    reason: "IRS Worksheet B line 4b combines lines 1e, 2c, 3, and 4a; the restatement adds Step 5 line 5 to the 1e and 2c helper, with statutory employee line 3 refused elsewhere."
  - key: "6 (eic.wsb_6)"
    status: MATCH
    reason: "IRS Worksheet B line 6 enters total earned income from line 4b; subtracting $0 and flooring at zero is equivalent where line 6 is reached because line 4b must be positive."
  - key: "1"
    status: MATCH
    reason: "IRS Worksheet A line 1 enters earned income from Step 5; when Worksheet A applies, the restatement uses Step 5 line 5, and the self-employed branch is not reached."
  - key: "2"
    status: MATCH
    reason: "IRS line 2 looks up line 1 in the EIC Table using filing status and the number of qualifying children with valid SSNs; the restatement does that and uses zero below the table start."
  - key: "3"
    status: MATCH
    reason: "IRS line 3 says to enter the amount from Form 1040 line 11b, exactly as restated."
  - key: "4"
    status: MATCH
    reason: "IRS line 4 asks whether lines 3 and 1 are the same; the restatement compares equality."
  - key: "5"
    status: MATCH
    reason: "IRS line 5, when not left blank, looks up line 3 in the EIC Table by filing status and qualifying children; the restatement uses the same table credits."
  - key: "6 (eic.line6)"
    status: MATCH
    reason: "IRS line 6 uses line 2 if line 4 is Yes or line 5 is blank, and otherwise the smaller of lines 5 and 2, matching the restatement and helper."
```
