# Review record e4c1d73514f8 — render s179

One pass of a review, stored once (tools/transcription/review_store.py); the form's index says which lines it still judges.

```json
{
 "family": "claude",
 "form": "s179",
 "kind": "render",
 "policies": {
  "prompt policy": "render-source-comparison-v2+lines-v1"
 },
 "prompt_sha256": "75c5152657ed2b92649fdc2263786fa0e0e9e075ba952c0776e4e3f313852b0e",
 "response_sha256": "9ff53488bb78fa3b71ecd7dec1553ffd9b77bef93a5d14dcbfefa2d9ab7a72f0",
 "scope": [
  "5",
  "10",
  "11",
  "12",
  "13"
 ],
 "subjects": {
  "10": "55993b78b468bea4e5729071f90d000928259b3c28339dc56108adf73303dd7a",
  "11": "006dfd9a75c081d3373160e6e3ae03a7463a4e912d5b076be7ee6c4a3433a540",
  "12": "5617d7e407cd68b021f19b4e4db6b591c532c8f7aedb2365053399b72c14f294",
  "13": "2960f60f54c65115d20937e71bdec835f1b0395073dcc75c2570e683d87e123c",
  "5": "8d9405dd84b012261aabcf0024d35f2b8f74f862c0cd13754f68d7e9851c173d"
 }
}
```

<!-- part block -->
#### Pass 75c5152657ed

| field | value |
| --- | --- |
| date | 2026-11-10 |
| review scope | lines 5, 10, 11, 12, 13 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 75c5152657ed2b92649fdc2263786fa0e0e9e075ba952c0776e4e3f313852b0e |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 596a4e0df067ae416506562fb6d1e6fc973b6a0f2dcb6e00b5e38e347f83e26e |
| receipt | .transcription/s179.render.lines-6a6b35d00667 |
| lines judged | 5 |
| match / mismatch / unclear / missing | 5 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f4562 | 2025; created 2025-10-09 | 1, 2, 3 | whole document | 71e2ace527072aaa7293e77897bb4ab8e473fa9c47b6b1ccb977fdc58a93bc2d | - | a1330c49d931e7ecdc867aef2d9e01390fc7b4d7e9321943a21ed0f8e883ed18 |
| i4562 | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 17, 18, 19, 31, 32, 33, 34, 37, 39, 41, 59, 61, 62, 63, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 18, 19, 31, 32, 33, 34, 37, 39, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |
| i1040sc | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| f7206 | 2025; created 2025-10-02 | 1 | whole document | 1f54af11e092a24258ac71f29d2bcfeeda1d6100ca332357d4569eea889e1dbb | - | e3b265efad583dd859c584d4e7e8a17d7b6e927878922ab5f020e2ff79a18d87 |
| i7206 | 2025 | 1, 2 | whole document | 88aebffe01e22b57dadeb703483459075718cb0b2514fe8f00185975cfbeef3a | 1, 2 | 5bfa308e7e4634d4a0162d76b4af6a4182b8539a390109360875303222231cfe |
| f1040sse | 2025; created 2025-05-07 | 1, 2 | whole document | d214b41a4e42da1953a1ee216b6f9d263be284a90cf9f7f28dcb87cd0e9913e6 | - | fbeaf5e9b8509f8fe754b52a6b5a643934ae2ff1a6f76e6e69af8be42fcd2cdd |
| i1040gi | 2025; printed date 2026-02-25 | 93, 94, 95, 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 93, 95, 117 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i1040sse | 2025 | 1, 2, 3, 4, 5 | whole document | bd4768e77e9087e707701447574c3fd8b1b6ac8deca77fcf2e1bce4c50b7db28 | 1, 2, 3, 4, 5 | 6cb68f929e214450ea7ffa33648d5602e2431f38e91c7a6c83dfbee0ab23f08c |
| iw2w3 | 2025; printed date 2025-02-19 | 18 | cited pages | 27ad850a44d58d9186afcccb33b8a32f4747911e2b1b3138de515f44d4de33f3 | 18 | 3876738db222e8abe6103f29d8a8654a3139b9896f97e325d50e80b87ed5b26a |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |
| p560 | For use in preparing 2025 returns | 7, 8, 9, 10, 11, 14, 15, 16, 17, 38, 39, 40 | cited pages | 38bbfa2efb2894e2527d66cd3478f33c6ceae4b777f78674c22bec16db9809aa | 7, 8, 9, 10, 11, 14, 15, 16, 17, 38, 40 | 7ef279c8f34addc2ff13420e35fab4a092bf8027f53907c28a5f46d2c21da737 |
| p463 | For use in preparing 2025 returns | 25, 26 | pages named by another document's citation | 153efad2a94bcccadf643b0f28f913d74b7d70b727f73eca540a2ce4d32bbfda | 25, 26 | a0b14576fdb49a7ba3e7a90092c1b8f6b8ba33889c8c35da5629156346581326 |
| p538 | None | 17 | pages named by another document's citation | 4186d7aaa8f711c9a524b87fac1e3df05640b6d66130093b2469480acb06ef6c | 17 | f500211df18a4aafd843e48bbad4b9102c598cf5ccc0fae96c7814a4bef0ae00 |

##### Raw response

```yaml
```yaml
lines:
  - key: "5"
    status: MATCH
    reason: "For other filers it is line 1 less line 4, floored at zero, as the form says. For married filing separately it is 50% of that limitation, the default allocation in the line 5 instructions. Any separate return with an election or a carryover is refused, so the joint-taxpayer limitation and other allocation percentages never reach a computed value."
  - key: "10"
    status: MATCH
    reason: "The line 10 instructions say to enter the amount from line 13 of your 2024 Form 4562, and define the carryover as cost elected in earlier years that the business income limit disallowed; the fallback to the last Form 4562 filed fits that definition. Leaving the line off when line 5 is zero follows the line 5 instruction to skip lines 6 through 11."
  - key: "11"
    status: MATCH
    reason: "The line is the smaller of line 5 or business income floored at zero, as printed. The income measure follows the Individuals instruction: active trade or business income figured without the section 179 deduction, the one-half SE tax deduction or an NOL, plus Form 1040 line 1a wages. Working-capital interest (Pub. 946) is added only when it could change the result, and the cases outside the tool are refused or screened."
  - key: "12"
    status: MATCH
    reason: "The form says 'Add lines 9 and 10, but don't enter more than line 11'; the smaller of (line 9 + line 10) or line 11 is the same."
  - key: "13"
    status: MATCH
    reason: "The form says 'Add lines 9 and 10, less line 12'; since line 12 never exceeds that sum, the zero floor changes nothing. When line 5 is zero this gives line 12 = 0 and line 13 = the prior carryover, matching the line 5 instruction. Carryovers with no Schedule C are refused."
```
```
<!-- part section 5 -->
5 — Dollar limitation for tax year. Subtract line 4 from line 1. If zero or less, enter -0- (i
Status: **MATCH**

Model: For other filers it is line 1 less line 4, floored at zero, as the form says. For married filing separately it is 50% of that limitation, the default allocation in the line 5 instructions. Any separate return with an election or a carryover is refused, so the joint-taxpayer limitation and other allocation percentages never reach a computed value.
Reviewed in: pass 75c5152657ed

<!-- part section 10 -->
10 — Carryover of disallowed deduction from line 13 of your 2024 Form 4562
Status: **MATCH**

Model: The line 10 instructions say to enter the amount from line 13 of your 2024 Form 4562, and define the carryover as cost elected in earlier years that the business income limit disallowed; the fallback to the last Form 4562 filed fits that definition. Leaving the line off when line 5 is zero follows the line 5 instruction to skip lines 6 through 11.
Reviewed in: pass 75c5152657ed

<!-- part section 11 -->
11 — Business income limitation. Enter the smaller of business income (not less than zero) or l
Status: **MATCH**

Model: The line is the smaller of line 5 or business income floored at zero, as printed. The income measure follows the Individuals instruction: active trade or business income figured without the section 179 deduction, the one-half SE tax deduction or an NOL, plus Form 1040 line 1a wages. Working-capital interest (Pub. 946) is added only when it could change the result, and the cases outside the tool are refused or screened.
Reviewed in: pass 75c5152657ed

<!-- part section 12 -->
12 — Section 179 expense deduction. Add lines 9 and 10, but don't enter more than line 11
Status: **MATCH**

Model: The form says 'Add lines 9 and 10, but don't enter more than line 11'; the smaller of (line 9 + line 10) or line 11 is the same.
Reviewed in: pass 75c5152657ed

<!-- part section 13 -->
13 — Carryover of disallowed deduction to 2026. Add lines 9 and 10, less line 12
Status: **MATCH**

Model: The form says 'Add lines 9 and 10, less line 12'; since line 12 never exceeds that sum, the zero floor changes nothing. When line 5 is zero this gives line 12 = 0 and line 13 = the prior carryover, matching the line 5 instruction. Carryovers with no Schedule C are refused.
Reviewed in: pass 75c5152657ed

<!-- end -->
