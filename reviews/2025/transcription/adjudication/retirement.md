# Adjudication — retirement

Method: `README.md` in this directory. Earlier rulings were made in the logs' sidecars (archived in
`.transcription/archive/before-stage21-2026-10-29/`); no summary was kept for them.

## Stage 21 (superseded subject)

Subject after Stage 21: the collection is a child of `person` (D1); codes `early_1`, `simple_S` and `disability_3`
(`bad_code` takes S only on `traditional_ira` and 3 only on an IRA); `retirement.special` without its code 1/J/S
clause; the Stage 21 block (`early`, `early_screen`, `code_screen`, `screen_refused`, `exception`, `exc_amount`,
`wrong_kind`, `l1`, `l2`, `l2_e05` to `l2_e23`, `l1_s`, `l2_s`). Triage `../triage/retirement.json` and
`../triage/retirement.deepseek.json` (executable-triage-v2; 1,372 fixtures, 500 generated returns seed 20261026, 1,140
partial records; 2,528 comparisons; both replies valid). Pages given: f1099r pp. 5 and 7, i1040gi pp. 26 to 31, i5329 pp.
1, 3 and 5, f8880. Rulings in `.transcription/proposed/stage21/` (`transcription.retirement[.deepseek].json`,
`render.retirement[.deepseek].json`, `classm.retirement[.deepseek].json`).

"Screens" below: `early_screen` is asked for code 1 and S, `code_screen` for codes 2, 4 and 7 (D3(a)); a candidate that
refuses every entry on them needs answers the source does not ask.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| both | transcription | retirement.is_ira | representation | 2,528/2,528 agree | i1040gi p. 26 | traditional or Roth = not plan. |
| both | transcription | retirement.has_rollover | scope | 2,186 agree; 227 project-refuses, 115 project-unknown (partials withholding account/special); no value | i1040gi pp. 27, 30 | Project reads `rolled`, refused on `special`/`bad_code`. |
| claude | transcription | retirement.taxable | model error | 2,431 agree; 37 value (classm.tcw.15 $39,110 vs $49,089; generated 395 $0 vs $22,738.41) | i1040gi p. 28, Fully Taxable | Worksheet line 9 on a cost-recovered annuity exceeds box 1. |
| deepseek | transcription | retirement.taxable | model error | 2,264 agree; 37 value (same); 170 project-refuses (`bad_code`, scope) | i1040gi p. 28; p. 27 Exception 2 | Same; also computes non-Q Roth and code other (refused). |
| claude | transcription | retirement.amount_a | model error | 2,383 agree; 2 value (generated 421 $29,413.54 vs $0); 87 candidate-unknown | i1040gi p. 29, SMW line 1 | Omits line 5a for an annuity whose worksheet line 8 is zero. |
| deepseek | transcription | retirement.amount_a | model error | 2,187 agree; 44 value (classm.tcw.15 $0 vs $39,110); 170 project-refuses (scope) | i1040gi p. 28, Fully Taxable | Shows line 5a for fully taxable annuities. |
| both | transcription | retirement.sav_amount | model error | 2,268 agree; 79 candidate-unknown (21 completed); 119 project-refuses (scope); no value | f8880 p. 2, Line 4 | Asks plan-only exclusions of IRAs and vice versa; inherited reading is amb.2025.savers_inherited_plans. |
| claude | transcription | retirement.l1 | model error (+ ambiguity) | 1,509 agree; 926 candidate-unknown (40 completed); 87 value, all code 2 | i5329 p. 3, Line 1 | Needs screens on every entry; code 2 on line 1 is amb.2025.f5329_line1_codes. |
| deepseek | transcription | retirement.l1 | model error (+ ambiguity) | 1,489 agree; 944 candidate-unknown; 88 value (code 2) | i5329 p. 3, Line 1 | Same; also code 3. |
| claude | transcription | retirement.l2 | model error (+ ambiguity) | 1,453 agree; 976 candidate-unknown; 84 value (code 2); 15 candidate-refuses (refused returns) | i5329 p. 5, Line 2 | Same as l1. |
| deepseek | transcription | retirement.l2 | model error (+ ambiguity, scope) | 1,429 agree; 997 candidate-unknown; 85 value; 1 project-refuses (`wrong_kind`) | i5329 p. 5, Line 2 | Same; no account rule. |
| both | transcription | retirement.l2_e05, l2_e09, l2_e19, l2_e22 | model error | claude 863-866, deepseek 967-973 candidate-unknown; no value | i5329 p. 5, Line 2 | Tests the exception answer on entries it is not asked of. |
| both | transcription | retirement.is_e23, l2_e23 | model error | claude 43/45, deepseek 973/969 candidate-unknown; no value | p590b p. 28; i5329 p. 5 | Same. |
| claude | transcription | retirement.l1_s, l2_s | model error (+ scope) | 2,526/2,528 agree; 1-2 candidate-unknown, 1 project-refuses (`bad_code`) | i5329 p. 5, Line 4 | Needs `code_screen` on a code S entry. |
| deepseek | transcription | retirement.l1_s, l2_s | model error | 1,562 agree; 949/950 candidate-unknown; no value | i5329 p. 5, Line 4 | Needs screens on every entry. |
| claude | transcription | (SMW 4) | representation | 2,528/2,528 agree | i1040gi p. 29, line 4 | Whole-year age bands equal. |
| deepseek | transcription | (SMW 4) | scope | 2,379 agree; 103 candidate-refuses (refused returns), 46 candidate-unknown (partials withholding `special`) | i1040gi p. 29 | Refuses on `special`, the project's own screen. |
| both | render | (SMW 2), (SMW 8), (SMW 10); claude also (SMW 4), (SMW 11) | scope | MISMATCH | i1040gi p. 29 | Death benefit exclusion and pre-1987/pre-Nov-1996 annuities refused by `special`/`annuity`, as archived. |
| both | classm | classm.retirement.1 r2 smw1, smw9 | finding (F3) | project $28,224.00 shown, model $0.00 | i1040gi pp. 28-29 | Worksheet lines shown on an IRA entry that never reaches the worksheet. |

Findings (`.transcription/proposed/stage21/retirement.findings.md`): F2 (EXC-NUMBER, low): the `retirement.exception`
question numbers terminal illness 21; i5329 p. 5 numbers it 20. F3 (SMW-SHOWN, low, display only, pre-existing): the ten
Simplified Method Worksheet lines have no `shown_when` and show amounts on entries that never use the worksheet. The
exception-amount question's missing limits are F1 (EXC-LIMITS) in `f5329.findings.md`. `retirement.special` and
`retirement.bad_code` changed exactly as D2 and Settled 3 say.

## Stage 21 round 2 (superseded subject)

Subject after the round-1 fixes BUG-0203 and BUG-0204 (question text only): `exc_amount` states the 22 and 23
account-value limits and the 07 and 08 amounts; `early_screen` lists a second emergency distribution within 3 years;
`exception` numbers terminal illness 20; `code` names `early_1`, `simple_S` and `disability_3`. The 16 compared project
expressions are byte-identical to round 1. Triage `../triage/retirement.json` and `../triage/retirement.deepseek.json`
(executable-triage-v2; 1,372 fixtures, 500 generated returns seed 20261026, 1,140 partial records; 2,528 comparisons;
both replies valid, no evaluation failures). Pages given as in round 1. Rulings in
`.transcription/proposed/stage21/round2/` (`transcription.retirement[.deepseek].json`,
`render.retirement[.deepseek].json`, `classm.retirement.json`). "Screens" as in the Stage 21 table.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| both | transcription | retirement.is_ira | representation | 2,528/2,528 agree | i1040gi p. 26 | traditional or Roth = not plan. |
| both | transcription | retirement.has_rollover | scope | 2,186 agree; 227 project-refuses, 115 project-unknown (partials); no value | i1040gi pp. 27, 30 | Project reads `rolled`, refused on `special`/`bad_code`. |
| claude | transcription | retirement.taxable | model error | 2,384 agree; 44 candidate-refuses on its `h_recovered_bad` (classm.tcw.15, generated 395, completed); 44 project-refuses (scope) | i1040gi p. 28, Fully Taxable | Refuses a cost-recovered annuity that the source makes fully taxable. |
| deepseek | transcription | retirement.taxable | model error | 2,257 agree; 37 value (classm.tcw.15 $39,110 vs $49,089; generated 395 $0 vs $22,738.41); 170 project-refuses (scope) | i1040gi p. 28; p. 27 Exception 2 | Worksheet line 9 on a cost-recovered annuity exceeds box 1. |
| claude | transcription | retirement.amount_a | model error | 2,300 agree; 2 value (generated 421 $29,413.54 vs $0); 44 candidate-refuses; 82 candidate-unknown | i1040gi p. 29, SMW line 1 | Omits line 5a for an annuity whose worksheet line 8 is zero. |
| deepseek | transcription | retirement.amount_a | model error | 985 agree; 916 value (272 completed; classm.s2.3.deepseek $0 vs $92) | i1040gi pp. 27, 28 | Copies box 1 to line 4a/5a on fully taxable entries. |
| claude | transcription | retirement.sav_amount | model error | 2,268 agree; 79 candidate-unknown (21 completed); no value | f8880 p. 2, Line 4 | Asks plan-only exclusions of IRAs and vice versa. |
| deepseek | transcription | retirement.sav_amount | model error | 2,186 agree; 64 value (classm.dependent.5.deepseek $6,151 vs $0); 67 candidate-unknown | f8880 p. 2, Line 4 | Drops a partly rolled-over distribution whole; same account point. |
| claude | transcription | retirement.l1 | model error (+ ambiguity) | 1,417 agree; 809 candidate-unknown (40 completed); 90 value (code 2) | i5329 p. 3, Line 1 | Needs screens on every entry; code 2/3 on line 1 is amb.2025.f5329_line1_codes. |
| deepseek | transcription | retirement.l1 | model error (+ ambiguity) | 1,485 agree; 848 candidate-unknown; 89 value (code 2) | i5329 p. 3, Line 1 | Same. |
| claude | transcription | retirement.l2 | model error (+ ambiguity) | 1,471 agree; 953 candidate-unknown; 90 value (code 2) | i5329 p. 5, Line 2 | Same as l1. |
| deepseek | transcription | retirement.l2 | model error (+ scope) | 1,191 agree; 320 value (classm.retirement.3 $4,915 vs $0; stage21.blind.e4 a to d); 854 candidate-unknown; 1 project-refuses (`wrong_kind`) | i5329 p. 5, Line 2 | Redefines l2 to omit the capped exceptions that `person.x_l2_all` sums. |
| both | transcription | retirement.l2_e05, l2_e09, l2_e19, l2_e22, l2_e23 | model error | claude 863-866, deepseek 872-878 candidate-unknown; no value | i5329 p. 5, Line 2 | Tests the exception answer on entries it is not asked of. |
| both | transcription | retirement.is_e23 | model error | claude 44 (codes 2, 3: classm.ira.2, stage21.blind.e9), deepseek 863 candidate-unknown; no value | p590b p. 28; i5329 p. 5 | Same. |
| claude | transcription | retirement.l1_s, l2_s | model error (+ scope) | 2,526/2,528 agree; 1-2 candidate-unknown, 1 project-refuses (`bad_code`) | i5329 p. 5, Line 4 | Needs `code_screen` on a code S entry. |
| deepseek | transcription | retirement.l1_s, l2_s | model error | 1,558 agree; 854/855 candidate-unknown; no value | i5329 p. 5, Line 4 | Needs screens on every entry. |
| both | transcription | (SMW 4) | representation | 2,528/2,528 agree | i1040gi p. 29, line 4, Tables 1 and 2 | Whole-year age bands equal. |
| both | render | (SMW 2), (SMW 4), (SMW 8), (SMW 10); claude also (SMW 11) | scope | MISMATCH | i1040gi p. 29 | Death benefit exclusion and pre-1987/pre-Nov-1996 annuities refused by `special`/`annuity`, as in round 1. |
| claude | classm | classm.retirement.3 r1 smw1, smw9 | finding (F3), dropped | project $11,843.00 shown, model $0.00 (traditional IRA, code S, `annuity` false) | i1040gi pp. 28-29 | Worksheet lines shown on an IRA entry; F3 unchanged (T-081 (2)). |

Findings (`.transcription/proposed/stage21/round2/retirement.findings.md`): the round-1 fixes check out against i5329
p. 5, p590b pp. 25, 27 and 28 and f1099r p. 7 (F2 closed; F1's account-value limbs stated). New: F4 (EXC-USE, medium,
tax overstated; it predates round 2): `exc_amount` asks for "the amount you used for that purpose" for 05, 19 and 22,
whose source rules have no use test. F3 (SMW-SHOWN) stands as recorded in round 1.

## Stage 21 round 3 (superseded subject)

Subject after BUG-0205 (question text only): `exc_amount` asks per exception for the amount that qualifies (05, 19, 22, no
use test), the amount used (09), the emergency amount (23), the premiums (07) and the education expenses (08), and 22 and 23
name the IRA or plan account. The 16 compared project expressions are unchanged. Triage `../triage/retirement.json` and
`../triage/retirement.deepseek.json` (executable-triage-v2; 1,373 fixtures, 500 generated returns seed 20261026, 1,118 partial
records from 40 bases; 2,463 comparisons; both replies valid). Rulings in `.transcription/proposed/stage21/round3/`
(`transcription.retirement[.deepseek].json`, `render.retirement[.deepseek].json`). Class M logs are current and ruled.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| both | transcription | retirement.is_ira | representation | 2,463/2,463 | i1040gi p. 26 | Same set. |
| both | transcription | retirement.has_rollover | scope | 2,157 agree; project-refuses and partials only | i1040gi pp. 27, 30 | Project reads `rolled` with its cited refusals. |
| claude | transcription | retirement.taxable | model error | 5 completed value (classm.tcw.15 $39,110.00 vs $49,089.00); code G with $0 rollover taxed (classm.aqee.1.deepseek) | i1040gi pp. 28, 30 | Signed worksheet line 7; reads the rollover amount on a direct rollover. |
| deepseek | transcription | retirement.taxable | model error | 7 completed value (classm.tcw.15; classm.f8962.2 $35,839.00 vs $41,992.24) | i1040gi pp. 28, 29 | Signed line 7; (SMW 4) ignores last year's line 4. |
| claude | transcription | retirement.amount_a | model error | 5 completed value (classm.tcw.15 $0.00 vs $39,110.00) | i1040gi pp. 28, 29 | Inherited from taxable. |
| deepseek | transcription | retirement.amount_a | scope | no value; cited gates and partials | i1040gi p. 28 | Round-2 error fixed. |
| claude | transcription | retirement.sav_amount | model error | 23 completed candidate-unknown; 47 value (classm.retirement.4 $0.00 vs $10,905.00) | f8880 p. 2, Line 4 | Account-wrong exclusions; code G with $0 rollover counted. |
| deepseek | transcription | retirement.sav_amount | model error | 23 completed candidate-unknown; no value | f8880 p. 2, Line 4 | Account-wrong exclusions; rollover now the project's. |
| claude | transcription | retirement.l1, l2 | model error and scope | 42 completed candidate-unknown; no value | i5329 pp. 3, 5 | Screens on every entry; codes 2 and 3 no longer on line 1. |
| deepseek | transcription | retirement.l1, l2 | ambiguity and model error | 20 completed value (generated 22, code 4: $0.00 vs $18,218.60; generated 278 via SMW 4) | i5329 pp. 3, 5; amb.2025.f5329_line1_codes | Codes 2-4 on line 1 offset on line 2; screens on every entry; l2 redefinition gone. |
| both | transcription | retirement.l2_e05, e09, e19, e22, e23 | model error | 862-1,065 candidate-unknown; deepseek e19 1 completed value (generated 278, via SMW 4) | i5329 p. 5, Line 2 | Exception answer needed on entries it is not asked of. |
| claude | transcription | retirement.is_e23 | representation | 2,463/2,463 | p590b p. 28 | Now guarded on code 1 or S. |
| deepseek | transcription | retirement.is_e23 | model error | 864 candidate-unknown | p590b p. 28 | Same reply as round 2. |
| both | transcription | retirement.l1_s, l2_s | model error (+ scope) | claude 2 differ (refused); deepseek 1,006 candidate-unknown/refuses, no value | i5329 p. 5, Line 4 | Screens needed on entries they do not concern. |
| claude | transcription | (SMW 4) | representation | 2,463/2,463 | i1040gi p. 29 | Same bands and prior-year branch. |
| deepseek | transcription | (SMW 4) | model error | 6 completed value (classm.f8962.2 $690.00 vs $177.23) | i1040gi p. 29, line 4 | No branch for last year's line 4. |
| both | render | (SMW 2), (SMW 4), (SMW 10); claude (SMW 8), (SMW 11); deepseek (SMW 5) | scope | MISMATCH | i1040gi p. 29 | Death benefit exclusion and pre-1987 / pre-November-19-1996 annuities refused by `special` and `annuity`. |

Findings: none. BUG-0205 checked against i5329 p. 5 and p590b pp. 25, 27 and 28: 05, 19 and 22 no longer carry a use test
(F4 EXC-USE closed); 22 and 23 name "the IRA or plan account" (round-2 observation addressed); 07 and 08 unchanged. No new
error. Observation (not ruled a finding): 09 asks for "the amount used to pay qualified acquisition costs" without p590b
p. 27's "before the close of the 120th day after the day you received it"; the question restates no exception's
qualification window (19 and 22 have one-year windows too), treating qualification as part of choosing the exception, so the
120-day test is consistent with that convention, but adding it would match the source's amount rule. F3 (SMW-SHOWN) stands
as recorded (T-081 (2)).

## Stage 21 round 4 (superseded subject)

Subject after the owner's round-3 answers: `exc_amount` exception 09 asks for "the amount used to pay qualified acquisition
costs before the close of the 120th day after the day you received it" (p590b p. 27, First home, requirement 1). The 16
compared project expressions are unchanged. Triage `../triage/retirement.json` and `../triage/retirement.deepseek.json`
(executable-triage-v2; 1,374 fixtures, 500 generated returns seed 20261026, 1,085 partial records from 40 bases; 2,387
comparisons; both replies valid). Rulings in `.transcription/proposed/stage21/round4/transcription.retirement[.deepseek].json` and
`render.retirement[.deepseek].json` (render logs re-run after the 09 rewording). Class M logs are current (round 3).

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| both | transcription | retirement.is_ira | representation | 2,387/2,387 | i1040gi p. 26 | Same set. |
| claude | transcription | retirement.has_rollover | model error and scope | 3 completed value (classm.tcw.5: code G, box 1 $0, project true, candidate false); project-refuses and partials | i1040gi pp. 27, 30 | A $0 direct rollover is still a rollover (box 1 on line 4c/5c). |
| deepseek | transcription | retirement.has_rollover | scope | 1,989 agree; project-refuses and partials only | i1040gi pp. 27, 30 | Project reads `rolled` with its cited refusals. |
| claude | transcription | retirement.taxable | model error and scope | 2 completed candidate-refuses (classm.tcw.15, generated 395); no value | i1040gi pp. 28, 29 | Refuses on recovered above cost (h_recovered_bad), which the source does not; signed line 7 gone. |
| deepseek | transcription | retirement.taxable | model error and scope | 2 completed value (classm.tcw.15 $39,110.00 vs $49,089.00; generated 395 $0.00 vs $22,738.41); 16 completed candidate-unknown | i1040gi pp. 27-29 | Signed worksheet line 7; reads box 5 and annuity on IRA entries. |
| claude | transcription | retirement.amount_a | model error and scope | 2 completed value (classm.tcw.15 $0.00 vs $39,110.00) | i1040gi pp. 28, 29 | Box 1 on line 5a for a cost-recovered annuity. |
| deepseek | transcription | retirement.amount_a | model error and scope | 3 completed value (classm.ira.2 $20,743.00 vs $0.00; classm.tcw.15 $0.00 vs $39,110.00) | i1040gi pp. 28, 30 | Ignores box 5; box 1 for a cost-recovered annuity; regression from round 3. |
| both | transcription | retirement.sav_amount | model error and scope | 20 completed candidate-unknown; no value | f8880 p. 2, Line 4 | Account-wrong exclusions (amb.2025.savers_inherited_plans for the inherited reading). |
| claude | transcription | retirement.l1 | model error and scope | 40 completed candidate-unknown; no value | i5329 p. 3 | Screens on every entry. |
| deepseek | transcription | retirement.l1 | model error and scope | 3 completed value (classm.f5329.2, code S: $25,190.00 vs $0.00; stage21.blind.e2) | i5329 pp. 3, 5 | Code S left off line 1; screens on every entry. |
| claude | transcription | retirement.l2 | model error | 39 completed candidate-unknown; no value | i5329 p. 5, Line 2 | Exception answer needed on every entry. |
| deepseek | transcription | retirement.l2 | model error and scope | 7 completed value, all the uncapped amount: stage21.example.teacher_education (p970 p. 56 official example) $500.00 vs $800.00 and 5 partials of it; generated 278 $0.00 vs $2,648.29 | i5329 p. 5, Line 2; p970 p. 56 | Code S left off; exception amount not capped by line 1; screens everywhere. |
| claude | transcription | retirement.l2_e05, e09, e19, e22, e23 | model error | 872-875 candidate-unknown (33-35 completed); no value | i5329 p. 5, Line 2 | Exception answer needed on entries it is not asked of. |
| deepseek | transcription | retirement.l2_e05, e09, e19, e22, e23 | model error | 903-915 candidate-unknown (40 completed); e19 generated 278 $0.00 vs $2,648.29 | i5329 p. 5, Line 2 | Exception amount not capped by line 1; screens everywhere. |
| claude | transcription | retirement.is_e23 | representation | 2,387/2,387 | p590b p. 28 | Guarded on code 1 or S. |
| deepseek | transcription | retirement.is_e23 | model error | 872 candidate-unknown (33 completed) | p590b p. 28 | Same reply as round 3. |
| both | transcription | retirement.l1_s | model error and scope | claude 2 differ (refused); deepseek 880 candidate-unknown, no value | i5329 p. 5, Line 4 | Screens needed on entries they do not concern. |
| claude | transcription | retirement.l2_s | model error | 1 candidate-unknown (refused) | i5329 p. 5, Line 4 | code_screen needed on a code S entry. |
| deepseek | transcription | retirement.l2_s | model error | 879 candidate-unknown; generated 286 $0.00 vs $5,412.88 (refused) | i5329 p. 5, Lines 2, 4 | Uncapped exception amount; screens everywhere. |
| both | transcription | (SMW 4) | representation | 2,387/2,387 | i1040gi p. 29 | Same bands and prior-year branch (deepseek's round-3 error gone). |
| both | render | (SMW 2), (SMW 4), (SMW 10); claude (SMW 8), (SMW 11); deepseek (SMW 5) | scope | MISMATCH (claude 5 open, deepseek 4 open) | i1040gi p. 29 | Death benefit exclusion and pre-November-19-1996 annuities refused by `special` and `annuity`; same reading as round 3, reworded. |

Findings: none. The exception 09 wording was checked against p590b p. 27 ("1. It must be used to pay qualified acquisition
costs (defined next) before the close of the 120th day after the day you received it"): it quotes requirement 1 word for
word, and it introduces no error. It asks for no more and no less than the source's amount. A 2025 distribution spent within
120 days in 2026 still counts, and money spent after the window is excluded. The $10,000 lifetime limit stays per person
(`person.x_prior09`, `f5329.cap_first_home`). Requirement 2, who the home may be for, is not restated, which follows the
convention that qualification is part of choosing the exception. No reply raised the 09 wording. Round-3 observation closed.
F3 (SMW-SHOWN) stands as recorded (T-081 (2)).

## T-067 (superseded subject)

The subject after T-067 (the owner's decision of 2026-10-29 on worksheet markers): the ten Simplified Method Worksheet lines
`(SMW 1)` to `(SMW 11)` carry `shown_when: retirement.annuity`, and no computing expression changed. Triage is
`../triage/retirement.json` and `../triage/retirement.deepseek.json` (executable-triage-v2: 1,374 fixtures, 500 generated
returns with seed 20261026, 1,096 partial records from 40 bases, 2,379 comparisons; both replies valid). Every completed
difference was checked against an uncapped re-run of `triage.mjs` in scratch. The rulings are in
`.transcription/proposed/t067/` (`transcription.retirement[.deepseek].json` and `render.retirement.deepseek.json`). The
Claude render log has no open section. "Screens" has the same meaning as in the Stage 21 table.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | retirement.has_rollover | model error and scope | 3 completed value (classm.tcw.5: code G, box 1 $0, project true, candidate false); the rest are project-refuses and partials | i1040gi pp. 27, 30 | A $0 direct rollover is still a rollover. |
| deepseek | transcription | retirement.has_rollover | scope | 2,066 agree; only project-refuses and partials, none completed | i1040gi pp. 27, 30 | The project reads `rolled` with its cited refusals. |
| both | transcription | retirement.taxable | model error and scope | 2 completed value (classm.tcw.15 $39,110.00 vs $49,089.00; generated 395 $0.00 vs $22,738.41); deepseek also has 10 completed candidate-unknown on box 5 of IRA entries | i1040gi pp. 28, 29 | Signed worksheet line 7 on a cost-recovered annuity. |
| claude | transcription | retirement.amount_a | model error and scope | 2 completed value (classm.tcw.15 $0.00 vs $39,110.00; generated 314 $0.00 vs $46,209.90) | i1040gi p. 28 | Box 1 on line 5a for a fully taxable annuity. |
| deepseek | transcription | retirement.amount_a | model error and scope | 328 completed value, all project $0.00 against box 1 (classm.s2.3 $92.00) | i1040gi pp. 27, 28 | Copies box 1 to 4a/5a on every entry. |
| both | transcription | retirement.sav_amount | model error and scope | 27 completed candidate-unknown (sav_military 10, sav_404k 10, sav_inherited 7); no value | f8880 p. 2, Line 4 | Exclusions applied to the wrong account kinds (amb.2025.savers_inherited_plans). |
| both | transcription | retirement.l1 | model error and scope | claude 57, deepseek 63 completed candidate-unknown; no value | i5329 pp. 3, 5 | Screens on every entry; deepseek's round-4 code S error is gone. |
| claude | transcription | retirement.l2 | model error | 51 completed candidate-unknown; no value | i5329 p. 5, Line 2 | Exception and screens needed on every entry. |
| deepseek | transcription | retirement.l2 | model error and scope | 59 completed candidate-unknown; no value | i5329 p. 5, Line 2 | Screens on every entry; the round-4 cap and code S errors are gone. |
| claude | transcription | retirement.l2_e05, e09, e19, e22, e23 | model error | 48-50 completed candidate-unknown; no value | i5329 p. 5, Line 2 | Exception answer needed on entries where it is not asked. |
| deepseek | transcription | retirement.l2_e05, e09, e19, e22, e23 | model error and scope | 57-58 completed candidate-unknown; no value | i5329 p. 5, Line 2 | Screens on every entry; now capped by line 1. |
| claude | transcription | retirement.is_e23 | representation | 2,379/2,379 | p590b p. 28 | Guarded on code 1 or S. |
| deepseek | transcription | retirement.is_e23 | model error | 48 completed candidate-unknown | p590b p. 28 | Exception answer needed on every entry. |
| claude | transcription | retirement.l1_s, l2_s | model error (+ scope) | 2 candidate-unknown, on refused returns only | i5329 p. 5, Line 4 | code_screen needed on a code S entry. |
| deepseek | transcription | retirement.l1_s, l2_s | model error (+ scope) | 57 completed candidate-unknown; no value | i5329 p. 5, Line 4 | Screens on every entry. |
| claude | transcription | (SMW 4) | finding (F5) and representation | 546 candidate-unknown and 15 candidate-shows-skipped, all on project-hidden lines; with the candidate's own `shown_when` applied, 2,346 agree and the 33 left are partials withholding `annuity` on IRA entries (project shows) | i1040gi pp. 29, 30 | The candidate's account guard is right; the project's condition fails open on IRA entries. |
| deepseek | transcription | (SMW 4) | model error and finding (F5) | the same 561 differences, all on project-hidden lines (classm.dcprov.1: candidate $624.31 shown) | i1040gi pp. 29, 30 | No hiding condition, so the line asks for worksheet answers on entries that never use the worksheet. |
| deepseek | render | (SMW 1), (SMW 2), (SMW 4) to (SMW 11) | scope | MISMATCH (10 open) | i1040gi p. 30, Simplified Method | Condition 1 alone (start July 2, 1986 to November 18, 1996) is refused by `special`. |

The brief's check: `shown_when: retirement.annuity` hides the worksheet correctly for a fully taxable pension. The plan
entry is asked `annuity`, the answer is false, and the worksheet is hidden (stage10.plan.direct_rollover with code 7: no
`(SMW` line, 5a $0, 5b $20,000). It fails on an IRA, because the interview never asks `annuity` on an IRA entry, so the
condition is unknown and all ten lines print, with `(SMW 1)` = box 1 (classm.s2.3.deepseek without the worksheet answers:
the interview completes and `(SMW 1)` shows $92). It also fails on an annuity whose cost was recovered before 2025, where
the project is fully taxable through `cost_left` yet shows the worksheet (generated 395: `(SMW 9)` $22,738.41 against a
taxable amount of $0; stage10.smw.cost_recovered). Suspected tooling defect: `triage.mjs` applies only the project's
`shown_when` and ignores a `shown_when` the candidate declares (Claude's `h_smw`), so the Claude (SMW 4) record counts
561 differences that the reply's own condition removes. T-079 (1) does not apply: retirement is a collection with no open
class M section.

Findings (`.transcription/proposed/t067/retirement.findings.md`): F5 (SMW-IRA-SHOWN, medium, display only): the worksheet is
shown on every IRA entry because `retirement.annuity` is never asked there. F6 (SMW-RECOVERED-SHOWN, medium, display only):
the worksheet is shown on an annuity whose cost was recovered before 2025, contrary to i1040gi p. 28 (b) and p. 29 line 11.
One helper fixes both (`is_ira` false and `annuity_with_cost`). F3 (SMW-SHOWN) is now closed for non-annuity plan entries
only.

## T-067 round 2 (superseded subject)

The subject after BUG-0207 and BUG-0208: the ten `(SMW n)` lines carry `shown_when: retirement.smw_shown`, a Bool that is
true when `is_ira` is false (tested first) and `annuity_with_cost` is true. Regressions: `stage21.t067.smw_hidden_ira` and
`stage21.t067.smw_hidden_cost_recovered`. No computing expression changed. Triage is `../triage/retirement[.deepseek].json`
(executable-triage-v2: 1,376 fixtures, 500 generated returns with seed 20261026, 1,000 partial records from 40 bases, 1,894
comparisons). Every completed difference was checked against an uncapped scratch re-run. The replies are fresh and declare
no `shown_when`. The rulings are in `.transcription/proposed/t067/round2/`.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| both | transcription | retirement.is_ira | representation | 1,894/1,894 | i1040gi p. 26 | Same set. |
| claude | transcription | retirement.has_rollover | model error and scope | 3 completed value (classm.tcw.5: code G, box 1 $0, project true, candidate false) | i1040gi pp. 27, 30 | A $0 direct rollover is a rollover. |
| deepseek | transcription | retirement.has_rollover | scope | nothing completed; project-refuses and partials | i1040gi pp. 27, 30 | The project's cited gates. |
| claude | transcription | retirement.taxable | model error and scope | 12 completed candidate-refuses (h_recovered_bad: classm.tcw.15 and partials, generated 395) | i1040gi p. 28 | Refuses a cost-recovered annuity, which the source makes fully taxable. |
| deepseek | transcription | retirement.taxable | model error and scope | 8 completed value (classm.tcw.15 $39,110.00 vs $49,089.00; generated 395 $0.00 vs $22,738.41); 4 completed candidate-unknown | i1040gi pp. 28, 29 | Signed line 7. |
| claude | transcription | retirement.amount_a | model error and scope | 12 completed candidate-refuses; generated 314 $0.00 vs $46,209.90 (cost $0) | i1040gi p. 28 | Box 1 on line 5a for a fully taxable annuity. |
| deepseek | transcription | retirement.amount_a | model error and scope | 157 completed value, all project $0.00 against box 1 | i1040gi pp. 27, 28 | Copies box 1 to line 4a/5a. |
| both | transcription | retirement.sav_amount | model error and scope | 18 completed candidate-unknown (sav_military 8, sav_404k 8, sav_inherited 2) | f8880 p. 2, Line 4 | Exclusions asked of the wrong account kinds. |
| claude | transcription | retirement.l1, l2 | ambiguity and model error | 2 completed value (generated 175 $0.00 vs $52,095.29; generated 348, code 2); 61 and 56 completed candidate-unknown | i5329 pp. 3, 5; amb.2025.f5329_line1_codes | Code 2 on line 1 offset on line 2; screens on every entry. |
| claude | transcription | retirement.l2_e05, e09, e19, e22, e23; is_e23 | model error | 53-54 completed candidate-unknown; no value | i5329 p. 5; p590b p. 28 | Exception answer needed on every entry (is_e23 lost its round-1 guard). |
| claude | transcription | retirement.l1_s | model error and scope | 2 completed candidate-unknown (code_screen on code S) | i5329 p. 5, Line 4 | A screen for codes 2, 4 and 7 only. |
| claude | transcription | retirement.l2_s | representation | 1,894/1,894 | i5329 p. 5, Line 4 | Same share. |
| deepseek | transcription | retirement.l1, l2, l2_e05 to e23, l1_s, l2_s | model error and scope | 61-62 completed candidate-unknown (early_screen 54, code_screen 7); no value | i5329 pp. 3, 5 | Screens on every entry. |
| deepseek | transcription | retirement.is_e23 | model error | 54 completed candidate-unknown | p590b p. 28 | Exception answer on every entry. |
| both | transcription | (SMW 4) | model error | 398 differences, all on project-hidden lines: 85 candidate-shows-skipped (cost-recovered annuities, e.g. generated 395 $1,550.08; classm.dcprov.1 IRA), 313 candidate-unknown (87 completed) | i1040gi pp. 28-30 | No hiding condition in the reply; the value matches wherever the project shows the line. |
| claude | render | (SMW 2), (SMW 4), (SMW 8), (SMW 10), (SMW 11) | scope | MISMATCH | i1040gi p. 29 | Death benefit exclusion and pre-November-19-1996 annuities are refused by `special`. |
| deepseek | render | (SMW 2), (SMW 4), (SMW 6), (SMW 7), (SMW 8), (SMW 10), (SMW 11) | scope | MISMATCH | i1040gi p. 29 | Same. |

Check of the fix, by evaluating cases, since the comparison ignores `shown_when`:

- **IRA with the pension answers unasked.** classm.s2.3.deepseek with those answers removed, and the regression
  `smw_hidden_ira`: the interview completes and no `(SMW` line shows. A traditional IRA answered `annuity` true is also
  hidden.
- **Cost recovered or $0.** stage10.smw.cost_recovered, recovered_exceeds_cost, `smw_hidden_cost_recovered`,
  classm.tcw.15 and generated 395 are hidden, with line 5a $0 and line 5b equal to box 1.
- **Fully taxable pension.** A code 7 plan entry with `annuity` false is hidden (5b $20,000).
- **Cost left.** stage10.smw.first_year and a variant with $500 of cost left show all ten lines, and `(SMW 9)` equals 5b.

A sweep of every fixture and generated return found `smw_shown` equal to (plan, annuity true, cost above recovered) on every
entry where those inputs are answered, and false on every IRA entry. It is unknown only on a plan entry of a return refused
on `special` before `annuity` is asked (stage16.cleanup.refuse.retirement.special_first). That is an observation, not a
finding, because the return is refused.

Findings: none. F5 and F6 are closed by BUG-0207 and BUG-0208. F3 (SMW-SHOWN) is closed.

## Fix round 2

The subject after BUG-0243 widened the `retirement.special` question. It now also lists a military disability pension, an
annuity received as the beneficiary of an employee who died or shared among beneficiaries, and a rollover of property
other than cash or of a QDRO distribution. No compared expression changed, and `retirement.smw_shown` and the (SMW n)
lines are unchanged. The replies are fresh. Triage is `../triage/retirement[.deepseek].json` (executable-triage-v2: 1,382
fixtures and 500 generated returns, seed 20261026; 1,035 / 1,026 partial records from 40 bases; 2,066 / 1,963
comparisons). An uncapped scratch re-run of `triage.mjs` gave the same counts, and every completed difference was read
from it. The rulings are in `.transcription/proposed/fixr2/` (`transcription.retirement[.deepseek].json` and
`render.retirement[.deepseek].json`). There is no open class M section. "Screens" has the same meaning as in the Stage
21 table.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| deepseek | transcription | retirement.is_ira | representation | 1,963/1,963 | i1040gi p. 26 | Same set. |
| claude | transcription | retirement.has_rollover | model error and scope | 3 completed value (classm.tcw.5, classm.f1040.3[.deepseek]: code G, box 1 $0, project true, candidate false); rest refused/partials | i1040gi pp. 27, 30 | A $0 direct rollover is a rollover. |
| deepseek | transcription | retirement.has_rollover | scope | nothing completed; project-refuses (bad_code, special) and partials | i1040gi pp. 27, 30 | The project's cited gates. |
| both | transcription | retirement.taxable | model error and scope | 8 completed value (classm.tcw.15 $39,110.00 vs $49,089.00 and partials; generated 395 $0.00 vs $22,738.41); deepseek also 10 completed candidate-unknown on box 5 of IRA entries | i1040gi pp. 27-29 | Signed worksheet line 7; deepseek subtracts box 5 on IRAs. |
| claude | transcription | retirement.amount_a | model error and scope | 12 completed value (classm.tcw.15 $0.00 vs $39,110.00 and partials; generated 314 $0.00 vs $46,209.90) | i1040gi p. 28 | Box 1 on line 5a for a fully taxable annuity. |
| deepseek | transcription | retirement.amount_a | model error and scope | 222 completed value, each checked: project $0.00, candidate box 1, fully taxable entry | i1040gi pp. 27, 28 | Copies box 1 to line 4a/5a. |
| both | transcription | retirement.sav_amount | model error and scope | claude 23, deepseek 27 completed candidate-unknown (sav_military, sav_404k on IRAs; sav_inherited on plans); no value | f8880 p. 2, Line 4 | Exclusions asked of the wrong account kinds. |
| claude | transcription | retirement.l1 | model error and scope | 62 completed candidate-unknown (early_screen 52, code_screen 10); no value | i5329 p. 3 | Screens on every entry; code 2 now off line 1. |
| deepseek | transcription | retirement.l1 | model error and scope | 6 completed value (generated 22 code 4 $0.00 vs $18,218.60; 175, 348 code 2; 314, 381, 421 code 4); 74 completed candidate-unknown | i5329 pp. 3, 5 | Codes 2-4 on line 1 with no line 2 offset (not the register's second reading); screens on every entry. |
| claude | transcription | retirement.l2, l2_e05, l2_e23, l1_s | model error (l1_s + scope) | 5 / 2 / 1 / 1 completed candidate-unknown, all code_screen partials on code 1/S entries; no value | i5329 p. 5 | code_screen needed through line 1. |
| claude | transcription | retirement.l2_e09, l2_e19, l2_e22, l2_s | representation | 2,066/2,066 | i5329 p. 5 | Same split. |
| deepseek | transcription | retirement.l2, l2_e05 to l2_e23, l1_s, l2_s | model error and scope | 67-76 completed candidate-unknown (early_screen 57, code_screen 10, exception 7, box 5 0-2); no value | i5329 pp. 3, 5 | Screens and exception on every entry. |
| deepseek | transcription | retirement.is_e23 | model error | 57 completed candidate-unknown | p590b p. 28 | Exception answer on every entry. |
| both | transcription | (SMW 4) | model error (claude + scope) | all differences on project-hidden lines (completed: generated 395 shows $1,550.08; 155 / 106 candidate-unknown); claude's 4 shown are special partials on refused/incomplete returns | i1040gi pp. 28-30 | No hiding condition in the reply; value matches where shown. |
| both | render | (SMW 2), (SMW 4), (SMW 6), (SMW 7), (SMW 8), (SMW 10), (SMW 11) | scope | MISMATCH (7 open each) | i1040gi p. 29 | Death benefit exclusion and pre-November-19-1996 annuities still refused by `special`. |

The brief's check: BUG-0243 causes no transcription or render difference. The military disability, shared-annuity and
QDRO items match i1040gi pp. 28 and 30. Two items refuse more than the source does, which changes no amount. Findings
(`.transcription/proposed/fixr2/retirement.findings.md`): F1 (BENEFICIARY-VS-SURVIVOR, low): "the beneficiary of an
employee who died" can be read by a survivor of a retiree, a case p. 30 computes and `retirement.age` provides for. F2
(PROPERTY-ROLLOVER, low): "a rollover of property other than cash" covers whole in-kind rollovers, where p. 30 names only
"partial rollovers of property".
