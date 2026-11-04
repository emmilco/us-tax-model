# Render comparison — sd

The rendered English of every printed line of `Schedule D — securities sales and supplied distribution subtotals` (`rendered/2025/sd.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| line-scoped reviews | 1 (latest 2026-11-04); see Line-scoped reviews |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | d8a1bade7e8895260afb189920619c7b281ba3f35ca05706a6924a7e0636eac5 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | eeaf337d5fa7492478be5ffa58f4ffcda447017332dba311b038e96279119959 |
| lines judged | 46 |
| match / mismatch / unclear / missing | 44 / 2 / 0 / 0 |
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

Model: Sums proceeds of Box A sales routed to aggregate, which matches line 1a for 1099-B transactions where basis was reported to the IRS and no adjustments apply. The aggregate-eligibility refusal (sales.bad_aggregate) excludes ineligible sales, and digital-asset (Box G) sales are refused.
Reviewed in: pass d8a8e06296ea

### 1a(e) — Line 1a, column (e) totals
Status: **MATCH**

Model: For Box A, column (e) is the broker-reported basis, as Exception 1 requires. Sales with corrections or codes are refused from the aggregate route.
Reviewed in: pass d8a8e06296ea

### 1a(g) — Line 1a, column (g) totals
Status: **MATCH**

Model: Aggregate eligibility requires code 'none', so column (g) works out to zero. This is consistent with line 1a covering transactions "for which you have no adjustments."
Reviewed in: pass d8a8e06296ea

### 1a(h) — Line 1a, column (h) totals
Status: **MATCH**

Model: Column (h) is proceeds less basis plus column (g), per "Subtract column (e) from column (d) and combine the result with column (g)," summed over aggregate Box A sales.
Reviewed in: pass d8a8e06296ea

### 1b(d) — Line 1b, column (d) totals
Status: **MATCH**

Model: Sums proceeds of Box A detail sales, matching Form 8949 line 2 totals carried to line 1b "if Box A or Box G above is checked." Box G is excluded by the digital-asset refusal.
Reviewed in: pass d8a8e06296ea

### 1b(e) — Line 1b, column (e) totals
Status: **MATCH**

Model: For Box A, column (e) is the reported basis even if it is incorrect, with a code B correction placed in column (g), as the Form 8949 Note and code B instructions require.
Reviewed in: pass d8a8e06296ea

### 1b(g) — Line 1b, column (g) totals
Status: **MATCH**

Model: Adds the code B correction (reported minus correct basis: positive when the reported basis is larger, negative otherwise, per the Worksheet for Basis Adjustments) and the code W wash-sale loss as a positive number. Other codes are refused.
Reviewed in: pass d8a8e06296ea

### 1b(h) — Line 1b, column (h) totals
Status: **MATCH**

Model: Sums per-sale column (h), which is (d) − (e) + (g), over Box A detail sales.
Reviewed in: pass d8a8e06296ea

### 2(d) — Line 2, column (d) totals
Status: **MATCH**

Model: Sums proceeds of Box B detail sales, which carry to line 2. Box H is excluded by the digital-asset refusal, and an aggregate Box B sale is refused.
Reviewed in: pass d8a8e06296ea

### 2(e) — Line 2, column (e) totals
Status: **MATCH**

Model: For Box B, column (e) is the correct basis from records, per "enter the correct basis in column (e), and enter -0- in column (g)."
Reviewed in: pass d8a8e06296ea

### 2(g) — Line 2, column (g) totals
Status: **MATCH**

Model: The basis correction is zero because the sale is not covered, and code B on an uncovered sale is otherwise refused. The wash-sale amount is added as a positive number per code W.
Reviewed in: pass d8a8e06296ea

### 2(h) — Line 2, column (h) totals
Status: **MATCH**

Model: Sums (d) − (e) + (g) over Box B detail sales.
Reviewed in: pass d8a8e06296ea

### 3(d) — Line 3, column (d) totals
Status: **MATCH**

Model: Sums proceeds (net proceeds if there is no report) of Box C detail sales, which carry to line 3. Box I is excluded by the digital-asset refusal.
Reviewed in: pass d8a8e06296ea

### 3(e) — Line 3, column (e) totals
Status: **MATCH**

Model: For Box C, column (e) is the correct adjusted basis from records.
Reviewed in: pass d8a8e06296ea

### 3(g) — Line 3, column (g) totals
Status: **MATCH**

Model: Code B on Box C is refused. Only the wash-sale amount can be nonzero, and it is entered as a positive number per code W.
Reviewed in: pass d8a8e06296ea

### 3(h) — Line 3, column (h) totals
Status: **MATCH**

Model: Sums (d) − (e) + (g) over Box C detail sales.
Reviewed in: pass d8a8e06296ea

### 8a(d) — Line 8a, column (d) totals
Status: **MATCH**

Model: Sums proceeds of Box D sales routed to aggregate, matching line 8a for long-term transactions where basis was reported to the IRS and no adjustments apply. Ineligible and digital-asset sales are refused.
Reviewed in: pass d8a8e06296ea

### 8a(e) — Line 8a, column (e) totals
Status: **MATCH**

Model: For Box D, column (e) is the broker-reported basis, and the aggregate route forbids corrections.
Reviewed in: pass d8a8e06296ea

### 8a(g) — Line 8a, column (g) totals
Status: **MATCH**

Model: Aggregate eligibility requires no codes, so column (g) is zero, consistent with "no adjustments."
Reviewed in: pass d8a8e06296ea

### 8a(h) — Line 8a, column (h) totals
Status: **MATCH**

Model: Sums (d) − (e) + (g) over aggregate Box D sales, consistent with the line 8a example ($6,000 − $2,000 = $4,000).
Reviewed in: pass d8a8e06296ea

### 8b(d) — Line 8b, column (d) totals
Status: **MATCH**

Model: Sums proceeds of Box D detail sales, which carry to line 8b "if Box D or Box J above is checked." Box J is refused.
Reviewed in: pass d8a8e06296ea

### 8b(e) — Line 8b, column (e) totals
Status: **MATCH**

Model: For Box D, column (e) is the reported basis, with any error corrected in column (g).
Reviewed in: pass d8a8e06296ea

### 8b(g) — Line 8b, column (g) totals
Status: **MATCH**

Model: Combines the code B correction (signed as on the Worksheet for Basis Adjustments) with the positive code W amount, as the net adjustment.
Reviewed in: pass d8a8e06296ea

### 8b(h) — Line 8b, column (h) totals
Status: **MATCH**

Model: Sums (d) − (e) + (g) over Box D detail sales.
Reviewed in: pass d8a8e06296ea

### 9(d) — Line 9, column (d) totals
Status: **MATCH**

Model: Sums proceeds of Box E detail sales, which carry to line 9. Box K is refused.
Reviewed in: pass d8a8e06296ea

### 9(e) — Line 9, column (e) totals
Status: **MATCH**

Model: For Box E, column (e) is the correct basis, per the code B instruction for Box E.
Reviewed in: pass d8a8e06296ea

### 9(g) — Line 9, column (g) totals
Status: **MATCH**

Model: The basis correction is zero for uncovered sales, and only the positive code W amount can apply.
Reviewed in: pass d8a8e06296ea

### 9(h) — Line 9, column (h) totals
Status: **MATCH**

Model: Sums (d) − (e) + (g) over Box E detail sales.
Reviewed in: pass d8a8e06296ea

### 10(d) — Line 10, column (d) totals
Status: **MATCH**

Model: Sums proceeds of Box F detail sales, which carry to line 10. Box L is refused.
Reviewed in: pass d8a8e06296ea

### 10(e) — Line 10, column (e) totals
Status: **MATCH**

Model: For Box F, column (e) is the correct adjusted basis from records.
Reviewed in: pass d8a8e06296ea

### 10(g) — Line 10, column (g) totals
Status: **MATCH**

Model: Code B on Box F is refused, so only the positive code W amount can be nonzero.
Reviewed in: pass d8a8e06296ea

### 10(h) — Line 10, column (h) totals
Status: **MATCH**

Model: Sums (d) − (e) + (g) over Box F detail sales.
Reviewed in: pass d8a8e06296ea

### 4 — Line 4: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 4 reports gains from Forms 6252, 4684, 6781 and 8824. It is zero, and the program refuses whenever such forms apply, so the line is correctly narrowed.

### 5 — Line 5: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 5 reports net short-term gain or loss from Schedule K-1. It is zero, and the program refuses when K-1 capital gains or losses exist.

### 6 — Short-term capital loss carryover, from line 8 of the Capital Loss Carryover Worksheet (a
Status: **MATCH**

Model: When 2024 line 21 showed a loss, line 6 enters Capital Loss Carryover Worksheet line 8 as a negative amount, matching the parenthesized line 6 ('from line 8 of your Capital Loss Carryover Worksheet'). Otherwise it is zero.

### 11 — Line 11: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 11 reports gains from Forms 4797, 2439, 6252, 4684, 6781 and 8824. It is zero, and the program refuses when any of these forms applies.

### 12 — Line 12: zero only after unsupported source/carryover screening
Status: **MATCH**

Model: Line 12 reports net long-term K-1 gain or loss. It is zero, and the program refuses when K-1 capital items exist.

### 14 — Long-term capital loss carryover, from line 13 of the Capital Loss Carryover Worksheet (a
Status: **MATCH**

Model: When 2024 line 21 showed a loss, line 14 enters worksheet line 13 as a negative amount, matching 'Enter the amount, if any, from line 13 of your Capital Loss Carryover Worksheet' shown in parentheses.

### 13 — Capital gain distributions
Status: **MATCH**

Model: Line 13 enters total capital gain distributions (Form 1099-DIV box 2a), matching 'Report the total gain (box 2a) on Schedule D, line 13'. Unsupported distribution cases are refused.

### 7 — Combine the amounts for Schedule D line 7
Status: **MATCH**

Model: "Combine lines 1a through 6 in column (h)": adds 1a(h), 1b(h), 2(h), 3(h), 4, 5 and 6, with line 6 held as a negative amount.
Reviewed in: pass d8a8e06296ea

### 15 — Combine the amounts for Schedule D line 15
Status: **MATCH**

Model: "Combine lines 8a through 14 in column (h)": adds 8a(h), 8b(h), 9(h), 10(h), 11, 12, 13 and 14, with line 14 held as a negative amount.
Reviewed in: pass d8a8e06296ea

### 16 — Combine the amounts for Schedule D line 16
Status: **MATCH**

Model: Matches 'Combine lines 7 and 15'.

### 17 — Are lines 15 and 16 both gains?
Status: **MATCH**

Model: Matches 'Are lines 15 and 16 both gains?' as both amounts being greater than zero.

### 20 — Are lines 18 and 19 zero and are you not filing Form 4952?
Status: **MISMATCH**

Restated: helper "Line 18. 28% Rate Gain Worksheet result, or zero when line 17 is No (lines 18 through 21 skipped)" = $0 and helper "Line 19. Unrecaptured Section 1250 Gain Worksheet result, or zero when line 17 is No (lines 18 through 21 skipped)" = $0 and helper "Are you filing Form 4952?" = false

Model: The restatement answers line 20 in every case. The IRS says 'If line 16 is a loss, skip lines 17 through 20' and, on line 17 No, 'Skip lines 18 through 21, and go to line 22'. On those paths the program answers Yes (QDCGT, don't complete lines 21 and 22) where the line should be skipped.

Ruling: representation; f1040sd p. 2, line 17: "No. Skip lines 18 through 21, and go to line 22". Line 20 (and line 22) are Boolean flow predicates, evaluated on every path by the documented convention (forms/2025/sd.yaml form note); the path the filer follows, and which lines show, is decided by line 17 and line 16 upstream, so the answer on a skipped path is never read. Same reading as the earlier rounds.

### 21 — Deductible loss, signed; zero when line 21 is skipped
Status: **MATCH**

Model: When line 16 is a loss, line 21 takes the larger signed amount of line 16 and -$3,000 (-$1,500 MFS). This equals 'the smaller of: The loss on line 16; or ($3,000), or if married filing separately, ($1,500)' treated as positive numbers.

### 22 — Do you have qualified dividends?
Status: **MISMATCH**

Restated: f1040 line 3a > $0

Model: The restatement answers line 22 unconditionally. The IRS line 20 says 'Don't complete lines 21 and 22 below', so line 22 should be completed only when line 16 is a loss or zero or line 17 is No.

Ruling: representation; f1040sd p. 2, line 17: "No. Skip lines 18 through 21, and go to line 22". Line 20 (and line 22) are Boolean flow predicates, evaluated on every path by the documented convention (forms/2025/sd.yaml form note); the path the filer follows, and which lines show, is decided by line 17 and line 16 upstream, so the answer on a skipped path is never read. Same reading as the earlier rounds.

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
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | d8a8e06296ea43c0f4c614efd6fa950ca88ca83b0f06663b6bd944cb8d27ec07 |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | bf1b84f240ed92e41aa326eb249d489746c10942aa6972948691ecd7e6ef2e1a |
| receipt | .transcription/sd.render.lines-c9db5685c8a4 |
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
```yaml
lines:
  - key: "1a(d)"
    status: MATCH
    reason: "Sums proceeds of Box A sales routed to aggregate, which matches line 1a for 1099-B transactions where basis was reported to the IRS and no adjustments apply. The aggregate-eligibility refusal (sales.bad_aggregate) excludes ineligible sales, and digital-asset (Box G) sales are refused."
  - key: "1a(e)"
    status: MATCH
    reason: "For Box A, column (e) is the broker-reported basis, as Exception 1 requires. Sales with corrections or codes are refused from the aggregate route."
  - key: "1a(g)"
    status: MATCH
    reason: "Aggregate eligibility requires code 'none', so column (g) works out to zero. This is consistent with line 1a covering transactions \"for which you have no adjustments.\""
  - key: "1a(h)"
    status: MATCH
    reason: "Column (h) is proceeds less basis plus column (g), per \"Subtract column (e) from column (d) and combine the result with column (g),\" summed over aggregate Box A sales."
  - key: "1b(d)"
    status: MATCH
    reason: "Sums proceeds of Box A detail sales, matching Form 8949 line 2 totals carried to line 1b \"if Box A or Box G above is checked.\" Box G is excluded by the digital-asset refusal."
  - key: "1b(e)"
    status: MATCH
    reason: "For Box A, column (e) is the reported basis even if it is incorrect, with a code B correction placed in column (g), as the Form 8949 Note and code B instructions require."
  - key: "1b(g)"
    status: MATCH
    reason: "Adds the code B correction (reported minus correct basis: positive when the reported basis is larger, negative otherwise, per the Worksheet for Basis Adjustments) and the code W wash-sale loss as a positive number. Other codes are refused."
  - key: "1b(h)"
    status: MATCH
    reason: "Sums per-sale column (h), which is (d) − (e) + (g), over Box A detail sales."
  - key: "2(d)"
    status: MATCH
    reason: "Sums proceeds of Box B detail sales, which carry to line 2. Box H is excluded by the digital-asset refusal, and an aggregate Box B sale is refused."
  - key: "2(e)"
    status: MATCH
    reason: "For Box B, column (e) is the correct basis from records, per \"enter the correct basis in column (e), and enter -0- in column (g).\""
  - key: "2(g)"
    status: MATCH
    reason: "The basis correction is zero because the sale is not covered, and code B on an uncovered sale is otherwise refused. The wash-sale amount is added as a positive number per code W."
  - key: "2(h)"
    status: MATCH
    reason: "Sums (d) − (e) + (g) over Box B detail sales."
  - key: "3(d)"
    status: MATCH
    reason: "Sums proceeds (net proceeds if there is no report) of Box C detail sales, which carry to line 3. Box I is excluded by the digital-asset refusal."
  - key: "3(e)"
    status: MATCH
    reason: "For Box C, column (e) is the correct adjusted basis from records."
  - key: "3(g)"
    status: MATCH
    reason: "Code B on Box C is refused. Only the wash-sale amount can be nonzero, and it is entered as a positive number per code W."
  - key: "3(h)"
    status: MATCH
    reason: "Sums (d) − (e) + (g) over Box C detail sales."
  - key: "8a(d)"
    status: MATCH
    reason: "Sums proceeds of Box D sales routed to aggregate, matching line 8a for long-term transactions where basis was reported to the IRS and no adjustments apply. Ineligible and digital-asset sales are refused."
  - key: "8a(e)"
    status: MATCH
    reason: "For Box D, column (e) is the broker-reported basis, and the aggregate route forbids corrections."
  - key: "8a(g)"
    status: MATCH
    reason: "Aggregate eligibility requires no codes, so column (g) is zero, consistent with \"no adjustments.\""
  - key: "8a(h)"
    status: MATCH
    reason: "Sums (d) − (e) + (g) over aggregate Box D sales, consistent with the line 8a example ($6,000 − $2,000 = $4,000)."
  - key: "8b(d)"
    status: MATCH
    reason: "Sums proceeds of Box D detail sales, which carry to line 8b \"if Box D or Box J above is checked.\" Box J is refused."
  - key: "8b(e)"
    status: MATCH
    reason: "For Box D, column (e) is the reported basis, with any error corrected in column (g)."
  - key: "8b(g)"
    status: MATCH
    reason: "Combines the code B correction (signed as on the Worksheet for Basis Adjustments) with the positive code W amount, as the net adjustment."
  - key: "8b(h)"
    status: MATCH
    reason: "Sums (d) − (e) + (g) over Box D detail sales."
  - key: "9(d)"
    status: MATCH
    reason: "Sums proceeds of Box E detail sales, which carry to line 9. Box K is refused."
  - key: "9(e)"
    status: MATCH
    reason: "For Box E, column (e) is the correct basis, per the code B instruction for Box E."
  - key: "9(g)"
    status: MATCH
    reason: "The basis correction is zero for uncovered sales, and only the positive code W amount can apply."
  - key: "9(h)"
    status: MATCH
    reason: "Sums (d) − (e) + (g) over Box E detail sales."
  - key: "10(d)"
    status: MATCH
    reason: "Sums proceeds of Box F detail sales, which carry to line 10. Box L is refused."
  - key: "10(e)"
    status: MATCH
    reason: "For Box F, column (e) is the correct adjusted basis from records."
  - key: "10(g)"
    status: MATCH
    reason: "Code B on Box F is refused, so only the positive code W amount can be nonzero."
  - key: "10(h)"
    status: MATCH
    reason: "Sums (d) − (e) + (g) over Box F detail sales."
  - key: "7"
    status: MATCH
    reason: "\"Combine lines 1a through 6 in column (h)\": adds 1a(h), 1b(h), 2(h), 3(h), 4, 5 and 6, with line 6 held as a negative amount."
  - key: "15"
    status: MATCH
    reason: "\"Combine lines 8a through 14 in column (h)\": adds 8a(h), 8b(h), 9(h), 10(h), 11, 12, 13 and 14, with line 14 held as a negative amount."
```
```

## Raw response

```yaml
```yaml
lines:
  - key: "1a(d)"
    status: MATCH
    reason: "Sums column (d) proceeds for box A sales routed to aggregate, which is line 1a: short-term 1099-B transactions with basis reported and no adjustments. Ineligible aggregate entries and digital assets (1099-DA) are refused."
  - key: "1a(e)"
    status: MATCH
    reason: "For box A, column (e) is the basis shown on the broker report, which is the reported basis line 1a requires."
  - key: "1a(g)"
    status: MATCH
    reason: "The aggregate route requires code 'none', so column (g) sums to zero. This fits line 1a, which is limited to transactions 'for which you have no adjustments'."
  - key: "1a(h)"
    status: MATCH
    reason: "Column (h) is proceeds less basis plus column (g), summed. This follows 'Subtract the cost or other basis in column (e) from the proceeds (sales price) in column (d).'"
  - key: "1b(d)"
    status: MATCH
    reason: "Sums proceeds for box A transactions reported in detail, which is line 1b ('Box A or Box G checked'). Box G digital assets are refused."
  - key: "1b(e)"
    status: MATCH
    reason: "For box A, column (e) is the reported basis even if incorrect. This matches the 8949 instruction to 'enter the basis shown on Form 1099-B ... in column (e), even though that basis is incorrect.'"
  - key: "1b(g)"
    status: MATCH
    reason: "Column (g) combines the code B correction (reported minus correct basis, matching worksheet lines 3–4) with the code W nondeductible loss as a positive amount. Both follow the 8949 instructions."
  - key: "1b(h)"
    status: MATCH
    reason: "Column (h) is (d) minus (e) combined with (g), summed over box A detail entries, as the line 1b column (h) instructions say."
  - key: "2(d)"
    status: MATCH
    reason: "Sums proceeds for box B detail entries; line 2 is 'Box B or Box H checked'. Box H is refused as a digital asset."
  - key: "2(e)"
    status: MATCH
    reason: "For box B (basis not reported), column (e) is the correct basis. This matches 'enter the correct basis in column (e), and enter -0- in column (g).'"
  - key: "2(g)"
    status: MATCH
    reason: "The basis correction applies only when basis was reported to the IRS, so box B gets no code B adjustment in (g). Only a code W adjustment can apply, consistent with the instructions."
  - key: "2(h)"
    status: MATCH
    reason: "(d) minus (e) combined with (g), summed over box B entries."
  - key: "3(d)"
    status: MATCH
    reason: "Sums proceeds for box C entries; line 3 is 'Box C or Box I checked'. Box I is refused, and box C entries use net proceeds when there is no report."
  - key: "3(e)"
    status: MATCH
    reason: "For box C, column (e) is the correct adjusted basis from records. Code B with box C is refused."
  - key: "3(g)"
    status: MATCH
    reason: "Only a code W adjustment can apply to box C, and it is entered as a positive amount per the code W instructions."
  - key: "3(h)"
    status: MATCH
    reason: "(d) minus (e) combined with (g), summed over box C entries."
  - key: "8a(d)"
    status: MATCH
    reason: "Sums proceeds for box D aggregate-route sales, which is line 8a: long-term transactions with basis reported and no adjustments. Ineligible entries are refused."
  - key: "8a(e)"
    status: MATCH
    reason: "For box D, column (e) is the reported basis, as line 8a requires."
  - key: "8a(g)"
    status: MATCH
    reason: "The aggregate route requires no codes, so column (g) is zero, matching 'for which you have no adjustments'."
  - key: "8a(h)"
    status: MATCH
    reason: "Column (d) minus (e) plus (g), summed, consistent with the line 8a example."
  - key: "8b(d)"
    status: MATCH
    reason: "Sums proceeds for box D detail entries; line 8b is 'Box D or Box J checked'. Box J is refused."
  - key: "8b(e)"
    status: MATCH
    reason: "For box D, column (e) is the reported basis even if incorrect, with the correction made in (g)."
  - key: "8b(g)"
    status: MATCH
    reason: "Combines the code B correction (reported minus correct basis) with the code W positive adjustment, per the 8949 instructions."
  - key: "8b(h)"
    status: MATCH
    reason: "(d) minus (e) combined with (g), summed over box D detail entries."
  - key: "9(d)"
    status: MATCH
    reason: "Sums proceeds for box E entries; line 9 is 'Box E or Box K checked'. Box K is refused."
  - key: "9(e)"
    status: MATCH
    reason: "For box E (basis not reported), column (e) is the correct basis, as instructed."
  - key: "9(g)"
    status: MATCH
    reason: "No code B adjustment applies when basis was not reported; only code W can apply, consistent with the instructions."
  - key: "9(h)"
    status: MATCH
    reason: "(d) minus (e) combined with (g), summed over box E entries."
  - key: "10(d)"
    status: MATCH
    reason: "Sums proceeds for box F entries; line 10 is 'Box F or Box L checked'. Box L is refused."
  - key: "10(e)"
    status: MATCH
    reason: "For box F, column (e) is the correct adjusted basis from records. Code B with box F is refused."
  - key: "10(g)"
    status: MATCH
    reason: "Only a code W positive adjustment can apply to box F entries, per the instructions."
  - key: "10(h)"
    status: MATCH
    reason: "(d) minus (e) combined with (g), summed over box F entries."
  - key: "4"
    status: MATCH
    reason: "Line 4 reports gains from Forms 6252, 4684, 6781 and 8824. It is zero, and the program refuses whenever such forms apply, so the line is correctly narrowed."
  - key: "5"
    status: MATCH
    reason: "Line 5 reports net short-term gain or loss from Schedule K-1. It is zero, and the program refuses when K-1 capital gains or losses exist."
  - key: "6"
    status: MATCH
    reason: "When 2024 line 21 showed a loss, line 6 enters Capital Loss Carryover Worksheet line 8 as a negative amount, matching the parenthesized line 6 ('from line 8 of your Capital Loss Carryover Worksheet'). Otherwise it is zero."
  - key: "11"
    status: MATCH
    reason: "Line 11 reports gains from Forms 4797, 2439, 6252, 4684, 6781 and 8824. It is zero, and the program refuses when any of these forms applies."
  - key: "12"
    status: MATCH
    reason: "Line 12 reports net long-term K-1 gain or loss. It is zero, and the program refuses when K-1 capital items exist."
  - key: "14"
    status: MATCH
    reason: "When 2024 line 21 showed a loss, line 14 enters worksheet line 13 as a negative amount, matching 'Enter the amount, if any, from line 13 of your Capital Loss Carryover Worksheet' shown in parentheses."
  - key: "13"
    status: MATCH
    reason: "Line 13 enters total capital gain distributions (Form 1099-DIV box 2a), matching 'Report the total gain (box 2a) on Schedule D, line 13'. Unsupported distribution cases are refused."
  - key: "7"
    status: MATCH
    reason: "Matches 'Combine lines 1a through 6 in column (h)'. Line 6 is carried as a negative amount."
  - key: "15"
    status: MATCH
    reason: "Matches 'Combine lines 8a through 14 in column (h)'. Line 14 is carried as a negative amount."
  - key: "16"
    status: MATCH
    reason: "Matches 'Combine lines 7 and 15'."
  - key: "17"
    status: MATCH
    reason: "Matches 'Are lines 15 and 16 both gains?' as both amounts being greater than zero."
  - key: "20"
    status: MISMATCH
    reason: "The restatement answers line 20 in every case. The IRS says 'If line 16 is a loss, skip lines 17 through 20' and, on line 17 No, 'Skip lines 18 through 21, and go to line 22'. On those paths the program answers Yes (QDCGT, don't complete lines 21 and 22) where the line should be skipped."
  - key: "21"
    status: MATCH
    reason: "When line 16 is a loss, line 21 takes the larger signed amount of line 16 and -$3,000 (-$1,500 MFS). This equals 'the smaller of: The loss on line 16; or ($3,000), or if married filing separately, ($1,500)' treated as positive numbers."
  - key: "22"
    status: MISMATCH
    reason: "The restatement answers line 22 unconditionally. The IRS line 20 says 'Don't complete lines 21 and 22 below', so line 22 should be completed only when line 16 is a loss or zero or line 17 is No."
```
```
