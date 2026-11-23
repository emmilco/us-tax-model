## BUG-NEW-release-prep-15 — A series of substantially equal payments changed in 2025 with a code 7 Form 1099-R, or with no 2025 Form 1099-R, is neither asked nor refused

- **Date:** 2026-11-23
- **Caught by:** the sampled screen and false-no reviews of gate:retirement.is_code2 run after the BUG-1202 fix, adjudicated in release preparation 2 (claude-opus-5-5, judgment), 2026-11-23: screen finding 0, false-no findings 0 and 2.
- **Source:** p590b p. 26: 'The recapture tax applies if you modify the series of payments ... before the later of ... The 5th anniversary of the date of the first distribution of the series; or ... The date you reach age 59½' and 'The recapture tax is imposed in the tax year in which the modification occurs'; reported on Form 5329 line 4.
- **Symptom:** The series question is asked only with codes 1 and S (retirement.early_screen) and, since BUG-1202's fix, code 2 (retirement.code2_partial). A filer past 59½ whose series began less than 5 years ago and was changed in 2025 gets code 7, and a filer who stopped the payments may get no 2025 Form 1099-R from that account; neither is asked, and the recapture of the earlier years' 10% tax is left off without a refusal (understated tax).
- **Where:** forms/2025/s2.yaml s2.other_tax; interview/2025/questions.yaml s2.other_tax (help).
- **Fix:** s2.other_tax, asked of every filer in the other-taxes group, now names the case: its help gives 'the 10% tax brought back when a series of equal retirement payments is changed too soon' as an example, and its encoded question lists 'the recapture of the 10% additional tax when a series of substantially equal payments from a retirement plan or IRA is changed before the later of age 59½ or 5 years after its first payment (Form 5329 line 4)', cited to p590b p. 26. A Yes refuses through s2.other, as before. Lane release-prep-2 (claude-opus-5-5, judgment), 2026-11-23.
- **Fix lines:** s2.other_tax
- **Siblings checked:** retirement.early_screen (codes 1 and S), retirement.code2_partial (code 2), s2.other (refusal unchanged).
- **Severity:** medium
- **Tags:** retirement, s2, Form 5329, missed refusal, sampled false-no review, fixed
