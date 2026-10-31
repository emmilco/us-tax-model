# Adjudication — person

Method: `README.md` in this directory. Triage records: `../triage/person.json`, `../triage/person.deepseek.json`
(executable-triage-v1; 1,083 fixtures, 500 generated returns, seed 20261026, 1,833 partial records). Full ruling text is in
`.transcription/proposed/person.json` and `.transcription/proposed/person.deepseek.json`, for the log and sidecar.

A ruling's class is the most serious class among its difference kinds (finding, model error, interface gap, ambiguity, scope,
representation); the ruling text rules each kind. Triage evaluates the candidate's whole person graph, so a line whose own
expression matches the project can still differ through a candidate line it reads; those differences are attributed to that
line's ruling. In the deepseek-flash graph every return with a Schedule C is unevaluable because of the person.income179 cycle,
so Schedule C-dependent deepseek lines are ruled on the derivation as well as the witnesses.

Round 1 table (superseded subject):

| family | line | class | triage | deciding source | reason |
| --- | --- | --- | --- | --- | --- |
| claude | person.educator_deduction | representation | 3,363/4,647 agree; 1249 candidate-unknown, 35 project-unknown | i1040gi p. 93, line 11 | Same deduction; only the order of the two dispositive questions differs. |
| claude | person.hsa_step1 | representation | 4,257/4,647 agree; 3 candidate-unknown, 387 value | i8889 p. 7, line 6 Step 2 | Unfiltered sum differs only on non-split forms, and the sums are read only where both forms are split. |
| claude | person.hsa_share | interface gap | 4,036/4,647 agree; 30 candidate-refuses, 204 candidate-unknown, 377 value | i8889 p. 7, line 6 Steps 2-3 | Candidate reads f8889.share, whose refusal reads the sum it feeds (cycle); the interface gave share and share_raw unlabelled. Value and refusal kinds cannot reach a printed amount. |
| claude | person.sc_total | scope | 4,646/4,647 agree; 1 project-refuses | i1040sc p. 15, line 32 | Only difference is the cited Form 6198 at-risk refusal. |
| claude | Step 1 | scope | 4,646/4,647 agree; 1 project-refuses | i1040sc p. 15, line 32; p560 p. 39 | Only difference is the cited Form 6198 at-risk refusal. |
| claude | person.se_line6 | scope | 3,234/4,647 agree; 173 candidate-refuses, 1239 candidate-unknown, 1 project-refuses | i1040sse p. 1, Who Must File | Candidate screens Schedule SE items for everyone; the project screens them with a Schedule C and at scope.schedule1/other_income otherwise. |
| claude | person.se_line12 | scope | 3,234/4,647 agree; 173 candidate-refuses, 1239 candidate-unknown, 1 project-refuses | i1040sse p. 1, Who Must File | Same Schedule SE; refusal placement only. |
| claude | person.se_line13 | scope | 3,234/4,647 agree; 173 candidate-refuses, 1239 candidate-unknown, 1 project-refuses | i1040sse p. 1, Who Must File | Same Schedule SE; refusal placement only. |
| claude | Step 2 | scope | 3,234/4,647 agree; 173 candidate-refuses, 1239 candidate-unknown, 1 project-refuses | i1040sse p. 1; p560 p. 39 | Same Schedule SE line 13; refusal placement only. |
| claude | person.eic_se | scope | 3,234/4,647 agree; 173 candidate-refuses, 1239 candidate-unknown, 1 project-refuses | i1040gi EIC Worksheet B; i1040sse p. 1 | Same Worksheet B amount; refusal placement only. |
| claude | person.dc_earned | scope | 2,827/4,647 agree; 171 candidate-refuses, 1645 candidate-unknown, 4 project-refuses | i2441 p. 4, earned income | Same earned income; project refusals are cited Form 2441 gates. |
| claude | person.dc_earned_b | scope | 3,252/4,647 agree; 173 candidate-refuses, 1221 candidate-unknown, 1 project-refuses | i2441 p. 4, earned income | Same earned income; refusal placement only. |
| claude | person.sav_ineligible | ambiguity | 4,542/4,647 agree; 54 candidate-unknown, 2 project-unknown, 49 value | f8880 p. 2, Who Can Take This Credit | Asking the dependent question only when someone can claim you is the owner decision. |
| claude | person.sav_line2 | scope | 3,325/4,647 agree; 48 candidate-refuses, 1058 candidate-unknown, 69 project-refuses, 147 value | f8880 p. 2, line 2 | Value differences need person.plan without a Schedule C (not asked); refusals are cited screens or placement. |
| claude | person.ira_contrib | scope | 2,269/4,647 agree; 1 candidate-refuses, 2351 candidate-unknown, 26 project-unknown | i1040gi p. 98, line 11; p590a p. 35 | Same amount; excess screen placed differently. |
| claude | person.ira_cov | ambiguity | 4,201/4,647 agree; 46 candidate-unknown, 76 project-unknown, 324 value | i1040gi p. 96, Were You Covered | Self-employed plan read only with a Schedule C is the owner decision. |
| claude | person.ira_line2 | ambiguity | 4,375/4,647 agree; 5 candidate-refuses, 90 candidate-unknown, 71 project-unknown, 106 value | i1040gi p. 97, line 2 | Follows ira_cov; candidate MFS-apart refusal is moot because MFS is refused at scope.ready. |
| claude | person.ira_line6 | representation | 3,097/4,647 agree; 508 candidate-refuses, 1001 candidate-unknown, 12 project-refuses, 24 project-unknown, 5 value | i1040gi p. 97, line 6 | Own formula is the project's; differences inherited (s16, ira_cov, placements). |
| claude | person.ira_line7 | representation | 4,031/4,647 agree; 446 candidate-refuses, 117 candidate-unknown, 7 project-refuses, 5 project-unknown, 41 value | i1040gi pp. 97-98, line 7 | Own formula is the project's; differences inherited. |
| claude | person.ira_deduction | scope | 1,410/4,647 agree; 685 candidate-refuses, 2522 candidate-unknown, 11 project-refuses, 19 project-unknown | i1040gi p. 98, line 12 | Same line 12; refusal placement and cited Pub. 590-A refusals. |
| claude | person.ira_nondeductible | scope | 1,409/4,647 agree; 764 candidate-refuses, 2445 candidate-unknown, 10 project-refuses, 19 project-unknown | i8606 p. 9, line 1 | Same formula; inherited placements. |
| claude | person.ira_files_8606 | scope | 1,409/4,647 agree; 764 candidate-refuses, 2445 candidate-unknown, 10 project-refuses, 19 project-unknown | i8606 p. 2, Who Must File | Extra distribution-with-basis condition is screened at retirement.special. |
| claude | person.ira_8606_line2 | scope | 2,260/4,647 agree; 2349 candidate-unknown, 12 project-refuses, 26 project-unknown | i8606 p. 9, line 2 | Same basis where Form 8606 is filed; placement only. |
| claude | person.ira_dist_gate | scope | 2,328/4,647 agree; 145 candidate-refuses, 2162 candidate-unknown, 12 project-refuses | f8606 Part I question | Same answer wherever asked; placement only. |
| claude | person.ira_8606_line14 | scope | 1,372/4,647 agree; 764 candidate-refuses, 2481 candidate-unknown, 11 project-refuses, 19 project-unknown | f8606 Part I, line 14 | Same line 14; inherited placements. |
| claude | person.ira_ssb | scope | 1,480/4,647 agree; 745 candidate-refuses, 2393 candidate-unknown, 10 project-refuses, 19 project-unknown | i1040gi p. 98, line 12 | Same no-coverage deduction copy; project also refuses ira.cov_gate (cited). |
| claude | person.ira_se | scope | 2,769/4,647 agree; 466 candidate-refuses, 1405 candidate-unknown, 7 project-refuses | i1040gi p. 97, line 9 | Same line 9 part; cited plan and simple_excess refusals. |
| claude | wages | scope | 4,369/4,647 agree; 85 candidate-refuses, 193 candidate-unknown | iw2w3 p. 18; amb.2025.ss_wages | Same boxes 3+7; rrta refused at this helper rather than at person.credit. |
| claude | eligible | representation | 4,513/4,647 agree; 76 candidate-refuses, 18 candidate-unknown, 1 project-unknown, 39 value | i1040gi p. 117, line 11 | Extra over-limit conjunct is where the project refuses the credit. |
| claude | Step 6 | scope | 4,423/4,647 agree; 180 candidate-refuses, 44 candidate-unknown | p560 p. 39, Step 6 | Same amount; plan screen refused at sep_contrib in the project. |
| claude | person.s16 | model error | 2,759/4,647 agree; 378 candidate-refuses, 1391 candidate-unknown, 9 project-refuses, 110 value | p560 p. 16; i1040gi p. 93, line 16 | Allows SIMPLE salary reduction contributions beyond compensation (gen#76: $5,686.54 against a refusal). |
| deepseek | person.educator_deduction | representation | 3,363/4,647 agree; 1249 candidate-unknown, 35 project-unknown | i1040gi p. 93, line 11 | Same deduction; only the order of the two dispositive questions differs. |
| deepseek | person.hsa_step1 | scope | 4,172/4,647 agree; 86 candidate-refuses, 2 candidate-unknown, 387 value | i8889 p. 7, line 6 Step 2 | Value kind as Claude; h_hsa_unsupported_any matches the project refusal at f8889 lines 13 and 16. |
| deepseek | person.hsa_share | interface gap | 3,953/4,647 agree; 116 candidate-refuses, 201 candidate-unknown, 377 value | i8889 p. 7, line 6 Steps 2-3 | Same cycle as Claude (interface gap); other kinds unprintable or matching project refusals. |
| deepseek | person.hsa_agreed | representation | 4,445/4,647 agree; 35 candidate-unknown, 167 value | i8889 p. 7, line 6 Step 2 | Allocation is asked only within the spouse rule; differences are unreachable records. |
| deepseek | person.sc_total | scope | 3,698/4,647 agree; 49 candidate-refuses, 892 candidate-unknown, 8 project-refuses | i1040sc p. 15, line 32 | As Claude; the deepseek graph also inherits the income179 cycle. |
| deepseek | Step 1 | scope | 3,698/4,647 agree; 49 candidate-refuses, 892 candidate-unknown, 8 project-refuses | i1040sc p. 15, line 32; p560 p. 39 | As Claude; inherits the income179 cycle. |
| deepseek | person.se_line6 | scope | 2,317/4,647 agree; 220 candidate-refuses, 2103 candidate-unknown, 7 project-refuses | i1040sse p. 1, Who Must File | As Claude; inherits the income179 cycle. |
| deepseek | person.se_line12 | scope | 2,317/4,647 agree; 220 candidate-refuses, 2103 candidate-unknown, 7 project-refuses | i1040sse p. 1, Who Must File | As Claude; inherits the income179 cycle. |
| deepseek | person.se_line13 | scope | 2,317/4,647 agree; 220 candidate-refuses, 2103 candidate-unknown, 7 project-refuses | i1040sse p. 1, Who Must File | As Claude; inherits the income179 cycle. |
| deepseek | Step 2 | scope | 2,317/4,647 agree; 220 candidate-refuses, 2103 candidate-unknown, 7 project-refuses | i1040sse p. 1; p560 p. 39 | As Claude; inherits the income179 cycle. |
| deepseek | person.eic_se | scope | 2,317/4,647 agree; 220 candidate-refuses, 2103 candidate-unknown, 7 project-refuses | i1040gi EIC Worksheet B; i1040sse p. 1 | Line 3 less line 13 equals the project choice below $400 too; placement only. |
| deepseek | person.dc_earned | model error | 2,297/4,647 agree; 218 candidate-refuses, 2075 candidate-unknown, 16 project-refuses, 1 project-unknown, 40 value | i2441 p. 4, earned income | Omits line 1e taxable benefits (classm.f5695.4: $36,412.00 against $37,824.00). |
| deepseek | person.dc_earned_b | scope | 2,335/4,647 agree; 220 candidate-refuses, 2085 candidate-unknown, 7 project-refuses | i2441 p. 4, earned income | Equals lines 18/19 earned income; placement only. |
| deepseek | person.dc_has_box10 | representation | 4,647/4,647 agree; none | i2441 Part III | Agrees on every compared record. |
| deepseek | person.sav_ineligible | ambiguity | 4,542/4,647 agree; 54 candidate-unknown, 2 project-unknown, 49 value | f8880 p. 2, Who Can Take This Credit | Asking the dependent question only when someone can claim you is the owner decision. |
| deepseek | person.sav_line2 | model error | 4,455/4,647 agree; 48 candidate-refuses, 41 candidate-unknown, 69 project-refuses, 14 project-unknown, 20 value | f8880 p. 2, line 2 | Omits self-employed SIMPLE deferrals (stage14.simple.at_limit: $0.00 against $16,500.00). |
| deepseek | person.sav_line1 | scope | 2,550/4,647 agree; 1 candidate-refuses, 2065 candidate-unknown, 1 project-refuses, 30 project-unknown | f8880 p. 2; p590a p. 35 | Same amount; project refuses excess contributions (cited). |
| deepseek | person.ira_contrib | scope | 2,269/4,647 agree; 1 candidate-refuses, 2351 candidate-unknown, 26 project-unknown | i1040gi p. 98, line 11; p590a p. 35 | Same amount; excess screen placed differently. |
| deepseek | person.ira_cov | model error | 4,446/4,647 agree; 89 candidate-unknown, 5 project-unknown, 107 value | i1040gi p. 96, Were You Covered | Drops self-employed SEP/SIMPLE coverage (gen#76: False against True). |
| deepseek | person.ira_line2 | representation | 2,298/4,647 agree; 1 candidate-refuses, 1291 candidate-unknown, 3 project-unknown, 1054 value | i1040gi p. 97, line 2 | Skipped-line and ira_cov-inherited differences; printed lines 2a/2b are zero when skipped. |
| deepseek | wages | representation | 4,647/4,647 agree; none | iw2w3 p. 18; amb.2025.ss_wages | Agrees on every compared record. |
| deepseek | eligible | model error | 3,820/4,647 agree; 1 project-unknown, 826 value | i1040gi p. 117, line 11 | Tests wages against $10,918.20 instead of $176,100. |
| deepseek | Step 6 | representation | 4,647/4,647 agree; none | p560 p. 39, Step 6 | Agrees on every compared record. |
| deepseek | Step 5 | model error | 3,611/4,647 agree; 222 candidate-refuses, 807 candidate-unknown, 7 project-refuses | p560 p. 38, Rate Worksheet | Uses the plan rate, not rate/(1+rate); masked in triage by the income179 cycle. |
| deepseek | person.s16 | model error | 2,964/4,647 agree; 179 candidate-refuses, 1479 candidate-unknown, 25 project-refuses | p560 p. 16; i1040gi p. 93, line 16 | Caps SIMPLE only at line 4c, allowing employer and catch-up amounts beyond their limits. |
| deepseek | person.s179_nonlisted | model error | 4,172/4,647 agree; 2 candidate-refuses, 473 value | i4562 p. 5, line 6 column (c) | Sums the cost (sc.cost179_a), not the elected amount (classm.asset.2: $55,439.00 against $3,189.00). |
| deepseek | person.s179_listed | model error | 4,524/4,647 agree; 2 project-refuses, 121 value | i4562 p. 5, line 7 | Sums vehicle cost, not the elected amount (classm.scveh.5: $41,575.39 against $11,266.04). |
| deepseek | person.income179 | model error | 3,576/4,647 agree; 53 candidate-refuses, 939 candidate-unknown, 79 project-refuses | i4562 p. 5, line 11 | Uses line 31 after section 179 (wrong amount) and creates a cycle through s179.income. |
| deepseek | person.sc_1a | model error | 4,642/4,647 agree; 2 project-unknown, 3 value | i1040gi p. 104, Schedule 1-A line 5 | Counts statutory-employee businesses, not tips/overtime businesses. |
| deepseek | person.ira_line6 | model error | 1,897/4,647 agree; 1 candidate-refuses, 924 candidate-unknown, 1053 project-refuses, 140 project-unknown, 632 value | i1040gi p. 97, line 6 | Copies the return-level column built from this line (cycle); no line 6 computed. |
| deepseek | person.ira_line7 | model error | 2,337/4,647 agree; 1 candidate-refuses, 149 candidate-unknown, 175 project-refuses, 89 project-unknown, 1896 value | i1040gi pp. 97-98, line 7 | Copies ira.line7a/7b built from this line (cycle). |
| deepseek | person.ira_deduction | model error | 79/4,647 agree; 4556 candidate-unknown, 12 project-refuses | i1040gi p. 98, line 12 | Copies ira.line12a/12b built from this line; cycle on 4,556 records. |
| deepseek | person.ira_nondeductible | scope | 79/4,647 agree; 4557 candidate-unknown, 11 project-refuses | i8606 p. 9, line 1 | Drops line 10, equal unless contributions exceed compensation (refused); cycle inherited. |
| deepseek | person.ira_files_8606 | model error | 81/4,647 agree; 4555 candidate-unknown, 11 project-refuses | i8606 p. 2, Who Must File | Files Form 8606 on any distribution or basis change; the text needs basis above zero. |
| deepseek | person.ira_8606_line2 | scope | 2,260/4,647 agree; 2349 candidate-unknown, 12 project-refuses, 26 project-unknown | i8606 p. 9, line 2 | Same basis where filed; placement only. |
| deepseek | person.ira_dist_gate | scope | 2,312/4,647 agree; 2323 candidate-unknown, 12 project-refuses | f8606 Part I question | Same answer wherever asked. |
| deepseek | person.ira_8606_line14 | scope | 80/4,647 agree; 4555 candidate-unknown, 12 project-refuses | f8606 Part I, line 14 | Same line 14; cycle inherited. |
| deepseek | person.ira_ssb | model error | 4,035/4,647 agree; 310 candidate-refuses, 214 candidate-unknown, 12 project-refuses, 49 project-unknown, 27 value | i1040gi p. 98, line 12 | Copies taxable social security (ssb.line18), not the IRA deduction (stage16.ira.i1: $0.00 against $7,000.00). |
| deepseek | person.ira_se | scope | 2,149/4,647 agree; 307 candidate-refuses, 2129 candidate-unknown, 62 project-refuses | i1040gi p. 97, line 9 | Same line 9 part; placement only. |

Refusal check (kinds_by_return): every project-refuses difference on both logs falls on a return the full interview refuses;
none is on a completed or incomplete return. The skipped-line rule finds no defect: person.ira_line2 and person.ira_line6 are
unprinted helpers, and the printed ira.line2a/2b and 6a/6b are zero whenever lines 2 through 6 are skipped.

Findings: none. No project line contradicts the archived source on a reachable return; project lines unchanged.

## Round 4 (2026-10-27) (superseded subject)

Fresh replies after BUG-0172 to BUG-0176. Full ruling text: `.transcription/proposed/round4/transcription.person.json`, `transcription.person.deepseek.json`, `render.person.deepseek.json`. Claude triage: `../triage/person.json`, executable-triage-v2 (1,111 fixtures, 500 generated returns seed 20261026, 1,616 partial records). The deepseek-flash reply fails validation (person.excess reads the undefined person.h_excess_raw; the f8889.unsupported refusal declarations of the five HSA lines fail the type check), so `../triage/person.deepseek.json` is `invalid` and no deepseek line was executed: lines whose own expression or dependency closure carries an error are model error on that failure (the five HSA lines, excess, credit, and qbi through qbi.deduction); every other line is ruled by reading the expressions against the source, citing the earlier reply's triage where the expression is identical. The render log for Claude has no open line.

Counts — claude transcription: ambiguity 3, interface gap 1, model error 2, representation 9, scope 19; deepseek transcription: ambiguity 1, model error 25, representation 6, scope 14; deepseek render: finding 1, model error 1, scope 1.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | person.educator_deduction | representation | 2,656/4,117 agree; 1,433 candidate-unknown, 28 project-unknown | i1040gi p. 93, line 11 | Same deduction; only the order of the two dispositive questions differs. |
| claude | transcription | person.hsa_agreed | representation | 4,073/4,117 agree; 35 candidate-unknown, 9 value | i8889 p. 7, line 6 Step 2 | Allocation is asked only under the spouse rule; non-split differences are unreachable and unprinted. |
| claude | transcription | person.hsa_step1 | representation | 3,621/4,117 agree; 3 candidate-unknown, 493 value | i8889 p. 7, line 6 Step 2 | Unfiltered sum differs only on non-split forms, read only where both forms are split. |
| claude | transcription | person.hsa_share | interface gap | 3,556/4,117 agree; 32 candidate-refuses, 46 candidate-unknown, 483 value | i8889 p. 7, line 6 Steps 2-3 | f8889.share cycles through its own refusal; interface listed share and share_raw unlabelled. |
| claude | transcription | person.sc_total | scope | 4,116/4,117 agree; 1 project-refuses | i1040sc p. 15, line 32 | Only difference is the cited Form 6198 at-risk refusal. |
| claude | transcription | person.se_line6 | scope | 2,698/4,117 agree; 69 candidate-refuses, 1,349 candidate-unknown, 1 project-refuses | i1040sse p. 1, Who Must File | Same Schedule SE; se_screen/rrta refusal placement only. |
| claude | transcription | person.se_line12 | scope | 2,698/4,117 agree; 69 candidate-refuses, 1,349 candidate-unknown, 1 project-refuses | i1040sse p. 1, Who Must File | Same Schedule SE; refusal placement only. |
| claude | transcription | person.se_line13 | scope | 2,698/4,117 agree; 69 candidate-refuses, 1,349 candidate-unknown, 1 project-refuses | i1040sse p. 1, Who Must File | Same Schedule SE; refusal placement only. |
| claude | transcription | Step 2 | scope | 2,698/4,117 agree; 69 candidate-refuses, 1,349 candidate-unknown, 1 project-refuses | p560 p. 39, Step 2; i1040sse p. 1 | Same Schedule SE line 13; placement only. |
| claude | transcription | person.eic_se | scope | 2,698/4,117 agree; 69 candidate-refuses, 1,349 candidate-unknown, 1 project-refuses | i1040gi EIC Worksheet B; i1040sse p. 1 | Line 31 less line 13 equals Part 1/Part 2 within scope; placement only. |
| claude | transcription | person.s16 | model error | 2,349/4,117 agree; 157 candidate-refuses, 1,517 candidate-unknown, 19 project-refuses, 75 value | p560 p. 16; i1040gi p. 93, line 16 | Deducts SIMPLE deferrals with no compensation (stage16.sd.line17_no_skips_18: $5,686.54 against a refusal). |
| claude | transcription | person.dc_has_box10 | representation | 4,117/4,117 agree | i2441 p. 5, line 12 | Agrees on every compared record. |
| claude | transcription | person.dc_earned | model error | 2,640/4,117 agree; 67 candidate-refuses, 1,320 candidate-unknown, 10 project-refuses, 2 project-unknown, 78 value | i2441 p. 4, earned income item 1 | Omits line 1e (classm.f5695.4: $36,412.00 against $37,824.00). |
| claude | transcription | person.dc_earned_b | scope | 2,716/4,117 agree; 69 candidate-refuses, 1,331 candidate-unknown, 1 project-refuses | i2441 p. 5, line 18 | Same earned income without line 1e; placement only. |
| claude | transcription | person.sav_ineligible | ambiguity | 4,020/4,117 agree; 46 candidate-unknown, 2 project-unknown, 49 value | f8880 p. 2, Who Can Take This Credit | Asking the dependent question only when someone can claim you is the owner decision. |
| claude | transcription | person.sav_line1 | scope | 2,085/4,117 agree; 2,007 candidate-unknown, 1 project-refuses, 24 project-unknown | f8880 line 1; p590a p. 35 | Same amount; project asks the traditional question first and refuses excess contributions. |
| claude | transcription | person.sav_line2 | scope | 2,690/4,117 agree; 89 candidate-refuses, 1,157 candidate-unknown, 69 project-refuses, 112 value | f8880 p. 2, line 2 | Value differences need person.plan without a Schedule C (not asked); refusals are cited screens or placement. |
| claude | transcription | person.ira_contrib | scope | 1,830/4,117 agree; 1 candidate-refuses, 2,264 candidate-unknown, 22 project-unknown | i1040gi p. 98, line 11; p590a p. 35 | Same amount; excess screen placed differently. |
| claude | transcription | person.ira_cov | ambiguity | 3,513/4,117 agree; 44 candidate-unknown, 238 project-unknown, 322 value | i1040gi p. 96, Were You Covered | Self-employed plan read only with a Schedule C is the owner decision. |
| claude | transcription | person.ira_line2 | ambiguity | 3,792/4,117 agree; 18 candidate-unknown, 200 project-unknown, 107 value | i1040gi p. 97, line 2 | Follows ira_cov (amb.2025.ira_covered). |
| claude | transcription | person.ira_line6 | representation | 2,878/4,117 agree; 171 candidate-refuses, 964 candidate-unknown, 24 project-refuses, 72 project-unknown, 8 value | i1040gi p. 97, line 6 | Own formula is the project's; differences inherited (s16, ira_cov, placements). |
| claude | transcription | person.ira_line7 | representation | 3,427/4,117 agree; 360 candidate-refuses, 121 candidate-unknown, 17 project-refuses, 9 project-unknown, 183 value | i1040gi pp. 97-98, line 7 | Reordered tree, same branches; differences inherited from ira_cov and s16. |
| claude | transcription | person.ira_deduction | scope | 1,305/4,117 agree; 322 candidate-refuses, 2,461 candidate-unknown, 11 project-refuses, 18 project-unknown | i1040gi p. 98, line 12 | Same smallest-of; refusal placement and cited Pub. 590-A refusals. |
| claude | transcription | person.ira_nondeductible | scope | 1,305/4,117 agree; 330 candidate-refuses, 2,454 candidate-unknown, 10 project-refuses, 18 project-unknown | i8606 p. 9, line 1 | Same formula; inherited placements. |
| claude | transcription | person.ira_files_8606 | scope | 1,305/4,117 agree; 330 candidate-refuses, 2,454 candidate-unknown, 10 project-refuses, 18 project-unknown | i8606 p. 2, Who Must File | Extra distribution-with-basis condition is screened at retirement.special. |
| claude | transcription | person.ira_8606_line2 | scope | 1,821/4,117 agree; 2,262 candidate-unknown, 12 project-refuses, 22 project-unknown | i8606 p. 9, line 2 | Same basis where Form 8606 is filed; placement only. |
| claude | transcription | person.ira_dist_gate | scope | 1,563/4,117 agree; 330 candidate-refuses, 2,214 candidate-unknown, 10 project-refuses | f8606 Part I question | Same answer wherever asked; placement only. |
| claude | transcription | person.ira_8606_line14 | scope | 1,270/4,117 agree; 330 candidate-refuses, 2,488 candidate-unknown, 11 project-refuses, 18 project-unknown | f8606 Part I, line 14 | Same line 14; inherited placements. |
| claude | transcription | person.ira_ssb | scope | 1,381/4,117 agree; 302 candidate-refuses, 2,406 candidate-unknown, 10 project-refuses, 18 project-unknown | i1040gi p. 98, line 12 | Same no-coverage copy; placement and cited refusals. |
| claude | transcription | person.ira_se | scope | 2,370/4,117 agree; 215 candidate-refuses, 1,516 candidate-unknown, 16 project-refuses | i1040gi p. 98, line 9 | Same line 9 part; cited plan, excess and at-risk refusals. |
| claude | transcription | wages | representation | 4,117/4,117 agree | iw2w3 p. 18; amb.2025.ss_wages | Agrees on every compared record. |
| claude | transcription | eligible | representation | 4,109/4,117 agree; 1 project-unknown, 7 value | i1040gi p. 117, line 11 | Extra over-limit conjunct is where the project refuses the credit. |
| claude | transcription | Step 1 | scope | 2,719/4,117 agree; 2 candidate-refuses, 62 project-refuses, 1,334 project-unknown | p560 p. 39, Step 1 | BUG-0176 refusal fires only where Step 2 already refuses; unknowns are persons without a Schedule C, where Step 1 is not read. |
| claude | transcription | Step 6 | representation | 4,117/4,117 agree | p560 p. 39, Step 6 | Agrees on every compared record. |
| deepseek | transcription | person.educator_deduction | representation | not executable (reply invalid) | i1040gi p. 93, line 11 | Same deduction; question order only. |
| deepseek | transcription | person.hsa_agreed | representation | not executable (reply invalid) | i8889 p. 7, line 6 Step 2 | Allocation asked only under the spouse rule (earlier identical expression: 4,445/4,647 agree). |
| deepseek | transcription | person.hsa_step1 | model error | not executable (reply invalid); validation error | host type check | Refusal declaration reads f8889.unsupported at person level (__type_gate_5). |
| deepseek | transcription | person.hsa_share | model error | not executable (reply invalid); validation error | host type check | Refusal declaration invalid (__type_gate_6). |
| deepseek | transcription | person.hsa_deduction | model error | not executable (reply invalid); validation error | host type check | Refusal declaration invalid (__type_gate_7). |
| deepseek | transcription | person.hsa_taxable | model error | not executable (reply invalid); validation error | host type check | Refusal declaration invalid (__type_gate_8). |
| deepseek | transcription | person.hsa_addtax | model error | not executable (reply invalid); validation error | host type check | Refusal declaration invalid (__type_gate_9). |
| deepseek | transcription | person.tip_employers | scope | not executable (reply invalid) | i1040gi p. 104, line 4c; p. 103 | Excludes only employers the project refuses (tipjob.mixed). |
| deepseek | transcription | person.tip_reported | model error | not executable (reply invalid) | i1040gi p. 104, worksheet columns (b), (c) | Sums column (c) (Form 4137) instead of column (b). |
| deepseek | transcription | person.s179_nonlisted | model error | not executable (reply invalid) | i4562 p. 5, line 6 column (c) | Sums cost, not the elected amount. |
| deepseek | transcription | person.s179_listed | model error | not executable (reply invalid) | i4562 p. 5, line 7 | Sums vehicle cost, not the elected amount. |
| deepseek | transcription | person.income179 | model error | not executable (reply invalid) | i4562 p. 5, line 11 | Uses profits after section 179 and drops losses. |
| deepseek | transcription | person.sc_total | scope | not executable (reply invalid) | i1040sc p. 15, line 32 | Only the cited at-risk refusal. |
| deepseek | transcription | person.se_line6 | scope | not executable (reply invalid) | i1040sse p. 1; f1040sse lines 4a-13 | Same Schedule SE; refusal placement. |
| deepseek | transcription | person.se_line12 | scope | not executable (reply invalid) | i1040sse p. 1; f1040sse lines 4a-13 | Same Schedule SE; refusal placement. |
| deepseek | transcription | person.se_line13 | scope | not executable (reply invalid) | i1040sse p. 1; f1040sse lines 4a-13 | Same Schedule SE; refusal placement. |
| deepseek | transcription | person.s16 | model error | not executable (reply invalid) | p560 p. 39, after Step 21 | Deducts Step 21 instead of the actual SEP contribution. |
| deepseek | transcription | person.qbi | model error | not executable (reply invalid) | i8995 p. 4, line 1; closure | Copies the return QBI deduction (cycle); closure reaches invalid hsa_deduction. |
| deepseek | transcription | person.eic_se | model error | not executable (reply invalid) | i1040gi EIC Worksheet B | Copies the return total built from this line (cycle). |
| deepseek | transcription | person.sc_1a | model error | not executable (reply invalid) | i1040gi p. 104, Schedule 1-A line 5 | Counts statutory-employee businesses, not tips/overtime businesses. |
| deepseek | transcription | person.dc_has_box10 | representation | not executable (reply invalid) | i2441 p. 5, line 12 | Same test (earlier identical expression: 4,647/4,647 agree). |
| deepseek | transcription | person.dc_earned | model error | not executable (reply invalid) | i2441 p. 4, lines 4 and 5 | Copies f2441.line4 built from this line (cycle). |
| deepseek | transcription | person.dc_earned_b | model error | not executable (reply invalid) | i2441 p. 5, line 18 | Copies the return's line 5 (spouse's, with line 1e) for every person. |
| deepseek | transcription | person.sav_ineligible | ambiguity | not executable (reply invalid) | f8880 p. 2, Who Can Take This Credit | amb.2025.savers_ineligible_column. |
| deepseek | transcription | person.sav_line1 | scope | not executable (reply invalid) | f8880 line 1; p590a p. 35 | Same amount; cited excess and ABLE refusals placed differently. |
| deepseek | transcription | person.sav_line2 | model error | not executable (reply invalid) | f8880 p. 2, line 2 | Omits self-employed SIMPLE deferrals. |
| deepseek | transcription | person.ira_contrib | scope | not executable (reply invalid) | i1040gi p. 98, line 11 | Same amount; screen placement. |
| deepseek | transcription | person.ira_cov | model error | not executable (reply invalid) | i1040gi p. 96, Were You Covered | Drops self-employed SEP/SIMPLE coverage. |
| deepseek | transcription | person.ira_line2 | representation | not executable (reply invalid) | i1040gi p. 97, line 2 | $246,000 for a person not covered is reached only on a joint return. |
| deepseek | transcription | person.ira_line6 | model error | not executable (reply invalid) | i1040gi p. 97, line 6 | Copies ira.line6a built from this line (cycle). |
| deepseek | transcription | person.ira_line7 | model error | not executable (reply invalid) | i1040gi pp. 97-98, line 7 | Copies ira.line7a built from this line (cycle). |
| deepseek | transcription | person.ira_deduction | model error | not executable (reply invalid) | i1040gi p. 98, line 12 | Copies ira.total built from this line (cycle). |
| deepseek | transcription | person.ira_nondeductible | scope | not executable (reply invalid) | i8606 p. 9, line 1 | Drops line 10, equal unless contributions exceed compensation (refused). |
| deepseek | transcription | person.ira_files_8606 | scope | not executable (reply invalid) | i8606 p. 2, Who Must File | Extra basis-change disjunct is an answer the project screens. |
| deepseek | transcription | person.ira_8606_line2 | scope | not executable (reply invalid) | i8606 p. 9, line 2 | Same basis where filed; placement. |
| deepseek | transcription | person.ira_dist_gate | scope | not executable (reply invalid) | f8606 Part I question | Same answer wherever asked. |
| deepseek | transcription | person.ira_ssb | model error | not executable (reply invalid) | i1040gi p. 98, line 12 | Copies ssb.ira_line20 built from this line (cycle). |
| deepseek | transcription | person.ira_se | model error | not executable (reply invalid) | i1040gi p. 98, line 9 | Copies Schedule SE line 6; no Schedule 1 lines 15 and 16. |
| deepseek | transcription | over | representation | not executable (reply invalid) | i1040gi p. 117, line 11 | Same sentence's conditions under different helper keys. |
| deepseek | transcription | eligible | representation | not executable (reply invalid) | i1040gi p. 117, line 11 | Over-limit conjunct is where the project refuses. |
| deepseek | transcription | excess | model error | not executable (reply invalid); validation error | host reference check | Reads undefined person.h_excess_raw. |
| deepseek | transcription | credit | model error | not executable (reply invalid); validation error | host reference check | Copies the invalid person.excess. |
| deepseek | transcription | Step 1 | scope | not executable (reply invalid) | p560 p. 39, Step 1 | At-risk and se_screened (BUG-0176) refusals are cited screens. |
| deepseek | transcription | Step 2 | scope | not executable (reply invalid) | p560 p. 39, Step 2 | Same line 13; placement. |
| deepseek | transcription | Step 5 | model error | not executable (reply invalid) | p560 p. 38, Rate Table | Rate rounded to 3 places, not 0.090909. |
| deepseek | transcription | Step 6 | scope | not executable (reply invalid) | p560 p. 39, Step 6 | Same amount; plan_screen placement. |
| deepseek | render | Step 3 | finding | render MISMATCH | p560 p. 39, Step 3 | Project floors Step 3 at zero; page prints no floor (F1, low). |
| deepseek | render | (screen) (person.sav_able) | scope | render MISMATCH | f8880 p. 2, line 4 | Screen refuses more ABLE distributions than line 4 counts; refusal only. |
| deepseek | render | (screen) (person.ira_excess) | model error | render MISMATCH | p590a p. 35; amb.2025.savers_traditional | English lists recharacterization as its own case, not as an excess. |

BUG-0176 check: person.sep_s1's se_screened refusal fires only where Step 2 (person.se_line2) already refuses; its project-unknown and project-refuses records on completed returns are persons without a Schedule C, where Step 1 is not read. No finding.

Findings: one, low severity — F1, person.sep_s3 (Step 3) floors at zero where p560 p. 39 prints no floor; printed worksheet steps only, no Form 1040 amount (`.transcription/proposed/round4/person.findings.md`). Project lines unchanged.

## Stage 19 (superseded subject)

Subject after Stage 19 (the education credits: the `person.edu_*` block, lines 23 to 31 through the `aqee` definition,
the line 7 questions and `person.edu_kid`; D1 to D9 of `research/premises/stage19-education-credits.decisions.md`). Fresh
replies of 2026-10-29. Full ruling text: `.transcription/proposed/stage19/transcription.person.json`,
`transcription.person.deepseek.json`, `render.person.deepseek.json`, `classm.person.deepseek.json`. Claude triage:
`../triage/person.json`, executable-triage-v2 (1,306 fixtures, 500 generated returns seed 20261026, 1,746 partial records;
4,366 comparisons per line). The deepseek-flash reply fails type validation (`person.sep_s5`, `person.sep_s6`: the Count
plan rate used as money; `person.h_se_line4a_pos`: a helper declared NonNegDollars that returns a loss; the five f8889
refusal declarations), so its lines are ruled by reading, and the 23 lines whose closure holds an error are model errors
on the declaration. Lines unchanged since round 4 reuse that round's reasoning, re-checked against the current
expressions, the new triage and the source; every edu line other than `edu_kid` and lines 27 to 31 agreed in both
families.

Counts — claude transcription: ambiguity 3, interface gap 1, model error 7, representation 9, scope 17; deepseek
transcription: ambiguity 1, model error 38, representation 6, scope 4; deepseek render: ambiguity 1; deepseek class M:
model error 1 (dropped).

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | person.educator_deduction | representation | 2,756/4,366 agree; 1,581 candidate-unknown, 29 project-unknown | i1040gi p. 93, Line 11 | Same deduction; only the order of the two dispositive questions differs. |
| claude | transcription | person.hsa_step1 | representation | 4,173/4,366 agree; 3 candidate-unknown, 190 value | i8889 p. 7, Line 6 | Unfiltered sum differs only on non-split forms, read only where both forms are split. |
| claude | transcription | person.hsa_share | interface gap | 4,112/4,366 agree; 30 candidate-refuses, 44 candidate-unknown, 180 value | i8889 p. 7, Line 6 | f8889.share cycles through its own refusal; interface listed share and share_raw unlabelled. |
| claude | transcription | person.s179_listed | representation | 4,366/4,366 agree | i4562 p. 5, Line 7 | s179_elected less f6 is f29 exactly; agrees on every compared record. |
| claude | transcription | person.se_line6 | scope | 2,857/4,366 agree; 25 candidate-refuses, 1,484 candidate-unknown | i1040sse p. 1, Who Must File Schedule SE | Same Schedule SE, now on sc.result; se_screen/rrta refusal placement only. |
| claude | transcription | person.se_line12 | scope | 2,857/4,366 agree; 25 candidate-refuses, 1,484 candidate-unknown | i1040sse p. 1, Who Must File Schedule SE | Same Schedule SE, now on sc.result; se_screen/rrta refusal placement only. |
| claude | transcription | person.se_line13 | scope | 2,857/4,366 agree; 25 candidate-refuses, 1,484 candidate-unknown | p560 p. 39, Deduction Worksheet for Self-Employed | Same Schedule SE, now on sc.result; se_screen/rrta refusal placement only. |
| claude | transcription | Step 2 | scope | 2,857/4,366 agree; 25 candidate-refuses, 1,484 candidate-unknown | p560 p. 39, Deduction Worksheet for Self-Employed | Same Schedule SE, now on sc.result; se_screen/rrta refusal placement only. |
| claude | transcription | person.eic_se | scope | 2,857/4,366 agree; 25 candidate-refuses, 1,484 candidate-unknown | i1040sse p. 1, Who Must File Schedule SE | Line 3 less line 13 equals Part 1/Part 2 within scope; placement only. |
| claude | transcription | person.dc_earned_b | scope | 2,875/4,366 agree; 25 candidate-refuses, 1,466 candidate-unknown | i2441 p. 5, Line 18 | Same earned income without line 1e; placement only. |
| claude | transcription | person.s16 | scope | 2,266/4,366 agree; 432 candidate-refuses, 1,636 candidate-unknown, 16 project-refuses, 2 project-unknown, 14 value | p560 p. 39 | SEP and SIMPLE arithmetic now the project's; differences are plan answers without a Schedule C (never asked) and cited plan refusals. |
| claude | transcription | person.dc_has_box10 | representation | 4,366/4,366 agree | i2441 p. 5, Line 12 | Agrees on every compared record. |
| claude | transcription | person.dc_earned | model error | 2,876/4,366 agree; 23 candidate-refuses, 1,456 candidate-unknown, 9 project-refuses, 2 value | i2441 p. 4 | Now omits Form 1040 line 1e (classm.carloan.1: $234,528.00 against $238,056.00). |
| claude | transcription | person.sav_ineligible | ambiguity | 4,308/4,366 agree; 44 candidate-unknown, 14 value | f8880 p. 2, Who Can Take This Credit | Asking the dependent question only when someone can claim you is the owner decision. |
| claude | transcription | person.sav_line1 | scope | 4,359/4,366 agree; 1 candidate-refuses, 1 project-refuses, 5 project-unknown | p590a p. 35 | Now gated on sav_trad as the project; only the cited excess screen and partials differ. |
| claude | transcription | person.sav_line2 | scope | 2,785/4,366 agree; 16 candidate-refuses, 1,306 candidate-unknown, 53 project-refuses, 1 project-unknown, 205 value | f8880 p. 2, Line 2 | Value differences need person.plan without a Schedule C (not asked); refusals are cited screens or placement. |
| claude | transcription | person.ira_contrib | scope | 2,534/4,366 agree; 1 candidate-refuses, 1,804 candidate-unknown, 27 project-unknown | i1040gi p. 98 | Same amount; drops the sav_trad gate (unknown where not asked), excess screen placed differently. |
| claude | transcription | person.ira_cov | ambiguity | 3,797/4,366 agree; 40 candidate-unknown, 44 project-unknown, 485 value | i1040gi p. 96 | Self-employed plan read only with a Schedule C is the owner decision. |
| claude | transcription | person.ira_line2 | ambiguity | 4,044/4,366 agree; 5 candidate-refuses, 81 candidate-unknown, 6 project-unknown, 230 value | i1040gi p. 97 | Follows ira_cov (amb.2025.ira_covered); MFS refusals are refused returns. |
| claude | transcription | person.ira_line6 | representation | 2,679/4,366 agree; 601 candidate-refuses, 1,043 candidate-unknown, 22 project-refuses, 17 project-unknown, 4 value | i1040gi p. 97 | Own formula is the project's; differences inherited (s16, ira_cov, placements). |
| claude | transcription | person.ira_line7 | representation | 3,935/4,366 agree; 1 candidate-refuses, 66 candidate-unknown, 313 project-refuses, 47 project-unknown, 4 value | i1040gi pp. 97-98 | Same branches where the worksheet is completed; no-contribution differences reach no amount. |
| claude | transcription | person.ira_deduction | scope | 1,429/4,366 agree; 968 candidate-refuses, 1,941 candidate-unknown, 11 project-refuses, 17 project-unknown | i1040gi p. 98 | Same smallest-of; inherited placements and cited Pub. 590-A refusals. |
| claude | transcription | person.ira_nondeductible | scope | 1,429/4,366 agree; 968 candidate-refuses, 1,942 candidate-unknown, 10 project-refuses, 17 project-unknown | i8606 p. 9, Line 1 | Same formula; inherited placements. |
| claude | transcription | person.ira_files_8606 | scope | 1,429/4,366 agree; 968 candidate-refuses, 1,942 candidate-unknown, 10 project-refuses, 17 project-unknown | i8606 p. 2, Who Must File | Extra distribution-with-basis condition is screened at retirement.special. |
| claude | transcription | person.ira_8606_line2 | scope | 2,523/4,366 agree; 1,803 candidate-unknown, 12 project-refuses, 28 project-unknown | i8606 p. 9, Line 2 | Same basis where Form 8606 is filed; placement only. |
| claude | transcription | person.ira_dist_gate | scope | 2,593/4,366 agree; 45 candidate-refuses, 1,716 candidate-unknown, 12 project-refuses | host type check | Same answer wherever asked; placement only. |
| claude | transcription | person.ira_8606_line14 | representation | 1,396/4,366 agree; 968 candidate-refuses, 1,974 candidate-unknown, 11 project-refuses, 17 project-unknown | host type check | Same line 14 (line 3); inherited placements. |
| claude | transcription | person.ira_ssb | scope | 1,429/4,366 agree; 968 candidate-refuses, 1,942 candidate-unknown, 10 project-refuses, 17 project-unknown | i1040gi p. 98 | Same no-coverage copy where read; covered-with-contribution case is refused. |
| claude | transcription | person.ira_se | scope | 2,265/4,366 agree; 450 candidate-refuses, 1,636 candidate-unknown, 15 project-refuses | i1040gi p. 97 | Same line 9 part; cited plan refusals. |
| claude | transcription | person.edu_kid | model error | 2,421/4,366 agree; 1,839 candidate-unknown, 36 project-refuses, 70 value | i8863 p. 7, Line 7 | Treats an 18-year-old as under 18 (support test dropped; sav_born was published); omits the line 7 gate. |
| claude | transcription | eligible | representation | 4,358/4,366 agree; 1 project-unknown, 7 value | i1040gi p. 117, Line 11 | Extra over-limit conjunct is where the project refuses the credit. |
| claude | transcription | Step 6 | representation | 4,366/4,366 agree | p560 p. 39, Step 6 | Agrees on every compared record. |
| claude | transcription | 27 | model error | 1,538/4,366 agree; 2,828 candidate-unknown | i8863 p. 3, Who cannot claim a credit | Omits the student and filer TIN tests and f8863.paid; arithmetic is the aqee definition. |
| claude | transcription | 28 | model error | 1,538/4,366 agree; 2,828 candidate-unknown | i8863 p. 3, Who cannot claim a credit | Omits the student and filer TIN tests and f8863.paid; arithmetic is the aqee definition. |
| claude | transcription | 29 | model error | 1,538/4,366 agree; 2,828 candidate-unknown | i8863 p. 3, Who cannot claim a credit | Omits the student and filer TIN tests and f8863.paid; arithmetic is the aqee definition. |
| claude | transcription | 30 | model error | 1,538/4,366 agree; 2,828 candidate-unknown | i8863 p. 3, Who cannot claim a credit | Omits the student and filer TIN tests and f8863.paid; arithmetic is the aqee definition. |
| claude | transcription | 31 | model error | 1,537/4,366 agree; 1 candidate-shows-skipped, 2,828 candidate-unknown | i8863 p. 3, Who cannot claim a credit | Omits the student TIN test (generated 47 shows $11,187.11 for a student with no TIN) and f8863.paid. |
| deepseek | transcription | person.educator_deduction | representation | not executable (reply invalid) | i1040gi p. 93, Line 11 | Same deduction as the Claude reply; question order only. |
| deepseek | transcription | person.hsa_agreed | representation | not executable (reply invalid) | i8889 p. 7, Line 6 | Allocation asked only under the spouse rule; no printed amount differs. |
| deepseek | transcription | person.hsa_step1 | model error | not executable (reply invalid) | host type check | Refusal declaration reads f8889.unsupported at person level (__type_gate_14). |
| deepseek | transcription | person.hsa_share | model error | not executable (reply invalid) | host type check | Refusal declaration reads f8889.unsupported at person level (__type_gate_15). |
| deepseek | transcription | person.hsa_deduction | model error | not executable (reply invalid) | host type check | Refusal declaration reads f8889.unsupported at person level (__type_gate_16). |
| deepseek | transcription | person.hsa_taxable | model error | not executable (reply invalid) | host type check | Refusal declaration reads f8889.unsupported at person level (__type_gate_17). |
| deepseek | transcription | person.hsa_addtax | model error | not executable (reply invalid) | host type check | Refusal declaration reads f8889.unsupported at person level (__type_gate_18). |
| deepseek | transcription | person.s179_nonlisted | model error | not executable (reply invalid) | i4562 p. 5, Line 6 | Sums cost, not the elected amount. |
| deepseek | transcription | person.s179_listed | model error | not executable (reply invalid) | i4562 p. 5, Line 7 | Sums vehicle cost, not the elected amount. |
| deepseek | transcription | person.income179 | model error | not executable (reply invalid) | i4562 p. 5, Line 11 | Uses profits after section 179, floored per business (drops losses); circular. |
| deepseek | transcription | person.se_line6 | model error | not executable (reply invalid) | i1040sse p. 1, Who Must File Schedule SE | Declaration invalid (h_se_line4a_pos not provably non-negative); tax reading not ruled. |
| deepseek | transcription | person.se_line12 | model error | not executable (reply invalid) | i1040sse p. 1, Who Must File Schedule SE | Declaration invalid (h_se_line4a_pos not provably non-negative); tax reading not ruled. |
| deepseek | transcription | person.se_line13 | model error | not executable (reply invalid) | i1040sse p. 1, Who Must File Schedule SE | Declaration invalid (h_se_line4a_pos not provably non-negative); tax reading not ruled. |
| deepseek | transcription | Step 2 | model error | not executable (reply invalid) | p560 p. 39, Step 2 | Declaration invalid (h_se_line4a_pos not provably non-negative); tax reading not ruled. |
| deepseek | transcription | Step 3 | model error | not executable (reply invalid) | host type check | Declaration invalid (h_se_line4a_pos not provably non-negative); tax reading not ruled. |
| deepseek | transcription | person.s16 | model error | not executable (reply invalid) | i1040gi p. 93, Line 16 | Declaration invalid (sep_s5/sep_s6 use the Count rate as money); also deducts capped SEP and lacks the Schedule C gate. |
| deepseek | transcription | person.eic_se | model error | not executable (reply invalid) | host type check | Declaration invalid (h_se_line4a_pos not provably non-negative); tax reading not ruled. |
| deepseek | transcription | person.dc_earned | model error | not executable (reply invalid) | host type check | Declaration invalid (h_se_line4a_pos not provably non-negative); tax reading not ruled. |
| deepseek | transcription | person.dc_earned_b | model error | not executable (reply invalid) | i2441 p. 5, Line 18 | Declaration invalid (h_se_line4a_pos not provably non-negative); tax reading not ruled. |
| deepseek | transcription | person.ira_se | model error | not executable (reply invalid) | i1040gi p. 97 | Declaration invalid (h_se_line4a_pos not provably non-negative); tax reading not ruled. |
| deepseek | transcription | person.ira_deduction | model error | not executable (reply invalid) | host type check | Declaration invalid (h_se_line4a_pos not provably non-negative); tax reading not ruled. |
| deepseek | transcription | person.ira_nondeductible | model error | not executable (reply invalid) | host type check | Declaration invalid (h_se_line4a_pos not provably non-negative); tax reading not ruled. |
| deepseek | transcription | person.ira_files_8606 | model error | not executable (reply invalid) | host type check | Declaration invalid (h_se_line4a_pos not provably non-negative); tax reading not ruled. |
| deepseek | transcription | person.ira_8606_line14 | model error | not executable (reply invalid) | host type check | Declaration invalid (h_se_line4a_pos not provably non-negative); tax reading not ruled. |
| deepseek | transcription | Step 5 | model error | not executable (reply invalid) | p560 p. 38, Rate Table for Self-Employed | Declaration invalid (sep_rate Count used as money in prorate); tax reading not ruled. |
| deepseek | transcription | Step 6 | model error | not executable (reply invalid) | p560 p. 39, Step 6 | Declaration invalid (sep_rate Count used as money in prorate); tax reading not ruled. |
| deepseek | transcription | Step 7 | model error | not executable (reply invalid) | host type check | Declaration invalid (sep_rate Count used as money in prorate); tax reading not ruled. |
| deepseek | transcription | Step 21 | model error | not executable (reply invalid) | host type check | Declaration invalid (sep_rate Count used as money in prorate); tax reading not ruled. |
| deepseek | transcription | person.sc_1a | model error | not executable (reply invalid) | i1040gi p. 104, Schedule 1-A Line 5 | Counts statutory-employee businesses, not tips/overtime businesses. |
| deepseek | transcription | person.dc_has_box10 | representation | not executable (reply invalid) | i2441 p. 5, Line 12 | Same test. |
| deepseek | transcription | person.sav_ineligible | ambiguity | not executable (reply invalid) | f8880 p. 2, Who Can Take This Credit | amb.2025.savers_ineligible_column; the added AGI test reaches no amount. |
| deepseek | transcription | person.sav_line1 | scope | not executable (reply invalid) | host type check | Same amount; cited excess screen placed differently. |
| deepseek | transcription | person.sav_line2 | model error | not executable (reply invalid) | f8880 p. 2, Line 2 | Omits self-employed SIMPLE deferrals. |
| deepseek | transcription | person.ira_contrib | scope | not executable (reply invalid) | i1040gi p. 98 | Same amount; screen placement. |
| deepseek | transcription | person.ira_cov | model error | not executable (reply invalid) | i1040gi p. 96 | Drops self-employed SEP/SIMPLE coverage. |
| deepseek | transcription | person.ira_line2 | representation | not executable (reply invalid) | i1040gi p. 97 | $246,000 for a person not covered is reached only on a joint return. |
| deepseek | transcription | person.ira_line6 | model error | not executable (reply invalid) | i1040gi p. 97 | Subtracts Form 1040 line 11a (AGI after the deduction) instead of worksheet line 5. |
| deepseek | transcription | person.ira_line7 | model error | not executable (reply invalid) | i1040gi pp. 97-98 | Tiers right, built on the wrong line 6. |
| deepseek | transcription | person.ira_8606_line2 | scope | not executable (reply invalid) | i8606 p. 9, Line 2 | Same basis where filed; placement. |
| deepseek | transcription | person.ira_dist_gate | scope | not executable (reply invalid) | host type check | Same answer wherever asked. |
| deepseek | transcription | person.ira_ssb | model error | not executable (reply invalid) | i1040gi p. 98 | Copies Form 1040 line 6b (taxable benefits), not the IRA deduction. |
| deepseek | transcription | person.edu_kid | model error | not executable (reply invalid) | i8863 p. 7, Line 7 | 18-year-old treated as under 18; QSS treated as joint; line 7 gate omitted. |
| deepseek | transcription | wages | representation | not executable (reply invalid) | iw2w3 p. 18 | Same boxes 3 and 7. |
| deepseek | transcription | eligible | representation | not executable (reply invalid) | i1040gi p. 117, Line 11 | Over-limit and railroad conjuncts are where the project refuses the credit. |
| deepseek | transcription | 27 | model error | not executable (reply invalid) | i8863 p. 3, Who cannot claim a credit | Omits TIN tests and f8863.paid; edu_over zeroes the AOC instead of refusing. |
| deepseek | transcription | 28 | model error | not executable (reply invalid) | i8863 p. 3, Who cannot claim a credit | Omits TIN tests and f8863.paid; edu_over zeroes the AOC instead of refusing. |
| deepseek | transcription | 29 | model error | not executable (reply invalid) | i8863 p. 3, Who cannot claim a credit | Omits TIN tests and f8863.paid; edu_over zeroes the AOC instead of refusing. |
| deepseek | transcription | 30 | model error | not executable (reply invalid) | i8863 p. 3, Who cannot claim a credit | Omits TIN tests and f8863.paid; edu_over zeroes the AOC instead of refusing. |
| deepseek | transcription | 31 | model error | not executable (reply invalid) | i8863 p. 3, Who cannot claim a credit | Omits the student TIN test; routes an edu_over student to line 31 on the netted total. |
| deepseek | render | Step 3 | ambiguity | render MISMATCH | p560 p. 39, Deduction Worksheet for Self-Employed | Floor is the registered reading (BUG-0181); the model read page and English correctly. |
| deepseek | class M | classm.person.1 — person[taxpayer].wages | model error (drop) | class M DISAGREE | iw2w3 p. 18 | Model summed box 1, not boxes 3 and 7 ($29,524.00 against $44,754.00). |

Findings: one, low severity, from scrutiny of the Stage 19 block rather than from a reply — Q1, `person.edu_over`: the D3
screen's question does not say which expenses a period's assistance is compared with, so a lifetime learning student whose
outside course materials cover the gap answers No and line 31 is netted over the year instead of flooring the period at zero
(`.transcription/proposed/stage19/person.findings.md`; the same on `dependent.edu_over`). The routing (`edu_student`,
`edu_aoc`, `edu_llc`), both TIN tests, the Form 1098-T question, the line 7 conditions and the display chain agree with
i8863 and f8863 (checked, not findings, in the same file). Traceability note: `person.sep_s3` carries no `ambiguity:` field
for amb.2025.sep_loss_floor.

## Stage 19 round 2 (superseded subject)

Subject after the round-1 fixes (BUG-0195 to BUG-0199; for this entry BUG-0197, the reworded `person.edu_over`). Fresh
replies of 2026-10-29. Full ruling text: `.transcription/proposed/stage19/round2/transcription.person.json`,
`transcription.person.deepseek.json`, `render.person.deepseek.json`. Claude triage: `../triage/person.json`,
executable-triage-v2 (1,325 fixtures, 500 generated returns seed 20261026, 1,792 partial records; 4,395 comparisons per
line). The deepseek-flash reply fails validation again (`person.hundred` retyped; `person.sep_s5_raw`, `person.sep_s6`:
the Count plan rate used as money; the five f8889 refusal declarations), so its lines are ruled by reading. Both replies
were re-read against round 1: the Claude reply moved its Schedule SE chain back to `sc.line31`, dropped the `sav_trad`
and plan gates on Form 8880 lines 1 and 2, fixed `edu_kid`'s age conditions and newly disagrees on `tip_reported`,
`sc_total`, `hsa_agreed` and SEP Step 1; the deepseek reply dropped the Schedule SE $400 test and now defines several IRA
lines by the return-level lines that sum them.

Counts — claude transcription: ambiguity 4, interface gap 1, model error 8, representation 8, scope 19; deepseek transcription: ambiguity 1, model error 37, representation 5, scope 6; deepseek render: ambiguity 1.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | person.educator_deduction | representation | 2,684/4,395 agree; 1,684 candidate-unknown, 27 project-unknown | i1040gi p. 93, Line 11 | Same expression; only question order differs. |
| claude | transcription | person.hsa_agreed | representation | 4,353/4,395 agree; 35 candidate-unknown, 7 value | i8889 p. 7, Line 6 Step 2 | Allocation asked only under the spouse rule; values supply it outside the rule. |
| claude | transcription | person.hsa_step1 | representation | 4,196/4,395 agree; 3 candidate-unknown, 196 value | i8889 p. 7, Line 6 Step 2 | Unfiltered sum equals the filtered one wherever it is read. |
| claude | transcription | person.hsa_share | interface gap | 4,135/4,395 agree; 30 candidate-refuses, 44 candidate-unknown, 186 value | i8889 p. 7, Line 6 Steps 2-3 | share vs share_raw not distinguishable from the interface. |
| claude | transcription | person.tip_reported | model error | 3,935/4,395 agree; 6 candidate-refuses, 9 project-refuses, 445 value | i1040gi p. 104, worksheet columns (b), (c) | Sums column (c) against the published label "column (b) total". |
| claude | transcription | person.sc_total | scope | 4,394/4,395 agree; 1 project-refuses | i1040sc p. 15, Line 32 | Only the cited at-risk refusal. |
| claude | transcription | person.se_line6 | scope | 2,727/4,395 agree; 96 candidate-refuses, 1,571 candidate-unknown, 1 project-refuses | i1040sse p. 1, Who Must File | Back on sc.line31; se_screen/rrta refusal placement only. |
| claude | transcription | person.se_line12 | scope | 2,727/4,395 agree; 96 candidate-refuses, 1,571 candidate-unknown, 1 project-refuses | i1040sse p. 1, Who Must File | Back on sc.line31; se_screen/rrta refusal placement only. |
| claude | transcription | person.se_line13 | scope | 2,727/4,395 agree; 96 candidate-refuses, 1,571 candidate-unknown, 1 project-refuses | p560 p. 39, Step 2 | Half of line 12; placement only. |
| claude | transcription | Step 2 | scope | 2,727/4,395 agree; 96 candidate-refuses, 1,571 candidate-unknown, 1 project-refuses | p560 p. 39, Step 2 | Copies line 13; placement only. |
| claude | transcription | Step 1 | scope | 2,737/4,395 agree; 1 candidate-refuses, 94 project-refuses, 1,563 project-unknown | p560 p. 39, Step 1 | Project refuses at se_screened; unknown gate where the worksheet is not reached. |
| claude | transcription | person.s16 | scope | 2,489/4,395 agree; 22 candidate-refuses, 1,752 candidate-unknown, 132 project-refuses | p560 p. 39, after Step 21 | SEP capped at Step 21 and SIMPLE capped formulas; differences are cited refusals. |
| claude | transcription | person.eic_se | scope | 2,727/4,395 agree; 96 candidate-refuses, 1,571 candidate-unknown, 1 project-refuses | i1040gi EIC Worksheet B | Same amount wherever both evaluate; placement only. |
| claude | transcription | person.dc_has_box10 | representation | 4,395/4,395 agree; no difference | i2441 p. 5, Line 12 | Count of W-2s with box 10 equals the box 10 test. |
| claude | transcription | person.dc_earned | model error | 2,748/4,395 agree; 94 candidate-refuses, 1,541 candidate-unknown, 10 project-refuses, 2 value | i2441 p. 4, earned income item 1 | Still omits Form 1040 line 1e (classm.carloan.1). |
| claude | transcription | person.dc_earned_b | scope | 2,745/4,395 agree; 96 candidate-refuses, 1,553 candidate-unknown, 1 project-refuses | i2441 p. 5, Line 18 | Same amount; placement only. |
| claude | transcription | person.sav_ineligible | ambiguity | 4,338/4,395 agree; 43 candidate-unknown, 14 value | f8880 p. 2, Who Can Take This Credit | amb.2025.savers_ineligible_column. |
| claude | transcription | person.sav_line1 | scope | 2,776/4,395 agree; 1,586 candidate-unknown, 1 project-refuses, 32 project-unknown | f8880 line 1 | Drops the sav_trad gate; unknown only where not asked. |
| claude | transcription | person.sav_line2 | scope | 2,495/4,395 agree; 16 candidate-refuses, 1,541 candidate-unknown, 53 project-refuses, 11 project-unknown, 279 value | f8880 p. 2, Line 2 | simple_deferral added without the plan gate; values on records the interview cannot produce. |
| claude | transcription | person.ira_contrib | scope | 2,573/4,395 agree; 1,794 candidate-unknown, 28 project-unknown | i1040gi p. 98, line 11 | No sav_trad gate; unknown only where not asked. |
| claude | transcription | person.ira_cov | ambiguity | 3,778/4,395 agree; 43 candidate-unknown, 13 project-unknown, 561 value | i1040gi p. 96 | amb.2025.ira_covered. |
| claude | transcription | person.ira_line2 | ambiguity | 1,795/4,395 agree; 1,290 candidate-unknown, 6 project-unknown, 1,304 value | i1040gi p. 97, line 2 | $246,000 for any uncovered person reaches nothing when lines 2-6 are skipped; joint differences are amb.2025.ira_covered. |
| claude | transcription | person.ira_line6 | representation | 2,220/4,395 agree; 14 candidate-refuses, 1,161 candidate-unknown, 136 project-refuses, 26 project-unknown, 838 value | i1040gi p. 97, line 6 | Inherited differences on skipped lines and ruled lines. |
| claude | transcription | person.ira_line7 | ambiguity | 3,789/4,395 agree; 56 candidate-refuses, 178 candidate-unknown, 129 project-refuses, 13 project-unknown, 230 value | i1040gi pp. 97-98, line 7 | Values are plan supplied without a Schedule C (amb.2025.ira_covered), no contribution. |
| claude | transcription | person.ira_deduction | scope | 2,064/4,395 agree; 158 candidate-refuses, 2,135 candidate-unknown, 11 project-refuses, 27 project-unknown | i1040gi p. 98, line 12 | Same smallest-of; placement only. |
| claude | transcription | person.ira_nondeductible | scope | 2,063/4,395 agree; 195 candidate-refuses, 2,100 candidate-unknown, 10 project-refuses, 27 project-unknown | i8606 p. 9, Line 1 | Same formula; placement only. |
| claude | transcription | person.ira_files_8606 | scope | 2,063/4,395 agree; 195 candidate-refuses, 2,100 candidate-unknown, 10 project-refuses, 27 project-unknown | i8606 p. 2, Who Must File | Extra basis condition is screened; placement only. |
| claude | transcription | person.ira_8606_line2 | scope | 2,533/4,395 agree; 1,821 candidate-unknown, 12 project-refuses, 29 project-unknown | i8606 p. 9, Line 2 | Basis asked only of a Form 8606 filer. |
| claude | transcription | person.ira_dist_gate | scope | 2,615/4,395 agree; 38 candidate-refuses, 1,730 candidate-unknown, 12 project-refuses | f8606 Part I | Same gate; placement only. |
| claude | transcription | person.ira_8606_line14 | representation | 2,010/4,395 agree; 195 candidate-refuses, 2,152 candidate-unknown, 11 project-refuses, 27 project-unknown | Form 8606 Part I, line 14 | Same two amounts. |
| claude | transcription | person.ira_ssb | scope | 2,180/4,395 agree; 152 candidate-refuses, 2,025 candidate-unknown, 11 project-refuses, 27 project-unknown | i1040gi p. 98, line 12 | Smallest of contribution, limit and line 10; no value differs. |
| claude | transcription | person.ira_se | scope | 2,412/4,395 agree; 111 candidate-refuses, 1,737 candidate-unknown, 135 project-refuses | i1040gi p. 97, line 9 | Same subtraction; cited plan refusals. |
| claude | transcription | person.edu_kid | model error | 2,502/4,395 agree; 1,770 candidate-unknown, 35 project-refuses, 17 project-unknown, 71 value | i8863 pp. 6-7, Line 7 | Age (a)/(b) fixed; still no kid_needed gate. |
| claude | transcription | eligible | representation | 4,387/4,395 agree; 1 project-unknown, 7 value | i1040gi p. 117, Line 11 | Over-limit test belongs to person.credit's refusal. |
| claude | transcription | Step 6 | representation | 4,395/4,395 agree; no difference | p560 p. 39, Step 6 | No difference. |
| claude | transcription | 27 | model error | 1,694/4,395 agree; 2,700 candidate-unknown, 1 project-unknown | i8863 p. 3, Who cannot claim a credit, item 5 | No student-TIN, filer-TIN or f8863.paid test. |
| claude | transcription | 28 | model error | 1,694/4,395 agree; 2,700 candidate-unknown, 1 project-unknown | i8863 p. 3, Who cannot claim a credit, item 5 | No student-TIN, filer-TIN or f8863.paid test. |
| claude | transcription | 29 | model error | 1,694/4,395 agree; 2,700 candidate-unknown, 1 project-unknown | i8863 p. 3, Who cannot claim a credit, item 5 | No student-TIN, filer-TIN or f8863.paid test. |
| claude | transcription | 30 | model error | 1,694/4,395 agree; 2,700 candidate-unknown, 1 project-unknown | i8863 p. 3, Who cannot claim a credit, item 5 | No student-TIN, filer-TIN or f8863.paid test. |
| claude | transcription | 31 | model error | 1,692/4,395 agree; 1 candidate-refuses, 1 candidate-shows-skipped, 2,700 candidate-unknown, 1 project-unknown | i8863 p. 3, Who cannot claim a credit, item 5 | Shows $11,187.11 for a student without a TIN (generated 47). |
| deepseek | transcription | person.educator_deduction | representation | not executable (reply invalid) | i1040gi p. 93, Line 11 | Same as the Claude expression. |
| deepseek | transcription | person.hsa_agreed | representation | not executable (reply invalid) | i8889 p. 7, Line 6 Step 2 | Allocation asked only under the spouse rule. |
| deepseek | transcription | person.hsa_step1 | model error | not executable (reply invalid) | i8889 p. 7, Line 6 | Declaration error (refusal reads a per-form field). |
| deepseek | transcription | person.hsa_share | model error | not executable (reply invalid) | i8889 p. 7, Line 6 | Declaration error (refusal reads a per-form field). |
| deepseek | transcription | person.hsa_deduction | model error | not executable (reply invalid) | i8889 p. 7 | Declaration error (refusal reads a per-form field). |
| deepseek | transcription | person.hsa_taxable | model error | not executable (reply invalid) | i8889 | Declaration error (refusal reads a per-form field). |
| deepseek | transcription | person.hsa_addtax | model error | not executable (reply invalid) | i8889 | Declaration error (refusal reads a per-form field). |
| deepseek | transcription | person.s179_nonlisted | model error | not executable (reply invalid) | i4562 p. 5, Line 6 | Cost for elected cost. |
| deepseek | transcription | person.s179_listed | model error | not executable (reply invalid) | i4562 p. 5, Line 7 | Vehicle cost for elected amount. |
| deepseek | transcription | person.income179 | model error | not executable (reply invalid) | i4562 p. 5, Line 11 | After-179 profit floored; circular. |
| deepseek | transcription | person.sc_total | scope | not executable (reply invalid) | i1040sc p. 15, Line 32 | Only the at-risk refusal. |
| deepseek | transcription | Step 1 | scope | not executable (reply invalid) | p560 p. 39, Step 1 | At-risk and se_screened refusals only. |
| deepseek | transcription | person.se_line6 | model error | not executable (reply invalid) | f1040sse line 4c | No $400 stop. |
| deepseek | transcription | person.se_line12 | model error | not executable (reply invalid) | f1040sse line 4c | No $400 stop. |
| deepseek | transcription | person.se_line13 | model error | not executable (reply invalid) | f1040sse line 4c | Inherits the missing $400 stop. |
| deepseek | transcription | Step 2 | model error | not executable (reply invalid) | p560 p. 39, Step 2 | Inherits the missing $400 stop. |
| deepseek | transcription | person.s16 | model error | not executable (reply invalid) | p560 p. 39, after Step 21 | Deducts Step 21, not the contribution; SEP declaration errors. |
| deepseek | transcription | Step 5 | model error | not executable (reply invalid) | p560 p. 38-39 | SEP declaration errors. |
| deepseek | transcription | Step 6 | model error | not executable (reply invalid) | p560 p. 39, Step 6 | SEP declaration errors. |
| deepseek | transcription | Step 7 | model error | not executable (reply invalid) | p560 p. 39, Step 7 | SEP declaration errors. |
| deepseek | transcription | Step 21 | model error | not executable (reply invalid) | p560 p. 39, Step 21 | SEP declaration errors. |
| deepseek | transcription | person.eic_se | model error | not executable (reply invalid) | i1040gi EIC Worksheet B; f1040sse line 4c | Subtracts SE tax below $400. |
| deepseek | transcription | person.sc_1a | model error | not executable (reply invalid) | i1040gi p. 104, Line 5 | Counts Schedules C with receipts, not with tips or overtime. |
| deepseek | transcription | person.dc_has_box10 | representation | not executable (reply invalid) | i2441 p. 5, Line 12 | Same test. |
| deepseek | transcription | person.dc_earned | model error | not executable (reply invalid) | i2441 p. 4 | Omits line 1e; no $400 stop. |
| deepseek | transcription | person.dc_earned_b | model error | not executable (reply invalid) | i2441 p. 5, Line 18 | Reads the spouse's earned income for every entry. |
| deepseek | transcription | person.sav_ineligible | ambiguity | not executable (reply invalid) | f8880 p. 2 | amb.2025.savers_ineligible_column. |
| deepseek | transcription | person.sav_line1 | scope | not executable (reply invalid) | f8880 line 1 | No sav_trad gate. |
| deepseek | transcription | person.sav_line2 | model error | not executable (reply invalid) | f8880 p. 2, Line 2 | Omits own SIMPLE deferral. |
| deepseek | transcription | person.ira_contrib | scope | not executable (reply invalid) | i1040gi p. 98, line 11 | No sav_trad gate. |
| deepseek | transcription | person.ira_cov | model error | not executable (reply invalid) | i1040gi p. 96 | Drops own SEP or SIMPLE. |
| deepseek | transcription | person.ira_line2 | representation | not executable (reply invalid) | i1040gi p. 97, line 2 | Reaches nothing when lines 2-6 are skipped. |
| deepseek | transcription | person.ira_line6 | model error | not executable (reply invalid) | i1040gi p. 97, line 6 | Defined by the return-level line that sums it (cycle). |
| deepseek | transcription | person.ira_line7 | model error | not executable (reply invalid) | i1040gi pp. 97-98, line 7 | Defined by the return-level line that sums it (cycle). |
| deepseek | transcription | person.ira_deduction | model error | not executable (reply invalid) | i1040gi p. 98, line 12 | Defined by the return-level line that sums it (cycle). |
| deepseek | transcription | person.ira_nondeductible | model error | not executable (reply invalid) | i8606 p. 9, Line 1 | Built on the circular line 12. |
| deepseek | transcription | person.ira_files_8606 | model error | not executable (reply invalid) | i8606 p. 2 | Built on the circular line 12. |
| deepseek | transcription | person.ira_8606_line14 | model error | not executable (reply invalid) | Form 8606 Part I | Built on the circular line 12. |
| deepseek | transcription | person.ira_8606_line2 | scope | not executable (reply invalid) | i8606 p. 9, Line 2 | Basis asked only of a Form 8606 filer. |
| deepseek | transcription | person.ira_dist_gate | scope | not executable (reply invalid) | f8606 Part I | Asked only of a Form 8606 filer. |
| deepseek | transcription | person.ira_ssb | model error | not executable (reply invalid) | i1040gi p. 98, line 12 | Sums itself over persons (cycle). |
| deepseek | transcription | person.ira_se | model error | not executable (reply invalid) | i1040gi p. 97, line 9 | Copies the IRA deduction for SE earned income. |
| deepseek | transcription | person.edu_kid | model error | not executable (reply invalid) | i8863 p. 7, Line 7 | Copies person.edu. |
| deepseek | transcription | eligible | representation | not executable (reply invalid) | i1040gi p. 117, Line 11 | Over-limit test belongs to person.credit's refusal. |
| deepseek | transcription | 27 | model error | not executable (reply invalid) | i8863 p. 3, item 5; p. 2 | No TIN, 1098-T, expense or f8863.paid tests. |
| deepseek | transcription | 28 | model error | not executable (reply invalid) | i8863 p. 3, item 5; p. 2 | No TIN, 1098-T, expense or f8863.paid tests. |
| deepseek | transcription | 29 | model error | not executable (reply invalid) | i8863 p. 3, item 5; p. 2 | No TIN, 1098-T, expense or f8863.paid tests. |
| deepseek | transcription | 30 | model error | not executable (reply invalid) | i8863 p. 3, item 5; p. 2 | No TIN, 1098-T, expense or f8863.paid tests. |
| deepseek | transcription | 31 | model error | not executable (reply invalid) | i8863 p. 3, item 5; p. 2 | No TIN, 1098-T, expense or f8863.paid tests. |
| deepseek | render | Step 3 | ambiguity | render MISMATCH | p560 p. 39, Step 3 | amb.2025.sep_loss_floor; the English states the chosen floor. |

Findings: none new on the person entry (`.transcription/proposed/stage19/round2/person.findings.md`). The BUG-0197 fix
was checked against i8863 pp. 4 and 9: comparing with the institution-paid base can only over-refuse, never compute a
wrong amount, and the round-1 witness is now refused; the label of `person.edu_over` still says "its own expenses"
(stale wording, no amount).

## Stage 19 round 3 (superseded subject)

Subject after the round-2 fixes; for this entry only the label of `person.edu_over` changed ("exceed its expenses paid to
the institution"). Fresh replies of 2026-10-29. Full ruling text: `.transcription/proposed/stage19/round3/transcription.person.json`,
`transcription.person.deepseek.json`, `render.person.deepseek.json`, `classm.person.deepseek.json`. Claude triage:
`../triage/person.json`, executable-triage-v2 (1,323 fixtures, 500 generated returns seed 20261026, 1,839 partial records;
4,425 comparisons per line). The deepseek-flash reply fails validation on one line only (`person.h_se_line4a_mult`,
NonNegDollars not proved), so its lines are ruled by reading; lines reaching that helper are model errors on the
declaration. Both replies were re-read against round 2: the Claude reply gated Form 8880 line 1 on `sav_trad`, dropped the
SIMPLE deferral from line 2, moved the whole section 179 election to Form 4562 line 6 (the reviewer's i4562 pages, 4 and 11,
omit the p. 5 line 6 and 7 text), recast EIC Worksheet B and IRA line 2 and 7, and now tests the student's TIN (without
`itin_applied`); the deepseek reply restored the Schedule SE $400 test, fixed its SEP type errors and HSA refusals, but
newly makes Form 4562 line 6, the section 179 income limit and Form 8606 line 2 circular.

Counts — claude transcription: ambiguity 4, interface gap 3, model error 8, representation 8, scope 18; deepseek transcription: ambiguity 1, interface gap 2, model error 32, representation 10, scope 4; deepseek render: ambiguity 1; deepseek class M: model error 1 (dropped).

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | person.educator_deduction | representation | 2,987/4,425 agree; 1,406 candidate-unknown, 32 project-unknown | i1040gi p. 93, Line 11 | Same formula; only question order differs. |
| claude | transcription | person.hsa_agreed | representation | 4,383/4,425 agree; 35 candidate-unknown, 7 value | i8889 p. 7, Line 6 Step 2 | Allocation asked only under the spouse rule. |
| claude | transcription | person.hsa_step1 | representation | 4,059/4,425 agree; 3 candidate-unknown, 363 value | i8889 p. 7, Line 6 Step 2 | Unfiltered sum equals the filtered one wherever read. |
| claude | transcription | person.hsa_share | interface gap | 3,998/4,425 agree; 30 candidate-refuses, 44 candidate-unknown, 353 value | i8889 p. 7, Line 6 Steps 2-3 | share vs share_raw not distinguishable from the interface. |
| claude | transcription | person.s179_nonlisted | interface gap | 4,341/4,425 agree; 15 candidate-refuses, 69 value | i4562 p. 5, Lines 6-7 (page not given) | Puts the whole election on line 6; p. 5 missing from the pages; line 8 unchanged. |
| claude | transcription | person.s179_listed | interface gap | 4,319/4,425 agree; 15 project-refuses, 22 project-unknown, 69 value | i4562 p. 5, Line 7 (page not given) | Zero on line 7; p. 5 missing from the pages; line 8 unchanged. |
| claude | transcription | person.sc_total | scope | 4,424/4,425 agree; 1 project-refuses | i1040sc p. 15, Line 32 | Only the cited at-risk refusal. |
| claude | transcription | person.se_line6 | scope | 2,961/4,425 agree; 83 candidate-refuses, 1,380 candidate-unknown, 1 project-refuses | i1040sse p. 1, Who Must File | se_screen/rrta placement and at-risk refusal only. |
| claude | transcription | person.se_line12 | scope | 2,961/4,425 agree; 83 candidate-refuses, 1,380 candidate-unknown, 1 project-refuses | i1040sse p. 1, Who Must File | As se_line6. |
| claude | transcription | person.se_line13 | scope | 2,961/4,425 agree; 83 candidate-refuses, 1,380 candidate-unknown, 1 project-refuses | p560 p. 39 Step 2; i1040sse p. 1 | As se_line6. |
| claude | transcription | Step 2 | scope | 2,961/4,425 agree; 83 candidate-refuses, 1,380 candidate-unknown, 1 project-refuses | p560 p. 39, Step 2 | As se_line13. |
| claude | transcription | Step 1 | scope | 2,937/4,425 agree; 112 project-refuses, 1,376 project-unknown | p560 p. 39, Step 1 | Cited se_screened refusal; evaluation order. |
| claude | transcription | person.s16 | scope | 2,778/4,425 agree; 22 candidate-refuses, 1,552 candidate-unknown, 73 project-refuses | p560 p. 39; i1040gi p. 93 | Capped amounts where the project refuses excess; placements. |
| claude | transcription | person.eic_se | scope | 4,401/4,425 agree; 1 candidate-refuses, 9 project-refuses, 14 project-unknown | i1040gi EIC Worksheet B; i1040sse p. 1 | Now chooses by Schedule SE filing; same amount; cited refusals. |
| claude | transcription | person.dc_has_box10 | representation | 4,425/4,425 agree | i2441 p. 5, Line 12 | No difference. |
| claude | transcription | person.dc_earned | model error | 2,980/4,425 agree; 81 candidate-refuses, 1,352 candidate-unknown, 10 project-refuses, 2 value | i2441 p. 4, item 1 (line 1z) | Omits Form 1040 line 1e. |
| claude | transcription | person.dc_earned_b | scope | 2,979/4,425 agree; 83 candidate-refuses, 1,362 candidate-unknown, 1 project-refuses | i2441 p. 5, Line 18 | Same amount; placements. |
| claude | transcription | person.sav_ineligible | ambiguity | 4,310/4,425 agree; 44 candidate-unknown, 2 project-unknown, 69 value | f8880 p. 2 | amb.2025.savers_ineligible_column. |
| claude | transcription | person.sav_line1 | scope | 4,418/4,425 agree; 1 project-refuses, 6 project-unknown | f8880 line 1; p590a p. 35 | Now gated on sav_trad; only the excess screen. |
| claude | transcription | person.sav_line2 | model error | 4,170/4,425 agree; 132 candidate-refuses, 38 candidate-unknown, 53 project-refuses, 15 project-unknown, 17 value | f8880 p. 2, Line 2 | Drops the self-employed SIMPLE deferral. |
| claude | transcription | person.ira_contrib | scope | 2,626/4,425 agree; 1 candidate-refuses, 1,768 candidate-unknown, 30 project-unknown | i1040gi p. 98, line 11; p590a p. 35 | No sav_trad gate; excess refusal as project. |
| claude | transcription | person.ira_cov | ambiguity | 3,771/4,425 agree; 44 candidate-unknown, 12 project-unknown, 598 value | i1040gi p. 96 | amb.2025.ira_covered. |
| claude | transcription | person.ira_line2 | ambiguity | 4,010/4,425 agree; 5 candidate-refuses, 60 candidate-unknown, 7 project-unknown, 343 value | i1040gi p. 97, line 2 | Joint values follow ira_cov; MFS refused at s3.mfs. |
| claude | transcription | person.ira_line6 | representation | 3,021/4,425 agree; 74 candidate-refuses, 1,106 candidate-unknown, 79 project-refuses, 35 project-unknown, 110 value | i1040gi p. 97, line 6 | Inherited from line 2 and placements. |
| claude | transcription | person.ira_line7 | ambiguity | 4,042/4,425 agree; 1 candidate-refuses, 84 candidate-unknown, 100 project-refuses, 71 project-unknown, 127 value | i1040gi pp. 97-98, line 7 | ira_cov reading; no-contribution helper values reach no amount. |
| claude | transcription | person.ira_deduction | scope | 2,181/4,425 agree; 135 candidate-refuses, 2,069 candidate-unknown, 11 project-refuses, 29 project-unknown | i1040gi p. 98, line 12 | Same formula; inherited placements. |
| claude | transcription | person.ira_nondeductible | scope | 2,181/4,425 agree; 140 candidate-refuses, 2,065 candidate-unknown, 10 project-refuses, 29 project-unknown | i8606 p. 9, Line 1 | Same formula; inherited placements. |
| claude | transcription | person.ira_files_8606 | scope | 2,181/4,425 agree; 140 candidate-refuses, 2,065 candidate-unknown, 10 project-refuses, 29 project-unknown | i8606 p. 2, Who Must File | Extra screened condition; placements. |
| claude | transcription | person.ira_8606_line2 | scope | 2,617/4,425 agree; 1,766 candidate-unknown, 12 project-refuses, 30 project-unknown | i8606 p. 9, Line 2 | Basis for everyone; cited refusals. |
| claude | transcription | person.ira_dist_gate | scope | 2,573/4,425 agree; 140 candidate-refuses, 1,702 candidate-unknown, 10 project-refuses | f8606 Part I | Same gate; placements. |
| claude | transcription | person.ira_8606_line14 | representation | 2,124/4,425 agree; 140 candidate-refuses, 2,121 candidate-unknown, 11 project-refuses, 29 project-unknown | f8606 Part I, line 14 | Same two amounts. |
| claude | transcription | person.ira_ssb | scope | 2,197/4,425 agree; 140 candidate-refuses, 2,049 candidate-unknown, 10 project-refuses, 29 project-unknown | i1040gi p. 98; amb.2025.ira_ssb_copy | Same figure; no sav_trad gate. |
| claude | transcription | person.ira_se | scope | 2,703/4,425 agree; 100 candidate-refuses, 1,548 candidate-unknown, 74 project-refuses | i1040gi p. 97, line 9 | Same amount; placements. |
| claude | transcription | person.edu_kid | model error | 1,533/4,425 agree; 2,723 candidate-unknown, 38 project-refuses, 131 value | i8863 p. 7, Line 7 | No f8863.kid_needed gate. |
| claude | transcription | eligible | representation | 4,384/4,425 agree; 1 project-unknown, 40 value | i1040gi p. 117, Line 11 | Over-limit test belongs to person.credit. |
| claude | transcription | Step 6 | representation | 4,425/4,425 agree | p560 p. 39, Step 6 | No difference. |
| claude | transcription | 27 | model error | 1,711/4,425 agree; 2,714 candidate-unknown | i8863 p. 3 item 5; p. 2; p970 p. 11 | No itin_applied, f8863.paid or filer-TIN test. |
| claude | transcription | 28 | model error | 1,746/4,425 agree; 2,678 candidate-unknown, 1 project-refuses | i8863 p. 3 item 5; p. 2; p970 p. 11 | As line 27. |
| claude | transcription | 29 | model error | 1,746/4,425 agree; 2,678 candidate-unknown, 1 project-refuses | i8863 p. 3 item 5; p. 2; p970 p. 11 | As line 27. |
| claude | transcription | 30 | model error | 1,746/4,425 agree; 2,678 candidate-unknown, 1 project-refuses | i8863 p. 3 item 5; p. 2; p970 p. 11 | As line 27. |
| claude | transcription | 31 | model error | 1,711/4,425 agree; 1 candidate-refuses, 2,713 candidate-unknown | i8863 p. 3 item 5; p. 2; p970 p. 11 | No itin_applied or f8863.paid test. |
| deepseek | transcription | person.educator_deduction | representation | not executable (reply invalid) | i1040gi p. 93, Line 11 | Same formula. |
| deepseek | transcription | person.hsa_agreed | representation | not executable (reply invalid) | i8889 p. 7, Line 6 Step 2 | As the Claude reply. |
| deepseek | transcription | person.hsa_step1 | representation | not executable (reply invalid) | i8889 p. 7, Line 6 Step 2 | Invalid refusal dropped; as the Claude reply. |
| deepseek | transcription | person.hsa_share | interface gap | not executable (reply invalid) | i8889 p. 7, Line 6 Step 3 | share vs share_raw not distinguishable. |
| deepseek | transcription | person.s179_nonlisted | model error | not executable (reply invalid) | i4562 p. 5, Lines 6, 8, 12 | Uses the line 12 deduction: circular. |
| deepseek | transcription | person.s179_listed | interface gap | not executable (reply invalid) | i4562 p. 5, Line 7 (page not given) | Zero; p. 5 missing from the pages. |
| deepseek | transcription | person.income179 | model error | not executable (reply invalid) | i4562 p. 5, Line 11 | Line 31 after section 179: circular. |
| deepseek | transcription | person.sc_total | scope | not executable (reply invalid) | i1040sc p. 15, Line 32 | Only the cited at-risk refusal. |
| deepseek | transcription | Step 1 | scope | not executable (reply invalid) | p560 p. 39, Step 1 | Cited se_screened and at-risk refusals. |
| deepseek | transcription | person.se_line6 | model error | not executable (reply invalid) | i1040sse p. 1, line 4c | Declaration error; $400 test now at line 12. |
| deepseek | transcription | person.se_line12 | model error | not executable (reply invalid) | i1040sse p. 1, line 4c | Declaration error; reading now the source's. |
| deepseek | transcription | person.se_line13 | model error | not executable (reply invalid) | i1040sse line 13 | Declaration error. |
| deepseek | transcription | Step 2 | model error | not executable (reply invalid) | p560 p. 39, Step 2 | Declaration error. |
| deepseek | transcription | Step 3 | model error | not executable (reply invalid) | p560 p. 39, Step 3 | Declaration error. |
| deepseek | transcription | Step 5 | model error | not executable (reply invalid) | p560 pp. 38-39, Step 5 | Declaration error; type errors fixed. |
| deepseek | transcription | Step 6 | representation | not executable (reply invalid) | p560 p. 39, Step 6 | Project's formula for a SEP. |
| deepseek | transcription | Step 7 | model error | not executable (reply invalid) | p560 p. 39, Step 7 | Declaration error. |
| deepseek | transcription | Step 8 | representation | not executable (reply invalid) | p560 p. 39, Step 8 | Zero for no SEP reaches nothing. |
| deepseek | transcription | Step 21 | model error | not executable (reply invalid) | p560 p. 39, Step 21 | Declaration error. |
| deepseek | transcription | person.s16 | model error | not executable (reply invalid) | p560 p. 39; p. 17 | Declaration error; SIMPLE uncapped where project refuses. |
| deepseek | transcription | person.eic_se | model error | not executable (reply invalid) | i1040gi EIC Worksheet B | Declaration error; reading now the project's. |
| deepseek | transcription | person.sc_1a | model error | not executable (reply invalid) | i1040gi p. 104, Schedule 1-A line 5 | Counts sc.statutory, not sc.tips_ot. |
| deepseek | transcription | person.dc_has_box10 | representation | not executable (reply invalid) | i2441 p. 5, Line 12 | Same test. |
| deepseek | transcription | person.dc_earned | model error | not executable (reply invalid) | i2441 p. 4, item 1 | Declaration error; omits line 1e. |
| deepseek | transcription | person.dc_earned_b | model error | not executable (reply invalid) | i2441 p. 5, Line 18 | Declaration error; reading now the project's. |
| deepseek | transcription | person.sav_ineligible | ambiguity | not executable (reply invalid) | f8880 p. 2 | amb.2025.savers_ineligible_column. |
| deepseek | transcription | person.sav_line2 | model error | not executable (reply invalid) | f8880 p. 2, Line 2 | Drops the self-employed SIMPLE deferral. |
| deepseek | transcription | person.ira_contrib | scope | not executable (reply invalid) | i1040gi p. 98, line 11 | No sav_trad gate. |
| deepseek | transcription | person.ira_cov | model error | not executable (reply invalid) | i1040gi p. 96 | Drops own SEP/SIMPLE coverage. |
| deepseek | transcription | person.ira_line2 | representation | not executable (reply invalid) | i1040gi p. 97, line 2 | $246,000 value unused when skipped. |
| deepseek | transcription | person.ira_line6 | model error | not executable (reply invalid) | i1040gi p. 97, lines 4-5 | Declaration error; subtracts line 24a. |
| deepseek | transcription | person.ira_line7 | model error | not executable (reply invalid) | i1040gi pp. 97-98, lines 6-7 | Declaration error; $200 after STOP; uncovered spouse unphased. |
| deepseek | transcription | person.ira_deduction | model error | not executable (reply invalid) | i1040gi p. 98, lines 8-12 | Declaration error; own earnings, not joint line 10. |
| deepseek | transcription | person.ira_nondeductible | model error | not executable (reply invalid) | i8606 p. 9, Line 1 | Declaration error. |
| deepseek | transcription | person.ira_files_8606 | model error | not executable (reply invalid) | i8606 p. 2 | Declaration error. |
| deepseek | transcription | person.ira_8606_line2 | model error | not executable (reply invalid) | i8606 p. 9, Line 2 | Sums f8606.line2, which copies it: circular. |
| deepseek | transcription | person.ira_dist_gate | model error | not executable (reply invalid) | f8606 Part I | Declaration error; reads the circular line 2. |
| deepseek | transcription | person.ira_ssb | model error | not executable (reply invalid) | amb.2025.ira_ssb_copy | Declaration error; copies the deduction: cycle. |
| deepseek | transcription | person.ira_se | model error | not executable (reply invalid) | i1040gi p. 98, line 9; p590a p. 6 | Declaration error; starts from SE line 6. |
| deepseek | transcription | person.edu_kid | model error | not executable (reply invalid) | i8863 p. 7, Line 7 | Age 18 without the support test. |
| deepseek | transcription | 27 | model error | not executable (reply invalid) | i8863 p. 3 item 5; p. 2 | No TIN or f8863.paid tests. |
| deepseek | transcription | 28 | model error | not executable (reply invalid) | i8863 p. 3 item 5; p. 2 | As line 27. |
| deepseek | transcription | 29 | model error | not executable (reply invalid) | i8863 p. 3 item 5; p. 2 | As line 27. |
| deepseek | transcription | 30 | model error | not executable (reply invalid) | i8863 p. 3 item 5; p. 2 | As line 27. |
| deepseek | transcription | 31 | model error | not executable (reply invalid) | i8863 p. 3 item 5; p. 2 | No student TIN or f8863.paid test. |
| deepseek | transcription | wages | representation | not executable (reply invalid) | iw2w3 p. 18 | Boxes 3 plus 7, as project. |
| deepseek | transcription | eligible | representation | not executable (reply invalid) | i1040gi p. 117, Line 11 | As the Claude reply. |
| deepseek | transcription | excess | representation | not executable (reply invalid) | i1040gi p. 117, Line 11 | Gated on eligible; credit unchanged. |
| deepseek | transcription | credit | scope | not executable (reply invalid) | i1040gi p. 117, Line 11 | Zero where project refuses at person.over. |
| deepseek | render | Step 3 | ambiguity | render MISMATCH | p560 p. 39, Step 3 | amb.2025.sep_loss_floor; the English states the chosen floor. |
| deepseek | classm | classm.person.1 — person[taxpayer].wages | model error (dropped) | case inputs: boxes 3+7 = $44,754.00 | iw2w3 p. 18 | Misses emp_b box 7 tips. |

Findings: none on the person entry (no `round3/person.findings.md`). Checked: the round-2 change (the `edu_over` label) is
wording only; the Claude reply's student-TIN test without `person.itin_applied` is the candidate's narrowing, not the
project's error (p970 p. 11). Review-coverage note: the person logs give i4562 pp. 4 and 11 but not p. 5, which holds the
Form 4562 line 6, 7 and 11 instructions; `person.s179_nonlisted` and `s179_listed` cite "i4562 p. 4, Part I", so the
cited-page selection misses p. 5 (a citation-locator gap, not a tax error). The Claude section 179 placements are ruled
interface gap on that ground.

## Stage 21 (superseded subject)

Subject after Stage 21 (Form 5329 Parts I and VII, decisions D1 to D10 in
`research/premises/stage21-form-5329.decisions.md`): the per-person Form 1099-R totals of D1 (`person.ira_amount_a` to
`person.sav_dist`) and the Form 5329 block (`person.x_*`); every other person line is unchanged. Fresh replies of
2026-10-29 (claude-opus-5-5, deepseek-flash). Full ruling text: `.transcription/proposed/stage21/transcription.person.json`,
`transcription.person.deepseek.json`, `render.person.deepseek.json`, `classm.person.json`, `classm.person.deepseek.json`.
Claude triage: `../triage/person.json`, executable-triage-v2 (1,372 fixtures, 500 generated returns seed 20261026, 2,084
partial records; 4,917 comparisons per line). The deepseek-flash reply fails validation on five expressions
(`person.se_line6`, `person.se_line12`, `person.h_se_line4a`, `person.h_sep_10000`, `person.h_educator_cap`, project
schema), so `../triage/person.deepseek.json` is `invalid`; lines reaching them are model errors on the declaration, the
others are ruled by reading. Lines whose expression is unchanged from Stage 19 round 3 keep that ruling with the new
counts; the Claude render log has no open line.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | person.educator_deduction | representation | 3,347/4,917 agree; 1,540 candidate-unknown, 30 project-unknown | i1040gi p. 93, Line 11 | As Stage 19 round 3: same expression; ruling stands. |
| claude | transcription | person.hsa_agreed | representation | 4,624/4,917 agree; 40 candidate-unknown, 253 value | i8889 p. 7, Line 6, Step 2 | As Stage 19 round 3: same expression; ruling stands. |
| claude | transcription | person.hsa_step1 | representation | 4,532/4,917 agree; 3 candidate-unknown, 382 value | i8889 p. 7, Line 6, Step 2 | As Stage 19 round 3: same expression; ruling stands. |
| claude | transcription | person.hsa_share | interface gap | 4,221/4,917 agree; 30 candidate-refuses, 295 candidate-unknown, 371 value | i8889 p. 7, Line 6, Step 2 | As Stage 19 round 3: same expression; ruling stands. |
| claude | transcription | person.s179_nonlisted | interface gap | 4,685/4,917 agree; 221 candidate-refuses, 11 value | i4562 p. 5, Line 6, column | As Stage 19 round 3: same expression; ruling stands. |
| claude | transcription | person.s179_listed | interface gap | 4,663/4,917 agree; 221 project-refuses, 22 project-unknown, 11 value | i4562 p. 5, Line 7 | As Stage 19 round 3: same expression; ruling stands. |
| claude | transcription | person.sc_total | scope | 4,916/4,917 agree; 1 project-refuses | i1040sc p. 15, Line 32, Some investment is not at risk | As Stage 19 round 3: same expression; ruling stands. |
| claude | transcription | person.se_line6 | scope | 3,468/4,917 agree; 26 candidate-refuses, 1,422 candidate-unknown, 1 project-refuses | i1040sse p. 1, Who Must File Schedule SE | As Stage 19 round 3: same expression; ruling stands. |
| claude | transcription | person.se_line12 | scope | 3,468/4,917 agree; 26 candidate-refuses, 1,422 candidate-unknown, 1 project-refuses | i1040sse p. 1, Who Must File Schedule SE | As Stage 19 round 3: same expression; ruling stands. |
| claude | transcription | person.se_line13 | scope | 3,468/4,917 agree; 26 candidate-refuses, 1,422 candidate-unknown, 1 project-refuses | p560 p. 39, Deduction Worksheet for Self-Employed, Step 2 | As Stage 19 round 3: same expression; ruling stands. |
| claude | transcription | person.dc_has_box10 | representation | 4,917/4,917 agree | i2441 p. 5, Line 12 | As Stage 19 round 3: same expression; ruling stands. |
| claude | transcription | person.dc_earned | model error | 3,485/4,917 agree; 24 candidate-refuses, 1,394 candidate-unknown, 12 project-refuses, 2 value | i2441 p. 4 | As Stage 19 round 3: same expression; ruling stands. |
| claude | transcription | person.dc_earned_b | scope | 3,486/4,917 agree; 26 candidate-refuses, 1,404 candidate-unknown, 1 project-refuses | i2441 p. 5, Line 18 | As Stage 19 round 3: same expression; ruling stands. |
| claude | transcription | person.sav_ineligible | ambiguity | 4,733/4,917 agree; 46 candidate-unknown, 2 project-unknown, 136 value | f8880 p. 2; amb.2025.savers_ineligible_column | As Stage 19 round 3: same expression; ruling stands. |
| claude | transcription | person.sav_line1 | scope | 4,912/4,917 agree; 1 project-refuses, 4 project-unknown | f8880 line 1 | As Stage 19 round 3: same expression; ruling stands. |
| claude | transcription | person.ira_contrib | scope | 3,077/4,917 agree; 1 candidate-refuses, 1,808 candidate-unknown, 31 project-unknown | i1040gi p. 98, line 11 | As Stage 19 round 3: same expression; ruling stands. |
| claude | transcription | person.ira_cov | ambiguity | 4,260/4,917 agree; 47 candidate-unknown, 10 project-unknown, 600 value | i1040gi p. 96; amb.2025.ira_covered | As Stage 19 round 3: same expression; ruling stands. |
| claude | transcription | person.ira_line2 | ambiguity | 4,559/4,917 agree; 5 candidate-refuses, 61 candidate-unknown, 6 project-unknown, 286 value | i1040gi p. 97, line 2 | As Stage 19 round 3: same expression; ruling stands. |
| claude | transcription | person.ira_line6 | representation | 3,563/4,917 agree; 76 candidate-refuses, 1,089 candidate-unknown, 40 project-refuses, 24 project-unknown, 125 value | i1040gi p. 97, line 6 | As Stage 19 round 3: same expression; ruling stands. |
| claude | transcription | person.ira_8606_line2 | scope | 3,066/4,917 agree; 1,807 candidate-unknown, 12 project-refuses, 32 project-unknown | i8606 p. 9, Line 2 | As Stage 19 round 3: same expression; ruling stands. |
| claude | transcription | person.ira_ssb | scope | 2,293/4,917 agree; 545 candidate-refuses, 2,043 candidate-unknown, 10 project-refuses, 26 project-unknown | i1040gi p. 98, line 12 | As Stage 19 round 3: same expression; ruling stands. |
| claude | transcription | eligible | representation | 4,875/4,917 agree; 1 project-unknown, 41 value | i1040gi p. 117, Line 11 | As Stage 19 round 3: same expression; ruling stands. |
| claude | transcription | Step 1 | scope | 3,447/4,917 agree; 2 candidate-refuses, 56 project-refuses, 1,412 project-unknown | p560 p. 39, Deduction Worksheet for Self-Employed, Step 1 | As Stage 19 round 3: same expression; ruling stands. |
| claude | transcription | Step 2 | scope | 3,468/4,917 agree; 26 candidate-refuses, 1,422 candidate-unknown, 1 project-refuses | p560 p. 39, Deduction Worksheet for Self-Employed, Step 2 | As Stage 19 round 3: same expression; ruling stands. |
| claude | transcription | Step 6 | representation | 4,917/4,917 agree | p560 p. 39, Step 6 | As Stage 19 round 3: same expression; ruling stands. |
| claude | transcription | person.s16 | scope | 3,199/4,917 agree; 82 candidate-refuses, 1,601 candidate-unknown, 35 project-refuses | p560 p. 39, after Step 21 | SIMPLE helpers restructured; no value differs; placements. |
| claude | transcription | person.eic_se | scope | 3,468/4,917 agree; 26 candidate-refuses, 1,422 candidate-unknown, 1 project-refuses | i1040gi EIC Worksheet B, Part 1 | Now line 3 less line 13 for everyone; same amount; placements. |
| claude | transcription | person.sav_line2 | scope | 3,421/4,917 agree; 216 candidate-refuses, 1,260 candidate-unknown, 10 project-refuses, 10 value | f8880 p. 2, Line 2 | Round-3 omission fixed; values only on refused over-limit SIMPLE returns. |
| claude | transcription | person.ira_line7 | ambiguity | 4,327/4,917 agree; 349 candidate-refuses, 132 candidate-unknown, 33 project-refuses, 7 project-unknown, 69 value | amb.2025.ira_covered; i1040gi pp. 97-98, line 7 | Now tests anyone_covered; values follow ira_cov (amb.2025.ira_covered). |
| claude | transcription | person.ira_deduction | scope | 2,173/4,917 agree; 654 candidate-refuses, 2,054 candidate-unknown, 11 project-refuses, 25 project-unknown | i1040gi p. 98 | Same formula; refusal declarations dropped; inherited placements. |
| claude | transcription | person.ira_nondeductible | scope | 2,173/4,917 agree; 654 candidate-refuses, 2,055 candidate-unknown, 10 project-refuses, 25 project-unknown | i8606 p. 9, Line 1 | Same formula; inherited placements. |
| claude | transcription | person.ira_files_8606 | scope | 2,173/4,917 agree; 654 candidate-refuses, 2,055 candidate-unknown, 10 project-refuses, 25 project-unknown | i8606 p. 2, Who Must File | Basis condition screened at retirement.special; placements. |
| claude | transcription | person.ira_dist_gate | scope | 3,153/4,917 agree; 21 candidate-refuses, 1,731 candidate-unknown, 12 project-refuses | f8606 | Same gate plus screened basis condition; placements. |
| claude | transcription | person.ira_8606_line14 | scope | 2,124/4,917 agree; 654 candidate-refuses, 2,103 candidate-unknown, 11 project-refuses, 25 project-unknown | f8606 (2025) Part I, line 14 | Same two amounts; placements. |
| claude | transcription | person.ira_se | scope | 3,182/4,917 agree; 101 candidate-refuses, 1,595 candidate-unknown, 39 project-refuses | i1040gi p. 97, line 9 | eic_se less s16, the same amount; placements. |
| claude | transcription | person.edu_kid | model error | 3,139/4,917 agree; 1,669 candidate-unknown, 42 project-refuses, 67 value | i8863 p. 7, Line 7 | Still no f8863.kid_needed gate. |
| claude | transcription | 27 | model error | 2,480/4,917 agree; 2,437 candidate-unknown | i8863 p. 3, Who cannot claim a credit | Restructured, same logic: no itin_applied or f8863.paid test. |
| claude | transcription | 28 | model error | 2,480/4,917 agree; 2,437 candidate-unknown | i8863 p. 3, Who cannot claim a credit | Restructured, same logic: no itin_applied or f8863.paid test. |
| claude | transcription | 29 | model error | 2,480/4,917 agree; 2,437 candidate-unknown | i8863 p. 3, Who cannot claim a credit | Restructured, same logic: no itin_applied or f8863.paid test. |
| claude | transcription | 30 | model error | 2,480/4,917 agree; 2,437 candidate-unknown | i8863 p. 3, Who cannot claim a credit | Restructured, same logic: no itin_applied or f8863.paid test. |
| claude | transcription | 31 | model error | 2,479/4,917 agree; 1 candidate-refuses, 2,437 candidate-unknown | i8863 p. 3, Who cannot claim a credit | Restructured, same logic: no itin_applied or f8863.paid test. |
| claude | transcription | person.ira_amount_a | representation | 4,917/4,917 agree | i1040gi p. 26, Lines 4a and 4b, IRA Distributions | Same per-person sum (D1); reference vs input only. |
| claude | transcription | person.ira_taxable | representation | 4,917/4,917 agree | i1040gi p. 26, Lines 4a and 4b, IRA Distributions | Same per-person sum (D1). |
| claude | transcription | person.ira_rollovers | representation | 4,917/4,917 agree | i1040gi pp. 26-27, Lines 4a and 4b, rollovers | Same count (D1). |
| claude | transcription | person.plan_amount_a | representation | 4,917/4,917 agree | i1040gi p. 28, Lines 5a and 5b, Pensions and Annuities | Same per-person sum (D1). |
| claude | transcription | person.plan_taxable | representation | 4,917/4,917 agree | i1040gi p. 28, Lines 5a and 5b, Pensions and Annuities | Same per-person sum (D1). |
| claude | transcription | person.plan_rollovers | representation | 4,917/4,917 agree | i1040gi pp. 28-29, Lines 5a and 5b, rollovers | Same count (D1). |
| claude | transcription | person.x_c05 | model error | 4,916/4,917 agree; 1 value | i5329 p. 5, Line 2, exception 05 | No Schedule A line 4 limit (stage21.blind.e6: $9,000.00 against $7,475.00). |
| claude | transcription | person.x_l2_all | model error | 1,871/4,917 agree; 3,045 candidate-unknown, 1 value | i5329 p. 5, Line 2 | Needs x_prior09/x_births on every return; its value is line 2 after limits, the printed line agrees. |
| claude | transcription | person.x_limited_sum | model error | 1,871/4,917 agree; 3,046 candidate-unknown | i5329 p. 5, Line 2 | Needs x_prior09/x_births everywhere; omits exception 05 from the limited set. |
| claude | transcription | person.x_other_exc | model error | 4,912/4,917 agree; 5 value | i5329 p. 5, Line 2, exception 05 | Carries exception 05 unlimited (stage21.blind.e6). |
| claude | transcription | person.x_limit_binds | model error | 1,870/4,917 agree; 3,045 candidate-unknown, 1 project-refuses, 1 value | i5329 p. 5, Line 4 | Drops the code S condition (stage21.blind.e4 True against False); unknown as x_l2_all. |
| deepseek | transcription | person.hsa_agreed | representation | not executable (reply invalid) | i8889 p. 7, Line 6, Step 2 | As Stage 19 round 3; same expression. |
| deepseek | transcription | person.hsa_step1 | representation | not executable (reply invalid) | i8889 p. 7, Line 6, Step 2 | As Stage 19 round 3; same expression. |
| deepseek | transcription | person.hsa_share | interface gap | not executable (reply invalid) | i8889 p. 7, Line 6, Step 3 | As Stage 19 round 3; same expression. |
| deepseek | transcription | person.s179_listed | interface gap | not executable (reply invalid) | i4562 p. 5, Line 7 | As Stage 19 round 3; same expression. |
| deepseek | transcription | person.sc_total | scope | not executable (reply invalid) | i1040sc p. 15, Line 32, Some investment is not at risk | As Stage 19 round 3; same expression. |
| deepseek | transcription | person.sc_1a | model error | not executable (reply invalid) | i1040gi p. 104, Schedule 1-A Line 5 | As Stage 19 round 3; same expression. |
| deepseek | transcription | person.sav_ineligible | ambiguity | not executable (reply invalid) | f8880 p. 2; amb.2025.savers_ineligible_column | As Stage 19 round 3; same expression. |
| deepseek | transcription | person.educator_deduction | model error | not executable (reply invalid) | i1040gi p. 93, Line 11 | Declaration error (malformed expression in its closure). |
| deepseek | transcription | person.se_line6 | model error | not executable (reply invalid) | i1040sse p. 1, line 4c | Declaration error (malformed expression in its closure). |
| deepseek | transcription | person.se_line12 | model error | not executable (reply invalid) | i1040sse p. 1, line 12 | Declaration error (malformed expression in its closure). |
| deepseek | transcription | person.se_line13 | model error | not executable (reply invalid) | i1040sse line 13 | Declaration error (malformed expression in its closure). |
| deepseek | transcription | person.s16 | model error | not executable (reply invalid) | p560 p. 39, after Step 21 | Declaration error (malformed expression in its closure). |
| deepseek | transcription | person.eic_se | model error | not executable (reply invalid) | i1040gi EIC Worksheet B, Part 1 | Declaration error (malformed expression in its closure). |
| deepseek | transcription | person.dc_earned | model error | not executable (reply invalid) | i2441 p. 4 | Declaration error (malformed expression in its closure). |
| deepseek | transcription | person.dc_earned_b | model error | not executable (reply invalid) | i2441 p. 5, Line 18 | Declaration error (malformed expression in its closure). |
| deepseek | transcription | person.ira_se | model error | not executable (reply invalid) | i1040gi p. 97, line 9 | Declaration error (malformed expression in its closure). |
| deepseek | transcription | Step 2 | model error | not executable (reply invalid) | p560 p. 39, Step 2 | Declaration error (malformed expression in its closure). |
| deepseek | transcription | Step 3 | model error | not executable (reply invalid) | p560 p. 39, Step 3 | Declaration error (malformed expression in its closure). |
| deepseek | transcription | Step 5 | model error | not executable (reply invalid) | p560 pp. 38-39, Rate Worksheet and Step 5 | Declaration error (malformed expression in its closure). |
| deepseek | transcription | Step 6 | model error | not executable (reply invalid) | p560 p. 39, Step 6 | Declaration error (malformed expression in its closure). |
| deepseek | transcription | Step 7 | model error | not executable (reply invalid) | p560 p. 39, Step 7 | Declaration error (malformed expression in its closure). |
| deepseek | transcription | Step 21 | model error | not executable (reply invalid) | p560 p. 39, Step 21 | Declaration error (malformed expression in its closure). |
| deepseek | transcription | person.hsa_forms | model error | not executable (reply invalid) | i8889 p. 4, Name and social security number | Counts only forms with contributions; a distribution-only Form 8889 escapes hsa_repeated. |
| deepseek | transcription | person.ira_taxable | model error | not executable (reply invalid) | i1040gi p. 26, Lines 4a and 4b, IRA Distributions | No IRA filter: pension entries added to line 4b (stage21.blind.e4: $19,000.00 against $15,500.00). |
| deepseek | transcription | person.plan_amount_a | representation | not executable (reply invalid) | i1040gi p. 28, Lines 5a and 5b, Pensions and Annuities | Same sum (D1). |
| deepseek | transcription | person.plan_taxable | representation | not executable (reply invalid) | i1040gi p. 28, Lines 5a and 5b, Pensions and Annuities | Same sum (D1). |
| deepseek | transcription | person.plan_rollovers | representation | not executable (reply invalid) | i1040gi pp. 28-29, Lines 5a and 5b, rollovers | Same count (D1). |
| deepseek | transcription | person.s179_nonlisted | interface gap | not executable (reply invalid) | i4562 p. 5, Line 6, column | Now the Claude expression; p. 5 of i4562 not given. |
| deepseek | transcription | person.income179 | model error | not executable (reply invalid) | i4562 p. 5, Line 11 | Sums positive line 29: drops losses and line 30. |
| deepseek | transcription | person.positive_profits | representation | not executable (reply invalid) | see ruling | Same total of profits. |
| deepseek | transcription | person.dc_has_box10 | model error | not executable (reply invalid) | i2441 p. 5, Line 12 | Tests box 10 net of the box 1 part, not box 10. |
| deepseek | transcription | person.sav_line1 | scope | not executable (reply invalid) | f8880 line 1 | No sav_trad gate; excess refusal as project. |
| deepseek | transcription | person.sav_line2 | model error | not executable (reply invalid) | f8880 p. 2, Line 2 | Omits own SIMPLE deferrals. |
| deepseek | transcription | person.ira_contrib | scope | not executable (reply invalid) | i1040gi p. 98, line 11 | No sav_trad gate; excess refusal. |
| deepseek | transcription | person.ira_cov | model error | not executable (reply invalid) | i1040gi p. 96; amb.2025.ira_covered | Drops own SEP/SIMPLE coverage. |
| deepseek | transcription | person.ira_line2 | model error | not executable (reply invalid) | i1040gi p. 97, line 2 | Copies ira.line2a/2b built from it: cycle. |
| deepseek | transcription | person.ira_line6 | model error | not executable (reply invalid) | i1040gi p. 97, line 6 | Copies ira.line6a/6b: cycle. |
| deepseek | transcription | person.ira_line7 | model error | not executable (reply invalid) | i1040gi pp. 97-98, line 7 | Copies ira.line7a/7b: cycle. |
| deepseek | transcription | person.ira_deduction | model error | not executable (reply invalid) | i1040gi p. 98 | Copies ira.line12a/12b: cycle. |
| deepseek | transcription | person.ira_nondeductible | model error | not executable (reply invalid) | i8606 p. 9, Line 1 | Sums f8606.line1, a copy of it: cycle. |
| deepseek | transcription | person.ira_files_8606 | model error | not executable (reply invalid) | i8606 p. 2, Who Must File | Reads circular lines; basis alone triggers. |
| deepseek | transcription | person.ira_8606_line2 | model error | not executable (reply invalid) | i8606 p. 9, Line 2 | Sums f8606.line2, a copy of it: cycle. |
| deepseek | transcription | person.ira_dist_gate | model error | not executable (reply invalid) | f8606 | Copies ira_dist alone. |
| deepseek | transcription | person.ira_ssb | model error | not executable (reply invalid) | amb.2025.ira_ssb_copy; i1040gi p. 98, line 12 | Copies the circular deduction. |
| deepseek | transcription | person.edu_kid | model error | not executable (reply invalid) | i8863 p. 7, Line 7 | Age 18 without the support test; no kid_needed gate. |
| deepseek | transcription | eligible | representation | not executable (reply invalid) | i1040gi p. 117, Line 11 | Extra over-limit test belongs to person.credit. |
| deepseek | transcription | Step 1 | scope | not executable (reply invalid) | p560 p. 39, Step 1 | Cited se_screened, at-risk and plan_screen refusals. |
| deepseek | transcription | 27 | model error | not executable (reply invalid) | i8863 p. 3, Who cannot claim a credit | Copies aqee for everyone: no eligibility or TIN gates. |
| deepseek | transcription | 28 | model error | not executable (reply invalid) | i8863 p. 3, Who cannot claim a credit | Copies aqee for everyone: no eligibility or TIN gates. |
| deepseek | transcription | 29 | model error | not executable (reply invalid) | i8863 p. 3, Who cannot claim a credit | Copies aqee for everyone: no eligibility or TIN gates. |
| deepseek | transcription | 30 | model error | not executable (reply invalid) | i8863 p. 3, Who cannot claim a credit | Copies aqee for everyone: no eligibility or TIN gates. |
| deepseek | transcription | 31 | model error | not executable (reply invalid) | i8863 p. 3, Who cannot claim a credit | Copies aqee for everyone: no eligibility or TIN gates. |
| deepseek | transcription | person.x_tax | model error | not executable (reply invalid) | f5329 p. 1, Part I, line 4 | No per-person limits and no Part VII (stage21.blind.e4: $0.00 against $520.00). |
| deepseek | transcription | person.x_must | model error | not executable (reply invalid) | i5329 p. 1, Who Must File | Counts code 1 entries: no no-form path (Tom Jones 1 against 0). |
| deepseek | transcription | person.x_c05 | model error | not executable (reply invalid) | i5329 p. 5, Line 2, exception 05 | No Schedule A line 4 limit. |
| deepseek | transcription | person.x_two23 | model error | not executable (reply invalid) | p590b p. 28, Distribution limits | Any 22 or 23 amount, not two 23 entries. |
| deepseek | transcription | person.x_limited_sum | model error | not executable (reply invalid) | p590b p. 27, First home | No limits at all (stage21.blind.e4: $19,000.00 against $13,800.00). |
| deepseek | transcription | person.x_limit_binds | model error | not executable (reply invalid) | i5329 p. 5, Line 4 | Any limited exception present: would refuse e6. |
| deepseek | render | Step 3 | ambiguity | render MISMATCH | p560 p. 39, Step 3 | amb.2025.sep_loss_floor; the English states the chosen floor. |
| claude | classm | classm.person.1 — person[taxpayer].wages | model error (dropped) | case inputs: boxes 3+7 = $44,754.00 | iw2w3 p. 18 | Uses box 1; misses emp_b box 7 tips. |
| deepseek | classm | classm.person.1 — person[taxpayer].wages | model error (dropped) | case inputs: boxes 3+7 = $44,754.00 | iw2w3 p. 18 | Uses box 1; misses emp_b box 7 tips. |

Findings: one, medium severity, from scrutiny of the Stage 21 block rather than from a reply — F1 `VALUE-LIMBS`,
`person.x_c22` and `person.x_c23` apply only the $10,300 and $1,000 limits; the 50%-of-value and interest-less-$1,000 limbs
of p590b p. 28 are neither computed nor attested by any question, although D4 and the `params` locators say they are
attested (witness: `stage21.mut.e23_over_cap` with $1,000.00 claimed, line 4 $200.00 against $220.00 for an IRA interest
of $1,800.00; `.transcription/proposed/stage21/person.findings.md`). Checked without finding: the 05 limit at Schedule A
line 4 and the joint refusal (`s2.e05_over`), the 09 limit less earlier distributions (p590b p. 27, item 3 and the
spouse tip), the 19 limit per birth (`amb.2025.f5329_birth_cap`), the one-a-year rule of 23 (`x_two23`), the code S
refusal `x_limit_binds` (`amb.2025.f5329_simple_limits`), the D3(b) screen `x_other` (its wording covers every D3(b)
item), `x_hsa_value` asked only with an excess, `x_hsa_excess` (line 2 less line 13 plus the employer excess), and
`x_must` against i5329 p. 1; each was evaluated on the 24 `stage21` fixtures. Noted: the three-year rule of exception 23
(p590b p. 28) is not screened (left to the filer's exception answer), and the `retirement.code` question wording does not
list the Stage 21 codes (retirement's owner).

## Fix round 2 (superseded subject)

Subject after the screen and completeness fixes of 2026-10-30 (BUG-0219 to BUG-0251): no person expression changed; the
reworded questions are `person.tin` (BUG-0225, an expired ITIN), `person.edu_1098t` (BUG-0226, the cooperation condition),
`person.edu_inst` (BUG-0227, sports, hobby and noncredit courses) and `person.x_other` (BUG-0242, an RMD not received in
full). Fresh replies of 2026-10-30 (claude-opus-5-5, deepseek-flash); Stage 21 logs archived in
`.transcription/archive/before-fix-round2-2026-10-30/`. Full ruling text: `.transcription/proposed/fixr2/transcription.person.json`,
`transcription.person.deepseek.json`, `render.person.json`, `render.person.deepseek.json`. Claude triage: `../triage/person.json`,
executable-triage-v2 (1,382 fixtures, 500 generated returns seed 20261026, 2,014 partial records; 4,711 comparisons per line);
every witness was listed by a scratch rerun of `tools/transcription/triage.mjs` with the witness cap lifted, and every
completed-return value difference was checked against its ruling's mechanism. The deepseek-flash reply fails validation on
three expressions (`person.positive_profits`, `person.dc_earned`, `person.dc_earned_b`: "model changed a published result
type"), so `../triage/person.deepseek.json` is `invalid`; those three are model errors on the declaration and the others are
ruled by reading. The class M logs have no open line.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | person.educator_deduction | representation | 3,046/4,711 agree; 28 project-unknown, 1,637 candidate-unknown | i1040gi p. 93, Line 11 | Same deduction; question order only. |
| claude | transcription | person.hsa_step1 | representation | 4,423/4,711 agree; 285 value, 3 candidate-unknown | i8889 p. 7, Line 6, Step 2 | All values non-split forms, project $0.00; no amount. |
| claude | transcription | person.hsa_share | interface gap | 4,111/4,711 agree; 274 value, 30 candidate-refuses, 296 candidate-unknown | i8889 p. 7, Line 6, Steps 2-3 | Cycle through f8889.share (unlabelled interface); values non-split. |
| claude | transcription | person.ira_amount_a | representation | 4,711/4,711 agree | i1040gi p. 26, Lines 4a and 4b | Same per-person sum (D1). |
| claude | transcription | person.ira_taxable | representation | 4,711/4,711 agree | i1040gi p. 26, Lines 4a and 4b | Same per-person sum (D1). |
| claude | transcription | person.ira_rollovers | representation | 4,711/4,711 agree | i1040gi pp. 26-27, rollovers | Same count (D1). |
| claude | transcription | person.plan_amount_a | representation | 4,711/4,711 agree | i1040gi p. 28, Lines 5a and 5b | Same per-person sum (D1). |
| claude | transcription | person.plan_taxable | representation | 4,711/4,711 agree | i1040gi p. 28, Lines 5a and 5b | Same per-person sum (D1). |
| claude | transcription | person.plan_rollovers | representation | 4,711/4,711 agree | i1040gi pp. 28-29, rollovers | Same count (D1). |
| claude | transcription | person.se_line6 | scope | 3,166/4,711 agree; 25 candidate-refuses, 1,520 candidate-unknown | i1040sse p. 1, Who Must File Schedule SE | Now on sc.result; se_screen/rrta placement only; no value. |
| claude | transcription | person.se_line12 | scope | 3,166/4,711 agree; 25 candidate-refuses, 1,520 candidate-unknown | i1040sse p. 1, Who Must File Schedule SE | Now on sc.result; se_screen/rrta placement only; no value. |
| claude | transcription | person.se_line13 | scope | 3,166/4,711 agree; 25 candidate-refuses, 1,520 candidate-unknown | f1040sse line 13 | Now on sc.result; se_screen/rrta placement only; no value. |
| claude | transcription | Step 2 | scope | 3,166/4,711 agree; 25 candidate-refuses, 1,520 candidate-unknown | p560 p. 39, Step 2 | Copies se_line13; placements. |
| claude | transcription | person.eic_se | scope | 3,164/4,711 agree; 27 candidate-refuses, 1,520 candidate-unknown | i1040gi EIC Worksheet B, Parts 1-2 | Now on sc.result; same amount; placements. |
| claude | transcription | person.dc_earned_b | scope | 3,182/4,711 agree; 27 candidate-refuses, 1,502 candidate-unknown | i2441 p. 5, Line 18 | Same sum; placements. |
| claude | transcription | person.dc_earned | model error | 3,181/4,711 agree; 2 value, 11 project-refuses, 25 candidate-refuses, 1,492 candidate-unknown | i2441 p. 4 | Still omits line 1e (classm.carloan.1: $238,056.00 against $234,528.00, refused). |
| claude | transcription | person.dc_has_box10 | representation | 4,711/4,711 agree | i2441 p. 5, Line 12 | No difference. |
| claude | transcription | person.s16 | scope | 3,147/4,711 agree; 37 project-refuses, 8 candidate-refuses, 1,519 candidate-unknown | p560 p. 39, after Step 21 | SIMPLE helpers restructured; no value; cited refusals and placements. |
| claude | transcription | person.sav_ineligible | ambiguity | 4,466/4,711 agree; 197 value, 4 project-unknown, 44 candidate-unknown | f8880 p. 2; amb.2025.savers_ineligible_column | All 197 values: sav_claimed yes with sa.dependent no (unproducible). |
| claude | transcription | person.sav_line2 | scope | 3,248/4,711 agree; 10 value, 10 project-refuses, 98 candidate-refuses, 1,345 candidate-unknown | f8880 p. 2, Line 2 | Own SIMPLE deferral now capped at compensation; values only where project refuses simple_excess. |
| claude | transcription | person.ira_cov | ambiguity | 4,238/4,711 agree; 419 value, 8 project-unknown, 46 candidate-unknown | i1040gi p. 96; amb.2025.ira_covered | All 419 values: plan answer without Schedule C; completed ones without traditional contribution. |
| claude | transcription | person.ira_line2 | ambiguity | 1,764/4,711 agree; 1,636 value, 1 candidate-refuses, 5 project-unknown, 1,305 candidate-unknown | i1040gi p. 97, line 2; amb.2025.ira_covered | $246,000 now status-free: equal wherever line 2 is reached; joint values follow ira_cov. |
| claude | transcription | person.ira_line6 | representation | 2,288/4,711 agree; 1,186 value, 41 project-refuses, 10 candidate-refuses, 26 project-unknown, 1,160 candidate-unknown | i1040gi p. 97, line 6 | Inherited from line 2 and ira_cov; all completed values inside skipped lines. |
| claude | transcription | person.ira_line7 | model error | 63/4,711 agree; 2,589 value, 220 project-refuses, 1 candidate-refuses, 1,770 project-unknown, 68 candidate-unknown | i1040gi p. 97, line 6; p. 98, line 7 | New zero for a non-contributor: printed 7b $7,000.00 against $0.00 (stage16.mut.ira_joint_full_edge); 867 others reach nothing. |
| claude | transcription | person.ira_deduction | scope | 4,669/4,711 agree; 11 project-refuses, 2 candidate-refuses, 29 candidate-unknown | i1040gi p. 98, line 12 | Now sav_trad-gated; no value; cited Pub. 590-A refusals. |
| claude | transcription | person.ira_nondeductible | scope | 2,582/4,711 agree; 10 project-refuses, 232 candidate-refuses, 1,887 candidate-unknown | i8606 p. 9, Line 1 | Same formula; placements. |
| claude | transcription | person.ira_files_8606 | scope | 2,551/4,711 agree; 10 project-refuses, 232 candidate-refuses, 1,918 candidate-unknown | i8606 p. 2, Who Must File | Basis condition screened at retirement.special; placements. |
| claude | transcription | person.ira_8606_line2 | scope | 2,897/4,711 agree; 12 project-refuses, 30 project-unknown, 1,772 candidate-unknown | i8606 p. 9, Line 2 | Same expression; placements. |
| claude | transcription | person.ira_dist_gate | scope | 2,761/4,711 agree; 10 project-refuses, 232 candidate-refuses, 1,708 candidate-unknown | f8606 Part I | Same gate plus screened basis condition; placements. |
| claude | transcription | person.ira_8606_line14 | scope | 2,496/4,711 agree; 11 project-refuses, 232 candidate-refuses, 1,972 candidate-unknown | f8606 Part I, line 14 | Same two amounts; placements. |
| claude | transcription | person.ira_ssb | scope | 4,670/4,711 agree; 10 project-refuses, 1 candidate-refuses, 30 candidate-unknown | i1040gi p. 98; amb.2025.ira_ssb_copy | Now sav_trad-gated; no value; placements. |
| claude | transcription | person.ira_se | scope | 3,090/4,711 agree; 36 project-refuses, 28 candidate-refuses, 1,557 candidate-unknown | i1040gi p. 98, line 9 | sc.result less lines 15 and 16, floored; same amount. |
| claude | transcription | person.edu_kid | model error | 2,887/4,711 agree; 65 value, 97 project-refuses, 2 project-unknown, 1,660 candidate-unknown | i8863 pp. 6-7, Line 7 | Still no f8863.kid_needed gate; values only with kid_needed false. |
| claude | transcription | person.x_l2_all | scope | 4,705/4,711 agree; 5 value, 1 candidate-refuses | i5329 p. 5, Line 2 | Unknowns gone; after-limit line 2 against before-limit helper; f5329.must agrees. |
| claude | transcription | person.x_c05 | model error | 4,710/4,711 agree; 1 value | i5329 p. 5, exception 05 | No Schedule A line 4 limit (stage21.blind.e6: $9,000.00 against $7,475.00). |
| claude | transcription | person.x_other_exc | model error | 4,706/4,711 agree; 5 value | i5329 p. 5, exception 05 | Carries 05 unlimited (stage21.blind.e6). |
| claude | transcription | person.x_limited_sum | model error | 4,701/4,711 agree; 10 value | i5329 p. 5, Line 2 | 05 limit never applied (e6); before/after-limit meaning not in interface. |
| claude | transcription | person.x_limit_binds | interface gap | 4,706/4,711 agree; 4 value, 1 project-refuses | i5329 p. 5, Line 4; amb.2025.f5329_simple_limits | No code S condition; the project scope decision is not in the id-only interface (Stage 21: model error). |
| claude | transcription | eligible | representation | 4,703/4,711 agree; 7 value, 1 project-unknown | i1040gi p. 117, Line 11 | Over test placed in eligible; values only where project refuses person.credit. |
| claude | transcription | Step 6 | representation | 4,711/4,711 agree | p560 p. 39, Step 6 | No difference. |
| claude | transcription | 27 | model error | 2,371/4,711 agree; 2 value, 1 project-unknown, 2,337 candidate-unknown | i8863 p. 3, Who cannot claim a credit | Adds sav_claimed; still no itin_applied or f8863.paid; values unproducible. |
| claude | transcription | 28 | model error | 2,371/4,711 agree; 2 value, 1 project-unknown, 2,337 candidate-unknown | i8863 p. 3, Who cannot claim a credit | Adds sav_claimed; still no itin_applied or f8863.paid; values unproducible. |
| claude | transcription | 29 | model error | 2,371/4,711 agree; 2 value, 1 project-unknown, 2,337 candidate-unknown | i8863 p. 3, Who cannot claim a credit | Adds sav_claimed; still no itin_applied or f8863.paid; values unproducible. |
| claude | transcription | 30 | model error | 2,371/4,711 agree; 2 value, 1 project-unknown, 2,337 candidate-unknown | i8863 p. 3, Who cannot claim a credit | Adds sav_claimed; still no itin_applied or f8863.paid; values unproducible. |
| claude | transcription | 31 | model error | 2,306/4,711 agree; 56 value, 9 project-unknown, 2,340 candidate-unknown | i8863 p. 3, Who cannot claim a credit | Adds sav_claimed; still no itin_applied or f8863.paid; values unproducible. |
| deepseek | transcription | person.educator_deduction | representation | not executable (reply invalid) | i1040gi p. 93, Line 11 | Now the Claude formula; question order only. |
| deepseek | transcription | person.hsa_agreed | representation | not executable (reply invalid) | i8889 p. 7, Line 6, Step 2 | As Stage 21. |
| deepseek | transcription | person.hsa_step1 | representation | not executable (reply invalid) | i8889 p. 7, Line 6, Step 2 | As Stage 21; adds h_hsa_unsupported placement. |
| deepseek | transcription | person.hsa_share | interface gap | not executable (reply invalid) | i8889 p. 7, Line 6, Step 3 | As Stage 21: cycle through f8889.share. |
| deepseek | transcription | person.ira_taxable | scope | not executable (reply invalid) | i1040gi p. 26, Lines 4a and 4b | IRA filter fixed; bypasses retirement.taxable refusals. |
| deepseek | transcription | person.plan_taxable | scope | not executable (reply invalid) | i1040gi p. 28, Lines 5a and 5b | Same amount; bypasses retirement.taxable refusals. |
| deepseek | transcription | person.s179_nonlisted | model error | not executable (reply invalid) | i4562 p. 5, Line 6 | Reads line 12 (allowed deduction): cycle; sc.f6 published. |
| deepseek | transcription | person.s179_listed | interface gap | not executable (reply invalid) | i4562 p. 5, Line 7 | As Stage 21; p. 5 not given. |
| deepseek | transcription | person.income179 | model error | not executable (reply invalid) | i4562 p. 5, Line 11 | Schedule C line 31 after section 179: cycle. |
| deepseek | transcription | person.sc_total | scope | not executable (reply invalid) | i1040sc p. 15, Line 32 | As Stage 21: at-risk refusal. |
| deepseek | transcription | person.se_line6 | scope | not executable (reply invalid) | f1040sse lines 4a-6 | Now valid and correct; se_screen placement, no rrta refusal (cited project refusal). |
| deepseek | transcription | person.se_line12 | scope | not executable (reply invalid) | f1040sse lines 9-12 | Now valid and correct; placements. |
| deepseek | transcription | person.se_line13 | scope | not executable (reply invalid) | f1040sse line 13 | Now valid and correct; placements. |
| deepseek | transcription | person.s16 | scope | not executable (reply invalid) | p560 p. 39; p. 17 | SIMPLE unlimited only where project refuses simple_excess; placements. |
| deepseek | transcription | person.positive_profits | model error | not executable (reply invalid) | f7206 line 5 | Declaration error: Bool for NonNegDollars. |
| deepseek | transcription | person.eic_se | scope | not executable (reply invalid) | i1040gi EIC Worksheet B | Now valid; same amount; placements. |
| deepseek | transcription | person.sc_1a | model error | not executable (reply invalid) | i1040gi p. 104, Schedule 1-A Line 5 | As Stage 21: statutory, not tips_ot. |
| deepseek | transcription | person.dc_has_box10 | representation | not executable (reply invalid) | i2441 p. 5, Line 12 | Now the Claude expression. |
| deepseek | transcription | person.dc_earned | model error | not executable (reply invalid) | i2441 p. 4 | Declaration error; omits line 1e, floors SE loss. |
| deepseek | transcription | person.dc_earned_b | model error | not executable (reply invalid) | i2441 p. 5, Line 18 | Declaration error. |
| deepseek | transcription | person.sav_ineligible | ambiguity | not executable (reply invalid) | f8880 p. 2; amb.2025.savers_ineligible_column | Now the Claude expression. |
| deepseek | transcription | person.sav_line1 | scope | not executable (reply invalid) | f8880 line 1 | As Stage 21. |
| deepseek | transcription | person.sav_line2 | model error | not executable (reply invalid) | f8880 p. 2, Line 2 | Omits own SIMPLE deferrals. |
| deepseek | transcription | person.ira_contrib | scope | not executable (reply invalid) | i1040gi p. 98, line 11 | As Stage 21; refusal no longer declared. |
| deepseek | transcription | person.ira_cov | model error | not executable (reply invalid) | i1040gi p. 96 | As Stage 21: drops own SEP/SIMPLE coverage. |
| deepseek | transcription | person.ira_line2 | representation | not executable (reply invalid) | i1040gi p. 97, line 2 | Now the Claude structure; inherits ira_cov. |
| deepseek | transcription | person.ira_line6 | model error | not executable (reply invalid) | i1040gi p. 97, lines 3-6 | AGI line 11a for worksheet line 5: cycle. |
| deepseek | transcription | person.ira_line7 | model error | not executable (reply invalid) | i1040gi pp. 97-98, lines 6-7 | $200 floor at zero, no full-limit threshold, wrong uncovered rule. |
| deepseek | transcription | person.ira_deduction | model error | not executable (reply invalid) | i1040gi p. 98, line 12 | Omits line 10. |
| deepseek | transcription | person.ira_nondeductible | model error | not executable (reply invalid) | i8606 p. 9, Line 1 | Omits line 10. |
| deepseek | transcription | person.ira_files_8606 | scope | not executable (reply invalid) | i8606 p. 2, Who Must File | Now the Claude test. |
| deepseek | transcription | person.ira_8606_line2 | scope | not executable (reply invalid) | i8606 p. 9, Line 2 | Basis for everyone; no adjusted-basis refusal (cited project refusal). |
| deepseek | transcription | person.ira_dist_gate | scope | not executable (reply invalid) | f8606 Part I | Project test plus screened basis condition. |
| deepseek | transcription | person.ira_8606_line14 | scope | not executable (reply invalid) | f8606 Part I, line 14 | Same amounts; placements. |
| deepseek | transcription | person.ira_ssb | model error | not executable (reply invalid) | i1040gi p. 98; amb.2025.ira_ssb_copy | Copies circular deduction. |
| deepseek | transcription | person.ira_se | scope | not executable (reply invalid) | i1040gi p. 98, line 9 | Now valid; same amount; placements. |
| deepseek | transcription | person.edu_kid | model error | not executable (reply invalid) | i8863 p. 7, Line 7 | Drops age bands; no kid_needed gate. |
| deepseek | transcription | person.x_c05 | model error | not executable (reply invalid) | i5329 p. 5, exception 05 | Zero: no medical exception. |
| deepseek | transcription | person.x_two23 | model error | not executable (reply invalid) | p590b p. 28 | Always false. |
| deepseek | transcription | person.x_limited_sum | model error | not executable (reply invalid) | p590b pp. 27-28; i5329 p. 5 | Zero: no limits. |
| deepseek | transcription | person.x_other_exc | model error | not executable (reply invalid) | i5329 p. 5, Line 2 | All exceptions unlimited. |
| deepseek | transcription | person.x_limit_binds | model error | not executable (reply invalid) | i5329 p. 5, Line 4 | Always false. |
| deepseek | transcription | person.x_hsa_excess | model error | not executable (reply invalid) | f5329 Part VII, lines 47-49 | Sums the line 49 tax: wrong quantity, cycle. |
| deepseek | transcription | eligible | representation | not executable (reply invalid) | i1040gi p. 117, Line 11 | Now the Claude test. |
| deepseek | transcription | excess | scope | not executable (reply invalid) | i1040gi p. 117, Line 11 | Gated on eligible; differs only where project refuses credit. |
| deepseek | transcription | credit | scope | not executable (reply invalid) | i1040gi p. 117, Line 11 | Zero where one employer over-withheld; project refuses (Form 843). |
| deepseek | transcription | Step 1 | scope | not executable (reply invalid) | p560 p. 39, Step 1 | As Stage 21. |
| deepseek | transcription | Step 2 | scope | not executable (reply invalid) | p560 p. 39, Step 2 | Now valid; copies se_line13. |
| deepseek | transcription | Step 5 | model error | not executable (reply invalid) | p560 p. 38, Rate Table | Rate to 3 places, table has 6 (0.091 for 0.090909). |
| deepseek | transcription | Step 6 | scope | not executable (reply invalid) | p560 p. 39, Step 6 | Now valid; exact for whole rates; placement. |
| deepseek | transcription | 27 | model error | not executable (reply invalid) | i8863 pp. 2-3 | As Stage 21: no gates; edu_over refusal dropped. |
| deepseek | transcription | 28 | model error | not executable (reply invalid) | i8863 pp. 2-3 | As Stage 21: no gates; edu_over refusal dropped. |
| deepseek | transcription | 29 | model error | not executable (reply invalid) | i8863 pp. 2-3 | As Stage 21: no gates; edu_over refusal dropped. |
| deepseek | transcription | 30 | model error | not executable (reply invalid) | i8863 pp. 2-3 | As Stage 21: no gates; edu_over refusal dropped. |
| deepseek | transcription | 31 | model error | not executable (reply invalid) | i8863 pp. 2-3 | As Stage 21: no gates; edu_over refusal dropped. |
| claude | render | 27 | ambiguity | render MISMATCH | i8863 p. 1; p970 pp. 2, 11 | amb.2025.edu_1098t_date; applied-for ITIN interface gap; new only because the prompt changed. |
| claude | render | 28 | ambiguity | render MISMATCH | i8863 p. 1; p970 pp. 2, 11 | amb.2025.edu_1098t_date; applied-for ITIN interface gap; new only because the prompt changed. |
| claude | render | 29 | ambiguity | render MISMATCH | i8863 p. 1; p970 pp. 2, 11 | amb.2025.edu_1098t_date; applied-for ITIN interface gap; new only because the prompt changed. |
| claude | render | 30 | ambiguity | render MISMATCH | i8863 p. 1; p970 pp. 2, 11 | amb.2025.edu_1098t_date; applied-for ITIN interface gap; new only because the prompt changed. |
| claude | render | 31 | ambiguity | render MISMATCH | i8863 p. 1; p970 pp. 2, 11 | amb.2025.edu_1098t_date; applied-for ITIN interface gap; new only because the prompt changed. |
| deepseek | render | Step 3 | ambiguity | render MISMATCH | p560 p. 39, Step 3 | amb.2025.sep_loss_floor; unchanged. |

Errors introduced by the fixes: one, low severity, found by scrutiny of the reworded questions rather than by a reply: F1
`EXPIRED-ITIN-RENEWAL`, the new `person.tin` sentence counts an expired ITIN whose renewal was only applied for by the due
date, and `household.id_count` reads `person.tin` for the child tax credit's other-spouse test, where
`amb.2025.ctc_spouse_itin_application` chose that an application does not count (p503 p. 3: an expired ITIN "must be renewed
before being used again"); `.transcription/proposed/fixr2/person.findings.md`. Checked without finding: `person.x_other`
(Part IX applies to a shortfall made up later, f5329 p. 3 and i5329 p. 9, so the wider screen is the source's);
`person.edu_1098t` (the cooperation sentence is i8863 p. 1's); `person.edu_inst` (the job-skills exception limited to the
lifetime learning credit, i8863 p. 4).
Reclassified from Stage 21: Claude `person.x_limit_binds` (model error to interface gap; the code S condition is a project
scope decision the id-only interface does not carry).

## Fix round 3 (superseded subject)

Subject after BUG-0256 (2026-10-30): `person.tin` no longer counts an expired ITIN whose renewal was only applied for
("An ITIN that has expired counts only if it has been renewed by then (a renewal only applied for does not count here)");
no person expression changed. Fresh replies of 2026-10-30 (claude-opus-5-5, deepseek-flash); fix-round-2 logs archived in
`.transcription/archive/before-fix-round3-2026-10-30/`. Full ruling text: `.transcription/proposed/fixr3/transcription.person.json`,
`transcription.person.deepseek.json`, `render.person.json`, `render.person.deepseek.json`. Claude triage: `../triage/person.json`,
executable-triage-v2 (1,390 fixtures, 500 generated returns seed 20261026, 2,014 partial records; 4,724 comparisons per line);
every witness was listed by a scratch rerun of `tools/transcription/triage.mjs` with the witness cap lifted, and every
completed-return value difference was checked against its ruling's mechanism. The deepseek-flash reply fails validation on
three declarations (`person.positive_profits`, non-negativity unproven; `person.h_llc31`, aqee has no line31;
`person.h_ira_line4`, `s1.line23` does not resolve), so `../triage/person.deepseek.json` is `invalid`; lines reaching them are
model errors on the declaration and the others are ruled by reading, illustrated by a scratch evaluation with the three
declarations minimally repaired (not a triage record). The class M logs have no open line. Rulings repeated from fix round 2
were re-checked against the new replies; most replies changed.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | person.educator_deduction | representation | 3,056/4,724 agree; 28 project-unknown, 1,640 candidate-unknown | i1040gi p. 93, Line 11 | Unchanged; question order only. |
| claude | transcription | person.hsa_share | interface gap | 4,702/4,724 agree; 16 candidate-refuses, 6 candidate-unknown | i8889 p. 7, Line 6, Steps 2-3 | Spouse-rule filter added; still the f8889.share cycle (id-only interface). |
| claude | transcription | person.tip_reported | scope | 4,719/4,724 agree; 5 project-refuses | i1040gi p. 103, qualified tips | New: qualified rows only; differences are the cited tipjob.mixed refusal. |
| claude | transcription | person.sc_total | scope | 4,723/4,724 agree; 1 project-refuses | i1040sc p. 15, Line 32 | New: sc.line31; at-risk refusal only. |
| claude | transcription | person.se_line6 | scope | 3,204/4,724 agree; 1 project-refuses, 17 candidate-refuses, 1,502 candidate-unknown | i1040sse p. 1, Who Must File | Back on sc.line31: at-risk refusal again; se_screen placement; no value. |
| claude | transcription | person.se_line12 | scope | 3,204/4,724 agree; 1 project-refuses, 17 candidate-refuses, 1,502 candidate-unknown | i1040sse p. 1, Who Must File | Back on sc.line31: at-risk refusal again; placement; no value. |
| claude | transcription | person.se_line13 | scope | 3,204/4,724 agree; 1 project-refuses, 17 candidate-refuses, 1,502 candidate-unknown | f1040sse line 13 | Back on sc.line31: at-risk refusal again; placement; no value. |
| claude | transcription | Step 2 | scope | 3,204/4,724 agree; 1 project-refuses, 17 candidate-refuses, 1,502 candidate-unknown | p560 p. 39, Step 2 | Copies se_line13; as there. |
| claude | transcription | person.eic_se | scope | 3,204/4,724 agree; 1 project-refuses, 17 candidate-refuses, 1,502 candidate-unknown | i1040gi EIC Worksheet B, Parts 1-2 | Back on sc.line31; same amount; placements. |
| claude | transcription | person.dc_earned_b | scope | 3,222/4,724 agree; 1 project-refuses, 17 candidate-refuses, 1,484 candidate-unknown | i2441 p. 5, Line 18 | Back on sc.line31; same sum; placements. |
| claude | transcription | person.dc_earned | model error | 3,128/4,724 agree; 6 project-refuses, 16 candidate-refuses, 1,574 candidate-unknown | i2441 p. 4; amb.2025.dc_line1e_attribution | Line 1e now added (round-2 error fixed) but to both spouses when both have box 10; no sample record. |
| claude | transcription | person.dc_has_box10 | representation | 4,724/4,724 agree; none differ | i2441 p. 5, Line 12 | No difference. |
| claude | transcription | person.s16 | scope | 2,982/4,724 agree; 37 project-refuses, 20 candidate-refuses, 1,685 candidate-unknown | p560 p. 39, after Step 21 | SIMPLE helpers on sc.line31; no value; cited refusals, placements. |
| claude | transcription | person.sav_ineligible | ambiguity | 4,479/4,724 agree; 197 value, 4 project-unknown, 44 candidate-unknown | f8880 p. 2; amb.2025.savers_ineligible_column | Unchanged; values unproducible (sav_claimed without sa.dependent). |
| claude | transcription | person.sav_line2 | scope | 3,197/4,724 agree; 149 value, 15 project-refuses, 16 candidate-refuses, 1 project-unknown, 1,346 candidate-unknown | f8880 p. 2, Line 2; amb.2025.ira_covered | Schedule C gate dropped: all 149 values are plan simple without a Schedule C (unproducible). |
| claude | transcription | person.ira_cov | ambiguity | 4,248/4,724 agree; 421 value, 9 project-unknown, 46 candidate-unknown | i1040gi p. 96; amb.2025.ira_covered | Unchanged; values plan answer without Schedule C, no contribution. |
| claude | transcription | person.ira_line2 | ambiguity | 4,488/4,724 agree; 164 value, 5 candidate-refuses, 6 project-unknown, 61 candidate-unknown | i1040gi p. 97, line 2; amb.2025.ira_covered | Joint-return test restored; 124 completed values all ira_cov plan reading. |
| claude | transcription | person.ira_line6 | representation | 3,424/4,724 agree; 129 value, 42 project-refuses, 11 candidate-refuses, 29 project-unknown, 1,089 candidate-unknown | i1040gi p. 97, line 6 | Inherited from line 2; completed values inside skipped lines. |
| claude | transcription | person.ira_line7 | representation | 4,390/4,724 agree; 6 value, 220 project-refuses, 1 candidate-refuses, 48 project-unknown, 59 candidate-unknown | i1040gi p. 97, line 1 | Round-2 zero branch gone; 6 values on returns with no contribution (printed lines zero). |
| claude | transcription | person.ira_deduction | model error | 2,518/4,724 agree; 11 project-refuses, 231 candidate-refuses, 1,964 candidate-unknown | i1040gi pp. 95, 98 | sav_trad gate dropped: needs coverage answers of 873 non-contributors (completed). |
| claude | transcription | person.ira_nondeductible | model error | 2,518/4,724 agree; 10 project-refuses, 231 candidate-refuses, 1,965 candidate-unknown | i8606 p. 9, Line 1; i1040gi p. 95 | sav_trad gate dropped: unneeded answers. |
| claude | transcription | person.ira_files_8606 | model error | 2,518/4,724 agree; 10 project-refuses, 231 candidate-refuses, 1,965 candidate-unknown | i8606 p. 2; i1040gi p. 95 | sav_trad gate dropped: unneeded answers. |
| claude | transcription | person.ira_8606_line2 | model error | 2,518/4,724 agree; 11 project-refuses, 231 candidate-refuses, 1,964 candidate-unknown | i8606 p. 9, Line 2; i1040gi p. 95 | Filer gate through ira_nondeductible: unneeded answers. |
| claude | transcription | person.ira_dist_gate | model error | 2,770/4,724 agree; 10 project-refuses, 231 candidate-refuses, 1,713 candidate-unknown | f8606 Part I; i1040gi p. 95 | Through ira_nondeductible: unneeded answers. |
| claude | transcription | person.ira_8606_line14 | model error | 2,518/4,724 agree; 12 project-refuses, 231 candidate-refuses, 1,963 candidate-unknown | f8606 Part I, line 14; i1040gi p. 95 | sav_trad gate dropped: unneeded answers. |
| claude | transcription | person.ira_ssb | model error | 2,522/4,724 agree; 10 project-refuses, 231 candidate-refuses, 1,961 candidate-unknown | i1040gi pp. 95, 98; amb.2025.ira_ssb_copy | sav_trad gate dropped: unneeded answers (871 completed). |
| claude | transcription | person.ira_se | scope | 2,984/4,724 agree; 39 project-refuses, 33 candidate-refuses, 1,668 candidate-unknown | i1040gi p. 98, line 9 | Back on sc.line31: at-risk refusal; same amount. |
| claude | transcription | person.edu_kid | model error | 2,881/4,724 agree; 66 value, 97 project-refuses, 1,680 candidate-unknown | i8863 pp. 6-7, Line 7 | Reordered; still no kid_needed gate; values only with kid_needed false. |
| claude | transcription | person.x_c05 | model error | 4,723/4,724 agree; 1 value | i5329 p. 5, exception 05 | Unchanged: no Schedule A line 4 limit (stage21.blind.e6). |
| claude | transcription | person.x_limited_sum | model error | 4,718/4,724 agree; 5 value, 1 candidate-refuses | i5329 p. 5, Line 2 | Limits now inside; 05 limit never applied (e6); interface-gap kind gone. |
| claude | transcription | person.x_other_exc | model error | 4,719/4,724 agree; 5 value | i5329 p. 5, exception 05 | Unchanged: 05 unlimited (e6). |
| claude | transcription | person.x_limit_binds | interface gap | 4,718/4,724 agree; 4 value, 1 project-refuses, 1 candidate-refuses | i5329 p. 5, Line 4; amb.2025.f5329_simple_limits | Unchanged; no code S condition (id-only interface). |
| claude | transcription | wages | representation | 4,724/4,724 agree; none differ | i1040gi p. 117; iw2w3 p. 18 | New: box 3 + box 7 = w2.wages. |
| claude | transcription | eligible | representation | 4,716/4,724 agree; 7 value, 1 project-unknown | i1040gi p. 117, Line 11 | Unchanged; values only where project refuses person.credit. |
| claude | transcription | Step 1 | scope | 3,187/4,724 agree; 23 project-refuses, 1 candidate-refuses, 1,513 project-unknown | p560 p. 39, Step 1 | New: no se_screened refusal (cited); project helper unknown where unreached. |
| claude | transcription | Step 6 | representation | 4,724/4,724 agree; none differ | p560 p. 39, Step 6 | No difference. |
| claude | transcription | 27 | model error | 2,381/4,724 agree; 2,343 candidate-unknown | i8863 pp. 2-3; p970 p. 11 | sav_claimed dropped; still no itin_applied or f8863.paid (unneeded answers). |
| claude | transcription | 28 | model error | 2,381/4,724 agree; 2,343 candidate-unknown | i8863 pp. 2-3; p970 p. 11 | sav_claimed dropped; still no itin_applied or f8863.paid (unneeded answers). |
| claude | transcription | 29 | model error | 2,381/4,724 agree; 2,343 candidate-unknown | i8863 pp. 2-3; p970 p. 11 | sav_claimed dropped; still no itin_applied or f8863.paid (unneeded answers). |
| claude | transcription | 30 | model error | 2,381/4,724 agree; 2,343 candidate-unknown | i8863 pp. 2-3; p970 p. 11 | sav_claimed dropped; still no itin_applied or f8863.paid (unneeded answers). |
| claude | transcription | 31 | model error | 2,380/4,724 agree; 1 candidate-refuses, 2,343 candidate-unknown | i8863 pp. 2-3; p970 p. 11 | sav_claimed dropped; still no itin_applied or f8863.paid; edu_over refusal as project. |
| deepseek | transcription | person.educator_deduction | representation | not executable (reply invalid) | i1040gi p. 93, Line 11 | Claude formula; question order only. |
| deepseek | transcription | person.hsa_agreed | representation | not executable (reply invalid) | i8889 p. 7, Line 6, Step 2 | As fix round 2. |
| deepseek | transcription | person.hsa_step1 | representation | not executable (reply invalid) | i8889 p. 7, Line 6, Step 2 | As fix round 2; non-split values. |
| deepseek | transcription | person.hsa_share | interface gap | not executable (reply invalid) | i8889 p. 7, Line 6, Step 3 | As fix round 2: f8889.share cycle. |
| deepseek | transcription | person.tip_employers | scope | not executable (reply invalid) | i1040gi p. 103 | New: qualified rows only; cited tipjob.mixed refusal. |
| deepseek | transcription | person.tip_total | scope | not executable (reply invalid) | i1040gi p. 103 | New: qualified rows only; cited refusal. |
| deepseek | transcription | person.tip_reported | scope | not executable (reply invalid) | i1040gi p. 103 | New: qualified rows only; cited refusal. |
| deepseek | transcription | person.ot_total | model error | not executable (reply invalid) | i1040gi p. 106, Schedule 1-A | New: otjob.figured without the FLSA test. |
| deepseek | transcription | person.plan_amount_a | representation | not executable (reply invalid) | i1040gi p. 28 | Same sum. |
| deepseek | transcription | person.plan_taxable | representation | not executable (reply invalid) | i1040gi p. 28 | Now the project expression. |
| deepseek | transcription | person.plan_rollovers | representation | not executable (reply invalid) | i1040gi pp. 28-29 | has_rollover is the project condition. |
| deepseek | transcription | person.sav_dist | model error | not executable (reply invalid) | f8880 p. 2, Line 4 | Prior-year questions instead of 2025 Forms 1099-R. |
| deepseek | transcription | person.s179_nonlisted | interface gap | not executable (reply invalid) | i4562 p. 5, Line 6 | Cost, not elected amount; p. 5 and form face not given. |
| deepseek | transcription | person.s179_listed | interface gap | not executable (reply invalid) | i4562 p. 5, Line 7 | Vehicle cost, not line 29; p. 5 not given. |
| deepseek | transcription | person.income179 | model error | not executable (reply invalid) | i4562 p. 5, Line 11 | sc.line31 after section 179: cycle. |
| deepseek | transcription | person.se_line6 | scope | not executable (reply invalid) | f1040sse lines 4a-6 | Correct computation; no se_screen/rrta refusal (cited project refusals); inherited 179 cycle. |
| deepseek | transcription | person.se_line12 | scope | not executable (reply invalid) | f1040sse lines 9-12 | As se_line6. |
| deepseek | transcription | person.se_line13 | scope | not executable (reply invalid) | f1040sse line 13 | As se_line6. |
| deepseek | transcription | Step 2 | scope | not executable (reply invalid) | p560 p. 39, Step 2 | Copies se_line13. |
| deepseek | transcription | person.s16 | scope | not executable (reply invalid) | p560 pp. 14-17, 39 | As fix round 2; plan without Schedule C unproducible. |
| deepseek | transcription | person.eic_se | model error | not executable (reply invalid) | i1040gi EIC Worksheet B, line 1a | Schedule SE line 6 for line 3. |
| deepseek | transcription | person.sc_1a | model error | not executable (reply invalid) | i1040gi p. 104 | statutory, not tips_ot. |
| deepseek | transcription | person.dc_has_box10 | representation | not executable (reply invalid) | i2441 p. 5, Line 12 | Same test. |
| deepseek | transcription | person.dc_earned | model error | not executable (reply invalid) | i2441 p. 4 | No line 1e; SE line 6 for line 3; loss floored. |
| deepseek | transcription | person.dc_earned_b | model error | not executable (reply invalid) | i2441 p. 5, Line 18 | Subtracts all box 10 benefits from box 1. |
| deepseek | transcription | person.sav_ineligible | ambiguity | not executable (reply invalid) | f8880 p. 2; amb.2025.savers_ineligible_column | Claude expression; unproducible values. |
| deepseek | transcription | person.sav_line1 | scope | not executable (reply invalid) | f8880 line 1 | As fix round 2. |
| deepseek | transcription | person.sav_line2 | model error | not executable (reply invalid) | f8880 p. 2, Line 2 | Omits own SIMPLE deferrals. |
| deepseek | transcription | person.ira_contrib | scope | not executable (reply invalid) | i1040gi p. 98, line 11 | As fix round 2. |
| deepseek | transcription | person.ira_cov | model error | not executable (reply invalid) | i1040gi p. 96 | Drops own SEP/SIMPLE coverage. |
| deepseek | transcription | person.ira_line2 | representation | not executable (reply invalid) | i1040gi p. 97, line 2 | As fix round 2; values inside skipped lines. |
| deepseek | transcription | person.ira_8606_line2 | scope | not executable (reply invalid) | i8606 p. 9, Line 2 | As fix round 2. |
| deepseek | transcription | person.ira_dist_gate | model error | not executable (reply invalid) | f8606 Part I | Distribution with basis only; misses nondeductible-contribution case. |
| deepseek | transcription | person.ira_se | model error | not executable (reply invalid) | i1040gi p. 98, line 9 | Schedule SE line 6 for net profit. |
| deepseek | transcription | person.edu_kid | model error | not executable (reply invalid) | i8863 p. 7, Line 7 | Redefined as an AOC-student test. |
| deepseek | transcription | person.x_l2_all | model error | not executable (reply invalid) | i5329 p. 5, Line 2 | Needs x_prior09 and x_births of everyone. |
| deepseek | transcription | person.x_tax | model error | not executable (reply invalid) | f1040s2 line 8; f5329 line 49 | Omits line 49 (HSA excess tax). |
| deepseek | transcription | person.x_c05 | model error | not executable (reply invalid) | i5329 p. 5, exception 05 | Unlimited exception 05. |
| deepseek | transcription | person.x_two23 | model error | not executable (reply invalid) | p590b p. 28 | Tests 22 and 23, not two 23s. |
| deepseek | transcription | person.x_limited_sum | model error | not executable (reply invalid) | i5329 p. 5; p590b pp. 27-28 | 05 unlimited; unneeded answers. |
| deepseek | transcription | person.x_limit_binds | interface gap | not executable (reply invalid) | i5329 p. 5, Line 4 | Claude reading: no code S condition. |
| deepseek | transcription | over | model error | not executable (reply invalid) | i1040gi p. 117, Line 11 | Redefined as wages over the base. |
| deepseek | transcription | eligible | representation | not executable (reply invalid) | i1040gi p. 117, Line 11 | Claude test as a whole. |
| deepseek | transcription | Step 1 | scope | not executable (reply invalid) | p560 p. 39, Step 1 | As fix round 2; cited se_screened refusal. |
| deepseek | transcription | Step 5 | model error | not executable (reply invalid) | p560 p. 38, Rate Table | Rate to 9 places (table 6): a cent. |
| deepseek | transcription | Step 6 | representation | not executable (reply invalid) | p560 p. 39, Step 6 | Exact for whole rates. |
| deepseek | transcription | Step 21 | scope | not executable (reply invalid) | p560 p. 39, Steps 8-21 | Extra half-of-step-3 term never binds. |
| deepseek | transcription | 27 | model error | not executable (reply invalid) | i8863 pp. 2-3; p970 p. 11 | Gate on redefined edu_kid: no itin_applied, filer TIN or f8863.paid. |
| deepseek | transcription | 28 | model error | not executable (reply invalid) | i8863 pp. 2-3; p970 p. 11 | Gate on redefined edu_kid: no itin_applied, filer TIN or f8863.paid. |
| deepseek | transcription | 29 | model error | not executable (reply invalid) | i8863 pp. 2-3; p970 p. 11 | Gate on redefined edu_kid: no itin_applied, filer TIN or f8863.paid. |
| deepseek | transcription | 30 | model error | not executable (reply invalid) | i8863 pp. 2-3; p970 p. 11 | Gate on redefined edu_kid: no itin_applied, filer TIN or f8863.paid. |
| deepseek | transcription | 31 | model error | not executable (reply invalid) | i8863 pp. 2-3 | Declaration error via h_llc31 (aqee has no line31). |
| deepseek | transcription | person.positive_profits | model error | not executable (reply invalid) | f7206 line 5 | Declaration error: non-negativity unproven. |
| deepseek | transcription | person.ira_line6 | model error | not executable (reply invalid) | i1040gi p. 97, lines 3-6 | Declaration error via h_ira_line4 (s1.line23). |
| deepseek | transcription | person.ira_line7 | model error | not executable (reply invalid) | i1040gi pp. 97-98 | Declaration error; full limit where source says STOP. |
| deepseek | transcription | person.ira_deduction | model error | not executable (reply invalid) | i1040gi p. 98, line 12 | Declaration error via h_ira_line4. |
| deepseek | transcription | person.ira_nondeductible | model error | not executable (reply invalid) | i8606 p. 9, Line 1 | Declaration error; omits line 10. |
| deepseek | transcription | person.ira_files_8606 | model error | not executable (reply invalid) | i8606 p. 2 | Declaration error via h_ira_line4. |
| deepseek | transcription | person.ira_8606_line14 | model error | not executable (reply invalid) | f8606 Part I, line 14 | Declaration error via h_ira_line4. |
| deepseek | transcription | person.ira_ssb | model error | not executable (reply invalid) | i1040gi p. 98; amb.2025.ira_ssb_copy | Declaration error; still circular through line 9. |
| claude | render | 27 | ambiguity | render MISMATCH | i8863 p. 1; p970 pp. 2, 11 | amb.2025.edu_1098t_date; applied-for ITIN interface gap; unchanged objection. |
| claude | render | 28 | ambiguity | render MISMATCH | i8863 p. 1; p970 pp. 2, 11 | amb.2025.edu_1098t_date; applied-for ITIN interface gap; unchanged objection. |
| claude | render | 29 | ambiguity | render MISMATCH | i8863 p. 1; p970 pp. 2, 11 | amb.2025.edu_1098t_date; applied-for ITIN interface gap; unchanged objection. |
| claude | render | 30 | ambiguity | render MISMATCH | i8863 p. 1; p970 pp. 2, 11 | amb.2025.edu_1098t_date; applied-for ITIN interface gap; unchanged objection. |
| claude | render | 31 | ambiguity | render MISMATCH | i8863 p. 1; p970 pp. 2, 11 | amb.2025.edu_1098t_date; applied-for ITIN interface gap; unchanged objection. |
| claude | render | 23 | ambiguity | render MISMATCH | i8863 p. 1; p970 pp. 2, 11 | New: objects only to the gate (date, applied-for ITIN), as at 27-31. |
| deepseek | render | Step 3 | ambiguity | render MISMATCH | p560 p. 39, Step 3 | amb.2025.sep_loss_floor; unchanged. |

Errors introduced by the fixes: none of medium or higher severity. BUG-0256 removes fix round 2's F1 (the pending renewal no
longer satisfies the child tax credit's other-spouse test); low L1 for T-092: `person.itin_applied` still does not say whether
a pending renewal is an application, so a filer sent away by the new "does not count here" may answer No and lose the credit
for other dependents (stage13.odc_spouse_no_tin witness: `f1040.line19` $0.00 against $500.00);
`.transcription/proposed/fixr3/person.findings.md`.
Reclassified from fix round 2 (same project line, changed reply): Claude `person.ira_deduction`, `person.ira_nondeductible`,
`person.ira_files_8606`, `person.ira_8606_line2`, `person.ira_dist_gate`, `person.ira_8606_line14`, `person.ira_ssb` (scope to
model error: the sav_trad gate was dropped, so coverage answers are needed of non-contributors); Claude `person.ira_line7`
(model error to representation: the zero branch is gone); deepseek `person.s179_nonlisted` (model error to interface gap),
`person.eic_se`, `person.ira_se`, `person.ira_dist_gate` (scope to model error), `person.x_limit_binds` (model error to interface
gap, the Claude reading), `person.ira_files_8606`, `person.ira_8606_line14` (scope to model error, declaration closure).
Engine change in progress (spec 4.7.5): no witness examined for these rulings looks affected (none was seen where an unknown
traced to an unanswered refusal gate let a count's lower bound decide a test); stage21.f1.lower_bound_still_decides (Claude `person.ira_line7`) is decided by a lower bound with an unanswered input,
which the change should leave as it is.

## Fix round 4

Subject after BUG-0259 (2026-10-30): `person.itin_applied` now counts an application to renew an expired ITIN ("If you have
neither (or your ITIN has expired and was not renewed), have you applied for an ITIN, or for the renewal of your expired
ITIN, on or before the due date of your 2025 return (including extensions)?"); no person expression changed. Fresh replies
of 2026-10-30 (claude-opus-5-5, deepseek-flash). Full ruling text: `.transcription/proposed/fixr4/transcription.person.json`,
`transcription.person.deepseek.json`, `render.person.json`, `render.person.deepseek.json`. Claude triage: `../triage/person.json`,
executable-triage-v2 (1,390 fixtures, 500 generated returns seed 20261026, 2,014 partial records; 4,724 comparisons per line);
every witness was listed by a scratch rerun of `tools/transcription/triage.mjs` with the witness cap lifted (counts identical
to the record), and every completed-return value difference was checked against its ruling's mechanism, with printed
amounts read in both graphs where a helper differs. The deepseek-flash reply fails validation on 55 declarations (53
collection sums naming the field without its collection's prefix, `h_ss_room` naming the parameter `ss.base` as a line,
`h_se_4a_pos` non-negativity unproven), so `../triage/person.deepseek.json` is `invalid`; lines reaching them are model errors
on the declaration (merits noted from a scratch evaluation with the prefixes restored, not a triage record) and the 19 lines
outside that closure are ruled by reading. The class M logs have no open line. Rulings repeated from fix round 3 were
re-checked; 8 Claude replies are unchanged, most others changed.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | person.educator_deduction | representation | 3,056/4,724 agree; 28 project-unknown, 1,640 candidate-unknown | i1040gi p. 93, Line 11 | Unchanged; question order only. |
| claude | transcription | person.hsa_share | interface gap | 4,702/4,724 agree; 16 candidate-refuses, 6 candidate-unknown | i8889 p. 7, Line 6, Steps 2-3 | Unchanged; f8889.share cycle (id-only interface). |
| claude | transcription | person.dc_has_box10 | representation | 4,724/4,724 agree; none differ | i2441 p. 5, Line 12 | Unchanged; no difference. |
| claude | transcription | person.sav_ineligible | ambiguity | 4,479/4,724 agree; 197 value, 4 project-unknown, 44 candidate-unknown | f8880 p. 2; amb.2025.savers_ineligible_column | Unchanged; values unproducible. |
| claude | transcription | person.sav_line2 | scope | 3,197/4,724 agree; 149 value, 15 project-refuses, 16 candidate-refuses, 1 project-unknown, 1,346 candidate-unknown | f8880 p. 2, Line 2; amb.2025.ira_covered | Unchanged; values plan simple without Schedule C. |
| claude | transcription | person.ira_cov | ambiguity | 4,248/4,724 agree; 421 value, 9 project-unknown, 46 candidate-unknown | i1040gi p. 96; amb.2025.ira_covered | Unchanged; plan answer without Schedule C, no contribution. |
| claude | transcription | eligible | representation | 4,716/4,724 agree; 7 value, 1 project-unknown | i1040gi p. 117, Line 11 | Unchanged; values only where project refuses person.credit. |
| claude | transcription | Step 6 | representation | 4,724/4,724 agree; none differ | p560 p. 39, Step 6 | Unchanged; no difference. |
| claude | transcription | person.se_line6 | scope | 3,176/4,724 agree; 25 candidate-refuses, 1,523 candidate-unknown | i1040sse p. 1, Who Must File | Back on sc.result: at-risk kind gone; se_screen/rrta placement; no value. |
| claude | transcription | person.se_line12 | scope | 3,176/4,724 agree; 25 candidate-refuses, 1,523 candidate-unknown | i1040sse p. 1, Who Must File | As se_line6. |
| claude | transcription | person.se_line13 | scope | 3,176/4,724 agree; 25 candidate-refuses, 1,523 candidate-unknown | i1040sse p. 1, Who Must File | As se_line6. |
| claude | transcription | Step 2 | scope | 3,176/4,724 agree; 25 candidate-refuses, 1,523 candidate-unknown | p560 p. 39, Step 2 | Copies se_line13; as there. |
| claude | transcription | person.eic_se | scope | 3,176/4,724 agree; 25 candidate-refuses, 1,523 candidate-unknown | i1040gi EIC Worksheet B, Parts 1-2 | Back on sc.result; same amount; placements. |
| claude | transcription | person.dc_earned_b | scope | 3,194/4,724 agree; 25 candidate-refuses, 1,505 candidate-unknown | i2441 p. 5, Line 18 | Back on sc.result; same sum; placements. |
| claude | transcription | person.dc_earned | model error | 3,101/4,724 agree; 5 project-refuses, 23 candidate-refuses, 1,595 candidate-unknown | i2441 p. 4; amb.2025.dc_line1e_attribution | Line 1e (now f1040.line1e) still added to both spouses with box 10. |
| claude | transcription | person.s16 | scope | 3,153/4,724 agree; 37 project-refuses, 8 candidate-refuses, 1,526 candidate-unknown | p560 p. 39, after Step 21 | Back on sc.result; no value; cited refusals, placements. |
| claude | transcription | person.ira_se | scope | 3,098/4,724 agree; 38 project-refuses, 28 candidate-refuses, 1,560 candidate-unknown | i1040gi p. 98, line 9 | Back on sc.result; same amount; placements. |
| claude | transcription | person.ira_line2 | ambiguity | 4,535/4,724 agree; 164 value, 6 project-unknown, 19 candidate-unknown | i1040gi p. 97, line 2; amb.2025.ira_covered | Unchanged; values inherit ira_cov, printed lines zero. |
| claude | transcription | person.ira_line6 | representation | 3,432/4,724 agree; 128 value, 41 project-refuses, 10 candidate-refuses, 29 project-unknown, 1,084 candidate-unknown | i1040gi p. 97, line 6 | Unchanged; values inside skipped lines (one more fixture). |
| claude | transcription | person.ira_line7 | representation | 4,443/4,724 agree; 68 value, 35 project-refuses, 41 candidate-refuses, 8 project-unknown, 129 candidate-unknown | i1040gi pp. 97-98, lines 1, 7 | Branches on ira.anyone_covered; 31 completed values with printed lines zero. |
| claude | transcription | person.ira_deduction | model error | 2,450/4,724 agree; 11 project-refuses, 270 candidate-refuses, 1,993 candidate-unknown | i1040gi pp. 95, 98 | sav_trad gate inside a smaller-of: still needs answers of 875 non-contributors. |
| claude | transcription | person.ira_nondeductible | model error | 2,450/4,724 agree; 10 project-refuses, 270 candidate-refuses, 1,994 candidate-unknown | i8606 p. 9, Line 1; i1040gi p. 95 | As ira_deduction. |
| claude | transcription | person.ira_files_8606 | model error | 2,450/4,724 agree; 10 project-refuses, 270 candidate-refuses, 1,994 candidate-unknown | i8606 p. 2; i1040gi p. 95 | As ira_deduction. |
| claude | transcription | person.ira_dist_gate | model error | 2,743/4,724 agree; 10 project-refuses, 270 candidate-refuses, 1,701 candidate-unknown | f8606 Part I; i1040gi p. 95 | Through ira_nondeductible: unneeded answers (805). |
| claude | transcription | person.ira_8606_line14 | model error | 2,395/4,724 agree; 11 project-refuses, 270 candidate-refuses, 2,048 candidate-unknown | f8606 Part I, line 14; i1040gi p. 95 | As ira_deduction. |
| claude | transcription | person.ira_8606_line2 | model error | 2,907/4,724 agree; 12 project-refuses, 30 project-unknown, 1,775 candidate-unknown | i8606 p. 9, Line 2 | Now copies ira_basis for everyone: unneeded answers (829). |
| claude | transcription | person.ira_ssb | model error | 2,534/4,724 agree; 10 project-refuses, 227 candidate-refuses, 1,953 candidate-unknown | i1040gi pp. 95, 98; amb.2025.ira_ssb_copy | sav_trad gate inside a smaller-of: unneeded answers (860). |
| claude | transcription | person.edu_kid | model error | 2,032/4,724 agree; 202 value, 97 project-refuses, 2,393 candidate-unknown | i8863 pp. 6-7, Line 7 | MFJ condition dropped; no kid_needed gate; 110 values reach no amount. |
| claude | transcription | person.x_limited_sum | model error | 2,037/4,724 agree; 1 candidate-refuses, 2,686 candidate-unknown | i5329 p. 5, Line 2; p590b p. 27 | 05 limit now applied; x_prior09 asked of everyone. |
| claude | transcription | person.x_l2_all | model error | 2,036/4,724 agree; 2 value, 1 candidate-refuses, 2,685 candidate-unknown | i5329 p. 5, Line 2; p590b p. 27 | New: after-limit amount under the pre-limit id; x_prior09 asked of everyone. |
| claude | transcription | person.x_other_exc | representation | 4,724/4,724 agree; none differ | i5329 p. 5, Line 2 | Unlimited exceptions summed directly; no difference. |
| claude | transcription | person.x_limit_binds | interface gap | 2,035/4,724 agree; 2 value, 1 project-refuses, 2 candidate-refuses, 2,684 candidate-unknown | i5329 p. 5, Line 4; amb.2025.f5329_simple_limits | Form only; no code S condition (id-only interface). |
| claude | transcription | person.x_must | model error | 4,367/4,724 agree; 297 value, 57 project-refuses, 1 candidate-refuses, 2 project-unknown | i5329 p. 1, Who Must File; f1040s2 line 8 | New: omits HSA excess as a reason; Schedule 2 line 8 box checked (119 completed). |
| claude | transcription | person.x_two23 | representation | 4,724/4,724 agree; none differ | p590b p. 28 | New: same test (>1 vs >=2). |
| claude | transcription | over | representation | 4,724/4,724 agree; none differ | i1040gi p. 117, Line 11 | New: same test (>0 vs >=1). |
| claude | transcription | 27 | model error | 2,372/4,724 agree; 2,352 candidate-unknown | i8863 pp. 2-3; p970 p. 11 | itin_applied now tested (round-3 TIN kind gone); still no f8863.paid (unneeded answers). |
| claude | transcription | 28 | model error | 2,372/4,724 agree; 2,352 candidate-unknown | i8863 pp. 2-3; p970 p. 11 | itin_applied now tested (round-3 TIN kind gone); still no f8863.paid (unneeded answers). |
| claude | transcription | 29 | model error | 2,372/4,724 agree; 2,352 candidate-unknown | i8863 pp. 2-3; p970 p. 11 | itin_applied now tested (round-3 TIN kind gone); still no f8863.paid (unneeded answers). |
| claude | transcription | 30 | model error | 2,372/4,724 agree; 2,352 candidate-unknown | i8863 pp. 2-3; p970 p. 11 | itin_applied now tested (round-3 TIN kind gone); still no f8863.paid (unneeded answers). |
| claude | transcription | 31 | model error | 2,371/4,724 agree; 1 candidate-refuses, 2,352 candidate-unknown | i8863 pp. 2-3; p970 p. 11 | As 27; edu_over refusal as project. |
| deepseek | transcription | person.educator_deduction | representation | not executable (reply invalid) | i1040gi p. 93, Line 11 | Unchanged; Claude formula. |
| deepseek | transcription | person.hsa_forms | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); otherwise the project expression. |
| deepseek | transcription | person.hsa_split | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); otherwise the project expression. |
| deepseek | transcription | person.hsa_agreed | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); as fix round 3 (refused-return values). |
| deepseek | transcription | person.hsa_step1 | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); as fix round 3 (non-split values, no printed amount). |
| deepseek | transcription | person.hsa_share | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); reply graph circular. |
| deepseek | transcription | person.hsa_deduction | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); also wrong on the merits. |
| deepseek | transcription | person.hsa_taxable | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); otherwise the project expression. |
| deepseek | transcription | person.hsa_addtax | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); otherwise the project expression. |
| deepseek | transcription | person.tip_employers | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); otherwise the project expression. |
| deepseek | transcription | person.tip_total | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); otherwise the project expression. |
| deepseek | transcription | person.tip_reported | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); otherwise the project expression. |
| deepseek | transcription | person.ot_employers | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); otherwise the project expression. |
| deepseek | transcription | person.ot_total | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); otherwise the project expression. |
| deepseek | transcription | person.box1 | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); otherwise the project expression. |
| deepseek | transcription | person.box2 | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); otherwise the project expression. |
| deepseek | transcription | person.ira_amount_a | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); also wrong on the merits. |
| deepseek | transcription | person.ira_taxable | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); also wrong on the merits. |
| deepseek | transcription | person.ira_rollovers | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); otherwise the project expression. |
| deepseek | transcription | person.plan_amount_a | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); otherwise the project expression. |
| deepseek | transcription | person.plan_taxable | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); also wrong on the merits. |
| deepseek | transcription | person.plan_rollovers | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); otherwise the project expression. |
| deepseek | transcription | person.sav_dist | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); otherwise the project expression. |
| deepseek | transcription | person.medicare5 | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); cited rrta refusal only. |
| deepseek | transcription | person.medicare6 | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); cited rrta refusal only. |
| deepseek | transcription | person.sc_count | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); otherwise the project expression. |
| deepseek | transcription | person.ho_count | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); otherwise the project expression. |
| deepseek | transcription | person.mq_q4 | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); otherwise the project expression. |
| deepseek | transcription | person.mq_total | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); otherwise the project expression. |
| deepseek | transcription | person.cost179 | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); otherwise the project expression. |
| deepseek | transcription | person.s179_nonlisted | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); reply graph circular. |
| deepseek | transcription | person.s179_listed | interface gap | not executable (reply invalid) | i4562 p. 5, Line 7 | Now zero; sc.f29 id-only, p. 5 not given. |
| deepseek | transcription | person.income179 | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); reply graph circular. |
| deepseek | transcription | person.sc_total | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); reply graph circular. |
| deepseek | transcription | person.se_line6 | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error via h_se_4a_pos; reply graph circular. |
| deepseek | transcription | person.se_line12 | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error via h_se_4a_pos; reply graph circular. |
| deepseek | transcription | person.se_line13 | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error via h_se_4a_pos; reply graph circular. |
| deepseek | transcription | person.s16 | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error via h_se_4a_pos; also wrong on the merits. |
| deepseek | transcription | person.positive_profits | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); reply graph circular. |
| deepseek | transcription | person.sehi | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); reply graph circular. |
| deepseek | transcription | person.qbi | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); reply graph circular. |
| deepseek | transcription | person.eic_se | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error via h_se_4a_pos; reply graph circular. |
| deepseek | transcription | person.sc_1a | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error via person.sc_count; also wrong on the merits. |
| deepseek | transcription | person.dc_benefits | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); otherwise the project expression. |
| deepseek | transcription | person.dc_has_box10 | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error via person.dc_benefits; same test. |
| deepseek | transcription | person.dc_earned | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error via person.box1; also wrong on the merits. |
| deepseek | transcription | person.dc_earned_b | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error via person.box1; also wrong on the merits. |
| deepseek | transcription | person.sav_ineligible | ambiguity | not executable (reply invalid) | f8880 p. 2; amb.2025.savers_ineligible_column | Form only; unproducible values. |
| deepseek | transcription | person.sav_line1 | scope | not executable (reply invalid) | f8880 line 1 | Unchanged. |
| deepseek | transcription | person.sav_line2 | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error via h_sav_deferral; also wrong on the merits. |
| deepseek | transcription | person.ira_contrib | scope | not executable (reply invalid) | i1040gi p. 98, line 11 | Unchanged. |
| deepseek | transcription | person.ira_cov | model error | not executable (reply invalid) | i1040gi p. 96 | Unchanged: drops own SEP/SIMPLE coverage. |
| deepseek | transcription | person.ira_line2 | representation | not executable (reply invalid) | i1040gi p. 97, line 2 | Unchanged. |
| deepseek | transcription | person.ira_line6 | model error | not executable (reply invalid) | i1040gi p. 97, lines 3-6 | Line 5 copies AGI: cycle through the IRA deduction. |
| deepseek | transcription | person.ira_line7 | model error | not executable (reply invalid) | i1040gi p. 98, line 7 | 70% and $200 for everyone; inherits the cycle. |
| deepseek | transcription | person.ira_deduction | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error via person.box1; reply graph circular. |
| deepseek | transcription | person.ira_nondeductible | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error via person.box1; reply graph circular. |
| deepseek | transcription | person.ira_files_8606 | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error via person.box1; reply graph circular. |
| deepseek | transcription | person.ira_8606_line2 | scope | not executable (reply invalid) | i8606 p. 9, Line 2 | Unchanged. |
| deepseek | transcription | person.ira_dist_gate | model error | not executable (reply invalid) | f8606 Part I; p590a p. 15 | Any distribution; ira_dist asked of everyone. |
| deepseek | transcription | person.ira_8606_line14 | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); reply graph circular. |
| deepseek | transcription | person.ira_ssb | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error via person.box1; reply graph circular. |
| deepseek | transcription | person.ira_se | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error via person.box1; reply graph circular. |
| deepseek | transcription | person.edu_kid | model error | not executable (reply invalid) | i8863 p. 7, Line 7 | Redefined as an AOC-student test. |
| deepseek | transcription | person.x_l1 | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); otherwise the project expression. |
| deepseek | transcription | person.x_l2_all | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); otherwise the project expression. |
| deepseek | transcription | person.x_l1_s | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); otherwise the project expression. |
| deepseek | transcription | person.x_l2_s | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); otherwise the project expression. |
| deepseek | transcription | person.x_tax | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); reply graph circular. |
| deepseek | transcription | person.x_must | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); reply graph circular. |
| deepseek | transcription | person.x_c05 | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); also wrong on the merits. |
| deepseek | transcription | person.x_two23 | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error via h_e23_count; otherwise the project expression. |
| deepseek | transcription | person.x_limited_sum | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); also wrong on the merits. |
| deepseek | transcription | person.x_other_exc | model error | not executable (reply invalid) | i5329 p. 5, Line 2 | Zero: unlimited exceptions never excluded. |
| deepseek | transcription | person.x_limit_binds | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error via person.x_limited_sum; also wrong on the merits. |
| deepseek | transcription | person.x_hsa_excess | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); reply graph circular. |
| deepseek | transcription | employers | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); otherwise the project expression. |
| deepseek | transcription | overcount | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); otherwise the project expression. |
| deepseek | transcription | over | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error via person.overcount; otherwise the project expression. |
| deepseek | transcription | wages | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); otherwise the project expression. |
| deepseek | transcription | withheld | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error (unprefixed collection field); otherwise the project expression. |
| deepseek | transcription | eligible | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error via person.employers; Claude test as a whole. |
| deepseek | transcription | excess | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error via person.employers; differs on refused returns only. |
| deepseek | transcription | credit | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error via person.employers; cited refusals only. |
| deepseek | transcription | Step 1 | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error via person.sc_total; reply graph circular. |
| deepseek | transcription | Step 2 | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error via h_se_4a_pos; reply graph circular. |
| deepseek | transcription | Step 3 | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error via h_se_4a_pos; reply graph circular. |
| deepseek | transcription | Step 5 | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error via h_se_4a_pos; reply graph circular. |
| deepseek | transcription | Step 6 | model error | not executable (reply invalid) | p560 p. 39, Step 6 | $350,000 itself ("not expressible"). |
| deepseek | transcription | Step 7 | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error via h_se_4a_pos; reply graph circular. |
| deepseek | transcription | Step 21 | model error | not executable (reply invalid) | validation record (triage/person.deepseek.json) | Declaration error via h_se_4a_pos; reply graph circular. |
| deepseek | transcription | 27 | model error | not executable (reply invalid) | i8863 pp. 2-3 | Gate on redefined edu_kid: no TIN test, no f8863.paid. |
| deepseek | transcription | 28 | model error | not executable (reply invalid) | i8863 pp. 2-3 | As 27. |
| deepseek | transcription | 29 | model error | not executable (reply invalid) | i8863 pp. 2-3 | As 27. |
| deepseek | transcription | 30 | model error | not executable (reply invalid) | i8863 pp. 2-3 | As 27. |
| deepseek | transcription | 31 | model error | not executable (reply invalid) | i8863 pp. 2-3 | No eligibility gate; shown for AOC students; amounts differ. |
| claude | render | 27 | ambiguity | render MISMATCH | i8863 p. 1; p970 pp. 2, 11 | amb.2025.edu_1098t_date; applied-for ITIN interface gap; renewal wording not objected to. |
| claude | render | 28 | ambiguity | render MISMATCH | i8863 p. 1; p970 pp. 2, 11 | amb.2025.edu_1098t_date; applied-for ITIN interface gap; renewal wording not objected to. |
| claude | render | 29 | ambiguity | render MISMATCH | i8863 p. 1; p970 pp. 2, 11 | amb.2025.edu_1098t_date; applied-for ITIN interface gap; renewal wording not objected to. |
| claude | render | 30 | ambiguity | render MISMATCH | i8863 p. 1; p970 pp. 2, 11 | amb.2025.edu_1098t_date; applied-for ITIN interface gap; renewal wording not objected to. |
| claude | render | 31 | ambiguity | render MISMATCH | i8863 p. 1; p970 pp. 2, 11 | amb.2025.edu_1098t_date; applied-for ITIN interface gap; renewal wording not objected to. |
| deepseek | render | Step 3 | ambiguity | render MISMATCH | p560 p. 39, Step 3 | amb.2025.sep_loss_floor; unchanged. |
| deepseek | render | (screen) (person.ira_excess) | finding (low) | render MISMATCH | p590a p. 35 | "including extensions" omitted: over-refusal only; L1 for T-092. |

Errors introduced by the fixes: none. BUG-0259 is not wider than its sources for its two readers (the credit for other
dependents, i1040gi p. 19, Step 5; the education credits, p970 p. 11), does not reach the child tax credit's other-spouse
test (`household.id_count` reads `person.tin` only), and both replies read the answer where the project does. Low for
T-092: L1 `person.ira_excess` omits "including extensions" from the withdrawal deadline (over-refusal only; raised by the
deepseek render reviewer); L2 the `person.itin_applied` label and help still describe the old scope (no answer changes);
`.transcription/proposed/fixr4/person.findings.md`.
Reclassified from fix round 3 (same project line, changed reply): Claude `person.x_other_exc` (model error to representation:
exception 05 no longer unlimited); new Claude disagreements `person.x_must` (model error: HSA excess omitted, printed
Schedule 2 line 8 box differs), `person.x_l2_all` (model error), `person.x_two23` and `over` (representation); deepseek
`person.hsa_agreed`, `person.hsa_step1`, `person.hsa_share`, `person.tip_*`, `person.plan_amount_a`, `person.plan_taxable`,
`person.plan_rollovers`, `person.s179_nonlisted`, `person.se_line6`, `person.se_line12`, `person.se_line13`, `person.s16`,
`Step 1`, `Step 2`, `Step 21`, `person.dc_has_box10`, `person.x_limit_binds`, `eligible` (to model error: the new reply's
declarations fail validation), `Step 6` (representation to model error: the reply now enters $350,000 itself). 36 deepseek
lines are new to the open list, most through the field-prefix failure; the deepseek render log's `person.ira_excess` screen
is new (L1).
