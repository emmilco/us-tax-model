# Adjudication — eic

Method: `README.md` in this directory.

## Stage 19 round 2

Fresh reviews of 2026-10-29 (Claude claude-opus-5-5 and deepseek-flash, transcription; Claude class M). eic was not
reviewed in Stage 19 round 1; its only change since round 4 is BUG-0195, the wording of `eic.us_home` ("Was your main
home, and your spouse's if filing a joint return, in the United States for more than half of 2025?", i1040gi p. 42,
Step 4, question 3, now quoted by the label and question), which changes no expression. Triage `../triage/eic.json`
(executable-triage-v2; 1,325 fixtures, 500 generated returns seed 20261026, 110 partial records; 1,935 comparisons). The
deepseek reply fails the project schema (`eic.self_employed`, `eic.separated_box`: any/all lists of bare ids), so
`../triage/eic.deepseek.json` is `invalid` and its lines are ruled by reading. Rulings in
`.transcription/proposed/stage19/round2/` (`transcription.eic[.deepseek].json`, `classm.eic.json`). Round 4 reasoning
was reused and re-checked against the new replies and witnesses. No difference turns on `eic.us_home`.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | eic.credit | model error | 1,830/1,935; 0 value; 38 candidate-unknown (8 completed), 55 candidate-refuses, 9 project-unknown, 3 project-refuses | i1040gi p. 40, Step 1 q1 | Child count needed above every Step 1 limit (classm.f8995a.1, dependent.us_half); refusals scope; project unknowns withhold tax-exempt interest. |
| claude | transcription | eic.check_27c | model error | 1,847/1,935; 0 value; 46 candidate-unknown (13 completed), 32 candidate-refuses, 10 project-refuses | i1040gi p. 43, Line 27c; p. 40 | Same unknowns; the round 4 household.married reading is gone; refusals on refused returns. |
| claude | transcription | eic.separated_box | model error | 1,891/1,935; 0 value; 3 candidate-unknown (1 completed), 32 candidate-refuses, 9 project-refuses | i1040gi p. 41, Step 3 q3 and q6; p. 44 | Same terms as the project (amb.2025.separated_spouses_box); unknowns as eic.credit (audit.household.hoh_married_no_community_property). |
| claude | transcription | 4b | model error | 661/1,935; 1,227 candidate-shows-skipped (641 completed), 21 candidate-unknown, 8 candidate-refuses, 18 project-refuses | i1040gi p. 47; p. 42, Step 5 q2 | Shown for filers who never use Worksheet B (classm.f2441.2.deepseek $85,000). |
| claude | transcription | 2 | model error | 1,683/1,935; 66 candidate-shows-skipped (22 completed), 46 candidate-unknown, 96 project-unknown (all refused), 44 refusals | i1040gi p. 40; p. 46 | Shown after STOPs (classm.f4952.2.deepseek $308); project unknowns are "no band" lookups where `eic.eligible` itself refuses (T-070 (2)). |
| claude | transcription | 5 | model error | 1,608/1,935; 242 candidate-shows-skipped (151 completed), 50 candidate-unknown, 35 refusals | i1040gi p. 46, lines 4 and 5 | Figured and shown when line 4 is Yes (classm.f2441.1.deepseek $65). |
| claude | transcription | 6 (eic.line6) | model error | 1,824/1,935; 25 candidate-shows-skipped (10 completed), 48 candidate-unknown, 38 refusals | i1040gi pp. 40, 46 | Shown after STOPs (stage13.eic_spouse_no_ssn $649). |
| deepseek | transcription | eic.self_employed | model error | invalid (schema) | i1040gi p. 42, Step 5 q2 | Declaration fails validation; the reading is otherwise the project's Schedule C test. |
| deepseek | transcription | eic.credit | model error | invalid; by reading | i1040gi p. 40, Steps 1 and 2; p. 42, Step 4 | No Steps 1 to 5 at all: table credit for every filer. |
| deepseek | transcription | eic.check_27c | model error | invalid; by reading | i1040gi p. 43, Line 27c | Checked whenever the credit is zero (as round 4). |
| deepseek | transcription | eic.separated_box | model error | invalid (schema) | i1040gi p. 41, Step 3 q3 and q6 | Declaration fails; no Steps 1 and 2, no household.married. |
| deepseek | transcription | eic.clergy | scope | invalid; by reading | i1040gi p. 43, Line 27b | Constant no; the project refuses on scope.schedule1. |
| deepseek | transcription | 1, 2, 5, 6 (eic.line6) | model error | invalid; by reading | i1040gi pp. 40, 42, 46 | Figured and shown on every return, after any STOP; line 1 omits the merged Worksheet B line 6. |
| claude | class M | classm.eic.2, (Step 5, 1) to (Step 5, 5) | model error (drop) | reply blank, project $31,939.00 / $0.00 | i1040gi p. 40, Step 1 q1 | Reply format "Step 5, n" (T-070 (1)); its blank is the source reading; the project's Step 5 helpers shown on a return that never reaches Step 5 are open T-067 (BUG-0151). |
| claude | class M | classm.eic.4 and classm.eic.6, (Step 5, 1) to (Step 5, 5) | model error | reply values equal the project's ($5,137.00 / $0.00) | i1040gi p. 42, Step 5 | Reply format only (T-070 (1)); nothing to drop. |
| claude | class M | classm.eic.5, 6 (eic.line6) | representation (drop) | model $0.00; project hidden (internal $4,080.00) | i1040gi p. 40, Step 1 q2 | No valid SSN: line 6 hidden, credit $0.00; class M compared the hidden value (T-079 (1)). |

Class M check (BUG-0195): none of the 16 disagreements turns on the reworded question; `eic.us_home` is Yes on cases 2, 4
and 5 and No on case 6, whose return is refused (`sa.excluded_income`).

Findings: none. Every disputed project line stands; the BUG-0195 wording matches the source and introduced no error.

## Round 4 (superseded subject)

Fresh reviews of 2026-10-27 (Claude claude-opus-5-5 and deepseek-flash). The only eic change since round 3 is T-071:
`eic.separated_box` now links `amb.2025.separated_spouses_box`, which changes no value. The batch also changed person and
f1040 inputs upstream. Triage records `../triage/eic.json` (1,747 comparisons, 136 partial records) and
`../triage/eic.deepseek.json` (1,739 comparisons, 128 partial records), both executable-triage-v2 with 1,111 fixtures and
500 generated returns seed 20261026. The full ruling text is in `.transcription/proposed/round4/transcription.eic[.deepseek].json`.
Both reviewers were given i1040gi pp. 40–60, so there is no page gap. The round 3 rulings were reused as prior reasoning
and re-checked against the new replies and witnesses. Value differences on refused returns, where `shown_when` itself
refuses, are ruled scope, as in round 3.

T-071 check: the link matches the expression (the box only on the Step 3, question 6 "No" path) and the register's chosen
reading. Worksheet B check: the project checks 27c on the line 4b STOP ("If line 4b is zero or less, STOP ... Check the box
on Form 1040 or 1040-SR, line 27c", p. 47; the column text misplaces "27c") through eligibility with line 2 of zero
(stage14.eic.wsb_stop_27c).

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | eic.credit | model error | 1,630/1,747; 0 value; 40 candidate-unknown (8 completed), 65 candidate-refuses, 9 project-unknown, 3 project-refuses | i1040gi p. 40, Step 1 q1 | Child count needed above every Step 1 limit (classm.f4952.1); refusals scope; project unknowns withhold tax-exempt interest (representation). |
| claude | transcription | eic.check_27c | model error | 1,653/1,747; 5 value, 50 candidate-unknown (13 completed), 35 candidate-refuses, 4 project-refuses | i1040gi p. 43, Line 27c; p. 41, Step 4 q1 | Same unknowns; MFS read through household.married (generated 71, refused). |
| claude | transcription | eic.separated_box | model error | 1,702/1,747; 3 value, 3 candidate-unknown (1 completed), 35 candidate-refuses, 4 project-refuses | i1040gi p. 41, Step 3 q6; p. 44 | Same unknowns (audit.household.hoh_married_no_community_property); MFS reading (classm.eic.6, refused). |
| claude | transcription | eic.clergy | representation | 1,747/1,747 | i1040gi p. 43, Line 27b | Constant no behind scope.schedule1. |
| claude | transcription | 4b | model error | 639/1,747; 1,080 candidate-shows-skipped (510 completed), 21 candidate-unknown, 7 candidate-refuses | i1040gi p. 47, Worksheet B use; p. 42, Step 5 q2 | Shown for filers who never use Worksheet B (classm.f2441.2.deepseek $85,000). |
| claude | transcription | 2 | model error | 1,126/1,747; 537 candidate-unknown (220 completed), 53 candidate-shows-skipped, 31 candidate-refuses | i1040gi p. 40, Step 1 q1; p. 46 | Table lookups above the table after STOPs; shown after STOPs (classm.dependent.5 $649). |
| claude | transcription | 5 | model error | 1,321/1,747; 362 candidate-unknown, 15 candidate-shows-skipped (7 completed), 41 candidate-refuses, 4 value, 4 project-refuses | i1040gi p. 46, lines 4–5; p. 47, line 5 | Shown after STOPs (stage14.eic.wsb_line5_stop_27c $83); values are refused returns (scope). |
| claude | transcription | 6 (eic.line6) | model error | 1,038/1,747; 648 candidate-unknown, 22 candidate-shows-skipped (10 completed), 39 candidate-refuses | i1040gi pp. 40, 46 | Shown after STOPs (stage13.eic_spouse_no_ssn $649). |
| deepseek | transcription | eic.self_employed | model error | 696/1,739; 150 value (42 completed), 820 candidate-unknown, 73 candidate-refuses | i1040gi p. 42, Step 5 q2 | Schedule SE filers only, plus Schedule 1-A tip counts and any se_screen answer; misses Schedule C losses. |
| deepseek | transcription | eic.credit | model error | 1,518/1,739; 13 value (10 completed), 161 candidate-unknown, 30 candidate-refuses, 15 project-refuses, 2 project-unknown | i1040gi p. 42 Step 5 q2; p. 47 | Worksheet A on wages for Schedule C filers (classm.f8880.1 $0 / $2,798; classm.s8812.3 $300 / $0). |
| deepseek | transcription | eic.check_27c | model error | 596/1,739; 933 value (441 completed) | i1040gi p. 43, Line 27c; p. 40, Step 1 q1 | Checks 27c whenever the credit is zero (classm.f2441.2.deepseek). |
| deepseek | transcription | eic.separated_box | model error | 1,300/1,739; 430 project-refuses, 4 value, 3 candidate-unknown | i1040gi p. 41, Step 3 q6; p. 40, Step 1 | Box without Steps 1 and 2 (generated 72, line 11b $274,465). |
| deepseek | transcription | eic.clergy | model error | 901/1,739; 795 candidate-unknown, 26 value (8 completed), 17 project-refuses | i1040gi p. 43, Line 27b | Any se_screen answer read as clergy (classm.f5695.2). |
| deepseek | transcription | 1 | model error | 451/1,739; 773 candidate-unknown, 306 candidate-shows-skipped, 101 value, 87 project-refuses, 21 candidate-refuses | i1040gi pp. 40, 42, 46 | Shown after STOPs; Worksheet B values on the merged line interface gap. |
| deepseek | transcription | 2 | model error | 361/1,739; 1,153 candidate-unknown, 46 candidate-shows-skipped, 24 value, 57 candidate-refuses, 82 project-refuses, 16 project-unknown | i1040gi p. 46 | Shown after STOPs (classm.sd.1 $2,798); stage14.eic.wsb_loss $614 / $649 merged line and routing. |
| deepseek | transcription | 5 | model error | 945/1,739; 654 candidate-unknown, 102 candidate-shows-skipped (74 completed), 32 candidate-refuses, 6 value | i1040gi p. 46, lines 4–5 | Looks up line 5 on every return (classm.f2441.1.deepseek $65). |
| deepseek | transcription | 6 (eic.line6) | model error | 558/1,739; 1,115 candidate-unknown, 43 candidate-refuses, 15 value, 6 candidate-shows-skipped, 2 project-refuses | i1040gi pp. 40, 46 | As lines 2 and 5; refuses completed returns on its se_screen clergy gate. |

Findings: none. Every disputed project line stands, and the T-071 change is correct.

## Round 3 (superseded subject)

Fresh reviews of 2026-10-26 (Claude claude-opus-5-5 and deepseek-flash) against the subject after BUG-0156. That fix
hides Worksheet A lines 3 and 5 after the line 2 STOP (`eic.show3`, `eic.show5`) and Worksheet B lines 4b and 6 unless
they are reached (`eic.show_wsb4b`, `eic.show_wsb6`, new `eic.reached_step5`), and relabels `eic.credit`. Triage records
`../triage/eic.json` (1,731 comparisons, 132 partial records) and `../triage/eic.deepseek.json` (1,725 comparisons, 126
partial records). Both are executable-triage-v2, with 1,099 fixtures and 500 generated returns seed 20261026. Full ruling
text: `.transcription/proposed/round3/transcription.eic[.deepseek].json`, `render.eic.deepseek.json` and
`classm.eic.json`. Render eic (Claude) has no open section. Both transcription reviewers were given i1040gi pp. 40–60;
no page gap. Triage counts a line as shown when its `shown_when` itself refuses or is unknown (classm.sc.1:
`eic.eligible` refuses on an HSA gate). The value differences on refused returns are therefore partly display
artifacts with no filed amount, and they are ruled scope.

BUG-0156 check: the fix is right. On every inspected witness, a candidate value that the project hides is on a return where
the source STOPs or skips (Step 1 question 1, Step 1 question 2, line 4 Yes) or the filer never reaches the worksheet.
`eic.show3`/`show5` require line 2 above zero and `eic.show_wsb4b` requires Step 5, so these lines cannot show after those
STOPs. Worksheet A lines 1, 2 and 6 and Worksheet B line 6 still show $0 for a Worksheet B filer whose line 4b is zero or
less (STOP), which the zero rule permits. The Step 5 lines are helpers that `shown_when` cannot hide (T-067). No
reviewed case shows a nonzero project amount on them without reaching Step 5 (classm.eic.2 shows $0.00), so no T-067
ruling arose.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | eic.credit | model error | 1,628/1,731; 0 value; 41 candidate-unknown (8 completed), 51 candidate-refuses, 8 project-unknown, 3 project-refuses | i1040gi p. 40, Step 1 q1 | Needs the child count and line 2a above every Step 1 limit (classm.f4952.1); refusals scope; project unknowns withhold line 2a (representation). |
| claude | transcription | eic.check_27c | model error | 1,631/1,731; 0 value; 48 candidate-unknown (13 completed), 51 candidate-refuses, 1 project-refuses | i1040gi p. 43, Line 27c; p. 40, Step 1 q1 | Same unknowns through eic.h_pre; refusals scope (sa.dependent cited). |
| claude | transcription | eic.separated_box | model error | 1,675/1,731; 0 value; 3 candidate-unknown (1 completed), 51 candidate-refuses, 2 project-refuses | i1040gi p. 41, Step 3 q6; p. 44 | Married test now right; same eic.h_pre unknowns (audit.household.hoh_married_no_community_property). |
| claude | transcription | eic.clergy | representation | 1,731/1,731 | i1040gi p. 43, Line 27b | Constant no behind scope.schedule1, as the project. |
| claude | transcription | 1 | model error | 724/1,731; 825 candidate-shows-skipped (347 completed), 104 value, 74 project-refuses, 4 candidate-refuses | i1040gi p. 40 Step 1 q1; p. 46 Worksheet A use | Shown after STOPs (classm.f2441.2.deepseek $85,000); Worksheet B values on the merged line are an interface gap (classm.scveh.3); refusals scope. |
| claude | transcription | 2 | model error | 1,375/1,731; 64 candidate-shows-skipped, 44 value, 49 candidate-unknown, 26 candidate-refuses, 101 project-unknown, 72 project-refuses | i1040gi p. 46, Worksheet A use and line 2 | Shown after STOPs (classm.sd.1 $2,798); merged-line values interface gap (classm.s8812.3 $300 / $0); refused-return differences scope. |
| claude | transcription | 5 | model error | 1,546/1,731; 101 candidate-shows-skipped (70 completed), 51 candidate-unknown, 27 candidate-refuses, 6 value | i1040gi p. 46, lines 2, 4 and 5 | Shown after line 4 Yes and STOPs (classm.f2441.1.deepseek $65); the 6 values are refused returns where eic.show5 refuses (scope). |
| claude | transcription | 6 (eic.line6) | model error | 1,596/1,731; 24 candidate-shows-skipped, 32 value, 49 candidate-unknown, 30 candidate-refuses | i1040gi pp. 40, 46 | Shown after STOPs (stage13.eic_spouse_no_ssn $649); merged-line values interface gap. |
| deepseek | transcription | eic.self_employed | representation | 1,725/1,725 | i1040gi p. 42, Step 5 q2 | Statutory-employee and clergy additions are refused elsewhere. |
| deepseek | transcription | eic.credit | model error | 665/1,725; 12 value, 254 candidate-refuses (126 completed), 563 candidate-unknown, 230 project-refuses | i1040gi pp. 40–42, Steps 1, 2 and 4 | No Step 1, 2 or age tests (stage9.eic.investment_income $0 / $1,369); refuses Worksheet B though person.eic_se is published. |
| deepseek | transcription | eic.check_27c | model error | 441/1,725; 240 value (118 completed), 254 candidate-refuses, 541 candidate-unknown, 248 project-refuses | i1040gi p. 43, Line 27c; p. 40, Step 1 q1 | Checks 27c on Worksheet A line 2 zero after a Step 1 q1 STOP (classm.f5695.4 no / yes). |
| deepseek | transcription | eic.separated_box | model error | 977/1,725; 144 value (35 completed), 182 candidate-unknown, 422 project-refuses | i1040gi p. 44; p. 41, Step 3 q3 | Filing status only: unmarried head of household gets the box (classm.f5695.1). |
| deepseek | transcription | eic.clergy | scope | 1,676/1,725; 0 value; 15 project-refuses, 34 project-unknown | i1040gi p. 43, Line 27b | Project refuses on the cited scope.schedule1 screen; unknowns are records without it (representation). |
| deepseek | transcription | 4b | model error | 491/1,725; 905 candidate-shows-skipped (418 completed), 297 candidate-refuses (127 completed), 21 candidate-unknown, 11 project-refuses | i1040gi p. 47, Worksheet B use | Shown for filers who never reach Worksheet B (classm.f2441.2.deepseek $85,000); refuses Worksheet B. |
| deepseek | transcription | 1 | model error | 698/1,725; 853 candidate-shows-skipped (363 completed), 92 value, 78 project-refuses, 4 candidate-refuses | i1040gi p. 40 Step 1 q1; p. 46 | As the Claude line 1. |
| deepseek | transcription | 2 | model error | 698/1,725; 819 candidate-unknown (307 completed), 68 candidate-shows-skipped, 20 value, 39 candidate-refuses, 74 project-refuses, 7 project-unknown | i1040gi p. 46 | Table lookup above the table with no outside-the-table case after a Step 1 STOP; shown after STOPs; merged-line values interface gap. |
| deepseek | transcription | 5 | model error | 757/1,725; 184 candidate-shows-skipped (114 completed), 754 candidate-unknown, 30 candidate-refuses | i1040gi p. 46, lines 4 and 5 | Looks up line 5 on every return (classm.f2441.1.deepseek $65). |
| deepseek | transcription | 6 (eic.line6) | model error | 826/1,725; 830 candidate-unknown, 24 candidate-shows-skipped, 11 value, 34 candidate-refuses | i1040gi pp. 40, 46 | As lines 2 and 5; merged-line values interface gap. |
| deepseek | render | 1 | representation | MISMATCH: Worksheet B line 6 on line 1 | i1040gi pp. 46, 48 | The English states the merge ("or Worksheet B, line 6"); lines 7–11 of Worksheet B repeat Worksheet A lines 2–6. |
| claude | classm | classm.eic.1, .2, .9 — (Step 5, 1) to (Step 5, 5) (15) | model error | MISSING: reply named "Step 5, n" without parentheses; values equal the project (eic.1, eic.9) or blank where Step 5 is not reached (eic.2, project $0.00) | i1040gi p. 42, Step 5 worksheet; p. 40, Step 1 q1 | Reply format, not the tax reading; nothing to drop; no T-067 finding (no nonzero amount on an unreached line). |
| claude | classm | classm.eic.9 — 5 | model error (drop) | project $281.00 / model $1,819.00 | i1040gi p. 56, EIC Table row 48,650–48,700 | Model read the two-children column; the line is also after the Worksheet B line 5 STOP. |

Findings: none. Every disputed project line stands, and the BUG-0156 fix changed no filed amount and introduced no error.

## Round 2 (superseded subject)

Round 2 rules the fresh 2026-10-26 replies against the subject changed by BUG-0152.

Triage records: `../triage/eic.json`, `../triage/eic.deepseek.json` (executable-triage-v2; 1,094 fixtures, 500 generated
returns, seed 20261026, 136 partial records; 1,730 comparisons). Full ruling text is in
`.transcription/proposed/round2/transcription.eic.json` and `transcription.eic.deepseek.json`; findings in
`.transcription/proposed/round2/eic.findings.md`. Both reviewers were given i1040gi pp. 40-60, which hold every deciding
sentence; no interface gap for missing pages. Render eic and eic.deepseek have no open sections.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | eic.self_employed | model error | 891/1,730 agree; 802 candidate-unknown, 37 candidate-refuses | i1040gi p. 42, Step 5 q2 | Candidate needs person.se_screen of filers without a Schedule C, never asked; clergy cases are behind scope.schedule1. |
| claude | transcription | eic.credit | model error | 1,540/1,730; 139 cand-unknown, 32 cand-refuses, 10 proj-unknown, 9 proj-refuses; 0 value | i1040gi pp. 40-46, STOPs | Same se_screen unknowns; refusals on refused returns or cited gates; project unknowns withhold line 2a. |
| claude | transcription | eic.check_27c | model error | 1,551/1,730; 148 cand-unknown, 17 cand-refuses, 9 proj-refuses, 5 value | i1040gi p. 41, Step 4 q1; p. 43, Line 27c | Candidate makes an MFS filer's "married" depend on household.married (generated 71). |
| claude | transcription | eic.separated_box | model error | 1,699/1,730; 17 cand-refuses, 8 proj-refuses, 3 value, 3 cand-unknown | i1040gi p. 44, Special rule for separated spouses | Same MFS reading (classm.eic.7); needs dependent.us_half above every Step 1 limit. |
| claude | transcription | eic.clergy | model error | 916/1,730; 786 cand-unknown, 28 cand-refuses | i1040gi p. 43, Line 27b | Adds the se_screen gate; same unknowns. |
| claude | transcription | 4b | finding | 936/1,730; 764 cand-unknown, 22 cand-refuses, 8 proj-refuses; 0 value | i1040gi p. 47, Worksheet B use and line 4b; p. 42 Step 5 | Candidate se_screen unknowns; project shows 4b on every return (R2-F2). |
| claude | transcription | 1 | model error | 458/1,730; 764 cand-unknown, 313 cand-shows-skipped, 99 value, 70 proj-refuses, 26 cand-refuses | i1040gi p. 43 Step 6; p. 46 Worksheet A use | Shows line 1 after STOPs and Worksheet A for Worksheet B filers; merged-line differences interface gap. |
| claude | transcription | 2 | model error | 692/1,730; 748 cand-unknown, 89 proj-unknown, 77 proj-refuses, 47 cand-shows-skipped, 41 cand-refuses, 36 value | i1040gi p. 46, Worksheet A | As line 1; classm.s8812.3 ($300 vs $0) is the merged-line interface gap. |
| claude | transcription | 5 | finding | 1,544/1,730; 126 cand-unknown, 38 cand-refuses, 12 cand-shows-skipped, 6 proj-refuses, 4 value | i1040gi p. 46, line 2 STOP; lines 4-5 | Candidate shows line 5 after STOPs; project shows lines 3 and 5 after the line 2 STOP (R2-F1). |
| claude | transcription | 6 (eic.line6) | model error | 983/1,730; 677 cand-unknown, 35 cand-refuses, 23 value, 6 cand-shows-skipped, 6 proj-refuses | i1040gi p. 46, Worksheet A use, line 6 | As line 2. |
| deepseek | transcription | eic.self_employed | model error | 898/1,730; 808 cand-unknown, 24 value | i1040gi p. 42, Step 5 q2 | Treats any se_screen answer as clergy. |
| deepseek | transcription | eic.credit | model error | 1,420/1,730; 137 cand-unknown, 68 proj-refuses, 56 proj-unknown, 44 cand-refuses, 5 value | i1040gi p. 41 Step 4 q1; p. 42 Step 5 q2; p. 47 | Stops every HOH at Step 4 q1, counts a child without SSN as none, refuses or skips Worksheet B. |
| deepseek | transcription | eic.check_27c | model error | 334/1,730; 876 value, 380 proj-refuses, 57 proj-unknown, 48 cand-unknown, 35 cand-refuses | i1040gi p. 40, Step 1 q1 | Checks 27c on Worksheet A line 2 zero after the Step 1 question 1 STOP, which has no 27c instruction. |
| deepseek | transcription | eic.separated_box | model error | 1,122/1,730; 415 proj-refuses, 128 cand-unknown, 59 value, 6 cand-refuses | i1040gi p. 44; p. 41, Step 3 q3 | Status only: unmarried HOH gets the box; household.married was in the interface. |
| deepseek | transcription | eic.clergy | model error | 901/1,730; 786 cand-unknown, 28 value, 15 proj-refuses | i1040gi p. 43, Line 27b | Every se_screen answer read as clergy. |
| deepseek | transcription | 4b | finding | 615/1,730; 764 cand-unknown, 312 cand-refuses, 39 proj-refuses | i1040gi p. 47, Part 2 and line 4b | Candidate refuses Worksheet B; project shows 4b on every return (R2-F2). |
| deepseek | transcription | 1 | model error | 698/1,730; 831 cand-shows-skipped, 99 value, 97 proj-refuses, 5 cand-refuses | i1040gi p. 42 Step 5 q2; p. 46 | Shows line 1 after STOPs; ignores Worksheet B. |
| deepseek | transcription | 2 | model error | 1,356/1,730; 105 proj-unknown, 90 proj-refuses, 64 cand-shows-skipped, 49 cand-unknown, 35 value, 31 cand-refuses | i1040gi p. 46 | As line 1; needs us_half the source does not need. |
| deepseek | transcription | 5 | finding | 1,460/1,730; 184 cand-shows-skipped, 49 cand-unknown, 35 cand-refuses, 2 proj-refuses | i1040gi p. 46, line 2 STOP; lines 4-5 | Candidate's own shown_when omits the STOPs (classm.eic.8); project R2-F1. Triage ignores candidate shown_when. |
| deepseek | transcription | 6 (eic.line6) | model error | 1,600/1,730; 49 cand-unknown, 38 cand-refuses, 23 value, 20 cand-shows-skipped | i1040gi p. 46 | Shows line 6 after STOPs; Worksheet A for Worksheet B filers. |

Findings: R2-F1 (Worksheet A lines 3 and 5 shown after "If line 2 is zero, STOP", also after the Worksheet B line 4b STOP)
and R2-F2 (Step 5 worksheet lines and Worksheet B lines 4b and 6 shown on returns that STOP before Step 5, on filers who do
not use Worksheet B, and line 6 after the Worksheet B line 5 STOP); both gaps left by BUG-0152, no filed amount changes.

## Round 1 (superseded subject)

Triage records: executable-triage-v1 (1,083 fixtures, 500 generated returns, seed 20261026, 134 partial records; 1,717
comparisons). Full ruling text is in `.transcription/proposed/eic.json` and `eic.deepseek.json`; findings in
`.transcription/proposed/eic.findings.md`.

| family | line | class | triage | deciding source | reason |
| --- | --- | --- | --- | --- | --- |
| claude | eic.self_employed | scope | 1,682/1,717 agree; 14 candidate-refuses, 21 candidate-unknown | i1040gi p. 42, Step 5 question 2 | Extra scope.schedule1 branch: refusals the project makes on that screen; unknowns on fixtures omitting an always-asked screen. |
| claude | eic.credit | ambiguity | 1,637/1,717 agree; 54 candidate-refuses, 13 candidate-unknown, 3 project-refuses, 10 project-unknown | i1040gi p. 46, Worksheet A line 2; p. 40, Step 1 question 1 | Below-$1 table lookup (amb.2025.eic_below_table); refusals only on Step 1 STOP returns; project refusals cited; unknowns on unreachable records. |
| claude | eic.check_27c | model error | 1,662/1,717 agree; 4 value, 13 candidate-unknown, 34 candidate-refuses, 4 project-refuses | i1040gi p. 41, Step 4 question 1 | Candidate treats MFS as not married-separate, passes Step 4 and checks 27c at Worksheet B. |
| claude | eic.separated_box | model error | 1,677/1,717 agree; 3 value, 34 candidate-refuses, 3 project-refuses | i1040gi p. 41, Step 3 questions 4 and 6 | Misses the box for MFS filers who did not share a home the last 6 months. |
| claude | 1 | finding | 1,717/1,717 agree | i1040gi p. 43, Step 6 | Equal; both compute Worksheet A on returns that STOP before it (F2). |
| claude | 2 | ambiguity | 1,434/1,717 agree; 268 candidate-unknown, 14 candidate-refuses, 1 project-refuses | i1040gi p. 46, line 2; amb.2025.eic_below_table | Below-$1 lookup; refusals scope; project also computes line 2 on stopped returns (F2, noted). |
| claude | 5 | finding | 1,717/1,717 agree | i1040gi p. 46, lines 4 and 5 | Both put a lookup on a skipped or blank line 5 (F1). |
| claude | 6 (eic.line6) | ambiguity | 1,574/1,717 agree; 143 candidate-unknown | i1040gi p. 46, line 2; amb.2025.eic_below_table | Below-$1 lookup; project line 6 nonzero on stopped returns (F2, noted). |
| deepseek | eic.self_employed | representation | 1,717/1,717 agree | i1040gi p. 42, Step 5 question 2 | Observed equivalence on the sample. |
| deepseek | eic.credit | model error | 892/1,717 agree; 18 value, 720 candidate-unknown, 58 candidate-refuses, 26 project-unknown, 3 project-refuses | i1040gi pp. 40-41, Steps 1-4 STOPs | Omits the filer-SSN, investment-income and Step 3/4 STOPs; needs off-table lookups the source never reaches. |
| deepseek | eic.check_27c | model error | 411/1,717 agree; 323 value, 624 candidate-unknown, 323 project-refuses, 35 candidate-refuses, 1 project-unknown | i1040gi p. 40, Step 1 questions 1-2 | Checks 27c on the Step 1 question 1 STOP, which carries no 27c instruction. |
| deepseek | eic.separated_box | model error | 1,274/1,717 agree; 4 value, 402 project-refuses, 34 candidate-refuses, 3 candidate-unknown | i1040gi p. 41, Step 3 questions 4 and 6 | Misses the separated-spouse box; project refusals are cited screens elsewhere. |
| deepseek | eic.clergy | model error | 894/1,717 agree; 25 value, 783 candidate-unknown, 15 project-refuses | i1040gi p. 43, Line 27b | Uses the general self-employment screen as the clergy test. |
| deepseek | 1 | finding | 1,372/1,717 agree; 265 value, 80 project-refuses | i1040gi p. 42, Step 5 question 2; p. 48, Worksheet B line 6; p. 43, Step 6 | Candidate ignores Worksheet B; project computes line 1 on stopped returns (F2). |
| deepseek | 2 | finding | 1,270/1,717 agree; 32 value, 293 candidate-unknown, 76 project-refuses, 32 project-unknown, 14 candidate-refuses | i1040gi p. 43, Step 6; p. 46, line 2 | Values inherit line 1; project line 2 nonzero or off-table on stopped returns (F2). |
| deepseek | 5 | finding | 1,529/1,717 agree; 92 value, 95 project-unknown, 1 candidate-refuses | i1040gi p. 46, lines 4 and 5 | Candidate zero on the skipped line; project carries a lookup or no value (F1). |
| deepseek | 6 (eic.line6) | finding | 1,527/1,717 agree; 20 value, 170 candidate-unknown | i1040gi p. 43, Step 6; p. 46, line 2 | Values inherit line 1; project line 6 nonzero on stopped returns (F2). |

Findings: F1 (Worksheet A line 5 not zero when skipped or blank) and F2 (Worksheet A evaluated on returns that STOP
before it; depends on reading a STOP as a skip), both under the skipped-line rule; Form 1040 line 27a is unaffected.
