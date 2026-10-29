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

## Stage 19 round 3

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
