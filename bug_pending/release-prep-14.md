## BUG-NEW-release-prep-14 — Closure: BUG-1202 is fixed

- **Closes:** BUG-1202
- **Closure:** fixed
- **Caught by:** release preparation 2 (release-prep-2, claude-opus-5-5, judgment), 2026-11-23, on the owner's direction to fix open bugs.
- **Fix:** retirement.code2_partial, the code 2 question asked of every code 2 entry, now asks 'Does that exception fail to cover all of this money, or is this money one of a series of substantially equal payments that was changed in 2025?', with help naming the recapture ('Changing a series before age 59½, or within 5 years of its first payment, brings back the extra tax on the earlier payments'); a Yes refuses through retirement.code_screen and retirement.screen_refused, whose remedy already names 'a modified series of substantially equal payments'. Cite: p590b p. 26 (recapture tax 'imposed in the tax year in which the modification occurs'). The gate label retirement.code2_partial_if_code2 says the same.
- **Fix lines:** retirement.code2_partial, retirement.code2_partial_if_code2
- **Siblings checked:** retirement.early_screen (codes 1 and S, already names a modified series), retirement.code_screen, retirement.screen_refused (remedy unchanged), retirement.code7_wrong and retirement.not_beneficiary_if_death (codes 7 and 4: a series payment coded 7 after 59½ owes no recapture; code 4 is a beneficiary's), f5329.l2, the lines the siblings tool lists for the fix lines.
- **Evidence:** fixtures/2025/retirement.json relprep2.retirement.code2_series_changed (refused at retirement.screen_refused on Form 1040 line 4b, predicted before evaluation) and relprep2.retirement.code2_exception_covers (line 4b $10,000, Schedule 2 line 8 $0, predicted before evaluation); coverage row retirement.code2_series_changed.
- **Tags:** retirement, Form 5329, missed refusal, fixed
