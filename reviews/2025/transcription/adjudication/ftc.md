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

## Landing round (2026-11-14)

Interview redraft (landing worktree), Claude line-scoped pass ea98d8b27ac6. Triage `.transcription/triage/2025/ftc.json` (executable-triage-v2, regenerated 2026-11-14 on the fresh build; not rerun). Rulings applied with `rule.py`; full text in the log and sidecar.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | ftc.has_tax | representation | 2,581/2,629; 35 candidate-unknown (12 completed), 13 project-unknown; no value | i1116 pp. 1-2 | Reads ftc.taxes without the ftc.asked parent. |
| claude | transcription | ftc.credit | model error | 1,757/2,629; 1 value (completed), 641 candidate-unknown, 198 candidate-refuses, 20 project-refuses, 12 project-unknown | i1116 p. 25, Line 20 | Limit by Form 1040 line 16 alone, dropping Schedule 2 line 1z (stage18.ftc_limit_with_repayment $200 / $0). |

Counts: model error 1, representation 1 (2). Findings: none. Project lines unchanged.

## Landing round (2026-11-14), render

Lane land3-adj7 (claude-opus-5-5, judgment). Open lines of the Claude render log `.transcription/logs/2025/render/ftc.md`, ruled on the rendered English (`rendered/2025/ftc.md`), the form YAML and the cited source; the deepseek log is dormant and not ruled.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | render | limited | scope | MISMATCH; form YAML | i1116 p. 25, Line 20 | Form 4972 tax is refused at Form 1040 line 16 (scope.other_line16), so nothing is subtracted on a completed return. |

Counts: claude render: scope 1.

Findings: none. No line left open.

## Goal-1 round (2026-11-15)

Lane b1-adj-e (claude-opus-5-5, judgment; tax year 2025, us). Open lines of the Claude logs after the goal-1 fix lanes (merge worktree nx-b1), ruled on the triage record `.transcription/triage/2025/<form>.json` (executable-triage-v2; not rerun), the archived sources and the form YAML; render lines on the rendered English (`rendered/2025/<form>.md`). Rulings files `/tmp/b1-adj-e/<form>[.render].json`, applied with `rule.py`; full text in the log and sidecar. The deepseek logs are dormant and not ruled.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | ftc.has_tax | representation | 2,511/2,671; 149 candidate-unknown (32 completed), 11 project-unknown; no value | i1116 pp. 1-2 | Reads ftc.taxes without the ftc.asked parent. |
| claude | transcription | ftc.credit | model error | 2,469/2,671; 151 candidate-unknown, 26 project-refuses, 23 project-unknown, 2 value (1 completed) | i1116 p. 25, Line 20 | Limit by Form 1040 line 16 alone, dropping Schedule 2 line 1z (stage18.ftc_limit_with_repayment $200 / $0). |
| claude | render | limited | scope | MISMATCH; form YAML | i1116 p. 25, Line 20 | Form 4972 tax is refused at Form 1040 line 16 (scope.other_line16). |

Counts: claude transcription model error 1, representation 1; claude render scope 1. Findings: none. Left open: none.
