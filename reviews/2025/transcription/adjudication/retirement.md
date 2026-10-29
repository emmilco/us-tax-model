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

## Stage 21 round 3

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
