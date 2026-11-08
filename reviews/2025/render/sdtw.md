# Render comparison — sdtw

The rendered English of every printed line of `Schedule D Tax Worksheet` (`rendered/2025/sdtw.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-26 |
| line-scoped reviews | 1 (latest 2026-11-07); see Line-scoped reviews |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | ceca9bfe032cb8ebdb4a5e57d80a85dbe28d0ee11f980b5167ebfa0becab8411 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 9e3683249bf7cfc8d40fec622971518f1ba9ced67cdd534ab8613a5b19645d9b |
| lines judged | 47 |
| match / mismatch / unclear / missing | 46 / 1 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sd | 2025; printed date 2025-12-11 | 8, 10, 11, 12, 15, 16 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 8, 11, 12 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| f1040sd | 2025; created 2025-10-06 | 1, 2 | whole document | 221151530f7cd599e8ad00bc3e1ba62d6b7ff34e402c336f4ae58d698c9f5187 | - | eb461181b39879c79d1c0b7761ca0cd9ade46fdb1531cdee3281053c348f6c41 |
| i1040gi | 2025; printed date 2026-02-25 | 38, 68, 80 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| f4952 | 2025; created 2025-05-28 | 1, 2, 3, 4 | whole document | efbeec4c44a1e43fb00231942c811a454d86b3632a2a662238893f8c4595bf81 | 3, 4 | c98eb27a83a89faecfdd0cd6597e8063fbd86a14ba1606f3e96c1c5f016d2b5c |
| i8949 | 2025; printed date 2026-01-20 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 | cited pages | d3ddc2b91cf89087ca348ebb00dbd1c80bbc025fa4df1176753d25013f581a67 | 2, 3, 4, 5, 6, 7, 9, 10 | cabdc81a0677c0e4de4a89f9a71d328395c4cc839206ebadb56aeb54bf954b85 |
| f1099div | January 2024 (continuous-use form) | 1, 2, 3, 4, 5, 6 | whole document | 833d93e5f2d0bfcc8c9d720c0e8cb8e623cd2c6a8ee25f364f1f69f49fa490e3 | 5 | 617419bd079b1520174ceca8549065c9e4001f2b06a16d1425c5469bbe49fa3d |
| f8949 | 2025; created 2025-05-05 | 1, 2 | whole document | f191f96ca2847b4c59875d5e1169f784a79b4d57f1f12d0196bd9bc2e7838e9d | - | cc308c3ff7751456647bed9c2855d077dcbd0a55469b57f9e8cccb6f4927f232 |
| i1040sb | TY2025; printed April 23, 2025 | 1, 2, 3 | whole document | 2bf62267574473b36fd9a69b6e0837ef74d72ac7d5dcbf1d26e7047d099f1e05 | 1, 2, 3 | 0d38b25d416cb650ef264faf8c1f118dfa4666f3949fbba7120f8c04d4e6914e |
| f8995 | 2025; created 2025-09-12 | 1 | whole document | 49922587df3bd093e24470f5b42d0e3382ef8f5210b3cedccb02ccb864f2f65a | - | 8e2e78d7610e1d45e93c10c8b03f9026d46a1166678c6ed93f852569c382f346 |
| i8995 | 2025; printed date 2026-01-26 | 3, 4 | pages named by another document's citation | 96284eaad2fe5ec324de9fd4335cea9ea3260e66ff1d8b1725c1cff7fbe1ddc2 | 3, 4 | 6671a64ba0011f89e03eb5985954073dcd984b3f346495182916b0ecaa42ec1a |

## Lines

### 1 — Taxable income
Status: **MISMATCH**

Restated: Enter the amount from f1040 line 15.

Model: The restatement always takes Form 1040 line 15. The IRS text adds: "However, if you are filing Form 2555 (relating to foreign earned income), enter instead the amount from line 3 of the Foreign Earned Income Tax Worksheet". No refusal names Form 2555 as excluded.

Ruling: scope; project retained. i1040sd p. 15, line 1: "Enter your taxable income from Form 1040, 1040-SR, or 1040-NR, line 15. (However, if you are filing Form 2555 (relating to foreign earned income), enter instead the amount from line 3 of the Foreign Earned Income Tax Worksheet in the instructions for Form 1040, line 16.)". The Form 2555 alternative is never reached on a return the tool computes: the exclusion is reported on Schedule 1, line 8d (i1040gi p. 91: "Foreign earned income exclusion and housing exclusion from Form 2555"), refused by s1.line8_other (forms/2025/s1.yaml: "lines 8a, 8d, 8e, 8k to 8q and 8s to 8v are refused by s1.line8_other"); the housing deduction (Schedule 1, line 24j) is refused at Form 1040 line 10 ("lines 24b to 24z are outside this tool"); and a filer who answers that Form 2555 is filed is refused at Schedule 1-A line 2a (forms/2025/s1a.yaml, gate sa.excluded_income, i1040gi p. 101). The worksheet note records Form 2555 as outside scope. The restatement says what the page says for every return the tool computes; as round 2. No change.

### 2 — Qualified dividends
Status: **MATCH**

Model: Line 2 says "Enter your qualified dividends from Form 1040, 1040-SR, or 1040-NR, line 3a", and the restatement uses Form 1040 line 3a. Its zero-unless-ordinary-dividends gate agrees with the 1040 instructions: "Qualified dividends are also included in the ordinary dividend total required to be shown on line 3b", so with no ordinary dividends there are no qualified dividends.
Reviewed in: pass e6b78a6f3605

### 3 — Form 4952 line 4g election
Status: **MATCH**

Model: This is the amount from Form 4952 line 4g. Refusals exclude carryovers, unsupported items, alternative allocation and invalid elections.

### 4 — Form 4952 line 4e (default capital-gain-first allocation), or zero when no Form 4952 is fi
Status: **MATCH**

Model: This is Form 4952 line 4e, or zero when Form 4952 isn't filed. The footnote's dotted-line "Elec." amount is excluded by the alternative-allocation refusal on the line 4g helper.

### 5 — Subtract line 4 from line 3; floor at zero
Status: **MATCH**

Model: Subtract line 4 from line 3, floored at zero, as printed.

### 6 — Subtract line 5 from line 2; floor at zero
Status: **MATCH**

Model: Same operands, direction and floor as "Subtract line 5 from line 2. If zero or less, enter -0-". The ** footnote only points Form 2555 filers to another worksheet's footnote and gives no different computation in the text provided.
Reviewed in: pass e6b78a6f3605

### 7 — Smaller of Schedule D lines 15 and 16
Status: **MATCH**

Model: Smaller of Schedule D line 15 or line 16, as printed.

### 8 — Smaller of lines 3 and 4
Status: **MATCH**

Model: Smaller of line 3 or line 4, as printed.

### 9 — Subtract line 8 from line 7; floor at zero
Status: **MATCH**

Model: Subtract line 8 from line 7, floored at zero, as printed.

### 10 — Add lines 6 and 9
Status: **MATCH**

Model: Add lines 6 and 9, as printed.

### 11 — Add Schedule D lines 18 and 19
Status: **MATCH**

Model: Adds Schedule D lines 18 and 19. Those lines are zero when Schedule D line 17 is No, consistent with Schedule D's skip instruction.

### 12 — Smaller of lines 9 and 11
Status: **MATCH**

Model: Smaller of line 9 or line 11, as printed.

### 13 — Subtract line 12 from line 10
Status: **MATCH**

Model: Subtract line 12 from line 10, as printed.

### 14 — Subtract line 13 from line 1; floor at zero
Status: **MATCH**

Model: Subtract line 13 from line 1, floored at zero, as printed.

### 15 — Zero-rate ceiling by filing status
Status: **MATCH**

Model: Uses $48,350 for single and MFS, $96,700 for MFJ and QSS, and $64,750 for HOH. These match the printed amounts.

### 16 — Smaller of lines 1 and 15
Status: **MATCH**

Model: Smaller of line 1 or line 15, as printed.

### 17 — Smaller of lines 14 and 16
Status: **MATCH**

Model: Smaller of line 14 or line 16, as printed.

### 18 — Subtract line 10 from line 1; floor at zero
Status: **MATCH**

Model: Subtract line 10 from line 1, floored at zero, as printed.

### 19 — Smaller of taxable income and ordinary-income ceiling
Status: **MATCH**

Model: Smaller of line 1 or the ceiling: $197,300 for single, MFS and HOH, and $394,600 for MFJ and QSS. These match the printed amounts.

### 20 — Smaller of lines 14 and 19
Status: **MATCH**

Model: Smaller of line 14 or line 19, as printed.

### 21 — Larger of lines 18 and 20
Status: **MATCH**

Model: Larger of line 18 or line 20, as printed.

### 22 — Subtract line 17 from line 16; taxed at zero percent
Status: **MATCH**

Model: Subtract line 17 from line 16, as printed.

### 23 — Smaller of lines 1 and 13
Status: **MATCH**

Model: Smaller of line 1 or line 13, zero when lines 1 and 16 are the same. This matches "If lines 1 and 16 are the same, skip lines 23 through 43".

### 24 — Amount from line 22
Status: **MATCH**

Model: Amount from line 22, zero when skipped, as printed.

### 25 — Subtract line 24 from line 23; floor at zero
Status: **MATCH**

Model: Subtract line 24 from line 23, floored at zero, under the line 22 skip rule.

### 26 — 15-percent ceiling by filing status
Status: **MATCH**

Model: Uses $533,400 for single, $300,000 for MFS, $600,050 for MFJ and QSS, and $566,700 for HOH. These match the printed amounts.

### 27 — Smaller of lines 1 and 26
Status: **MATCH**

Model: Smaller of line 1 or line 26, under the skip rule.

### 28 — Add lines 21 and 22
Status: **MATCH**

Model: Add lines 21 and 22, under the skip rule.

### 29 — Subtract line 28 from line 27; floor at zero
Status: **MATCH**

Model: Subtract line 28 from line 27, floored at zero, under the skip rule.

### 30 — Smaller of lines 25 and 29
Status: **MATCH**

Model: Smaller of line 25 or line 29, under the skip rule.

### 31 — Multiply line 30 by 15 percent
Status: **MATCH**

Model: Line 30 times 15%, as printed.

### 32 — Add lines 24 and 30
Status: **MATCH**

Model: Add lines 24 and 30, under the skip rule.

### 33 — Subtract line 32 from line 23
Status: **MATCH**

Model: Subtract line 32 from line 23. The line is zero when lines 1 and 32 are the same, or when the earlier skip applied.

### 34 — Multiply line 33 by 20 percent
Status: **MATCH**

Model: Line 33 times 20%, under the same skip rule.

### 35 — Smaller of line 9 and Schedule D line 19
Status: **MATCH**

Model: Smaller of line 9 or Schedule D line 19. Lines 35–40 are skipped when Schedule D line 19 is zero, as printed.

### 36 — Add lines 10 and 21
Status: **MATCH**

Model: Add lines 10 and 21, under the line 19 skip rule.

### 37 — Amount from line 1
Status: **MATCH**

Model: Amount from line 1, under the skip rule.

### 38 — Subtract line 37 from line 36; floor at zero
Status: **MATCH**

Model: Subtract line 37 from line 36, floored at zero, under the skip rule.

### 39 — Subtract line 38 from line 35; floor at zero
Status: **MATCH**

Model: Subtract line 38 from line 35, floored at zero, under the skip rule.

### 40 — Multiply line 39 by 25 percent
Status: **MATCH**

Model: Line 39 times 25%, under the skip rule.

### 41 — Add lines 21, 22, 30, 33 and 39
Status: **MATCH**

Model: Add lines 21, 22, 30, 33 and 39, reported only when Schedule D line 18 is more than zero. The gate also computes this line when line 19 is zero, but there line 42 works out to zero, so the result matches the printed skip rule.

### 42 — Subtract line 41 from line 1
Status: **MATCH**

Model: Subtract line 41 from line 1, under the line 18 skip rule.

### 43 — Multiply line 42 by 28 percent
Status: **MATCH**

Model: Line 42 times 28%, under the line 18 skip rule.

### 44 — Tax on line 21 using Tax Table or Tax Computation Worksheet
Status: **MATCH**

Model: Tax on line 21: the Tax Table below $100,000, otherwise the Tax Computation Worksheet, as printed.

### 45 — Add lines 31, 34, 40, 43 and 44
Status: **MATCH**

Model: Add lines 31, 34, 40, 43 and 44, as printed.

### 46 — Tax on all taxable income using Tax Table or Tax Computation Worksheet
Status: **MATCH**

Model: Tax on line 1: the Tax Table below $100,000, otherwise the Tax Computation Worksheet, as printed.

### 47 — Smaller of lines 45 and 46; tax on all taxable income
Status: **MATCH**

Model: Smaller of line 45 or line 46, as printed.

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| 1 | e3e1f172c06c39832be059dacbe52895fa0cd4cb978d39a6ef4c72d52987f58a |
| 2 | 4efbcf739fdb1d59e4adca3468628cae8d33602ca0b9636f1a57b1d920570be3 |
| 3 | d5a5630d6dc680e58b475a338c061f795530760f0ac16c0732337b7c27fb3eb1 |
| 4 | 953ce7388b160cbdcec60228ac0c56a7d2adaa0e503c61f7d47a40f609d96730 |
| 5 | 43ca8fb4d0d7fe4688dd6a73b72c5260a0d35687c7f0b8ba62083a7bb2cfa471 |
| 6 | 94c4b9a5837135c342a816c488b50d7e7c8c7e4ac5f0d4108f58032b5c8d7c39 |
| 7 | d251ecad6534b1a4c814c468cc63fb6936948622b13ddea5401576d84e5f0249 |
| 8 | e803b1c359c9240d6751028dd2fa1548f97ddbd3f22e5478cfd37bf9c22c8238 |
| 9 | 2743d0efcd830957b827c4519327ff0b7e966027acbdefbd598336cad7e65b08 |
| 10 | 4fbef8d5348c9ea2e21545716b13a77425cd6dd0783c663f3e83f3ecd60e51e9 |
| 11 | 866ae63587503ca6cd426ac6f0bce2bd247331fa41b57e0434bd8ead7eca682a |
| 12 | 1d3b0c9da72c91701981ff423250f764c96574600c4199f3e61ab667eaeb7e1b |
| 13 | 8526923e5b41d69c4beed1f538088dd4c65cfa8f74d6b94df313c1dc5d781cf8 |
| 14 | ef06a0eacbe145ada84f38a030520bcd24ff4c6a60baaed2455db584b574e48e |
| 15 | ce995ef8b4a78b738e264ac39998188dcb55a646010bffbbab4f146a1efcc0de |
| 16 | 620732100c723c347a08473a326945eeaaec0089ca8b7f8356974799e258b8da |
| 17 | fb448ef7e865e43148d92feb737ba25860ad849fe20b4cbec4374d839acea716 |
| 18 | f48b3a1d45cc940b137e4d7e7ee164a7982f1e242c44f25da471b2b0e5841b4c |
| 19 | 82a242b06af9d57daa18583288300f7881c73d63c025883abfdc637f35cdb7fa |
| 20 | 0d9b886df74eefeaff6e45a7ebdf284a669c87e5ac827fd6ebd9b84a01248720 |
| 21 | e12d3cfe997b9f9851d9a83765c5e958d737fe14d4328922f88abaf6bb6bd426 |
| 22 | c56fd9910988160314338e2bf4851500f062ff9ac0a19c93c6a739af55189b97 |
| 23 | 3a2de3dbeff6935337155007662cbbf55d70e6984f57f74dea350de90250c5aa |
| 24 | fb757949210a23c640be27e565abaf94dd8357cdd65fc979ad169f3e85a2c8a9 |
| 25 | 56743b1e6ad5e536ad053b9e42321452c4e406caae0e2d6d8be7a0661d5ae53d |
| 26 | 8ee2f28c407a58f5c5306e904a5da711df0446c5fb96cfe3acc614250267d161 |
| 27 | aef5aecc0180e78bbf3af7fd0211986d866af071ba0ab4d12753062ca806a357 |
| 28 | a14bae7811ff4ba61b2548499a5842cfe7a0098c16cb2da416b741c8b6c07d45 |
| 29 | b5470f5f0dec0819cdd7c4ee5145d3f9cc903047b502b59d0dfd6653faeac4c3 |
| 30 | 1927d5affeaba3c16eec4e146d37d3253df528b349cad75880b33efae4433dbd |
| 31 | 485861d73ab0c58cdc9516b36f9523a7ce43dab082980e509a36a26367f2d455 |
| 32 | af2a5552a5be2469952e0a33b0a544f3bee24f28ff67f7c73584925bdc1f0d27 |
| 33 | 60b3db18baad123807a7c535296c6fb4d71ef2d9a67a0b072d550ad6c743be00 |
| 34 | c22facdad6f2a3d54c272bc2634cf6226d41aa4de225dc66270333fbcb4ea523 |
| 35 | 685fec3d39f522bbbfb330f1b396d1d4b5cff82dd34e33f589629b1426c515fc |
| 36 | a79b89fb5ecba11614a4075708bdf10d9670159cbde23231105bb268025c0ab7 |
| 37 | d73e9c57d7ae14322ec1c1a30390c5ae7bc53ceb0c2c5e662e33647754cb8a16 |
| 38 | 99ba1b8ef309b4658b6d6cf92aca411d262c58297bc8d8cb045e710605f27429 |
| 39 | 89e96e9803d6c4d8966b7408ad6e4684af87a697220536acc8a8be568e3a7072 |
| 40 | e7dd899fcb371f28be00624d38cd1d624126cd313a7981fadee8fe879e32b090 |
| 41 | 6dbec7d321b4e4bb8054246ead2c43b936845d0279796faba3da60c7916dd8fc |
| 42 | c0c7827efcf59cd14f11b092a38ac4c65ea0cb50dd7887145429e4267e1b8e96 |
| 43 | 7e223072d552871d3f9e4ca4c9669f4261b598cfbb4772a2d605dc35a05652d9 |
| 44 | 54cc6cf1dbafd76ebe7ce2c4de1d28392771d4112ccea03fb04594159d77bdbd |
| 45 | 0e6286c360d30e0f0137fe5b0647bd489f171ef0bc2240530543c16062bca174 |
| 46 | 764a7d496474d63b36065c9469ee561935d5cd497bc8f513969e8fae79b758ed |
| 47 | b820b1ad2f6110d485d2a70df0a0a8bf4be5e7bba3191fc06b4488898afbd1e8 |
| (rest of the document) | ed48da6f1926de4f9e1acee968d8270ecf7d89b6e2b1b50424561f92a30136ee |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass e6b78a6f3605

| field | value |
| --- | --- |
| date | 2026-11-07 |
| review scope | lines 2, 6 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | e6b78a6f36057b61e69eaaef1bd96e77eab58f1bdd75dd1e3eafe9a046b53e3d |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 2ec656c8d6411d265f571fc58c0bbab22a909e586b0421189ac8b7c89092a7a1 |
| receipt | .transcription/sdtw.render.lines-a44c8a6613d9 |
| lines judged | 2 |
| match / mismatch / unclear / missing | 2 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sd | 2025; printed date 2025-12-11 | 15, 16 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | - | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| i1040gi | 2025; printed date 2026-02-25 | 25, 26 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 25, 26 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| f1099div | January 2024 (continuous-use form) | 1, 2, 3, 4, 5, 6 | whole document | 833d93e5f2d0bfcc8c9d720c0e8cb8e623cd2c6a8ee25f364f1f69f49fa490e3 | 5 | 617419bd079b1520174ceca8549065c9e4001f2b06a16d1425c5469bbe49fa3d |
| i1040sb | TY2025; printed April 23, 2025 | 1, 2, 3 | whole document | 2bf62267574473b36fd9a69b6e0837ef74d72ac7d5dcbf1d26e7047d099f1e05 | 1, 2, 3 | 0d38b25d416cb650ef264faf8c1f118dfa4666f3949fbba7120f8c04d4e6914e |

##### Raw response

```yaml
```yaml
lines:
  - key: "2"
    status: MATCH
    reason: "Line 2 says \"Enter your qualified dividends from Form 1040, 1040-SR, or 1040-NR, line 3a\", and the restatement uses Form 1040 line 3a. Its zero-unless-ordinary-dividends gate agrees with the 1040 instructions: \"Qualified dividends are also included in the ordinary dividend total required to be shown on line 3b\", so with no ordinary dividends there are no qualified dividends."
  - key: "6"
    status: MATCH
    reason: "Same operands, direction and floor as \"Subtract line 5 from line 2. If zero or less, enter -0-\". The ** footnote only points Form 2555 filers to another worksheet's footnote and gives no different computation in the text provided."
```
```

## Raw response

```yaml
```yaml
lines:
  - key: "1"
    status: MISMATCH
    reason: "The restatement always takes Form 1040 line 15. The IRS text adds: \"However, if you are filing Form 2555 (relating to foreign earned income), enter instead the amount from line 3 of the Foreign Earned Income Tax Worksheet\". No refusal names Form 2555 as excluded."
  - key: "2"
    status: MATCH
    reason: "Qualified dividends from Form 1040 line 3a, as the line says."
  - key: "3"
    status: MATCH
    reason: "This is the amount from Form 4952 line 4g. Refusals exclude carryovers, unsupported items, alternative allocation and invalid elections."
  - key: "4"
    status: MATCH
    reason: "This is Form 4952 line 4e, or zero when Form 4952 isn't filed. The footnote's dotted-line \"Elec.\" amount is excluded by the alternative-allocation refusal on the line 4g helper."
  - key: "5"
    status: MATCH
    reason: "Subtract line 4 from line 3, floored at zero, as printed."
  - key: "6"
    status: MATCH
    reason: "Subtract line 5 from line 2, floored at zero, as printed."
  - key: "7"
    status: MATCH
    reason: "Smaller of Schedule D line 15 or line 16, as printed."
  - key: "8"
    status: MATCH
    reason: "Smaller of line 3 or line 4, as printed."
  - key: "9"
    status: MATCH
    reason: "Subtract line 8 from line 7, floored at zero, as printed."
  - key: "10"
    status: MATCH
    reason: "Add lines 6 and 9, as printed."
  - key: "11"
    status: MATCH
    reason: "Adds Schedule D lines 18 and 19. Those lines are zero when Schedule D line 17 is No, consistent with Schedule D's skip instruction."
  - key: "12"
    status: MATCH
    reason: "Smaller of line 9 or line 11, as printed."
  - key: "13"
    status: MATCH
    reason: "Subtract line 12 from line 10, as printed."
  - key: "14"
    status: MATCH
    reason: "Subtract line 13 from line 1, floored at zero, as printed."
  - key: "15"
    status: MATCH
    reason: "Uses $48,350 for single and MFS, $96,700 for MFJ and QSS, and $64,750 for HOH. These match the printed amounts."
  - key: "16"
    status: MATCH
    reason: "Smaller of line 1 or line 15, as printed."
  - key: "17"
    status: MATCH
    reason: "Smaller of line 14 or line 16, as printed."
  - key: "18"
    status: MATCH
    reason: "Subtract line 10 from line 1, floored at zero, as printed."
  - key: "19"
    status: MATCH
    reason: "Smaller of line 1 or the ceiling: $197,300 for single, MFS and HOH, and $394,600 for MFJ and QSS. These match the printed amounts."
  - key: "20"
    status: MATCH
    reason: "Smaller of line 14 or line 19, as printed."
  - key: "21"
    status: MATCH
    reason: "Larger of line 18 or line 20, as printed."
  - key: "22"
    status: MATCH
    reason: "Subtract line 17 from line 16, as printed."
  - key: "23"
    status: MATCH
    reason: "Smaller of line 1 or line 13, zero when lines 1 and 16 are the same. This matches \"If lines 1 and 16 are the same, skip lines 23 through 43\"."
  - key: "24"
    status: MATCH
    reason: "Amount from line 22, zero when skipped, as printed."
  - key: "25"
    status: MATCH
    reason: "Subtract line 24 from line 23, floored at zero, under the line 22 skip rule."
  - key: "26"
    status: MATCH
    reason: "Uses $533,400 for single, $300,000 for MFS, $600,050 for MFJ and QSS, and $566,700 for HOH. These match the printed amounts."
  - key: "27"
    status: MATCH
    reason: "Smaller of line 1 or line 26, under the skip rule."
  - key: "28"
    status: MATCH
    reason: "Add lines 21 and 22, under the skip rule."
  - key: "29"
    status: MATCH
    reason: "Subtract line 28 from line 27, floored at zero, under the skip rule."
  - key: "30"
    status: MATCH
    reason: "Smaller of line 25 or line 29, under the skip rule."
  - key: "31"
    status: MATCH
    reason: "Line 30 times 15%, as printed."
  - key: "32"
    status: MATCH
    reason: "Add lines 24 and 30, under the skip rule."
  - key: "33"
    status: MATCH
    reason: "Subtract line 32 from line 23. The line is zero when lines 1 and 32 are the same, or when the earlier skip applied."
  - key: "34"
    status: MATCH
    reason: "Line 33 times 20%, under the same skip rule."
  - key: "35"
    status: MATCH
    reason: "Smaller of line 9 or Schedule D line 19. Lines 35–40 are skipped when Schedule D line 19 is zero, as printed."
  - key: "36"
    status: MATCH
    reason: "Add lines 10 and 21, under the line 19 skip rule."
  - key: "37"
    status: MATCH
    reason: "Amount from line 1, under the skip rule."
  - key: "38"
    status: MATCH
    reason: "Subtract line 37 from line 36, floored at zero, under the skip rule."
  - key: "39"
    status: MATCH
    reason: "Subtract line 38 from line 35, floored at zero, under the skip rule."
  - key: "40"
    status: MATCH
    reason: "Line 39 times 25%, under the skip rule."
  - key: "41"
    status: MATCH
    reason: "Add lines 21, 22, 30, 33 and 39, reported only when Schedule D line 18 is more than zero. The gate also computes this line when line 19 is zero, but there line 42 works out to zero, so the result matches the printed skip rule."
  - key: "42"
    status: MATCH
    reason: "Subtract line 41 from line 1, under the line 18 skip rule."
  - key: "43"
    status: MATCH
    reason: "Line 42 times 28%, under the line 18 skip rule."
  - key: "44"
    status: MATCH
    reason: "Tax on line 21: the Tax Table below $100,000, otherwise the Tax Computation Worksheet, as printed."
  - key: "45"
    status: MATCH
    reason: "Add lines 31, 34, 40, 43 and 44, as printed."
  - key: "46"
    status: MATCH
    reason: "Tax on line 1: the Tax Table below $100,000, otherwise the Tax Computation Worksheet, as printed."
  - key: "47"
    status: MATCH
    reason: "Smaller of line 45 or line 46, as printed."
```
```
