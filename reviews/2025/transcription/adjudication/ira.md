# Adjudication — ira

Method: `README.md` in this directory. Triage records: `../triage/ira.json`, `../triage/ira.deepseek.json`
(executable-triage-v1; 1,083 fixtures, 500 generated returns, seed 20261026, 57 partial records). Every
differing record, not only the recorded witnesses, was classified by rerunning the same evaluator without
the witness cap. Full ruling text is in each log and its sidecar.

Recurring facts. The project asks `person.sav_trad` (Yes/No) before the amount `person.ira_trad`; both
candidates read the amount directly, so after No it is unsupplied though necessarily zero. `person.plan`
is asked only with a Schedule C (amb.2025.ira_covered). The worksheet applies only with traditional
contributions (i1040gi p. 95), so lines shown on a return without them reach no amount. "Refused
elsewhere" means the project refuses scope.ready, Form 1040 line 24 or Schedule 1 line 20 for another
cited gate. Skipped-line rule (README): a nonzero amount on a skipped line of a reachable return is a
defect of the side producing it; the project shows zero on every skipped line.

| family | line | class | triage | deciding source | reason |
| --- | --- | --- | --- | --- | --- |
| claude | ira.anyone_covered | representation | 1476/1640 agree; 140 value, 17 candidate-unknown, 7 project-unknown | i1040gi p. 96, self-employed SEP/SIMPLE coverage | Every difference is `person.plan` supplied or needed for a person with no Schedule C, which the interview never asks. |
| claude | ira.cov_gate | representation | 1617/1640; 23 candidate-unknown | i1040gi p. 31, Lines 6a and 6b, Exception | Unknowns come from the unasked `ira_trad` amount (zero) or `person.plan` without a Schedule C. |
| claude | ira.kbh_short | model error | 1472/1640; 148 candidate-unknown, 10 value, 10 candidate-refuses | i1040gi p. 98, Caution; p. 95 | Drops the traditional-contribution condition and refuses joint low-income returns with no contributions (classm.sli.4, classm.ssb.4). |
| claude | ira.both_kinds | representation | 1617/1640; 23 candidate-unknown | i1040gi p. 95, item 2 | Same broad reading (amb.2025.ira_both_kinds); unknowns are the unasked zero amount. |
| claude | ira.over_comp | scope | 599/1640; 987 candidate-unknown, 52 candidate-refuses, 2 value | p590a p. 35, Excess Contributions | Both value records are refused elsewhere; where they could differ the project refuses an excess contribution with a cited screen. |
| claude | ira.special_gate | model error | 674/1640; 966 candidate-unknown | i1040gi p. 95, "read the following list before you fill in the worksheet" | Asks the special-case screen and would refuse on it without any traditional contribution. |
| claude | ira.combat_gate | model error | 1599/1640; 21 candidate-unknown, 20 value | i1040gi p. 98, line 8, nontaxable combat pay | Refuses combat-pay returns with no IRA contribution (stage8.refuse.s8812.combat_pay). |
| claude | ira.excl_gate | model error | 1596/1640; 36 candidate-unknown, 8 value | i1040gi p. 96, Form 2555 or 8815 | Omits the contribution condition; needs coverage on returns without contributions. |
| claude | ira.line20 | model error | 520/1640; 1016 candidate-unknown, 102 candidate-refuses, 2 project-refuses | i1040gi p. 98, line 12 | No value differs; inherits the kbh_short refusal on 5 reachable no-contribution returns; other kinds representation or scope. |
| claude | 1a | representation | 530/1640; 938 candidate-unknown, 172 value | i1040gi p. 97, line 1; p. 95 | All differences on returns without contributions or with `person.plan` and no Schedule C. |
| claude | 1b | representation | 1466/1640; 136 candidate-unknown, 38 value | i1040gi p. 97, line 1 | As 1a, spouse column. |
| claude | 2a | model error | 18/1640; 1419 value, 184 candidate-unknown, 14 project-unknown, 5 candidate-refuses | i1040gi p. 97, "skip lines 2 through 6" | Skipped-line rule: candidate enters line 2 on 176 reachable returns where no one is covered (stage16.ira.i6: $89,000, project $0); MFS refusals fall under s3.mfs. |
| claude | 2b | model error | 7/1640; 1483 value, 136 candidate-unknown, 14 project-unknown | i1040gi p. 97; p. 95 item 6 | Skipped-line rule: 176 reachable returns with an amount on a skipped line (classm.f5695.2: $246,000, project $0). |
| claude | 6a | model error | 469/1640; 610 value, 373 candidate-refuses, 188 candidate-unknown | i1040gi p. 97, "skip lines 2 through 6" | Skipped-line rule: 94 reachable returns (stage16.ira.i6: $84,000, project $0); refusals are on returns refused elsewhere. |
| claude | 6b | model error | 493/1640; 626 value, 373 candidate-refuses, 148 candidate-unknown | i1040gi p. 97; p. 95 item 6 | Skipped-line rule: 92 reachable returns (classm.f5695.3: $72,349, project $0). |
| claude | 7a | representation | 93/1640; 943 candidate-unknown, 517 value, 87 candidate-refuses | i1040gi p. 97; p. 95 | All value records have no contributions; on contributing returns rates, thresholds and the $200 floor agree. |
| claude | 7b | representation | 1397/1640; 136 candidate-unknown, 69 value, 24 candidate-refuses, 14 project-unknown | i1040gi p. 97; p. 95 item 6 | As 7a. |
| claude | 8 | model error | 677/1640; 949 candidate-unknown, 12 candidate-refuses, 2 project-refuses | i1040gi p. 98, line 8; p. 95 list | Wages agree; the line's special-case and combat refusals lack the contribution condition. |
| claude | 9 | ambiguity | 671/1640; 921 candidate-unknown, 46 project-refuses, 2 value | p590a p. 7, Self-employment loss | Per-spouse floor (amb.2025.ira_se_floor) against combined floor (generated 293: $157,316.78 / $109,209.37); unconditional ira.se_capital screen partly model error. |
| claude | 11a | representation | 693/1640; 947 candidate-unknown | i1040gi p. 98, line 11 | Unasked zero amount. |
| claude | 11b | representation | 1505/1640; 134 candidate-unknown, 1 project-unknown | i1040gi p. 98, line 11 | Unasked zero amount; one roster the interview cannot produce. |
| claude | 12a | model error | 538/1640; 996 candidate-unknown, 104 candidate-refuses, 2 project-refuses | i1040gi p. 98, line 12 | No value differs; inherits kbh_short refusal on 6 reachable returns. |
| claude | 12b | model error | 556/1640; 1006 candidate-unknown, 78 candidate-refuses | i1040gi p. 98, line 12 | As 12a. |
| deepseek | ira.anyone_covered | representation | 1640/1640 agree | i1040gi p. 96 | Observed equivalence on the sample. |
| deepseek | ira.cov_gate | model error | 645/1640; 925 candidate-unknown, 70 value | i1040gi p. 31, Exception | Copies anyone_covered, dropping benefits and contributions (stage16.ira.i1). |
| deepseek | ira.kbh_short | model error | 1473/1640; 148 candidate-unknown, 10 value, 9 candidate-refuses | i1040gi p. 98, Caution | Drops the contribution condition, as in the Claude log. |
| deepseek | ira.both_kinds | model error | 1439/1640; 200 candidate-unknown, 1 value | i1040gi p. 95, item 2 | No joint-return condition: refuses a single filer with both kinds (stage16.mut.ira_trad_and_roth, project $3,000). |
| deepseek | ira.over_comp | scope | 611/1640; 987 candidate-unknown, 41 candidate-refuses, 1 value | p590a p. 35 | Only value record refused elsewhere; project's stricter screen is cited. |
| deepseek | ira.special_gate | model error | 674/1640; 966 candidate-unknown | i1040gi p. 95, list | As in the Claude log. |
| deepseek | ira.combat_gate | model error | 1621/1640; 18 project-unknown, 1 value | i1040gi p. 98, line 8 | Constant false: leaves nontaxable combat pay off line 8 (stage16.refuse.ira.combat_pay computed $5,000). |
| deepseek | ira.excl_gate | model error | 1622/1640; 17 project-unknown, 1 value | i1040gi p. 96 | Constant false: computes the covered Form 2555 case the source sends to Pub. 590-A. |
| deepseek | ira.line20 | model error | 576/1640; 1006 candidate-unknown, 51 candidate-refuses, 6 project-refuses, 1 value | i1040gi p. 97, line 6 | stage16.ira.i2: $200 deducted where line 5 is not less than line 2 (project $0). |
| deepseek | 1a | representation | 668/1640; 924 candidate-unknown, 48 value | i1040gi p. 97, line 1 | All on returns without contributions. |
| deepseek | 1b | representation | 1496/1640; 134 candidate-unknown, 10 value | i1040gi p. 97, line 1 | As 1a. |
| deepseek | 2a | model error | 18/1640; 1475 value, 133 candidate-unknown, 14 project-unknown | i1040gi p. 97 | Skipped-line rule: 180 reachable returns (stage16.ira.i6: $89,000, project $0); MFS refused by s3.mfs. |
| deepseek | 2b | model error | 9/1640; 1485 value, 132 candidate-unknown, 14 project-unknown | i1040gi p. 97; p. 95 item 6 | Skipped-line rule: 180 reachable returns (stage16.mut.ira_kbh_none_edge: $246,000, project $0). |
| deepseek | 6a | model error | 500/1640; 628 value, 372 candidate-refuses, 140 candidate-unknown | i1040gi p. 97 | Skipped-line rule: 99 reachable returns (stage16.ira.i6: $84,000, project $0); refusals on returns refused elsewhere. |
| deepseek | 6b | model error | 493/1640; 635 value, 373 candidate-refuses, 139 candidate-unknown | i1040gi p. 97; p. 95 item 6 | Skipped-line rule: 99 reachable returns (stage16.ira.i7: $146,000, project $0). |
| deepseek | 7a | model error | 48/1640; 947 candidate-unknown, 620 value, 25 candidate-refuses | i1040gi p. 97, line 6 | $200 floor on a zero line 6a (stage16.ira.i2) and a percentage above the threshold ($7,010 / $7,000). |
| deepseek | 7b | model error | 27/1640; 925 candidate-unknown, 651 value, 37 candidate-refuses | i1040gi p. 97, line 6 threshold | stage16.ira.i1: $83,650 where the applicable $7,000 applies. |
| deepseek | 8 | model error | 688/1640; 949 candidate-unknown, 2 project-refuses, 1 candidate-refuses | i1040gi p. 98, line 8; p. 95 list | Wages agree; refuses on ira.special with no contribution condition. |
| deepseek | 11a | representation | 693/1640; 947 candidate-unknown | i1040gi p. 98, line 11 | Unasked zero amount. |
| deepseek | 11b | representation | 1505/1640; 135 candidate-unknown | i1040gi p. 98, line 11 | Unasked zero amount. |
| deepseek | 12a | model error | 595/1640; 985 candidate-unknown, 53 candidate-refuses, 6 project-refuses, 1 value | i1040gi p. 98, line 12; p. 97 line 6 | stage16.ira.i2 $200 / $0; refuses reachable both_kinds and kbh_short returns. |
| deepseek | 12b | model error | 584/1640; 989 candidate-unknown, 67 candidate-refuses | i1040gi p. 98, line 12 | Refuses reachable both_kinds and kbh_short returns. |

Findings: none. Project lines unchanged.

## Landing round (2026-11-14), render

Lane land3-adj7 (claude-opus-5-5, judgment). Open lines of the Claude render log `.transcription/logs/2025/render/ira.md`, ruled on the rendered English (`rendered/2025/ira.md`), the form YAML and the cited source; the deepseek log is dormant and not ruled.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | render | (screen) (ira.reservist_repaid) | interface gap | UNCLEAR; form YAML (scope.armed_forces) | p590a p. 9, When repayment contributions can be made | Repayment is allowed only within 2 years after active duty ends, so every 2025 repayer served after the start of 2022; the gate loses nothing. The page was not given to the reviewer. |

Counts: claude render: interface gap 1.

Findings: none. No line left open.

## Landing round (2026-11-14)

Lane land3-adj6 (claude-opus-5-5, judgment; tax year 2025, us). Open lines of the Claude transcription log after the line-scoped pass 12f36e046fb1 of the interview redraft, rerun after the fix that keys two or more computed `(screen)` lines as `(screen) (<id>)` (`docs/provisional/lanes/land3-screen.md`). Evidence: the executable triage record of that pass (`.transcription/triage/2025/ira.json`, executable-triage-v2; 1,986 fixtures, 500 generated returns seed 20261026), `triage.py --explain` derivations where cited, the archived sources and `forms/2025/ira.yaml`. Triage applies the project's display condition only; the reply's own display conditions were ruled by reading its expressions. Full ruling text: the log and its sidecar; rulings file `/tmp/land3-adj6/ira.json`. The deepseek log is dormant and not ruled.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | ira.both_kinds | representation | 2,585/2,591 agree; 6 candidate-unknown; completed: none | i1040gi p. 95, Line 20 | Return-wide reading on both sides (amb.2025.ira_both_kinds); differences are the unasked ira_trad amount. |
| claude | transcription | ira.over_comp | model error | 2,544/2,591 agree; 17 value, 13 candidate-refuses, 9 project-unknown, 6 candidate-unknown, 2 project-refuses; completed: 7 value | p590a p. 35; i1040gi p. 98, Caution | Reply transcribes the line 10 caution (the project's ira.kbh_short) for the excess-contribution screen, without the traditional-contribution condition. |
| claude | transcription | ira.special_gate | model error | 1,978/2,591 agree; 576 candidate-unknown, 24 value, 13 candidate-refuses; completed: 46 candidate-unknown, 7 value | i1040gi p. 95, "read the following list" | No traditional-contribution condition; refuses through its over_comp on returns without contributions. |
| claude | transcription | ira.line20 | model error | 1,987/2,591 agree; 572 candidate-unknown, 31 candidate-refuses, 1 project-refuses; completed: 46 candidate-unknown, 7 candidate-refuses | i1040gi p. 98, line 12 | No value differs; inherits the special_gate refusals on returns without contributions. |
| claude | transcription | (screen) (ira.special) | model error | 2,563/2,591 agree; 26 candidate-unknown, 2 value; completed: 8 candidate-unknown | i1040gi p. 95; p590a pp. 6-7, 16 | Drops the reservist repayment named in the label and adds ira.se_capital (unasked without a Schedule C). |

Counts: claude transcription model error 4, representation 1. Findings: none. Left open: none.


## Landing round (2026-11-14), class M

Lane land3-adj12 (claude-opus-5-5, judgment). Claude class M log of 2026-11-14 (subject hash equal to the current computation); `carry.py --kind classm` ruled nothing. Rulings file `/tmp/land3-adj12/ira.json`, applied with `rule.py --kind classm` (see the lane note `docs/provisional/lanes/land3-adj12.md` for whether it has been applied: the review store index for this log had not been carried into the landing tree when the rulings were written).

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | classm | classm.ira.3 — 7a | representation | dropped from the fixture | i1040gi Line 20, IRA Deduction | project retained. No one on the return made traditional IRA contributions (both persons' traditional contributions are $0.00; ira.any_trad false), and the IRA Deduction W... |
| claude | classm | classm.ira.3 — 7b | representation | dropped from the fixture | i1040gi Line 20, IRA Deduction | project retained. No one on the return made traditional IRA contributions (both persons' traditional contributions are $0.00; ira.any_trad false), and the IRA Deduction W... |

Counts: claude classm representation 2. Findings: none. Left open: none.

## Goal-1 round (2026-11-15)

Lane b1-adj-b (claude-opus-5-5, judgment; tax year 2025, us), B1 merge worktree nx-b1. Open lines of the Claude transcription log (b349202bae5e (line-scoped)), ruled against `.transcription/triage/2025/ira.json` (executable-triage-v2, log sha matches), the archived sources and `forms/2025/ira.yaml`. Rulings `/tmp/b1-adj-b/ira.json`, applied with `rule.py --kind transcription`; full text in the log and sidecar.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | (screen) (ira.special) | model error | 2,680/2,728 agree; 44 candidate-unknown, 4 value; completed: 16 candidate-unknown | i1040gi p. 95, list items 2, 5, 9; p590a pp. 6-7, 16 | Drops the reservist repayment the label names; adds item 2 and ira.se_capital, which the project carries on their own lines. |

Counts: claude transcription model error 1. Findings: none. Left open: none.

## Goal-1 coverage-expansion round (2026-11-15)

Lane xadj-e (claude-opus-5-5, judgment; tax year 2025, us), coverage-expansion merge worktree xint. Open lines of the Claude transcription log after the line-scoped round-2 review (rerun_all ran triage and carry), ruled against `.transcription/triage/2025/ira.json` (fresh for this reply), the archived sources and `forms/2025/ira.yaml`. Rulings `/tmp/xadj/e/ira.transcription.json` (retirement.taxable and amount_a amended to verbatim quotes), applied with `rule.py --kind transcription`; full text in the log and sidecar.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | ira.any_trad | representation | executable triage 2,430/2,999 agree; 559 candidate-unknown, 10 project-unknown, no value differs (completed: 6 candidate-unknown) | i1040gi p. 95, Line 20 | Same test (traditional contributions above zero); the reply sums person.ira_trad without its parent person.ira_owner, so it is unknown where the interview never asks the amount. i1040gi p. 95, Line 20. |
| claude | transcription | ira.anyone_covered | representation | executable triage 2,940/2,999 agree; 40 candidate-unknown, 10 project-unknown, 9 value (completed: 1 value; 2 completed witnesses in total) | i1040gi p. 97, worksheet lines 1a/1b; p. 96, Married persons filing separately | Every value witness is project true, reply false on a return with no traditional contribution: the reply reads worksheet lines 1a/1b, which are No without a contribution, while the project tests coverage itself. Both readers (ira.lines2to6, ira.cov_gate) also require ira.any_trad, so no value downstream differs. On a separate return both take the spouse's coverage through the same lived-apart rule (i1040gi p. 96, Married persons filing separately). |
| claude | transcription | ira.cov_gate | model error | executable triage 2,418/2,999 agree; 559 candidate-unknown, 22 value (completed: 6 candidate-unknown, 6 value) | i1040gi p. 31, Lines 6a and 6b, Exception | The reply drops the social security condition of the label ('Social security benefits, traditional IRA contributions for 2025, and you or your spouse covered'): it is true on classm.person.2, stage16.ira.i1 and i2 (ssb.any false). The deciding source is the exception of i1040gi p. 31, Lines 6a and 6b, which concerns the benefits worksheet only; a filer with no benefits is not sent to Pub. 590-A by it. |
| claude | transcription | ira.excl_gate | model error | executable triage 2,978/2,999 agree; 12 candidate-unknown, 7 project-unknown, 2 value (refused returns only) | i1040gi p. 96, Were You Covered by a Retirement Plan? (Form 2555 or 8815) | The reply encodes a different exclusion, the joint traditional-and-Roth one (i1040gi p. 95, Line 20, 'If you are filing a joint return and you or your spouse made contributions to both a traditional IRA and a Roth IRA for 2025, don't use the IRA Deduction Worksheet'), which the project carries in its own gate ira.both_kinds. This gate's label and cite are the excluded-income rule: i1040gi p. 96, 'If you were covered by a retirement plan and you file Form 2555 or 8815, or you exclude employer-provided adoption benefits, see Pub. 590-A'. |
| claude | transcription | 1a | representation | executable triage 2,329/2,999 agree; 592 candidate-unknown, 68 value, 10 project-unknown (completed: 6 candidate-unknown, 6 value; value pairs all project No, reply Yes) | i1040gi p. 97, line 1a; p. 96, Married persons filing separately | A display line: the project answers line 1a only when the worksheet is used (a traditional contribution); every value witness has none (e.g. classm.person.3, a SIMPLE plan with person.ira_owner false; triage explain of the 6a witnesses shows ira.any_trad false). With a contribution both read the same coverage, including the separate-return rule 'considered covered by a plan unless you lived apart from your spouse for all of 2025' (i1040gi p. 96). Unknowns: the reply reads person.ira_work_plan unasked. |
| claude | transcription | 2a | representation | executable triage 2,329/2,999 agree; 592 candidate-unknown, 68 value, 10 project-unknown (value pairs all project $0, reply $89,000 or $146,000) | i1040gi p. 97, line 2; skip lines 2 through 6 | Display line: the project shows zero when lines 2 through 6 are skipped (ira.lines2to6 false); every value witness has no traditional contribution (triage explain of stage14.sep.basic: ira.any_trad false). The reply's own note says the amount is computed but not shown in that case. i1040gi p. 97, IRA Deduction Worksheet, 'skip lines 2 through 6'. |
| claude | transcription | 2b | representation | executable triage 2,882/2,999 agree; 97 candidate-unknown, 11 project-unknown, 9 value (value pairs all project $0, reply $246,000, e.g. stage21.f1.lower_bound_still_decides, ira.any_trad false) | i1040gi p. 97, line 2; skip lines 2 through 6 | Display line, zero when lines 2 through 6 are skipped; the reply computes the not-covered amount regardless (its note: 'computed but unused'). i1040gi p. 97, line 2, 'Married filing jointly, enter $146,000 in both columns' with the $246,000 not-covered amount. |
| claude | transcription | 6a | representation | executable triage 2,338/2,999 agree; 593 candidate-unknown, 46 candidate-refuses, 12 value, 10 project-unknown (value pairs all project $0, reply positive) | i1040gi p. 97, line 6 | Display line, zero when lines 2 through 6 are skipped; triage explain of stage14.sep.basic (witness 21): ira.lines2to6 false through ira.any_trad false. The reply subtracts regardless of the skip. i1040gi p. 97, line 6. |
| claude | transcription | 6b | representation | executable triage 2,882/2,999 agree; 97 candidate-unknown, 11 project-unknown, 8 candidate-refuses, 1 value (value pair project $0, reply $71,339) | i1040gi p. 97, line 6 | Display line, zero when lines 2 through 6 are skipped (no traditional contribution), as 6a; the reply subtracts regardless. i1040gi p. 97, line 6, 'Subtract line 5 from line 2 in each column'. |

Counts: claude transcription representation 7, model error 2. Findings: none. Left open: none.

## Goal-1 coverage-expansion round (2026-11-15), class M

Lane xadj-e (claude-opus-5-5, judgment; tax year 2025, us). Claude class M log of the round-2 rerun (classm.py, 2026-11-15); carry.py ruled nothing (the project line changed). Rulings `/tmp/xadj/e/ira.classm.json`, applied with `rule.py --kind classm`; the model's values are dropped from the fixture.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | classm | classm.ira.2 — 1b | model error | classm.ira.2 is a joint return with no traditional IRA contribution (person.ira_owner false for both; branch ira.any_trad:false), the spouse covered through a SEP; dropped | i1040gi p. 95, Line 20; p. 97, IRA Deduction Worksheet | The IRA Deduction Worksheet is used only for traditional contributions (i1040gi p. 95, Line 20, 'If you made contributions to a traditional IRA for 2025, you may be able to take an IRA deduction'); the project's display lines 1a through 6 then read No and zero (ira.lines2to6 false) and lines 11 and 12 are $0, as the model's are. The model filled the worksheet as if it were used (1b Yes); its value is not evidence for the line as defined. |
| claude | classm | classm.ira.2 — 2a | model error | classm.ira.2 is a joint return with no traditional IRA contribution (person.ira_owner false for both; branch ira.any_trad:false), the spouse covered through a SEP; dropped | i1040gi p. 95, Line 20; p. 97, IRA Deduction Worksheet | The IRA Deduction Worksheet is used only for traditional contributions (i1040gi p. 95, Line 20, 'If you made contributions to a traditional IRA for 2025, you may be able to take an IRA deduction'); the project's display lines 1a through 6 then read No and zero (ira.lines2to6 false) and lines 11 and 12 are $0, as the model's are. The model filled the worksheet as if it were used (2a $246,000); its value is not evidence for the line as defined. |
| claude | classm | classm.ira.2 — 2b | model error | classm.ira.2 is a joint return with no traditional IRA contribution (person.ira_owner false for both; branch ira.any_trad:false), the spouse covered through a SEP; dropped | i1040gi p. 95, Line 20; p. 97, IRA Deduction Worksheet | The IRA Deduction Worksheet is used only for traditional contributions (i1040gi p. 95, Line 20, 'If you made contributions to a traditional IRA for 2025, you may be able to take an IRA deduction'); the project's display lines 1a through 6 then read No and zero (ira.lines2to6 false) and lines 11 and 12 are $0, as the model's are. The model filled the worksheet as if it were used (2b $146,000); its value is not evidence for the line as defined. |

Counts: claude classm model error 3. Findings: none. Left open: none.
