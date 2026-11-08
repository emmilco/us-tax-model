# Render comparison — sd

The rendered English of every printed line of `Schedule D — securities sales and supplied distribution subtotals` (`rendered/2025/sd.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| line-scoped reviews | 2 (latest 2026-11-07); see Line-scoped reviews |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | d8a1bade7e8895260afb189920619c7b281ba3f35ca05706a6924a7e0636eac5 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | eeaf337d5fa7492478be5ffa58f4ffcda447017332dba311b038e96279119959 |
| lines judged | 46 |
| match / mismatch / unclear / missing | 46 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sd | 2025; created 2025-10-06 | 1, 2 | whole document | 221151530f7cd599e8ad00bc3e1ba62d6b7ff34e402c336f4ae58d698c9f5187 | - | eb461181b39879c79d1c0b7761ca0cd9ade46fdb1531cdee3281053c348f6c41 |
| i1040sd | 2025; printed date 2025-12-11 | 8, 10, 11, 12, 15 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 8, 11, 12 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| i1040gi | 2025; printed date 2026-02-25 | 31, 38 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i8949 | 2025; printed date 2026-01-20 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 | cited pages | d3ddc2b91cf89087ca348ebb00dbd1c80bbc025fa4df1176753d25013f581a67 | 2, 3, 4, 5, 6, 7, 9, 10 | cabdc81a0677c0e4de4a89f9a71d328395c4cc839206ebadb56aeb54bf954b85 |
| f1099div | January 2024 (continuous-use form) | 1, 2, 3, 4, 5, 6 | whole document | 833d93e5f2d0bfcc8c9d720c0e8cb8e623cd2c6a8ee25f364f1f69f49fa490e3 | 5 | 617419bd079b1520174ceca8549065c9e4001f2b06a16d1425c5469bbe49fa3d |
| f4952 | 2025; created 2025-05-28 | 1, 2, 3, 4 | whole document | efbeec4c44a1e43fb00231942c811a454d86b3632a2a662238893f8c4595bf81 | 3, 4 | c98eb27a83a89faecfdd0cd6597e8063fbd86a14ba1606f3e96c1c5f016d2b5c |
| f8949 | 2025; created 2025-05-05 | 1, 2 | whole document | f191f96ca2847b4c59875d5e1169f784a79b4d57f1f12d0196bd9bc2e7838e9d | - | cc308c3ff7751456647bed9c2855d077dcbd0a55469b57f9e8cccb6f4927f232 |
| i1040sb | TY2025; printed April 23, 2025 | 1, 2, 3 | whole document | 2bf62267574473b36fd9a69b6e0837ef74d72ac7d5dcbf1d26e7047d099f1e05 | 1, 2, 3 | 0d38b25d416cb650ef264faf8c1f118dfa4666f3949fbba7120f8c04d4e6914e |
| f8995 | 2025; created 2025-09-12 | 1 | whole document | 49922587df3bd093e24470f5b42d0e3382ef8f5210b3cedccb02ccb864f2f65a | - | 8e2e78d7610e1d45e93c10c8b03f9026d46a1166678c6ed93f852569c382f346 |
| p550 | 2025 returns; printed date 2026-03-05 | 82, 86 | pages named by another document's citation | e40622e028486d7eb31a6da342ba2ba3c8b2f7ea9d341d9f47a1d33407d5aa26 | 82, 86 | 7629580e9cb35aa5f67e5d7c035b45850164eb1fe458f8acaa2781578ad0bf51 |
| i8995 | 2025; printed date 2026-01-26 | 3, 4 | pages named by another document's citation | 96284eaad2fe5ec324de9fd4335cea9ea3260e66ff1d8b1725c1cff7fbe1ddc2 | 3, 4 | 6671a64ba0011f89e03eb5985954073dcd984b3f346495182916b0ecaa42ec1a |

## Lines

### 1a(d) — Line 1a, column (d) totals
Status: **MATCH**

Model: Matches Schedule D line 1a column (d): short-term basis-reported no-adjustment aggregate proceeds; digital G cases are excluded by the named digital-asset refusal.
Reviewed in: pass 790975e2b01d

### 1a(e) — Line 1a, column (e) totals
Status: **MATCH**

Model: Matches line 1a column (e): reported cost or other basis for short-term basis-reported no-adjustment aggregate transactions; digital G cases are excluded by the named refusal.
Reviewed in: pass 790975e2b01d

### 1a(g) — Line 1a, column (g) totals
Status: **MATCH**

Model: Matches line 1a column (g) within supported aggregate cases; no adjustments are allowed on line 1a, and invalid adjustment cases are refused.
Reviewed in: pass 790975e2b01d

### 1a(h) — Line 1a, column (h) totals
Status: **MATCH**

Model: Matches line 1a column (h): proceeds less column (e) plus column (g) for the supported short-term aggregate transactions.
Reviewed in: pass 790975e2b01d

### 1b(d) — Line 1b, column (d) totals
Status: **MATCH**

Model: Matches line 1b column (d): Box A detail-route proceeds; digital G detail cases are excluded by the named digital-asset refusal.
Reviewed in: pass 790975e2b01d

### 1b(e) — Line 1b, column (e) totals
Status: **MATCH**

Model: Matches line 1b column (e): reported basis for Box A detail-route transactions; digital G cases are excluded by the named refusal.
Reviewed in: pass 790975e2b01d

### 1b(g) — Line 1b, column (g) totals
Status: **MATCH**

Model: Matches line 1b column (g): net supported B and W adjustments for Box A detail-route transactions; other codes are refused.
Reviewed in: pass 790975e2b01d

### 1b(h) — Line 1b, column (h) totals
Status: **MATCH**

Model: Matches line 1b column (h): proceeds less basis plus column (g) adjustments.
Reviewed in: pass 790975e2b01d

### 2(d) — Line 2, column (d) totals
Status: **MATCH**

Model: Matches line 2 column (d): Box B detail-route proceeds; digital H cases are excluded by the named digital-asset refusal.
Reviewed in: pass 790975e2b01d

### 2(e) — Line 2, column (e) totals
Status: **MATCH**

Model: Matches line 2 column (e): correct basis for Box B transactions where basis was not reported to the IRS; digital H cases are excluded.
Reviewed in: pass 790975e2b01d

### 2(g) — Line 2, column (g) totals
Status: **MATCH**

Model: Matches line 2 column (g): supported net adjustments, including wash-sale losses, for Box B detail-route transactions.
Reviewed in: pass 790975e2b01d

### 2(h) — Line 2, column (h) totals
Status: **MATCH**

Model: Matches line 2 column (h): proceeds less basis plus column (g) adjustments.
Reviewed in: pass 790975e2b01d

### 3(d) — Line 3, column (d) totals
Status: **MATCH**

Model: Matches line 3 column (d): Box C detail-route proceeds; digital I cases are excluded by the named digital-asset refusal.
Reviewed in: pass 790975e2b01d

### 3(e) — Line 3, column (e) totals
Status: **MATCH**

Model: Matches line 3 column (e): correct basis for Box C transactions not reported on Form 1099-B or Form 1099-DA; digital I cases are excluded.
Reviewed in: pass 790975e2b01d

### 3(g) — Line 3, column (g) totals
Status: **MATCH**

Model: Matches line 3 column (g): supported net adjustments for Box C detail-route transactions.
Reviewed in: pass 790975e2b01d

### 3(h) — Line 3, column (h) totals
Status: **MATCH**

Model: Matches line 3 column (h): proceeds less basis plus column (g) adjustments.
Reviewed in: pass 790975e2b01d

### 8a(d) — Line 8a, column (d) totals
Status: **MATCH**

Model: Matches line 8a column (d): long-term basis-reported no-adjustment aggregate proceeds; digital J cases are excluded by the named digital-asset refusal.
Reviewed in: pass 790975e2b01d

### 8a(e) — Line 8a, column (e) totals
Status: **MATCH**

Model: Matches line 8a column (e): reported cost or other basis for long-term basis-reported no-adjustment aggregate transactions; digital J cases are excluded.
Reviewed in: pass 790975e2b01d

### 8a(g) — Line 8a, column (g) totals
Status: **MATCH**

Model: Matches line 8a column (g) within supported aggregate cases; no adjustments are allowed on line 8a, and invalid adjustment cases are refused.
Reviewed in: pass 790975e2b01d

### 8a(h) — Line 8a, column (h) totals
Status: **MATCH**

Model: Matches line 8a column (h): proceeds less column (e) plus column (g) for supported long-term aggregate transactions.
Reviewed in: pass 790975e2b01d

### 8b(d) — Line 8b, column (d) totals
Status: **MATCH**

Model: Matches line 8b column (d): Box D detail-route proceeds; digital J detail cases are excluded by the named digital-asset refusal.
Reviewed in: pass 790975e2b01d

### 8b(e) — Line 8b, column (e) totals
Status: **MATCH**

Model: Matches line 8b column (e): reported basis for Box D detail-route transactions; digital J cases are excluded.
Reviewed in: pass 790975e2b01d

### 8b(g) — Line 8b, column (g) totals
Status: **MATCH**

Model: Matches line 8b column (g): net supported B and W adjustments for Box D detail-route transactions.
Reviewed in: pass 790975e2b01d

### 8b(h) — Line 8b, column (h) totals
Status: **MATCH**

Model: Matches line 8b column (h): proceeds less basis plus column (g) adjustments.
Reviewed in: pass 790975e2b01d

### 9(d) — Line 9, column (d) totals
Status: **MATCH**

Model: Matches line 9 column (d): Box E detail-route proceeds; digital K cases are excluded by the named digital-asset refusal.
Reviewed in: pass 790975e2b01d

### 9(e) — Line 9, column (e) totals
Status: **MATCH**

Model: Matches line 9 column (e): correct basis for Box E transactions where basis was not reported to the IRS; digital K cases are excluded.
Reviewed in: pass 790975e2b01d

### 9(g) — Line 9, column (g) totals
Status: **MATCH**

Model: Matches line 9 column (g): supported net adjustments for Box E detail-route transactions.
Reviewed in: pass 790975e2b01d

### 9(h) — Line 9, column (h) totals
Status: **MATCH**

Model: Matches line 9 column (h): proceeds less basis plus column (g) adjustments.
Reviewed in: pass 790975e2b01d

### 10(d) — Line 10, column (d) totals
Status: **MATCH**

Model: Matches line 10 column (d): Box F detail-route proceeds; digital L cases are excluded by the named digital-asset refusal.
Reviewed in: pass 790975e2b01d

### 10(e) — Line 10, column (e) totals
Status: **MATCH**

Model: Matches line 10 column (e): correct basis for Box F transactions not reported on Form 1099-B or Form 1099-DA; digital L cases are excluded.
Reviewed in: pass 790975e2b01d

### 10(g) — Line 10, column (g) totals
Status: **MATCH**

Model: Matches line 10 column (g): supported net adjustments for Box F detail-route transactions.
Reviewed in: pass 790975e2b01d

### 10(h) — Line 10, column (h) totals
Status: **MATCH**

Model: Matches line 10 column (h): proceeds less basis plus column (g) adjustments.
Reviewed in: pass 790975e2b01d

### 4 — Line 4: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 4 is zero when no other-source form gains apply, and the refusal excludes those forms when present.

### 5 — Line 5: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 5 is zero when no Schedule K-1 or other-source gains apply, with those cases refused.

### 6 — Short-term capital loss carryover, from line 8 of the Capital Loss Carryover Worksheet (a
Status: **MATCH**

Model: Line 6 correctly uses the Capital Loss Carryover Worksheet line 8 as a negative loss when the 2024 line 21 loss condition is met, otherwise zero.

### 11 — Line 11: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 11 is zero when no other-source long-term gains apply, with those forms refused.

### 12 — Line 12: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 12 is zero when no Schedule K-1 or other-source long-term gains apply, with those cases refused.

### 14 — Long-term capital loss carryover, from line 13 of the Capital Loss Carryover Worksheet (a
Status: **MATCH**

Model: Line 14 correctly uses the Capital Loss Carryover Worksheet line 13 as a negative loss when the 2024 line 21 loss condition is met, otherwise zero.

### 13 — Capital gain distributions
Status: **MATCH**

Model: Schedule D line 13 is capital gain distributions; the restatement uses the Form 1099-DIV box 2a capital gain distributions helper subject to distribution screening.
Reviewed in: pass 577abbc56b37

### 7 — Combine the amounts for Schedule D line 7
Status: **MATCH**

Model: Matches Schedule D line 7: combines lines 1a through 6 in column (h).
Reviewed in: pass 790975e2b01d

### 15 — Combine the amounts for Schedule D line 15
Status: **MATCH**

Model: The IRS text says to combine lines 8a through 14 in column (h), and the restatement adds the same lines, with line 14 treated as a negative loss.
Reviewed in: pass 577abbc56b37

### 16 — Combine the amounts for Schedule D line 16
Status: **MATCH**

Model: Line 16 correctly combines lines 7 and 15.

### 17 — Are lines 15 and 16 both gains?
Status: **MATCH**

Model: Line 17 correctly tests whether lines 15 and 16 are both positive gains.

### 20 — Are lines 18 and 19 zero and are you not filing Form 4952?
Status: **MATCH**

Model: The IRS text asks whether lines 18 and 19 are both zero or blank and whether Form 4952 is not being filed, which is what the restatement checks.
Reviewed in: pass 577abbc56b37

### 21 — Deductible loss, signed; zero when line 21 is skipped
Status: **MATCH**

Model: Line 21 correctly applies the smaller positive loss limit by taking the larger of the signed line 16 loss and the signed annual limit, entering the result as a loss.

### 22 — Do you have qualified dividends?
Status: **MATCH**

Model: The IRS text asks whether there are qualified dividends on Form 1040 line 3a, and the restatement checks whether qualified dividends are greater than zero.
Reviewed in: pass 577abbc56b37

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| 1a(d) | 3bee05cac71f53f3d78d26ecc947f6b8d4a39e3a07c048dbf8c6561261da0cb3 |
| 1a(e) | dd91e7a1dd80c85ff323decdd4bb8d539743bfa0bdbd49bdc7c7f563763445f0 |
| 1a(g) | 7729dc65d5eee64c3ddc0023a8076c61bd9ba3aaeddf20236368a06a4e32a9f9 |
| 1a(h) | 76d0fd19c94dd2674dc9dfd067a38fb1c0369568824cd1feace141efadddff32 |
| 1b(d) | 0d80e82611214999218549f12740bfaa4960437f08bb1491092b7212db39880a |
| 1b(e) | 48ceaa71218911e327574465eb9802082ac9e0daa6f2347f4c4494186edea8b1 |
| 1b(g) | bd6d6ed0b7f99d9eb90ccb85d816396f326bb11bbba6cbcc860caf4ecea12c7b |
| 1b(h) | faaf5dfe3bc0127faf76d68b3d39cc392fea2fa18125aeaf87c0ea1062ce31ac |
| 2(d) | d772a1293664eeb806502e1d10580416255ea8f84a838ebc6526cf5aa4c0d595 |
| 2(e) | cd3592a81ad8d4a3acd16c705de8f926571b25110144c0646fefef1f36e1d1e7 |
| 2(g) | 78bbc2b4cd507aa20aea002a2529b69e7f46e9086e306c4b60aefb316013aa0f |
| 2(h) | bc3a118fc2550e059ef4f4f52c8cc2925054f91995ee44249542b66aba69d8ec |
| 3(d) | 20eec0db6b9f5d8a3e1d35123bb6f1da2b3983b66adb7954c2008ecf0fa8b0c7 |
| 3(e) | f151c4b82145cee97dec6060df7080e6b89532f0ea9e09dc3131b21498c678de |
| 3(g) | 09219ae7715e614dcf6f963b0f1b007a2a53c00b87dc4c2e840e296f3d98037b |
| 3(h) | d4f546067a00d65edbc76372bc1e2577b8391616a1e05714bbe953db5659e72d |
| 8a(d) | b4134746aaca52f0b6d8dcd91e6d8e5c9469697badd48bcf2465f74a852398f8 |
| 8a(e) | 282db986e8c73de6ac571187057d76b19c1ca13cbb6a8c48387339a0040badfc |
| 8a(g) | 2c7d245264d42229c2755688328b669993309f0a109df162c715dece41269a86 |
| 8a(h) | 015236a2931ff5562b8ea267edda7f5a9c6ac050d7f4115b80550bdb13f131e6 |
| 8b(d) | 668f55d47f07d496e52df7c5907f350bb87eba75b00526c3974087a164390f6d |
| 8b(e) | f2ea7e54680ee86ceadc5810eb16b167c51f734e58e8766e1ee39fedfd7825e7 |
| 8b(g) | 9269902b97764279a2bb50f4189723d1e561d54360111321580a6c496c5ec9e6 |
| 8b(h) | 9c68703e94e218793ad99367a984ad6603720b42ca7b6bed19e4405af1a52ac6 |
| 9(d) | 98b830231b4673ce75733ff4794e328562ad5f662b6832645e6d79ef9663a8cd |
| 9(e) | 8955c31d9eefed98817945f71009ba9eed541fe247a9a6cb752a4714a2c17dae |
| 9(g) | d64dc1903def1c74cce438fc93f3538018ed1cbaa2d655943cded427b2bff4e7 |
| 9(h) | 367265e1e0762a7e72071807a191fec220085a941e8b0ec07fa84b1cabae4765 |
| 10(d) | b2418e70e11bf5216c7757cfb6ec84bdb56d2cbb8a478508126cc0074cd3f07d |
| 10(e) | b22f066aba03b7649a3688374252aa2128bad7c32780dd8727162da5ddbe3e86 |
| 10(g) | 72752701757475cc7b0522dd116d8dc3b9133e0ecbe51f94fab1e03bc5903ffd |
| 10(h) | 31ad9a12544efe55f1459f4d5c1e5f54844bcf6ec5b229dce2316bc702b4089f |
| 4 | fc140fb363c2880a6ad4044547d651a95f3e0b2331f4c8f24148a188cd5eb60a |
| 5 | f717c41fbbeaebe05ba5f6d4487fc21983ef8650db4ae4a71665c900956fbedb |
| 6 | 71e9facbb1accd7b9339b79993aaab8d2829f113250db0b7ee1bdcf2ffae80aa |
| 11 | f771edaa32d289030a74d7189648bab320f53c24543262825a52bff3fc797449 |
| 12 | 6b73101b3aad0baea3bd1a2ca3d6212077528516b286cb108a32f972c036671e |
| 14 | 647156c672e55b5f86525437cb48b58f7e69078c9e39ca7e1ba8b729b780c3a6 |
| 13 | 4a683e41f2f2cb3103646519b99f211042a98a517bf9dc0cdc3c0602af126761 |
| 7 | dbf8a9a44f37b3cf67dc555dbf48a8664b9a8ebbedfc49924ddb781c800a0110 |
| 15 | 57bf70b5fdc5e71a80d07bea9dd84b3cd595a370d853f98925e381e4272a7921 |
| 16 | 0f76ecb634638a67f68c0728370c592d43b31b38b3ccde6dc6c2d7c174edb44e |
| 17 | 31117d838592d91e2901cdbbbc25ab6ddde06e1f462f23a3d043c8974973312d |
| 20 | d06d7e43fd62877e184baaa7cb93a6e4df537890a8e9231029ddbc3b2f22a835 |
| 21 | 01ed960f703ca2f324cbc7f80d1669824b80307f2b0302c0e053541c678be277 |
| 22 | 336f2a96ba7ce335826970badbf2d93af7cf24106542da2b2dec8d2c02177ee1 |
| (rest of the document) | 9b5ec474c37e31a1a667821669b753fb7357857a86f4d07c43af9f9de2bff699 |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass 577abbc56b37

| field | value |
| --- | --- |
| date | 2026-11-07 |
| review scope | lines 13, 15, 20, 22 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 577abbc56b37d1cebe808323852558d3bd94585db765f728dbf63e0577cd43fe |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 884443bc10a74221ffffae8b97356b0c0610d7129346cbeb06b585fdb1bbc439 |
| receipt | .transcription/sd.deepseek.render.lines-6a3b38decded |
| lines judged | 4 |
| match / mismatch / unclear / missing | 4 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sd | 2025; printed date 2025-12-11 | 8, 11, 12 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 8, 11, 12 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| f1040sd | 2025; created 2025-10-06 | 1, 2 | whole document | 221151530f7cd599e8ad00bc3e1ba62d6b7ff34e402c336f4ae58d698c9f5187 | - | eb461181b39879c79d1c0b7761ca0cd9ade46fdb1531cdee3281053c348f6c41 |
| i1040gi | 2025; printed date 2026-02-25 | 25, 26, 38 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 25, 26 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| f1099div | January 2024 (continuous-use form) | 1, 2, 3, 4, 5, 6 | whole document | 833d93e5f2d0bfcc8c9d720c0e8cb8e623cd2c6a8ee25f364f1f69f49fa490e3 | 5 | 617419bd079b1520174ceca8549065c9e4001f2b06a16d1425c5469bbe49fa3d |
| f4952 | 2025; created 2025-05-28 | 1, 2, 3, 4 | whole document | efbeec4c44a1e43fb00231942c811a454d86b3632a2a662238893f8c4595bf81 | 3, 4 | c98eb27a83a89faecfdd0cd6597e8063fbd86a14ba1606f3e96c1c5f016d2b5c |
| i1040sb | TY2025; printed April 23, 2025 | 1, 2, 3 | whole document | 2bf62267574473b36fd9a69b6e0837ef74d72ac7d5dcbf1d26e7047d099f1e05 | 1, 2, 3 | 0d38b25d416cb650ef264faf8c1f118dfa4666f3949fbba7120f8c04d4e6914e |
| f8995 | 2025; created 2025-09-12 | 1 | whole document | 49922587df3bd093e24470f5b42d0e3382ef8f5210b3cedccb02ccb864f2f65a | - | 8e2e78d7610e1d45e93c10c8b03f9026d46a1166678c6ed93f852569c382f346 |
| i8995 | 2025; printed date 2026-01-26 | 3, 4 | pages named by another document's citation | 96284eaad2fe5ec324de9fd4335cea9ea3260e66ff1d8b1725c1cff7fbe1ddc2 | 3, 4 | 6671a64ba0011f89e03eb5985954073dcd984b3f346495182916b0ecaa42ec1a |

##### Raw response

```yaml
lines:
  - key: "13"
    status: MATCH
    reason: "Schedule D line 13 is capital gain distributions; the restatement uses the Form 1099-DIV box 2a capital gain distributions helper subject to distribution screening."
  - key: "15"
    status: MATCH
    reason: "The IRS text says to combine lines 8a through 14 in column (h), and the restatement adds the same lines, with line 14 treated as a negative loss."
  - key: "20"
    status: MATCH
    reason: "The IRS text asks whether lines 18 and 19 are both zero or blank and whether Form 4952 is not being filed, which is what the restatement checks."
  - key: "22"
    status: MATCH
    reason: "The IRS text asks whether there are qualified dividends on Form 1040 line 3a, and the restatement checks whether qualified dividends are greater than zero."
```

#### Pass 790975e2b01d

| field | value |
| --- | --- |
| date | 2026-11-07 |
| review scope | lines 1a(d), 1a(e), 1a(g), 1a(h), 1b(d), 1b(e), 1b(g), 1b(h), 2(d), 2(e), 2(g), 2(h), 3(d), 3(e), 3(g), 3(h), 8a(d), 8a(e), 8a(g), 8a(h), 8b(d), 8b(e), 8b(g), 8b(h), 9(d), 9(e), 9(g), 9(h), 10(d), 10(e), 10(g), 10(h), 7, 15 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 790975e2b01d251806ec7900a96a0b7cb849c378d67aa63773d66eba4ffdf4e0 |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 329cc96b9d07419958471ec059f8d25fd2da2c05e9915067d6fad57d1b87a01d |
| receipt | .transcription/sd.deepseek.render.lines-c9db5685c8a4 |
| lines judged | 34 |
| match / mismatch / unclear / missing | 34 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sd | 2025; created 2025-10-06 | 1, 2 | whole document | 221151530f7cd599e8ad00bc3e1ba62d6b7ff34e402c336f4ae58d698c9f5187 | - | eb461181b39879c79d1c0b7761ca0cd9ade46fdb1531cdee3281053c348f6c41 |
| i8949 | 2025; printed date 2026-01-20 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 | cited pages | d3ddc2b91cf89087ca348ebb00dbd1c80bbc025fa4df1176753d25013f581a67 | 2, 3, 4, 5, 6, 7, 9, 10 | cabdc81a0677c0e4de4a89f9a71d328395c4cc839206ebadb56aeb54bf954b85 |
| f8949 | 2025; created 2025-05-05 | 1, 2 | whole document | f191f96ca2847b4c59875d5e1169f784a79b4d57f1f12d0196bd9bc2e7838e9d | - | cc308c3ff7751456647bed9c2855d077dcbd0a55469b57f9e8cccb6f4927f232 |
| i1040sd | 2025; printed date 2025-12-11 | 5, 6, 10, 11, 12 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 5, 6, 11, 12 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| p550 | 2025 returns; printed date 2026-03-05 | 59, 60, 61, 81, 82, 86, 87, 88 | pages named by another document's citation | e40622e028486d7eb31a6da342ba2ba3c8b2f7ea9d341d9f47a1d33407d5aa26 | 59, 60, 61, 81, 82, 86, 87, 88 | 7629580e9cb35aa5f67e5d7c035b45850164eb1fe458f8acaa2781578ad0bf51 |

##### Raw response

```yaml
lines:
  - key: "1a(d)"
    status: MATCH
    reason: "Matches Schedule D line 1a column (d): short-term basis-reported no-adjustment aggregate proceeds; digital G cases are excluded by the named digital-asset refusal."
  - key: "1a(e)"
    status: MATCH
    reason: "Matches line 1a column (e): reported cost or other basis for short-term basis-reported no-adjustment aggregate transactions; digital G cases are excluded by the named refusal."
  - key: "1a(g)"
    status: MATCH
    reason: "Matches line 1a column (g) within supported aggregate cases; no adjustments are allowed on line 1a, and invalid adjustment cases are refused."
  - key: "1a(h)"
    status: MATCH
    reason: "Matches line 1a column (h): proceeds less column (e) plus column (g) for the supported short-term aggregate transactions."
  - key: "1b(d)"
    status: MATCH
    reason: "Matches line 1b column (d): Box A detail-route proceeds; digital G detail cases are excluded by the named digital-asset refusal."
  - key: "1b(e)"
    status: MATCH
    reason: "Matches line 1b column (e): reported basis for Box A detail-route transactions; digital G cases are excluded by the named refusal."
  - key: "1b(g)"
    status: MATCH
    reason: "Matches line 1b column (g): net supported B and W adjustments for Box A detail-route transactions; other codes are refused."
  - key: "1b(h)"
    status: MATCH
    reason: "Matches line 1b column (h): proceeds less basis plus column (g) adjustments."
  - key: "2(d)"
    status: MATCH
    reason: "Matches line 2 column (d): Box B detail-route proceeds; digital H cases are excluded by the named digital-asset refusal."
  - key: "2(e)"
    status: MATCH
    reason: "Matches line 2 column (e): correct basis for Box B transactions where basis was not reported to the IRS; digital H cases are excluded."
  - key: "2(g)"
    status: MATCH
    reason: "Matches line 2 column (g): supported net adjustments, including wash-sale losses, for Box B detail-route transactions."
  - key: "2(h)"
    status: MATCH
    reason: "Matches line 2 column (h): proceeds less basis plus column (g) adjustments."
  - key: "3(d)"
    status: MATCH
    reason: "Matches line 3 column (d): Box C detail-route proceeds; digital I cases are excluded by the named digital-asset refusal."
  - key: "3(e)"
    status: MATCH
    reason: "Matches line 3 column (e): correct basis for Box C transactions not reported on Form 1099-B or Form 1099-DA; digital I cases are excluded."
  - key: "3(g)"
    status: MATCH
    reason: "Matches line 3 column (g): supported net adjustments for Box C detail-route transactions."
  - key: "3(h)"
    status: MATCH
    reason: "Matches line 3 column (h): proceeds less basis plus column (g) adjustments."
  - key: "8a(d)"
    status: MATCH
    reason: "Matches line 8a column (d): long-term basis-reported no-adjustment aggregate proceeds; digital J cases are excluded by the named digital-asset refusal."
  - key: "8a(e)"
    status: MATCH
    reason: "Matches line 8a column (e): reported cost or other basis for long-term basis-reported no-adjustment aggregate transactions; digital J cases are excluded."
  - key: "8a(g)"
    status: MATCH
    reason: "Matches line 8a column (g) within supported aggregate cases; no adjustments are allowed on line 8a, and invalid adjustment cases are refused."
  - key: "8a(h)"
    status: MATCH
    reason: "Matches line 8a column (h): proceeds less column (e) plus column (g) for supported long-term aggregate transactions."
  - key: "8b(d)"
    status: MATCH
    reason: "Matches line 8b column (d): Box D detail-route proceeds; digital J detail cases are excluded by the named digital-asset refusal."
  - key: "8b(e)"
    status: MATCH
    reason: "Matches line 8b column (e): reported basis for Box D detail-route transactions; digital J cases are excluded."
  - key: "8b(g)"
    status: MATCH
    reason: "Matches line 8b column (g): net supported B and W adjustments for Box D detail-route transactions."
  - key: "8b(h)"
    status: MATCH
    reason: "Matches line 8b column (h): proceeds less basis plus column (g) adjustments."
  - key: "9(d)"
    status: MATCH
    reason: "Matches line 9 column (d): Box E detail-route proceeds; digital K cases are excluded by the named digital-asset refusal."
  - key: "9(e)"
    status: MATCH
    reason: "Matches line 9 column (e): correct basis for Box E transactions where basis was not reported to the IRS; digital K cases are excluded."
  - key: "9(g)"
    status: MATCH
    reason: "Matches line 9 column (g): supported net adjustments for Box E detail-route transactions."
  - key: "9(h)"
    status: MATCH
    reason: "Matches line 9 column (h): proceeds less basis plus column (g) adjustments."
  - key: "10(d)"
    status: MATCH
    reason: "Matches line 10 column (d): Box F detail-route proceeds; digital L cases are excluded by the named digital-asset refusal."
  - key: "10(e)"
    status: MATCH
    reason: "Matches line 10 column (e): correct basis for Box F transactions not reported on Form 1099-B or Form 1099-DA; digital L cases are excluded."
  - key: "10(g)"
    status: MATCH
    reason: "Matches line 10 column (g): supported net adjustments for Box F detail-route transactions."
  - key: "10(h)"
    status: MATCH
    reason: "Matches line 10 column (h): proceeds less basis plus column (g) adjustments."
  - key: "7"
    status: MATCH
    reason: "Matches Schedule D line 7: combines lines 1a through 6 in column (h)."
  - key: "15"
    status: MATCH
    reason: "Matches Schedule D line 15: combines lines 8a through 14 in column (h)."
```

## Raw response

```yaml
lines:
  - key: "1a(d)"
    status: MATCH
    reason: 'Restatement correctly totals column (d) proceeds for the short-term basis-reported aggregate route, with digital and unsupported cases excluded by refusal.'
  - key: "1a(e)"
    status: MATCH
    reason: 'Restatement correctly totals column (e) basis for the short-term basis-reported aggregate route.'
  - key: "1a(g)"
    status: MATCH
    reason: 'For supported aggregate short-term basis-reported transactions there are no adjustments, so the column (g) total is zero.'
  - key: "1a(h)"
    status: MATCH
    reason: 'Restatement correctly totals column (h) gain or loss as proceeds less basis plus adjustments.'
  - key: "1b(d)"
    status: MATCH
    reason: 'Restatement correctly totals column (d) proceeds for short-term basis-reported detail transactions reported on Form 8949.'
  - key: "1b(e)"
    status: MATCH
    reason: 'Restatement correctly totals column (e) basis for short-term basis-reported detail transactions.'
  - key: "1b(g)"
    status: MATCH
    reason: 'Restatement correctly totals supported column (g) adjustments for short-term basis-reported detail transactions.'
  - key: "1b(h)"
    status: MATCH
    reason: 'Restatement correctly totals column (h) gain or loss for short-term basis-reported detail transactions.'
  - key: "2(d)"
    status: MATCH
    reason: 'Restatement correctly totals column (d) proceeds for short-term transactions with basis not reported to the IRS.'
  - key: "2(e)"
    status: MATCH
    reason: 'Restatement correctly totals column (e) basis for short-term transactions with basis not reported to the IRS.'
  - key: "2(g)"
    status: MATCH
    reason: 'Restatement correctly totals supported column (g) adjustments for short-term transactions with basis not reported.'
  - key: "2(h)"
    status: MATCH
    reason: 'Restatement correctly totals column (h) gain or loss for short-term transactions with basis not reported.'
  - key: "3(d)"
    status: MATCH
    reason: 'Restatement correctly totals column (d) proceeds for short-term transactions not reported on Form 1099-B or Form 1099-DA.'
  - key: "3(e)"
    status: MATCH
    reason: 'Restatement correctly totals column (e) basis for short-term transactions not reported on Form 1099-B or Form 1099-DA.'
  - key: "3(g)"
    status: MATCH
    reason: 'Restatement correctly totals supported column (g) adjustments for short-term transactions not reported on Form 1099-B or Form 1099-DA.'
  - key: "3(h)"
    status: MATCH
    reason: 'Restatement correctly totals column (h) gain or loss for short-term transactions not reported on Form 1099-B or Form 1099-DA.'
  - key: "8a(d)"
    status: MATCH
    reason: 'Restatement correctly totals column (d) proceeds for the long-term basis-reported aggregate route.'
  - key: "8a(e)"
    status: MATCH
    reason: 'Restatement correctly totals column (e) basis for the long-term basis-reported aggregate route.'
  - key: "8a(g)"
    status: MATCH
    reason: 'For supported aggregate long-term basis-reported transactions there are no adjustments, so the column (g) total is zero.'
  - key: "8a(h)"
    status: MATCH
    reason: 'Restatement correctly totals column (h) gain or loss for the long-term basis-reported aggregate route.'
  - key: "8b(d)"
    status: MATCH
    reason: 'Restatement correctly totals column (d) proceeds for long-term basis-reported detail transactions reported on Form 8949.'
  - key: "8b(e)"
    status: MATCH
    reason: 'Restatement correctly totals column (e) basis for long-term basis-reported detail transactions.'
  - key: "8b(g)"
    status: MATCH
    reason: 'Restatement correctly totals supported column (g) adjustments for long-term basis-reported detail transactions.'
  - key: "8b(h)"
    status: MATCH
    reason: 'Restatement correctly totals column (h) gain or loss for long-term basis-reported detail transactions.'
  - key: "9(d)"
    status: MATCH
    reason: 'Restatement correctly totals column (d) proceeds for long-term transactions with basis not reported to the IRS.'
  - key: "9(e)"
    status: MATCH
    reason: 'Restatement correctly totals column (e) basis for long-term transactions with basis not reported to the IRS.'
  - key: "9(g)"
    status: MATCH
    reason: 'Restatement correctly totals supported column (g) adjustments for long-term transactions with basis not reported.'
  - key: "9(h)"
    status: MATCH
    reason: 'Restatement correctly totals column (h) gain or loss for long-term transactions with basis not reported.'
  - key: "10(d)"
    status: MATCH
    reason: 'Restatement correctly totals column (d) proceeds for long-term transactions not reported on Form 1099-B or Form 1099-DA.'
  - key: "10(e)"
    status: MATCH
    reason: 'Restatement correctly totals column (e) basis for long-term transactions not reported on Form 1099-B or Form 1099-DA.'
  - key: "10(g)"
    status: MATCH
    reason: 'Restatement correctly totals supported column (g) adjustments for long-term transactions not reported on Form 1099-B or Form 1099-DA.'
  - key: "10(h)"
    status: MATCH
    reason: 'Restatement correctly totals column (h) gain or loss for long-term transactions not reported on Form 1099-B or Form 1099-DA.'
  - key: "4"
    status: MATCH
    reason: 'Line 4 is zero when no other-source form gains apply, and the refusal excludes those forms when present.'
  - key: "5"
    status: MATCH
    reason: 'Line 5 is zero when no Schedule K-1 or other-source gains apply, with those cases refused.'
  - key: "6"
    status: MATCH
    reason: 'Line 6 correctly uses the Capital Loss Carryover Worksheet line 8 as a negative loss when the 2024 line 21 loss condition is met, otherwise zero.'
  - key: "11"
    status: MATCH
    reason: 'Line 11 is zero when no other-source long-term gains apply, with those forms refused.'
  - key: "12"
    status: MATCH
    reason: 'Line 12 is zero when no Schedule K-1 or other-source long-term gains apply, with those cases refused.'
  - key: "14"
    status: MATCH
    reason: 'Line 14 correctly uses the Capital Loss Carryover Worksheet line 13 as a negative loss when the 2024 line 21 loss condition is met, otherwise zero.'
  - key: "13"
    status: MATCH
    reason: 'Line 13 correctly uses the capital gain distributions amount, with distribution scope checks refusing unsupported special cases.'
  - key: "7"
    status: MATCH
    reason: 'Line 7 correctly combines lines 1a through 6 in column (h).'
  - key: "15"
    status: MATCH
    reason: 'Line 15 correctly combines lines 8a through 14 in column (h).'
  - key: "16"
    status: MATCH
    reason: 'Line 16 correctly combines lines 7 and 15.'
  - key: "17"
    status: MATCH
    reason: 'Line 17 correctly tests whether lines 15 and 16 are both positive gains.'
  - key: "20"
    status: MISMATCH
    reason: 'The form says if line 17 is No, skip lines 18 through 21 and go to line 22; the restatement evaluates line 20 from zeroed lines 18 and 19 without requiring line 17 to be Yes.'
  - key: "21"
    status: MATCH
    reason: 'Line 21 correctly applies the smaller positive loss limit by taking the larger of the signed line 16 loss and the signed annual limit, entering the result as a loss.'
  - key: "22"
    status: MATCH
    reason: 'Line 22 correctly tests whether Form 1040 line 3a qualified dividends are greater than zero.'
```
