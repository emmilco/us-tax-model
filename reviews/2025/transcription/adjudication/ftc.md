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

## Goal-1 coverage-expansion round (2026-11-15)

Lane xadj-d (claude-opus-5-5, judgment; tax year 2025, us), round 2 of the coverage-expansion merge (uncommitted worktree xint). Open lines of the Claude transcription log of this round's review, ruled on the triage record `.transcription/triage/2025/ftc.json` (executable-triage-v2, written by triage.py after the review; not rerun), the archived sources, the form YAML and the interview bank. Rulings `/tmp/xadj/xadj-d/ftc.json`, applied with `rule.py`; full text in the log and sidecar. The deepseek logs are dormant and not ruled.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | ftc.taxes_if_asked, ftc.has_tax, ftc.all_passive_if_tax, ftc.statements_if_tax, ftc.eligible_if_tax | model error | 2,811 to 2,821/2,995 agree; 16 completed value differences each (classm.f1040.6.deepseek $195.00 v. $0.00; classm.s2.1 $444.00 v. $0.00) | i1116 p. 1, election without Form 1116: qualified payee statements include Form 1099-DIV and 1099-INT | The reply asks the foreign tax only on s3.foreign_any, whose help tells a filer to leave out Form 1099-DIV box 7 tax unless Form 1116 was once filed; the project's parent ftc.asked (dividends, interest or s3.foreign_any) reaches it. |
| claude | transcription | ftc.credit | model error | 2,823/2,995; 13 completed value (the same gate cases), 77 project-refuses (f1116.line35) | i1116 p. 1; p. 25, Line 20 | Inherits the gate; its extra sa.foreign_tax_deduct test matters only on returns Schedule A refuses. |
| claude | transcription | ftc.carryover_if_asked | representation | 2,989/2,995; 6 differences, none completed | i1116 p. 1, no carryover under the election | The project also asks a filer whose 2024 return had a separate form (s3.prior_other_forms); a carryover refuses the return. |

Counts: model error 6, representation 1 (7). Findings: none. Left open: none.

## Goal-1 coverage-expansion round (2026-11-15), render

Lane xadj-d (claude-opus-5-5, judgment). Open lines of the Claude render log of this round, ruled on the rendered English, the form YAML and the cited source. Rulings `/tmp/xadj/xadj-d/ftc.render.json`.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | render | needs1116 | finding (medium) | UNCLEAR | i1040gi Schedule 3, line 1, condition 4, "You aren't filing Form 4563 or excluding income from sources within Puerto Rico" | ftc.needs1116 does not test condition 4, and sa.excluded_income does not refuse on the ftc path (BUG-0769). |
| claude | render | elect | ambiguity | MISMATCH | i1116 pp. 1-2; amb.2025.f1116_carryover_election; decision D3 | The election is made whenever available; the forfeited carryforward when the foreign tax exceeds the regular tax is raised for the owner. |
| claude | render | regular_tax | scope | MISMATCH | i1116 p. 25, Line 20 | Form 4972 tax is refused at Form 1040 line 16 (scope.other_line16). |

Counts: claude render 22 match; finding 1 (medium), ambiguity 1, scope 1. Findings: BUG-0769 (medium): add sa.excluded_income = true to ftc.needs1116's failed conditions (cite i1040gi Schedule 3 line 1, condition 4), so the return goes to Form 1116, where f1116.reduction refuses. Left open: none. No class M run for ftc this round.

## Goal-1 coverage-expansion round (2026-11-15), after the d-01 fix

Lane xadj (claude-opus-5-5, judgment, tax year 2025, jurisdiction us), xint worktree, after the integrator added sa.excluded_income to ftc.needs1116 (BUG-0769) and built. Line-scoped reruns: transcription pass 73f790ce759c (ftc.credit); render 2 match, 0 mismatch. Rulings file `/tmp/xadj/g/ftc.transcription.json`.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | ftc.credit | model error | triage 73f790ce759c: 352 agree of 3,002; no value difference; 2,068 candidate-refuses (no zero branch, routes no-tax returns to f1116.line35), 579 candidate-unknown (reads ftc.all_passive, ftc.carryover unasked), 3 project-refuses (f2441.line14_bad upstream) | i1040gi p. 115, Schedule 3, line 1, condition 4; i1116 pp. 1–2; p. 25, Line 20 | The reply drops the zero branch and requirement 4 (Form 4563 or Puerto Rico exclusion); the project tests it in ftc.needs1116. |

Counts: claude transcription model error 1; render no disagreement. Findings: none. Left open: none.
