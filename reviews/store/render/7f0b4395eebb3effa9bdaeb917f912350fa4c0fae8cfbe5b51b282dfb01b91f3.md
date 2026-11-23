# Review record 7f0b4395eebb — render f8960

One pass of a review, stored once (tools/transcription/review_store.py); the form's index says which lines it still judges.

```json
{
 "family": "claude",
 "form": "f8960",
 "kind": "render",
 "policies": {
  "prompt policy": "render-source-comparison-v2+lines-v1"
 },
 "prompt_sha256": "6c7e46c439c8d5eb1930697bb16aca112fdc4fa458d5647fe38a6c6d87b7967b",
 "response_sha256": "6ba27639247ff72a8ba6cf3e9a03005f536083d1b1d792e1aa0d18edbf3dc3ab",
 "scope": [
  "1",
  "8",
  "16",
  "17"
 ],
 "subjects": {
  "1": "a5fa3c90ac56ab3d7a6530f05ebe41c9065dcf0efe947bbdecdb33d9c275ba04",
  "16": "d8af20ddda4fc27e52bcda9847d4ce615b8a412a064e4495c984138582c8b594",
  "17": "250c6a17e93a5ba79a075b15447d528cd8b5dc42574df4d7d05a4d02e9965c0b",
  "8": "910f2a04592546636d0ebe479ed4ffb95e856b42d13c85f81e351cfba072d6fa"
 }
}
```

<!-- part block -->
#### Pass 6c7e46c439c8

| field | value |
| --- | --- |
| date | 2026-11-22 |
| review scope | lines 1, 8, 16, 17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 6c7e46c439c8d5eb1930697bb16aca112fdc4fa458d5647fe38a6c6d87b7967b |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 19d60179a5f082b2145743f28d657428a05e31c35cc44fcd84243f6af38e8519 |
| receipt | .transcription/f8960.render.lines-b1acfe7eb87f |
| lines judged | 4 |
| match / mismatch / unclear / missing | 4 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f8960 | 2025; created 2025-08-19 | 1 | whole document | 76d992342a282067460ae60eaf8bda63925b514b721a6e8763f1174abedb59e9 | - | 35521c3ad7dfcd341a9de35529db4ea02c74bde6b9659da0d9388cfa46f9e4cb |
| i8960 | 2025; printed date 2026-02-04 | 1, 2, 3, 7, 9, 13, 14, 15, 17, 18, 22 | cited pages | fcae098ebc1ad79343de101a66765d3b3597f664dc744de3a7588be123c900a1 | 1, 2, 3, 7, 9, 13, 17, 18 | d6dc1f475c511790abb02d6d6cfff554a59b40c0da1c56eb2f26af4e3cb7fa51 |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040sca | 2025; printed date 2025-12-08 | 7 | cited pages | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | - | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
| i1099div | January 2024 (continuous-use instructions) | 1, 2, 3, 4, 5 | whole document | c0f334a4f8c8032dfce868bbfad5bf4cba1d48c9f2226d42d736b69ae784bcf3 | 1, 2, 3, 4, 5 | d9599f4871f4d473ff9c582e205b5e9385bd865210e9c2af4c4aede3a33af4f3 |
| i1040gi | 2025; printed date 2026-02-25 | 90 | pages named by another document's citation | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

##### Raw response

```yaml
```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "The Line 1 instructions say to enter taxable interest from \"Form 1040 or 1040-SR, line 2b\". The refusals exclude the line 7 adjustments to interest (such as self-charged interest), deduction recoveries, and the section 6013(g)/(h) election checkbox, all of which this slice does not support."
  - key: "8"
    status: MATCH
    reason: "The form says \"Total investment income. Combine lines 1, 2, 3, 4c, 5d, 6, and 7\". The restatement adds exactly these lines."
  - key: "16"
    status: MATCH
    reason: "The form says \"Enter the smaller of line 12 or line 15\". When Form 8960 is not filed, MAGI is not over the threshold, so line 15 is 0 and the smaller amount is also 0. MAGI equals AGI only when there is no section 911 exclusion or CFC/PFIC holding (\"your MAGI is your AGI as reported on Form 1040\"), and the unsupported refusal excludes those cases."
  - key: "17"
    status: MATCH
    reason: "The form says \"Multiply line 16 by 3.8% (0.038)\". 38/1000 equals 0.038."
```
```
<!-- part section 1 -->
1 — Taxable interest (Form 1040 line 2b)
Status: **MATCH**

Model: The Line 1 instructions say to enter taxable interest from "Form 1040 or 1040-SR, line 2b". The refusals exclude the line 7 adjustments to interest (such as self-charged interest), deduction recoveries, and the section 6013(g)/(h) election checkbox, all of which this slice does not support.
Reviewed in: pass 6c7e46c439c8

<!-- part section 8 -->
8 — Add f8960.line1, f8960.line2, f8960.line3, f8960.line4c, f8960.line5d, f8960.line6, f8960.
Status: **MATCH**

Model: The form says "Total investment income. Combine lines 1, 2, 3, 4c, 5d, 6, and 7". The restatement adds exactly these lines.
Reviewed in: pass 6c7e46c439c8

<!-- part section 16 -->
16 — Smaller of f8960.line12, f8960.line15 (zero when modified AGI is not more than the thresho
Status: **MATCH**

Model: The form says "Enter the smaller of line 12 or line 15". When Form 8960 is not filed, MAGI is not over the threshold, so line 15 is 0 and the smaller amount is also 0. MAGI equals AGI only when there is no section 911 exclusion or CFC/PFIC holding ("your MAGI is your AGI as reported on Form 1040"), and the unsupported refusal excludes those cases.
Reviewed in: pass 6c7e46c439c8

<!-- part section 17 -->
17 — Multiply f8960.line16 by niit.rate
Status: **MATCH**

Model: The form says "Multiply line 16 by 3.8% (0.038)". 38/1000 equals 0.038.
Reviewed in: pass 6c7e46c439c8

<!-- end -->
