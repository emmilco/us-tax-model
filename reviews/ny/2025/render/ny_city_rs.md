# Render comparison — ny_city_rs

The rendered English of every printed line of `New York City tax rate schedule` (`rendered/ny/2025/ny_city_rs.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-04 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | f65e532b15f0dc5f29768e6027e58f8e02bd1b17e616482d7faf5f4654ac55a3 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 390d22ff0e196470cf6119d363b160934f85d1c37fcc6196dd053b2d9797cb11 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 1d5ab9d94846c20ec66c20d0412c3bf395b2b2c7bb9dec109ecf1cf2328fdaa7 |
| lines judged | 53 |
| match / mismatch / unclear / missing | 41 / 0 / 12 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| ny_it201i-html | Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny) | 1 | cited sections: New York City tax rate schedule | 63863fe461c33d052e26a67c87d000ed70b896c72437350880a9e1c680104982 | - | - |
| ny_it201i | Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20 | 4 | cited pages | 05f677379d60faca0da08ac2dc171a937cf56878f73956511975c1dcc48aeff9 | 4 | 460f67bd9e14ac9d7ed2e001426510569307546a5c2cf0a97784808e2678eeaf |

## Lines

### (line 47) — New York City taxable income (line 47)
Status: **MATCH**

Model: The schedule is keyed to "If line 47 is:". Taking line 47 as an input from the calling line matches.

### (band 1) (single.b1.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: For $0 to $12,000 the tax is "3.078% of line 47". The excess over $0 is line 47 itself.

### (band 1) (single.b1.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 1) (single.b1.excess) by 3078/100000 (ny.city.b1.rate), rounded to the nearest multiple of $1 (half up).

Model: The 3.078% rate matches. The text gives no rounding rule ("3.078% of line 47"), so rounding to the nearest dollar cannot be confirmed.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the City rate schedule section, do not carry the whole-dollar rule.

### (band 1) (single.b1.base) — The band's base amount
Status: **MATCH**

Model: The first single bracket prints no base amount before "3.078% of line 47". A base of $0 matches.

### The tax is (single.b1.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: Base plus product gives the first-bracket tax, which is 3.078% of line 47.

### (band 2) (single.b2.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: The text says "of the excess over $12,000".

### (band 2) (single.b2.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 2) (single.b2.excess) by 3762/100000 (ny.city.b2.rate), rounded to the nearest multiple of $1 (half up).

Model: The 3.762% rate matches. The text states no rounding of the product.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the City rate schedule section, do not carry the whole-dollar rule.

### (band 2) (single.b2.base) — The band's base amount
Status: **MATCH**

Model: The text says "$369 plus 3.762%".

### The tax is (single.b2.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: The text says "$369 plus 3.762% of the excess over $12,000".

### (band 3) (single.b3.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: The text says "of the excess over 25,000".

### (band 3) (single.b3.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 3) (single.b3.excess) by 3819/100000 (ny.city.b3.rate), rounded to the nearest multiple of $1 (half up).

Model: The 3.819% rate matches. The text states no rounding of the product.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the City rate schedule section, do not carry the whole-dollar rule.

### (band 3) (single.b3.base) — The band's base amount
Status: **MATCH**

Model: The text says "858 plus 3.819%".

### The tax is (single.b3.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: The text says "858 plus 3.819% of the excess over 25,000".

### (band 4) (single.b4.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: The text says "of the excess over 50,000".

### (band 4) (single.b4.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 4) (single.b4.excess) by 3876/100000 (ny.city.b4.rate), rounded to the nearest multiple of $1 (half up).

Model: The 3.876% rate matches. The text states no rounding of the product.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the City rate schedule section, do not carry the whole-dollar rule.

### (band 4) (single.b4.base) — The band's base amount
Status: **MATCH**

Model: The text says "1,813 plus 3.876%".

### The tax is (single.b4.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: The text says "1,813 plus 3.876% of the excess over 50,000".

### The tax is (single.result) — Single and married filing separately—filing status ① and ③: the tax for the band that hold
Status: **MATCH**

Model: The bracket bounds follow "over / but not over": $0–12,000, 12,000–25,000, 25,000–50,000, and over 50,000. The selection matches.

### (band 1) (mfj.b1.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: For $0 to $21,600 the tax is "3.078% of line 47".

### (band 1) (mfj.b1.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 1) (mfj.b1.excess) by 3078/100000 (ny.city.b1.rate), rounded to the nearest multiple of $1 (half up).

Model: The 3.078% rate matches. The text states no rounding of the product.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the City rate schedule section, do not carry the whole-dollar rule.

### (band 1) (mfj.b1.base) — The band's base amount
Status: **MATCH**

Model: No base amount is printed for the first married-filing-jointly bracket. A base of $0 matches.

### The tax is (mfj.b1.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: Base plus product gives 3.078% of line 47.

### (band 2) (mfj.b2.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: The text says "of the excess over $21,600".

### (band 2) (mfj.b2.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 2) (mfj.b2.excess) by 3762/100000 (ny.city.b2.rate), rounded to the nearest multiple of $1 (half up).

Model: The 3.762% rate matches. The text states no rounding of the product.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the City rate schedule section, do not carry the whole-dollar rule.

### (band 2) (mfj.b2.base) — The band's base amount
Status: **MATCH**

Model: The text says "$665 plus 3.762%".

### The tax is (mfj.b2.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: The text says "$665 plus 3.762% of the excess over $21,600".

### (band 3) (mfj.b3.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: The text says "of the excess over 45,000".

### (band 3) (mfj.b3.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 3) (mfj.b3.excess) by 3819/100000 (ny.city.b3.rate), rounded to the nearest multiple of $1 (half up).

Model: The 3.819% rate matches. The text states no rounding of the product.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the City rate schedule section, do not carry the whole-dollar rule.

### (band 3) (mfj.b3.base) — The band's base amount
Status: **MATCH**

Model: The text says "1,545 plus 3.819%".

### The tax is (mfj.b3.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: The text says "1,545 plus 3.819% of the excess over 45,000".

### (band 4) (mfj.b4.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: The text says "of the excess over 90,000".

### (band 4) (mfj.b4.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 4) (mfj.b4.excess) by 3876/100000 (ny.city.b4.rate), rounded to the nearest multiple of $1 (half up).

Model: The 3.876% rate matches. The text states no rounding of the product.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the City rate schedule section, do not carry the whole-dollar rule.

### (band 4) (mfj.b4.base) — The band's base amount
Status: **MATCH**

Model: The text says "3,264 plus 3.876%".

### The tax is (mfj.b4.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: The text says "3,264 plus 3.876% of the excess over 90,000".

### The tax is (mfj.result) — Married filing jointly and qualifying surviving spouse—filing status ② and ⑤: the tax for
Status: **MATCH**

Model: The bracket bounds are $0–21,600, 21,600–45,000, 45,000–90,000, and over 90,000, using "over / but not over". The selection matches.

### (band 1) (hoh.b1.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: For $0 to $14,400 the tax is "3.078% of line 47".

### (band 1) (hoh.b1.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 1) (hoh.b1.excess) by 3078/100000 (ny.city.b1.rate), rounded to the nearest multiple of $1 (half up).

Model: The 3.078% rate matches. The text states no rounding of the product.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the City rate schedule section, do not carry the whole-dollar rule.

### (band 1) (hoh.b1.base) — The band's base amount
Status: **MATCH**

Model: No base amount is printed for the first head-of-household bracket. A base of $0 matches.

### The tax is (hoh.b1.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: Base plus product gives 3.078% of line 47.

### (band 2) (hoh.b2.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: The text says "of the excess over $14,400".

### (band 2) (hoh.b2.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 2) (hoh.b2.excess) by 3762/100000 (ny.city.b2.rate), rounded to the nearest multiple of $1 (half up).

Model: The 3.762% rate matches. The text states no rounding of the product.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the City rate schedule section, do not carry the whole-dollar rule.

### (band 2) (hoh.b2.base) — The band's base amount
Status: **MATCH**

Model: The text says "$443 plus 3.762%".

### The tax is (hoh.b2.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: The text says "$443 plus 3.762% of the excess over $14,400".

### (band 3) (hoh.b3.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: The text says "of the excess over 30,000".

### (band 3) (hoh.b3.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 3) (hoh.b3.excess) by 3819/100000 (ny.city.b3.rate), rounded to the nearest multiple of $1 (half up).

Model: The 3.819% rate matches. The text states no rounding of the product.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the City rate schedule section, do not carry the whole-dollar rule.

### (band 3) (hoh.b3.base) — The band's base amount
Status: **MATCH**

Model: The text says "1,030 plus 3.819%".

### The tax is (hoh.b3.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: The text says "1,030 plus 3.819% of the excess over 30,000".

### (band 4) (hoh.b4.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: The text says "of the excess over 60,000".

### (band 4) (hoh.b4.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 4) (hoh.b4.excess) by 3876/100000 (ny.city.b4.rate), rounded to the nearest multiple of $1 (half up).

Model: The 3.876% rate matches. The text states no rounding of the product.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the City rate schedule section, do not carry the whole-dollar rule.

### (band 4) (hoh.b4.base) — The band's base amount
Status: **MATCH**

Model: The text says "2,176 plus 3.876%".

### The tax is (hoh.b4.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: The text says "2,176 plus 3.876% of the excess over 60,000".

### The tax is (hoh.result) — Head of household—filing status ④: the tax for the band that holds the amount
Status: **MATCH**

Model: The bracket bounds are $0–14,400, 14,400–30,000, 30,000–60,000, and over 60,000, using "over / but not over". The selection matches.

### The tax is (tax) — The tax from the schedule for the filing status
Status: **MATCH**

Model: The schedules are headed "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", "Single and married filing separately—filing status ① and ③" and "Head of household—filing status ④". The status mapping matches.

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| (line 47) | b6c75940b9089cbfb4bc99876d4b60f74f21848e7246a183cbe15d031f32b1ce |
| (band 1) (single.b1.excess) | 2d348abeff5609c37838a199d40ee231b445f1797ed7cfe0935ab57637ac909c |
| (band 1) (single.b1.product) | 72511aecc9344e93176e043331a307abbd56f4b40657674902263719878663e9 |
| (band 1) (single.b1.base) | ff804b9aa684dfffc5d3e6f0e6249a49de6a06d20f3a8b19d051b2e2b79a55be |
| The tax is (single.b1.tax) | 487e441c29bf6521008d6434448230e84199b13a854716274750ea32fbe406f3 |
| (band 2) (single.b2.excess) | 40cf68c514092483ec7469fc69b88d66a47ce73c9d8e8ff303132f4f63fdce28 |
| (band 2) (single.b2.product) | 3ed169c93ccb5e2096645cf4b67d4c7c84e1e57f5025966baef84dcfcbd0915e |
| (band 2) (single.b2.base) | c1a4a15838854a917e70d3a34fb7b6826bd8c49ed26e44eef5ae6e52a53c23ff |
| The tax is (single.b2.tax) | 29a8a2e979135dc45b28f5abb314251da5a5926c268e10f21281b3faa1198c0f |
| (band 3) (single.b3.excess) | d5819e5c9045953b514af2af88509908a9bb5d7de7b4ebe7ba68046747880bf3 |
| (band 3) (single.b3.product) | b4f803da2b54143fb8ba4e3ec45b526a9fd4586f4111ecde37e185965c6932f2 |
| (band 3) (single.b3.base) | f6a3db7d323a47534e2b038fb37f40bae03569135a97d5059d72a8c6783932f9 |
| The tax is (single.b3.tax) | 18c4d13bff5999d873b7fae273071bf4a76a40491a2e02fb791687598e6ae174 |
| (band 4) (single.b4.excess) | 9b9725d8c0c1fbbe82e66db548b0231156c4dd682f4f83f814dbe7980b2f1e25 |
| (band 4) (single.b4.product) | 5168b24fad89694f5db033ddecae10ba2730d9d96975036f9c0a26bc95e18c7f |
| (band 4) (single.b4.base) | 54ff0dbe4620a69ac4a41ffdccfd4bed88cc68fdd7e3087635c0403ffcfdd2f1 |
| The tax is (single.b4.tax) | 8f53ae879c45491a1b7474f8ede164fbce7caa47626ac9ca26eaeae6b56dcf65 |
| The tax is (single.result) | bd492a43c3db16096d705a83200c9116b3ff80d2f428cd8c6fffc416d532c5d1 |
| (band 1) (mfj.b1.excess) | 87245a6a97d785950a9205a62ef7cb71f5cd47c2145a2dd0f991d486ef468536 |
| (band 1) (mfj.b1.product) | 72511aecc9344e93176e043331a307abbd56f4b40657674902263719878663e9 |
| (band 1) (mfj.b1.base) | ccd6fabb30f6efe4a82d542f019c4eef5acb32f81c7bd4dec8104afdbfc9b02e |
| The tax is (mfj.b1.tax) | c92dceba1c6c92e4206676d2553a8d93cd5c26d58fea4008b016c8e9ca5c5d1c |
| (band 2) (mfj.b2.excess) | 77f6f50c364f2cf7af426e9e4d83eb88df42f70870060a8ba00ff2e1bb775e18 |
| (band 2) (mfj.b2.product) | 3ed169c93ccb5e2096645cf4b67d4c7c84e1e57f5025966baef84dcfcbd0915e |
| (band 2) (mfj.b2.base) | 43ceb43c5373039872402814d618e4a43a8c5a252ecb30f092bde2fab9e7759d |
| The tax is (mfj.b2.tax) | 3242dcc11cd04e83cb5f7b2a5dca8923d234ef9717d07a15ba7f07b4e420993f |
| (band 3) (mfj.b3.excess) | 172cef53a066858e7f8b7a7422d022ae4890608cc9ddaa7ae43c6018a1e65842 |
| (band 3) (mfj.b3.product) | b4f803da2b54143fb8ba4e3ec45b526a9fd4586f4111ecde37e185965c6932f2 |
| (band 3) (mfj.b3.base) | 5d26151acfb6e0cd78d23143049dac6f5ec789489fc3f5972f5bef892fb6ce3d |
| The tax is (mfj.b3.tax) | 9a27fdab71fce0a97d617c44d11ac45c417f25912ed572a44cca7b26c868e3cf |
| (band 4) (mfj.b4.excess) | dfe6f381caf0b05343fe038ffe99904af1c5f398b903bdfdaed1a95c8e527e3e |
| (band 4) (mfj.b4.product) | 5168b24fad89694f5db033ddecae10ba2730d9d96975036f9c0a26bc95e18c7f |
| (band 4) (mfj.b4.base) | 4de8a07e7aa05dac91b82bcbc6a81bb0169e1af9ffb41e910a1e99f18bbebdb9 |
| The tax is (mfj.b4.tax) | cb99481c2e279b2fd9b4569dfcd043fe0d5ba20ded771a8c548c2ac708d56b13 |
| The tax is (mfj.result) | bd492a43c3db16096d705a83200c9116b3ff80d2f428cd8c6fffc416d532c5d1 |
| (band 1) (hoh.b1.excess) | bdd1564cee5cbef15c28d11499147f69ce47d7d0e95f5ffe49de44dd573a925c |
| (band 1) (hoh.b1.product) | 72511aecc9344e93176e043331a307abbd56f4b40657674902263719878663e9 |
| (band 1) (hoh.b1.base) | c190f0c0b2e0e4545aa20affe80f97f011795dd2d077feef9add33dd9d8a3de7 |
| The tax is (hoh.b1.tax) | 5ef6821d061737f675b02a1b7bdfb35d08c4e00d5fc5fc919544684e204bbae5 |
| (band 2) (hoh.b2.excess) | 058a9bdf69580a50aa80e2189bacde50f723345c69c01496229af547e26e1510 |
| (band 2) (hoh.b2.product) | 3ed169c93ccb5e2096645cf4b67d4c7c84e1e57f5025966baef84dcfcbd0915e |
| (band 2) (hoh.b2.base) | fd3f8dd845a833ef50526035d69aa00e1f12527bb5d6d1fefeb47190a3e3344b |
| The tax is (hoh.b2.tax) | 543b74706ce7937e148126f823ae75a4b775755eb9c5f92b6e421d229c24fd61 |
| (band 3) (hoh.b3.excess) | 0ceec8bb149b65708bf32b06a1a1f0fdc8e21751c82302fc6d05a6c3f40ff043 |
| (band 3) (hoh.b3.product) | b4f803da2b54143fb8ba4e3ec45b526a9fd4586f4111ecde37e185965c6932f2 |
| (band 3) (hoh.b3.base) | ee618727984e8caa263680f2c9091b66c2742aca855004d3ed7fddd92d019c2b |
| The tax is (hoh.b3.tax) | 8b352d4d1e51c90daf10e2247b2db08e61caaab71bbbcd7ad2fc86f8bf45af18 |
| (band 4) (hoh.b4.excess) | 280ea4030288f491ee99a8a3da90d3befaeade81d80c23c1692a7f066c729934 |
| (band 4) (hoh.b4.product) | 5168b24fad89694f5db033ddecae10ba2730d9d96975036f9c0a26bc95e18c7f |
| (band 4) (hoh.b4.base) | 4ededbdea7ae8deeb8f7b8d69ecf8ab3f3cdff6d5405f3d1a1b927d0af413bd3 |
| The tax is (hoh.b4.tax) | b2d39f5a8fd8c873602ff4e2dee7247c6a90c47d0a7cabd1b086e90d6af1bb5e |
| The tax is (hoh.result) | bd492a43c3db16096d705a83200c9116b3ff80d2f428cd8c6fffc416d532c5d1 |
| The tax is (tax) | 6e5c20c94f5d3a766ce328739d89d3087dc28cc48af4cb2108ea048348c8e2eb |
| (rest of the document) | f1bedf750e2d3a887fc608070478b3a63699ecb34bf9740306f406c21fa7e364 |

## Raw response

```yaml
```yaml
lines:
  - key: "(line 47)"
    status: MATCH
    reason: "The schedule is keyed to \"If line 47 is:\". Taking line 47 as an input from the calling line matches."
  - key: "(band 1) (single.b1.excess)"
    status: MATCH
    reason: "For $0 to $12,000 the tax is \"3.078% of line 47\". The excess over $0 is line 47 itself."
  - key: "(band 1) (single.b1.product)"
    status: UNCLEAR
    reason: "The 3.078% rate matches. The text gives no rounding rule (\"3.078% of line 47\"), so rounding to the nearest dollar cannot be confirmed."
  - key: "(band 1) (single.b1.base)"
    status: MATCH
    reason: "The first single bracket prints no base amount before \"3.078% of line 47\". A base of $0 matches."
  - key: "The tax is (single.b1.tax)"
    status: MATCH
    reason: "Base plus product gives the first-bracket tax, which is 3.078% of line 47."
  - key: "(band 2) (single.b2.excess)"
    status: MATCH
    reason: "The text says \"of the excess over $12,000\"."
  - key: "(band 2) (single.b2.product)"
    status: UNCLEAR
    reason: "The 3.762% rate matches. The text states no rounding of the product."
  - key: "(band 2) (single.b2.base)"
    status: MATCH
    reason: "The text says \"$369 plus 3.762%\"."
  - key: "The tax is (single.b2.tax)"
    status: MATCH
    reason: "The text says \"$369 plus 3.762% of the excess over $12,000\"."
  - key: "(band 3) (single.b3.excess)"
    status: MATCH
    reason: "The text says \"of the excess over 25,000\"."
  - key: "(band 3) (single.b3.product)"
    status: UNCLEAR
    reason: "The 3.819% rate matches. The text states no rounding of the product."
  - key: "(band 3) (single.b3.base)"
    status: MATCH
    reason: "The text says \"858 plus 3.819%\"."
  - key: "The tax is (single.b3.tax)"
    status: MATCH
    reason: "The text says \"858 plus 3.819% of the excess over 25,000\"."
  - key: "(band 4) (single.b4.excess)"
    status: MATCH
    reason: "The text says \"of the excess over 50,000\"."
  - key: "(band 4) (single.b4.product)"
    status: UNCLEAR
    reason: "The 3.876% rate matches. The text states no rounding of the product."
  - key: "(band 4) (single.b4.base)"
    status: MATCH
    reason: "The text says \"1,813 plus 3.876%\"."
  - key: "The tax is (single.b4.tax)"
    status: MATCH
    reason: "The text says \"1,813 plus 3.876% of the excess over 50,000\"."
  - key: "The tax is (single.result)"
    status: MATCH
    reason: "The bracket bounds follow \"over / but not over\": $0–12,000, 12,000–25,000, 25,000–50,000, and over 50,000. The selection matches."
  - key: "(band 1) (mfj.b1.excess)"
    status: MATCH
    reason: "For $0 to $21,600 the tax is \"3.078% of line 47\"."
  - key: "(band 1) (mfj.b1.product)"
    status: UNCLEAR
    reason: "The 3.078% rate matches. The text states no rounding of the product."
  - key: "(band 1) (mfj.b1.base)"
    status: MATCH
    reason: "No base amount is printed for the first married-filing-jointly bracket. A base of $0 matches."
  - key: "The tax is (mfj.b1.tax)"
    status: MATCH
    reason: "Base plus product gives 3.078% of line 47."
  - key: "(band 2) (mfj.b2.excess)"
    status: MATCH
    reason: "The text says \"of the excess over $21,600\"."
  - key: "(band 2) (mfj.b2.product)"
    status: UNCLEAR
    reason: "The 3.762% rate matches. The text states no rounding of the product."
  - key: "(band 2) (mfj.b2.base)"
    status: MATCH
    reason: "The text says \"$665 plus 3.762%\"."
  - key: "The tax is (mfj.b2.tax)"
    status: MATCH
    reason: "The text says \"$665 plus 3.762% of the excess over $21,600\"."
  - key: "(band 3) (mfj.b3.excess)"
    status: MATCH
    reason: "The text says \"of the excess over 45,000\"."
  - key: "(band 3) (mfj.b3.product)"
    status: UNCLEAR
    reason: "The 3.819% rate matches. The text states no rounding of the product."
  - key: "(band 3) (mfj.b3.base)"
    status: MATCH
    reason: "The text says \"1,545 plus 3.819%\"."
  - key: "The tax is (mfj.b3.tax)"
    status: MATCH
    reason: "The text says \"1,545 plus 3.819% of the excess over 45,000\"."
  - key: "(band 4) (mfj.b4.excess)"
    status: MATCH
    reason: "The text says \"of the excess over 90,000\"."
  - key: "(band 4) (mfj.b4.product)"
    status: UNCLEAR
    reason: "The 3.876% rate matches. The text states no rounding of the product."
  - key: "(band 4) (mfj.b4.base)"
    status: MATCH
    reason: "The text says \"3,264 plus 3.876%\"."
  - key: "The tax is (mfj.b4.tax)"
    status: MATCH
    reason: "The text says \"3,264 plus 3.876% of the excess over 90,000\"."
  - key: "The tax is (mfj.result)"
    status: MATCH
    reason: "The bracket bounds are $0–21,600, 21,600–45,000, 45,000–90,000, and over 90,000, using \"over / but not over\". The selection matches."
  - key: "(band 1) (hoh.b1.excess)"
    status: MATCH
    reason: "For $0 to $14,400 the tax is \"3.078% of line 47\"."
  - key: "(band 1) (hoh.b1.product)"
    status: UNCLEAR
    reason: "The 3.078% rate matches. The text states no rounding of the product."
  - key: "(band 1) (hoh.b1.base)"
    status: MATCH
    reason: "No base amount is printed for the first head-of-household bracket. A base of $0 matches."
  - key: "The tax is (hoh.b1.tax)"
    status: MATCH
    reason: "Base plus product gives 3.078% of line 47."
  - key: "(band 2) (hoh.b2.excess)"
    status: MATCH
    reason: "The text says \"of the excess over $14,400\"."
  - key: "(band 2) (hoh.b2.product)"
    status: UNCLEAR
    reason: "The 3.762% rate matches. The text states no rounding of the product."
  - key: "(band 2) (hoh.b2.base)"
    status: MATCH
    reason: "The text says \"$443 plus 3.762%\"."
  - key: "The tax is (hoh.b2.tax)"
    status: MATCH
    reason: "The text says \"$443 plus 3.762% of the excess over $14,400\"."
  - key: "(band 3) (hoh.b3.excess)"
    status: MATCH
    reason: "The text says \"of the excess over 30,000\"."
  - key: "(band 3) (hoh.b3.product)"
    status: UNCLEAR
    reason: "The 3.819% rate matches. The text states no rounding of the product."
  - key: "(band 3) (hoh.b3.base)"
    status: MATCH
    reason: "The text says \"1,030 plus 3.819%\"."
  - key: "The tax is (hoh.b3.tax)"
    status: MATCH
    reason: "The text says \"1,030 plus 3.819% of the excess over 30,000\"."
  - key: "(band 4) (hoh.b4.excess)"
    status: MATCH
    reason: "The text says \"of the excess over 60,000\"."
  - key: "(band 4) (hoh.b4.product)"
    status: UNCLEAR
    reason: "The 3.876% rate matches. The text states no rounding of the product."
  - key: "(band 4) (hoh.b4.base)"
    status: MATCH
    reason: "The text says \"2,176 plus 3.876%\"."
  - key: "The tax is (hoh.b4.tax)"
    status: MATCH
    reason: "The text says \"2,176 plus 3.876% of the excess over 60,000\"."
  - key: "The tax is (hoh.result)"
    status: MATCH
    reason: "The bracket bounds are $0–14,400, 14,400–30,000, 30,000–60,000, and over 60,000, using \"over / but not over\". The selection matches."
  - key: "The tax is (tax)"
    status: MATCH
    reason: "The schedules are headed \"Married filing jointly and qualifying surviving spouse—filing status ② and ⑤\", \"Single and married filing separately—filing status ① and ③\" and \"Head of household—filing status ④\". The status mapping matches."
```
```
