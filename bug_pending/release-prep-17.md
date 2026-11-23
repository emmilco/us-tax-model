## BUG-NEW-release-prep-17 — Private activity bond exempt-interest dividends (Form 1099-DIV box 13) are left out of the AMT line 2g amount the screen reads

- **Date:** 2026-11-23
- **Caught by:** the sampled completeness review of s2 run after the s2.other_tax change, adjudicated in release preparation 2 (claude-opus-5-5, judgment), 2026-11-23: claim s2#1.1.
- **Source:** i6251 pp. 3-4, Line 2g: 'Exempt-interest dividends paid by a mutual fund or other regulated investment company are treated as interest income on specified private activity bonds ...' and 'This specified private activity bond interest dividends amount should be reported to you in box 13 of Form 1099-DIV.'
- **Symptom:** s2.amt_pab asks for Form 1099-INT box 9 and tax-exempt OID on a private activity bond only; div.box13 (asked with the dividends) is read by no AMT line. The line 2g amount the AMT screen adds is too low by the box 13 dividends, so a filer near the AMT exemption can pass the screen with AMT owed (no refusal, understated tax).
- **Where:** forms/2025/s2.yaml s2.amt_pab and the line 2g sum it feeds; interview/2025/questions.yaml s2.amt_pab.
- **Proposed fix:** Add div.box13_if_dividends to the line 2g amount (or name Form 1099-DIV box 13 in s2.amt_pab's question), with a hand-predicted fixture near the AMT screen's threshold.
- **Proposed fix lines:** s2.amt_pab
- **Severity:** low
- **Tags:** s2, AMT, Form 6251, completeness review; open
