# Render comparison — sd

The rendered English of every printed line of `Schedule D — securities sales and supplied distribution subtotals` (`rendered/2025/sd.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| line-scoped reviews | 2 (latest 2026-11-07); see Line-scoped reviews |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | d8a1bade7e8895260afb189920619c7b281ba3f35ca05706a6924a7e0636eac5 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
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

Model: Line 1a totals short-term transactions whose basis was reported to the IRS and that need no adjustments. Box A sales on the aggregate route meet this, because bad_aggregate refuses any entry without reported basis, with a code, or with an unconfirmed eligibility. Box G is refused as digital, and column (d) is the reported proceeds.
Reviewed in: pass 790975e2b01d

### 1a(e) — Line 1a, column (e) totals
Status: **MATCH**

Model: For box A (basis reported), column (e) is the basis shown on the broker report. The Schedule D example for lines 1a/8a enters exactly that cost or other basis in column (e).
Reviewed in: pass 790975e2b01d

### 1a(g) — Line 1a, column (g) totals
Status: **MATCH**

Model: Aggregate entries must have code 'none', so both the B correction and the W adjustment are $0. The sum is therefore zero, which fits the IRS condition 'for which you have no adjustments'.
Reviewed in: pass 790975e2b01d

### 1a(h) — Line 1a, column (h) totals
Status: **MATCH**

Model: Column (h) is (d) less (e) plus (g), with (g) zero, summed over aggregate box A sales. This matches 'Subtract the cost or other basis in column (e) from the proceeds (sales price) in column (d)'.
Reviewed in: pass 790975e2b01d

### 1b(d) — Line 1b, column (d) totals
Status: **MATCH**

Model: Line 1b is the Form 8949 total for transactions with Box A checked (Box G is refused as digital). Column (d) sums the proceeds of box A detail entries.
Reviewed in: pass 790975e2b01d

### 1b(e) — Line 1b, column (e) totals
Status: **MATCH**

Model: For box A, column (e) is the reported basis even when it is incorrect, as the 8949 instructions require for code B. Adding over the box A detail entries gives the line 2 total that carries to line 1b.
Reviewed in: pass 790975e2b01d

### 1b(g) — Line 1b, column (g) totals
Status: **MATCH**

Model: Column (g) adds the code B correction, figured as reported basis minus correct basis per the Worksheet for Basis Adjustments, and the code W nondeductible loss as a positive number. Other codes are refused.
Reviewed in: pass 790975e2b01d

### 1b(h) — Line 1b, column (h) totals
Status: **MATCH**

Model: Column (h) is (d) less (e), combined with (g), summed over box A detail entries. This matches the Lines 1b–10 column (h) instructions.
Reviewed in: pass 790975e2b01d

### 2(d) — Line 2, column (d) totals
Status: **MATCH**

Model: Line 2 totals Form 8949 transactions with Box B checked (Box H is refused as digital). Column (d) sums the proceeds of box B entries.
Reviewed in: pass 790975e2b01d

### 2(e) — Line 2, column (e) totals
Status: **MATCH**

Model: For box B, basis was not reported, so column (e) is the correct basis. This follows 'enter the correct basis in column (e), and enter -0- in column (g)'.
Reviewed in: pass 790975e2b01d

### 2(g) — Line 2, column (g) totals
Status: **MATCH**

Model: The B correction applies only to covered boxes, so it is $0 for box B, and the W amount is added. This is consistent with the code B and code W instructions.
Reviewed in: pass 790975e2b01d

### 2(h) — Line 2, column (h) totals
Status: **MATCH**

Model: Column (h) is (d) less (e) plus (g), summed over box B entries.
Reviewed in: pass 790975e2b01d

### 3(d) — Line 3, column (d) totals
Status: **MATCH**

Model: Line 3 totals Form 8949 transactions with Box C checked (Box I is refused as digital). Column (d) is net proceeds when there is no report.
Reviewed in: pass 790975e2b01d

### 3(e) — Line 3, column (e) totals
Status: **MATCH**

Model: For box C, column (e) is the correct basis from records.
Reviewed in: pass 790975e2b01d

### 3(g) — Line 3, column (g) totals
Status: **MATCH**

Model: Code B on box C is refused, so column (g) holds only the W amount. Summing it matches the Form 8949 totals.
Reviewed in: pass 790975e2b01d

### 3(h) — Line 3, column (h) totals
Status: **MATCH**

Model: Column (h) is (d) less (e) plus (g), summed over box C entries.
Reviewed in: pass 790975e2b01d

### 8a(d) — Line 8a, column (d) totals
Status: **MATCH**

Model: Line 8a is the long-term counterpart of line 1a. It sums the proceeds of box D aggregate-route sales, which are restricted to entries with reported basis and no adjustments.
Reviewed in: pass 790975e2b01d

### 8a(e) — Line 8a, column (e) totals
Status: **MATCH**

Model: Column (e) is the reported basis for box D, which matches the line 8a example ($2,000 in column (e)).
Reviewed in: pass 790975e2b01d

### 8a(g) — Line 8a, column (g) totals
Status: **MATCH**

Model: Aggregate entries carry no code, so column (g) is zero, consistent with 'no adjustments'.
Reviewed in: pass 790975e2b01d

### 8a(h) — Line 8a, column (h) totals
Status: **MATCH**

Model: Column (h) is (d) less (e), matching the example '$4,000 ($6,000 − $2,000) in column (h)'.
Reviewed in: pass 790975e2b01d

### 8b(d) — Line 8b, column (d) totals
Status: **MATCH**

Model: Line 8b totals Form 8949 transactions with Box D checked (Box J is refused). Column (d) sums the proceeds.
Reviewed in: pass 790975e2b01d

### 8b(e) — Line 8b, column (e) totals
Status: **MATCH**

Model: For box D, column (e) is the reported basis, with any error corrected in column (g).
Reviewed in: pass 790975e2b01d

### 8b(g) — Line 8b, column (g) totals
Status: **MATCH**

Model: Column (g) adds the code B worksheet correction (reported minus correct basis) and the code W positive amount.
Reviewed in: pass 790975e2b01d

### 8b(h) — Line 8b, column (h) totals
Status: **MATCH**

Model: Column (h) is (d) less (e) plus (g), summed over box D detail entries.
Reviewed in: pass 790975e2b01d

### 9(d) — Line 9, column (d) totals
Status: **MATCH**

Model: Line 9 totals Box E transactions (Box K is refused). Column (d) sums the proceeds.
Reviewed in: pass 790975e2b01d

### 9(e) — Line 9, column (e) totals
Status: **MATCH**

Model: For box E, column (e) is the correct basis, because basis was not reported to the IRS.
Reviewed in: pass 790975e2b01d

### 9(g) — Line 9, column (g) totals
Status: **MATCH**

Model: The B correction is $0 for a non-covered box, and the W amount is added, per the instructions.
Reviewed in: pass 790975e2b01d

### 9(h) — Line 9, column (h) totals
Status: **MATCH**

Model: Column (h) is (d) less (e) plus (g), summed over box E entries.
Reviewed in: pass 790975e2b01d

### 10(d) — Line 10, column (d) totals
Status: **MATCH**

Model: Line 10 totals Box F transactions (Box L is refused). Column (d) sums the proceeds.
Reviewed in: pass 790975e2b01d

### 10(e) — Line 10, column (e) totals
Status: **MATCH**

Model: For box F, column (e) is the correct basis from records.
Reviewed in: pass 790975e2b01d

### 10(g) — Line 10, column (g) totals
Status: **MATCH**

Model: Code B on box F is refused, so column (g) holds only the W amount, summed.
Reviewed in: pass 790975e2b01d

### 10(h) — Line 10, column (h) totals
Status: **MATCH**

Model: Column (h) is (d) less (e) plus (g), summed over box F entries.
Reviewed in: pass 790975e2b01d

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

Model: Line 13 is 'Capital gain distributions', and the instructions say to 'Report the total gain (box 2a) on Schedule D, line 13'; the restatement enters box 2a when distributions were received. The $0 screen adds nothing and only refuses unsupported cases such as box 2c section 1202 gain, which it names.
Reviewed in: pass 577abbc56b37

### 7 — Combine the amounts for Schedule D line 7
Status: **MATCH**

Model: The form says 'Combine lines 1a through 6 in column (h)'. The restatement adds the column (h) amounts of lines 1a–3 with lines 4, 5 and 6, and line 6 is held as a negative loss.
Reviewed in: pass 790975e2b01d

### 15 — Combine the amounts for Schedule D line 15
Status: **MATCH**

Model: The IRS text says 'Combine lines 8a through 14 in column (h)'. The restatement adds the column (h) totals of lines 8a, 8b, 9 and 10, plus lines 11, 12 and 13, plus line 14, which it holds as a negative loss carryover.
Reviewed in: pass 577abbc56b37

### 16 — Combine the amounts for Schedule D line 16
Status: **MATCH**

Model: Matches 'Combine lines 7 and 15'.

### 17 — Are lines 15 and 16 both gains?
Status: **MATCH**

Model: Matches 'Are lines 15 and 16 both gains?' as both amounts being greater than zero.

### 20 — Are lines 18 and 19 zero and are you not filing Form 4952?
Status: **MATCH**

Model: The IRS asks 'Are lines 18 and 19 both zero or blank and you are not filing Form 4952?' The restatement tests line 18 = $0, line 19 = $0, and not filing Form 4952. Blank or skipped lines 18 and 19 are held as zero.
Reviewed in: pass 577abbc56b37

### 21 — Deductible loss, signed; zero when line 21 is skipped
Status: **MATCH**

Model: When line 16 is a loss, line 21 takes the larger signed amount of line 16 and -$3,000 (-$1,500 MFS). This equals 'the smaller of: The loss on line 16; or ($3,000), or if married filing separately, ($1,500)' treated as positive numbers.

### 22 — Do you have qualified dividends?
Status: **MATCH**

Model: The IRS asks 'Do you have qualified dividends on Form 1040, 1040-SR, or 1040-NR, line 3a?' The restatement tests Form 1040 line 3a > $0. Its gate on ordinary dividends being above zero changes nothing, because 'Qualified dividends are also included in the ordinary dividend total required to be shown on line 3b.'
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
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 577abbc56b37d1cebe808323852558d3bd94585db765f728dbf63e0577cd43fe |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 884443bc10a74221ffffae8b97356b0c0610d7129346cbeb06b585fdb1bbc439 |
| receipt | .transcription/sd.render.lines-6a3b38decded |
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
```yaml
lines:
  - key: "13"
    status: MATCH
    reason: "Line 13 is 'Capital gain distributions', and the instructions say to 'Report the total gain (box 2a) on Schedule D, line 13'; the restatement enters box 2a when distributions were received. The $0 screen adds nothing and only refuses unsupported cases such as box 2c section 1202 gain, which it names."
  - key: "15"
    status: MATCH
    reason: "The IRS text says 'Combine lines 8a through 14 in column (h)'. The restatement adds the column (h) totals of lines 8a, 8b, 9 and 10, plus lines 11, 12 and 13, plus line 14, which it holds as a negative loss carryover."
  - key: "20"
    status: MATCH
    reason: "The IRS asks 'Are lines 18 and 19 both zero or blank and you are not filing Form 4952?' The restatement tests line 18 = $0, line 19 = $0, and not filing Form 4952. Blank or skipped lines 18 and 19 are held as zero."
  - key: "22"
    status: MATCH
    reason: "The IRS asks 'Do you have qualified dividends on Form 1040, 1040-SR, or 1040-NR, line 3a?' The restatement tests Form 1040 line 3a > $0. Its gate on ordinary dividends being above zero changes nothing, because 'Qualified dividends are also included in the ordinary dividend total required to be shown on line 3b.'"
```
```

#### Pass 790975e2b01d

| field | value |
| --- | --- |
| date | 2026-11-07 |
| review scope | lines 1a(d), 1a(e), 1a(g), 1a(h), 1b(d), 1b(e), 1b(g), 1b(h), 2(d), 2(e), 2(g), 2(h), 3(d), 3(e), 3(g), 3(h), 8a(d), 8a(e), 8a(g), 8a(h), 8b(d), 8b(e), 8b(g), 8b(h), 9(d), 9(e), 9(g), 9(h), 10(d), 10(e), 10(g), 10(h), 7, 15 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 790975e2b01d251806ec7900a96a0b7cb849c378d67aa63773d66eba4ffdf4e0 |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 329cc96b9d07419958471ec059f8d25fd2da2c05e9915067d6fad57d1b87a01d |
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
| i1040sd | 2025; printed date 2025-12-11 | 5, 6, 10, 11, 12 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 5, 6, 11, 12 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| p550 | 2025 returns; printed date 2026-03-05 | 59, 60, 61, 81, 82, 86, 87, 88 | pages named by another document's citation | e40622e028486d7eb31a6da342ba2ba3c8b2f7ea9d341d9f47a1d33407d5aa26 | 59, 60, 61, 81, 82, 86, 87, 88 | 7629580e9cb35aa5f67e5d7c035b45850164eb1fe458f8acaa2781578ad0bf51 |

##### Raw response

```yaml
```yaml
lines:
  - key: "1a(d)"
    status: MATCH
    reason: "Line 1a totals short-term transactions whose basis was reported to the IRS and that need no adjustments. Box A sales on the aggregate route meet this, because bad_aggregate refuses any entry without reported basis, with a code, or with an unconfirmed eligibility. Box G is refused as digital, and column (d) is the reported proceeds."
  - key: "1a(e)"
    status: MATCH
    reason: "For box A (basis reported), column (e) is the basis shown on the broker report. The Schedule D example for lines 1a/8a enters exactly that cost or other basis in column (e)."
  - key: "1a(g)"
    status: MATCH
    reason: "Aggregate entries must have code 'none', so both the B correction and the W adjustment are $0. The sum is therefore zero, which fits the IRS condition 'for which you have no adjustments'."
  - key: "1a(h)"
    status: MATCH
    reason: "Column (h) is (d) less (e) plus (g), with (g) zero, summed over aggregate box A sales. This matches 'Subtract the cost or other basis in column (e) from the proceeds (sales price) in column (d)'."
  - key: "1b(d)"
    status: MATCH
    reason: "Line 1b is the Form 8949 total for transactions with Box A checked (Box G is refused as digital). Column (d) sums the proceeds of box A detail entries."
  - key: "1b(e)"
    status: MATCH
    reason: "For box A, column (e) is the reported basis even when it is incorrect, as the 8949 instructions require for code B. Adding over the box A detail entries gives the line 2 total that carries to line 1b."
  - key: "1b(g)"
    status: MATCH
    reason: "Column (g) adds the code B correction, figured as reported basis minus correct basis per the Worksheet for Basis Adjustments, and the code W nondeductible loss as a positive number. Other codes are refused."
  - key: "1b(h)"
    status: MATCH
    reason: "Column (h) is (d) less (e), combined with (g), summed over box A detail entries. This matches the Lines 1b–10 column (h) instructions."
  - key: "2(d)"
    status: MATCH
    reason: "Line 2 totals Form 8949 transactions with Box B checked (Box H is refused as digital). Column (d) sums the proceeds of box B entries."
  - key: "2(e)"
    status: MATCH
    reason: "For box B, basis was not reported, so column (e) is the correct basis. This follows 'enter the correct basis in column (e), and enter -0- in column (g)'."
  - key: "2(g)"
    status: MATCH
    reason: "The B correction applies only to covered boxes, so it is $0 for box B, and the W amount is added. This is consistent with the code B and code W instructions."
  - key: "2(h)"
    status: MATCH
    reason: "Column (h) is (d) less (e) plus (g), summed over box B entries."
  - key: "3(d)"
    status: MATCH
    reason: "Line 3 totals Form 8949 transactions with Box C checked (Box I is refused as digital). Column (d) is net proceeds when there is no report."
  - key: "3(e)"
    status: MATCH
    reason: "For box C, column (e) is the correct basis from records."
  - key: "3(g)"
    status: MATCH
    reason: "Code B on box C is refused, so column (g) holds only the W amount. Summing it matches the Form 8949 totals."
  - key: "3(h)"
    status: MATCH
    reason: "Column (h) is (d) less (e) plus (g), summed over box C entries."
  - key: "8a(d)"
    status: MATCH
    reason: "Line 8a is the long-term counterpart of line 1a. It sums the proceeds of box D aggregate-route sales, which are restricted to entries with reported basis and no adjustments."
  - key: "8a(e)"
    status: MATCH
    reason: "Column (e) is the reported basis for box D, which matches the line 8a example ($2,000 in column (e))."
  - key: "8a(g)"
    status: MATCH
    reason: "Aggregate entries carry no code, so column (g) is zero, consistent with 'no adjustments'."
  - key: "8a(h)"
    status: MATCH
    reason: "Column (h) is (d) less (e), matching the example '$4,000 ($6,000 − $2,000) in column (h)'."
  - key: "8b(d)"
    status: MATCH
    reason: "Line 8b totals Form 8949 transactions with Box D checked (Box J is refused). Column (d) sums the proceeds."
  - key: "8b(e)"
    status: MATCH
    reason: "For box D, column (e) is the reported basis, with any error corrected in column (g)."
  - key: "8b(g)"
    status: MATCH
    reason: "Column (g) adds the code B worksheet correction (reported minus correct basis) and the code W positive amount."
  - key: "8b(h)"
    status: MATCH
    reason: "Column (h) is (d) less (e) plus (g), summed over box D detail entries."
  - key: "9(d)"
    status: MATCH
    reason: "Line 9 totals Box E transactions (Box K is refused). Column (d) sums the proceeds."
  - key: "9(e)"
    status: MATCH
    reason: "For box E, column (e) is the correct basis, because basis was not reported to the IRS."
  - key: "9(g)"
    status: MATCH
    reason: "The B correction is $0 for a non-covered box, and the W amount is added, per the instructions."
  - key: "9(h)"
    status: MATCH
    reason: "Column (h) is (d) less (e) plus (g), summed over box E entries."
  - key: "10(d)"
    status: MATCH
    reason: "Line 10 totals Box F transactions (Box L is refused). Column (d) sums the proceeds."
  - key: "10(e)"
    status: MATCH
    reason: "For box F, column (e) is the correct basis from records."
  - key: "10(g)"
    status: MATCH
    reason: "Code B on box F is refused, so column (g) holds only the W amount, summed."
  - key: "10(h)"
    status: MATCH
    reason: "Column (h) is (d) less (e) plus (g), summed over box F entries."
  - key: "7"
    status: MATCH
    reason: "The form says 'Combine lines 1a through 6 in column (h)'. The restatement adds the column (h) amounts of lines 1a–3 with lines 4, 5 and 6, and line 6 is held as a negative loss."
  - key: "15"
    status: MATCH
    reason: "The form says 'Combine lines 8a through 14 in column (h)'. The restatement adds lines 8a(h)–10(h) and lines 11–14, and line 14 is held as a negative loss."
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
