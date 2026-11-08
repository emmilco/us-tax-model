# Render comparison — div

The rendered English of every printed line of `Form 1099-DIV — distribution components and scope screening` (`rendered/2025/div.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| line-scoped reviews | 1 (latest 2026-11-07); see Line-scoped reviews |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 1778c4ca6275720af58f1a3ee8f80e2626e709f958faccda1dc7f7ab98a04116 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | bb04e5c4028849b3e76ebf138151c7dd3ffde5befd99506428206e6b1b32cf77 |
| lines judged | 39 |
| match / mismatch / unclear / missing | 39 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1099div | January 2024 (continuous-use form) | 1, 2, 3, 4, 5, 6 | whole document | 833d93e5f2d0bfcc8c9d720c0e8cb8e623cd2c6a8ee25f364f1f69f49fa490e3 | 5 | 617419bd079b1520174ceca8549065c9e4001f2b06a16d1425c5469bbe49fa3d |
| i1040sd | 2025; printed date 2025-12-11 | 8, 11 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 8, 11 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| i1040sb | TY2025; printed April 23, 2025 | 1, 2, 3 | whole document | 2bf62267574473b36fd9a69b6e0837ef74d72ac7d5dcbf1d26e7047d099f1e05 | 1, 2, 3 | 0d38b25d416cb650ef264faf8c1f118dfa4666f3949fbba7120f8c04d4e6914e |
| f8995 | 2025; created 2025-09-12 | 1 | whole document | 49922587df3bd093e24470f5b42d0e3382ef8f5210b3cedccb02ccb864f2f65a | - | 8e2e78d7610e1d45e93c10c8b03f9026d46a1166678c6ed93f852569c382f346 |
| i8995 | 2025; printed date 2026-01-26 | 3, 4 | pages named by another document's citation | 96284eaad2fe5ec324de9fd4335cea9ea3260e66ff1d8b1725c1cff7fbe1ddc2 | 3, 4 | 6671a64ba0011f89e03eb5985954073dcd984b3f346495182916b0ecaa42ec1a |

## Lines

### box2b — Unrecaptured section 1250 gain, box 2b
Status: **MATCH**

Model: Direct input of box 2b, "Unrecap. Sec. 1250 gain", described as "the portion of the amount in box 2a that is unrecaptured section 1250 gain".

### box2c — Section 1202 gain, box 2c
Status: **MATCH**

Model: Direct input of box 2c, "Section 1202 gain".

### box2d — Collectibles (28%) gain, box 2d
Status: **MATCH**

Model: Direct input of box 2d, "Collectibles (28%) gain".

### box2e — Section 897 ordinary dividends, box 2e
Status: **MATCH**

Model: Direct input of box 2e, "Section 897 ordinary dividends".

### box2f — Section 897 capital gain, box 2f
Status: **MATCH**

Model: Direct input of box 2f, "Section 897 capital gain".

### box3 — Nondividend distributions/return of capital, box 3
Status: **MATCH**

Model: Direct input of box 3, "Nondividend distributions", which "Shows a return of capital".

### box9 — Cash liquidation distributions, box 9
Status: **MATCH**

Model: Direct input of box 9, "Cash liquidation distributions".

### box10 — Noncash liquidation distributions, box 10
Status: **MATCH**

Model: Direct input of box 10, "Noncash liquidation distributions".

### box12 — Exempt-interest dividends, box 12
Status: **MATCH**

Model: Direct input of box 12, "Exempt-interest dividends". The note that box 13 is already included agrees with the box 13 instruction: "This amount is included in box 12."

### box13 — Specified private activity bond interest dividends, box 13
Status: **MATCH**

Model: Direct input of box 13, which "Shows exempt-interest dividends subject to the alternative minimum tax".

### basis_reconciled — For box 3, have basis reductions been applied to records with no distribution exceeding ba
Status: **MATCH**

Model: This yes/no input screens the box 3 rule: the distribution "reduces your basis and is not taxable", and any excess over basis "is taxable to you as capital gain". The program refuses the cases it does not handle.

### box1a — Amount from sb.ordinary_dividends_if_dividends
Status: **MATCH**

Model: Box 1a 'Shows total ordinary dividends that are taxable.' The restatement takes the total ordinary dividends from box 1a when the filer received dividends, and zero otherwise.
Reviewed in: pass cc1da444533f

### box1b — Amount from f1040.line3a_if_ordinary
Status: **MATCH**

Model: Box 1b 'Shows the portion of the amount in box 1a that may be eligible for reduced capital gains rates. See the Instructions for Form 1040 for how to determine this amount.' Using the Form 1040 line 3a total after the line 3a exceptions follows that pointer and is still a portion of box 1a.
Reviewed in: pass cc1da444533f

### box2a — Amount from sd.distributions_if_dividends
Status: **MATCH**

Model: Box 2a 'Shows total capital gain distributions.' The restatement takes that amount when the filer received distributions, and zero otherwise.
Reviewed in: pass cc1da444533f

### box5 — Amount from qbi.dividends_if_ordinary
Status: **MATCH**

Model: Box 5 'Shows the portion of the amount in box 1a that may be eligible for the 20% qualified business income deduction.' The i8995 holding-period and obligated-payment conditions ('held for more than 45 days and for which the payment isn't obligated to someone else') support the confirmed input.
Reviewed in: pass cc1da444533f

### section1202 — Section 1202 distribution present
Status: **MATCH**

Model: Box 2c is section 1202 gain that 'may be subject to an exclusion.' The Schedule D instructions require Form 8949 code 'Q' and a Form 6251 line 13 entry, and the refusal names both as outside scope.
Reviewed in: pass cc1da444533f

### amt — Specified private activity bond dividends present
Status: **MATCH**

Model: Box 13 'Shows exempt-interest dividends subject to the alternative minimum tax... See the Instructions for Form 6251.' A positive box 13 amount correctly triggers the Form 6251 refusal.
Reviewed in: pass cc1da444533f

### unsupported — Unsupported section 897, liquidation or unreconciled basis/excess distribution
Status: **MATCH**

Model: Boxes 2e and 2f (section 897), boxes 9 and 10 (liquidation distributions) and box 3 return of capital where basis is not reconciled ('Any amount received in excess of your basis is taxable to you as capital gain') need treatment outside scope. The refusal names that treatment. The 'and' binds only to the box 3 condition, as intended.
Reviewed in: pass cc1da444533f

### bad_special — A gain component exceeds total capital gain distributions
Status: **MATCH**

Model: Boxes 2b, 2c and 2d each show 'the portion of the amount in box 2a.' They describe distinct gain types (real property, small business stock, collectibles), so neither any one of them nor their total can exceed box 2a.
Reviewed in: pass cc1da444533f

### screen — Zero only after distribution scope checks
Status: **MATCH**

Model: This is a $0 screening value whose refusals name the excluded cases: section 1202, Form 6251, section 897 and liquidation distributions, unreconciled basis, and inconsistent component totals.
Reviewed in: pass cc1da444533f

### bad_components — Qualified or section 199A dividends exceed ordinary dividends
Status: **MATCH**

Model: Box 1b and box 5 are each described as 'the portion of the amount in box 1a.' Qualified dividends (no more than box 1b) or section 199A dividends that exceed box 1a are therefore inconsistent.
Reviewed in: pass cc1da444533f

### special_total — Total special capital-gain distribution components
Status: **MATCH**

Model: The restatement adds the box 2b, 2c and 2d components, each of which is a portion of box 2a, for the consistency check.
Reviewed in: pass cc1da444533f

### any — In 2025, did you (or your spouse) receive any dividends or other distributions from a comp
Status: **MATCH**

Model: This is a scope question about whether the filer received any dividends or distributions. It covers the box 1a through box 13 distribution types and nominee amounts, consistent with the form and the Schedule B instructions.
Reviewed in: pass cc1da444533f

### has_ordinary — Ordinary dividends (box 1a) are above zero
Status: **MATCH**

Model: The test is box 1a above zero, as labeled.
Reviewed in: pass cc1da444533f

### has_capital_gain — Capital gain distributions (box 2a) are above zero
Status: **MATCH**

Model: The test is box 2a above zero, as labeled.
Reviewed in: pass cc1da444533f

### has_return_of_capital — Nondividend distributions (box 3) are above zero
Status: **MATCH**

Model: The test is box 3 above zero, as labeled.
Reviewed in: pass cc1da444533f

### zero — No amount in a box whose condition does not hold
Status: **MATCH**

Model: The program enters $0 for a box whose gating condition does not hold.
Reviewed in: pass cc1da444533f

### no — No answer needed without nondividend distributions (box 3)
Status: **MATCH**

Model: The program enters false when there is no box 3 amount, so no basis question needs an answer.
Reviewed in: pass cc1da444533f

### box2b_if_capital_gain — Unrecaptured section 1250 gain, box 2b, when capital gain distributions (box 2a) are above
Status: **MATCH**

Model: Box 2b is 'the portion of the amount in box 2a,' so gating it on box 2a being above zero loses nothing.
Reviewed in: pass cc1da444533f

### box2c_if_capital_gain — Section 1202 gain, box 2c, when capital gain distributions (box 2a) are above zero; zero o
Status: **MATCH**

Model: Box 2c is 'the portion of the amount in box 2a,' so gating it on box 2a being above zero loses nothing.
Reviewed in: pass cc1da444533f

### box2d_if_capital_gain — Collectibles (28%) gain, box 2d, when capital gain distributions (box 2a) are above zero;
Status: **MATCH**

Model: Box 2d is 'the portion of the amount in box 2a,' so gating it on box 2a being above zero loses nothing.
Reviewed in: pass cc1da444533f

### box2f_if_capital_gain — Section 897 capital gain, box 2f, when capital gain distributions (box 2a) are above zero;
Status: **MATCH**

Model: Box 2f 'Shows the portion of the amount in box 2a that is section 897 gain,' so gating it on box 2a being above zero loses nothing.
Reviewed in: pass cc1da444533f

### box2e_if_ordinary — Section 897 ordinary dividends, box 2e, when ordinary dividends (box 1a) are above zero; z
Status: **MATCH**

Model: Box 2e 'Shows the portion of the amount in box 1a,' so gating it on box 1a being above zero loses nothing.
Reviewed in: pass cc1da444533f

### box3_if_dividends — Nondividend distributions/return of capital, box 3, when you or your spouse received divid
Status: **MATCH**

Model: Box 3 nondividend distributions are taken when the filer received distributions, and zero otherwise.
Reviewed in: pass cc1da444533f

### box9_if_dividends — Cash liquidation distributions, box 9, when you or your spouse received dividends or other
Status: **MATCH**

Model: Box 9 cash liquidation distributions are taken when the filer received distributions, and zero otherwise.
Reviewed in: pass cc1da444533f

### box10_if_dividends — Noncash liquidation distributions, box 10, when you or your spouse received dividends or o
Status: **MATCH**

Model: Box 10 noncash liquidation distributions are taken when the filer received distributions, and zero otherwise.
Reviewed in: pass cc1da444533f

### box12_if_dividends — Exempt-interest dividends, box 12, when you or your spouse received dividends or other dis
Status: **MATCH**

Model: Box 12 exempt-interest dividends are taken when the filer received distributions, and zero otherwise. The input correctly notes that box 13 'is included in box 12.'
Reviewed in: pass cc1da444533f

### box13_if_dividends — Specified private activity bond interest dividends, box 13, when you or your spouse receiv
Status: **MATCH**

Model: Box 13 specified private activity bond interest dividends are taken when the filer received distributions, and zero otherwise.
Reviewed in: pass cc1da444533f

### basis_reconciled_if_return_of_capital — For box 3, basis reductions applied, when nondividend distributions (box 3) are above zero
Status: **MATCH**

Model: Box 3 'reduces your basis and is not taxable' only 'To the extent of your cost (or other basis).' Asking whether basis has been reduced with no distribution exceeding basis is the right question when box 3 is above zero; otherwise the answer is false.
Reviewed in: pass cc1da444533f

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| box2b | e4386aece57b512175c8c8a7db7ba82c9ab377fbd9251adb3ffec4695677cbe1 |
| box2c | bb41837e1a267c4bb4e21c77f1f9da9d7a14e7108cc19e1a17be7d990fb06ff9 |
| box2d | b541f3b20e9b749f82cca8ff52efb1f10884e1dac2880f78026700515d6e7218 |
| box2e | 84ba23ee4d0a07b100becc2f0740ee5a885bc519aa50015c880f08eb026a47ad |
| box2f | 31bc662d32fa192b993bb7775d73c13f8364dffad53a37d6ece5b3761e96cf2e |
| box3 | e823aced51aca020a861fa2d5bf7c241a7229a82d5abdad82dd6a3228000f3fe |
| box9 | 26cf78aaa08edb24c983bbbe95d20157ab17ecc82530a360cc7f5c7a7f34f6fd |
| box10 | 7ec74a0d1a27054678588be8f5bf9738e101e162c05eaa736254a8c6757f7625 |
| box12 | c44a263712c56dc638fc6fd0d9cbce69558783a492154d3345eb18595528d2e6 |
| box13 | 184ff288b4b9d7fe14588a16572d762bc3cb7bfc2f8a1dfa8fa37a01b6d2faa5 |
| basis_reconciled | bc9ddebd4a68e1092b9e8f28bf92c8ae35f71aec15f61dd6eca2454e1fe83dba |
| box1a | c2ca6a18c1f899686e4a4b355ff907977cf334ee2f801df782df55295cb0856c |
| box1b | 0e7b7fec792f5764cc28b07d9330d43209f75400bf712a71f8a40b1c0eb68d58 |
| box2a | 5a1ed9c77232175bac9afb483c02ec3e66c79a3df2bfa1745aad5418d70d6841 |
| box5 | 8fd5282ce32ec47c7ac709abf5d672d08577dc833de40390585d4f1299554c66 |
| section1202 | 6b00f5ce1417288f84206cd1427b951e737f4fa1de00dd4d58e754cebddc4b25 |
| amt | 53f7de60dd06c05757c33966960523a74dc66290c0da7ee42d0ca06ec9e30c86 |
| unsupported | e65dd4d5cf8c0cd583e2e07b468c2f5ba702c09c6456dc46805919a601b81775 |
| bad_special | 0d2b26e1982c3ec085af815b03fc7db7b65d7ecfff6afb2a44bae484290a5a88 |
| screen | 5ed163c00b4965b8019f9ffea9148f90185cfd840659bfe2882f524ec22d6c99 |
| bad_components | 78a765130805bb1c24ec4c9ed5b02bd461bafed00e929832e0d9f9b391ed1c0e |
| special_total | ff93f028621361b560c7f815ab966f15888c4f6102e32074b591840279cf4b5e |
| any | f7f8eca4f900dfd8b63b82e54587955b167a76f5c5ab6bc4734be37567d6e1c9 |
| has_ordinary | 32036257a0fa989dfd8e10094f125efc9b72bd230fddc92d4a2b796b3efa7c48 |
| has_capital_gain | 85a4c63ed1422645a8fe52bf464c0b554436d510c09a526e6cadb79c44bee847 |
| has_return_of_capital | 0ede2ce620dc25d6bbfbe579697700eb1bfdf8bda58049aa1b8c8b2a3c7c98c7 |
| zero | 81e03ac28d2a7399c7206d4cd2fa6b2067819991a0664e25e4bc8ec9f103e06b |
| no | 86328eb62e9effb0a35b5d4f2a9bef67a69f51fc25ab32d083f572d30517a742 |
| box2b_if_capital_gain | 093826c9dc75713c909e45b766421db55ae12cf2ecbbf096020e52c32a6594a6 |
| box2c_if_capital_gain | 912015453f6bf32ef6c2d51416f68c7693efe2c027633c1e7fa793db82373690 |
| box2d_if_capital_gain | 501e9a966270d4e7a45463476870d4380d169c763dd6495a4162461bb5a991c4 |
| box2f_if_capital_gain | 8d01e7f4c0fbb736e3ad2b9e7818c90b3dd4a6055c61b8a59649472125b3c25f |
| box2e_if_ordinary | b494c27376ff2e5f747ae37a039f36150b801f894472565f8e51ea5ce055abe2 |
| box3_if_dividends | 8f6b745edc950ade02538cfc7dac3b253f1a21eedb05b983c950ab8b3b5337a8 |
| box9_if_dividends | 0f74bf2ae66db1caf27cd5c137a9ad1c233e982864fbc1413c5fc8daa8eb1432 |
| box10_if_dividends | 2f5a7042c5bd9c193d85a8e12688d7ed01f64b7d7fdb23ef8d318c001b2a4194 |
| box12_if_dividends | 36a77b3b763ca983d7348a792268309d5fba94dad3f2fe2862b33eff4046f496 |
| box13_if_dividends | cc1bbd38fb0b42bea0647bef3c964a4d0f7de3552c9f0366a998f3d9422c661b |
| basis_reconciled_if_return_of_capital | c425142b472a319bccecf8bbcfe23aa4b8f08eacf0a1bb0566f25e529b1a0444 |
| (rest of the document) | a85f53df7da43a251cbe59da94288581f632b3d79e337c9ee2ba4785671b029b |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass cc1da444533f

| field | value |
| --- | --- |
| date | 2026-11-07 |
| review scope | lines box1a, box1b, box2a, box5, section1202, amt, unsupported, bad_special, screen, bad_components, special_total, any, has_ordinary, has_capital_gain, has_return_of_capital, zero, no, box2b_if_capital_gain, box2c_if_capital_gain, box2d_if_capital_gain, box2f_if_capital_gain, box2e_if_ordinary, box3_if_dividends, box9_if_dividends, box10_if_dividends, box12_if_dividends, box13_if_dividends, basis_reconciled_if_return_of_capital |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | cc1da444533f1eae7aa88a37e3d1edb6c9dbe9535438174c78f4f006985feb13 |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 50cc9f6743109d1725ac00ebd1a961174abfff8db1e23f228411bf9b11f41fae |
| receipt | .transcription/div.render.lines-31be2faa5d38 |
| lines judged | 28 |
| match / mismatch / unclear / missing | 28 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1099div | January 2024 (continuous-use form) | 1, 2, 3, 4, 5, 6 | whole document | 833d93e5f2d0bfcc8c9d720c0e8cb8e623cd2c6a8ee25f364f1f69f49fa490e3 | 5 | 617419bd079b1520174ceca8549065c9e4001f2b06a16d1425c5469bbe49fa3d |
| i1040sd | 2025; printed date 2025-12-11 | 8, 11 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 8, 11 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| i1040sb | TY2025; printed April 23, 2025 | 1, 2, 3 | whole document | 2bf62267574473b36fd9a69b6e0837ef74d72ac7d5dcbf1d26e7047d099f1e05 | 1, 2, 3 | 0d38b25d416cb650ef264faf8c1f118dfa4666f3949fbba7120f8c04d4e6914e |
| i1040gi | 2025; printed date 2026-02-25 | 25, 26 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 25, 26 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| f8995 | 2025; created 2025-09-12 | 1 | whole document | 49922587df3bd093e24470f5b42d0e3382ef8f5210b3cedccb02ccb864f2f65a | - | 8e2e78d7610e1d45e93c10c8b03f9026d46a1166678c6ed93f852569c382f346 |
| i8995 | 2025; printed date 2026-01-26 | 3, 4 | pages named by another document's citation | 96284eaad2fe5ec324de9fd4335cea9ea3260e66ff1d8b1725c1cff7fbe1ddc2 | 3, 4 | 6671a64ba0011f89e03eb5985954073dcd984b3f346495182916b0ecaa42ec1a |

##### Raw response

```yaml
```yaml
lines:
  - key: "box1a"
    status: MATCH
    reason: "Box 1a 'Shows total ordinary dividends that are taxable.' The restatement takes the total ordinary dividends from box 1a when the filer received dividends, and zero otherwise."
  - key: "box1b"
    status: MATCH
    reason: "Box 1b 'Shows the portion of the amount in box 1a that may be eligible for reduced capital gains rates. See the Instructions for Form 1040 for how to determine this amount.' Using the Form 1040 line 3a total after the line 3a exceptions follows that pointer and is still a portion of box 1a."
  - key: "box2a"
    status: MATCH
    reason: "Box 2a 'Shows total capital gain distributions.' The restatement takes that amount when the filer received distributions, and zero otherwise."
  - key: "box5"
    status: MATCH
    reason: "Box 5 'Shows the portion of the amount in box 1a that may be eligible for the 20% qualified business income deduction.' The i8995 holding-period and obligated-payment conditions ('held for more than 45 days and for which the payment isn't obligated to someone else') support the confirmed input."
  - key: "section1202"
    status: MATCH
    reason: "Box 2c is section 1202 gain that 'may be subject to an exclusion.' The Schedule D instructions require Form 8949 code 'Q' and a Form 6251 line 13 entry, and the refusal names both as outside scope."
  - key: "amt"
    status: MATCH
    reason: "Box 13 'Shows exempt-interest dividends subject to the alternative minimum tax... See the Instructions for Form 6251.' A positive box 13 amount correctly triggers the Form 6251 refusal."
  - key: "unsupported"
    status: MATCH
    reason: "Boxes 2e and 2f (section 897), boxes 9 and 10 (liquidation distributions) and box 3 return of capital where basis is not reconciled ('Any amount received in excess of your basis is taxable to you as capital gain') need treatment outside scope. The refusal names that treatment. The 'and' binds only to the box 3 condition, as intended."
  - key: "bad_special"
    status: MATCH
    reason: "Boxes 2b, 2c and 2d each show 'the portion of the amount in box 2a.' They describe distinct gain types (real property, small business stock, collectibles), so neither any one of them nor their total can exceed box 2a."
  - key: "screen"
    status: MATCH
    reason: "This is a $0 screening value whose refusals name the excluded cases: section 1202, Form 6251, section 897 and liquidation distributions, unreconciled basis, and inconsistent component totals."
  - key: "bad_components"
    status: MATCH
    reason: "Box 1b and box 5 are each described as 'the portion of the amount in box 1a.' Qualified dividends (no more than box 1b) or section 199A dividends that exceed box 1a are therefore inconsistent."
  - key: "special_total"
    status: MATCH
    reason: "The restatement adds the box 2b, 2c and 2d components, each of which is a portion of box 2a, for the consistency check."
  - key: "any"
    status: MATCH
    reason: "This is a scope question about whether the filer received any dividends or distributions. It covers the box 1a through box 13 distribution types and nominee amounts, consistent with the form and the Schedule B instructions."
  - key: "has_ordinary"
    status: MATCH
    reason: "The test is box 1a above zero, as labeled."
  - key: "has_capital_gain"
    status: MATCH
    reason: "The test is box 2a above zero, as labeled."
  - key: "has_return_of_capital"
    status: MATCH
    reason: "The test is box 3 above zero, as labeled."
  - key: "zero"
    status: MATCH
    reason: "The program enters $0 for a box whose gating condition does not hold."
  - key: "no"
    status: MATCH
    reason: "The program enters false when there is no box 3 amount, so no basis question needs an answer."
  - key: "box2b_if_capital_gain"
    status: MATCH
    reason: "Box 2b is 'the portion of the amount in box 2a,' so gating it on box 2a being above zero loses nothing."
  - key: "box2c_if_capital_gain"
    status: MATCH
    reason: "Box 2c is 'the portion of the amount in box 2a,' so gating it on box 2a being above zero loses nothing."
  - key: "box2d_if_capital_gain"
    status: MATCH
    reason: "Box 2d is 'the portion of the amount in box 2a,' so gating it on box 2a being above zero loses nothing."
  - key: "box2f_if_capital_gain"
    status: MATCH
    reason: "Box 2f 'Shows the portion of the amount in box 2a that is section 897 gain,' so gating it on box 2a being above zero loses nothing."
  - key: "box2e_if_ordinary"
    status: MATCH
    reason: "Box 2e 'Shows the portion of the amount in box 1a,' so gating it on box 1a being above zero loses nothing."
  - key: "box3_if_dividends"
    status: MATCH
    reason: "Box 3 nondividend distributions are taken when the filer received distributions, and zero otherwise."
  - key: "box9_if_dividends"
    status: MATCH
    reason: "Box 9 cash liquidation distributions are taken when the filer received distributions, and zero otherwise."
  - key: "box10_if_dividends"
    status: MATCH
    reason: "Box 10 noncash liquidation distributions are taken when the filer received distributions, and zero otherwise."
  - key: "box12_if_dividends"
    status: MATCH
    reason: "Box 12 exempt-interest dividends are taken when the filer received distributions, and zero otherwise. The input correctly notes that box 13 'is included in box 12.'"
  - key: "box13_if_dividends"
    status: MATCH
    reason: "Box 13 specified private activity bond interest dividends are taken when the filer received distributions, and zero otherwise."
  - key: "basis_reconciled_if_return_of_capital"
    status: MATCH
    reason: "Box 3 'reduces your basis and is not taxable' only 'To the extent of your cost (or other basis).' Asking whether basis has been reduced with no distribution exceeding basis is the right question when box 3 is above zero; otherwise the answer is false."
```
```

## Raw response

```yaml
lines:
  - key: "box2b"
    status: MATCH
    reason: "Direct input of box 2b, \"Unrecap. Sec. 1250 gain\", described as \"the portion of the amount in box 2a that is unrecaptured section 1250 gain\"."
  - key: "box2c"
    status: MATCH
    reason: "Direct input of box 2c, \"Section 1202 gain\"."
  - key: "box2d"
    status: MATCH
    reason: "Direct input of box 2d, \"Collectibles (28%) gain\"."
  - key: "box2e"
    status: MATCH
    reason: "Direct input of box 2e, \"Section 897 ordinary dividends\"."
  - key: "box2f"
    status: MATCH
    reason: "Direct input of box 2f, \"Section 897 capital gain\"."
  - key: "box3"
    status: MATCH
    reason: "Direct input of box 3, \"Nondividend distributions\", which \"Shows a return of capital\"."
  - key: "box9"
    status: MATCH
    reason: "Direct input of box 9, \"Cash liquidation distributions\"."
  - key: "box10"
    status: MATCH
    reason: "Direct input of box 10, \"Noncash liquidation distributions\"."
  - key: "box12"
    status: MATCH
    reason: "Direct input of box 12, \"Exempt-interest dividends\". The note that box 13 is already included agrees with the box 13 instruction: \"This amount is included in box 12.\""
  - key: "box13"
    status: MATCH
    reason: "Direct input of box 13, which \"Shows exempt-interest dividends subject to the alternative minimum tax\"."
  - key: "basis_reconciled"
    status: MATCH
    reason: "This yes/no input screens the box 3 rule: the distribution \"reduces your basis and is not taxable\", and any excess over basis \"is taxable to you as capital gain\". The program refuses the cases it does not handle."
  - key: "box1a"
    status: MATCH
    reason: "Box 1a \"Total ordinary dividends\" is the amount the Schedule B instructions say \"should be shown in box 1a of your Forms 1099-DIV\"."
  - key: "box1b"
    status: MATCH
    reason: "Box 1b is \"Qualified dividends\", the same name as Form 1040 line 3a. The box 1b instruction says \"See the Instructions for Form 1040 for how to determine this amount and where to report.\""
  - key: "box2a"
    status: MATCH
    reason: "Box 2a \"Total capital gain distr.\" is taken from the Schedule D capital gain distributions input, which is labeled as generally box 2a."
  - key: "box5"
    status: MATCH
    reason: "Box 5 \"Section 199A dividends\" is the portion of box 1a \"that may be eligible for the 20% qualified business income deduction\". The Form 8995 instructions require holding \"for more than 45 days\" and say the amount \"is reported to you on Form 1099-DIV, line 5\"."
  - key: "section1202"
    status: MATCH
    reason: "Box 2c gain \"may be subject to an exclusion\". The Schedule D instructions require Form 8949 code \"Q\" and, for AMT, \"enter 7% of your allowable exclusion ... on line 13 of Form 6251\". The refusal names both."
  - key: "amt"
    status: MATCH
    reason: "Box 13 \"Shows exempt-interest dividends subject to the alternative minimum tax ... See the Instructions for Form 6251\". The program refuses when the amount is above $0."
  - key: "unsupported"
    status: MATCH
    reason: "The program refuses boxes 2e/2f (section 897 treatment), boxes 9/10 (liquidation distributions), and box 3 when basis is unreconciled (\"Any amount received in excess of your basis is taxable to you as capital gain\"). This is a narrowing, and the refusal names it."
  - key: "bad_special"
    status: UNCLEAR
    reason: "The text supports each check on its own, since boxes 2b, 2c and 2d are each \"the portion of the amount in box 2a\". The text never says these portions are disjoint, so it does not establish that their sum cannot exceed box 2a."
  - key: "screen"
    status: MATCH
    reason: "The line enters $0 after the scope refusals, and each refusal names the excluded treatment or the correction needed."
  - key: "bad_components"
    status: MATCH
    reason: "Box 1b \"Shows the portion of the amount in box 1a\" and box 5 \"Shows the portion of the amount in box 1a\". So neither amount may exceed ordinary dividends."
  - key: "special_total"
    status: MATCH
    reason: "This is the sum of boxes 2b, 2c and 2d, used only for the consistency check against box 2a."
```
