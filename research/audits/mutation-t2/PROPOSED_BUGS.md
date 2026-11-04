# mutation-t2 proposed bug entries

## PENDING-1 — Social Security Benefits Worksheet shows amounts on skipped lines 9, 11 and 15 (married filing separately, lived together)

- **Caught by:** T-159 tier 2 mutation analysis (survivor `operand.ssb.ssb.line16.line16_together.then0` is equivalent only because of this; found while writing `mutation.t2.ssb.mfs_together_skip`).
- **Source:** i1040gi p. 32, Social Security Benefits Worksheet, line 8: "Married filing separately and you lived with your spouse at any time in 2025, skip lines 8 through 15; multiply line 7 by 85% (0.85) and enter the result on line 16."
- **Symptom:** stage10.ss.mfs_together (MFS, lived together, line 7 $20,000): line 8 $0, line 9 $20,000, line 10 $0, line 11 $20,000, line 12 $0, line 13 $0, line 14 $0, line 15 $17,000, line 16 $17,000. Lines 9, 11 and 15 are skipped by the instruction but print amounts. Line 16 and line 18 (and Form 1040 line 6b) are right: line 16 takes `ssb.line16_together`.
- **Fix:** for `ssb.mfs_together`, show lines 8 to 15 as blank: either `shown_when` on lines 8 to 15 (not mfs_together), or a choose to $0 on lines 9, 11 and 15. Owner of `forms/2025/ssb.yaml` to choose.
- **Fix lines:** ssb.line9, ssb.line11, ssb.line15 (and possibly 8, 10, 12 to 14 for display).
- **Siblings checked:** none beyond the worksheet.
- **Regression predictions:** stage10.ss.mfs_together: lines 9, 11 and 15 blank ($0, or hidden); line 16 $17,000; line 18 $17,000; Form 1040 line 6b $17,000 (unchanged). After the fix, `operand.ssb.ssb.line16.line16_together.then0` becomes killable (line 15 is then $0) and the case-split acceptance lapses on its own.
- **Validation:** observed by running the evaluator on the corpus case. The source reading has not had a second review.
- **Tags:** display, ssb, low.
