# Adjudication — refund

Method: `README.md` in this directory. Triage record: `../triage/refund.deepseek.json`
(executable-triage-v1; 1,083 fixtures, 500 generated returns, seed 20261026, 295 partial records over
17 bases). DeepSeek family only. Full ruling text is in the log and its sidecar.

## Backlog round (2026-11-03)

Fresh reviews of 2026-11-03 (claude-opus-5-5 and deepseek-flash) after the backlog packages; the change record of this form's package is `research/audits/credits-misc/PROPOSED_BUGS.md`. Triage: `../triage/<stem>.json`, executable-triage-v2 rerun 2026-11-03 for these stems (1,495 fixtures, 500 generated returns seed 20261026, 40 partial bases), with every completed-return witness enumerated by an uncapped scratch rerun where a ruling counts them. Full ruling text: `.transcription/proposed/bklg/{transcription,render}.refund[.<family>].json`. The refund change is PENDING-5: `refund.not_2024` and the `refund.taxable` remedy add tax paid "before 2024"; wording only, a screen that refuses on Yes. Every partial base of the bank has no refund, so their differences are on lines `s1.line1` never reads; the refund-return witnesses are the stage16 mutation and refusal fixtures named in the rulings. No value difference on any record. Class M: no open section.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | refund.taxable | model error and scope | 2,552 of 2,635 agree; completed: 44 project-unknown | i1040gi p. 88, TIP; p. 90, lines 3 and 6 | Choice is the project's; differences inherited from lines 6 and 9, or on no-refund bases. |
| claude | transcription | 6 | model error | 2,514 of 2,635 agree; completed: 44 candidate-unknown, 22 project-unknown | i1040gi p. 90, line 6 and footnote; p. 33 | Spouse boxes needed for every status (stage16.mut.refund_single_unasked). |
| claude | transcription | 8 | model error | 2,554 of 2,635 agree; completed: 44 candidate-unknown | i1040gi p. 90, Note and line 8 | Own logic equal; inherited from line 6. |
| claude | transcription | 9 | model error | 2,310 of 2,635 agree; completed: 176 candidate-unknown | i1040gi p. 90, lines 3 and 9 | Needs line 8 after the line 3 STOP (stage16.mut.refund_line3_stop); reclassified from "equivalent". |
| claude | render | 1 | ambiguity and scope | MISMATCH | i1040gi pp. 89-90, Exception; line 1 | Exceptions 1 and 5 refused by refund.not_2024 on refund.taxable; cap is amb.2025.refund_cap_5d. |
| claude | render | 6 | representation | UNCLEAR | i1040gi p. 90, line 6 | Per-box helpers sum to boxes times the amount; MFS condition in the questions. |
| deepseek | transcription | refund.has | model error | 848 of 2,380 agree; completed: 254 candidate-unknown | i1040gi p. 88, Line 1 | Redefined as line 9 above zero. |
| deepseek | transcription | refund.taxable | model error and scope | 2,216 of 2,380 agree; completed: 91 candidate-unknown | i1040gi p. 88, TIP; p. 90 | Inherited from lines 6 and 9; line5e_bad refusal is scope. |
| deepseek | transcription | 1 | representation and scope | 2,263 of 2,380 agree; completed: 39 candidate-unknown, 13 project-unknown | i1040gi p. 90, line 1 | Same cap where the worksheet is used; gate placement on refused returns. |
| deepseek | transcription | 2 | representation and scope | 2,310 of 2,380 agree; completed: 26 project-unknown, 13 candidate-unknown | i1040gi p. 90, line 2 | Same where used; line5e_bad refusal. |
| deepseek | transcription | 4 | representation | 2,334 of 2,380 agree; completed: 13 candidate-unknown, 13 project-unknown | i1040gi p. 90, line 4 | Same where used; zero otherwise. |
| deepseek | transcription | 6 | model error | 2,310 of 2,380 agree; completed: 26 candidate-unknown, 13 project-unknown | i1040gi p. 90, line 6 | As Claude line 6. |
| deepseek | transcription | 8 | model error | 2,287 of 2,380 agree; completed: 39 candidate-unknown, 13 project-unknown | i1040gi p. 90, line 8 | Inherited from line 6. |
| deepseek | transcription | 9 | model error | 2,122 of 2,380 agree; completed: 104 candidate-unknown, 26 project-unknown | i1040gi p. 90, line 3 | Needs line 8 after the STOP. |
| deepseek | render | 1 | scope | MISMATCH | i1040gi p. 89, Exception | As Claude. |
| deepseek | render | 6 | representation | MISMATCH | i1040gi p. 90, line 6 | As Claude. |

## Round 1 (superseded subject)

| family | line | class | triage | deciding source | reason |
| --- | --- | --- | --- | --- | --- |
| deepseek | refund.has | model error | 870/1,878 agree; 981 candidate-unknown, 17 project-unknown, 6 value, 4 candidate-refuses | i1040gi p. 88, Line 1, "If you received a refund, credit, or offset" | Redefines "a refund was received" as "line 9 is positive", so it asks the itemizing questions on returns with no refund. |
| deepseek | refund.taxable | model error | 1,841/1,878 agree; 34 project-unknown, 2 candidate-unknown, 1 project-refuses | f1099g p. 5, Box 8, "If taxable, report the amount in box 2 on Schedule C or F"; i1040gi p. 88, TIP | Skips the box 8 and other-year questions when 2024 deductions were not itemized, though neither depends on 2024 itemizing (amb.2025.refund_exceptions). |
| deepseek | 1 | representation | 1,791/1,878 agree; 51 candidate-unknown, 34 project-unknown, 2 candidate-refuses | i1040gi p. 90, worksheet line 1 | Same smaller-of on the worksheet path; the differences are partial records off that path or returns the project refuses on refund.taxable. |
| deepseek | 2 | representation | 1,826/1,878 agree; 34 project-unknown, 17 candidate-unknown, 1 project-refuses | i1040gi p. 90, worksheet line 2 | Same subtraction on the worksheet path; the project refusal is the cited impossible-entry screen on line 5e (i1040sca p. 7). |
| deepseek | 4 | representation | 1,844/1,878 agree; 17 candidate-unknown, 17 project-unknown | i1040gi p. 90, worksheet line 4 | Same entry where the worksheet is used; the differences are partial records off the worksheet path. |
| deepseek | 6 | model error | 1,826/1,878 agree; 35 candidate-unknown, 17 project-unknown | i1040gi p. 90, line 6 footnote; p. 33, "Don't check any boxes for your spouse if your filing status is head of household" | Asks the spouse boxes of single and head of household filers. |
| deepseek | 8 | model error | 1,809/1,878 agree; 52 candidate-unknown, 17 project-unknown | i1040gi p. 90, Note and line 8 | Own logic is equivalent; it inherits the line 6 spouse questions on a reachable single return (stage16.mut.refund_single_unasked). |
| deepseek | 9 | model error | 1,771/1,878 agree; 85 project-unknown, 19 candidate-unknown, 2 candidate-refuses, 1 project-refuses | i1040gi p. 90, line 3, "No. STOP None of your refund is taxable" | Ignores the line 3 STOP and needs the 2024 filing status after it (stage16.mut.refund_line3_stop). |

Findings: none. Project lines unchanged.

## Fix round 2 (superseded subject)

Fresh reviews of 2026-10-30 (claude-opus-5-5 and deepseek-flash, transcription and render) of the subject after BUG-0230
(`refund.not_2024` asks about any 2024 tax paid in 2025) and BUG-0251 (`refund.box8` asks about any business-only income
tax refund, with or without a Form 1099-G); no expression changed. Triage `../triage/refund[.deepseek].json`
(executable-triage-v2; 1,382 fixtures, 500 generated returns seed 20261026, 640 / 445 partial records from 40 bases, all
without a refund; 2,522 / 2,327 comparisons per line), every witness enumerated by an uncapped scratch rerun. No value
difference on a completed return reaches a printed amount (the 4 completed `refund.has` values leave Schedule 1 line 1 at
$0.00 on both sides). Class M log: no open section. Full ruling text:
`.transcription/proposed/fixr2/{transcription,render}.refund[.deepseek].json`.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | refund.taxable | representation and scope | 1,242 agree; 1,239 project-unknown (524 completed), all with no refund; 40 candidate-unknown (refund.received); 1 project-refuses (line5e_bad) | i1040gi p. 88, TIP; f1099g p. 5, Box 8 | Same choice and same gates; s1.line1 never reads the line without a refund. |
| claude | transcription | 6 | representation | 2,482 agree; 40 project-unknown (refund.status withheld, no box checked) | i1040gi p. 90, line 6 and footnote; p. 33 | Spouse boxes now only for joint or separate, as the project; per-box sum equals count times rate. |
| claude | transcription | 8 | representation | 2,522 / 2,522 agree | i1040gi p. 90, Note and line 8 | Equivalent. |
| deepseek | transcription | refund.has | model error | 1,034 agree; 6 value (4 completed: stage16.refund.f1, f2, f4, f7, true vs false, Schedule 1 line 1 $0 both); 1,256 candidate-unknown | i1040gi p. 88, Line 1 | Redefines "a refund was received" as "line 9 is positive". |
| deepseek | transcription | refund.taxable | model error and scope | 2,270 agree; 56 candidate-unknown (2 fixtures need refund.mfs_spouse_itemized); 1 project-refuses | i1040gi p. 88, TIP; p. 90, line 3 | Box 8 and other-year now asked of every refund; inherits lines 8 and 9. |
| deepseek | transcription | 6 | model error and scope | 2,133 agree; 163 candidate-unknown (stage16.mut.refund_single_unasked); 4 candidate-refuses | i1040gi p. 90, line 6 footnote; p. 33 | Spouse boxes asked of single and head of household filers. |
| deepseek | transcription | 8 | model error and scope | 2,133 agree; 190 candidate-unknown (stage16.mut.refund_single_unasked, $1,400 project); 4 candidate-refuses | i1040gi p. 90, Note | Spouse-itemized question asked of every status. |
| deepseek | transcription | 9 | model error and scope | 2,160 agree; 83 candidate-unknown (refund_line3_stop, refund_single_unasked); 81 project-unknown (no refund); 2 candidate-refuses; 1 project-refuses | i1040gi p. 90, line 3 STOP | Ignores the line 3 STOP; inherits line 8. |
| claude | render | 1 | ambiguity and scope | - | i1040gi p. 90, line 1; p. 89, exceptions 1, 2, 5 | 5d cap is amb.2025.refund_cap_5d; exceptions refused by refund.not_2024 on refund.taxable and scope.schedule1. |
| claude | render | 6 | representation | - | i1040gi p. 90, line 6 | Rate is in refund.per_box's label; MFS footnote in the spouse questions. |
| deepseek | render | 1 | scope | - | i1040gi p. 89, exceptions 1, 2, 5 | As the Claude render ruling. |
| deepseek | render | 6 | representation | - | i1040gi p. 90, line 6 footnote | MFS conditions are in the spouse questions. |

Findings: none. Errors introduced by the fixes: none found; both rewordings are wider than before (safe direction).

## Fix round 5 (superseded subject)

The render logs (claude-opus-5-5 and deepseek-flash) were rerun on 2026-10-30 because the rendered English of `refund`
changed through a shared line. The refund form and its transcription were not changed or rerun, so fix round 2's
transcription rows stand. The open render lines are 1 and 6 in both families. Their restatements match fix round 2's
word for word, and the objections are the same. Fix round 2's rulings were rechecked against the current
`refund.not_2024`, `refund.received`, `scope.schedule1`, `refund.per_box` and spouse questions and the register. The
Claude line-6 reply also asks why the spouse boxes are zero for a qualifying surviving spouse; amb.2025.refund_boxes_2024
records that reading. Full ruling text: `.transcription/proposed/fixr5/render.refund[.deepseek].json`.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | render | 1 | ambiguity and scope | render MISMATCH | i1040gi p. 90, line 1; p. 89, exceptions 1, 2, 5 | 5d cap is amb.2025.refund_cap_5d; exceptions refused by refund.not_2024 on refund.taxable and scope.schedule1. |
| claude | render | 6 | representation | render UNCLEAR | i1040gi p. 90, line 6; p. 33; amb.2025.refund_boxes_2024 | Rate in refund.per_box; MFS footnote in the spouse questions; no spouse boxes on a qss return. |
| deepseek | render | 1 | scope | render MISMATCH | i1040gi p. 89, exceptions 1, 2, 5 | As the Claude render ruling. |
| deepseek | render | 6 | representation | render MISMATCH | i1040gi p. 90, line 6 footnote | MFS conditions are in the spouse questions. |

Findings: none.

## Landing round (2026-11-14)

Lane land3-adj5, interview redraft landing. Open lines of the Claude pass 643525b6700d, ruled on `.transcription/triage/2025/refund.json` (executable-triage-v2; 3,206 comparisons per line) and the sources. Rulings `/tmp/land3-adj5/refund.json`.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | refund.taxable | representation | 2,584/3,206 agree; no value; 66 project-unknown on completed returns with no refund (refund.box8 unasked) | i1040gi p. 88, Line 1 | Same zero-or-line-9 rule; Schedule 1 line 1 reads it only when refund.has. |
| claude | transcription | 1 | representation | 3,002/3,206; 2 value, both mutation.t2.refund.not_itemized (incomplete; worksheet not used); 60 candidate-unknown completed | i1040gi p. 90, worksheet line 1 | Same cap; the project reads the refund through refund.received_if_worksheet. |

Counts: representation 2.

Findings: none.

## Landing round (2026-11-14), render

Lane land3-adj7 (claude-opus-5-5, judgment). Open lines of the Claude render log `.transcription/logs/2025/render/refund.md`, ruled on the rendered English (`rendered/2025/refund.md`), the form YAML and the cited source; the deepseek log is dormant and not ruled.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | render | 1 | ambiguity and scope | MISMATCH; form YAML, register | i1040gi pp. 89-90; amb.2025.refund_cap_5d, amb.2025.refund_exceptions | Exceptions 1 and 5 refused by refund.not_prior_year on refund.taxable; cap at 2024 line 5d is the chosen reading. Same as earlier rounds. |

Counts: claude render: ambiguity and scope 1.

Findings: none. No line left open.

## Goal-1 round (2026-11-15)

Lane b1-adj-c (claude-opus-5-5, judgment; tax year 2025, us), goal-1 merge B1 (worktree nx-b1). Open lines of the Claude transcription pass 0e1ac073bd9b, ruled on `.transcription/triage/2025/refund.json` (3,291 comparisons per line), the form YAML and i1040gi. Rulings `/tmp/b1-adj-c/refund.transcription.json`.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | refund.taxable | representation | 2,611/3,291 agree; no value; 100 project-unknown on completed returns with no refund | i1040gi p. 88, Line 1; amb.2025.refund_two_returns | Same zero-or-line-9 rule; Schedule 1 line 1 reads it only when refund.has. |
| claude | transcription | 1 | representation | 2,602/3,291; no value; 101 project-unknown completed where the reply's line is hidden | i1040gi p. 90, worksheet line 1 | Same cap; project reads the refund through refund.received_if_worksheet. |

Counts: representation 2. Findings: none.

## Goal-1 round (2026-11-15), render

Lane b1-adj-c. Rulings `/tmp/b1-adj-c/refund.render.json`.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | render | 1 | ambiguity | MISMATCH; form YAML, register | i1040gi pp. 89-90; amb.2025.refund_two_returns, amb.2025.refund_cap_5d | Two-returns zero and the 5d cap are chosen readings; exceptions 1 and 5 refused by refund.not_prior_year on refund.taxable. |
| claude | render | 6 | representation | UNCLEAR; refund.per_box, spouse questions | i1040gi p. 90, line 6 | Amount helpers are per_box when checked; MFS condition in the spouse questions. |

Counts: claude render: ambiguity 1, representation 1. Findings: none. No line left open.

## Goal-1 coverage-expansion round (2026-11-15)

Lane xadj-e (claude-opus-5-5, judgment; tax year 2025, us), coverage-expansion merge worktree xint. Open lines of the Claude transcription log after the line-scoped round-2 review (rerun_all ran triage and carry), ruled against `.transcription/triage/2025/refund.json` (fresh for this reply), the archived sources and `forms/2025/refund.yaml`. Rulings `/tmp/xadj/e/refund.transcription.json` (retirement.taxable and amount_a amended to verbatim quotes), applied with `rule.py --kind transcription`; full text in the log and sidecar.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | refund.received_if_worksheet | representation | executable triage 2,974/3,633 agree, 614 project-unknown, 45 candidate-unknown, no value differs (completed: 190 project-unknown, 1 candidate-unknown) | i1040gi p. 88, Line 1 (none taxable without 2024 itemizing) | The reply's zero branch tests refund.any, the project's refund.worksheet does not; every witness is a return with refund.any false where the project leaves refund.itemized or refund.two_returns unasked, and no reader reaches the line on such a return (refund.received is gated by it; refund.line1 and rec read it only on the refund path). i1040gi p. 88, Line 1: 'None of your refund is taxable if, in the year you paid the tax, ... you either (a) didn't itemize deductions, or (b) elected to deduct state and local general sales taxes' - both expressions give that zero where it applies. |
| claude | transcription | refund.taxable | model error | executable triage 3,274/3,633 agree; 186 project-unknown, 165 candidate-unknown, 5 project-refuses, 3 value (completed: 3 value) | i1040gi p. 88, Line 1 exceptions (see Pub. 525); p525 Example 31, Worksheet 2 | The three value witnesses are the Pub. 525 Worksheet 2 fixtures rec.ex31_allocation (project $300, reply $500), rec.salt_cap_partial (project $666.67, reply $0) and rec.allocation_rounding (project $200, reply $800). The reply always takes the i1040gi worksheet line 9 and drops the recovery path; i1040gi p. 88: 'See Itemized Deduction Recoveries in Pub. 525 instead of using the State and Local Income Tax Refund Worksheet ... if ... You received a refund other than an income tax refund, such as a general sales tax or real property tax refund'. rec.ex31_allocation reproduces Pub. 525 Example 31 (line A 20%, line B $300 to Schedule 1 line 1), which the project's switch to rec.to_line1 gives. The unknowns are the same rec-path inputs read on returns that do not reach them. |

Counts: claude transcription representation 1, model error 1. Findings: none. Left open: none.

## Goal-1 coverage-expansion round (2026-11-15), render

Lane xadj-e (claude-opus-5-5, judgment; tax year 2025, us). Claude render log of the round-2 rerun (whole; render_compare.py via rerun_all), ruled against `rendered/2025/refund.md`, the cited i1040gi text, `forms/2025/refund.yaml` and the ambiguity register. Rulings `/tmp/xadj/e/refund.render.json`.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | render | 1 | ambiguity | render MISMATCH | i1040gi p. 90 worksheet line 1; p. 89 exceptions; amb.2025.refund_cap_5d | The cap is the registered ambiguity amb.2025.refund_cap_5d: i1040gi p. 90, worksheet line 1, 'But don't enter more than the amount of your state and local income taxes shown on your 2024 Schedule A, line 5d'; line 5d is the total of 5a, 5b and 5c, and the project chose the cap as printed (line 5d), the reply the income tax part. The exceptions the reply names are not omitted: 1 ('a refund in 2025 that is for a tax year other than 2024') and 5 ('You made your last payment of 2024 estimated state or local income tax in 2025') refuse at refund.not_prior_year (remedy: Pub. 525), and 2 ('a refund other than an income tax refund') is now computed by Pub. 525 Worksheet 2 (rec, refund.taxable), as i1040gi p. 89 directs; line 1's own refusals are only those the worksheet itself raises (refund.exc_tax, refund.exc_who). |
| claude | render | 6 | representation | render UNCLEAR | i1040gi p. 90 worksheet line 6 and footnote | The four helpers are defined lines rendered by label (refund.amt_you_born, amt_you_blind, amt_spouse_born, amt_spouse_blind: $1,550 or $1,950 per box checked), so line 6 is 'Multiply the number of boxes checked by $1,550 ($1,950 if your 2024 filing status was single or head of household)'. The married-filing-separately condition of the worksheet footnote ('you can check the boxes for your spouse only if your spouse had no income, isn't filing a return, and can't be claimed as a dependent on another person's return', i1040gi p. 90) is in the spouse-box questions themselves (refund.spouse_born, refund.spouse_blind); a 2024 qualifying surviving spouse return has no spouse on it, so its spouse boxes are zero (refund.spouse_boxes; amb.2025.refund_boxes_2024). |

Counts: claude render ambiguity 1, representation 1. Findings: none. Left open: none.
