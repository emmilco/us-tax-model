## BUG-NEW-lane-lints-08 — Closure: BUG-NEW-release-prep-16 is fixed (whose education and whose first home count, in the early-distribution exception question)

- **Date:** 2026-11-24
- **Closes:** BUG-NEW-release-prep-16
- **Closure:** fixed
- **Evidence:** reproduced against forms/2025/retirement.yaml: the source of retirement.exception listed conditions for 01, 02, 03, 04, 09, 11 and 19, none for 08, and stated 09's no-ownership test for "you" and the spouse only; p590b (2025) p. 27: "The education must be for you, your spouse, or the children or grandchildren of you or your spouse." and the first-time homebuyer "who is any of the following" list (yourself, your spouse, your or your spouse's child, grandchild, parent or other ancestor).
- **Fix:** retirement.exception's question (source) adds "08, an IRA distribution for qualified higher education expenses, only for the education of you, your spouse, or your or your spouse's children or grandchildren" and restates 09 as a first home "of a first-time homebuyer who is you, your spouse, or your or your spouse's child, grandchild, parent or other ancestor", the no-ownership test stated of that homebuyer and their spouse. The locator adds the i5329 table row for 08 and the p590b p. 27 quotes; the 2026 operation that sets the locator (changes/2026/retirement.yaml, C-PEOP-05+C-PEOP-07) carries them, at p590b p. 28 in the 2026 edition. No fixture: the enumeration and its values are unchanged.
- **Fix lines:** retirement.exception
- **Siblings checked:** retirement.has_exception, retirement.is_e05, retirement.is_e09, retirement.is_e19, retirement.is_e22, retirement.is_e23, retirement.wrong_kind
- **Tags:** retirement, Form 5329, wording; fixed
