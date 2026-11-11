# Review record 734cb0eb8490 — render refund

One pass of a review, stored once (tools/transcription/review_store.py); the form's index says which lines it still judges.

```json
{
 "family": "claude",
 "form": "refund",
 "kind": "render",
 "policies": {
  "prompt policy": "render-source-comparison-v2+lines-v1"
 },
 "prompt_sha256": "ccae52fca6255754a650583c3782b90aa88a269adfa6dd9b5b1924a470e54a07",
 "response_sha256": "6d8adadfec4a8461374adb697302d5f5635dc6d5381321960b8b2c08f1914084",
 "scope": [
  "1"
 ],
 "subjects": {
  "1": "03f5c2c443202541add3fbdef3b12072118748cce5f84b44956e0d6701130b57"
 }
}
```

<!-- part block -->
#### Pass ccae52fca625

| field | value |
| --- | --- |
| date | 2026-11-10 |
| review scope | lines 1 |
| model requested | claude-fable-5-2 |
| model reported | claude-fable-5-2 |
| prompt sha256 | ccae52fca6255754a650583c3782b90aa88a269adfa6dd9b5b1924a470e54a07 |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | d0ed1d5155a0f96e681ba9f42408e93bbd5f4f3bf5549e3ce615bb9011321e94 |
| receipt | .transcription/refund.render.lines-6b86b273ff34 |
| lines judged | 1 |
| match / mismatch / unclear / missing | 1 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 88, 89, 90 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 88, 89 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| f1099g | Rev. March 2024 (continuous-use form for calendar year 2025; the December 2026 revision is first used for 2026) | 1, 2, 3, 4, 5, 6 | whole document | c3505294585e00ec5e957f73aa97dee32ad4b6916cd3eb48fef7f3c79f123270 | 5 | 49cc781de5cf6d881cc347361880de4b4b20fca0f13397bc94c94e84a20cff6d |
| p525 | 2025 | 24 | pages named by another document's citation | 7df495537860edb313c70301e591c2a0775567fab771e3d5f9bbb0cbccb69182 | 24 | 27f9e8c0836aae6360658725d1b0db69ecaf91bfa77998e1637b51f92b18df65 |

##### Raw response

```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "The worksheet says to enter the income tax refund from Form(s) 1099-G (or similar statement) but not more than the amount on 2024 Schedule A, line 5d, which is the smaller of the two helpers; the input's inclusion of amounts applied to 2025 estimated tax, offsets and refunds with no Form 1099-G agrees with the line 1 and box 2 instructions. The two refusals cover Exception items 3, 4, 6, 7, 8 and 9 and the nonresident alien case; items 1, 2 and 5 (refund for a year other than 2024, non-income-tax refund, last 2024 estimated payment made in 2025) are not named in the refusals shown for this line."
```
<!-- part section 1 -->
1 — Enter the income tax refund from Form(s) 1099-G (or similar statement). But don’t enter mo
Status: **MATCH**

Model: The worksheet says to enter the income tax refund from Form(s) 1099-G (or similar statement) but not more than the amount on 2024 Schedule A, line 5d, which is the smaller of the two helpers; the input's inclusion of amounts applied to 2025 estimated tax, offsets and refunds with no Form 1099-G agrees with the line 1 and box 2 instructions. The two refusals cover Exception items 3, 4, 6, 7, 8 and 9 and the nonresident alien case; items 1, 2 and 5 (refund for a year other than 2024, non-income-tax refund, last 2024 estimated payment made in 2025) are not named in the refusals shown for this line.
Reviewed in: pass ccae52fca625

<!-- end -->
