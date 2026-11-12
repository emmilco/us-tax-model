# Review record 1fa5aab7c28f — render s3

One pass of a review, stored once (tools/transcription/review_store.py); the form's index says which lines it still judges.

```json
{
 "family": "claude",
 "form": "s3",
 "kind": "render",
 "policies": {
  "prompt policy": "render-source-comparison-v2+lines-v1"
 },
 "prompt_sha256": "02e928e7c372d9cd2b2412105d1455c4d263bf6b7343a0de5d616f755f71b9da",
 "response_sha256": "8d0ee1f471193b6b6e6869aa8a90746da8b625a5d4a9c8e443c0cff54f092108",
 "scope": [
  "7",
  "12"
 ],
 "subjects": {
  "12": "a68485d052614fadd19f42abf42c0f99a0746f113994c8671d50c4e7c0fc82a9",
  "7": "b61804707d63709d3911680f1bae8f0b696624a0f10750207c90e8b168af0f56"
 }
}
```

<!-- part block -->
#### Pass 02e928e7c372

| field | value |
| --- | --- |
| date | 2026-11-12 |
| review scope | lines 7, 12 |
| model requested | claude-fable-5-2 |
| model reported | claude-fable-5-2 |
| prompt sha256 | 02e928e7c372d9cd2b2412105d1455c4d263bf6b7343a0de5d616f755f71b9da |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 49481f05ed1f8f5dc978d8063ca3373c63631f5bb4a1e6274fe11da61d206e8a |
| receipt | .transcription/s3.render.lines-fb9058ebc189 |
| lines judged | 2 |
| match / mismatch / unclear / missing | 0 / 2 / 0 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 116, 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 117 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i8839 | 2025 | 1, 3 | cited pages | aba1b0860ba08ea9e0953f31580e22421bdb92427957682acc3d79b98cb43626 | 1, 3 | ba3ee91ddad989767d0c8aa84b7b53b7a4a1161c0d0731cbb8eb275febf19d8b |
| i8912 | December 2024 (continuous-use revision, the current one on irs.gov/pub/irs-pdf when fetched, so in force for 2025) | 1, 2, 3, 4, 5 | whole document | e23ca6f7fb979757f2f3590fdf4823eba19cc909f724b0d91a61ce02f0300c40 | 1, 2, 3, 4, 5 | e9178b04d7fc4e89ac00e77cea2a660b26eeb1c552cd4580a72a79b189f99f1b |
| i1040sr | 2025 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision) | 1, 3 | cited pages | 8e01e7e4db0054efbeac87d4246ad14425e599b9e93a4d73ba6eda964726880c | 1, 3 | 9b45d1c5b76440d18a3d1118b274368669e683ced562a0d8b208e92b856a84db |
| i8936 | 2025 | 1, 2, 7 | cited pages | c29fb417b3f05e5067c6261e0eecf14e6dc2bb5d099b0179395b9e12bf9f0b0d | 1, 2, 7 | 754e3102c5109789dd39499aed7275f3323010ad0736619519d4d96b98c18930 |
| i8911 | December 2025 (for tax years beginning in 2025 or later) | 1, 2, 3, 4, 5 | whole document | 9258095d5fbe83d1a67ef6ed338f5d0a706823c1b84475f53160171b49e02c29 | 1, 2, 3, 4 | 6afc575ca0eeb12440668d8f8df07b23ab9250cf7b9058fc4e9a52294581aea6 |
| i4136 | 2025 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision) | 2 | cited pages | f2338a673161989fd24a575b29bd75077fda30429f135592b78c03b3bbdbf571 | 2 | 031aac61c09cba6aadf939df9388eb5665127f2fde52f4b9a2a1bde53ed84ab5 |
| f8396 | 2025; created 2025-08-28 | 1, 2 | whole document | 7d27fdfd3ca9b205d00b68cff4f6261540d0ccc556b13edf05ccb0dd11885ec9 | 2 | 71ea89f5ee5d170488cc56526b409eb38c10d65ce5abe72dcaee21064281eca9 |
| i8801 | 2025 | 1, 2, 3, 4, 5 | whole document | 0b107826c9e29d2b284a4aba175837438fd8d8e3f405b214909ddf3d39ed0656 | 1, 3, 4, 5 | 5505010794a0984c4345b545b2602b3bbc71348cde05091aa76e1a4c99bc6ddb |
| i3800 | 2025 | 3 | cited pages | 8f87d7d4652fdd97673c64cf436c3edfb4d31155a90efcb4a11d06a014bfe12d | 3 | f14b444e5dcde07304dc6f5f8c9309bacf8c621eca24a4d9093f9732c39d2b9f |
| f1040s3 | 2025; created 2025-11-17 | 1 | whole document | 43c7ba36b506a538179465978807938c64bde632d7e1bff225bb6b13b19f37bd | - | 1ae44325c8d22211a6eadd11b393254317542704e5fed0fb419e41690210fc48 |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i8978 | December 2024 (continuous-use revision, the current one on irs.gov/pub/irs-pdf when fetched, so in force for 2025) | 1, 2, 3, 4, 5, 6 | whole document | a9456f3e1bc501835fd77546b222244be22efac4296249f07d42496903c03c28 | 1, 2, 3, 4, 5, 6 | a3edf1c9e8fe76a4a57b31f0d779677a41df7558277ee3b62c5947a60e9aa8d5 |
| f8801 | 2025; created 2025-11-12 | 1, 2, 3, 4 | whole document | 8d6a9d2d7388958b1ef192d4ea86f72742b249ea7361494bbd6c100c52d0dbbd | - | 1a2853e41754fc296460caa33ce7d5afcd0a2c76f3794b66cdec9e1c3f20655c |
| f8834 | October 2024 (continuous-use revision, the current one on irs.gov/pub/irs-pdf when fetched, so in force for 2025) | 1, 2 | whole document | 294996953deaa0a29ce39ade08a10ab5de5d41a0eb955117b2543a94b17a0e41 | 2 | 15f21877e903e0b003bcb978d98712c7e8913bed71ae5e453700cb8150b9b4d1 |
| f8859 | 2025; created 2025-08-07 | 1 | whole document | 718b7d6bc801be84b557f42af42a44cc2dcdbce3ce93d169c0589b2266fb7295 | - | 648bf239b24daf08f051b1da3808a13b9c78d05e7c47d71665cf8a28219e7d8c |

##### Raw response

```yaml
lines:
  - key: "7"
    status: MISMATCH
    reason: "The IRS line is \"Total other nonrefundable credits. Add lines 6a through 6z\", and 6a is \"General business credit. Attach Form 3800\" (credits that \"usually apply only to individuals who are partners, shareholders in an S corporation, self-employed, or who have rental property\"). The refusals cover 6b through 6m and carryovers shown by a 2024 Form 3800, but nothing refuses a current-year general business credit, so such a filer gets $0 with no refusal."
  - key: "12"
    status: MISMATCH
    reason: "The IRS line is \"Enter any credit for federal excise taxes paid on fuels that are ultimately used for a nontaxable purpose (for example, an off-highway business use). Attach Form 4136.\" The only refusal is for undyed kerosene used in the home, so a filer with a business fuel-tax credit gets $0 with no refusal."
```
<!-- part section 7 -->
7 — Total other nonrefundable credits. Add lines 6a through 6z
Status: **MISMATCH**

Restated: Enter $0 (sales.zero).

Model: The IRS line is "Total other nonrefundable credits. Add lines 6a through 6z", and 6a is "General business credit. Attach Form 3800" (credits that "usually apply only to individuals who are partners, shareholders in an S corporation, self-employed, or who have rental property"). The refusals cover 6b through 6m and carryovers shown by a 2024 Form 3800, but nothing refuses a current-year general business credit, so such a filer gets $0 with no refusal.

Ruling: open
Reviewed in: pass 02e928e7c372

<!-- part section 12 -->
12 — Credit for federal tax on fuels. Attach Form 4136
Status: **MISMATCH**

Restated: Enter $0 (sales.zero).

Model: The IRS line is "Enter any credit for federal excise taxes paid on fuels that are ultimately used for a nontaxable purpose (for example, an off-highway business use). Attach Form 4136." The only refusal is for undyed kerosene used in the home, so a filer with a business fuel-tax credit gets $0 with no refusal.

Ruling: open
Reviewed in: pass 02e928e7c372

<!-- end -->
