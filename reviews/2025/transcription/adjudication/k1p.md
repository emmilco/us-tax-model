# k1p adjudication

Adjudication of the review logs of k1p (Schedule K-1 (Form 1065), one partner's share), a form new in the coverage expansion (lane x2-k1p).

## Goal-1 round (2026-11-15)

Lane xrev-new (claude-opus-5-5, judgment, tax year 2025, jurisdiction us), in worktree x2-k1p (uncommitted). First (whole-form) Claude transcription review of k1p, ruled on `.transcription/triage/2025/k1p.json` (26 fixtures, 497 partial records; no generated return reaches k1p while `scope.k1` refuses every K-1 filer), the reply, the archived sources and `forms/2025/k1p.yaml`. Rulings `/tmp/xrev-new/k1p.tr.json`, applied with rule.py; full text in the log and sidecar.

The reply declares its own refusals on lines (ptp, r_b2223, a basis/at-risk loss gate) where the project refuses once on `k1p.screened`, which every person sum filters on; it does not refuse trader, tests 4/6/7 or a former passive activity, and inverts `k1p.screened`. Every value difference falls on a fixture the project refuses.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | k1p.box9b_if_any | representation | 509/523 agree; 7 candidate-unknown, 7 project-unknown | i1065sk1 pp. 3, 9-16 (gates) | Unknowns on partial records only; reads gates differently. |
| claude | transcription | k1p.box9c_if_any | representation | 509/523 agree; 7 candidate-unknown, 7 project-unknown | i1065sk1 pp. 3, 9-16 (gates) | Unknowns on partial records only; reads gates differently. |
| claude | transcription | k1p.prior_total | representation | 510/523 agree; 13 project-unknown | i1065sk1 pp. 3, 9-16 (gates) | Unknowns on partial records only; reads gates differently. |
| claude | transcription | k1p.sche_row | representation | 517/523 agree; 1 candidate-unknown, 5 project-unknown | i1065sk1 pp. 3, 9-16 (gates) | Unknowns on partial records only; reads gates differently. |
| claude | transcription | IV/V (a) | representation | 518/523 agree; 5 candidate-unknown | i1065sk1 pp. 3, 9-16 (gates) | Unknowns on partial records only; reads gates differently. |
| claude | transcription | V (a) (k1p.b3_net_income) | representation | 521/523 agree; 2 candidate-unknown | i1065sk1 pp. 3, 9-16 (gates) | Unknowns on partial records only; reads gates differently. |
| claude | transcription | V (b) (k1p.b3_net_loss) | representation | 521/523 agree; 2 candidate-unknown | i1065sk1 pp. 3, 9-16 (gates) | Unknowns on partial records only; reads gates differently. |
| claude | transcription | (e) (k1p.b3_overall_loss) | representation | 509/523 agree; 14 project-unknown | i1065sk1 pp. 3, 9-16 (gates) | Unknowns on partial records only; reads gates differently. |
| claude | transcription | IV (a) | representation | 517/523 agree; 4 candidate-unknown, 2 project-unknown | i1065sk1 pp. 3, 9-16 (gates) | Unknowns on partial records only; reads gates differently. |
| claude | transcription | IV (b) | representation | 517/523 agree; 4 candidate-unknown, 2 project-unknown | i1065sk1 pp. 3, 9-16 (gates) | Unknowns on partial records only; reads gates differently. |
| claude | transcription | VI (a) | representation | 512/523 agree; 5 candidate-unknown, 6 project-unknown | i1065sk1 pp. 3, 9-16 (gates) | Unknowns on partial records only; reads gates differently. |
| claude | transcription | k1p.passive_loss | scope | 349/523 agree; 139 candidate-refuses, 27 candidate-unknown, 7 project-unknown, 1 value | i1065sk1 pp. 3, 9-11; i8582 Parts IV-V | Differs only on entries refused on k1p.screened. |
| claude | transcription | k1p.nonpassive_net | scope | 357/523 agree; 139 candidate-refuses, 22 candidate-unknown, 2 project-unknown, 3 value | i1065sk1 pp. 3, 9-11; i8582 Parts IV-V | Differs only on entries refused on k1p.screened. |
| claude | transcription | V (a) (k1p.b1_net_income) | scope | 506/523 agree; 2 candidate-hides-shown, 11 candidate-unknown, 3 project-unknown, 1 value | i1065sk1 pp. 3, 9-11; i8582 Parts IV-V | Differs only on entries refused on k1p.screened. |
| claude | transcription | V (b) (k1p.b1_net_loss) | scope | 445/523 agree; 64 candidate-refuses, 12 candidate-unknown, 2 project-unknown | i1065sk1 pp. 3, 9-11; i8582 Parts IV-V | Differs only on entries refused on k1p.screened. |
| claude | transcription | IV/V (b) | scope | 517/523 agree; 1 candidate-refuses, 5 candidate-unknown | i1065sk1 pp. 3, 9-11; i8582 Parts IV-V | Differs only on entries refused on k1p.screened. |
| claude | transcription | (e) (k1p.b1_overall_loss) | scope | 437/523 agree; 64 candidate-refuses, 11 candidate-unknown, 10 project-unknown, 1 value | i1065sk1 pp. 3, 9-11; i8582 Parts IV-V | Differs only on entries refused on k1p.screened. |
| claude | transcription | (e) (k1p.b2_overall_loss) | scope | 497/523 agree; 1 candidate-refuses, 11 candidate-unknown, 14 project-unknown | i1065sk1 pp. 3, 9-11; i8582 Parts IV-V | Differs only on entries refused on k1p.screened. |
| claude | transcription | V (a) (k1p.p5_income) | scope | 500/523 agree; 2 candidate-hides-shown, 16 candidate-unknown, 4 project-unknown, 1 value | i1065sk1 pp. 3, 9-11; i8582 Parts IV-V | Differs only on entries refused on k1p.screened. |
| claude | transcription | V (b) (k1p.p5_loss) | scope | 438/523 agree; 65 candidate-refuses, 17 candidate-unknown, 3 project-unknown | i1065sk1 pp. 3, 9-11; i8582 Parts IV-V | Differs only on entries refused on k1p.screened. |
| claude | transcription | 28 (h) | scope | 495/523 agree; 22 candidate-unknown, 3 project-unknown, 3 value | i1065sk1 pp. 3, 9-11; i8582 Parts IV-V | Differs only on entries refused on k1p.screened. |
| claude | transcription | 28 (k) | scope | 426/523 agree; 68 candidate-refuses, 24 candidate-unknown, 2 project-unknown, 3 value | i1065sk1 pp. 3, 9-11; i8582 Parts IV-V | Differs only on entries refused on k1p.screened. |
| claude | transcription | 28 (i) | scope | 428/523 agree; 70 candidate-refuses, 23 candidate-unknown, 2 project-unknown | i1065sk1 pp. 3, 9-11; i8582 Parts IV-V | Differs only on entries refused on k1p.screened. |
| claude | transcription | IV (c) | scope | 451/523 agree; 1 candidate-unknown, 7 project-unknown, 64 value | i8582, Part IV column (c) | Differs only on entries refused on k1p.screened. |
| claude | transcription | V (c) | scope | 440/523 agree; 15 candidate-unknown, 6 project-unknown, 62 value | i8582, Part IV column (c) | Differs only on entries refused on k1p.screened. |
| claude | transcription | k1p.screened | model error | 87/523 agree; 157 project-refuses, 93 project-unknown, 186 value | form note (scope) | Inverted screened line; omits screens. |

Counts: representation 11, scope 14, model error 1. Findings: none.

## Goal-1 round (2026-11-15), render

First Claude render review of k1p (34 lines: 16 match, 18 mismatch). The reviewer sees each line's restatement without the refusals on `k1p.screened`, the global refusal of married filing separately (`s3.mfs`) or the real estate professional refusal (`sche.re_pro`, lane x1-sche, scout R-K20); 17 mismatches name only refused cases. Integration must keep `sche.re_pro` asked of a K-1 box 2 filer.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | render | 1 | finding (BUG-0911, medium) | MISMATCH | k1p.screened refusals; s3.mfs; sche.re_pro | The case the reply names is refused. |
| claude | render | 9c | scope | MISMATCH | k1p.screened refusals; s3.mfs; sche.re_pro | The case the reply names is refused. |
| claude | render | V (b) (k1p.b1_net_loss) | scope | MISMATCH | k1p.screened refusals; s3.mfs; sche.re_pro | The case the reply names is refused. |
| claude | render | IV/V (a) | scope | MISMATCH | k1p.screened refusals; s3.mfs; sche.re_pro | The case the reply names is refused. |
| claude | render | IV/V (b) | scope | MISMATCH | k1p.screened refusals; s3.mfs; sche.re_pro | The case the reply names is refused. |
| claude | render | V (a) (k1p.b3_net_income) | scope | MISMATCH | k1p.screened refusals; s3.mfs; sche.re_pro | The case the reply names is refused. |
| claude | render | V (b) (k1p.b3_net_loss) | scope | MISMATCH | k1p.screened refusals; s3.mfs; sche.re_pro | The case the reply names is refused. |
| claude | render | (e) (k1p.b1_overall_loss) | scope | MISMATCH | k1p.screened refusals; s3.mfs; sche.re_pro | The case the reply names is refused. |
| claude | render | (e) (k1p.b2_overall_loss) | scope | MISMATCH | k1p.screened refusals; s3.mfs; sche.re_pro | The case the reply names is refused. |
| claude | render | IV (b) | scope | MISMATCH | k1p.screened refusals; s3.mfs; sche.re_pro | The case the reply names is refused. |
| claude | render | IV (c) | scope | MISMATCH | k1p.screened refusals; s3.mfs; sche.re_pro | The case the reply names is refused. |
| claude | render | VI (a) | scope | MISMATCH | k1p.screened refusals; s3.mfs; sche.re_pro | The case the reply names is refused. |
| claude | render | V (a) (k1p.p5_income) | scope | MISMATCH | k1p.screened refusals; s3.mfs; sche.re_pro | The case the reply names is refused. |
| claude | render | V (b) (k1p.p5_loss) | scope | MISMATCH | k1p.screened refusals; s3.mfs; sche.re_pro | The case the reply names is refused. |
| claude | render | V (c) | scope | MISMATCH | k1p.screened refusals; s3.mfs; sche.re_pro | The case the reply names is refused. |
| claude | render | 28 (h) | scope | MISMATCH | k1p.screened refusals; s3.mfs; sche.re_pro | The case the reply names is refused. |
| claude | render | 28 (k) | scope | MISMATCH | k1p.screened refusals; s3.mfs; sche.re_pro | The case the reply names is refused. |
| claude | render | 28 (i) | scope | MISMATCH | k1p.screened refusals; s3.mfs; sche.re_pro | The case the reply names is refused. |

Counts: scope 17, finding 1. Findings: BUG-0911 (medium): `k1p.box9b` is NonNegDollars, so a box 9b collectibles loss cannot be entered (i1065sk1 p. 16, 'Collectibles (28%) Gain (Loss)').

## Goal-1 round (2026-11-15), class M

Lane xrev-new (claude-opus-5-5, judgment, tax year 2025, jurisdiction us). Whole-form class M run (10 cases, 19 lines each; 0 amounts given, the entries' own answers only): agree 190, disagree 0, skipped 0, missing 0; cost $2.26. Nothing to rule. No generated return reaches k1p in this tree (scope.k1 still refuses every K-1 filer); the cases are built from the lane's fixtures.
