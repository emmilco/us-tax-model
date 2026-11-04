# Render comparison — sd

The rendered English of every printed line of `Schedule D — securities sales and supplied distribution subtotals` (`rendered/2025/sd.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| line-scoped reviews | 1 (latest 2026-11-04); see Line-scoped reviews |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | d8a1bade7e8895260afb189920619c7b281ba3f35ca05706a6924a7e0636eac5 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | eeaf337d5fa7492478be5ffa58f4ffcda447017332dba311b038e96279119959 |
| lines judged | 46 |
| match / mismatch / unclear / missing | 45 / 1 / 0 / 0 |
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

Model: It computes column (d) proceeds for short-term basis-reported, no-adjustment transactions in the supported box A aggregate case; digital G–L cases are excluded by refusal.
Reviewed in: pass 6d1419919e1c

### 1a(e) — Line 1a, column (e) totals
Status: **MATCH**

Model: It computes column (e) basis for the same box A aggregate-route transactions, where reported basis is the required basis because no adjustments are allowed.
Reviewed in: pass 6d1419919e1c

### 1a(g) — Line 1a, column (g) totals
Status: **MATCH**

Model: Line 1a permits no adjustments; within the aggregate-route eligibility gate sales.g is zero, so summing it matches the line's adjustment column.
Reviewed in: pass 6d1419919e1c

### 1a(h) — Line 1a, column (h) totals
Status: **MATCH**

Model: It computes column (h) as proceeds less column (e) plus column (g), matching Schedule D line 1a column (h).
Reviewed in: pass 6d1419919e1c

### 1b(d) — Line 1b, column (d) totals
Status: **MATCH**

Model: It computes column (d) proceeds for box A detail-route transactions reported on Form 8949; box G digital cases are excluded by refusal.
Reviewed in: pass 6d1419919e1c

### 1b(e) — Line 1b, column (e) totals
Status: **MATCH**

Model: It computes column (e) basis for box A detail-route transactions, using reported basis where required and allowing the adjustment column to correct it.
Reviewed in: pass 6d1419919e1c

### 1b(g) — Line 1b, column (g) totals
Status: **MATCH**

Model: It computes column (g) net adjustments for box A detail-route transactions, limited to supported B and W adjustments.
Reviewed in: pass 6d1419919e1c

### 1b(h) — Line 1b, column (h) totals
Status: **MATCH**

Model: It computes column (h) as proceeds less basis plus adjustments, matching Form 8949 and Schedule D line 1b column (h).
Reviewed in: pass 6d1419919e1c

### 2(d) — Line 2, column (d) totals
Status: **MATCH**

Model: It computes column (d) proceeds for box B detail-route transactions; box H digital cases are excluded by refusal.
Reviewed in: pass 6d1419919e1c

### 2(e) — Line 2, column (e) totals
Status: **MATCH**

Model: It computes column (e) basis for box B detail-route transactions, where basis was not reported and the correct basis is required.
Reviewed in: pass 6d1419919e1c

### 2(g) — Line 2, column (g) totals
Status: **MATCH**

Model: It computes column (g) net adjustments for box B detail-route transactions, limited to supported B and W adjustments.
Reviewed in: pass 6d1419919e1c

### 2(h) — Line 2, column (h) totals
Status: **MATCH**

Model: It computes column (h) as proceeds less basis plus adjustments, matching Schedule D line 2 column (h).
Reviewed in: pass 6d1419919e1c

### 3(d) — Line 3, column (d) totals
Status: **MATCH**

Model: It computes column (d) proceeds for box C detail-route transactions; box I digital cases are excluded by refusal.
Reviewed in: pass 6d1419919e1c

### 3(e) — Line 3, column (e) totals
Status: **MATCH**

Model: It computes column (e) basis for box C detail-route transactions, using the correct basis where no broker basis was reported.
Reviewed in: pass 6d1419919e1c

### 3(g) — Line 3, column (g) totals
Status: **MATCH**

Model: It computes column (g) net adjustments for box C detail-route transactions, limited to supported B and W adjustments.
Reviewed in: pass 6d1419919e1c

### 3(h) — Line 3, column (h) totals
Status: **MATCH**

Model: It computes column (h) as proceeds less basis plus adjustments, matching Schedule D line 3 column (h).
Reviewed in: pass 6d1419919e1c

### 8a(d) — Line 8a, column (d) totals
Status: **MATCH**

Model: It computes column (d) proceeds for long-term basis-reported, no-adjustment transactions in the supported box D aggregate case; digital J–L cases are excluded by refusal.
Reviewed in: pass 6d1419919e1c

### 8a(e) — Line 8a, column (e) totals
Status: **MATCH**

Model: It computes column (e) basis for the same box D aggregate-route transactions, where reported basis is the required basis because no adjustments are allowed.
Reviewed in: pass 6d1419919e1c

### 8a(g) — Line 8a, column (g) totals
Status: **MATCH**

Model: Line 8a permits no adjustments; within the aggregate-route eligibility gate sales.g is zero, so summing it matches the line's adjustment column.
Reviewed in: pass 6d1419919e1c

### 8a(h) — Line 8a, column (h) totals
Status: **MATCH**

Model: It computes column (h) as proceeds less column (e) plus column (g), matching Schedule D line 8a column (h).
Reviewed in: pass 6d1419919e1c

### 8b(d) — Line 8b, column (d) totals
Status: **MATCH**

Model: It computes column (d) proceeds for box D detail-route transactions reported on Form 8949; box J digital cases are excluded by refusal.
Reviewed in: pass 6d1419919e1c

### 8b(e) — Line 8b, column (e) totals
Status: **MATCH**

Model: It computes column (e) basis for box D detail-route transactions, using reported basis where required and allowing the adjustment column to correct it.
Reviewed in: pass 6d1419919e1c

### 8b(g) — Line 8b, column (g) totals
Status: **MATCH**

Model: It computes column (g) net adjustments for box D detail-route transactions, limited to supported B and W adjustments.
Reviewed in: pass 6d1419919e1c

### 8b(h) — Line 8b, column (h) totals
Status: **MATCH**

Model: It computes column (h) as proceeds less basis plus adjustments, matching Form 8949 and Schedule D line 8b column (h).
Reviewed in: pass 6d1419919e1c

### 9(d) — Line 9, column (d) totals
Status: **MATCH**

Model: It computes column (d) proceeds for box E detail-route transactions; box K digital cases are excluded by refusal.
Reviewed in: pass 6d1419919e1c

### 9(e) — Line 9, column (e) totals
Status: **MATCH**

Model: It computes column (e) basis for box E detail-route transactions, where basis was not reported and the correct basis is required.
Reviewed in: pass 6d1419919e1c

### 9(g) — Line 9, column (g) totals
Status: **MATCH**

Model: It computes column (g) net adjustments for box E detail-route transactions, limited to supported B and W adjustments.
Reviewed in: pass 6d1419919e1c

### 9(h) — Line 9, column (h) totals
Status: **MATCH**

Model: It computes column (h) as proceeds less basis plus adjustments, matching Schedule D line 9 column (h).
Reviewed in: pass 6d1419919e1c

### 10(d) — Line 10, column (d) totals
Status: **MATCH**

Model: It computes column (d) proceeds for box F detail-route transactions; box L digital cases are excluded by refusal.
Reviewed in: pass 6d1419919e1c

### 10(e) — Line 10, column (e) totals
Status: **MATCH**

Model: It computes column (e) basis for box F detail-route transactions, using the correct basis where no broker basis was reported.
Reviewed in: pass 6d1419919e1c

### 10(g) — Line 10, column (g) totals
Status: **MATCH**

Model: It computes column (g) net adjustments for box F detail-route transactions, limited to supported B and W adjustments.
Reviewed in: pass 6d1419919e1c

### 10(h) — Line 10, column (h) totals
Status: **MATCH**

Model: It computes column (h) as proceeds less basis plus adjustments, matching Schedule D line 10 column (h).
Reviewed in: pass 6d1419919e1c

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

Model: Line 13 correctly uses the capital gain distributions amount, with distribution scope checks refusing unsupported special cases.

### 7 — Combine the amounts for Schedule D line 7
Status: **MATCH**

Model: Schedule D line 7 combines lines 1a through 6 in column (h); the restated sum of the listed h-column amounts plus lines 4 through 6 is exactly that combination.
Reviewed in: pass 6d1419919e1c

### 15 — Combine the amounts for Schedule D line 15
Status: **MATCH**

Model: Schedule D line 15 combines lines 8a through 14 in column (h); the restated sum of the listed h-column amounts plus lines 11 through 14 is exactly that combination.
Reviewed in: pass 6d1419919e1c

### 16 — Combine the amounts for Schedule D line 16
Status: **MATCH**

Model: Line 16 correctly combines lines 7 and 15.

### 17 — Are lines 15 and 16 both gains?
Status: **MATCH**

Model: Line 17 correctly tests whether lines 15 and 16 are both positive gains.

### 20 — Are lines 18 and 19 zero and are you not filing Form 4952?
Status: **MISMATCH**

Restated: helper "Line 18. 28% Rate Gain Worksheet result, or zero when line 17 is No (lines 18 through 21 skipped)" = $0 and helper "Line 19. Unrecaptured Section 1250 Gain Worksheet result, or zero when line 17 is No (lines 18 through 21 skipped)" = $0 and helper "Are you filing Form 4952?" = false

Model: The form says if line 17 is No, skip lines 18 through 21 and go to line 22; the restatement evaluates line 20 from zeroed lines 18 and 19 without requiring line 17 to be Yes.

Ruling: representation; f1040sd p. 2, line 17: "No. Skip lines 18 through 21, and go to line 22". Line 20 (and line 22) are Boolean flow predicates, evaluated on every path by the documented convention (forms/2025/sd.yaml form note); the path the filer follows, and which lines show, is decided by line 17 and line 16 upstream, so the answer on a skipped path is never read. Same reading as the earlier rounds.

### 21 — Deductible loss, signed; zero when line 21 is skipped
Status: **MATCH**

Model: Line 21 correctly applies the smaller positive loss limit by taking the larger of the signed line 16 loss and the signed annual limit, entering the result as a loss.

### 22 — Do you have qualified dividends?
Status: **MATCH**

Model: Line 22 correctly tests whether Form 1040 line 3a qualified dividends are greater than zero.

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| 1a(d) | 7787227469e288c247094e959cafce0d3fff7fdd332d66f48977e9068de3e5be |
| 1a(e) | 8faab2424a1b1392335be37909007f0e27827669618430d5e5eb02afdd94f7e1 |
| 1a(g) | 769fe9d1946bdcd24329d0a0188151c5372a36df05cfbc70883d0ce1de1fd6ce |
| 1a(h) | 41556c86d657404043c5ae5ed7ed7f8b5e122abf0d7700707d758cbdc8771fa0 |
| 1b(d) | 2cfa922ec992e0ae4c464b6eef7f9f25436ac245912bfa640f26c8c58dd7e52e |
| 1b(e) | 243d6925486c927ecf18e9e836170507557257c738a71c42afbc52bda330482b |
| 1b(g) | 6cdf4a3559a75677d0f9b7ee0bb4296f57dd45a9fb58122145a4e40da5eda74b |
| 1b(h) | 9e0aaa4ed88b122fc576dc2b9fc3b9e4cef5d0dc5aa53d19697d6edd6e4221f1 |
| 2(d) | 626e544b7464834905860e8d57056ee5020cb48f294e85222c89413469f545f4 |
| 2(e) | bc6e0ad48470dc0be6de3f3a447373ef47bc234c1a6bf7c4057864403bd64965 |
| 2(g) | 52667e180f69acb7753c1b5f63a4bc2672cf61c110b9ffe55982e46510e6a33d |
| 2(h) | ddc12db35faff98f4fb60f5f4b764a480e7d507f815f83a5b00fc91cf55c31b1 |
| 3(d) | 3d1bbc7c4ebb6a2fd2e5be5d08afa48fa43c5948041e05f030f48051b4f075df |
| 3(e) | c2920f27f02841a69e650c1bed9e47170ecfd091458769d00be3c99b2f248eac |
| 3(g) | b46a34dc34dca504af9fdde8b077f61cc7f5ba8c476d335beb9c21518ae621bc |
| 3(h) | 006903b9cba5022102079f043f0d3017274efa748b58f0626a6d49dcf7c248e0 |
| 8a(d) | b56885b752d8d3f1bd4bdbb2fda1f35f651f60b839b412509f51f01554dc4a33 |
| 8a(e) | 5440c9182646021cd3dd16ea4faaafd64d537c5fb5dde4db9c3777b57cb3c3c0 |
| 8a(g) | 143e1502d5cc60d232c0526648719fdda8b1c80d5fbf61a263911d1f0c86c464 |
| 8a(h) | b073584952008681962c2740a7719d593617cf6ed491e565ac2aad8ade2501c8 |
| 8b(d) | d91dcc75318a5168141d9441098af8ae99ec85db38002ff62982160e2f702d4f |
| 8b(e) | 123d9ae79cd6973561b0ce9e6547f2445c061150c6aca68f0cd9d15a6cca70ad |
| 8b(g) | 82d8b97248bd2509102f1f870c351a8b396b4a5e33ce7fc1bdd963d4c8974e88 |
| 8b(h) | 66f6d70d1dc65a514085840e6408670d69786b5be0abf299d635d98d9bd04bc2 |
| 9(d) | e0a70db237f66b4a6693df0de3bf4bb4d1b2259dced1587a0cdf03c46e31704c |
| 9(e) | d8ae089aee5ba800de7a0d204fe1d94ed5f5b783135ef1bfd7aa084c5229e04f |
| 9(g) | 6585c51b09bfc2e9a3a65778fd8f40dc03f6d771b10df9b29f23546628f119b7 |
| 9(h) | ed1de01294f1217a33c05a9c32e79a9cce52e6ad619c6e8daee3ba11bae4044d |
| 10(d) | cbe503c4e426c9b6b95f112f8c90cdfc53eabfbc898dbfe750b92d3c5dfc557c |
| 10(e) | 52c425deac01adcdc65636d5f6bbe2d1d1254c08d50d0738ad6df22927fb38cc |
| 10(g) | a983a2faec9eaf0ca2557fef297b42bb0125cc7aac859dd12f7ad2ce6797044c |
| 10(h) | 75c7473069b87652e8298a37d746c9a2ab718e8cd96707c37daa57fa282152c0 |
| 4 | fc140fb363c2880a6ad4044547d651a95f3e0b2331f4c8f24148a188cd5eb60a |
| 5 | f717c41fbbeaebe05ba5f6d4487fc21983ef8650db4ae4a71665c900956fbedb |
| 6 | 71e9facbb1accd7b9339b79993aaab8d2829f113250db0b7ee1bdcf2ffae80aa |
| 11 | f771edaa32d289030a74d7189648bab320f53c24543262825a52bff3fc797449 |
| 12 | 6b73101b3aad0baea3bd1a2ca3d6212077528516b286cb108a32f972c036671e |
| 14 | 647156c672e55b5f86525437cb48b58f7e69078c9e39ca7e1ba8b729b780c3a6 |
| 13 | 092e3a4875fe86adf11131745dbc0c146a982515002b44daf6406ee928db9b84 |
| 7 | e9638d20efdb8776b5d2589678533b9f4b9b11e7097162ebe3721a73d27c9ea1 |
| 15 | 2b0bca8e8361e2a7eb89f72c426ae7f44a8b0c174636344896ab415bf79212b3 |
| 16 | 0f76ecb634638a67f68c0728370c592d43b31b38b3ccde6dc6c2d7c174edb44e |
| 17 | 31117d838592d91e2901cdbbbc25ab6ddde06e1f462f23a3d043c8974973312d |
| 20 | e69c889c4021467127fd0589b3546974c7726f302201f4389749b724db35e7ca |
| 21 | 01ed960f703ca2f324cbc7f80d1669824b80307f2b0302c0e053541c678be277 |
| 22 | e11951cb4d3a686d6f7a0ef1a1ce5a3c2cefd39849da3fe395d105c371f5b1d5 |
| (rest of the document) | 9b5ec474c37e31a1a667821669b753fb7357857a86f4d07c43af9f9de2bff699 |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass 6d1419919e1c

| field | value |
| --- | --- |
| date | 2026-11-04 |
| review scope | lines 1a(d), 1a(e), 1a(g), 1a(h), 1b(d), 1b(e), 1b(g), 1b(h), 2(d), 2(e), 2(g), 2(h), 3(d), 3(e), 3(g), 3(h), 8a(d), 8a(e), 8a(g), 8a(h), 8b(d), 8b(e), 8b(g), 8b(h), 9(d), 9(e), 9(g), 9(h), 10(d), 10(e), 10(g), 10(h), 7, 15 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 6d1419919e1c1551e61173dd905ca370ae49fec742047997cebd9e9432dcb4b1 |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | e5dd0475ee5085b32f35c6967decaece96ca3b5e204e7d63f30518152395f2e5 |
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
    reason: "It computes column (d) proceeds for short-term basis-reported, no-adjustment transactions in the supported box A aggregate case; digital G–L cases are excluded by refusal."
  - key: "1a(e)"
    status: MATCH
    reason: "It computes column (e) basis for the same box A aggregate-route transactions, where reported basis is the required basis because no adjustments are allowed."
  - key: "1a(g)"
    status: MATCH
    reason: "Line 1a permits no adjustments; within the aggregate-route eligibility gate sales.g is zero, so summing it matches the line's adjustment column."
  - key: "1a(h)"
    status: MATCH
    reason: "It computes column (h) as proceeds less column (e) plus column (g), matching Schedule D line 1a column (h)."
  - key: "1b(d)"
    status: MATCH
    reason: "It computes column (d) proceeds for box A detail-route transactions reported on Form 8949; box G digital cases are excluded by refusal."
  - key: "1b(e)"
    status: MATCH
    reason: "It computes column (e) basis for box A detail-route transactions, using reported basis where required and allowing the adjustment column to correct it."
  - key: "1b(g)"
    status: MATCH
    reason: "It computes column (g) net adjustments for box A detail-route transactions, limited to supported B and W adjustments."
  - key: "1b(h)"
    status: MATCH
    reason: "It computes column (h) as proceeds less basis plus adjustments, matching Form 8949 and Schedule D line 1b column (h)."
  - key: "2(d)"
    status: MATCH
    reason: "It computes column (d) proceeds for box B detail-route transactions; box H digital cases are excluded by refusal."
  - key: "2(e)"
    status: MATCH
    reason: "It computes column (e) basis for box B detail-route transactions, where basis was not reported and the correct basis is required."
  - key: "2(g)"
    status: MATCH
    reason: "It computes column (g) net adjustments for box B detail-route transactions, limited to supported B and W adjustments."
  - key: "2(h)"
    status: MATCH
    reason: "It computes column (h) as proceeds less basis plus adjustments, matching Schedule D line 2 column (h)."
  - key: "3(d)"
    status: MATCH
    reason: "It computes column (d) proceeds for box C detail-route transactions; box I digital cases are excluded by refusal."
  - key: "3(e)"
    status: MATCH
    reason: "It computes column (e) basis for box C detail-route transactions, using the correct basis where no broker basis was reported."
  - key: "3(g)"
    status: MATCH
    reason: "It computes column (g) net adjustments for box C detail-route transactions, limited to supported B and W adjustments."
  - key: "3(h)"
    status: MATCH
    reason: "It computes column (h) as proceeds less basis plus adjustments, matching Schedule D line 3 column (h)."
  - key: "8a(d)"
    status: MATCH
    reason: "It computes column (d) proceeds for long-term basis-reported, no-adjustment transactions in the supported box D aggregate case; digital J–L cases are excluded by refusal."
  - key: "8a(e)"
    status: MATCH
    reason: "It computes column (e) basis for the same box D aggregate-route transactions, where reported basis is the required basis because no adjustments are allowed."
  - key: "8a(g)"
    status: MATCH
    reason: "Line 8a permits no adjustments; within the aggregate-route eligibility gate sales.g is zero, so summing it matches the line's adjustment column."
  - key: "8a(h)"
    status: MATCH
    reason: "It computes column (h) as proceeds less column (e) plus column (g), matching Schedule D line 8a column (h)."
  - key: "8b(d)"
    status: MATCH
    reason: "It computes column (d) proceeds for box D detail-route transactions reported on Form 8949; box J digital cases are excluded by refusal."
  - key: "8b(e)"
    status: MATCH
    reason: "It computes column (e) basis for box D detail-route transactions, using reported basis where required and allowing the adjustment column to correct it."
  - key: "8b(g)"
    status: MATCH
    reason: "It computes column (g) net adjustments for box D detail-route transactions, limited to supported B and W adjustments."
  - key: "8b(h)"
    status: MATCH
    reason: "It computes column (h) as proceeds less basis plus adjustments, matching Form 8949 and Schedule D line 8b column (h)."
  - key: "9(d)"
    status: MATCH
    reason: "It computes column (d) proceeds for box E detail-route transactions; box K digital cases are excluded by refusal."
  - key: "9(e)"
    status: MATCH
    reason: "It computes column (e) basis for box E detail-route transactions, where basis was not reported and the correct basis is required."
  - key: "9(g)"
    status: MATCH
    reason: "It computes column (g) net adjustments for box E detail-route transactions, limited to supported B and W adjustments."
  - key: "9(h)"
    status: MATCH
    reason: "It computes column (h) as proceeds less basis plus adjustments, matching Schedule D line 9 column (h)."
  - key: "10(d)"
    status: MATCH
    reason: "It computes column (d) proceeds for box F detail-route transactions; box L digital cases are excluded by refusal."
  - key: "10(e)"
    status: MATCH
    reason: "It computes column (e) basis for box F detail-route transactions, using the correct basis where no broker basis was reported."
  - key: "10(g)"
    status: MATCH
    reason: "It computes column (g) net adjustments for box F detail-route transactions, limited to supported B and W adjustments."
  - key: "10(h)"
    status: MATCH
    reason: "It computes column (h) as proceeds less basis plus adjustments, matching Schedule D line 10 column (h)."
  - key: "7"
    status: MATCH
    reason: "Schedule D line 7 combines lines 1a through 6 in column (h); the restated sum of the listed h-column amounts plus lines 4 through 6 is exactly that combination."
  - key: "15"
    status: MATCH
    reason: "Schedule D line 15 combines lines 8a through 14 in column (h); the restated sum of the listed h-column amounts plus lines 11 through 14 is exactly that combination."
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
