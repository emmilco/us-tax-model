# Adjudication — sa

Method: `README.md` in this directory. Triage records: `../triage/sa.json`,
`../triage/sa.deepseek.json` (executable-triage-v1; 1,083 fixtures, 500 generated returns,
seed 20261026, 537 partial records). Full ruling text is in each log and its sidecar (proposed in
`.transcription/proposed/sa.json` and `sa.deepseek.json`).

## Backlog round (2026-11-03)

Fresh reviews of 2026-11-03 (claude-opus-5-5 and deepseek-flash, and gpt-6-astra for the transcription) after the backlog packages; the change record of this form's package is `research/audits/ptc-sa/PROPOSED_BUGS.md`. Triage: `../triage/<stem>.json`, executable-triage-v2 rerun 2026-11-03 for these stems (1,495 fixtures, 500 generated returns seed 20261026, 40 partial bases), with every completed-return witness enumerated by an uncapped scratch rerun where a ruling counts them. Full ruling text: `.transcription/proposed/bklg/{transcription,render}.sa[.<family>].json`. The sa changes are PENDING-2 and PENDING-4 (wording of `sa.line1`, `sa.line5a` to `sa.line5c`); no expression changed. Line 9 now reads `f4952.line8`, gated on `f4952.used` by PENDING-6 of credits-misc. Completed-return value differences: `sa.age65` (Claude 17, deepseek 16; the candidates' readings), and `sa.itemizes`/`sa.deduction` only on `classm.f5695.8.deepseek`, a single record answering the married-filing-separately question Yes. Class M: no open section.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | sa.age65 | model error | 2,427 of 2,521 agree; completed: 17 value | f1040s1a line 36a; i1040gi p. 33 | Reads any line 12d box for a question about you (17 completed value witnesses). |
| claude | transcription | sa.itemizes | model error | 1,392 of 2,521 agree; completed: 170 candidate-unknown, 3 candidate-refuses, 3 value | i1040gi pp. 14, 33; i1040sca p. 11 | Spouse-itemizes without MFS; gambling losses without winnings; value only on an unreachable single record. |
| claude | transcription | sa.deduction | model error | 1,388 of 2,521 agree; completed: 171 candidate-unknown, 3 candidate-refuses, 2 value | i1040gi p. 34 | Inherited from sa.itemizes and line 16. |
| claude | transcription | 16 | model error | 1,035 of 2,521 agree; completed: 144 candidate-unknown | i1040sca p. 11, Line 16 | Needs gambling losses without winnings. |
| claude | render | 1 | scope | MISMATCH | i1040sca p. 2, Line 1 | The claimable-filer person is unreachable: sa.dependent refuses. |
| claude | render | 9 | representation | UNCLEAR | f4952 p. 3, Who Must File | A filer under the exception still has line 1 above zero, so line 8 is computed. |
| deepseek | transcription | sa.age65 | model error | 2,475 of 2,520 agree; completed: 16 value | f1040s1a line 36a | Counts the spouse (16 completed value witnesses). |
| deepseek | transcription | sa.itemizes | model error | 1,374 of 2,520 agree; completed: 165 candidate-unknown, 13 candidate-refuses, 1 value | i1040gi p. 33, death of spouse; p. 14; i1040sca p. 11 | No died-before-65 rule; spouse-itemizes without MFS; gambling losses. |
| deepseek | transcription | sa.deduction | model error | 1,369 of 2,520 agree; completed: 165 candidate-unknown, 13 candidate-refuses, 1 value | i1040gi p. 34 | Inherited. |
| deepseek | transcription | 5e | scope | 2,463 of 2,520 agree; completed: none | i1040sca p. 7, worksheet line 10 | Same amount; its excluded-income refusal on refused returns. |
| deepseek | transcription | 16 | model error | 1,027 of 2,520 agree; completed: 143 candidate-unknown | i1040sca p. 11 | As Claude. |
| deepseek | transcription | 9 | interface gap | 2,304 of 2,520 agree; completed: 13 candidate-refuses, 13 candidate-unknown | f4952 p. 3; i1040sca p. 9 | Rebuilds line 8 from lines 3 and 6 (pre-PENDING-6 screens); pages lacked Form 4952 and i1040sca p. 9. |
| deepseek | render | 1 | scope | MISMATCH | i1040sca p. 2, Line 1 | As Claude. |
| deepseek | render | 2 | ambiguity | MISMATCH | Schedule A line 2 | amb.2025.sa_medical_negative_agi. |
| gpt | transcription | sa.itemizes | model error | 1,397 of 2,521 agree; completed: 155 candidate-unknown, 3 candidate-refuses | i1040sca p. 11 | Selection equal; gambling losses without winnings; sa.spouse_extra on single records. |
| gpt | transcription | sa.deduction | model error | 1,385 of 2,521 agree; completed: 155 candidate-unknown, 3 candidate-refuses | i1040gi p. 34 | Inherited. |
| gpt | transcription | 5e | scope | 2,162 of 2,521 agree; completed: none | i1040sca p. 7, worksheet line 10 | Same amount; refusals only. |
| gpt | transcription | 16 | model error | 1,029 of 2,521 agree; completed: 142 candidate-unknown | i1040sca p. 11 | As Claude. |

## Earlier rounds (superseded subject)

| family | line | class | triage | deciding source | reason |
| --- | --- | --- | --- | --- | --- |
| claude | sa.age65 | model error | 2,070/2,120 agree; 50 value | f1040s1a lines 36a–36b; i1040gi p. 33, line 12d | Counts the spouse in a question about you, which would give the taxpayer the senior deduction on line 36a. |
| claude | sa.itemizes | model error | 1,270/2,120 agree; 790 candidate-unknown, 59 candidate-refuses, 1 project-refuses | i1040sca p. 11, gambling losses; Schedule A line 18 | Comparison matches, but its line 17 needs gambling losses with no winnings; refusals are MFS (refused by scope.ready) or gates the project hits on sa.deduction. |
| claude | sa.deduction | model error | 1,285/2,120 agree; 799 candidate-unknown, 35 candidate-refuses, 1 project-refuses | i1040gi p. 34, line 12e; i1040sca p. 11 | Same selection; line 12e unknown wherever its line 16 needs unneeded losses; no value differences. |
| claude | 5e | scope | 2,006/2,120 agree; 52 candidate-refuses, 53 candidate-unknown, 9 project-refuses | i1040sca p. 7, SALT worksheet lines 1–10 | Formula agrees on every return; differences are excluded-income and unsupported screens placed on 5d/5e instead of line 17. |
| claude | 16 | model error | 879/2,120 agree; 1,116 candidate-unknown, 91 project-refuses, 34 project-unknown | i1040sca p. 11; amb.2025.gambling_losses | Unguarded smaller_of needs gambling losses when there are no winnings and the line is zero; project's extra line-16 screens are also on line 17. |
| deepseek | sa.age65 | model error | 2,066/2,120 agree; 54 value | f1040s1a lines 36a–36b | Counts any person's age box for a question about you. |
| deepseek | sa.itemizes | model error | 1,178/2,120 agree; 13 value, 814 candidate-unknown, 43 candidate-refuses, 69 project-refuses, 3 project-unknown | i1040gi p. 33, line 12d; p501 p. 23 | Counts people not boxes, ignores died-before-65, and compares its own wrong line 17 (lines 9, 12, 16). |
| deepseek | sa.deduction | model error | 987/2,120 agree; 226 value, 823 candidate-unknown, 32 candidate-refuses, 52 project-refuses | i1040gi pp. 33–34, lines 12d–12e | Both amounts it chooses between are wrong as ruled at sa.itemizes. |
| deepseek | 5e | model error | 2,032/2,120 agree; 4 value (all MFS), 51 candidate-refuses, 24 candidate-unknown, 9 project-refuses | i1040sca p. 7, SALT worksheet line 1 | Halves $40,000 at line 1 and again at line 10 for MFS; MFS is refused by every interview, so no in-scope amount differs. |
| deepseek | 16 | model error | 879/2,120 agree; 1,116 candidate-unknown, 91 project-refuses, 34 project-unknown | i1040sca p. 11; amb.2025.gambling_losses | As in the Claude log. |
| deepseek | 9 | interface gap | 1,485/2,120 agree; 635 value | f4952 lines 7–8; i1040sca p. 9 | Copies Form 4952 line 7 (carryforward) instead of line 8; no Form 4952 page or line 9 instruction was given and the interface entries are unlabeled. |
| deepseek | 12 | model error | 1,367/2,120 agree; 401 value, 197 project-refuses, 155 project-unknown | i1040sca p. 10, line 12 | Enters zero claiming no gift input, though the gift collection is in its interface. |

Findings: none. Project lines unchanged.

## Landing round (2026-11-14)

The interview redraft's line-scoped Claude review (pass a4485d8179f7) of sa.itemizes, sa.deduction and lines 5a, 5b,
8a, 11, 12 and 16, ruled by the land3-adj5 lane against `.transcription/triage/2025/sa.json` (executable-triage-v2;
3,708 comparisons; not rebuilt). No line shows a value difference; the differences are unknowns from parent questions
the reply reads around (the separate-return questions, the home and gift parents) and refusal placement. Rulings in
`/tmp/land3-adj5/sa.json`, applied with rule.py.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | sa.itemizes | representation | 3,046/3,708 agree; no value; candidate-unknown 41 completed (`sa.spouse_extra` read for every filer) | i1040sca p. 1, "your federal income tax will be less if you take the larger of your itemized deductions or your standard deduction"; p. 12, Line 18 | Same three reasons to itemize and the same tie rule; the reply ignores the separate-return parents. |
| claude | transcription | sa.deduction | representation | 3,030/3,708 agree; no value; follows sa.itemizes | f1040 line 12e | Line 17 or the standard deduction, as the project. |
| claude | transcription | 5a | finding (low) | 3,620/3,708 agree; no value in the sample; candidate-refuses 10 (sales tax election refused on this line) | i1040sca p. 3, Line 5a ("State and local estimated tax payments made during 2025", "taxes paid in 2025 for a prior year") | The project's sum of withholding (`sa.line5a`) and other payments (`sa.state_tax_other`) is right as the interview asks it, but `sa.line5a`'s label and source still describe the whole total, so read as declared the sum double-counts (BUG-0632). |
| claude | transcription | 5b | representation | 3,686/3,708 agree; no value; project-unknown 22 only | f1040sa line 5b; i1040sca p. 6, Line 5b | The project asks 5b under `sa.home_asked`; the reply reads the inputs directly. |
| claude | transcription | 8a | representation | 3,566/3,708 agree; no value; candidate-unknown 15 completed (`s3.mcc` in its refusal helper) | i1040sca p. 8, Line 8a | Same amount; the reply reads `sa.home_other` also of an owner. |
| claude | transcription | 11 | representation | 3,666/3,708 agree; no value; candidate-refuses 24 (limited-charity refusal placed here) | f1040sa line 11 | Same amount; the project refuses that case on lines 12 and 16. |
| claude | transcription | 12 | representation | 3,250/3,708 agree; no value; unknowns and refusal placement | f1040sa line 12 | Same sum of `gift.allowed`. |
| claude | transcription | 16 | representation | 3,367/3,708 agree; no value; unknowns and refusal placement | i1040sca p. 11, "only to the extent of gambling winnings reported on Schedule 1 (Form 1040), line 8b" | Same smaller-of; 0 without winnings either way. |

Counts: 7 representation, 1 finding (low). Finding BUG-0632 (`bug_pending/land3-adj5-02.md`): fix the
label and input source of `sa.line5a` (W-2 boxes 17 and 19 only), move the other payments' text to
`sa.state_tax_other`'s source, and narrow `sa.state_tax_any`'s text to tax taken out of pay.
Citation corrections to the ruling texts as written in the log: the sa.itemizes quote is "your federal income tax will
be less" (i1040sca p. 1); Line 5b is on i1040sca p. 6 (not p. 4) and the gambling-loss rule on p. 11 (not p. 12).

## Landing round (2026-11-14), render

Line-scoped Claude render review, pass 4bc7a200f1c1. `carry.py --kind render` ruled nothing. Ruled by lane land3-adj9;
rulings in `/tmp/land3-adj9/sa.json`, applied with rule.py.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | render | 1 | scope | MISMATCH; fifth category of people omitted | i1040sca p. 2, Line 1 | As before: a filer who can be claimed as a dependent is refused by `sa.dependent` on sa.standard and sa.deduction. |
| claude | render | 5a | finding (medium) | MISMATCH; withheld amount plus other taxes counted twice as encoded | i1040sca Line 5a | `sa.line5a`'s source still asks for every state income tax; the interview prompts are right. The ruling cites BUG-0636, a duplicate of BUG-0632 (transcription lane), found after the ruling was applied. |
| claude | render | 8a | finding (low) | MISMATCH; no share rule, no Form 8396 subtraction | i1040sca Line 8a, "deduct only your share of the interest" | Form 8396 refused by `s3.mcc_if_interest`; the co-borrower's share is the open BUG-0459. |
| claude | render | 6 | scope | MISMATCH; no refusal for the GST deduction | i1040sca Line 6, "generation-skipping tax (GST) imposed on certain income distributions" | The GST is on trust income distributions, reported on a Schedule K-1 (Form 1041); `scope.k1` refuses through scope.schedule1. |
| claude | render | 15 | finding (low) | MISMATCH; no question behind sa.unsupported asks about a casualty | i1040sca Line 15 | Value right (`sd.casualty` through sd.other_forms); the refusal on lines 6, 15, 16 still names Form 4684. BUG-0639. |
| claude | render | 16 | scope | MISMATCH; other line 16 items not refused | i1040sca Line 16 list | Casualty by `sd.casualty`, claim of right by `s3.repaid_income`, the rest by their own questions. |

6 lines: 3 scope, 3 finding (1 medium, 2 low). Findings: line 5a, BUG-0632 (already recorded by the
transcription lane; this lane rates it medium because fixtures and other readers use the encoded text; the ruling's
BUG-0636 duplicates it and should be dropped before `new_bug.py --assign`, with the ruling's reference
read as BUG-0632); line 8a, the
open BUG-0459; line 15, BUG-0639 (`bug_pending/land3-adj9-04.md`): drop "/ Form 4684" from the
sa.unsupported refusal on lines 6, 15 and 16 and name sd.casualty in line 15's citation.

## Landing round (2026-11-14), after the sa text fix

Subject after lane land3-sa (BUG-0632 and BUG-0639: `sa.line5a` limited to W-2 boxes 17 and
19, `sa.state_tax_any` relabelled, the `sa.unsupported` refusal renamed, line 15 re-cited). Last review of this round
for sa. Claude transcription pass 51a9b88c8eed (line 16), triage `.transcription/triage/2025/sa.json`
(executable-triage-v2, 3,717 comparisons; carry ruled nothing). Claude render pass e804cc14a78b (lines 6, 8b, 8c, 13,
15, 16). Rulings in `/tmp/land3-adj14/sa.transcription.json` and `/tmp/land3-adj14/sa.render.json` (lane land3-adj14).

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | 16 | representation | 2,735/3,717 agree; no value; 733 candidate-unknown (gambling losses read ungated), 61 project-refuses, 1 candidate-refuses (s3.repaid_income) | i1040sca p. 11, "only to the extent of gambling winnings reported on Schedule 1 (Form 1040), line 8b" | Same smaller-of; 0 without winnings either way; the other list items are refused elsewhere. |
| claude | render | 6 | scope | MISMATCH; no refusal for the GST deduction | i1040sca Line 6 | As before: GST on a trust's income distribution comes with a Schedule K-1 (Form 1041); `scope.k1` refuses. |
| claude | render | 15 | scope | MISMATCH; no listed refusal covers a casualty | i1040sca p. 11, Line 15; mutation.json (gate sd.other_forms) | `sd.casualty`, asked of every filer, refuses through sd.other_forms; the line's citation now says so. |
| claude | render | 16 | scope | MISMATCH; casualty, claim of right, disaster loss not refused | i1040sca p. 11, Line 16 list; p525 p. 36 | `sd.casualty`, `s3.repaid_income` and `sa.unsupported` refuse them. |

4 lines: transcription 1 representation; render 3 scope. Findings: none.

## Goal-1 round (2026-11-15)

Lane b1-adj-a (claude-opus-5-5, judgment, tax year 2025, jurisdiction us), in the B1 integration worktree. Open lines of the Claude transcription log (line-scoped pass a9e1a8c8fc0e; triage `.transcription/triage/2025/sa.json`) and render log (pass 572805c12157). Full ruling text is in the logs and sidecars; rulings files `/tmp/b1-adj-a/<form>.json` (transcription) and `/tmp/b1-adj-a/render/<form>.json` (render), applied with rule.py. The deepseek family is dormant and not ruled.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | sa.itemizes | representation | 3,276/3,757 agree; no value; 443 candidate-unknown (sa.gambling_losses, s3.mcc read ungated), 17 candidate-refuses (refusals the project places elsewhere), 21 project-refuses | i1040sca, Line 18; f1040 line 12e | Same choice; differences only from inputs the interview gates. |
| claude | transcription | sa.deduction | representation | 3,263/3,757 agree; no value; 464 candidate-unknown, 11 candidate-refuses, 19 project-refuses | as sa.itemizes | As sa.itemizes. |
| claude | transcription | 8a | representation | 3,572/3,757 agree; no value; 184 candidate-unknown (s3.mcc), 1 candidate-refuses (mcc, refused at s3 in the project) | i1040sca p. 8, Line 8a | sa.home_other is asked only under sa.home_owner No; same condition. |
| claude | transcription | 16 | representation | 2,738/3,757 agree; no value; 793 candidate-unknown (sa.gambling_losses without winnings) | i1040sca p. 11, Line 16 | With no winnings line 8b is $0, so the ungated smaller_of equals the project's $0. |
| claude | render | 8a | scope | MISMATCH; Form 8396 subtraction | i1040sca p. 8, Line 8a | A mortgage credit certificate refuses through s3.mcc_if_interest (Schedule 3 line 7). |
| claude | render | 6 | scope | MISMATCH; GST | i1040sca p. 7, Other Taxes | GST on trust income distributions comes with a K-1, refused by scope.k1; foreign tax by sa.unsupported. |
| claude | render | 15 | scope | MISMATCH; casualty | i1040sca p. 11, Line 15 | The line's cite names sd.casualty through sd.other_forms; BUG-0639's stale refusal name is gone. |
| claude | render | 16 | scope | MISMATCH; casualty, claim of right, disaster loss | i1040sca p. 11, Line 16 list | sd.casualty, sd.business_property, s3.repaid_income and sa.unsupported refuse them, as earlier rounds. |

Counts: claude transcription: representation 4; claude render: scope 4. Findings: none. No line left open.
