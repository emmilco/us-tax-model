# Screen adjudication, group 9 (2026-11-04, refresh round 2)

Brief: `.transcription/proposed/fixr2/BRIEF.md`, "Refresh round (2026-11-03)", applied to the round-2 fixes (BUG-0408,
BUG-0409). Screens: 6, rerun after those fixes changed their questions or cited pages (`check_screens.py` reported them
as `rerun`). Rulings are in `rulings.json` under `unruled:<screen>` with each review's `prompt_sha`, replacing the
group 7 and group 8 rulings of the same screens; earlier rulings were reused where the finding repeats, after checking
the current lines. Quotes were checked against `sources/2025/*.cols.txt`.

Findings: 29. Classes: covered 13, accepted WIDE 10, accepted (minor UNCLEAR, leans WIDE) 3, model error 2, out of scope / presentation 1. No defect.

## Refresh round 2

| screen | findings (n: class) | disposition |
| --- | --- | --- |
| `f8960.unsupported` | 0: covered; 1: covered; 2: covered; 3: covered; 4: model error; 5: accepted WIDE; 6: accepted WIDE; 7: covered | No defect. BUG-0408's additions (life insurance contract gain or loss, the capital loss carryforward adjustment) drew no finding and closed group 8's two lows. Alaska Permanent Fund dividends are Schedule 1 line 8g, not in Form 1040 line 3b, which `f8960.line2` copies. |
| `retirement.special` | 0: covered; 1: model error; 2: accepted WIDE; 3: accepted (minor UNCLEAR, leans WIDE) | No defect. BUG-0408's recontribution item closed group 8's low. Box 5 is subtracted (`retirement.plan_excluded`). |
| `sales.special` | 0: accepted WIDE; 1: accepted WIDE; 2: accepted WIDE | No defect. BUG-0408's wording on depreciated real property closed group 8's low. |
| `scope.other_income` | 0: covered; 1: covered; 2: covered; 3: accepted (minor UNCLEAR, leans WIDE) | No defect. Form 4972 and Form 8814 are named in `scope.other_line16`; Schedule 1 items are asked separately. |
| `scope.other_line16` | 0: covered; 1: accepted WIDE; 2: accepted WIDE; 3: out of scope / presentation | No defect. The CFC/PFIC findings are the over-refusal accepted in BUG-0409 (T-216). |
| `scope.schedule1` | 0: covered; 1: covered; 2: covered; 3: accepted WIDE; 4: accepted WIDE; 5: accepted (minor UNCLEAR, leans WIDE) | No defect; as group 7 (rechecked). |

## Errors introduced by the round-2 fixes

None found in these screens. One defect outside the screen reviews' findings touches `retirement.special`: net
unrealized appreciation in employer securities (Form 1099-R box 6) is neither asked nor refused, and
`retirement.plan_simple` taxes it on line 5b (completeness retirement#2, BUG-0413, medium; it predates round 2).
