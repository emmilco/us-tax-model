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

Model: Matches Schedule D line 1a column (d): proceeds for aggregate short-term basis-reported transactions with no adjustments; digital-asset counterparts are excluded by the program's refusal.
Reviewed in: pass 5bc4e84ee576

### 1a(e) — Line 1a, column (e) totals
Status: **MATCH**

Model: Matches Schedule D line 1a column (e): basis for aggregate short-term basis-reported transactions with no adjustments; digital-asset counterparts are excluded by the program's refusal.
Reviewed in: pass 5bc4e84ee576

### 1a(g) — Line 1a, column (g) totals
Status: **MATCH**

Model: Matches Schedule D line 1a column (g): adjustments for aggregate short-term transactions; the aggregate route enforces that no adjustments apply, so this is zero.
Reviewed in: pass 5bc4e84ee576

### 1a(h) — Line 1a, column (h) totals
Status: **MATCH**

Model: Matches Schedule D line 1a column (h): gain or loss for aggregate short-term basis-reported transactions with no adjustments; digital-asset counterparts are excluded by the program's refusal.
Reviewed in: pass 5bc4e84ee576

### 1b(d) — Line 1b, column (d) totals
Status: **MATCH**

Model: Matches Schedule D line 1b column (d) for short-term Form 8949 Box A detail transactions; the digital Box G counterpart is excluded by the program's refusal.
Reviewed in: pass 5bc4e84ee576

### 1b(e) — Line 1b, column (e) totals
Status: **MATCH**

Model: Matches Schedule D line 1b column (e) for short-term Form 8949 Box A detail transactions; the digital Box G counterpart is excluded by the program's refusal.
Reviewed in: pass 5bc4e84ee576

### 1b(g) — Line 1b, column (g) totals
Status: **MATCH**

Model: Matches Schedule D line 1b column (g) for short-term Form 8949 Box A detail transactions; the digital Box G counterpart is excluded by the program's refusal.
Reviewed in: pass 5bc4e84ee576

### 1b(h) — Line 1b, column (h) totals
Status: **MATCH**

Model: Matches Schedule D line 1b column (h) for short-term Form 8949 Box A detail transactions; the digital Box G counterpart is excluded by the program's refusal.
Reviewed in: pass 5bc4e84ee576

### 2(d) — Line 2, column (d) totals
Status: **MATCH**

Model: Matches Schedule D line 2 column (d) for short-term Form 8949 Box B detail transactions; the digital Box H counterpart is excluded by the program's refusal.
Reviewed in: pass 5bc4e84ee576

### 2(e) — Line 2, column (e) totals
Status: **MATCH**

Model: Matches Schedule D line 2 column (e) for short-term Form 8949 Box B detail transactions; the digital Box H counterpart is excluded by the program's refusal.
Reviewed in: pass 5bc4e84ee576

### 2(g) — Line 2, column (g) totals
Status: **MATCH**

Model: Matches Schedule D line 2 column (g) for short-term Form 8949 Box B detail transactions; the digital Box H counterpart is excluded by the program's refusal.
Reviewed in: pass 5bc4e84ee576

### 2(h) — Line 2, column (h) totals
Status: **MATCH**

Model: Matches Schedule D line 2 column (h) for short-term Form 8949 Box B detail transactions; the digital Box H counterpart is excluded by the program's refusal.
Reviewed in: pass 5bc4e84ee576

### 3(d) — Line 3, column (d) totals
Status: **MATCH**

Model: Matches Schedule D line 3 column (d) for short-term Form 8949 Box C detail transactions; the digital Box I counterpart is excluded by the program's refusal.
Reviewed in: pass 5bc4e84ee576

### 3(e) — Line 3, column (e) totals
Status: **MATCH**

Model: Matches Schedule D line 3 column (e) for short-term Form 8949 Box C detail transactions; the digital Box I counterpart is excluded by the program's refusal.
Reviewed in: pass 5bc4e84ee576

### 3(g) — Line 3, column (g) totals
Status: **MATCH**

Model: Matches Schedule D line 3 column (g) for short-term Form 8949 Box C detail transactions; the digital Box I counterpart is excluded by the program's refusal.
Reviewed in: pass 5bc4e84ee576

### 3(h) — Line 3, column (h) totals
Status: **MATCH**

Model: Matches Schedule D line 3 column (h) for short-term Form 8949 Box C detail transactions; the digital Box I counterpart is excluded by the program's refusal.
Reviewed in: pass 5bc4e84ee576

### 8a(d) — Line 8a, column (d) totals
Status: **MATCH**

Model: Matches Schedule D line 8a column (d): proceeds for aggregate long-term basis-reported transactions with no adjustments; digital-asset counterparts are excluded by the program's refusal.
Reviewed in: pass 5bc4e84ee576

### 8a(e) — Line 8a, column (e) totals
Status: **MATCH**

Model: Matches Schedule D line 8a column (e): basis for aggregate long-term basis-reported transactions with no adjustments; digital-asset counterparts are excluded by the program's refusal.
Reviewed in: pass 5bc4e84ee576

### 8a(g) — Line 8a, column (g) totals
Status: **MATCH**

Model: Matches Schedule D line 8a column (g): adjustments for aggregate long-term transactions; the aggregate route enforces that no adjustments apply, so this is zero.
Reviewed in: pass 5bc4e84ee576

### 8a(h) — Line 8a, column (h) totals
Status: **MATCH**

Model: Matches Schedule D line 8a column (h): gain or loss for aggregate long-term basis-reported transactions with no adjustments; digital-asset counterparts are excluded by the program's refusal.
Reviewed in: pass 5bc4e84ee576

### 8b(d) — Line 8b, column (d) totals
Status: **MATCH**

Model: Matches Schedule D line 8b column (d) for long-term Form 8949 Box D detail transactions; the digital Box J counterpart is excluded by the program's refusal.
Reviewed in: pass 5bc4e84ee576

### 8b(e) — Line 8b, column (e) totals
Status: **MATCH**

Model: Matches Schedule D line 8b column (e) for long-term Form 8949 Box D detail transactions; the digital Box J counterpart is excluded by the program's refusal.
Reviewed in: pass 5bc4e84ee576

### 8b(g) — Line 8b, column (g) totals
Status: **MATCH**

Model: Matches Schedule D line 8b column (g) for long-term Form 8949 Box D detail transactions; the digital Box J counterpart is excluded by the program's refusal.
Reviewed in: pass 5bc4e84ee576

### 8b(h) — Line 8b, column (h) totals
Status: **MATCH**

Model: Matches Schedule D line 8b column (h) for long-term Form 8949 Box D detail transactions; the digital Box J counterpart is excluded by the program's refusal.
Reviewed in: pass 5bc4e84ee576

### 9(d) — Line 9, column (d) totals
Status: **MATCH**

Model: Matches Schedule D line 9 column (d) for long-term Form 8949 Box E detail transactions; the digital Box K counterpart is excluded by the program's refusal.
Reviewed in: pass 5bc4e84ee576

### 9(e) — Line 9, column (e) totals
Status: **MATCH**

Model: Matches Schedule D line 9 column (e) for long-term Form 8949 Box E detail transactions; the digital Box K counterpart is excluded by the program's refusal.
Reviewed in: pass 5bc4e84ee576

### 9(g) — Line 9, column (g) totals
Status: **MATCH**

Model: Matches Schedule D line 9 column (g) for long-term Form 8949 Box E detail transactions; the digital Box K counterpart is excluded by the program's refusal.
Reviewed in: pass 5bc4e84ee576

### 9(h) — Line 9, column (h) totals
Status: **MATCH**

Model: Matches Schedule D line 9 column (h) for long-term Form 8949 Box E detail transactions; the digital Box K counterpart is excluded by the program's refusal.
Reviewed in: pass 5bc4e84ee576

### 10(d) — Line 10, column (d) totals
Status: **MATCH**

Model: Matches Schedule D line 10 column (d) for long-term Form 8949 Box F detail transactions; the digital Box L counterpart is excluded by the program's refusal.
Reviewed in: pass 5bc4e84ee576

### 10(e) — Line 10, column (e) totals
Status: **MATCH**

Model: Matches Schedule D line 10 column (e) for long-term Form 8949 Box F detail transactions; the digital Box L counterpart is excluded by the program's refusal.
Reviewed in: pass 5bc4e84ee576

### 10(g) — Line 10, column (g) totals
Status: **MATCH**

Model: Matches Schedule D line 10 column (g) for long-term Form 8949 Box F detail transactions; the digital Box L counterpart is excluded by the program's refusal.
Reviewed in: pass 5bc4e84ee576

### 10(h) — Line 10, column (h) totals
Status: **MATCH**

Model: Matches Schedule D line 10 column (h) for long-term Form 8949 Box F detail transactions; the digital Box L counterpart is excluded by the program's refusal.
Reviewed in: pass 5bc4e84ee576

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

Model: Combines the column (h) amounts of lines 1a through 6, as Schedule D line 7 instructs.
Reviewed in: pass 5bc4e84ee576

### 15 — Combine the amounts for Schedule D line 15
Status: **MATCH**

Model: Combines the column (h) amounts of lines 8a through 14, as Schedule D line 15 instructs.
Reviewed in: pass 5bc4e84ee576

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
| 1a(d) | 3ae79332512cc1fafba221465db6165de85bf85d690b1ba35e3b8c3096abcfce |
| 1a(e) | 7872dfcbf2c27596d5f1dc8aef8df822280f68a3bd5189099114d0d3d21b0301 |
| 1a(g) | d5ec08d2b379aea0b2ae65fe5f6ab86767102f9d48bc3eb31002b0ac4e1a02d9 |
| 1a(h) | 33c9c8df2f0217f54c6bbe87d6e4b1dceee9053dbd327f01078b9cecc992de0f |
| 1b(d) | 719fc2310c123dab2728dd88cbdbcf1c3df17fbca9b4ea0f35280ebae61703cf |
| 1b(e) | fead2789fde6e6e60dd2e65145197eb14bba43201275ff35b66b75c744cfc12d |
| 1b(g) | 526607ba9addfef41757b6f14551a1f4155b6d01eea6d188adfaf662497cc6e3 |
| 1b(h) | 5a5b8769e6e228398ec8c107b0bcd47bdb858f6de6f647e9cb49fa868272160c |
| 2(d) | fc15b7137e85cfd057f00d716f3541d9f226388cd3fd2374ac955aeebf2a87be |
| 2(e) | 7a2d904b969752987599ed1cd2ae4d559bb5ba67bf90b8b38451ceaf47858855 |
| 2(g) | 0076e5d3add71f3b8259642837faa8b2d69c0885e0a1f510394717cdc5357e05 |
| 2(h) | c2baca91ab9d70daf9ea6ae2b2d1b003de029bcec9bb4288adfdd54c83d1896d |
| 3(d) | ecb863852934d726651ff464e41961562b5154d850edf398d5cfa9ca4ffc6c07 |
| 3(e) | 7352f147a3de5ac4c453ea59253350863e5b2f1b05f6f239a408b1f059987635 |
| 3(g) | 87342b2716789f703f84b2e790f3d7d538d71e0b3b9577b919c02d4ee13ded79 |
| 3(h) | 2b8676d642d8774f9b1742bf24ffe52ad8bb712553adcd33e072fcbf050ca544 |
| 8a(d) | 32fd84f6f47a892ae98dfc17b2ff8b8a824793917817510dc7d7d41ed9515c22 |
| 8a(e) | 668878d8c5f134067ff8d7e4ec35aad8eb4061d667b4fcb570476c57e234e7a1 |
| 8a(g) | 3b034bde46a2451d2d18ed160ce5f3ea829c85348e7056ac6ae9e79063352c05 |
| 8a(h) | 1f69d27013db6fb9f36685f66414a763742cf6dbd5554b915ad93df3724582c6 |
| 8b(d) | 748be0fa06775171a9a411554a3b2b535e540f68a77756927b4ef5a987fa664a |
| 8b(e) | 654072e33f2783be577d2368db8dbb5d51ba46c8dbb1193cbbbe3691aee4be27 |
| 8b(g) | 0a5d200811b4822e86c27d47373cfabd1492187b46a8f5ae3014043000b6cb2e |
| 8b(h) | d108c6b711da7d9331fe5fa94b8d3b8b0f8646814aa95cecea32077d2479f1d1 |
| 9(d) | a54525c71b423f1f92010d354b519a80028d7be3e93a9f97dc4a9c44afb76b7c |
| 9(e) | dd0c806b55a6cfe810df9cd37aada188c5ee8be38eec3aed7c6a8447dcb094b7 |
| 9(g) | ec1d24b3f1dbb7a91f2c9436be2389fc075a234786fab862815b073e02e325a6 |
| 9(h) | 1d645b93ef1678583f4d90a4bdfb9b9d742c10ae5d27af94866a4e277604cb8f |
| 10(d) | f6f6cc6a0518e5783d10339a974a00cbc480ebde75d2f98d1d967b7ef6340770 |
| 10(e) | 700609783174ae2ecbcc45fe5bc700c135846965561c8c99955bfa4899b9fe4c |
| 10(g) | 79396b093d414a3fa15409271de3cc7a21ed79aa4027884012b5cafef91df85c |
| 10(h) | 3db07d35bbf2394ca9aad58929d33760061292212d3d858f3e80917e379328a0 |
| 4 | fc140fb363c2880a6ad4044547d651a95f3e0b2331f4c8f24148a188cd5eb60a |
| 5 | f717c41fbbeaebe05ba5f6d4487fc21983ef8650db4ae4a71665c900956fbedb |
| 6 | 71e9facbb1accd7b9339b79993aaab8d2829f113250db0b7ee1bdcf2ffae80aa |
| 11 | f771edaa32d289030a74d7189648bab320f53c24543262825a52bff3fc797449 |
| 12 | 6b73101b3aad0baea3bd1a2ca3d6212077528516b286cb108a32f972c036671e |
| 14 | 647156c672e55b5f86525437cb48b58f7e69078c9e39ca7e1ba8b729b780c3a6 |
| 13 | 092e3a4875fe86adf11131745dbc0c146a982515002b44daf6406ee928db9b84 |
| 7 | b3aba073245a5d5fa50e920fd3e3697bd0df0affeac5bf3a04fe59b3d88b4025 |
| 15 | 3ab8a9c986436834acca98a087a283ec688663f0b4f1625b4dcdb7e9020cfdc5 |
| 16 | 0f76ecb634638a67f68c0728370c592d43b31b38b3ccde6dc6c2d7c174edb44e |
| 17 | 31117d838592d91e2901cdbbbc25ab6ddde06e1f462f23a3d043c8974973312d |
| 20 | e69c889c4021467127fd0589b3546974c7726f302201f4389749b724db35e7ca |
| 21 | 01ed960f703ca2f324cbc7f80d1669824b80307f2b0302c0e053541c678be277 |
| 22 | e11951cb4d3a686d6f7a0ef1a1ce5a3c2cefd39849da3fe395d105c371f5b1d5 |
| (rest of the document) | 9b5ec474c37e31a1a667821669b753fb7357857a86f4d07c43af9f9de2bff699 |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass 5bc4e84ee576

| field | value |
| --- | --- |
| date | 2026-11-04 |
| review scope | lines 1a(d), 1a(e), 1a(g), 1a(h), 1b(d), 1b(e), 1b(g), 1b(h), 2(d), 2(e), 2(g), 2(h), 3(d), 3(e), 3(g), 3(h), 8a(d), 8a(e), 8a(g), 8a(h), 8b(d), 8b(e), 8b(g), 8b(h), 9(d), 9(e), 9(g), 9(h), 10(d), 10(e), 10(g), 10(h), 7, 15 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 5bc4e84ee576988837c468786f4a6c265ea12664a6b13ee8cf792027dbafd531 |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 03c8ca70ae0f2bf9cc4f18741de37d629aa19a808f1581b9f43e5aeab0842444 |
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
    reason: "Matches Schedule D line 1a column (d): proceeds for aggregate short-term basis-reported transactions with no adjustments; digital-asset counterparts are excluded by the program's refusal."
  - key: "1a(e)"
    status: MATCH
    reason: "Matches Schedule D line 1a column (e): basis for aggregate short-term basis-reported transactions with no adjustments; digital-asset counterparts are excluded by the program's refusal."
  - key: "1a(g)"
    status: MATCH
    reason: "Matches Schedule D line 1a column (g): adjustments for aggregate short-term transactions; the aggregate route enforces that no adjustments apply, so this is zero."
  - key: "1a(h)"
    status: MATCH
    reason: "Matches Schedule D line 1a column (h): gain or loss for aggregate short-term basis-reported transactions with no adjustments; digital-asset counterparts are excluded by the program's refusal."
  - key: "1b(d)"
    status: MATCH
    reason: "Matches Schedule D line 1b column (d) for short-term Form 8949 Box A detail transactions; the digital Box G counterpart is excluded by the program's refusal."
  - key: "1b(e)"
    status: MATCH
    reason: "Matches Schedule D line 1b column (e) for short-term Form 8949 Box A detail transactions; the digital Box G counterpart is excluded by the program's refusal."
  - key: "1b(g)"
    status: MATCH
    reason: "Matches Schedule D line 1b column (g) for short-term Form 8949 Box A detail transactions; the digital Box G counterpart is excluded by the program's refusal."
  - key: "1b(h)"
    status: MATCH
    reason: "Matches Schedule D line 1b column (h) for short-term Form 8949 Box A detail transactions; the digital Box G counterpart is excluded by the program's refusal."
  - key: "2(d)"
    status: MATCH
    reason: "Matches Schedule D line 2 column (d) for short-term Form 8949 Box B detail transactions; the digital Box H counterpart is excluded by the program's refusal."
  - key: "2(e)"
    status: MATCH
    reason: "Matches Schedule D line 2 column (e) for short-term Form 8949 Box B detail transactions; the digital Box H counterpart is excluded by the program's refusal."
  - key: "2(g)"
    status: MATCH
    reason: "Matches Schedule D line 2 column (g) for short-term Form 8949 Box B detail transactions; the digital Box H counterpart is excluded by the program's refusal."
  - key: "2(h)"
    status: MATCH
    reason: "Matches Schedule D line 2 column (h) for short-term Form 8949 Box B detail transactions; the digital Box H counterpart is excluded by the program's refusal."
  - key: "3(d)"
    status: MATCH
    reason: "Matches Schedule D line 3 column (d) for short-term Form 8949 Box C detail transactions; the digital Box I counterpart is excluded by the program's refusal."
  - key: "3(e)"
    status: MATCH
    reason: "Matches Schedule D line 3 column (e) for short-term Form 8949 Box C detail transactions; the digital Box I counterpart is excluded by the program's refusal."
  - key: "3(g)"
    status: MATCH
    reason: "Matches Schedule D line 3 column (g) for short-term Form 8949 Box C detail transactions; the digital Box I counterpart is excluded by the program's refusal."
  - key: "3(h)"
    status: MATCH
    reason: "Matches Schedule D line 3 column (h) for short-term Form 8949 Box C detail transactions; the digital Box I counterpart is excluded by the program's refusal."
  - key: "8a(d)"
    status: MATCH
    reason: "Matches Schedule D line 8a column (d): proceeds for aggregate long-term basis-reported transactions with no adjustments; digital-asset counterparts are excluded by the program's refusal."
  - key: "8a(e)"
    status: MATCH
    reason: "Matches Schedule D line 8a column (e): basis for aggregate long-term basis-reported transactions with no adjustments; digital-asset counterparts are excluded by the program's refusal."
  - key: "8a(g)"
    status: MATCH
    reason: "Matches Schedule D line 8a column (g): adjustments for aggregate long-term transactions; the aggregate route enforces that no adjustments apply, so this is zero."
  - key: "8a(h)"
    status: MATCH
    reason: "Matches Schedule D line 8a column (h): gain or loss for aggregate long-term basis-reported transactions with no adjustments; digital-asset counterparts are excluded by the program's refusal."
  - key: "8b(d)"
    status: MATCH
    reason: "Matches Schedule D line 8b column (d) for long-term Form 8949 Box D detail transactions; the digital Box J counterpart is excluded by the program's refusal."
  - key: "8b(e)"
    status: MATCH
    reason: "Matches Schedule D line 8b column (e) for long-term Form 8949 Box D detail transactions; the digital Box J counterpart is excluded by the program's refusal."
  - key: "8b(g)"
    status: MATCH
    reason: "Matches Schedule D line 8b column (g) for long-term Form 8949 Box D detail transactions; the digital Box J counterpart is excluded by the program's refusal."
  - key: "8b(h)"
    status: MATCH
    reason: "Matches Schedule D line 8b column (h) for long-term Form 8949 Box D detail transactions; the digital Box J counterpart is excluded by the program's refusal."
  - key: "9(d)"
    status: MATCH
    reason: "Matches Schedule D line 9 column (d) for long-term Form 8949 Box E detail transactions; the digital Box K counterpart is excluded by the program's refusal."
  - key: "9(e)"
    status: MATCH
    reason: "Matches Schedule D line 9 column (e) for long-term Form 8949 Box E detail transactions; the digital Box K counterpart is excluded by the program's refusal."
  - key: "9(g)"
    status: MATCH
    reason: "Matches Schedule D line 9 column (g) for long-term Form 8949 Box E detail transactions; the digital Box K counterpart is excluded by the program's refusal."
  - key: "9(h)"
    status: MATCH
    reason: "Matches Schedule D line 9 column (h) for long-term Form 8949 Box E detail transactions; the digital Box K counterpart is excluded by the program's refusal."
  - key: "10(d)"
    status: MATCH
    reason: "Matches Schedule D line 10 column (d) for long-term Form 8949 Box F detail transactions; the digital Box L counterpart is excluded by the program's refusal."
  - key: "10(e)"
    status: MATCH
    reason: "Matches Schedule D line 10 column (e) for long-term Form 8949 Box F detail transactions; the digital Box L counterpart is excluded by the program's refusal."
  - key: "10(g)"
    status: MATCH
    reason: "Matches Schedule D line 10 column (g) for long-term Form 8949 Box F detail transactions; the digital Box L counterpart is excluded by the program's refusal."
  - key: "10(h)"
    status: MATCH
    reason: "Matches Schedule D line 10 column (h) for long-term Form 8949 Box F detail transactions; the digital Box L counterpart is excluded by the program's refusal."
  - key: "7"
    status: MATCH
    reason: "Combines the column (h) amounts of lines 1a through 6, as Schedule D line 7 instructs."
  - key: "15"
    status: MATCH
    reason: "Combines the column (h) amounts of lines 8a through 14, as Schedule D line 15 instructs."
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
