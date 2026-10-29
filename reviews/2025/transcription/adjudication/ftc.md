# Adjudication summary: ftc

`forms/2025/ftc.yaml` is the foreign tax credit by election without Form 1116. It had no summary before. Earlier
rulings are in the sidecars of the archived logs. The latest before Stage 18 is
`.transcription/archive/stage18-before-findings-fixes-2026-10-29/reviews__2025__{transcription,render}__ftc[.deepseek].rulings.json`.
Those rulings accepted Form 1040 line 16 alone as the regular tax, because Schedule 2 Part I was refused.

Stage 18 made Schedule 2 line 1a (the excess advance PTC repayment) computed. The round-1 adjudication found that the
limit then left out line 1z (F1, `.transcription/proposed/stage18/s3.findings.md`). BUG-0190 fixed it:
`ftc.regular_tax` = Form 1040 line 16 + Schedule 2 line 1z (i1116 p. 25, Line 20), and `ftc.limited` reads it.

## Stage 18 round 2

These are the fresh logs of 2026-10-29, reviewed after BUG-0190. Each reviewer was given i1116 pp. 1, 2 and 25. The
transcription triage is in `../triage/ftc[.deepseek].json` (executable-triage-v2: 1,228 fixtures, 500 generated
returns, seed 20261026, 200 partial records, 1,928 comparisons, no errors). The full ruling text is in
`.transcription/proposed/stage18/round2/{transcription,render}.ftc[.deepseek].json`.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | ftc.credit | model error; scope | 1,229/1,928 agree; candidate-unknown 244 (70 completed; zero-tax returns, e.g. stage10.ira.fully_taxable needs s1a.tips via line 16); candidate-refuses 454 (all on refused returns); project-refuses 1 (stage4.refuse.ftc.election: conditions met, ftc.elect false; project ftc.needs1116, candidate $0.00) | i1116 p. 2, "the smaller of (a) your total foreign tax, or (b) your regular tax"; p. 2, Who should file; p. 25, Line 20 | The regular tax matches: line 16 + line 1z on both sides. With no foreign tax the candidate still needs regular tax, which the source does not need. A not-elected credit goes to Form 1116, which the project refuses with a cited gate. |
| deepseek | transcription | ftc.credit | model error; scope | 1,166/1,928 agree; candidate-unknown 244 (70 completed); candidate-refuses 456 (all on refused returns); project-refuses 62 (e.g. classm.asset.4, classm.s1.2: a failed condition; project ftc.needs1116, candidate $0.00) | the same | The same zero-tax defect. On a failed election the candidate's $0.00 would drop a credit that Form 1116 allows, and the project refuses with a cited gate. |
| claude | render | regular_tax | scope | scope.other_line16 (Form 4972, a positive Form 8978 amount) at f1040.line16; scope.credits (a negative Form 8978 adjustment); regression stage18.ftc_limit_with_repayment: regular tax $375.00, credit $200.00, line 22 $175.00 | i1116 p. 25, Line 20, "less any tax included on line 16 from Form 4972"; the Form 8978 paragraph | The omitted subtraction, adjustment and zero floor apply only to refused items. Without them the sum of two NonNegDollars amounts is never negative. |
| deepseek | render | regular_tax | scope | the same | the same | The same. |

Counts per log: transcription ftc (Claude) 1 model error (with scope on the project-refuses kind); transcription
ftc.deepseek 1 model error (with scope on the project-refuses kind); render ftc 1 scope; render ftc.deepseek 1 scope.

Findings: none. Both reviewers' regular tax is the BUG-0190 expression. The fix's choice of line 1z over line 3 agrees
with Line 20, because line 3 adds the alternative minimum tax, which section 26(b)(2) excludes. Nothing reads
`ftc.regular_tax` except `ftc.limited`. When Form 8962 refuses, the refusal reaches the credit only on returns that are
refused anyway (stage18.refuse.alien_below_100, stage18.refuse.two_counted_same_state). No new error found.
