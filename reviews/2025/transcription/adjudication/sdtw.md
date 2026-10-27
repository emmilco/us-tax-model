# Adjudication — sdtw

Method: `README.md` in this directory.

## Round 3

Fresh reviews of 2026-10-26 (Claude claude-opus-5-5 and deepseek-flash) against the subject after BUG-0160 (line 4 is
zero when no Form 4952 is filed; closes BUG-0099). Triage records `../triage/sdtw.json` (state "invalid": the Claude reply
declares `sdtw.line44` and `sdtw.line46` NonNegDollars where the published type is Dollars; nothing executed) and
`../triage/sdtw.deepseek.json` (executable-triage-v2; 1,099 fixtures, 500 generated returns seed 20261026, no partial
records; 1,599 comparisons). The Claude lines 44 to 47 are ruled model error on the validation failure (44 and 46 fail;
45 and 47 read them). Its other 21 open lines are ruled by reading against i1040sd pp. 15–16, with counts from a read-only
scratch rerun of `tools/transcription/triage.mjs` on the same bank with those two declarations evaluated as the published
Dollars and lines 44–47 excluded (not a triage record; the raw reply is unchanged). Those candidate expressions for lines
15, 23–38, 40, 41 and 43 are identical to the round 2 Claude reply. Full ruling text:
`.transcription/proposed/round3/{transcription,render}.sdtw[.deepseek].json`. "Skip return" means a return on which the
worksheet's printed instructions skip the line (i1040sd pp. 15–16).

BUG-0160 check: the fix is right. Both fresh candidates copy `f4952.line4e` unguarded, the pre-fix project reading, and
show amounts from an unfiled Form 4952 (`classm.f5695.5`, `f4952.required` false: project $0.00, candidate $13,526.00).
No amount changes: line 3 is 0 on those returns, so lines 5, 8 and 47 are the same. The fix brings the cited
`f4952.carryover` refusal into line 4 (81 Claude, 99 DeepSeek project-refuses). All 81 and all 99 are on returns refused under the full interview, so in the bank
no return that completes now refuses.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | 4 | model error | scratch 1,379/1,599; 139 value (34 completed), 81 project-refuses (scope) | i1040sd p. 15, line 4 | Copies Form 4952 line 4e when no Form 4952 is filed (classm.f5695.5 $0 / $13,526). |
| claude | transcription | 15 | representation | scratch 1,599/1,599 | i1040sd p. 15, line 15 | The zero floor of a positive parameter never binds. |
| claude | transcription | 23, 24, 32 | model error | scratch each 1,558/1,599; 39 value (13 completed), 2 project-refuses | i1040sd p. 15, skip after line 22 | Nonzero amounts on skipped lines (classm.dependent.5 $0 / $52,797.20). |
| claude | transcription | 25, 29, 31, 34, 39, 40 | scope | scratch each 1,597/1,599; 2 project-refuses | i1040sd pp. 15–16, skips after lines 22, 32 and 34 | 0 by derivation (or gated) on skip returns; the only differences are cited line 1 refusals. |
| claude | transcription | 26 | model error | scratch 364/1,599; 516 value (355 completed), 572 project-refuses, 147 project-unknown | i1040sd p. 15, skip after line 22 | Ceiling on skipped lines (classm.f2441.2.deepseek $0 / $600,050); refusals scope, unknowns representation. |
| claude | transcription | 27, 28 | model error | scratch each 1,265/1,599; 332 value (257 completed), 2 project-refuses | i1040sd p. 15, skip after line 22 | Nonzero amounts on skipped lines (classm.f2441.1.deepseek $0 / $26,375). |
| claude | transcription | 35 | model error | scratch 1,147/1,599; 9 value (4 completed), 441 project-refuses, 2 project-unknown | i1040sd pp. 15–16, skips after lines 22 and 32 | Skipped earlier although Schedule D line 19 is positive (classm.s8812.2 $0 / $1,585). |
| claude | transcription | 36, 37, 38 | model error | scratch 779 / 814 / 1,416 of 1,599; 709 / 674 / 72 value, 109 candidate-unknown, 2 project-refuses | i1040sd p. 16, skip after line 34 (and 32) | Nonzero amounts on skipped lines (classm.f5695.7 line 38 $0 / $31,500); unknowns are records withholding f1040.line13a/13b (representation). |
| claude | transcription | 41 | model error | scratch 377/1,599; 668 candidate-shows-skipped (414 completed), 7 value, 435 candidate-refuses, 110 candidate-unknown | i1040sd p. 16, skip after line 40 | Not gated ("Line 41 is not gated separately"); shows amounts where lines 41–43 are skipped. |
| claude | transcription | 42, 43 | scope | scratch each 1,162/1,599; 435 candidate-refuses, 2 project-refuses | i1040sd p. 16, skip after line 40 | Gated on Schedule D line 18 and the earlier skips, as the BUG-0150 fix; refusals only, on refused returns. |
| claude | transcription | 44, 46 | model error | not executed (host type check) | i1040sd p. 16, lines 44 and 46 | Ruled on the validation failure (NonNegDollars for Dollars), not the tax reading; the floor is a no-op. |
| claude | transcription | 45, 47 | model error | not executed | i1040sd p. 16, lines 45 and 47 | Same expression as the project; the dependency closure carries the line 44/46 validation failure. |
| deepseek | transcription | 4 | model error | 1,361/1,599; 139 value (34 completed), 99 project-refuses (scope) | i1040sd p. 15, line 4 | As the Claude line 4 (classm.f4952.2 $0 / $37,231, no investment interest). |
| deepseek | transcription | 23, 24, 32 | model error | each 1,560/1,599; 39 value (13 completed) | i1040sd p. 15, skip after line 22 | Nonzero amounts on skipped lines. |
| deepseek | transcription | 25, 29, 30, 31, 33, 40 | representation | each 1,599/1,599 | i1040sd pp. 15–16, skips after lines 22, 32 and 34 | 0 by derivation or by the candidate's own gate on every skip return. |
| deepseek | transcription | 26, 27, 28 | model error | 364 / 1,267 / 1,267 of 1,599; 516 / 332 / 332 value | i1040sd p. 15, skip after line 22 | Nonzero amounts on skipped lines; line 26 refusals scope, unknowns representation. |
| deepseek | transcription | 35 | model error | 1,129/1,599; 9 value (4 completed), 459 project-refuses, 2 project-unknown | i1040sd pp. 15–16, skips after lines 22 and 32 | As the Claude line 35. |
| deepseek | transcription | 36, 37, 38 | model error | 781 / 816 / 1,418 of 1,599; 709 / 674 / 72 value, 109 candidate-unknown | i1040sd p. 16, skip after line 34 (and 32) | Nonzero amounts on skipped lines; unknowns representation. |
| deepseek | transcription | 39 | representation | 1,490/1,599; 109 candidate-unknown, no value | i1040sd p. 16, skip after line 34 | Line 35 is 0 when Schedule D line 19 is zero, so the floored difference is 0; unknowns withhold taxable income. |
| deepseek | transcription | 41 | model error | 379/1,599; 668 candidate-shows-skipped (414 completed), 7 value, 435 candidate-refuses, 110 candidate-unknown | i1040sd p. 16, skip after line 40 | Not gated; shows amounts where lines 41–43 are skipped (classm.f8889.2.deepseek $324,872.80). |
| deepseek | transcription | 42, 43 | scope | 1,054 / 1,164 of 1,599; 435 candidate-refuses (110 candidate-unknown on 42) | i1040sd p. 16, skip after line 40 | No shown value differs; candidate refusals on refused returns; unknowns representation. |
| claude, deepseek | render | 1 | scope | — | i1040sd p. 15, line 1; i1040gi pp. 91, 101 | The Form 2555 alternative is unreachable: Schedule 1 lines 8d and 24j and Schedule 1-A line 2a (sa.excluded_income) refuse. |

Findings: none. Every disputed project line stands. BUG-0160 changed no filed amount and introduced no error.
BUG-0150 check: neither fresh reply disputes a shown value of the project's lines 42 and 43. The Claude reply gates line 42 on Schedule D line 18, and DeepSeek gates line 43.

## Round 2 (superseded subject)

Round 2 (fresh replies of 2026-10-26 after BUG-0149 and BUG-0150): triage `../triage/sdtw.json`
(executable-triage-v2; 1,094 fixtures, 500 generated returns, seed 20261026, no partial records; 1,594 comparisons) and
`../triage/sdtw.deepseek.json` (state "invalid": `sdtw.line7` and `sdtw.line28` are declared NonNegDollars where the
published type is Dollars; nothing executed). Of the 36 open DeepSeek lines, 32 depend on those two lines. Lines 15,
26, 27 and 37 do not and are ruled by reading. Full ruling text:
`.transcription/proposed/round2/{transcription,render}.sdtw[.deepseek].json`; finding note in
`.transcription/proposed/round2/sdtw.findings.md`. "Skip return" means a return on which the worksheet's printed
instructions skip the line (i1040sd pp. 15–16). On every value witness for lines 23–41, the project took its skip branch
(`sdtw.after22`, `after32`, `use1250`, `use28`).

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | 3 | scope | 1,577/1,594; 17 candidate-refuses (Schedule B gates) | i1040sd p. 15, line 3 | Same line 4g; refusals only, on returns the project refuses. |
| claude | transcription | 4 | finding (BUG-0099, open) | 1,358/1,594; 139 value (project f4952.line4e, candidate 0; classm.tcw.1 $16,981), 97 candidate-refuses | i1040sd p. 15, line 4 and applicability | Project enters a Form 4952 amount when no Form 4952 is filed. Tax unchanged (line 3 is 0). |
| claude | transcription | 15 | representation | 1,594/1,594 agree | i1040sd p. 15, line 15 | The floor of a positive parameter never binds. |
| claude | transcription | 23, 24, 32 | model error | each 1,553/1,594; 39 value (classm.sdtw.2 $74,841), 2 project-refuses | i1040sd p. 15, skip after line 22 | Nonzero amounts on skipped lines. |
| claude | transcription | 26 | model error | 361/1,594; 512 value, 574 project-refuses, 147 project-unknown | i1040sd p. 15, skip after line 22 | Ceiling shown on skipped lines. The refusals (scope) and unknowns (representation) come from line 1. |
| claude | transcription | 27, 28 | model error | each 1,265/1,594; 327 value (classm.f2441.1.deepseek $26,375), 2 project-refuses | i1040sd p. 15, skip after line 22 | Nonzero amounts on skipped lines. |
| claude | transcription | 25, 29, 31, 34, 39, 40 | scope | each 1,592/1,594; 2 project-refuses | i1040sd pp. 15–16, skips after lines 22, 32 and 34 | 0 by derivation on skip returns; refusals only. |
| claude | transcription | 35 | model error | 1,237/1,594; 9 value (classm.s8812.2 $1,585), 346 project-refuses, 2 project-unknown | i1040sd pp. 15–16, skips after lines 22 and 32 | Line 19 positive, but the line is skipped earlier. |
| claude | transcription | 36, 37, 38 | model error | 783 / 817 / 1,413 of 1,594; 700 / 666 / 70 value, 109 candidate-unknown, 2 project-refuses | i1040sd p. 16, skip after line 34 | Nonzero amounts on skipped lines. The unknowns are fixtures without s1a.tips (representation). |
| claude | transcription | 41 | model error | 379/1,594; 661 candidate-shows-skipped, 6 value, 436 candidate-refuses, 110 candidate-unknown, 2 project-refuses | i1040sd p. 16, skip after line 40 | Shows amounts where the source skips 41–43, against the BUG-0150 fix. |
| claude | transcription | 42, 43 | scope | each 1,156/1,594; 436 candidate-refuses, 2 project-refuses | i1040sd p. 16, skip after line 40 | The candidate applies the line-18 skip, as the BUG-0150 fix does; refusals only. |
| deepseek | transcription | 7, 9, 10, 12–14, 17, 18, 20–25, 28–36, 38–45, 47 (32 lines) | model error | not executed | host type check (`sdtw.line7`, `sdtw.line28`) | Ruled on the validation failure in the expression or its closure, not the tax reading. |
| deepseek | transcription | 15 | representation | not executed; the identical Claude expression agrees 1,594/1,594 | i1040sd p. 15, line 15 | The floor is a no-op. |
| deepseek | transcription | 26, 27, 37 | model error | not executed; identical Claude lines: 512 / 327 / 666 value | i1040sd pp. 15–16, skips after lines 22 and 34 | Nonzero amounts on skipped lines. |
| claude, deepseek | render | 1 | scope | — | i1040sd p. 15, line 1; i1040gi pp. 36, 91 | The Form 2555 alternative is unreachable: Schedule 1 lines 8d and 24j are refused. |

BUG-0150 check: both families' fresh lines 42 and 43 skip when Schedule D line 18 is zero (DeepSeek's only on its
invalid line 43), which is the fix. The Claude line 41 does not apply the skip and is a model error. The fix follows
i1040sd p. 16 ("If Schedule D, line 18, is zero or blank, skip lines 41 through 43"). When lines 18 and 19 are both
zero, the hidden line 41 equals line 1 by derivation, so line 42 is 0 and lines 43, 45 and 47 are unchanged. No new error
was found. BUG-0149 check: line 11 agrees in both families.

Findings: line 4 (Claude log), a Form 4952 line 4e amount entered when no Form 4952 is filed. This is the already
recorded, still-open BUG-0099, not a new defect; see `.transcription/proposed/round2/sdtw.findings.md`. No new
finding.

## Round 1 (superseded subject)

Triage records: `../triage/sdtw.json` (executable-triage-v1;
1,083 fixtures, 500 generated returns, seed 20261026, no partial records) and
`../triage/sdtw.deepseek.json` (state invalid: `sdtw.line28` and `sdtw.line34` declare NonNegDollars
where the published type is Dollars; the open DeepSeek lines 23–27 and 35–40 do not depend on them and
are ruled by reading). Full ruling text is in `.transcription/proposed/sdtw.json` and
`sdtw.deepseek.json`. "Skip return" means a return on which the worksheet's printed instructions skip
the line (i1040sd pp. 15–16).

| family | line | class | triage | deciding source | reason |
| --- | --- | --- | --- | --- | --- |
| claude | 15 | representation | 1,583/1,583 agree | i1040sd p. 15, line 15 | The floor at zero of a positive parameter never binds. |
| claude | 25, 29, 30, 31, 32, 34 | scope | each 1,581/1,583 agree; 2 project-refuses | i1040sd p. 15, skip after line 22 (p. 16 after line 32 for 34) | On skip returns the candidate's line is 0 by derivation; the 2 refusals are cited taxable-income gates where the candidate is unknown. |
| claude | 26 | model error | 358/1,583; 507 value, 568 project-refuses, 150 project-unknown | i1040sd p. 15, skip after line 22 | Nonzero ceiling on a skipped line (skipped-line policy); the refusals (scope) and unknowns (representation) come from taxable income. |
| claude | 27, 28 | model error | each 1,258/1,583; 323 value, 2 project-refuses | i1040sd p. 15, skip after line 22 | Nonzero amounts (= line 1) on skipped lines, including returns that use the worksheet (classm.sdtw.2); the refusals are scope. |
| claude | 36, 37, 38 | model error | 779 / 811 / 1,402 of 1,583; 690 / 658 / 67 value, 112 candidate-unknown, 2 project-refuses | i1040sd p. 16, skip after line 34 | Nonzero amounts on skipped lines (classm.sdtw.2, classm.tcw.1); the unknowns are records with taxable income unknown (representation). |
| claude | 39, 40 | representation | each 1,469/1,583; 112 candidate-unknown, 2 project-refuses | i1040sd p. 16, skip after line 34 | No value differs; the unknowns are records with taxable income unknown. |
| claude | 41 | finding | 1,160/1,583; 309 value, 112 project-unknown, 2 project-refuses | i1040sd p. 16, skip after line 40 | The project completes line 41 (= line 1) when Schedule D line 18 is zero, e.g. sales.select.sdtw.election $50,000; lines 42–43 and 47 are unchanged. |
| claude | 42, 43 | representation | each 1,469/1,583; 112 project-unknown, 2 project-refuses | i1040sd p. 16, skip after line 40 | No value differs; the unknowns are records with taxable income unknown. |
| deepseek | 23, 24 | model error | not executable (reply invalid elsewhere) | i1040sd p. 15, skip after line 22 | Nonzero amounts on skipped lines (classm.sdtw.2 $27,569; stage4.sdtw.skip22 $40,000, by read-only evaluation of the same expressions). |
| deepseek | 25 | representation | not executable | i1040sd p. 15, skip after line 22 | Line 25 is 0 on every skip return by derivation, the same as the project. |
| deepseek | 26, 27 | model error | not executable | i1040sd p. 15, skip after line 22 | Nonzero amounts on skipped lines; the Claude candidate's identical lines were executed with the same values. |
| deepseek | 35, 36, 37, 38 | model error | not executable | i1040sd p. 16, skip after line 34 | Nonzero amounts on skipped lines (line 35: classm.s8812.2 $1,585; 36–38 the same as the Claude lines); line 39 stays 0. |
| deepseek | 39, 40 | representation | not executable | i1040sd p. 16, skip after line 34 | Its values equal the project's on every input by derivation. |

Findings: line 41 (Claude log), completed on a skipped line when Schedule D line 18 is zero; see
`.transcription/proposed/sdtw.findings.md`. A bank-wide check of the project's lines 23–43 against all
four printed skips found no other project line with a nonzero amount on a skipped line. The
sd.line18/sd.line19 finding (see `sd.md`) also shows on worksheet lines 11 and 35–43 of Form 4952
returns; it is ruled under sd.
