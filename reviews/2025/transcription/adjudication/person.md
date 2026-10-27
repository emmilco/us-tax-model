# Adjudication — person

Method: `README.md` in this directory. Triage records: `../triage/person.json`, `../triage/person.deepseek.json`
(executable-triage-v1; 1,083 fixtures, 500 generated returns, seed 20261026, 1,833 partial records). Full ruling text is in
`.transcription/proposed/person.json` and `.transcription/proposed/person.deepseek.json`, for the log and sidecar.

A ruling's class is the most serious class among its difference kinds (finding, model error, interface gap, ambiguity, scope,
representation); the ruling text rules each kind. Triage evaluates the candidate's whole person graph, so a line whose own
expression matches the project can still differ through a candidate line it reads; those differences are attributed to that
line's ruling. In the deepseek-flash graph every return with a Schedule C is unevaluable because of the person.income179 cycle,
so Schedule C-dependent deepseek lines are ruled on the derivation as well as the witnesses.

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
