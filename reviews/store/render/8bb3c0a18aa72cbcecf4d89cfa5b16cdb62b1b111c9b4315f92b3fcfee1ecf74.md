# Review record 8bb3c0a18aa7 — render s3

One pass of a review, stored once (tools/transcription/review_store.py); the form's index says which lines it still judges.

```json
{
 "family": "claude",
 "form": "s3",
 "kind": "render",
 "policies": {
  "prompt policy": "render-source-comparison-v2+lines-v1"
 },
 "prompt_sha256": "2ff549802f98083ca8a620a94bcc076ab21417dc5725eafc773b9696c89ea32a",
 "response_sha256": "987e3e4558333e224d6faebb5747620b0c4f42596ec56c8ad69ef9ac144674ab",
 "scope": [
  "10",
  "15"
 ],
 "subjects": {
  "10": "aecbee88b43d622e6b0866d81c7655a1c544ff5c8552eb15bd3f94f525ce0dc1",
  "15": "79b72a9e70ad9ebaca9b3168b065e03b38fc3be79e5128869f5c8e5de12acd85"
 }
}
```

<!-- part block -->
#### Pass 2ff549802f98

| field | value |
| --- | --- |
| date | 2026-11-10 |
| review scope | lines 10, 15 |
| model requested | claude-fable-5-2 |
| model reported | claude-fable-5-2 |
| prompt sha256 | 2ff549802f98083ca8a620a94bcc076ab21417dc5725eafc773b9696c89ea32a |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | ed5d6ecf20fca2654e5c0a553855ee64cee0f4cca56e089ecec55ce022b4a22d |
| receipt | .transcription/s3.render.lines-1638632c2096 |
| lines judged | 2 |
| match / mismatch / unclear / missing | 2 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040s3 | 2025; created 2025-11-17 | 1 | whole document | 43c7ba36b506a538179465978807938c64bde632d7e1bff225bb6b13b19f37bd | - | 1ae44325c8d22211a6eadd11b393254317542704e5fed0fb419e41690210fc48 |
| i1040gi | 2025; printed date 2026-02-25 | 117 | pages named by another document's citation | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 117 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| f4868 | 2025; created 2025-10-01 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision) | 1, 2, 3, 4 | whole document | aaf7bc8b49cec44ea4681a20af7fe2ac5a53467f0dfe9840e48eae12bc7b1268 | 1, 2, 3 | 9c0ff5e0c719dcee49782077737610c6d8892e33871c8ae00f63cfaa796999ee |

##### Raw response

```yaml
lines:
  - key: "10"
    status: MATCH
    reason: "The instructions say to enter the payment made to get an automatic extension or any amount paid with Form 4868, exclude any fee charged, and include amounts paid with Form 2350; the restatement covers all of these, and counting a spouse's payment on a joint return agrees with the Form 4868 instructions."
  - key: "15"
    status: MATCH
    reason: "The form says 'Add lines 9 through 12 and 14', which is line 9 + line 10 + line 11 + line 12 + line 14, as restated."
```
<!-- part section 10 -->
10 — Amount paid with request for extension to file (see instructions)
Status: **MATCH**

Model: The instructions say to enter the payment made to get an automatic extension or any amount paid with Form 4868, exclude any fee charged, and include amounts paid with Form 2350; the restatement covers all of these, and counting a spouse's payment on a joint return agrees with the Form 4868 instructions.
Reviewed in: pass 2ff549802f98

<!-- part section 15 -->
15 — Add lines 9 through 12 and 14. Enter here and on Form 1040, line 31
Status: **MATCH**

Model: The form says 'Add lines 9 through 12 and 14', which is line 9 + line 10 + line 11 + line 12 + line 14, as restated.
Reviewed in: pass 2ff549802f98

<!-- end -->
