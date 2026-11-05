# Render comparison — ny_rs

The rendered English of every printed line of `New York State tax rate schedule` (`rendered/ny/2025/ny_rs.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-04 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 0df624d5ecc0f13b19af2ce1d427a40e0655f67a2fd300af46ba9115db2f5617 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 390d22ff0e196470cf6119d363b160934f85d1c37fcc6196dd053b2d9797cb11 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 1d350021a1c9d3955540ba38fe65b1f5a1b89253889a6abf4ddd553d4d5c7fe9 |
| lines judged | 113 |
| match / mismatch / unclear / missing | 86 / 0 / 27 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| ny_it201i-html | Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny) | 1 | cited sections: New York State tax rate schedule | 63863fe461c33d052e26a67c87d000ed70b896c72437350880a9e1c680104982 | - | - |
| ny_it201i | Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20 | 4 | cited pages | 05f677379d60faca0da08ac2dc171a937cf56878f73956511975c1dcc48aeff9 | 4 | 460f67bd9e14ac9d7ed2e001426510569307546a5c2cf0a97784808e2678eeaf |

## Lines

### (line 38) — Taxable income (line 38)
Status: **MATCH**

Model: The schedule is keyed on 'If line 38 is:', so taking the taxable income on line 38 as the input matches.

### (band 1) (single.b1.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: Band 1 (single/MFS) is '4% of line 38'. Line 38 minus $0, floored at zero, equals line 38.

### (band 1) (single.b1.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 1) (single.b1.excess) by 4% (0.04) (ny.rs.b1.rate), rounded to the nearest multiple of $1 (half up).

Model: The schedule says '4% of line 38' and gives no rounding. The pages provided do not support rounding the product to the nearest dollar, half up.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the rate schedule section, do not carry the whole-dollar rule.

### (band 1) (single.b1.base) — The band's base amount
Status: **MATCH**

Model: The first band has no base amount, only '4% of line 38', so the base is $0.

### The tax is (single.b1.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: Base of $0 plus 4% of line 38 is the band 1 tax.

### (band 2) (single.b2.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: The schedule says 'of the excess over $8,500'.

### (band 2) (single.b2.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 2) (single.b2.excess) by 45/1000 (ny.rs.b2.rate), rounded to the nearest multiple of $1 (half up).

Model: The 4.5% rate matches. The schedule states no rounding, so rounding to the nearest dollar, half up, cannot be confirmed from the text given.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the rate schedule section, do not carry the whole-dollar rule.

### (band 2) (single.b2.base) — The band's base amount
Status: **MATCH**

Model: The schedule gives '$340 plus 4.5%'.

### The tax is (single.b2.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: Base plus product matches '$340 plus 4.5% of the excess over $8,500'.

### (band 3) (single.b3.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: The schedule says 'of the excess over 11,700'.

### (band 3) (single.b3.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 3) (single.b3.excess) by 525/10000 (ny.rs.b3.rate), rounded to the nearest multiple of $1 (half up).

Model: The 5.25% rate matches. No rounding is stated in the text given.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the rate schedule section, do not carry the whole-dollar rule.

### (band 3) (single.b3.base) — The band's base amount
Status: **MATCH**

Model: The schedule gives '484 plus 5.25%'.

### The tax is (single.b3.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: Base plus product matches the band 3 schedule entry.

### (band 4) (single.b4.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: The schedule says 'of the excess over 13,900'.

### (band 4) (single.b4.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 4) (single.b4.excess) by 55/1000 (ny.rs.b4.rate), rounded to the nearest multiple of $1 (half up).

Model: The 5.5% rate matches. No rounding is stated in the text given.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the rate schedule section, do not carry the whole-dollar rule.

### (band 4) (single.b4.base) — The band's base amount
Status: **MATCH**

Model: The schedule gives '600 plus 5.5%'.

### The tax is (single.b4.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: Base plus product matches the band 4 schedule entry.

### (band 5) (single.b5.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: The schedule says 'of the excess over 80,650'.

### (band 5) (single.b5.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 5) (single.b5.excess) by 6% (0.06) (ny.rs.b5.rate), rounded to the nearest multiple of $1 (half up).

Model: The 6% rate matches. No rounding is stated in the text given.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the rate schedule section, do not carry the whole-dollar rule.

### (band 5) (single.b5.base) — The band's base amount
Status: **MATCH**

Model: The schedule gives '4,271 plus 6%'.

### The tax is (single.b5.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: Base plus product matches the band 5 schedule entry.

### (band 6) (single.b6.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: The schedule says 'of the excess over 215,400'.

### (band 6) (single.b6.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 6) (single.b6.excess) by 685/10000 (ny.rs.b6.rate), rounded to the nearest multiple of $1 (half up).

Model: The 6.85% rate matches. No rounding is stated in the text given.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the rate schedule section, do not carry the whole-dollar rule.

### (band 6) (single.b6.base) — The band's base amount
Status: **MATCH**

Model: The schedule gives '12,356 plus 6.85%'.

### The tax is (single.b6.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: Base plus product matches the band 6 schedule entry.

### (band 7) (single.b7.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: The schedule says 'of the excess over 1,077,550'.

### (band 7) (single.b7.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 7) (single.b7.excess) by 965/10000 (ny.rs.b7.rate), rounded to the nearest multiple of $1 (half up).

Model: The 9.65% rate matches. No rounding is stated in the text given.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the rate schedule section, do not carry the whole-dollar rule.

### (band 7) (single.b7.base) — The band's base amount
Status: **MATCH**

Model: The schedule gives '71,413 plus 9.65%'.

### The tax is (single.b7.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: Base plus product matches the band 7 schedule entry.

### (band 8) (single.b8.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: The schedule says 'of the excess over 5,000,000'.

### (band 8) (single.b8.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 8) (single.b8.excess) by 103/1000 (ny.rs.b8.rate), rounded to the nearest multiple of $1 (half up).

Model: The 10.3% rate matches. No rounding is stated in the text given.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the rate schedule section, do not carry the whole-dollar rule.

### (band 8) (single.b8.base) — The band's base amount
Status: **MATCH**

Model: The schedule gives '449,929 plus 10.3%'.

### The tax is (single.b8.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: Base plus product matches the band 8 schedule entry.

### (band 9) (single.b9.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: The schedule says 'of the excess over 25,000,000'.

### (band 9) (single.b9.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 9) (single.b9.excess) by 109/1000 (ny.rs.b9.rate), rounded to the nearest multiple of $1 (half up).

Model: The 10.9% rate matches. No rounding is stated in the text given.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the rate schedule section, do not carry the whole-dollar rule.

### (band 9) (single.b9.base) — The band's base amount
Status: **MATCH**

Model: The schedule gives '2,509,929 plus 10.9%'.

### The tax is (single.b9.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: Base plus product matches the band 9 schedule entry.

### The tax is (single.result) — Single and married filing separately—filing status ① and ③: the tax for the band that hold
Status: **MATCH**

Model: The band selection follows the schedule's 'over / but not over' bounds for single and MFS: 8,500, 11,700, 13,900, 80,650, 215,400, 1,077,550, 5,000,000 and 25,000,000.

### (band 1) (mfj.b1.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: MFJ band 1 is '4% of line 38'. Line 38 minus $0 equals line 38.

### (band 1) (mfj.b1.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 1) (mfj.b1.excess) by 4% (0.04) (ny.rs.b1.rate), rounded to the nearest multiple of $1 (half up).

Model: The 4% rate matches. No rounding is stated in the text given.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the rate schedule section, do not carry the whole-dollar rule.

### (band 1) (mfj.b1.base) — The band's base amount
Status: **MATCH**

Model: The first band has no base amount, so the base is $0.

### The tax is (mfj.b1.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: Base of $0 plus 4% of line 38 matches.

### (band 2) (mfj.b2.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: The schedule says 'of the excess over $17,150'.

### (band 2) (mfj.b2.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 2) (mfj.b2.excess) by 45/1000 (ny.rs.b2.rate), rounded to the nearest multiple of $1 (half up).

Model: The 4.5% rate matches. No rounding is stated in the text given.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the rate schedule section, do not carry the whole-dollar rule.

### (band 2) (mfj.b2.base) — The band's base amount
Status: **MATCH**

Model: The schedule gives '$686 plus 4.5%'.

### The tax is (mfj.b2.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: Base plus product matches the band 2 schedule entry.

### (band 3) (mfj.b3.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: The schedule says 'of the excess over 23,600'.

### (band 3) (mfj.b3.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 3) (mfj.b3.excess) by 525/10000 (ny.rs.b3.rate), rounded to the nearest multiple of $1 (half up).

Model: The 5.25% rate matches. No rounding is stated in the text given.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the rate schedule section, do not carry the whole-dollar rule.

### (band 3) (mfj.b3.base) — The band's base amount
Status: **MATCH**

Model: The schedule gives '976 plus 5.25%'.

### The tax is (mfj.b3.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: Base plus product matches the band 3 schedule entry.

### (band 4) (mfj.b4.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: The schedule says 'of the excess over 27,900'.

### (band 4) (mfj.b4.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 4) (mfj.b4.excess) by 55/1000 (ny.rs.b4.rate), rounded to the nearest multiple of $1 (half up).

Model: The 5.5% rate matches. No rounding is stated in the text given.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the rate schedule section, do not carry the whole-dollar rule.

### (band 4) (mfj.b4.base) — The band's base amount
Status: **MATCH**

Model: The schedule gives '1,202 plus 5.5%'.

### The tax is (mfj.b4.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: Base plus product matches the band 4 schedule entry.

### (band 5) (mfj.b5.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: The schedule says 'of the excess over 161,550'.

### (band 5) (mfj.b5.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 5) (mfj.b5.excess) by 6% (0.06) (ny.rs.b5.rate), rounded to the nearest multiple of $1 (half up).

Model: The 6% rate matches. No rounding is stated in the text given.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the rate schedule section, do not carry the whole-dollar rule.

### (band 5) (mfj.b5.base) — The band's base amount
Status: **MATCH**

Model: The schedule gives '8,553 plus 6%'.

### The tax is (mfj.b5.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: Base plus product matches the band 5 schedule entry.

### (band 6) (mfj.b6.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: The schedule says 'of the excess over 323,200'.

### (band 6) (mfj.b6.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 6) (mfj.b6.excess) by 685/10000 (ny.rs.b6.rate), rounded to the nearest multiple of $1 (half up).

Model: The 6.85% rate matches. No rounding is stated in the text given.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the rate schedule section, do not carry the whole-dollar rule.

### (band 6) (mfj.b6.base) — The band's base amount
Status: **MATCH**

Model: The schedule gives '18,252 plus 6.85%'.

### The tax is (mfj.b6.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: Base plus product matches the band 6 schedule entry.

### (band 7) (mfj.b7.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: The schedule says 'of the excess over 2,155,350'.

### (band 7) (mfj.b7.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 7) (mfj.b7.excess) by 965/10000 (ny.rs.b7.rate), rounded to the nearest multiple of $1 (half up).

Model: The 9.65% rate matches. No rounding is stated in the text given.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the rate schedule section, do not carry the whole-dollar rule.

### (band 7) (mfj.b7.base) — The band's base amount
Status: **MATCH**

Model: The schedule gives '143,754 plus 9.65%'.

### The tax is (mfj.b7.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: Base plus product matches the band 7 schedule entry.

### (band 8) (mfj.b8.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: The schedule says 'of the excess over 5,000,000'.

### (band 8) (mfj.b8.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 8) (mfj.b8.excess) by 103/1000 (ny.rs.b8.rate), rounded to the nearest multiple of $1 (half up).

Model: The 10.3% rate matches. No rounding is stated in the text given.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the rate schedule section, do not carry the whole-dollar rule.

### (band 8) (mfj.b8.base) — The band's base amount
Status: **MATCH**

Model: The schedule gives '418,263 plus 10.3%'.

### The tax is (mfj.b8.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: Base plus product matches the band 8 schedule entry.

### (band 9) (mfj.b9.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: The schedule says 'of the excess over 25,000,000'.

### (band 9) (mfj.b9.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 9) (mfj.b9.excess) by 109/1000 (ny.rs.b9.rate), rounded to the nearest multiple of $1 (half up).

Model: The 10.9% rate matches. No rounding is stated in the text given.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the rate schedule section, do not carry the whole-dollar rule.

### (band 9) (mfj.b9.base) — The band's base amount
Status: **MATCH**

Model: The schedule gives '2,478,263 plus 10.9%'.

### The tax is (mfj.b9.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: Base plus product matches the band 9 schedule entry.

### The tax is (mfj.result) — Married filing jointly and qualifying surviving spouse—filing status ② and ⑤: the tax for
Status: **MATCH**

Model: The band selection follows the MFJ/QSS 'over / but not over' bounds: 17,150, 23,600, 27,900, 161,550, 323,200, 2,155,350, 5,000,000 and 25,000,000.

### (band 1) (hoh.b1.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: HOH band 1 is '4% of line 38'. Line 38 minus $0 equals line 38.

### (band 1) (hoh.b1.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 1) (hoh.b1.excess) by 4% (0.04) (ny.rs.b1.rate), rounded to the nearest multiple of $1 (half up).

Model: The 4% rate matches. No rounding is stated in the text given.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the rate schedule section, do not carry the whole-dollar rule.

### (band 1) (hoh.b1.base) — The band's base amount
Status: **MATCH**

Model: The first band has no base amount, so the base is $0.

### The tax is (hoh.b1.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: Base of $0 plus 4% of line 38 matches.

### (band 2) (hoh.b2.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: The schedule says 'of the excess over $12,800'.

### (band 2) (hoh.b2.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 2) (hoh.b2.excess) by 45/1000 (ny.rs.b2.rate), rounded to the nearest multiple of $1 (half up).

Model: The 4.5% rate matches. No rounding is stated in the text given.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the rate schedule section, do not carry the whole-dollar rule.

### (band 2) (hoh.b2.base) — The band's base amount
Status: **MATCH**

Model: The schedule gives '$512 plus 4.5%'.

### The tax is (hoh.b2.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: Base plus product matches the band 2 schedule entry.

### (band 3) (hoh.b3.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: The schedule says 'of the excess over 17,650'.

### (band 3) (hoh.b3.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 3) (hoh.b3.excess) by 525/10000 (ny.rs.b3.rate), rounded to the nearest multiple of $1 (half up).

Model: The 5.25% rate matches. No rounding is stated in the text given.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the rate schedule section, do not carry the whole-dollar rule.

### (band 3) (hoh.b3.base) — The band's base amount
Status: **MATCH**

Model: The schedule gives '730 plus 5.25%'.

### The tax is (hoh.b3.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: Base plus product matches the band 3 schedule entry.

### (band 4) (hoh.b4.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: The schedule says 'of the excess over 20,900'.

### (band 4) (hoh.b4.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 4) (hoh.b4.excess) by 55/1000 (ny.rs.b4.rate), rounded to the nearest multiple of $1 (half up).

Model: The 5.5% rate matches. No rounding is stated in the text given.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the rate schedule section, do not carry the whole-dollar rule.

### (band 4) (hoh.b4.base) — The band's base amount
Status: **MATCH**

Model: The schedule gives '901 plus 5.5%'.

### The tax is (hoh.b4.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: Base plus product matches the band 4 schedule entry.

### (band 5) (hoh.b5.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: The schedule says 'of the excess over 107,650'.

### (band 5) (hoh.b5.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 5) (hoh.b5.excess) by 6% (0.06) (ny.rs.b5.rate), rounded to the nearest multiple of $1 (half up).

Model: The 6% rate matches. No rounding is stated in the text given.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the rate schedule section, do not carry the whole-dollar rule.

### (band 5) (hoh.b5.base) — The band's base amount
Status: **MATCH**

Model: The schedule gives '5,672 plus 6%'.

### The tax is (hoh.b5.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: Base plus product matches the band 5 schedule entry.

### (band 6) (hoh.b6.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: The schedule says 'of the excess over 269,300'.

### (band 6) (hoh.b6.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 6) (hoh.b6.excess) by 685/10000 (ny.rs.b6.rate), rounded to the nearest multiple of $1 (half up).

Model: The 6.85% rate matches. No rounding is stated in the text given.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the rate schedule section, do not carry the whole-dollar rule.

### (band 6) (hoh.b6.base) — The band's base amount
Status: **MATCH**

Model: The schedule gives '15,371 plus 6.85%'.

### The tax is (hoh.b6.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: Base plus product matches the band 6 schedule entry.

### (band 7) (hoh.b7.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: The schedule says 'of the excess over 1,616,450'.

### (band 7) (hoh.b7.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 7) (hoh.b7.excess) by 965/10000 (ny.rs.b7.rate), rounded to the nearest multiple of $1 (half up).

Model: The 9.65% rate matches. No rounding is stated in the text given.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the rate schedule section, do not carry the whole-dollar rule.

### (band 7) (hoh.b7.base) — The band's base amount
Status: **MATCH**

Model: The schedule gives '107,651 plus 9.65%'.

### The tax is (hoh.b7.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: Base plus product matches the band 7 schedule entry.

### (band 8) (hoh.b8.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: The schedule says 'of the excess over 5,000,000'.

### (band 8) (hoh.b8.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 8) (hoh.b8.excess) by 103/1000 (ny.rs.b8.rate), rounded to the nearest multiple of $1 (half up).

Model: The 10.3% rate matches. No rounding is stated in the text given.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the rate schedule section, do not carry the whole-dollar rule.

### (band 8) (hoh.b8.base) — The band's base amount
Status: **MATCH**

Model: The schedule gives '434,163 plus 10.3%'.

### The tax is (hoh.b8.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: Base plus product matches the band 8 schedule entry.

### (band 9) (hoh.b9.excess) — The amount over the band's lower bound (the excess over)
Status: **MATCH**

Model: The schedule says 'of the excess over 25,000,000'.

### (band 9) (hoh.b9.product) — Multiply the excess by the band's rate, rounded to the whole dollar
Status: **UNCLEAR**

Restated: Multiply column (band 9) (hoh.b9.excess) by 109/1000 (ny.rs.b9.rate), rounded to the nearest multiple of $1 (half up).

Model: The 10.9% rate matches. No rounding is stated in the text given.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. The schedule's rate and band are as printed (the reviewer confirms the rate); its pages, the rate schedule section, do not carry the whole-dollar rule.

### (band 9) (hoh.b9.base) — The band's base amount
Status: **MATCH**

Model: The schedule gives '2,494,163 plus 10.9%'.

### The tax is (hoh.b9.tax) — The base amount plus the rate times the excess
Status: **MATCH**

Model: Base plus product matches the band 9 schedule entry.

### The tax is (hoh.result) — Head of household—filing status ④: the tax for the band that holds the amount
Status: **MATCH**

Model: The band selection follows the HOH 'over / but not over' bounds: 12,800, 17,650, 20,900, 107,650, 269,300, 1,616,450, 5,000,000 and 25,000,000.

### The tax is (tax) — The tax from the schedule for the filing status
Status: **MATCH**

Model: Statuses ② and ⑤ use the MFJ/QSS schedule, ① and ③ use the single/MFS schedule, and ④ uses the HOH schedule, as the headings state. The text also says to use the tax computation instead when line 33 is 'more than $107,650'; that redirect sits outside the schedule's own computation.

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| (line 38) | 8717bf74f48454bf59c9aef5e6d2a5405ff8b98243e8190d75919270a773df2e |
| (band 1) (single.b1.excess) | 04bcff0b659af51af0a360000b6bfb503e294daf6f2d391e359031e2280dc1fd |
| (band 1) (single.b1.product) | 64835fcbd1c546f293daeca9431c38b9fdd737719f3c811627feafac864542e9 |
| (band 1) (single.b1.base) | 50ddd23fcf691eac45e142c40b953b4f728d65746d3a5c7b7c847e5cdaca7896 |
| The tax is (single.b1.tax) | ed53d6833716f50e48d23fe72291baff0ca582f90e21ebdc6e3c2e247c077dd8 |
| (band 2) (single.b2.excess) | de8a814c622785f9845a549bc0c4b5f614a42aaa4d5b089f8f7770c7cbe05741 |
| (band 2) (single.b2.product) | 98a7106325e036c7d42e5200b186bcf3e058b1707c8ae9cde75d3183cca2c17e |
| (band 2) (single.b2.base) | 5a5070de281e400877024a8e1fea596d91f4d0ee21605dfb3021470040052fe3 |
| The tax is (single.b2.tax) | eeaf918781cd3c63bbbe437dbd94f080ed297ce99b7f4b559d4a9ad63a2d3e31 |
| (band 3) (single.b3.excess) | 9c4558e8de1b7ebff5a918d5feff4da36e986d44f9c43678963c998db075408b |
| (band 3) (single.b3.product) | 4f2a30b2964a40feb3d2a622be26bb052904efd87efa2aa5a379de71251d26f0 |
| (band 3) (single.b3.base) | b0a353e21e4e7d61ddadaf375ab82cb79675b8c803cb4f8024d399e852eea2e6 |
| The tax is (single.b3.tax) | 9c627e4d5f9571f33f821a4789fcbc7b8025eff7a2bbde732a18d928f7c53483 |
| (band 4) (single.b4.excess) | b068ee3b6bd1fbb9e027cb11bb9edd60e963c2face0d8106a8377615d5165cde |
| (band 4) (single.b4.product) | 2b6599dc27a4bdd3c87d17e6b568a491a8b1135efda3a0259ff5494ba6f21989 |
| (band 4) (single.b4.base) | 7d9b99e9ce6deb2d906d09d8990f93d48a55418a145cab28b3a97c9ed9ce0ee9 |
| The tax is (single.b4.tax) | d14765626255d3e14c5384c09976390406d719fde022624891914442a36b5e9c |
| (band 5) (single.b5.excess) | d8a70f250db11b8d1c0c1366daea66140f9e30d30978b917a86a6de07b5f8fc9 |
| (band 5) (single.b5.product) | f62a12d01e274439fed086190d057983ae4387f48354926f21642d3e828085ce |
| (band 5) (single.b5.base) | d3e9721a6252bb0029ae2ed1d09dfabea3368582cb05fee1bd6ac51cbb6ff715 |
| The tax is (single.b5.tax) | d79a0ca210dcaded926dd94b732f0b54f0054bc665713a0f4e50cec3abcd2051 |
| (band 6) (single.b6.excess) | 2c81cf2c560b2923250d2f49d23d4fd6c5c7f9f7ca33d4a8b6307b531db23194 |
| (band 6) (single.b6.product) | 1537928e1c82e9edfe286db911486b27fd4eaa07265bfa853a1993bffec4ca15 |
| (band 6) (single.b6.base) | d24f5830f74ff6ed21d0b12cc9e976554d47c968fa35e1e94e59a0f38bc52621 |
| The tax is (single.b6.tax) | 0965ddac9f918560a8be2aef72d109ebd93f9a56b3b2b5038009a962511afc2b |
| (band 7) (single.b7.excess) | eac4ca5392c5e847024230e4817b5b02f8c512d7b3657ff524ff7289f32580fb |
| (band 7) (single.b7.product) | 901bd2e2b7229f9bb544ff486a03aa83cb582fa8e73354f4c43cefa35dad41c3 |
| (band 7) (single.b7.base) | d77f4e1d3b5335c7e7834f5b838fb113a0df775ce8205ee033ee841a7b7bb51d |
| The tax is (single.b7.tax) | 4c811686817373028e8f4bcc6ff2bfbf77a9c96c4f510eac5d939c22ba7bd960 |
| (band 8) (single.b8.excess) | a67b3a3c20c24b0350327e15288534860491ea78c868726b767873b247b80144 |
| (band 8) (single.b8.product) | 9b525cd37b34a29aed577dad90e767ee110e45dc6163b06b32eb3429679336c5 |
| (band 8) (single.b8.base) | 89f9042c7fd067888ebb1693b40841a65e2bdf2bbcc5f9d66d5a2cc2a06235e1 |
| The tax is (single.b8.tax) | 38985425d7d31b7029303a3d8ce3cec36f4899faff6b3e8464ce832c803e7e38 |
| (band 9) (single.b9.excess) | fb3b6122e3327de34e3caf08b268f22c9451841750318f8865de7fe3d4e3dedc |
| (band 9) (single.b9.product) | 274ca7a439bc40271762db51b213dffdd490aca2a9fa79951e70baf21511a920 |
| (band 9) (single.b9.base) | 3d2fc6aaa261866d95f6d764a56dda426582bb299d3e2665427e2914a1344ff8 |
| The tax is (single.b9.tax) | 4ded06c5eaebfaa91db86beb0f5a49ea58fc5c78d1c3ace61c6a06aad7e0d029 |
| The tax is (single.result) | bb4890ac3994af7ee73904956dcb82b2030737e9e974b80884280171df854aa8 |
| (band 1) (mfj.b1.excess) | 5bf2a5c2cf26d29d79a19c77d62f1a1ca46dccf30cc53102d4e027376c5ec47a |
| (band 1) (mfj.b1.product) | 64835fcbd1c546f293daeca9431c38b9fdd737719f3c811627feafac864542e9 |
| (band 1) (mfj.b1.base) | bfba967dc9f26ac452eb9cd5d1a94b028efa5f3bdf1214dddd810f1314f00092 |
| The tax is (mfj.b1.tax) | 6ba1530c10f1877c39946c8cf2387c91601d39fad028c9154572a189095dca8d |
| (band 2) (mfj.b2.excess) | adeccce5cffc67d857a86a34f7c0744694ba4246c4ede0833dc1f9169191d4b2 |
| (band 2) (mfj.b2.product) | 98a7106325e036c7d42e5200b186bcf3e058b1707c8ae9cde75d3183cca2c17e |
| (band 2) (mfj.b2.base) | ec7ed415c8e71d9e77fd456d07189e144a0509d81081e5a982179de32950ba27 |
| The tax is (mfj.b2.tax) | b912962101d7db682b2a5d30b3c8578b85799d539b504a3f0ab8ba79c2a3cb1f |
| (band 3) (mfj.b3.excess) | 19f5881da2ee1a3a42bbbc7695e3eb8dd5fadd0ac5d26ad591dfedb2f780aedf |
| (band 3) (mfj.b3.product) | 4f2a30b2964a40feb3d2a622be26bb052904efd87efa2aa5a379de71251d26f0 |
| (band 3) (mfj.b3.base) | edbbb774ababbf118601282625ea13717f5bccbc0570ff5a5116472f92e8ffe4 |
| The tax is (mfj.b3.tax) | b6e3366d2cae4d1b395fba9ab88e38a2aa3efaaf59eee1022f779acda3a5813f |
| (band 4) (mfj.b4.excess) | 15f16fd3814e197453e40b122122470e2923cadb16e124850c0c14dc6f522fd3 |
| (band 4) (mfj.b4.product) | 2b6599dc27a4bdd3c87d17e6b568a491a8b1135efda3a0259ff5494ba6f21989 |
| (band 4) (mfj.b4.base) | 8130a29f9030609f3b76840916ab976dcfd7ac42007826cdcdc260febf2ece74 |
| The tax is (mfj.b4.tax) | e65fe3bc0dce5c659ec1fca866dc6cd6039449a1c97e3fc6fb3949a627c799cb |
| (band 5) (mfj.b5.excess) | 278e224db8bb05d9f6689d9452ca39a799f4846d88ec1809abca2c7031ebd3fd |
| (band 5) (mfj.b5.product) | f62a12d01e274439fed086190d057983ae4387f48354926f21642d3e828085ce |
| (band 5) (mfj.b5.base) | ab4cb9c3cf1f6d2f8d8d4585b1ed23ef218db93d4d639faa0df23f752b013c7e |
| The tax is (mfj.b5.tax) | d681001040f90ca91a3c2a7896b56f5ce9cec053aa311706f121db3ee51eac6c |
| (band 6) (mfj.b6.excess) | 2a9c428a43d1169162fa1f93896626d1091a3cbfe670cfc74981a507e85238ab |
| (band 6) (mfj.b6.product) | 1537928e1c82e9edfe286db911486b27fd4eaa07265bfa853a1993bffec4ca15 |
| (band 6) (mfj.b6.base) | 5a16c70e2b71155b5ac818374aa15cc52db2a0d2e1ec3711a84a2d0ef1a7d2ef |
| The tax is (mfj.b6.tax) | 976f85a2f91c407a82911dcf4f5e27617e145342e7e342c7ebca53083008ee03 |
| (band 7) (mfj.b7.excess) | 8a10c8128a5f5dc885628377d5570b6af8ebe26f2f273930ba3cb3b481f2e2b7 |
| (band 7) (mfj.b7.product) | 901bd2e2b7229f9bb544ff486a03aa83cb582fa8e73354f4c43cefa35dad41c3 |
| (band 7) (mfj.b7.base) | 0c49108605c3171499cc637f403a7ef1c3e605913b6faea4fa5248bdfa194deb |
| The tax is (mfj.b7.tax) | b6e0b7b677c016c92b14606480f7fcaa8f6a629552341941ea4751f0b74f21da |
| (band 8) (mfj.b8.excess) | 09b6d6c19baafead5a46fa00aa96bb934fd04d64ea77836c677d16a7b0468ae8 |
| (band 8) (mfj.b8.product) | 9b525cd37b34a29aed577dad90e767ee110e45dc6163b06b32eb3429679336c5 |
| (band 8) (mfj.b8.base) | 349ddee0d2d5ca69cc7c8f02f99a8ecccf6320a5c2ff60ae41435df881cdbcd0 |
| The tax is (mfj.b8.tax) | 45b190e87cb7fadec1a14da1ee30b5390a3e9d8fd0f19a4972d7defe7979c298 |
| (band 9) (mfj.b9.excess) | 03b0d5f8f9fa703ab45bbdf7fac7ac542c618dc1614041181f6fe200f4c33326 |
| (band 9) (mfj.b9.product) | 274ca7a439bc40271762db51b213dffdd490aca2a9fa79951e70baf21511a920 |
| (band 9) (mfj.b9.base) | 6253f30d3be726e0da5dd4e7a9f510a7cdbc45e001bf493b5631771b3ce9ba94 |
| The tax is (mfj.b9.tax) | a15412228606c1b5552a49bb8a0db819aa93511f51c7f39f837071559bb0b3de |
| The tax is (mfj.result) | bb4890ac3994af7ee73904956dcb82b2030737e9e974b80884280171df854aa8 |
| (band 1) (hoh.b1.excess) | ba6e1e80ef7652bf623bc187f9357af8977a1ec7563e6382239938395a6ed7e8 |
| (band 1) (hoh.b1.product) | 64835fcbd1c546f293daeca9431c38b9fdd737719f3c811627feafac864542e9 |
| (band 1) (hoh.b1.base) | bccf1540bb82c52a9147bc9e8fb74481dd2bb7b817a60313dca83f93f6e9b172 |
| The tax is (hoh.b1.tax) | 85c243c997c67366c8d3b7e79d3221aa3feb847a0ee18ea972cdc0ff64a063ab |
| (band 2) (hoh.b2.excess) | c6bc906df8958d5a8553671007a0c5ecb4a73ee1b61c33b964d3c5003c0de9d7 |
| (band 2) (hoh.b2.product) | 98a7106325e036c7d42e5200b186bcf3e058b1707c8ae9cde75d3183cca2c17e |
| (band 2) (hoh.b2.base) | e9254b51687d14cf7babd3e324255c4495a9a96a574bb36e60374dd18ffee9f3 |
| The tax is (hoh.b2.tax) | f87f684bec08b3bedce3d232c4801e19403aa3d54c014adfb792257c20dfab2f |
| (band 3) (hoh.b3.excess) | 2a435c35a0bca80139ffa729832f3c15d4186255966cd32d2c81ec7436876303 |
| (band 3) (hoh.b3.product) | 4f2a30b2964a40feb3d2a622be26bb052904efd87efa2aa5a379de71251d26f0 |
| (band 3) (hoh.b3.base) | 28e5717d53fbaf1f5b4d0916b628b5f6d16b3fdf8034c0ca18ff794618ba235d |
| The tax is (hoh.b3.tax) | afbe0bbee18d4fad0856f0c64f3fdbca5ac7da49e2b8451130a87be28251e984 |
| (band 4) (hoh.b4.excess) | 94a11c80d73f6b28465f4f8fd42237d4df392b09c9abd7645a5c4c839f5a1433 |
| (band 4) (hoh.b4.product) | 2b6599dc27a4bdd3c87d17e6b568a491a8b1135efda3a0259ff5494ba6f21989 |
| (band 4) (hoh.b4.base) | 061947bd13e1ae052f56e3749b57d10c3e7a2bc910237ab26c022a8a06170bb4 |
| The tax is (hoh.b4.tax) | 56aa34a41b2867c1a268f23414ace557514de5d1acd2c5f5ee44570250f2844d |
| (band 5) (hoh.b5.excess) | dbc766d78fbf6328e635e98ce104245f8b82951e8578e9db980b4357aaf9f67f |
| (band 5) (hoh.b5.product) | f62a12d01e274439fed086190d057983ae4387f48354926f21642d3e828085ce |
| (band 5) (hoh.b5.base) | 8ee8cf6902a59c50d16d0187bea8735f97c82de42cfa857334bc6b4881fc1083 |
| The tax is (hoh.b5.tax) | b0544fbff9b10e16ff1be18883f189c07120faaccef3cfb711309aba59b9ac00 |
| (band 6) (hoh.b6.excess) | 82ad09acd14f38aa116773147f56448ae22fc5011f42bd3b1f07d6c9bf033379 |
| (band 6) (hoh.b6.product) | 1537928e1c82e9edfe286db911486b27fd4eaa07265bfa853a1993bffec4ca15 |
| (band 6) (hoh.b6.base) | 090d16215ebd16070ecf7675465ad8eb5104d3b8da63a2d66c0a2b53f09e7d24 |
| The tax is (hoh.b6.tax) | f342f09e9dcabe371ee4b315fce6dedccee9bf7382da27e6fbf6a4eaecea3375 |
| (band 7) (hoh.b7.excess) | 0b3e19168b9c4018606c387f67a0ee4a9f277af7e7ce9ccec7a4cfa9aae24a28 |
| (band 7) (hoh.b7.product) | 901bd2e2b7229f9bb544ff486a03aa83cb582fa8e73354f4c43cefa35dad41c3 |
| (band 7) (hoh.b7.base) | 167394f18949100d697b5d82dcf02d19fe33b7f3d6da7f35630abc2235737ac7 |
| The tax is (hoh.b7.tax) | eb9eae7af31f7a502ca508a6f266431b988783e872b0961285002d36c3fec059 |
| (band 8) (hoh.b8.excess) | 264160ff8a6dadd88e155dc3532098df416020fe9b77271f3f815033838fbf01 |
| (band 8) (hoh.b8.product) | 9b525cd37b34a29aed577dad90e767ee110e45dc6163b06b32eb3429679336c5 |
| (band 8) (hoh.b8.base) | cb7dc18d42a6eeb1bba8883672bb538ae3905671e4b91611b3a5a0d5c8dd25d5 |
| The tax is (hoh.b8.tax) | 15d3024cba6a49b4777766a83296ca18db6ea50e44152e03c59667e109d23d55 |
| (band 9) (hoh.b9.excess) | 53fdaf21f0dcef9efda3f27101e451545f1bfc3760a4fbfcf444ddbde40c652c |
| (band 9) (hoh.b9.product) | 274ca7a439bc40271762db51b213dffdd490aca2a9fa79951e70baf21511a920 |
| (band 9) (hoh.b9.base) | 32885a9b52e00309239f5c7181d4c0aa0f40b986b76b32f0d0cde674190c7089 |
| The tax is (hoh.b9.tax) | e0605507c936cfdb52c9183062e1190001109e1b2b05b6d9b0b3162a8e047d82 |
| The tax is (hoh.result) | bb4890ac3994af7ee73904956dcb82b2030737e9e974b80884280171df854aa8 |
| The tax is (tax) | 67dd14e62181ab75e3da3ca6f1280c9cee7fb6af9461f513d619d4bc3e9e3c03 |
| (rest of the document) | e93245fa311883b38850802b473ec4378d4fe5d1201a40befaeee0ba468eb14f |

## Raw response

```yaml
```yaml
lines:
  - key: "(line 38)"
    status: MATCH
    reason: "The schedule is keyed on 'If line 38 is:', so taking the taxable income on line 38 as the input matches."
  - key: "(band 1) (single.b1.excess)"
    status: MATCH
    reason: "Band 1 (single/MFS) is '4% of line 38'. Line 38 minus $0, floored at zero, equals line 38."
  - key: "(band 1) (single.b1.product)"
    status: UNCLEAR
    reason: "The schedule says '4% of line 38' and gives no rounding. The pages provided do not support rounding the product to the nearest dollar, half up."
  - key: "(band 1) (single.b1.base)"
    status: MATCH
    reason: "The first band has no base amount, only '4% of line 38', so the base is $0."
  - key: "The tax is (single.b1.tax)"
    status: MATCH
    reason: "Base of $0 plus 4% of line 38 is the band 1 tax."
  - key: "(band 2) (single.b2.excess)"
    status: MATCH
    reason: "The schedule says 'of the excess over $8,500'."
  - key: "(band 2) (single.b2.product)"
    status: UNCLEAR
    reason: "The 4.5% rate matches. The schedule states no rounding, so rounding to the nearest dollar, half up, cannot be confirmed from the text given."
  - key: "(band 2) (single.b2.base)"
    status: MATCH
    reason: "The schedule gives '$340 plus 4.5%'."
  - key: "The tax is (single.b2.tax)"
    status: MATCH
    reason: "Base plus product matches '$340 plus 4.5% of the excess over $8,500'."
  - key: "(band 3) (single.b3.excess)"
    status: MATCH
    reason: "The schedule says 'of the excess over 11,700'."
  - key: "(band 3) (single.b3.product)"
    status: UNCLEAR
    reason: "The 5.25% rate matches. No rounding is stated in the text given."
  - key: "(band 3) (single.b3.base)"
    status: MATCH
    reason: "The schedule gives '484 plus 5.25%'."
  - key: "The tax is (single.b3.tax)"
    status: MATCH
    reason: "Base plus product matches the band 3 schedule entry."
  - key: "(band 4) (single.b4.excess)"
    status: MATCH
    reason: "The schedule says 'of the excess over 13,900'."
  - key: "(band 4) (single.b4.product)"
    status: UNCLEAR
    reason: "The 5.5% rate matches. No rounding is stated in the text given."
  - key: "(band 4) (single.b4.base)"
    status: MATCH
    reason: "The schedule gives '600 plus 5.5%'."
  - key: "The tax is (single.b4.tax)"
    status: MATCH
    reason: "Base plus product matches the band 4 schedule entry."
  - key: "(band 5) (single.b5.excess)"
    status: MATCH
    reason: "The schedule says 'of the excess over 80,650'."
  - key: "(band 5) (single.b5.product)"
    status: UNCLEAR
    reason: "The 6% rate matches. No rounding is stated in the text given."
  - key: "(band 5) (single.b5.base)"
    status: MATCH
    reason: "The schedule gives '4,271 plus 6%'."
  - key: "The tax is (single.b5.tax)"
    status: MATCH
    reason: "Base plus product matches the band 5 schedule entry."
  - key: "(band 6) (single.b6.excess)"
    status: MATCH
    reason: "The schedule says 'of the excess over 215,400'."
  - key: "(band 6) (single.b6.product)"
    status: UNCLEAR
    reason: "The 6.85% rate matches. No rounding is stated in the text given."
  - key: "(band 6) (single.b6.base)"
    status: MATCH
    reason: "The schedule gives '12,356 plus 6.85%'."
  - key: "The tax is (single.b6.tax)"
    status: MATCH
    reason: "Base plus product matches the band 6 schedule entry."
  - key: "(band 7) (single.b7.excess)"
    status: MATCH
    reason: "The schedule says 'of the excess over 1,077,550'."
  - key: "(band 7) (single.b7.product)"
    status: UNCLEAR
    reason: "The 9.65% rate matches. No rounding is stated in the text given."
  - key: "(band 7) (single.b7.base)"
    status: MATCH
    reason: "The schedule gives '71,413 plus 9.65%'."
  - key: "The tax is (single.b7.tax)"
    status: MATCH
    reason: "Base plus product matches the band 7 schedule entry."
  - key: "(band 8) (single.b8.excess)"
    status: MATCH
    reason: "The schedule says 'of the excess over 5,000,000'."
  - key: "(band 8) (single.b8.product)"
    status: UNCLEAR
    reason: "The 10.3% rate matches. No rounding is stated in the text given."
  - key: "(band 8) (single.b8.base)"
    status: MATCH
    reason: "The schedule gives '449,929 plus 10.3%'."
  - key: "The tax is (single.b8.tax)"
    status: MATCH
    reason: "Base plus product matches the band 8 schedule entry."
  - key: "(band 9) (single.b9.excess)"
    status: MATCH
    reason: "The schedule says 'of the excess over 25,000,000'."
  - key: "(band 9) (single.b9.product)"
    status: UNCLEAR
    reason: "The 10.9% rate matches. No rounding is stated in the text given."
  - key: "(band 9) (single.b9.base)"
    status: MATCH
    reason: "The schedule gives '2,509,929 plus 10.9%'."
  - key: "The tax is (single.b9.tax)"
    status: MATCH
    reason: "Base plus product matches the band 9 schedule entry."
  - key: "The tax is (single.result)"
    status: MATCH
    reason: "The band selection follows the schedule's 'over / but not over' bounds for single and MFS: 8,500, 11,700, 13,900, 80,650, 215,400, 1,077,550, 5,000,000 and 25,000,000."
  - key: "(band 1) (mfj.b1.excess)"
    status: MATCH
    reason: "MFJ band 1 is '4% of line 38'. Line 38 minus $0 equals line 38."
  - key: "(band 1) (mfj.b1.product)"
    status: UNCLEAR
    reason: "The 4% rate matches. No rounding is stated in the text given."
  - key: "(band 1) (mfj.b1.base)"
    status: MATCH
    reason: "The first band has no base amount, so the base is $0."
  - key: "The tax is (mfj.b1.tax)"
    status: MATCH
    reason: "Base of $0 plus 4% of line 38 matches."
  - key: "(band 2) (mfj.b2.excess)"
    status: MATCH
    reason: "The schedule says 'of the excess over $17,150'."
  - key: "(band 2) (mfj.b2.product)"
    status: UNCLEAR
    reason: "The 4.5% rate matches. No rounding is stated in the text given."
  - key: "(band 2) (mfj.b2.base)"
    status: MATCH
    reason: "The schedule gives '$686 plus 4.5%'."
  - key: "The tax is (mfj.b2.tax)"
    status: MATCH
    reason: "Base plus product matches the band 2 schedule entry."
  - key: "(band 3) (mfj.b3.excess)"
    status: MATCH
    reason: "The schedule says 'of the excess over 23,600'."
  - key: "(band 3) (mfj.b3.product)"
    status: UNCLEAR
    reason: "The 5.25% rate matches. No rounding is stated in the text given."
  - key: "(band 3) (mfj.b3.base)"
    status: MATCH
    reason: "The schedule gives '976 plus 5.25%'."
  - key: "The tax is (mfj.b3.tax)"
    status: MATCH
    reason: "Base plus product matches the band 3 schedule entry."
  - key: "(band 4) (mfj.b4.excess)"
    status: MATCH
    reason: "The schedule says 'of the excess over 27,900'."
  - key: "(band 4) (mfj.b4.product)"
    status: UNCLEAR
    reason: "The 5.5% rate matches. No rounding is stated in the text given."
  - key: "(band 4) (mfj.b4.base)"
    status: MATCH
    reason: "The schedule gives '1,202 plus 5.5%'."
  - key: "The tax is (mfj.b4.tax)"
    status: MATCH
    reason: "Base plus product matches the band 4 schedule entry."
  - key: "(band 5) (mfj.b5.excess)"
    status: MATCH
    reason: "The schedule says 'of the excess over 161,550'."
  - key: "(band 5) (mfj.b5.product)"
    status: UNCLEAR
    reason: "The 6% rate matches. No rounding is stated in the text given."
  - key: "(band 5) (mfj.b5.base)"
    status: MATCH
    reason: "The schedule gives '8,553 plus 6%'."
  - key: "The tax is (mfj.b5.tax)"
    status: MATCH
    reason: "Base plus product matches the band 5 schedule entry."
  - key: "(band 6) (mfj.b6.excess)"
    status: MATCH
    reason: "The schedule says 'of the excess over 323,200'."
  - key: "(band 6) (mfj.b6.product)"
    status: UNCLEAR
    reason: "The 6.85% rate matches. No rounding is stated in the text given."
  - key: "(band 6) (mfj.b6.base)"
    status: MATCH
    reason: "The schedule gives '18,252 plus 6.85%'."
  - key: "The tax is (mfj.b6.tax)"
    status: MATCH
    reason: "Base plus product matches the band 6 schedule entry."
  - key: "(band 7) (mfj.b7.excess)"
    status: MATCH
    reason: "The schedule says 'of the excess over 2,155,350'."
  - key: "(band 7) (mfj.b7.product)"
    status: UNCLEAR
    reason: "The 9.65% rate matches. No rounding is stated in the text given."
  - key: "(band 7) (mfj.b7.base)"
    status: MATCH
    reason: "The schedule gives '143,754 plus 9.65%'."
  - key: "The tax is (mfj.b7.tax)"
    status: MATCH
    reason: "Base plus product matches the band 7 schedule entry."
  - key: "(band 8) (mfj.b8.excess)"
    status: MATCH
    reason: "The schedule says 'of the excess over 5,000,000'."
  - key: "(band 8) (mfj.b8.product)"
    status: UNCLEAR
    reason: "The 10.3% rate matches. No rounding is stated in the text given."
  - key: "(band 8) (mfj.b8.base)"
    status: MATCH
    reason: "The schedule gives '418,263 plus 10.3%'."
  - key: "The tax is (mfj.b8.tax)"
    status: MATCH
    reason: "Base plus product matches the band 8 schedule entry."
  - key: "(band 9) (mfj.b9.excess)"
    status: MATCH
    reason: "The schedule says 'of the excess over 25,000,000'."
  - key: "(band 9) (mfj.b9.product)"
    status: UNCLEAR
    reason: "The 10.9% rate matches. No rounding is stated in the text given."
  - key: "(band 9) (mfj.b9.base)"
    status: MATCH
    reason: "The schedule gives '2,478,263 plus 10.9%'."
  - key: "The tax is (mfj.b9.tax)"
    status: MATCH
    reason: "Base plus product matches the band 9 schedule entry."
  - key: "The tax is (mfj.result)"
    status: MATCH
    reason: "The band selection follows the MFJ/QSS 'over / but not over' bounds: 17,150, 23,600, 27,900, 161,550, 323,200, 2,155,350, 5,000,000 and 25,000,000."
  - key: "(band 1) (hoh.b1.excess)"
    status: MATCH
    reason: "HOH band 1 is '4% of line 38'. Line 38 minus $0 equals line 38."
  - key: "(band 1) (hoh.b1.product)"
    status: UNCLEAR
    reason: "The 4% rate matches. No rounding is stated in the text given."
  - key: "(band 1) (hoh.b1.base)"
    status: MATCH
    reason: "The first band has no base amount, so the base is $0."
  - key: "The tax is (hoh.b1.tax)"
    status: MATCH
    reason: "Base of $0 plus 4% of line 38 matches."
  - key: "(band 2) (hoh.b2.excess)"
    status: MATCH
    reason: "The schedule says 'of the excess over $12,800'."
  - key: "(band 2) (hoh.b2.product)"
    status: UNCLEAR
    reason: "The 4.5% rate matches. No rounding is stated in the text given."
  - key: "(band 2) (hoh.b2.base)"
    status: MATCH
    reason: "The schedule gives '$512 plus 4.5%'."
  - key: "The tax is (hoh.b2.tax)"
    status: MATCH
    reason: "Base plus product matches the band 2 schedule entry."
  - key: "(band 3) (hoh.b3.excess)"
    status: MATCH
    reason: "The schedule says 'of the excess over 17,650'."
  - key: "(band 3) (hoh.b3.product)"
    status: UNCLEAR
    reason: "The 5.25% rate matches. No rounding is stated in the text given."
  - key: "(band 3) (hoh.b3.base)"
    status: MATCH
    reason: "The schedule gives '730 plus 5.25%'."
  - key: "The tax is (hoh.b3.tax)"
    status: MATCH
    reason: "Base plus product matches the band 3 schedule entry."
  - key: "(band 4) (hoh.b4.excess)"
    status: MATCH
    reason: "The schedule says 'of the excess over 20,900'."
  - key: "(band 4) (hoh.b4.product)"
    status: UNCLEAR
    reason: "The 5.5% rate matches. No rounding is stated in the text given."
  - key: "(band 4) (hoh.b4.base)"
    status: MATCH
    reason: "The schedule gives '901 plus 5.5%'."
  - key: "The tax is (hoh.b4.tax)"
    status: MATCH
    reason: "Base plus product matches the band 4 schedule entry."
  - key: "(band 5) (hoh.b5.excess)"
    status: MATCH
    reason: "The schedule says 'of the excess over 107,650'."
  - key: "(band 5) (hoh.b5.product)"
    status: UNCLEAR
    reason: "The 6% rate matches. No rounding is stated in the text given."
  - key: "(band 5) (hoh.b5.base)"
    status: MATCH
    reason: "The schedule gives '5,672 plus 6%'."
  - key: "The tax is (hoh.b5.tax)"
    status: MATCH
    reason: "Base plus product matches the band 5 schedule entry."
  - key: "(band 6) (hoh.b6.excess)"
    status: MATCH
    reason: "The schedule says 'of the excess over 269,300'."
  - key: "(band 6) (hoh.b6.product)"
    status: UNCLEAR
    reason: "The 6.85% rate matches. No rounding is stated in the text given."
  - key: "(band 6) (hoh.b6.base)"
    status: MATCH
    reason: "The schedule gives '15,371 plus 6.85%'."
  - key: "The tax is (hoh.b6.tax)"
    status: MATCH
    reason: "Base plus product matches the band 6 schedule entry."
  - key: "(band 7) (hoh.b7.excess)"
    status: MATCH
    reason: "The schedule says 'of the excess over 1,616,450'."
  - key: "(band 7) (hoh.b7.product)"
    status: UNCLEAR
    reason: "The 9.65% rate matches. No rounding is stated in the text given."
  - key: "(band 7) (hoh.b7.base)"
    status: MATCH
    reason: "The schedule gives '107,651 plus 9.65%'."
  - key: "The tax is (hoh.b7.tax)"
    status: MATCH
    reason: "Base plus product matches the band 7 schedule entry."
  - key: "(band 8) (hoh.b8.excess)"
    status: MATCH
    reason: "The schedule says 'of the excess over 5,000,000'."
  - key: "(band 8) (hoh.b8.product)"
    status: UNCLEAR
    reason: "The 10.3% rate matches. No rounding is stated in the text given."
  - key: "(band 8) (hoh.b8.base)"
    status: MATCH
    reason: "The schedule gives '434,163 plus 10.3%'."
  - key: "The tax is (hoh.b8.tax)"
    status: MATCH
    reason: "Base plus product matches the band 8 schedule entry."
  - key: "(band 9) (hoh.b9.excess)"
    status: MATCH
    reason: "The schedule says 'of the excess over 25,000,000'."
  - key: "(band 9) (hoh.b9.product)"
    status: UNCLEAR
    reason: "The 10.9% rate matches. No rounding is stated in the text given."
  - key: "(band 9) (hoh.b9.base)"
    status: MATCH
    reason: "The schedule gives '2,494,163 plus 10.9%'."
  - key: "The tax is (hoh.b9.tax)"
    status: MATCH
    reason: "Base plus product matches the band 9 schedule entry."
  - key: "The tax is (hoh.result)"
    status: MATCH
    reason: "The band selection follows the HOH 'over / but not over' bounds: 12,800, 17,650, 20,900, 107,650, 269,300, 1,616,450, 5,000,000 and 25,000,000."
  - key: "The tax is (tax)"
    status: MATCH
    reason: "Statuses ② and ⑤ use the MFJ/QSS schedule, ① and ③ use the single/MFS schedule, and ④ uses the HOH schedule, as the headings state. The text also says to use the tax computation instead when line 33 is 'more than $107,650'; that redirect sits outside the schedule's own computation."
```
```
