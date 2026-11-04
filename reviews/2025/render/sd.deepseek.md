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

Model: It restates the column (d) proceeds total for the short-term basis-reported no-adjustment aggregate route, which is what Schedule D line 1a totals.
Reviewed in: pass d8a8e06296ea

### 1a(e) — Line 1a, column (e) totals
Status: **MATCH**

Model: It restates the column (e) cost or other basis total for the short-term basis-reported no-adjustment aggregate route, matching line 1a.
Reviewed in: pass d8a8e06296ea

### 1a(g) — Line 1a, column (g) totals
Status: **MATCH**

Model: For the qualifying aggregate population there are no adjustments, so summing the column (g) adjustment field yields the line 1a column (g) amount.
Reviewed in: pass d8a8e06296ea

### 1a(h) — Line 1a, column (h) totals
Status: **MATCH**

Model: It restates column (h) as proceeds less basis plus adjustments for the short-term aggregate population, matching line 1a column (h).
Reviewed in: pass d8a8e06296ea

### 1b(d) — Line 1b, column (d) totals
Status: **MATCH**

Model: It restates the column (d) proceeds total for short-term basis-reported transactions reported on Form 8949 in detail, matching line 1b.
Reviewed in: pass d8a8e06296ea

### 1b(e) — Line 1b, column (e) totals
Status: **MATCH**

Model: It restates the column (e) cost or other basis total for short-term basis-reported Form 8949 detail transactions, matching line 1b.
Reviewed in: pass d8a8e06296ea

### 1b(g) — Line 1b, column (g) totals
Status: **MATCH**

Model: It restates the column (g) adjustment total for short-term Form 8949 detail transactions, matching line 1b column (g).
Reviewed in: pass d8a8e06296ea

### 1b(h) — Line 1b, column (h) totals
Status: **MATCH**

Model: It restates column (h) as proceeds less basis plus adjustments for short-term Form 8949 detail transactions, matching line 1b.
Reviewed in: pass d8a8e06296ea

### 2(d) — Line 2, column (d) totals
Status: **MATCH**

Model: It restates the column (d) proceeds total for short-term basis-not-reported Form 8949 detail transactions, matching line 2.
Reviewed in: pass d8a8e06296ea

### 2(e) — Line 2, column (e) totals
Status: **MATCH**

Model: It restates the column (e) correct basis total for short-term basis-not-reported Form 8949 detail transactions, matching line 2.
Reviewed in: pass d8a8e06296ea

### 2(g) — Line 2, column (g) totals
Status: **MATCH**

Model: It restates the column (g) adjustment total for short-term basis-not-reported Form 8949 detail transactions, matching line 2.
Reviewed in: pass d8a8e06296ea

### 2(h) — Line 2, column (h) totals
Status: **MATCH**

Model: It restates column (h) as proceeds less basis plus adjustments for short-term basis-not-reported Form 8949 detail transactions, matching line 2.
Reviewed in: pass d8a8e06296ea

### 3(d) — Line 3, column (d) totals
Status: **MATCH**

Model: It restates the column (d) proceeds total for short-term non-1099-B/1099-DA Form 8949 detail transactions, matching line 3.
Reviewed in: pass d8a8e06296ea

### 3(e) — Line 3, column (e) totals
Status: **MATCH**

Model: It restates the column (e) correct basis total for short-term non-1099-B/1099-DA Form 8949 detail transactions, matching line 3.
Reviewed in: pass d8a8e06296ea

### 3(g) — Line 3, column (g) totals
Status: **MATCH**

Model: It restates the column (g) adjustment total for short-term non-1099-B/1099-DA Form 8949 detail transactions, matching line 3.
Reviewed in: pass d8a8e06296ea

### 3(h) — Line 3, column (h) totals
Status: **MATCH**

Model: It restates column (h) as proceeds less basis plus adjustments for short-term non-1099-B/1099-DA Form 8949 detail transactions, matching line 3.
Reviewed in: pass d8a8e06296ea

### 8a(d) — Line 8a, column (d) totals
Status: **MATCH**

Model: It restates the column (d) proceeds total for the long-term basis-reported no-adjustment aggregate route, matching line 8a.
Reviewed in: pass d8a8e06296ea

### 8a(e) — Line 8a, column (e) totals
Status: **MATCH**

Model: It restates the column (e) cost or other basis total for the long-term basis-reported no-adjustment aggregate route, matching line 8a.
Reviewed in: pass d8a8e06296ea

### 8a(g) — Line 8a, column (g) totals
Status: **MATCH**

Model: For the qualifying aggregate population there are no adjustments, so summing the column (g) adjustment field yields the line 8a column (g) amount.
Reviewed in: pass d8a8e06296ea

### 8a(h) — Line 8a, column (h) totals
Status: **MATCH**

Model: It restates column (h) as proceeds less basis plus adjustments for the long-term aggregate population, matching line 8a column (h).
Reviewed in: pass d8a8e06296ea

### 8b(d) — Line 8b, column (d) totals
Status: **MATCH**

Model: It restates the column (d) proceeds total for long-term basis-reported Form 8949 detail transactions, matching line 8b.
Reviewed in: pass d8a8e06296ea

### 8b(e) — Line 8b, column (e) totals
Status: **MATCH**

Model: It restates the column (e) cost or other basis total for long-term basis-reported Form 8949 detail transactions, matching line 8b.
Reviewed in: pass d8a8e06296ea

### 8b(g) — Line 8b, column (g) totals
Status: **MATCH**

Model: It restates the column (g) adjustment total for long-term Form 8949 detail transactions, matching line 8b column (g).
Reviewed in: pass d8a8e06296ea

### 8b(h) — Line 8b, column (h) totals
Status: **MATCH**

Model: It restates column (h) as proceeds less basis plus adjustments for long-term Form 8949 detail transactions, matching line 8b.
Reviewed in: pass d8a8e06296ea

### 9(d) — Line 9, column (d) totals
Status: **MATCH**

Model: It restates the column (d) proceeds total for long-term basis-not-reported Form 8949 detail transactions, matching line 9.
Reviewed in: pass d8a8e06296ea

### 9(e) — Line 9, column (e) totals
Status: **MATCH**

Model: It restates the column (e) correct basis total for long-term basis-not-reported Form 8949 detail transactions, matching line 9.
Reviewed in: pass d8a8e06296ea

### 9(g) — Line 9, column (g) totals
Status: **MATCH**

Model: It restates the column (g) adjustment total for long-term basis-not-reported Form 8949 detail transactions, matching line 9.
Reviewed in: pass d8a8e06296ea

### 9(h) — Line 9, column (h) totals
Status: **MATCH**

Model: It restates column (h) as proceeds less basis plus adjustments for long-term basis-not-reported Form 8949 detail transactions, matching line 9.
Reviewed in: pass d8a8e06296ea

### 10(d) — Line 10, column (d) totals
Status: **MATCH**

Model: It restates the column (d) proceeds total for long-term non-1099-B/1099-DA Form 8949 detail transactions, matching line 10.
Reviewed in: pass d8a8e06296ea

### 10(e) — Line 10, column (e) totals
Status: **MATCH**

Model: It restates the column (e) correct basis total for long-term non-1099-B/1099-DA Form 8949 detail transactions, matching line 10.
Reviewed in: pass d8a8e06296ea

### 10(g) — Line 10, column (g) totals
Status: **MATCH**

Model: It restates the column (g) adjustment total for long-term non-1099-B/1099-DA Form 8949 detail transactions, matching line 10.
Reviewed in: pass d8a8e06296ea

### 10(h) — Line 10, column (h) totals
Status: **MATCH**

Model: It restates column (h) as proceeds less basis plus adjustments for long-term non-1099-B/1099-DA Form 8949 detail transactions, matching line 10.
Reviewed in: pass d8a8e06296ea

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

Model: It combines the column (h) amounts for lines 1a through 3 and lines 4 through 6, which is what Schedule D line 7 says to combine.
Reviewed in: pass d8a8e06296ea

### 15 — Combine the amounts for Schedule D line 15
Status: **MATCH**

Model: It combines the column (h) amounts for lines 8a through 10 and lines 11 through 14, which is what Schedule D line 15 says to combine.
Reviewed in: pass d8a8e06296ea

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
| 1a(d) | ebdfd89ce557a8cc278f4f22a732c9da0df0bb31778862bff27b47d82947ab5e |
| 1a(e) | 9a893588b47cba33ef6bd39e020d8bc28032f1005659b6aaf4f681a5e6f6fb79 |
| 1a(g) | 66ba85abac2350c2ce6ea354aef7ad9c5783a8212497142ba0522da23b02231d |
| 1a(h) | be489351e598244a19d8e82ad56f2fb0bd2deb7bc929a4ea97ea0cdeb47766a1 |
| 1b(d) | 535a6741b5fdac7044a51b72a7086184ce37acbf2ceded09d11b85eea4a58ff1 |
| 1b(e) | 7f9ea40fe34d4ca39821cbfc7974b907096a4f5061dce9d68d2b83e4dcaf0461 |
| 1b(g) | 0a95d2830528d70b7d2ebca1deeb93132333f71f13e1c0b8a372e956be1314da |
| 1b(h) | 9d25dca367f6d5c9d256fe076f46fc4dd3380d7d9c0d3e0808a40ca7f8966005 |
| 2(d) | e84d29039d4aaa12fc8377a5260e33a32649036f9f736522fd3697056369a326 |
| 2(e) | d837835b77eae4813ee7f60ee0815d8f4d6032b9dbf30bb68c9e82c1ca0950af |
| 2(g) | 2d327b9b14cb7e9037fc3897d3ddf4fb1de4d0154f387404e0e077d268df33d5 |
| 2(h) | d4571a24ca808342d464578928bb32fbec3ad3b944938901fea0e79b776ffbe8 |
| 3(d) | 5c1ef7e27aaf83cff03f81b0b4f36767479a900a3d9a204f8384551fe708faee |
| 3(e) | e95d44123775f42e98d5f4991986a55b1a9880253b7f3ddc81818883d30bcc5e |
| 3(g) | 7def3b0eaf7e65fc6157f58c560f3d2785f58aea6046c3382638f2d584bb9660 |
| 3(h) | 72a4d6aa54af6b51271259c679804611ba4597f5c901673761af4638d9315a78 |
| 8a(d) | 50bffd91d1b19d2ed6a044c220c70f13b33638af14eb839855ec46c60342925b |
| 8a(e) | 448d42a22a32a5a1cf63695367897d5cc98f0f0b31e6b992d3cdcd2c171e2b7d |
| 8a(g) | d59bd4f8bd06744dff7d469231aec29da1146864b47ef90c1a3e6083586daf36 |
| 8a(h) | 3d3e67316a21c47fde3b31cccef7e5d8f33d6acb456c61ce8703af19e7c8460c |
| 8b(d) | 8bddf98fdcd8f102a086abfd09ff6bbdd4b903f05b6b02b360c7d6e9a5a6df97 |
| 8b(e) | f9d42cc921e75f5c34cc89f740bd48c41435646d35e987d84c0cedce6d8c7c95 |
| 8b(g) | 45d1925c9f6c875934432208da84de4c436fcff5db4f6dbda48904d21d57a1b1 |
| 8b(h) | a90a90d075bab1b7d821c2cc7500d7323b712715936cb3ce0ef3f1194a128bb8 |
| 9(d) | 5c21fec124aa90d849c2ba94b3b5d049bffea64852ea497e204c804e85a9d86b |
| 9(e) | a06dcd3c2a2168b1477a6f79119e612a6a7158450a7fece75cbe71e0c2558814 |
| 9(g) | 7a0408a220f5b809a65cbb64d3fb65d95b6335d017792335926dd7ef4abdf94a |
| 9(h) | 16998ab479d8cdc2b34b76c8d781a0608af5706a0e32a2d072e01a6c22229d47 |
| 10(d) | 50840ded219a78a9f26b4b8634a14480e5ef5f6ceb4e9546711e1e990a47824a |
| 10(e) | f708f297dea8489af9dff9a9abda9c1289b4a1e449b5ce99011e31f39345b603 |
| 10(g) | 2a2f362becd78ff56ae0fe70d540783224caf3ba6b8df52adf6d4055e6682f72 |
| 10(h) | b47c49560fa6a7dd007b948b7b73d8d3420250da0ef86473926d096b736a390e |
| 4 | fc140fb363c2880a6ad4044547d651a95f3e0b2331f4c8f24148a188cd5eb60a |
| 5 | f717c41fbbeaebe05ba5f6d4487fc21983ef8650db4ae4a71665c900956fbedb |
| 6 | 71e9facbb1accd7b9339b79993aaab8d2829f113250db0b7ee1bdcf2ffae80aa |
| 11 | f771edaa32d289030a74d7189648bab320f53c24543262825a52bff3fc797449 |
| 12 | 6b73101b3aad0baea3bd1a2ca3d6212077528516b286cb108a32f972c036671e |
| 14 | 647156c672e55b5f86525437cb48b58f7e69078c9e39ca7e1ba8b729b780c3a6 |
| 13 | 092e3a4875fe86adf11131745dbc0c146a982515002b44daf6406ee928db9b84 |
| 7 | 86773be221eb5e9d820294df7461721c01f9df0aac04ca9f8b66b70830821d02 |
| 15 | 7a60d70bcfbbbfa555d2e0c7181eb1bcb3187677f4a6f8ac4c7452ff613a12fc |
| 16 | 0f76ecb634638a67f68c0728370c592d43b31b38b3ccde6dc6c2d7c174edb44e |
| 17 | 31117d838592d91e2901cdbbbc25ab6ddde06e1f462f23a3d043c8974973312d |
| 20 | e69c889c4021467127fd0589b3546974c7726f302201f4389749b724db35e7ca |
| 21 | 01ed960f703ca2f324cbc7f80d1669824b80307f2b0302c0e053541c678be277 |
| 22 | e11951cb4d3a686d6f7a0ef1a1ce5a3c2cefd39849da3fe395d105c371f5b1d5 |
| (rest of the document) | 9b5ec474c37e31a1a667821669b753fb7357857a86f4d07c43af9f9de2bff699 |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass d8a8e06296ea

| field | value |
| --- | --- |
| date | 2026-11-04 |
| review scope | lines 1a(d), 1a(e), 1a(g), 1a(h), 1b(d), 1b(e), 1b(g), 1b(h), 2(d), 2(e), 2(g), 2(h), 3(d), 3(e), 3(g), 3(h), 8a(d), 8a(e), 8a(g), 8a(h), 8b(d), 8b(e), 8b(g), 8b(h), 9(d), 9(e), 9(g), 9(h), 10(d), 10(e), 10(g), 10(h), 7, 15 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | d8a8e06296ea43c0f4c614efd6fa950ca88ca83b0f06663b6bd944cb8d27ec07 |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | bf1b84f240ed92e41aa326eb249d489746c10942aa6972948691ecd7e6ef2e1a |
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
| i1040sd | 2025; printed date 2025-12-11 | 10, 11, 12 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 11, 12 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| p550 | 2025 returns; printed date 2026-03-05 | 82, 86 | pages named by another document's citation | e40622e028486d7eb31a6da342ba2ba3c8b2f7ea9d341d9f47a1d33407d5aa26 | 82, 86 | 7629580e9cb35aa5f67e5d7c035b45850164eb1fe458f8acaa2781578ad0bf51 |

##### Raw response

```yaml
lines:
  - key: "1a(d)"
    status: MATCH
    reason: "It restates the column (d) proceeds total for the short-term basis-reported no-adjustment aggregate route, which is what Schedule D line 1a totals."
  - key: "1a(e)"
    status: MATCH
    reason: "It restates the column (e) cost or other basis total for the short-term basis-reported no-adjustment aggregate route, matching line 1a."
  - key: "1a(g)"
    status: MATCH
    reason: "For the qualifying aggregate population there are no adjustments, so summing the column (g) adjustment field yields the line 1a column (g) amount."
  - key: "1a(h)"
    status: MATCH
    reason: "It restates column (h) as proceeds less basis plus adjustments for the short-term aggregate population, matching line 1a column (h)."
  - key: "1b(d)"
    status: MATCH
    reason: "It restates the column (d) proceeds total for short-term basis-reported transactions reported on Form 8949 in detail, matching line 1b."
  - key: "1b(e)"
    status: MATCH
    reason: "It restates the column (e) cost or other basis total for short-term basis-reported Form 8949 detail transactions, matching line 1b."
  - key: "1b(g)"
    status: MATCH
    reason: "It restates the column (g) adjustment total for short-term Form 8949 detail transactions, matching line 1b column (g)."
  - key: "1b(h)"
    status: MATCH
    reason: "It restates column (h) as proceeds less basis plus adjustments for short-term Form 8949 detail transactions, matching line 1b."
  - key: "2(d)"
    status: MATCH
    reason: "It restates the column (d) proceeds total for short-term basis-not-reported Form 8949 detail transactions, matching line 2."
  - key: "2(e)"
    status: MATCH
    reason: "It restates the column (e) correct basis total for short-term basis-not-reported Form 8949 detail transactions, matching line 2."
  - key: "2(g)"
    status: MATCH
    reason: "It restates the column (g) adjustment total for short-term basis-not-reported Form 8949 detail transactions, matching line 2."
  - key: "2(h)"
    status: MATCH
    reason: "It restates column (h) as proceeds less basis plus adjustments for short-term basis-not-reported Form 8949 detail transactions, matching line 2."
  - key: "3(d)"
    status: MATCH
    reason: "It restates the column (d) proceeds total for short-term non-1099-B/1099-DA Form 8949 detail transactions, matching line 3."
  - key: "3(e)"
    status: MATCH
    reason: "It restates the column (e) correct basis total for short-term non-1099-B/1099-DA Form 8949 detail transactions, matching line 3."
  - key: "3(g)"
    status: MATCH
    reason: "It restates the column (g) adjustment total for short-term non-1099-B/1099-DA Form 8949 detail transactions, matching line 3."
  - key: "3(h)"
    status: MATCH
    reason: "It restates column (h) as proceeds less basis plus adjustments for short-term non-1099-B/1099-DA Form 8949 detail transactions, matching line 3."
  - key: "8a(d)"
    status: MATCH
    reason: "It restates the column (d) proceeds total for the long-term basis-reported no-adjustment aggregate route, matching line 8a."
  - key: "8a(e)"
    status: MATCH
    reason: "It restates the column (e) cost or other basis total for the long-term basis-reported no-adjustment aggregate route, matching line 8a."
  - key: "8a(g)"
    status: MATCH
    reason: "For the qualifying aggregate population there are no adjustments, so summing the column (g) adjustment field yields the line 8a column (g) amount."
  - key: "8a(h)"
    status: MATCH
    reason: "It restates column (h) as proceeds less basis plus adjustments for the long-term aggregate population, matching line 8a column (h)."
  - key: "8b(d)"
    status: MATCH
    reason: "It restates the column (d) proceeds total for long-term basis-reported Form 8949 detail transactions, matching line 8b."
  - key: "8b(e)"
    status: MATCH
    reason: "It restates the column (e) cost or other basis total for long-term basis-reported Form 8949 detail transactions, matching line 8b."
  - key: "8b(g)"
    status: MATCH
    reason: "It restates the column (g) adjustment total for long-term Form 8949 detail transactions, matching line 8b column (g)."
  - key: "8b(h)"
    status: MATCH
    reason: "It restates column (h) as proceeds less basis plus adjustments for long-term Form 8949 detail transactions, matching line 8b."
  - key: "9(d)"
    status: MATCH
    reason: "It restates the column (d) proceeds total for long-term basis-not-reported Form 8949 detail transactions, matching line 9."
  - key: "9(e)"
    status: MATCH
    reason: "It restates the column (e) correct basis total for long-term basis-not-reported Form 8949 detail transactions, matching line 9."
  - key: "9(g)"
    status: MATCH
    reason: "It restates the column (g) adjustment total for long-term basis-not-reported Form 8949 detail transactions, matching line 9."
  - key: "9(h)"
    status: MATCH
    reason: "It restates column (h) as proceeds less basis plus adjustments for long-term basis-not-reported Form 8949 detail transactions, matching line 9."
  - key: "10(d)"
    status: MATCH
    reason: "It restates the column (d) proceeds total for long-term non-1099-B/1099-DA Form 8949 detail transactions, matching line 10."
  - key: "10(e)"
    status: MATCH
    reason: "It restates the column (e) correct basis total for long-term non-1099-B/1099-DA Form 8949 detail transactions, matching line 10."
  - key: "10(g)"
    status: MATCH
    reason: "It restates the column (g) adjustment total for long-term non-1099-B/1099-DA Form 8949 detail transactions, matching line 10."
  - key: "10(h)"
    status: MATCH
    reason: "It restates column (h) as proceeds less basis plus adjustments for long-term non-1099-B/1099-DA Form 8949 detail transactions, matching line 10."
  - key: "7"
    status: MATCH
    reason: "It combines the column (h) amounts for lines 1a through 3 and lines 4 through 6, which is what Schedule D line 7 says to combine."
  - key: "15"
    status: MATCH
    reason: "It combines the column (h) amounts for lines 8a through 10 and lines 11 through 14, which is what Schedule D line 15 says to combine."
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
