# Review record f90804ebdc2a — render f1116

One pass of a review, stored once (tools/transcription/review_store.py); the form's index says which lines it still judges.

```json
{
 "family": "claude",
 "form": "f1116",
 "kind": "render",
 "policies": {
  "prompt policy": "render-source-comparison-v2"
 },
 "prompt_sha256": "d6d0f6a78cda678e1f17a249a182ac2355736d1306e383db71b908707d0b6de2",
 "response_sha256": "c3ed6bf4dd4bff754f614cca62a977cdf2282e4a75794e171dc77c36840fe14f",
 "scope": "whole",
 "subjects": {
  "10": "96a20e0910ce78f24a9ddaa89700eee655ccf9cc41dd35330bff543bbf8763c5",
  "11": "154910564a314794ff36a829db5dbb3a058f7977856d317be0ccf249726689ac",
  "12": "3a10eca8346afb814f3946076371bd1e5bdaadc6375061cd878c6477d65aa583",
  "13": "f68d85cb5bfb36855069f1844ed668afe59952db504a3bb3ddfe02510f5a9605",
  "14": "8b4c55742e140affcb500c27522e0080e86ecc92d518a5dc219a3132c16cee56",
  "15": "803ad6362dda484e7d168f87bc97e6f3f881b0af5cdc2770c60a05869fb1408e",
  "16": "a6d271ebb1c54734560796d9279c73b02a9f317091036ab0273674a9ec5ee561",
  "17": "7343ff7daff916dfba0760b6542c31d7ba5be3c27f5c1db64ecb15fe227afef2",
  "18": "b9827db39a1073e61f64730982496cd3324f1cee4d46ed6f8729c90aeaddcbd8",
  "1a (Total)": "787d3ef70c4b3360d3d9e37b204098c19c804464f1a259cfecb34864d7ae2414",
  "20": "a8f5ed3d8d6158812eb44af57deba260b67a4e7ed7e05ff954e4131fa5adc3ed",
  "21": "1082557603fc4e0e9b407dddd483877e1efae90bda6533612ccc36186cb78a36",
  "22": "29b071b72f1693cde96814f9a203a4db7d2f52439a4edd4797dabf3b86e246c7",
  "23": "792057c7f7fd8e5837ed5b97e383dce4c74fcef4a43b4302c2270628817c5429",
  "24": "9ee95c0edd5404e59c200449574ff0765f06f9a1f07959175c47b5cbc2aa3d57",
  "27": "6362171d32364907b29fa0cf8b07296138348afcf2669e257791fe69e3a4fee7",
  "32": "8fd6f9617560c60453c4f2ae3567dfb8cead89a73e29fbe7276904ad06a20d88",
  "33": "2d12ac9256fc8b550ae5b7cb8d305c074bad5a7194b788f01b8305269ba7f044",
  "34": "ce049cb74fe83b6a84641a2159aa6a4d97020d330bade12e1afdbbc7083b5933",
  "35": "371e300e3e099f07127f038da892772c72ecd68b77d2defc1e265c99fcfe2e7c",
  "3a": "991444101f6403433342c77fc906791e5ab978ddfd22aba448a8f6f0f75d81f2",
  "3b": "e8ff1d8b1eabaf38059f85c7e35d72d6b2ffabfa84c96b749e5755ded0694517",
  "3c": "cb236962df847702979b13c92cfd448f0bada2d3dc5996218907e336d4045e8a",
  "3e": "0832510460471f5291a589d452b460095d0b999af6d0261fef05d6f3d277d0b9",
  "6 (Total)": "73c478d2e89a0619bf90646dd0c7d90b8e12ac238d55750371637498036db1e3",
  "7 (Total)": "35c04fee3549f39461d015f5e2e0019741ab39b79739d30e1438b0dc8232202a",
  "8": "1a8c83109393a5561e4de251867619bd11cc70f82c377eb2e5d3422188a3f79c",
  "9": "4d4fe61dbdec2457cb622a1e8522e580783c8ef34c56c82d8dc7df3db305a5c5"
 }
}
```

<!-- part head -->
# Render comparison — f1116

The rendered English of every printed line of `Form 1116 — Foreign Tax Credit (passive category, one form)` (`rendered/2025/f1116.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-15 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | d6d0f6a78cda678e1f17a249a182ac2355736d1306e383db71b908707d0b6de2 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 902ed458417a7c79b988adfe4a72f5107a50a3f6f66a3164ec429de27913a6ce |
| lines judged | 28 |
| match / mismatch / unclear / missing | 26 / 0 / 2 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1116 | 2025; created 2025-09-16 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision) | 1, 2 | whole document | 35fb2ea431123e1b99d31ebffd382e3452d1d1c9a2ca56f5c1e658cf2d2c4e20 | - | 47a5c4ac2284a31b7c1c9d473905bf2e1d6ac3e68875543a6e19bc9224861b76 |
| i1116 | 2025; printed date 2025-12-23 | 1, 2, 3, 9, 11, 17, 18, 19, 20, 21, 23, 24, 25 | cited pages | ca3e843c3bead1e7991566852707530b6bb7c2fd6008c1dbda0ac0bbd40c48ff | 1, 2, 3, 9, 11, 17, 19, 20, 21, 24, 25 | 4e9025bfc8a73bcfd687c7f45cb1a037cd39e7445319bbc71c748e12db68a46a |
| p514 | 2025 (Publication 514 (2025), Catalog Number 15018A, Jan 30, 2026) | 27, 37, 38, 39 | cited pages | db756c91fb3988617c583cbb077c6390dd7e235736f6df0ab2b2a63568f934ba | 27, 37, 38, 39 | 8ba7d10e464cb1323987bc176a435020718ff8bc7d1b9407fdc32f24a86c6e6a |
| cfr-26-1-904-4 | 26 CFR Ch. I (4-1-25 Edition), section 1.904-4 (GovInfo, GPO) | 3, 4 | cited pages | 8e53df6404606a73b955b1d3af6a8e427db995546f51466975de1020d5557850 | 3, 4 | cb3ffa1c80dfe882de47403ff42d30e2a32a63039fe0a990cee47f4061163b26 |
| i1116sb | Rev. December 2022 (printed 'Instructions for Schedule B (Form 1116) (Rev. 12-2022)', Dec 29, 2022); current irs-pdf edition, not year-specific; the IRS had posted no 2025 edition | 1, 2, 3, 4 | whole document | 90f1313e93bf416f2ee96a62d18d70f06016968268aca1055653869475205766 | 1, 2, 3 | 4f7920df06efd2f3f67a5f5f7b3a83f7307e81fb9342cd91461ba433b47486fd |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040gi | 2025; printed date 2026-02-25 | 8, 13, 14, 15, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 41, 43, 66, 80, 91, 92, 93, 95, 99, 100, 115, 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 8, 13, 14, 15, 23, 24, 25, 26, 27, 28, 30, 31, 33, 34, 36, 39, 41, 43, 66, 91, 92, 93, 95, 100, 115, 117 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i1040sca | 2025; printed date 2025-12-08 | 1, 2, 3, 6, 7, 8, 9, 10, 11, 12 | cited pages | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | 1, 2, 3, 6, 8, 9, 10, 11, 12 | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
| i8949 | 2025; printed date 2026-01-20 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 | cited pages | d3ddc2b91cf89087ca348ebb00dbd1c80bbc025fa4df1176753d25013f581a67 | 2, 3, 4, 5, 6, 7, 9, 10 | cabdc81a0677c0e4de4a89f9a71d328395c4cc839206ebadb56aeb54bf954b85 |
| f1040s1 | 2025; created 2025-07-25 | 1, 2 | whole document | 30004f72691a7078d8720e432e83110aa2bc3852ce9b45867becdb8c28222956 | - | 2293cadd525c2df84256455db693bbd46b710c62d28a98d503b1a6f8d8aea444 |
| i8801 | 2025 | 1, 2, 3, 4, 5 | whole document | 0b107826c9e29d2b284a4aba175837438fd8d8e3f405b214909ddf3d39ed0656 | 1, 3, 4, 5 | 5505010794a0984c4345b545b2602b3bbc71348cde05091aa76e1a4c99bc6ddb |
| i1040sd | 2025; printed date 2025-12-11 | 1, 4, 5, 6, 8, 10, 11, 12, 15 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 1, 4, 5, 6, 8, 11, 12 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| i1040sc | 2025 | 3, 14 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 3, 14 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1099div | January 2024 (continuous-use form) | 1, 2, 3, 4, 5, 6 | whole document | 833d93e5f2d0bfcc8c9d720c0e8cb8e623cd2c6a8ee25f364f1f69f49fa490e3 | 5 | 617419bd079b1520174ceca8549065c9e4001f2b06a16d1425c5469bbe49fa3d |
| i1040sb | TY2025; printed April 23, 2025 | 1, 2, 3 | whole document | 2bf62267574473b36fd9a69b6e0837ef74d72ac7d5dcbf1d26e7047d099f1e05 | 1, 2, 3 | 0d38b25d416cb650ef264faf8c1f118dfa4666f3949fbba7120f8c04d4e6914e |
| f1040sd | 2025; created 2025-10-06 | 1, 2 | whole document | 221151530f7cd599e8ad00bc3e1ba62d6b7ff34e402c336f4ae58d698c9f5187 | - | eb461181b39879c79d1c0b7761ca0cd9ade46fdb1531cdee3281053c348f6c41 |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| f4952 | 2025; created 2025-05-28 | 1, 2, 3, 4 | whole document | efbeec4c44a1e43fb00231942c811a454d86b3632a2a662238893f8c4595bf81 | 3, 4 | c98eb27a83a89faecfdd0cd6597e8063fbd86a14ba1606f3e96c1c5f016d2b5c |
| i8283 | December 2025; printed date 2026-01-30 | 1, 2, 3, 9, 12 | cited pages | cd582a9f231564c755d552a21d937b33e24df8b9fe65f4f823b7c9eca9dfe1ad | 1, 2, 3, 9, 12 | 53a4b54ff613d5c600c1af7ba5bf9024418fe89441ae8d629a955bd59aa6e3c7 |
| f8949 | 2025; created 2025-05-05 | 1, 2 | whole document | f191f96ca2847b4c59875d5e1169f784a79b4d57f1f12d0196bd9bc2e7838e9d | - | cc308c3ff7751456647bed9c2855d077dcbd0a55469b57f9e8cccb6f4927f232 |
| f8995 | 2025; created 2025-09-12 | 1 | whole document | 49922587df3bd093e24470f5b42d0e3382ef8f5210b3cedccb02ccb864f2f65a | - | 8e2e78d7610e1d45e93c10c8b03f9026d46a1166678c6ed93f852569c382f346 |
| p501 | 2025 returns; PDF created 2026-02-04 | 6, 8, 9, 11 | cited pages | 6aca9108a08fb6d4725c630023df5e17084d92135c6607cd7c536e8e0c67f19b | 6, 8, 11 | 2e0a281a7d3f73f1334d5f59a39a9fe4c393fd10dd6e6c6b1b8639c5ef038671 |
| f8995a | 2025; created 2025-09-12 | 1, 2 | whole document | 240927847d55e46348a41276d2bb81438c6fecae38b8106523444e56688c95b1 | - | c6abd31f2fb127536ba771d57a44e1487beebf502d934a3ebb8614e0508370d4 |
| i8995a | 2025; printed date 2026-01-26 | 1 | cited pages | 83411868381d4f5edbb455d348b480a63d96586bcb4f821f67acc0e027d5401d | 1 | 1843d02e5f17b6a3f1ba9d1ab3304a5c0b6862916c5ff0e622e3ccb411a89af3 |
| p525 | 2025 | 24, 33 | cited pages | 7df495537860edb313c70301e591c2a0775567fab771e3d5f9bbb0cbccb69182 | 24, 33 | 27f9e8c0836aae6360658725d1b0db69ecaf91bfa77998e1637b51f92b18df65 |
| i8995-correction | Post-release correction to the 2025 Instructions for Form 8995 (published 2026-02-13); page last reviewed 2026-06-28 | 1 | whole document | 879132e6955e44a171e1d163d25d817e0c1a0d004bb9ab14b79e424dd3ab75eb | - | - |
| i8995 | 2025; printed date 2026-01-26 | 1, 3, 4, 5 | cited pages | 96284eaad2fe5ec324de9fd4335cea9ea3260e66ff1d8b1725c1cff7fbe1ddc2 | 1, 3, 4, 5 | 6671a64ba0011f89e03eb5985954073dcd984b3f346495182916b0ecaa42ec1a |
| f2441 | 2025; created 2025-03-18 | 1, 2 | whole document | f39ca34d11c156e1ac55f4e2b5f16ef03c919773245cd7e50836e4c1555339c7 | - | 0e24fa891992674b84736c78565752c4a7d6f411fca4e24e5bb1307f239f60d6 |
| i5329 | 2025 | 3, 5 | cited pages | bc85a048e4293ab244d68023ac7bb45333ceede0763b3b1cb3430eb4829a18bf | 3, 5 | e46adbf118d780a00b73957b6ef4c6e436e651f6f076a36fa9b6717bd138ee5d |
| iw2w3 | 2025; printed date 2025-02-19 | 17 | cited pages | 27ad850a44d58d9186afcccb33b8a32f4747911e2b1b3138de515f44d4de33f3 | 17 | 3876738db222e8abe6103f29d8a8654a3139b9896f97e325d50e80b87ed5b26a |
| i8839 | 2025 | 1, 3 | cited pages | aba1b0860ba08ea9e0953f31580e22421bdb92427957682acc3d79b98cb43626 | 1, 3 | ba3ee91ddad989767d0c8aa84b7b53b7a4a1161c0d0731cbb8eb275febf19d8b |
| f1040s8812 | 2025; created 2025-07-30 | 1, 2 | whole document | 9b38295071c42fe489ec8f93e117b31eda11355b5a95e3fe388eeee69601c8c9 | - | 3525d47f51cb713591081610a862cae77eff08a8aa7e2064a96b15cee4fd5cb9 |
| f1099r | 2025 (calendar-year form) | 5, 7, 9 | cited pages | 97b0b54ae7c95303418077d54e349c0106cbbd5c4b5695ef684c23c39a5fda3f | 5, 7, 9 | af300d066f4492afc97aa90824bfc681581f64482976e6d6a705e7e94b0e4e67 |
| f8859 | 2025; created 2025-08-07 | 1 | whole document | 718b7d6bc801be84b557f42af42a44cc2dcdbce3ce93d169c0589b2266fb7295 | - | 648bf239b24daf08f051b1da3808a13b9c78d05e7c47d71665cf8a28219e7d8c |
| p502 | None | 12 | pages named by another document's citation | a85451b60db3f8c4d2be78bf08975f2ba8bd5c56093a86b24e5ae4ed5051d40b | 12 | 71bbda10a232ac104b7a59173c2901b409cd010f035f28e9bb615cab6db21c08 |
| i8962 | 2025 | 2 | pages named by another document's citation | 6b2be38425bc1a8b3073bfec01f18b7042e21187f37eec114ba185878be59976 | 2 | 11c5be397953d0f6bf8303148ac17e51c68c3cfed87cf2dc2de8a4173be5f309 |
| p969 | 2025 | 9, 13 | pages named by another document's citation | 0491c6445304fc8c1b7ae3097b8a3ea30260bb35f706da40900d06416502b9c8 | 9, 13 | f643ce7086d88eabd1d8006ab0b5609f775af36b9b8a5b74637e1f366d8c29c3 |
| p550 | 2025 returns; printed date 2026-03-05 | 59, 60, 61, 79, 81, 82, 86, 87, 88, 102 | pages named by another document's citation | e40622e028486d7eb31a6da342ba2ba3c8b2f7ea9d341d9f47a1d33407d5aa26 | 59, 60, 61, 79, 81, 82, 86, 87, 88 | 7629580e9cb35aa5f67e5d7c035b45850164eb1fe458f8acaa2781578ad0bf51 |
| i4562 | 2025 | 4 | pages named by another document's citation | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | - | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| f8283 | December 2025; created 2025-07-01 | 1, 2 | whole document | d33f4c2762c7366b560ae700f7c403b698b6567187a94eb4f7943b3ab6c20219 | - | 2a4ef5ee41c489f0de7f68915540d45a11937f39759f0c9ffb0f326461ee9320 |
| f1099b | 2025 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision) | 7 | pages named by another document's citation | 8e4cb19e9c4de2a62859d2c7840e85dc7053439f918cc0ef20480899ca583479 | 7 | 625fd05188d42f69a6af9c44b376cce3ee376487d9431a878c8f96a4368d7535 |
| fw2 | 2025 | 4 | pages named by another document's citation | 9729489962b46c0b21379fdfc29f3eb6f4be0e7c60594bdeb73a7ac72d5f509a | - | 2340d3c27b805bd389bfc5b9234ffa4c5e42c590b2fef8c77cb354fd686509fc |
| i1040se | 2025 | 1 | pages named by another document's citation | 3dc51debb6cc8744c7e7f3296b8d6e1d9e8aad4538aac12f85ad0f532defe705 | 1 | 26a1350f359a7001f1bfdcd3e9d5f4c6721f46208e81d8645149bc972cf9e78a |
| i1040sf | 2025 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision) | 2 | pages named by another document's citation | 7884d1d819e0129df3bac4773d92a7d888350042d03d71b4d3a842effec3e1d3 | 2 | 378b66baf8311c4034d58d8ed12cb658fa23643a06927a21b23ae9d8cca640b9 |
| i1040sse | 2025 | 1, 2, 3, 4, 5 | whole document | bd4768e77e9087e707701447574c3fd8b1b6ac8deca77fcf2e1bce4c50b7db28 | 1, 2, 3, 4, 5 | 6cb68f929e214450ea7ffa33648d5602e2431f38e91c7a6c83dfbee0ab23f08c |
| i8889 | 2025 | 4 | pages named by another document's citation | bfbdc8bbe0b85d088325243f176d4c8261b0ca2428f75f4f41e4a339ecb5495c | 4 | 533a42f870f12dc6c1984815eae1a4bf59d6fde28cbc909d9a4e76ff41c6eda7 |
| i2441 | 2025 | 1, 5 | pages named by another document's citation | 361baee739cc7cb7b6a84c7412397cfba901c1a3e5f225a8077cb8716917887e | 1, 5 | 3046d96b0769e20213f700deb20a0de9edc6a4572eda61bd70f5c8c88bc912ee |
| i8915f | December 2025 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision) | 2 | pages named by another document's citation | 7e822c561025dd03ee9850e3a0a0e2d0380ba5afb0ad7f3fa57c0804cf059eb9 | 2 | a4d999efa40ff6fdf2eb5565d40d061b4c9a775f8752dd8991d3725c06d011c9 |
| i8582 | 2025 | 1 | pages named by another document's citation | c7d05b8f9f05eaa0ede717f07f8e844ff7cec74c2bd71a79c6ecd032ec8cecaa | 1 | 7c2f83d446387ce35258f4a1c181512fd7816100a62441658fb48844f4fb516f |
| p575 | None | 12, 16, 21, 23, 24, 34 | pages named by another document's citation | 4d6ee3802a2906a4633dcfc104aa33bb3d9ddedebddc9eadbd0393cfdb61e07b | 12, 16, 21, 23, 24, 34 | 3962801dde168fda9f4ee239245d9746b12e2d60bf358b25186ae4a57aa5b837 |
| p590b | 2025 | 5, 6, 28 | pages named by another document's citation | 24de404e77c2a3d1f0540b91ac8c28ca4d45c7fcf968de613407419eba9266f4 | 5, 6, 28 | 464639ba13341fe9c824b6f495922126cb3d158650887bf9beb265fd951c3e77 |
| p560 | For use in preparing 2025 returns | 18 | pages named by another document's citation | 38bbfa2efb2894e2527d66cd3478f33c6ceae4b777f78674c22bec16db9809aa | 18 | 7ef279c8f34addc2ff13420e35fab4a092bf8027f53907c28a5f46d2c21da737 |

<!-- part section 1a (Total) -->
1a (Total) — Gross income from sources within country shown above and of the type checked above (Total,
Status: **MATCH**

Model: Each column's line 1a is its foreign-source dividends plus interest, and the total adds the columns. The f1116.adjust refusal covers the qualified-dividend adjustment. The foreign_gain refusal covers capital gains and capital gain distributions, so including the dividends unadjusted on line 1a follows the 'No adjustments required' instruction.

<!-- part section 3a -->
3a — Certain itemized deductions or standard deduction
Status: **MATCH**

Model: If itemizing, the program enters Schedule A line 4 (medical) plus line 5e. Income tax on line 5a is refused, the sales-tax election is refused, and line 5e is the SALT-limited amount, which keeps within 'Don't include more state and local taxes on Form 1116, lines 2 and 3a, than ... line 5e'. If not itemizing, it enters the standard deduction from line 12e, as the instructions say ('If you don't itemize deductions, enter your standard deduction on line 3a').

<!-- part section 3b -->
3b — Other deductions (Schedule 1, Part II adjustments to income, less the student loan interes
Status: **MATCH**

Model: Schedule 1 Part II adjustments (line 26) are entered without student loan interest (line 21), which the instructions route to line 4b. Schedule 1-A lines 30 and 37 are never in line 26, matching 'Don't include the enhanced deduction for seniors' and the routing of car loan interest to line 4b.

<!-- part section 3c -->
3c — Add lines 3a and 3b
Status: **MATCH**

Model: Add lines 3a and 3b, as the form says.

<!-- part section 3e -->
3e — Gross income from all sources (wages, taxable interest, ordinary dividends, taxable IRA di
Status: **MATCH**

Model: Gross income from all sources is built from wage, interest, dividend, retirement, social security and Schedule 1 income, plus capital gains before losses (each gain entry) and capital gain distributions. This follows 'total capital and ordinary gains (before subtracting any losses), and all other income'. Business gross receipts are refused by f1116.business.

<!-- part section 6 (Total) -->
6 (Total) — Add lines 2, 3g, 4a, 4b, and 5 (Total, add cols. A, B, and C)
Status: **MATCH**

Model: Each column adds lines 3g and 4a, and the total adds the columns. The other lines are zero in supported cases: line 2 (state income tax) is refused via itemized_unread, line 4b is refused via asset_method when interest must be apportioned, and line 5 (foreign losses) is refused via foreign_gain.

<!-- part section 7 (Total) -->
7 (Total) — Subtract line 6 from line 1a (Total, add cols. A, B, and C)
Status: **MATCH**

Model: Subtract line 6 from line 1a in each column, then total the columns.

<!-- part section 8 -->
8 — Add lines A through C, column (u)
Status: **MATCH**

Model: Column (u) adds columns (q) through (t). Rents (r) and other taxes (t) are zero for 1099 dividend and interest taxes, and the totals are summed over the country lines as line 8 directs.

<!-- part section 9 -->
9 — Enter the amount from line 8. These are your total foreign taxes paid or accrued for the c
Status: **MATCH**

Model: Enter the amount from line 8.

<!-- part section 10 -->
10 — Carryover of foreign taxes (Schedule B (Form 1116), line 3, column (xiv)) when a carryover
Status: **MATCH**

Model: If a carryover is claimed, the program enters Schedule B line 3, column (xiv), per 'Enter the sum of any carryover of foreign taxes (from Schedule B, line 3, column (xiv))'; otherwise zero. A carryback into 2025 cannot exist on an original 2025 return.

<!-- part section 11 -->
11 — Add lines 9 and 10
Status: **MATCH**

Model: Add lines 9 and 10.

<!-- part section 12 -->
12 — Reduction in foreign taxes (zero on the returns prepared; a reduction is refused)
Status: **MATCH**

Model: Zero, with the f1116.reduction refusal covering the line 12 reductions: Form 2555/4563, Puerto Rico, oil and gas, mineral, Form 5471/8865 failures, boycott, and splitting events.

<!-- part section 13 -->
13 — Taxes reclassified under high tax kickout (zero on the returns prepared; possible high-tax
Status: **MATCH**

Model: Zero, with the high_taxed refusal applying the grouping test from Regulations 1.904-4(c): the 15%-or-greater and under-15% withholding groups, with tax compared against the highest section 1 rate times income after deductions.

<!-- part section 14 -->
14 — Combine lines 11, 12, and 13. This is the total amount of foreign taxes available for cred
Status: **MATCH**

Model: Line 11 less line 12 (a reduction entered in parentheses) plus line 13 carries out 'Combine lines 11, 12, and 13'.

<!-- part section 15 -->
15 — Enter the amount from line 7. This is your taxable income or (loss) from sources outside t
Status: **MATCH**

Model: Enter the amount from line 7.

<!-- part section 16 -->
16 — Adjustments to line 15 (zero on the returns prepared; a U.S. loss or a loss account is ref
Status: **MATCH**

Model: Zero. The refusals cover the line 16 adjustments: loss-account recapture (loss_accounts), U.S. loss allocation (us_loss), and foreign-loss allocation and section 461(l) losses (another category and business both refused).

<!-- part section 17 -->
17 — Combine the amounts on lines 15 and 16. This is your net foreign source taxable income
Status: **MATCH**

Model: Combine lines 15 and 16.

<!-- part section 18 -->
18 — Individuals, the sum of (i) Form 1040 line 11b minus line 14 and (ii) Schedule 1-A line 37
Status: **MATCH**

Model: The program enters (Form 1040 line 11b minus line 14) plus Schedule 1-A line 37, floored at zero, per 'If the result is zero or less, enter -0-'. The Worksheet for Line 18 case is refused by f1116.adjust.

<!-- part section 20 -->
20 — Individuals, the total of Form 1040 line 16 and Schedule 2 line 1z
Status: **MATCH**

Model: Form 1040 line 16 plus Schedule 2 line 1z. The 'less any tax ... from Form 4972' case is excluded, because lump-sum distributions are refused through retirement.special.

<!-- part section 21 -->
21 — Multiply line 20 by line 19 (maximum amount of credit)
Status: **UNCLEAR**

Restated: Choose — [helper "Line 18 is more than zero (line 19 is figured)" = true → helper "Divide line 17 by line 18, rounded to four decimal places, not more than 1 and not less than 0 (line 19); multiply line 20 by the result"] [helper "Line 18 is more than zero (line 19 is figured)" = false → helper "Year parameter sales.zero"]

Model: Line 19 follows the IRS conditions: zero when line 18 is zero, '1' when line 17 is more than line 18, and zero when line 17 is zero or less. But the program rounds the ratio to four decimal places, and the line 19 text ('Divide line 17 by line 18') gives no rounding precision; only line 3f states four-place rounding. Whether this rounding is allowed cannot be judged from the text.

Ruling: open

<!-- part section 22 -->
22 — Increase in limitation (section 960(c)) (zero on the returns prepared; refused on Schedule
Status: **UNCLEAR**

Restated: Enter the amount from helper "Year parameter sales.zero".

Model: Always zero, but no refusal or gate names the case the instructions describe: an excess limitation account under section 960(c) from prior section 951(a) inclusions, with a later distribution of previously taxed earnings. The text gives no way to confirm that this case is outside the returns prepared.

Ruling: open

<!-- part section 23 -->
23 — Add lines 21 and 22
Status: **MATCH**

Model: Add lines 21 and 22.

<!-- part section 24 -->
24 — Enter the smaller of line 14 or line 23
Status: **MATCH**

Model: Enter the smaller of line 14 or line 23.

<!-- part section 27 -->
27 — Credit for taxes on passive category income
Status: **MATCH**

Model: Line 24 of this passive category form is entered on line 27, per 'Enter amounts from Part III, line 24, for each applicable category'.

<!-- part section 32 -->
32 — Add lines 25 through 31 (only line 27 is used on the returns prepared)
Status: **MATCH**

Model: Lines 25 through 31 are added. Only line 27 can be nonzero, since another category of income is refused.

<!-- part section 33 -->
33 — Enter the smaller of line 20 or line 32
Status: **MATCH**

Model: Enter the smaller of line 20 or line 32.

<!-- part section 34 -->
34 — Reduction of credit for international boycott operations (zero on the returns prepared; re
Status: **MATCH**

Model: Zero. The boycott reduction is refused by the f1116.reduction question, whose list includes an international boycott.

<!-- part section 35 -->
35 — Subtract line 34 from line 33. This is your foreign tax credit
Status: **MATCH**

Model: Subtract line 34 from line 33. Each refusal names an excluded case the IRS text describes: other categories, foreign currency, creditability, business gross receipts, foreign capital gains, Schedule C (Form 1116), lines 12, 13 and 16, Schedule B lines 2 and 7 and spouse allocation, state income tax on line 2, the asset method, and the Worksheet for Line 18.

<!-- part raw -->

## Raw response

```yaml
```yaml
lines:
  - key: "1a (Total)"
    status: MATCH
    reason: "Each column's line 1a is its foreign-source dividends plus interest, and the total adds the columns. The f1116.adjust refusal covers the qualified-dividend adjustment. The foreign_gain refusal covers capital gains and capital gain distributions, so including the dividends unadjusted on line 1a follows the 'No adjustments required' instruction."
  - key: "3a"
    status: MATCH
    reason: "If itemizing, the program enters Schedule A line 4 (medical) plus line 5e. Income tax on line 5a is refused, the sales-tax election is refused, and line 5e is the SALT-limited amount, which keeps within 'Don't include more state and local taxes on Form 1116, lines 2 and 3a, than ... line 5e'. If not itemizing, it enters the standard deduction from line 12e, as the instructions say ('If you don't itemize deductions, enter your standard deduction on line 3a')."
  - key: "3b"
    status: MATCH
    reason: "Schedule 1 Part II adjustments (line 26) are entered without student loan interest (line 21), which the instructions route to line 4b. Schedule 1-A lines 30 and 37 are never in line 26, matching 'Don't include the enhanced deduction for seniors' and the routing of car loan interest to line 4b."
  - key: "3c"
    status: MATCH
    reason: "Add lines 3a and 3b, as the form says."
  - key: "3e"
    status: MATCH
    reason: "Gross income from all sources is built from wage, interest, dividend, retirement, social security and Schedule 1 income, plus capital gains before losses (each gain entry) and capital gain distributions. This follows 'total capital and ordinary gains (before subtracting any losses), and all other income'. Business gross receipts are refused by f1116.business."
  - key: "6 (Total)"
    status: MATCH
    reason: "Each column adds lines 3g and 4a, and the total adds the columns. The other lines are zero in supported cases: line 2 (state income tax) is refused via itemized_unread, line 4b is refused via asset_method when interest must be apportioned, and line 5 (foreign losses) is refused via foreign_gain."
  - key: "7 (Total)"
    status: MATCH
    reason: "Subtract line 6 from line 1a in each column, then total the columns."
  - key: "8"
    status: MATCH
    reason: "Column (u) adds columns (q) through (t). Rents (r) and other taxes (t) are zero for 1099 dividend and interest taxes, and the totals are summed over the country lines as line 8 directs."
  - key: "9"
    status: MATCH
    reason: "Enter the amount from line 8."
  - key: "10"
    status: MATCH
    reason: "If a carryover is claimed, the program enters Schedule B line 3, column (xiv), per 'Enter the sum of any carryover of foreign taxes (from Schedule B, line 3, column (xiv))'; otherwise zero. A carryback into 2025 cannot exist on an original 2025 return."
  - key: "11"
    status: MATCH
    reason: "Add lines 9 and 10."
  - key: "12"
    status: MATCH
    reason: "Zero, with the f1116.reduction refusal covering the line 12 reductions: Form 2555/4563, Puerto Rico, oil and gas, mineral, Form 5471/8865 failures, boycott, and splitting events."
  - key: "13"
    status: MATCH
    reason: "Zero, with the high_taxed refusal applying the grouping test from Regulations 1.904-4(c): the 15%-or-greater and under-15% withholding groups, with tax compared against the highest section 1 rate times income after deductions."
  - key: "14"
    status: MATCH
    reason: "Line 11 less line 12 (a reduction entered in parentheses) plus line 13 carries out 'Combine lines 11, 12, and 13'."
  - key: "15"
    status: MATCH
    reason: "Enter the amount from line 7."
  - key: "16"
    status: MATCH
    reason: "Zero. The refusals cover the line 16 adjustments: loss-account recapture (loss_accounts), U.S. loss allocation (us_loss), and foreign-loss allocation and section 461(l) losses (another category and business both refused)."
  - key: "17"
    status: MATCH
    reason: "Combine lines 15 and 16."
  - key: "18"
    status: MATCH
    reason: "The program enters (Form 1040 line 11b minus line 14) plus Schedule 1-A line 37, floored at zero, per 'If the result is zero or less, enter -0-'. The Worksheet for Line 18 case is refused by f1116.adjust."
  - key: "20"
    status: MATCH
    reason: "Form 1040 line 16 plus Schedule 2 line 1z. The 'less any tax ... from Form 4972' case is excluded, because lump-sum distributions are refused through retirement.special."
  - key: "21"
    status: UNCLEAR
    reason: "Line 19 follows the IRS conditions: zero when line 18 is zero, '1' when line 17 is more than line 18, and zero when line 17 is zero or less. But the program rounds the ratio to four decimal places, and the line 19 text ('Divide line 17 by line 18') gives no rounding precision; only line 3f states four-place rounding. Whether this rounding is allowed cannot be judged from the text."
  - key: "22"
    status: UNCLEAR
    reason: "Always zero, but no refusal or gate names the case the instructions describe: an excess limitation account under section 960(c) from prior section 951(a) inclusions, with a later distribution of previously taxed earnings. The text gives no way to confirm that this case is outside the returns prepared."
  - key: "23"
    status: MATCH
    reason: "Add lines 21 and 22."
  - key: "24"
    status: MATCH
    reason: "Enter the smaller of line 14 or line 23."
  - key: "27"
    status: MATCH
    reason: "Line 24 of this passive category form is entered on line 27, per 'Enter amounts from Part III, line 24, for each applicable category'."
  - key: "32"
    status: MATCH
    reason: "Lines 25 through 31 are added. Only line 27 can be nonzero, since another category of income is refused."
  - key: "33"
    status: MATCH
    reason: "Enter the smaller of line 20 or line 32."
  - key: "34"
    status: MATCH
    reason: "Zero. The boycott reduction is refused by the f1116.reduction question, whose list includes an international boycott."
  - key: "35"
    status: MATCH
    reason: "Subtract line 34 from line 33. Each refusal names an excluded case the IRS text describes: other categories, foreign currency, creditability, business gross receipts, foreign capital gains, Schedule C (Form 1116), lines 12, 13 and 16, Schedule B lines 2 and 7 and spouse allocation, state income tax on line 2, the asset method, and the Worksheet for Line 18."
```
```

<!-- end -->
