# rental adjudication

Rental real estate entry (Schedule E Part I lines 3-22 and the entry's Form 8582 columns), new in coverage wave X1 (lane x1-sche).

## Goal-1 round (2026-11-15)

Lane xrev-new (claude-opus-5-5, judgment, tax year 2025, jurisdiction us), worktree x1-sche (uncommitted). First whole-form Claude transcription review (cost $1.43): agree 7, disagree 28; carry ruled none (no earlier log). Ruled on `.transcription/triage/2025/rental.json` (36 fixtures, 560 partial records; no generated return reaches a rental entry, so the sample is fixtures and their partials), the reply, the archived sources and `forms/2025/rental.yaml`. Rulings `/tmp/xrev-new/rental.tr.json`.

The reply's expense lines divide by the same fraction as the project (fair-rental days over fair + personal - overlap days) but round it to four places; the project carries six places under `amb.2025.rental_use_ratio_places`. Its Form 8582 columns carry shown_when conditions (not on Form 8582, part does not apply) where the project shows the column value. Witnesses on `classm.sche.2` are a class M fixture that leaves the rental answers unsupplied.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | rental.part4 | representation | 532/596; completed: 1 value (x1sche.f9.excluded_home) | i8582 p. 3, Part IV | Reply folds in tests the project refuses elsewhere and the home tests; the one completed difference is a home left off Schedule E. |
| claude | transcription | rental.has_2025 | representation | 596/596 | i4562, Who Must File | Equivalent sums. |
| claude | transcription | 5, 7, 8, 10, 11, 13, 14, 15, 19 | ambiguity | 596/596 each | p527 p. 26, Dividing Expenses | Four-place vs six-place ratio (amb.2025.rental_use_ratio_places). |
| claude | transcription | 9, 12, 16, 17 | ambiguity | 595, 595, 553, 595/596; completed differences by cents | p527 p. 26 | As above. |
| claude | transcription | 18 | ambiguity | 585/596; completed: 1 value by cents, 1 unknown (class M fixture) | p527 p. 26 | As above; the reply also reads rental.depletion ungated. |
| claude | transcription | 21 | representation | 504/596; completed: 3 values by cents, 1 unknown (class M fixture) | i1040se Line 21 | Ratio rounding; the rest refused returns or partials. |
| claude | transcription | 22 | representation | 505/596; completed: 1 value by cents | i1040se Line 22 | As 21. |
| claude | transcription | IV/V (a), IV/V (b), IV/V (e) | representation | 403, 406, 407/596; completed: candidate-hides-shown only | i8582 Parts IV-V | Reply hides the column where Form 8582 is not filed; no amount differs. |
| claude | transcription | IV/V (c) | representation | 266/596; no value difference | i8582 column (c) | Reply's refusals on returns the project refuses; partials. |
| claude | transcription | VI (a), VI (c), VII (a), VIII (c) | representation | 427, 496, 499, 495/596; completed: hides-shown only | i8582 Parts VI-VIII | As IV/V (a); VI (c) also rounds the ratio to four places. |
| claude | transcription | VII (c), VIII (b) | representation | 502/596 each; no completed difference | i8582 Parts VII-VIII | Refused returns and partials only. |

Counts: ambiguity 14, representation 14. Findings: none.

## Goal-1 round (2026-11-15), render

First whole-form Claude render review (cost $0.39): match 29, mismatch 2. Rulings `/tmp/xrev-new/rental.render.json`.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | render | 2 (rental.days_personal) | finding (medium) | prompt and help of rental.personal_any / days_personal | i1040se p. 4, Line 2 | Repair days, main-home days around a 12-month rental and swap arrangements not explained (BUG-0918). |
| claude | render | VI (a) | scope | scope.yaml refusal on s3.mfs | i8582 Part IV (MFS lived with spouse) | MFS refused for every return. |

Counts: finding 1, scope 1. Findings: BUG-0918 (medium).

## Goal-1 round (2026-11-15), class M

First Claude class M run (cost $0.62): agree 112, disagree 0. Nothing to rule.
