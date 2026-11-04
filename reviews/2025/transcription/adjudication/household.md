# Adjudication — household

Method: `README.md` in this directory. Triage records: `../triage/household.json`,
`../triage/household.deepseek.json` (executable-triage-v1; 1,083 fixtures, 500 generated returns,
seed 20261026, 200 partial records). Full ruling text is in each log and its sidecar (proposed in
`.transcription/proposed/household.json` and `household.deepseek.json`).

## Round 1 (superseded subject)

| family | line | class | triage | deciding source | reason |
| --- | --- | --- | --- | --- | --- |
| claude | household.roster_bad | ambiguity | 1,771/1,783 agree; 11 project-unknown, 1 project-refuses | f1040 p. 1; i1040gi p. 66 (amb.2025.filer_under_16) | Roster formula is the exact complement of roster_ok; the only differences are the owner's under-16 entry check and fixtures omitting person.under16. |
| claude | household.hsa_both | representation | 1,783/1,783 agree | i8889 p. 4, Name and SSN | Exactly two and at least two coincide because the roster gate allows at most two people. |
| claude | household.all_eic_ssn | scope | 1,741/1,783 agree; 2 candidate-refuses, 40 candidate-unknown | i1040gi p. 40, Step 1 q. 2; p. 43, Form 8862 | Equivalent count; differences are the candidate's Form 8862 gate, which the project applies on eic.credit and s8812.line12. |
| claude | household.all_tin | scope | 1,741/1,783 agree; 2 candidate-refuses, 40 candidate-unknown | i1040gi p. 19, Step 5 q. 1 | Equivalent count; differences are the same Form 8862 gate placed on the predicate. |
| claude | household.ctc_ssn | model error | 1,717/1,783 agree; 47 candidate-unknown, 17 value, 2 candidate-refuses | i1040gi p. 17, Before you begin | Requires person.tin of a person whose work-valid SSN already answers the rule, and counts an applied-for ITIN the text says must be issued; value differences are contradictory answers. |
| claude | household.taxpayer_work_ssn | representation | 1,783/1,783 agree | i1040gi p. 18, Step 3 q. 4 | Count above zero and count at least one are the same test. |
| claude | household.hoh_fails | finding | 1,782/1,783 agree; 1 project-refuses (amb.2025.hoh_community_property) | p501 p. 9, Death or birth; i1040gi p. 15 | Candidate reused the project's Test 1/Test 2 lines; checked against the source, their inputs default the death-year rule, refusing line 12e for a qualifying parent or relative who died in 2025. |
| deepseek | household.roster_bad | model error | 1,634/1,783 agree; 126 value, 22 candidate-unknown, 1 project-refuses | f1040 p. 1 | Encodes dependent screening answers instead of the person-entries-versus-filing-status check. |
| deepseek | household.all_eic_ssn | model error | 1,614/1,783 agree; 19 value, 87 candidate-unknown, 63 candidate-refuses | i1040gi p. 40, Step 1 qq. 1–2 | Adds qualifying children's SSNs to a question about you and your spouse; a child without a valid SSN does not stop the credit. |
| deepseek | household.all_tin | model error | 1,586/1,783 agree; 16 value, 174 candidate-refuses, 7 project-unknown | i1040gi p. 19, Step 5 q. 1 | Tests the dependents' TINs instead of the filers'. |
| deepseek | household.ctc_ssn | model error | 1,759/1,783 agree; 17 value, 7 candidate-unknown | i1040gi p. 17, Before you begin | Requires person.tin beside a work-valid SSN and accepts an applied-for ITIN; value differences are contradictory answers. |
| deepseek | household.hoh_fails | model error | 425/1,783 agree; 1,216 value, 46 candidate-unknown, 93 candidate-refuses, 3 project-refuses | i1040gi p. 14, Head of Household | Ignores f1040.status, failing every non-HOH return, and requires your own home cost for Test 1. |

Findings: one — household.hoh_fails (via dependent.months and dependent.parent_home_paid): the death-year rule of p501 p. 9 is defaulted, so a head of household whose qualifying parent or relative died in 2025 is refused at Form 1040 line 12e. Details in `.transcription/proposed/household.findings.md`.

## Round 2 (superseded subject)

Render only (2026-10-26 replies after BUG-0153; the subject's dependent helpers changed). Rulings proposed in
`.transcription/proposed/round2/render.household.json` and `render.household.deepseek.json`. Render reviews have no
executable triage.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | render | test1_persons | interface gap | UNCLEAR: the helper is defined only in rendered/2025/dependent.md; i1040gi p. 15 and p501 p. 9 were not given | i1040gi p. 14, Test 1 | The count is right. The helper is ruled in the dependent transcription logs. |
| claude | render | test2_persons | interface gap | UNCLEAR, same cause | i1040gi p. 14, Test 2; p501 p. 9 | The count is right. The helper's content was checked against Test 2 items 1 and 2 and the death-or-birth rule. |
| deepseek | render | test2_persons | model error | MISMATCH: "confirmed dependent entry" read as "your dependent" | i1040gi p. 14, Test 2 item 2 | The helper counts unmarried qualifying children who are not dependents. |

Findings: none on these lines. The Test 2 helper's remaining gaps (adoption part-year rule, juvenile-detention wording) are
recorded against `dependent` in `.transcription/proposed/round2/dependent.findings.md` (F2, F3).

## Completeness fixes (superseded subject)

Subject after BUG-0211 to BUG-0217. The only household change links `household.id_count` to
amb.2025.ctc_spouse_itin_application. The session's reading, which follows the placement in i1040s8812, is that the
ITIN-application deeming applies to the credit for other dependents only. The subject's dependent helpers also changed (the
kidnapped screen). Fresh replies of 2026-10-30. Full ruling text: `.transcription/proposed/dfix/transcription.household.json`,
`transcription.household.deepseek.json`, `render.household.json`, `render.household.deepseek.json`. Triage:
`../triage/household.json` and `../triage/household.deepseek.json`, executable-triage-v2 (1,378 fixtures, 500 generated
returns seed 20261026, 200 partial records; 2,078 comparisons per line). Every completed-return difference was enumerated
with the witness cap lifted and assigned.

The ambiguity link was checked against i1040s8812 p. 1. "SSN Required Before the Due Date of Your Return To Claim the CTC
and ACTC" states the other-spouse rule without the deeming sentence. The deeming sentence appears only under "TIN Required by
Due Date of Your Return To Claim the ODC". The Claude reply takes reading 2, through household.all_tin, but no sampled record
exercises it. Its one completed-return value, generated 147, is a filer with work_ssn yes and tin no: contradictory answers.

Counts. Claude transcription: ambiguity 2, representation 2, scope 2. Deepseek transcription: model error 6, scope 1. Render:
Claude interface gap 3; deepseek model error 1 and representation 1.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | household.roster_bad | ambiguity | 2,066/2,078 agree; completed returns: none | amb.2025.filer_under_16; f1040 p. 1 | Same roster; the owner's under-16 check and fixtures lacking person.under16 differ. |
| claude | transcription | household.hsa_both | representation | 2,078/2,078 agree | i8889 p. 4 | Two and at least two coincide under the roster gate. |
| claude | transcription | household.all_eic_ssn | scope | 2,036/2,078 agree; completed returns: none | i1040gi p. 40, Step 1 q. 2 | Only its credit_disallowed refusal differs (refused or incomplete returns). |
| claude | transcription | household.all_tin | scope | 2,036/2,078 agree; completed returns: none | i1040gi p. 19, Step 5 q. 1 | As all_eic_ssn. |
| claude | transcription | household.ctc_ssn | ambiguity | 2,012/2,078 agree; completed returns: 1 value | amb.2025.ctc_spouse_itin_application; i1040gi p. 17; i1040s8812 | Applied-for ITIN accepted for the other spouse (reading 2, not chosen; not executed); triage values are contradictory answers. |
| claude | transcription | household.taxpayer_work_ssn | representation | 2,078/2,078 agree | i1040gi p. 18, Step 3 q. 4 | Same test on a count. |
| deepseek | transcription | household.persons | model error | 1,211/2,078 agree; completed returns: 297 value | f1040 p. 1 | Adds claimed dependents (297 completed values). |
| deepseek | transcription | household.roster_bad | model error | 1,913/2,078 agree; completed returns: 2 value | f1040 p. 1 | Reads the more-than-four-dependents box as the roster check. |
| deepseek | transcription | household.all_eic_ssn | model error | 1,844/2,078 agree; completed returns: 14 value, 10 candidate-unknown | i1040gi p. 40, Step 1 qq. 1-2 | Adds dependents' EIC SSNs (14 completed values). |
| deepseek | transcription | household.all_tin | scope | 1,947/2,078 agree; completed returns: none | i1040gi p. 19, Step 5 | Only inherited refusals on refused returns; the dependent-TIN conjunct cannot bite. |
| deepseek | transcription | household.ctc_ssn | model error | 1,610/2,078 agree; completed returns: 193 candidate-unknown | i1040gi p. 17 | Cycle through dependent.ctc_child (193 completed unknowns). |
| deepseek | transcription | household.taxpayer_work_ssn | model error | 2,070/2,078 agree; completed returns: 5 value | i1040gi p. 18, Step 3 q. 4; s1a line 36a | Counts the spouse's SSN as yours (5 completed values). |
| deepseek | transcription | household.hoh_fails | model error | 543/2,078 agree; completed returns: 569 value, 7 candidate-unknown | i1040gi p. 14 | Ignores f1040.status; home cost required for Test 1. |
| claude | render | hsa_step1_sum | interface gap | render MISMATCH | i8889 p. 7, Line 6, Step 1; f8889.unsupported | Archer MSA line 4 is zero because Archer contributions are refused on Form 8889, outside the render. |
| claude | render | hsa_share_sum | interface gap | render MISMATCH | i8889 p. 7, Line 6, Step 2; f8889.unsupported | Same. |
| claude | render | test2_persons | interface gap | render UNCLEAR | i1040gi pp. 14-15; p501 p. 9 | Page 15 and the helper's definition were not given (as round 2). |
| deepseek | render | test1_persons | representation | render MISMATCH | i1040gi p. 14, Test 1 | The label excludes a co-resident parent; the expression does not, and Test 2 covers that parent on the same facts. |
| deepseek | render | test2_persons | model error | render MISMATCH | i1040gi p. 14, Test 2 item 2 | "Confirmed dependent entry" read as "your dependent" (as round 2). |

Findings: none. The deepseek reviewer's test1_persons objection is about the helper label "through a parent who does not
live with you". The expression and the `parent_home_paid` question carry no residence condition, and Test 2 covers a
co-resident parent on the same facts. Representation, no defect.

## Fix round 2 (superseded subject)

Subject after BUG-0219 and BUG-0220: new `household.qss_eligible` and `household.qss_fails` (refusing at Form 1040
line 12e), and `household.rdp` and `household.rdp_community_property` (refusing at line 1a). The community property
question is now asked of every filer who is not filing jointly. Fresh replies of 2026-10-30. Triage
`../triage/household.json` and `../triage/household.deepseek.json` (executable-triage-v2; 1,382 fixtures, 500 generated
returns seed 20261026, 206 partial records from 40 bases; 2,088 comparisons per line). Every completed-return
difference was enumerated with the witness cap lifted (scratch `/tmp/adj-fixr2-f1040-household/`). Full ruling text:
`.transcription/proposed/fixr2/` (`transcription.household[.deepseek].json`, `render.household[.deepseek].json`).

Counts. Claude transcription: ambiguity 2, representation 2, scope 1, model error 1. Deepseek transcription: model
error 8, representation 1. Render: Claude interface gap 1; deepseek scope 2, interface gap 3, ambiguity 2,
representation 1, model error 1.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | household.roster_bad | ambiguity | 2,076/2,088 agree; completed: none | amb.2025.filer_under_16 | As before. |
| claude | transcription | household.hsa_both | representation | 2,088/2,088 agree | i8889 p. 4 | Two and at least two coincide. |
| claude | transcription | household.ctc_ssn | ambiguity | 2,064/2,088 agree; completed: 1 value (generated 147, contradictory) | amb.2025.ctc_spouse_itin_application | Reading 2, not chosen; not executed. |
| claude | transcription | household.taxpayer_work_ssn | representation | 2,088/2,088 agree | i1040gi p. 18 | Same test on a count. |
| claude | transcription | household.hoh_fails | scope | 2,085/2,088 agree; completed: none | i1040gi pp. 14, 23; amb.2025.hoh_community_property | Inline test drops the project's cited community property refusal. |
| claude | transcription | household.rdp_community_property | model error | 570/2,088 agree; completed: 633 candidate-unknown | i1040gi p. 23; p525 p. 24; p501 p. 6 | Refuses every partner on any status; asks rdp of joint filers and non-community-property filers. |
| deepseek | transcription | household.persons | model error | completed: 305 value | f1040 p. 1 | Adds dependent entries. |
| deepseek | transcription | household.roster_bad | model error | completed: 58 value | f1040 p. 1 | Reads an unclaimed listed entry as a roster mismatch. |
| deepseek | transcription | household.all_eic_ssn | model error | completed: 3 value, 8 candidate-unknown | i1040gi p. 40 | Adds EIC children's SSNs. |
| deepseek | transcription | household.all_tin | model error | completed: 1 value | i1040gi p. 19 | Adds every dependent entry's TIN. |
| deepseek | transcription | household.ctc_ssn | model error | completed: 1 value (stage13.ctc_spouse_no_id) | i1040gi p. 17 | Omits the other spouse's SSN or ITIN. |
| deepseek | transcription | household.taxpayer_work_ssn | representation | 2,088/2,088 agree | i1040gi p. 18 | Same test under the roster. |
| deepseek | transcription | household.hoh_fails | model error | completed: 561 value, 7 candidate-unknown | i1040gi p. 14 | Ignores f1040.status; home cost for Test 1. |
| deepseek | transcription | household.qss_fails | model error | completed: 615 candidate-unknown | i1040gi p. 15 | Ignores f1040.status. |
| deepseek | transcription | household.rdp_community_property | model error | completed: 633 candidate-unknown, 1 value | i1040gi p. 23 | Refuses everyone in a community property state. |
| claude | render | test2_persons | interface gap | UNCLEAR | i1040gi p. 15; p501 p. 9 | Pub. 501 and the helper's definition not given. |
| deepseek | render | roster_ok, roster_bad | scope | MISMATCH | i1040gi p. 14; s3.mfs | MFS refused for the whole return. |
| deepseek | render | hsa_step1_sum, hsa_share_sum | interface gap | MISMATCH | i8889 p. 7; f8889.unsupported | Archer MSA refused outside the render. |
| deepseek | render | under16_count, filer_under16 | ambiguity | UNCLEAR | amb.2025.filer_under_16 | Owner's entry check. |
| deepseek | render | test1_persons | representation | MISMATCH | i1040gi p. 14, Test 1 | Label imprecise, expression right. |
| deepseek | render | test2_persons | model error | MISMATCH | i1040gi p. 14, Test 2 item 2 | "Confirmed dependent entry" misread. |
| deepseek | render | test1_met | interface gap | MISMATCH | i1040gi p. 14, Test 1 | The cost condition is in dependent.hoh_test1, not given. |

The two new gates were checked against i1040gi pp. 15 and 23, with scenarios on stage21.pending1 and pending2.

The qualifying surviving spouse gate refuses exactly when status is qss and the five-test answer is no. The answer is
asked only then, and line 12e, 16 and 24 refuse. Its five tests match p. 15 (spouse died in 2023 or 2024, not
remarried; child or stepchild with the three "could claim except" cases; all year with the temporary-absence, birth,
death and adoption exceptions; over half the cost; could have filed jointly), with one gap. The kidnapped-child
exception (p. 15, "Also see Kidnapped child"; p501 p. 11) is not stated, so the question is narrower than the source
there: F1, low, since every path ends in a refusal.

The registered domestic partner gate refuses a partner in a community property state who does not file jointly, on
single, head of household and qss returns, and computes when either answer is no. That matches p. 23, p525 p. 24
(RDPs domiciled in community property states) and p501 p. 6 (RDPs are not married for federal tax). It is neither
too wide nor too narrow, apart from "at any time in 2025" standing in for domicile.

Findings: one, F1 (low), in `.transcription/proposed/fixr2/household.findings.md`.

## Fix round 4 (superseded subject)

Subject after BUG-0258 (`household.home_cost` gains the p501 p. 9 definition of the cost of keeping up a home), with the
BUG-0257 engine change in place. No expression changed. Fresh replies of 2026-10-30. Triage `../triage/household.json`
and `../triage/household.deepseek.json` (executable-triage-v2; 1,390 fixtures, 500 generated returns seed 20261026, 206
partial records from 40 bases; 2,096 comparisons per line), reproduced exactly by an uncapped rerun; every
completed-return difference was enumerated (scratch `/tmp/adj-fixr2-dependent-household/`). Full ruling text:
`.transcription/proposed/fixr4/` (`transcription.household[.deepseek].json`, `render.household[.deepseek].json`); findings
in `.transcription/proposed/fixr4/household.findings.md`. Both replies validate.

The Claude reply is identical to fix round 2 on roster_bad, taxpayer_work_ssn, hoh_fails and rdp_community_property; its
ctc_ssn now takes the register's chosen reading (scope, for a credit_disallowed refusal it lists). The deepseek reply is
identical on persons, hoh_fails and qss_fails; it changed roster_bad, all_eic_ssn, all_tin, ctc_ssn and
rdp_community_property, and hsa_both is newly open. The rewording itself produces no difference. Checked against p501
p. 9, the definition is right but omits the Worksheet 1 note that amounts paid from the qualifying person's own funds,
such as Social Security, count as paid by that person (F1, medium), which BUG-0258 gave to `dependent.parent_home_paid`
only. `household.qss_eligible` test 4 asks about the same cost with no definition (p501 p. 11, test 5, "See Keeping Up a
Home"; F2, medium). Both render objections concern Form 8889 line 4 (Archer MSA), refused outside the render.

Counts:
- Claude transcription: representation 2, scope 2, ambiguity 1, model error 1.
- Deepseek transcription: model error 7, representation 1, ambiguity 1.
- Claude render: interface gap 2.
- Deepseek render: interface gap 2.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | household.roster_bad | ambiguity | 2,084/2,096 agree; completed returns: none | amb.2025.filer_under_16 | As before. |
| claude | transcription | household.hsa_both | representation | 2,096/2,096 agree | i8889 p. 4 | Two and at least two coincide. |
| claude | transcription | household.ctc_ssn | scope | 2,054/2,096 agree; completed returns: none | i1040gi p. 17; amb.2025.ctc_spouse_itin_application | Now the chosen reading; only its credit_disallowed refusal differs, on refused returns and partials. |
| claude | transcription | household.taxpayer_work_ssn | representation | 2,096/2,096 agree | i1040gi p. 18 | Same test on a count. |
| claude | transcription | household.hoh_fails | scope | 2,093/2,096 agree; completed returns: none | i1040gi pp. 14, 23; amb.2025.hoh_community_property | Inline test drops the project's cited community property refusal. |
| claude | transcription | household.rdp_community_property | model error | 570/2,096 agree; completed returns: 634 candidate-unknown | i1040gi p. 23; p525 p. 24; p501 p. 6 | Refuses every partner on any status; asks rdp of joint filers and non-community-property filers. |
| deepseek | transcription | household.persons | model error | 1,134/2,096 agree; completed returns: 306 value | f1040 p. 1 | Adds dependent entries. |
| deepseek | transcription | household.roster_bad | model error | 1,932/2,096 agree; completed returns: none | f1040 p. 1 | Reads claimed_no_tin; never compares entries with the status. |
| deepseek | transcription | household.hsa_both | representation | 2,095/2,096 agree; completed returns: none | i8889 pp. 3, 4 | Differs only for one person with two forms, refused at person.hsa_repeated. |
| deepseek | transcription | household.all_eic_ssn | model error | 1,929/2,096 agree; completed returns: 21 value, 11 candidate-unknown | i1040gi p. 40 | Adds every dependent entry's EIC SSN. |
| deepseek | transcription | household.all_tin | model error | 2,027/2,096 agree; completed returns: 1 value | i1040gi p. 19 | Adds every dependent entry's TIN. |
| deepseek | transcription | household.ctc_ssn | ambiguity | 2,072/2,096 agree; completed returns: 1 value | amb.2025.ctc_spouse_itin_application | Reading 2, not chosen (itin_applied counts). |
| deepseek | transcription | household.hoh_fails | model error | 552/2,096 agree; completed returns: 561 value, 7 candidate-unknown | i1040gi p. 14 | Ignores f1040.status; home cost for Test 1. |
| deepseek | transcription | household.qss_fails | model error | 590/2,096 agree; completed returns: 616 candidate-unknown | i1040gi p. 15 | Ignores f1040.status. |
| deepseek | transcription | household.rdp_community_property | model error | 2,087/2,096 agree; completed returns: 3 candidate-unknown | i1040gi p. 23; p501 p. 6 | Drops the not-joint condition; asks rdp of joint filers. |
| claude | render | hsa_step1_sum | interface gap | render UNCLEAR | i8889 p. 7; f8889.unsupported | Archer MSA refused outside the render. |
| claude | render | hsa_share_sum | interface gap | render UNCLEAR | i8889 p. 7; f8889.unsupported | Archer MSA refused outside the render. |
| deepseek | render | hsa_step1_sum | interface gap | render MISMATCH | i8889 p. 7; f8889.unsupported | Archer MSA refused outside the render. |
| deepseek | render | hsa_share_sum | interface gap | render MISMATCH | i8889 p. 7; f8889.unsupported | Archer MSA refused outside the render. |

Findings: two of medium severity, F1 (`household.home_cost` own-funds rule) and F2 (`household.qss_eligible` cost
definition), and one low (L1, the TANF note, for T-092), in `.transcription/proposed/fixr4/household.findings.md`.

## Fix round 5 (superseded subject)

Subject after BUG-0260: `household.home_cost` and test 4 of `household.qss_eligible` gain the p501 p. 9 cost definition
and the own-funds rule. No expression changed. Fresh replies of 2026-10-30. Triage `../triage/household.json` and
`../triage/household.deepseek.json` (executable-triage-v2; 1,390 fixtures, 500 generated returns seed 20261026, 206
partial records from 40 bases; 2,096 comparisons per line). An uncapped rerun reproduced the recorded counts exactly, and
every completed-return difference was enumerated (scratch `/tmp/adj-fixr5-household-refund/`). Full ruling text:
`.transcription/proposed/fixr5/` (`transcription.household[.deepseek].json`, `render.household[.deepseek].json`).
Findings are in `.transcription/proposed/fixr5/household.findings.md`. Both replies validate.

The Claude reply is identical to fix round 4 on all six open lines. Its ctc_ssn no longer lists the
`household.credit_disallowed` refusal, so that line now agrees on every record (representation, was scope).

The deepseek reply:
- is identical on hoh_fails and rdp_community_property, and the same test on qss_fails;
- now agrees with the project on persons, all_eic_ssn and all_tin;
- changed roster_bad, hsa_both, ctc_ssn and taxpayer_work_ssn.

The rewording itself produces no difference. Checked against p501 pp. 9 and 11, BUG-0260 closes fix round 4's F1 and F2.
Two lows remain for T-092: the TANF note, which the own-funds sentence can now push toward a No that ends in a refusal,
and "anyone's services" in test 4.

The render objections:
- Claude: whether the domestic-partner gate may exclude joint filers. p501 p. 6 decides it, and that page was not
  given.
- Deepseek: the Test 1 label, as ruled in fix round 2.

Counts:
- Claude transcription: representation 3, ambiguity 1, scope 1, model error 1.
- Deepseek transcription: model error 5, representation 2.
- Claude render: interface gap 1.
- Deepseek render: representation 2.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | household.roster_bad | ambiguity | 2,084/2,096 agree; completed returns: none | amb.2025.filer_under_16 | As before. |
| claude | transcription | household.hsa_both | representation | 2,096/2,096 agree | i8889 p. 4 | Two and at least two coincide. |
| claude | transcription | household.ctc_ssn | representation | 2,096/2,096 agree | i1040gi p. 17; amb.2025.ctc_spouse_itin_application | The chosen reading; the credit_disallowed refusal is no longer listed. |
| claude | transcription | household.taxpayer_work_ssn | representation | 2,096/2,096 agree | i1040gi p. 18 | Same test on a count. |
| claude | transcription | household.hoh_fails | scope | 2,093/2,096 agree; completed returns: none | i1040gi pp. 14, 23; amb.2025.hoh_community_property | Inline test drops the project's cited community property refusal. |
| claude | transcription | household.rdp_community_property | model error | 570/2,096 agree; completed returns: 634 candidate-unknown | i1040gi p. 23; p525 p. 24; p501 p. 6 | Refuses every partner on any status; asks rdp of joint filers and non-community-property filers. |
| deepseek | transcription | household.roster_bad | model error | 2,060/2,096 agree; completed returns: 7 value, 3 candidate-unknown | f1040 p. 1; i1040gi p. 13 | Reads household.married instead of f1040.status; the 7 values are joint fixtures answering married no. |
| deepseek | transcription | household.hsa_both | representation | 2,096/2,096 agree | i8889 p. 4 | Two and at least two coincide. |
| deepseek | transcription | household.ctc_ssn | model error | 2,095/2,096 agree; completed returns: 1 value (stage13.ctc_spouse_no_id) | i1040gi p. 17 | Omits the other spouse's SSN or ITIN. |
| deepseek | transcription | household.taxpayer_work_ssn | representation | 2,096/2,096 agree | i1040gi p. 18 | Exactly one and at least one coincide under the roster. |
| deepseek | transcription | household.hoh_fails | model error | 552/2,096 agree; completed returns: 561 value, 7 candidate-unknown | i1040gi p. 14 | Ignores f1040.status; home cost for Test 1. |
| deepseek | transcription | household.qss_fails | model error | 590/2,096 agree; completed returns: 616 candidate-unknown | i1040gi p. 15 | Ignores f1040.status. |
| deepseek | transcription | household.rdp_community_property | model error | 2,087/2,096 agree; completed returns: 3 candidate-unknown | i1040gi p. 23; p501 p. 6 | Drops the not-joint condition; asks rdp of joint filers. |
| claude | render | rdp_community_property | interface gap | render UNCLEAR | i1040gi pp. 13, 23; p501 p. 6 | The not-joint condition is decided by p501 p. 6, not given. |
| deepseek | render | test1_persons | representation | render MISMATCH | i1040gi p. 14, Test 1 | Label imprecise, expression right; Test 2 covers a co-resident parent. |
| deepseek | render | test1_met | representation | render MISMATCH | i1040gi p. 14, Test 1 | Inherits test1_persons' objection. |

Findings: none of medium or higher severity. There are two lows for T-092: L1, the TANF note, and L2, "anyone's
services" in test 4, both in `.transcription/proposed/fixr5/household.findings.md`. Completeness review round 5
(`../../completeness/r5.findings.md`) has no real gap.

## T-091 round (superseded subject)

Subject after T-091 (BUG-0264 to BUG-0266). In household, only the wording of `household.qss_eligible` changed: test 3
gains p501 p. 9's expected-return condition, which p501 p. 11 applies to QSS. The new dependent gate
`dependent.hoh_absence` refuses `dependent.hoh_test2` and reaches household only through `household.test2_persons`. Fresh
replies of 2026-10-31. Triage `../triage/household.json` and `../triage/household.deepseek.json`
(executable-triage-v2; 1,408 fixtures, 500 generated returns seed 20261026, 211 partial records from 40 bases; 2,119
comparisons per line). An uncapped rerun reproduced the recorded counts exactly, and every completed-return difference
was enumerated (scratch `/private/var/folders/kw/rp67pf8d5ng588lqp7d_gb240000gn/T/opencode/adj-t091-household/`). Full
ruling text is in `.transcription/proposed/t091/` (`transcription.household[.deepseek].json`). Both replies validate.
Both render logs are 39/0/0/0 with no open section.

The Claude reply is new. Five lines are the project's test in another form. Unlike its fix-round-5 reply, it drops
`f1040.status` from hoh_fails and qss_fails. Its rdp_community_property reads any registered domestic partner and any
married filer in a community property state. The deepseek reply is new on roster_bad (it reads `dependent.claimed`), on
all_tin and ctc_ssn (it adds dependents' TINs and SSNs; ctc_ssn has a cycle), on taxpayer_work_ssn (it counts the
spouse) and on hsa_both (it adds `household.married`). It repeats its earlier hoh_fails, qss_fails and
rdp_community_property.

T-091 introduced no error that changes an amount. The QSS clause matches p501 pp. 9 and 11. On head of household,
`hoh_absence` refuses as designed, and it cannot reach another status. One low for T-092: the gate refuses a head of
household return even when another person qualifies cleanly, or when the gated person could never be a Test 2 person
(L1). The completed-return sample is smaller than in fix round 5 for an unrelated reason: many fixtures stop at
`s179.line10`, an input added in the hardening commit.

Counts:
- Claude transcription: representation 5, ambiguity 1, model error 3.
- Deepseek transcription: representation 1, model error 7.
- Render: no open sections.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | household.roster_bad | ambiguity | 2,107/2,119 agree; completed returns: none | amb.2025.filer_under_16 | As before. |
| claude | transcription | household.hsa_both | representation | 2,119/2,119 agree | i8889 p. 4 | Two and at least two coincide. |
| claude | transcription | household.all_eic_ssn | representation | 2,119/2,119 agree | i1040gi p. 40 | None answering no equals all answering yes. |
| claude | transcription | household.all_tin | representation | 2,119/2,119 agree | i1040gi pp. 17, 19 | Same test (De Morgan). |
| claude | transcription | household.ctc_ssn | representation | 2,119/2,119 agree | i1040gi p. 17; amb.2025.ctc_spouse_itin_application | Same test, reading 1. |
| claude | transcription | household.taxpayer_work_ssn | representation | 2,119/2,119 agree | i1040gi p. 18 | Same test on a count. |
| claude | transcription | household.hoh_fails | model error | 562/2,119 agree; completed returns: 230 value, 14 candidate-unknown | i1040gi p. 14 | Drops f1040.status; no completed head of household return differs. |
| claude | transcription | household.qss_fails | model error | 624/2,119 agree; completed returns: 201 candidate-unknown | i1040gi p. 15 | Drops f1040.status; asks qss_eligible of every filer. |
| claude | transcription | household.rdp_community_property | model error | 595/2,119 agree; completed returns: 220 candidate-unknown | i1040gi p. 23; p501 p. 6 | Any partner, any status; drops not-joint. |
| deepseek | transcription | household.roster_bad | model error | 1,721/2,119 agree; completed returns: 66 value | f1040 p. 1 | Reads an unclaimed listed entry as a roster mismatch. |
| deepseek | transcription | household.hsa_both | representation | 2,110/2,119 agree; completed returns: none | i8889 p. 4; i1040gi p. 13 | Added married conjunct only bites on contradictory joint answers (refused). |
| deepseek | transcription | household.all_tin | model error | 2,040/2,119 agree; completed returns: none | i1040gi pp. 17, 18 | Adds every dependent entry's TIN; 79 values off completed returns. |
| deepseek | transcription | household.ctc_ssn | model error | 1,650/2,119 agree; completed returns: 103 candidate-unknown | i1040gi p. 17 | Cycle through dependent.ctc_child; drops the other spouse's SSN or ITIN. |
| deepseek | transcription | household.taxpayer_work_ssn | model error | 2,108/2,119 agree; completed returns: 3 value | i1040gi p. 18; s1a line 36a | Counts the spouse's SSN as yours. |
| deepseek | transcription | household.hoh_fails | model error | 530/2,119 agree; completed returns: 237 value, 14 candidate-unknown | i1040gi p. 14 | Ignores f1040.status; home cost for Test 1 (generated 381). |
| deepseek | transcription | household.qss_fails | model error | 624/2,119 agree; completed returns: 201 candidate-unknown | i1040gi p. 15 | Ignores f1040.status. |
| deepseek | transcription | household.rdp_community_property | model error | 2,110/2,119 agree; completed returns: 3 candidate-unknown | i1040gi p. 23; p501 p. 6 | Drops the not-joint condition. |

Findings: none of medium or higher severity. One low for T-092, L1 (`dependent.hoh_absence` over-refuses on head of
household returns), is in `.transcription/proposed/t091/household.findings.md`.

## T-091 round 2 (superseded subject)

Subject after the T-091 correction (BUG-0267). `household.test2_absence_persons` counts the entries with
`dependent.hoh_absence`. The gate `household.hoh_absence` (unmarried, Test 1 not met, home cost yes, no clean Test 2
person, at least one absence-only Test 2 person) refuses `household.hoh_eligible`. No other household expression changed.
Fresh replies of 2026-10-31. Triage `../triage/household.json` and `../triage/household.deepseek.json`
(executable-triage-v2; 1,411 fixtures, 500 generated returns seed 20261026, 211 partial records from 40 bases; 2,122
comparisons per line). An uncapped rerun reproduced the recorded counts exactly, and every completed-return difference
was enumerated (scratch `/private/var/folders/kw/rp67pf8d5ng588lqp7d_gb240000gn/T/opencode/adj-t091r2-household/`). Full
ruling text is in `.transcription/proposed/t091r2/` (`transcription.household[.deepseek].json`,
`render.household.deepseek.json`). Both replies validate. The Claude render log is 41/0/0/0 with no open section.

The gate was checked on 19 scenarios built from `t091.absence.hoh_refused`. It fires only when head of household turns
on the recount. It does not fire when Test 1 is met, when unmarried or home cost is no, when another person passes Test 2
cleanly, or when the absence person cannot be a Test 2 person. It does fire for one or more absence-only persons. It
cannot reach another status. All six absence regressions hold. The details are in
`.transcription/proposed/t091r2/household.findings.md`.

The Claude reply restores the `f1040.status` test on hoh_fails. Its only differences there are the project's two cited
refusals on `hoh_eligible` (scope). Its ctc_ssn is new in form, and it differs only on contradictory answers. The deepseek
reply again adds dependent entries to `persons` and dependents' SSNs to all_eic_ssn. Its roster_bad now reads claimed
entries that are neither kind of dependent, and it misses both stage13 roster-mismatch fixtures. Its hoh_fails is AGREE,
but the comparison does not judge refusals (an observation in the findings file). The deepseek render objects to three
lines. The test2_persons objection is to the helper label's summary, which predates T-091 (interface gap). The
qss_eligible objection is fix round 2's F1, already in T-092. The rdp_community_property objection turns on p501 p. 6,
which was not given.

Counts:
- Claude transcription: representation 5, ambiguity 1, scope 1, model error 1.
- Deepseek transcription: representation 1, model error 7.
- Deepseek render: interface gap 2, finding 1 (existing, T-092).
- Claude render: no open sections.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | household.roster_bad | ambiguity | 2,109/2,122 agree; completed returns: none | amb.2025.filer_under_16 | As before. |
| claude | transcription | household.hsa_both | representation | 2,122/2,122 agree | i8889 p. 4 | Above zero and at least one coincide. |
| claude | transcription | household.all_eic_ssn | representation | 2,122/2,122 agree | i1040gi p. 40 | None answering no equals all answering yes. |
| claude | transcription | household.all_tin | representation | 2,122/2,122 agree | i1040gi pp. 17, 19 | Same test (De Morgan). |
| claude | transcription | household.ctc_ssn | representation | 2,098/2,122 agree; completed returns: 1 value (generated 147, contradictory answers) | i1040gi p. 17; amb.2025.ctc_spouse_itin_application | Requires person.tin of everyone; a work SSN implies it on consistent answers. |
| claude | transcription | household.taxpayer_work_ssn | representation | 2,122/2,122 agree | i1040gi p. 18 | Same test on a count. |
| claude | transcription | household.hoh_fails | scope | 2,119/2,122 agree; completed returns: none | i1040gi pp. 14, 23; p501 p. 9; amb.2025.hoh_community_property | Omits the cited absence and community property refusals on hoh_eligible. |
| claude | transcription | household.rdp_community_property | model error | 595/2,122 agree; completed returns: 220 candidate-unknown | i1040gi p. 23; p501 p. 6 | Any partner, any status. |
| deepseek | transcription | household.persons | model error | 1,139/2,122 agree; completed returns: 207 value | f1040 p. 1 | Adds dependent entries. |
| deepseek | transcription | household.roster_bad | model error | 1,951/2,122 agree; completed returns: none | f1040 p. 1 | Reads dependent tests; misses stage13.refuse.joint_without_spouse and single_with_spouse. |
| deepseek | transcription | household.hsa_both | representation | 2,122/2,122 agree | i8889 p. 4 | At least two and exactly two coincide under the roster. |
| deepseek | transcription | household.all_eic_ssn | model error | 1,972/2,122 agree; completed returns: 2 value | i1040gi p. 40 | Adds EIC children's SSNs. |
| deepseek | transcription | household.all_tin | model error | 2,043/2,122 agree; completed returns: none | i1040gi pp. 17, 18 | Adds every dependent entry's TIN. |
| deepseek | transcription | household.ctc_ssn | model error | 1,650/2,122 agree; completed returns: 103 candidate-unknown | i1040gi p. 17 | Cycle through dependent.ctc_child. |
| deepseek | transcription | household.taxpayer_work_ssn | model error | 2,111/2,122 agree; completed returns: 3 value | i1040gi p. 18; s1a line 36a | Counts the spouse's SSN as yours. |
| deepseek | transcription | household.rdp_community_property | model error | 2,113/2,122 agree; completed returns: 3 candidate-unknown | i1040gi p. 23; p501 p. 6 | Drops the not-joint condition. |
| deepseek | render | test2_persons | interface gap | render MISMATCH | p501 p. 9; rendered/2025/dependent.md | Adoption and kidnapping are handled in dependent helpers outside the text; the label predates T-091. |
| deepseek | render | qss_eligible | finding | render MISMATCH | p501 p. 11, Kidnapped child | Fix round 2 household F1, already in T-092; not new. |
| deepseek | render | rdp_community_property | interface gap | render MISMATCH | i1040gi pp. 13, 23; p501 p. 6 | The not-joint condition is decided by p501 p. 6, not given. |

Findings: none. No error introduced by T-091 or its correction, and no new low. Two observations (refusals are not
judged by the comparison; the generated sample never sets `absence_no_return`) are in
`.transcription/proposed/t091r2/household.findings.md`.

## Household pass

Subject after the household pass (BUG-0272 to BUG-0275; T-114 to T-117). The changes are wording only:
- `household.unmarried` states the considered-unmarried rules, with the spouse's temporary absence and its
  expected-return condition.
- `household.qss_eligible` test 3 tells a filer with a kidnapped child to answer No. Test 4 excludes "the value of your own
  or a household member's services" and gains the TANF sentence.
- `household.home_cost` gains the TANF sentence.
- The `household.qss_fails` remedy at `f1040.line12e` names the kidnapped case.

No household expression changed. Fresh replies of 2026-11-01. Triage `../triage/household.json` and
`../triage/household.deepseek.json` (executable-triage-v2; 1,411 fixtures, 500 generated returns seed 20261026, 211
partial records from 40 bases; 2,122 comparisons per line). An uncapped rerun reproduced the recorded counts exactly, and
every completed-return difference was enumerated (scratch
`/private/var/folders/kw/rp67pf8d5ng588lqp7d_gb240000gn/T/opencode/adj-hhpass-household/`). Full ruling text is in
`.transcription/proposed/hhpass/` (`transcription.household[.deepseek].json`, `render.household[.deepseek].json`). Both
replies validate.

The reworded questions are inputs, so the transcription comparison cannot see them. Every transcription difference
comes from the replies:
- **Claude.** The reply is new on hsa_both. It reads the spouse-rule count, which cycles through `f8889.split`.
- **Deepseek.** The reply is new on roster_bad (dependent screening answers) and on all_eic_ssn and all_tin (dependents'
  numbers). On hoh_fails and qss_fails it again drops `f1040.status`; both were AGREE in T-091 round 2.

The new words were read against i1040gi pp. 14-15 and p501 pp. 8-9 and 11. The table is in the findings file.
- **The Claude render** objects to two narrowings of the new `household.unmarried`, and both are right (F1, F2).
- **Completeness household#3** raises F1 as well.
- **The deepseek render** objects to the kidnapped No, which is the cited refusal BUG-0273 designed (scope). Its other
  four objections repeat earlier rulings.

Counts:
- Claude transcription: representation 2, ambiguity 1, scope 1, model error 2.
- Deepseek transcription: representation 1, model error 8.
- Claude render: finding 1 (F1 and F2, introduced by BUG-0272).
- Deepseek render: interface gap 2, representation 2, scope 2.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | household.roster_bad | ambiguity | 2,110/2,122 agree; completed returns: none | amb.2025.filer_under_16 | roster_ok's complement without the owner's under-16 check. |
| claude | transcription | household.hsa_both | model error | 2,047/2,122 agree; completed returns: 3 value, 9 candidate-unknown | i8889 pp. 4, 7 | Counts spouse-rule forms, a cycle through f8889.split; misses both spouses with self-only HSAs. |
| claude | transcription | household.ctc_ssn | representation | 2,122/2,122 agree | i1040gi p. 17; amb.2025.ctc_spouse_itin_application | Same test on a count. |
| claude | transcription | household.taxpayer_work_ssn | representation | 2,122/2,122 agree | i1040gi p. 18 | Same test on a count. |
| claude | transcription | household.hoh_fails | scope | 2,119/2,122 agree; completed returns: none | i1040gi pp. 14, 23; p501 p. 9; amb.2025.hoh_community_property | Omits the cited absence and community property refusals on hoh_eligible. |
| claude | transcription | household.rdp_community_property | model error | 595/2,122 agree; completed returns: 220 candidate-unknown | i1040gi p. 23; p501 p. 6 | Any partner, any status. |
| deepseek | transcription | household.persons | model error | 1,139/2,122 agree; completed returns: 207 value | f1040 p. 1 | Adds dependent entries. |
| deepseek | transcription | household.roster_bad | model error | 1,987/2,122 agree; completed returns: 5 value | f1040 p. 1 | Reads dependent screening answers; misses both stage13 roster mismatches. |
| deepseek | transcription | household.hsa_both | representation | 2,122/2,122 agree | i8889 p. 4 | At least two and exactly two coincide under the roster. |
| deepseek | transcription | household.all_eic_ssn | model error | 1,936/2,122 agree; completed returns: 27 value | i1040gi p. 40 | Adds every dependent entry's EIC SSN. |
| deepseek | transcription | household.all_tin | model error | 2,043/2,122 agree; completed returns: none | i1040gi pp. 17, 18 | Adds every dependent entry's TIN. |
| deepseek | transcription | household.ctc_ssn | model error | 1,634/2,122 agree; completed returns: 103 candidate-unknown, 1 value | i1040gi p. 17 | Cycle through the child test; generated 147 contradictory. |
| deepseek | transcription | household.hoh_fails | model error | 532/2,122 agree; completed returns: 237 value, 14 candidate-unknown | i1040gi p. 14 | Drops f1040.status; home cost for Test 1 (generated 381). |
| deepseek | transcription | household.qss_fails | model error | 624/2,122 agree; completed returns: 201 candidate-unknown | i1040gi p. 15 | Drops f1040.status. |
| deepseek | transcription | household.rdp_community_property | model error | 2,113/2,122 agree; completed returns: 3 candidate-unknown | i1040gi p. 23; p501 p. 6 | Drops the not-joint condition. |
| claude | render | unmarried | finding | render MISMATCH; W1/W2 (stage8.hoh.child.ctc, newborn): yes computes, no refuses at hoh_fails | i1040gi p. 15; p501 p. 8 | Introduced by BUG-0272: "more than half of 2025" without the exception (F1); "claims" for "can claim" (F2). |
| deepseek | render | hsa_step1_sum | interface gap | render MISMATCH | i8889 p. 7; f8889.unsupported | Line 4 is zero; Archer MSAs refused on Form 8889. |
| deepseek | render | hsa_share_sum | interface gap | render MISMATCH | i8889 p. 7; f8889.unsupported | As hsa_step1_sum. |
| deepseek | render | test1_persons | representation | render MISMATCH | i1040gi p. 14, Test 1 | Helper label imprecise; expression has no residence condition. |
| deepseek | render | test1_met | representation | render MISMATCH | i1040gi p. 14, Test 1 | Inherits test1_persons. |
| deepseek | render | qss_eligible | scope | render MISMATCH; stage21.pending1.qss_valid_computes yes $31,500, no refused | p501 p. 11, Kidnapped child | The No is BUG-0273's cited refusal with a remedy naming the case. |
| deepseek | render | qss_fails | scope | render MISMATCH | p501 p. 11 | As qss_eligible. |

Findings (`.transcription/proposed/hhpass/household.findings.md`):
- **Introduced by the household pass** (reported whatever their severity):
  - F1, low: `household.unmarried` drops the exception to time lived with you (BUG-0272).
  - F2, low: `household.unmarried` has "claims" for "can claim" (BUG-0272).
  - F3, very low: the kidnapped clause of `qss_eligible` has no time anchor (BUG-0273).
- **Predating the pass** (medium, no TASKS row):
  - P1: a filer whose spouse died in 2025 answers Yes to "unmarried" and gets head of household (p501 p. 6).
  - P2: a filer divorced during 2025 in a community property state is not screened (completeness household#4; an
    owner's decision).
- **Completeness round 8:** `reviews/2025/completeness/r8.findings.md`.

## Household pass, round 2 — 2026-11-01

Current logs were refreshed with Claude Opus 5.5 and deepseek-flash. Original round-1 receipts were archived under `.transcription/archive/before-household-round2-2026-11-01/` with a checked hash manifest. Rulings below refer to the refreshed replies; original verdicts are retained.

### transcription — household

- **household.roster_bad**: scope — The Boolean roster tests agree on complete age-screened records. Form1040 p.1 names the taxpayer and, on a joint return, spouse. The project also propagates household.roster_ok's under16 refusal (amb.2025.filer_under_16); the candidate bypasses it. All 12 observed differences are that extra scope prerequisite: 11 project-unknown on incomplete records and one project-refuses. This is not unconditional partial-input equivalence. Evidence: triage/household.json, executable-triage-v2, 2210 comparisons, 2198 agreements; differences by return state {"incomplete": {"project-unknown": 11}, "refused": {"project-refuses": 1}}. Sample witnesses: {'id': 'classm.f8889.3.deepseek', 'kind': 'fixture'}, {'id': 'classm.f8889.3', 'kind': 'fixture'}.
- **household.hsa_both**: representation — i8889 p.4 says to complete separate Forms8889 if both spouses have HSAs. On a valid roster there are at most two persons, so exactly two and at least two HSA filers coincide. All 2210 comparisons agree; no conclusion is asserted for invalid larger rosters. Evidence: triage/household.json, executable-triage-v2, 2210 comparisons, 2210 agreements; differences by return state {}.
- **household.all_eic_ssn**: representation — i1040gi Step1 asks whether you and your spouse on a joint return have valid SSNs. Counting all persons with true versus counting zero persons with false expresses the same Boolean requirement for answered records. All 2210 comparisons, including the sampled partial records, agree; this is sample evidence, not a universal partial-input proof. Evidence: triage/household.json, executable-triage-v2, 2210 comparisons, 2210 agreements; differences by return state {}.
- **household.all_tin**: representation — i1040gi Step5 question1 includes an ITIN applied for by the due date. Both expressions accept tin OR itin_applied for each filer; the candidate counts zero people failing both rather than counting all passing. All 2210 comparisons agree. Evidence: triage/household.json, executable-triage-v2, 2210 comparisons, 2210 agreements; differences by return state {}.
- **household.ctc_ssn**: representation — i1040s8812 p.2 requires a work-valid SSN for you or your spouse, and an issued SSN/ITIN for the other spouse. Both expressions require at least one work SSN and every filer to have work_ssn OR tin; the candidate counts failures and uses >=1 instead of >0. All 2210 comparisons agree. Evidence: triage/household.json, executable-triage-v2, 2210 comparisons, 2210 agreements; differences by return state {}.
- **household.taxpayer_work_ssn**: representation — Both expressions restrict the sum to person.role=taxpayer and person.work_ssn=true. The Form1040 identification requirement is taxpayer-specific at this interface; a nonnegative integral count >0 equals >=1. All 2210 comparisons agree. Evidence: triage/household.json, executable-triage-v2, 2210 comparisons, 2210 agreements; differences by return state {}.
- **household.rdp_community_property**: model error — i1040gi p.23 describes the registered-partner community-income regime. The published gate explicitly applies to a nonjoint return; the candidate drops that applicability guard and demands the community_property answer on joint returns where the interview does not ask it. All nine observed differences are candidate-unknown (three completed, three incomplete and three refused), not tax-value disagreements. Evidence: triage/household.json, executable-triage-v2, 2210 comparisons, 2201 agreements; differences by return state {"completed": {"candidate-unknown": 3}, "incomplete": {"candidate-unknown": 3}, "refused": {"candidate-unknown": 3}}. Sample witnesses: {'base': 'classm.s2.3.deepseek', 'kind': 'partial', 'withheld': 'household.community_property'}, {'base': 'classm.f8880.2', 'kind': 'partial', 'withheld': 'household.community_property'}.

### transcription — household.deepseek

- **household.persons**: model error — Form1040 p.1 has taxpayer and joint-return spouse entries separate from Dependents. This interface counts those filers; the candidate adds claimed dependents. Completed witness classm.f8889.1.deepseek changes two to three. Remaining unknown/refused differences also arise from evaluating dependency eligibility to count filers, which the source does not require. Evidence: triage/household.deepseek.json, executable-triage-v2, 2210 comparisons, 1262 agreements; differences by return state {"completed": {"value": 203}, "incomplete": {"candidate-unknown": 29, "value": 230}, "refused": {"candidate-refuses": 147, "candidate-unknown": 8, "value": 331}}. Sample witnesses: {'id': 'classm.f8889.1.deepseek', 'kind': 'fixture'}, {'id': 'classm.f4952.1.deepseek', 'kind': 'fixture'}.
- **household.roster_bad**: model error — The interface tests whether taxpayer/spouse entries match Filing Status (Form1040 p.1), not whether dependents have TINs. The candidate substitutes a dependent-identification test and omits the filer-roster invariant. The observed incomplete/refused differences include dependent evaluation and the project under16 scope screen; no completed-return difference was sampled, but that does not validate the substituted predicate. Evidence: triage/household.deepseek.json, executable-triage-v2, 2210 comparisons, 2122 agreements; differences by return state {"incomplete": {"candidate-unknown": 15}, "refused": {"candidate-refuses": 9, "candidate-unknown": 8, "project-refuses": 1, "value": 55}}. Sample witnesses: {'id': 'classm.eic.8.deepseek', 'kind': 'fixture'}, {'id': 'classm.retirement.3.deepseek', 'kind': 'fixture'}.
- **household.hsa_both**: representation — i8889 p.4 says to complete separate Forms8889 if both spouses have HSAs. On a valid roster there are at most two persons, so exactly two and at least two HSA filers coincide. All 2210 comparisons agree; no conclusion is asserted for invalid larger rosters. Evidence: triage/household.deepseek.json, executable-triage-v2, 2210 comparisons, 2210 agreements; differences by return state {}.
- **household.all_eic_ssn**: model error — i1040gi Step1 tests the filer and joint spouse SSNs, whereas qualifying-child SSNs are separately counted for the worksheet credit. The candidate incorrectly requires every EIC child to have an SSN as part of this filer gate. Generated completed witnesses gen29 and gen242 turn true into false; dependency evaluation additionally produces unknown/refused differences. A child without an SSN does not invalidate the filers' SSNs. Evidence: triage/household.deepseek.json, executable-triage-v2, 2210 comparisons, 2050 agreements; differences by return state {"completed": {"value": 2}, "incomplete": {"candidate-refuses": 1, "candidate-unknown": 51, "value": 1}, "refused": {"candidate-refuses": 56, "candidate-unknown": 30, "value": 19}}. Sample witnesses: {'index': 29, 'kind': 'generated', 'seed': 20261026}, {'index': 242, 'kind': 'generated', 'seed': 20261026}.
- **household.all_tin**: model error — i1040gi Step5 question1 concerns you and your spouse. The candidate adds dependent TIN eligibility to a filer-only public interface. All 142 sampled differences occur on refused returns as candidate-refuses; this records the declaration/interface error and does not claim an observed completed-return tax error. Evidence: triage/household.deepseek.json, executable-triage-v2, 2210 comparisons, 2068 agreements; differences by return state {"refused": {"candidate-refuses": 142}}. Sample witnesses: {'id': 'classm.eic.8.deepseek', 'kind': 'fixture'}, {'id': 'classm.retirement.1.deepseek', 'kind': 'fixture'}.
- **household.ctc_ssn**: model error — i1040s8812 p.2 separates filer/spouse identification from the child SSN condition. The candidate expressly chooses the dependent-side condition for this filer-side interface, reads dependent.ctc_child (which itself reads household.ctc_ssn), and omits the required filer condition. Completed records show both candidate-unknown and unequal values; the cyclic dependency and changed predicate are not equivalent formulations. Evidence: triage/household.deepseek.json, executable-triage-v2, 2210 comparisons, 1629 agreements; differences by return state {"completed": {"candidate-unknown": 113, "project-unknown": 1, "value": 19}, "incomplete": {"candidate-unknown": 179, "value": 5}, "refused": {"candidate-refuses": 75, "candidate-unknown": 164, "project-unknown": 1, "value": 24}}. Sample witnesses: {'id': 'classm.f4952.1.deepseek', 'kind': 'fixture'}, {'id': 'classm.f8960.1.deepseek', 'kind': 'fixture'}.
- **household.taxpayer_work_ssn**: model error — The public question is "Do you have an SSN valid for employment" and is taxpayer-specific; the candidate counts a spouse's SSN as well. Generated completed witnesses include gen49 and gen150 where project false becomes true. The count comparison >=1 itself is harmless; removing the role restriction is the defect. Evidence: triage/household.deepseek.json, executable-triage-v2, 2210 comparisons, 2199 agreements; differences by return state {"completed": {"value": 3}, "incomplete": {"value": 5}, "refused": {"value": 3}}. Sample witnesses: {'index': 49, 'kind': 'generated', 'seed': 20261026}, {'index': 150, 'kind': 'generated', 'seed': 20261026}.
- **household.hoh_fails**: model error — i1040gi p.14 Head of Household tests govern the HOH choice, not every filing status. The candidate omits status=hoh, producing true or unknown on non-HOH returns, including completed witnesses. Other dependency unknown/refusal differences flow from running those inapplicable tests. The published gate must be false when HOH is not selected. Evidence: triage/household.deepseek.json, executable-triage-v2, 2210 comparisons, 571 agreements; differences by return state {"completed": {"candidate-unknown": 14, "value": 249}, "incomplete": {"candidate-unknown": 26, "project-unknown": 1, "value": 616}, "refused": {"candidate-refuses": 62, "candidate-unknown": 22, "project-refuses": 5, "value": 644}}. Sample witnesses: {'id': 'classm.f4952.2.deepseek', 'kind': 'fixture'}, {'id': 'classm.f8960.2.deepseek', 'kind': 'fixture'}.
- **household.qss_fails**: model error — i1040gi p.15 QSS tests apply when QSS is selected. The candidate drops status=qss and reads qss_eligible on returns where it is unasked. All observed differences are candidate-unknown, including 214 completed returns; the absence of an answer is appropriate for another status. Evidence: triage/household.deepseek.json, executable-triage-v2, 2210 comparisons, 638 agreements; differences by return state {"completed": {"candidate-unknown": 214}, "incomplete": {"candidate-unknown": 797}, "refused": {"candidate-unknown": 561}}. Sample witnesses: {'id': 'classm.f8889.1.deepseek', 'kind': 'fixture'}, {'id': 'classm.f4952.1.deepseek', 'kind': 'fixture'}.
- **household.widowed_2025**: model error — p501 p.6 allows joint filing after a spouse dies. This owner-selected refusal applies only to single/HOH selections (BUG-0277), as the published label and question specify. The candidate drops the status guard, demanding an unasked answer on other statuses; five completed comparisons become unknown. It is not a universal widowhood refusal. Evidence: triage/household.deepseek.json, executable-triage-v2, 2210 comparisons, 2195 agreements; differences by return state {"completed": {"candidate-unknown": 5}, "incomplete": {"candidate-unknown": 3}, "refused": {"candidate-unknown": 7}}. Sample witnesses: {'base': 'classm.dependent.3.deepseek', 'kind': 'partial', 'withheld': 'household.spouse_died_2025'}, {'base': 'classm.s2.3.deepseek', 'kind': 'partial', 'withheld': 'household.spouse_died_2025'}.
- **household.cp_marriage_ended**: model error — i1040gi p.23 community-income scope is implemented by the conjunction of nonjoint status, community-state residence, married=false and cp_married=true. The candidate treats a conditionally asked question as an unconditional gate; it becomes unknown when that question is correctly unasked, and stale injected answers produce the two value differences on incomplete/refused records. The stage21.household negative controls expose the need for applicability guards. Evidence: triage/household.deepseek.json, executable-triage-v2, 2210 comparisons, 2165 agreements; differences by return state {"completed": {"candidate-unknown": 13}, "incomplete": {"candidate-unknown": 12, "value": 1}, "refused": {"candidate-unknown": 18, "value": 1}}. Sample witnesses: {'base': 'classm.u1250.1.deepseek', 'kind': 'partial', 'withheld': 'household.cp_married'}, {'base': 'classm.dependent.3.deepseek', 'kind': 'partial', 'withheld': 'household.cp_married'}.
- **household.rdp_community_property**: model error — i1040gi p.23 community-property treatment is scoped by the community-state and nonjoint conditions in the published interface. The candidate copies the RDP answer without them and requires it even on inapplicable returns. All sampled differences are candidate-unknown, including 235 completed returns; a conditionally asked input is not an unconditional gate. Evidence: triage/household.deepseek.json, executable-triage-v2, 2210 comparisons, 609 agreements; differences by return state {"completed": {"candidate-unknown": 235}, "incomplete": {"candidate-unknown": 783}, "refused": {"candidate-unknown": 583}}. Sample witnesses: {'id': 'classm.f8889.1.deepseek', 'kind': 'fixture'}, {'id': 'classm.f4952.1.deepseek', 'kind': 'fixture'}.

### render — household.deepseek

- **hoh_community_property**: scope — The cited part-year community-property situation is now separately refused by household.cp_marriage_ended on f1040.line1a (BUG-0278); household.hoh_community_property continues to cover the married HOH case. The eight stage21.household regression fixtures exercise both gates and their negative controls. The review interpreted this one gate as the entire return screen.
- **test1_persons**: representation — i1040gi p. 14 Test 1 says the parent did not have to live with you. dependent.hoh_test1 tests relationship=parent, claimed=true and parent_home_paid=true; it imposes no nonresidency condition. parent_home_paid asks whether the home was the parent's main home, including death-year/rest-home cases (p501 p. 9). Its label describes the typical Test 1 route, but the actual input question and expression do not exclude a live-in parent.
- **qss_eligible**: scope — p501 p. 11 allows the kidnapped-child exception, which the owner explicitly kept outside this tool (BUG-0273). The question names that exclusion and f1040.line12e refuses through household.qss_fails with the kidnapped-child remedy. BUG-0276 limits this instruction to kidnapping that kept the child away during 2025; the exclusion is not a claim that the IRS forbids QSS.

## Household pass, round 4 — 2026-11-01 (superseded subject)

Subject after `BUG-0286` (adding the entry-level marriage/filing-status consistency gate `household.filing_status_conflict` on `scope.ready` and tightening `household.widowed_2025`, `household.cp_marriage_ended`, and `household.rdp_community_property` to exclude married-filing-jointly returns). Prior `hh3` receipts were archived under `.transcription/archive/before-household-status-gate-review-2026-11-01/` with a checked hash manifest. Fresh transcription and render reviews were run with `claude-opus-5-5` and `deepseek-flash`. The Claude transcription reply validates and executes (`triage/household.json`, `executable-triage-v2`: 1,425 fixtures, 500 generated returns seed 20261026, 291 partial records from 40 bases; 2,216 comparisons per line). The DeepSeek transcription reply fails schema and type validation at helper `household.h_has_hoh_person` (`triage/household.deepseek.json`, state `invalid`); lines outside `h_has_hoh_person`'s dependency closure are ruled by reading against the source and interface. Proposed rulings are in `.transcription/proposed/hhpass4/`.

Counts:
- Claude transcription: representation 3, scope 3, model error 2.
- DeepSeek transcription: representation 2, model error 11.
- Claude render: scope 1.
- DeepSeek render: representation 5, scope 1.
- Findings: none.

### transcription — household

- **household.roster_bad**: scope — The Boolean roster tests agree on complete age-screened records. Form 1040 p. 1 names the taxpayer and, on a joint return, spouse. The project also propagates household.roster_ok's under16 refusal (amb.2025.filer_under_16); the candidate bypasses it. All 12 observed differences are that extra scope prerequisite: 11 project-unknown on incomplete records and one project-refuses. This is not unconditional partial-input equivalence. Evidence: triage/household.json, executable-triage-v2, 2216 comparisons, 2204 agreements; differences by return state {"incomplete": {"project-unknown": 11}, "refused": {"project-refuses": 1}}. Sample witnesses: {"id": "classm.f8889.3.deepseek", "kind": "fixture"}, {"id": "classm.f8889.3", "kind": "fixture"}.
- **household.hsa_both**: representation — i8889 p. 4 says to complete separate Forms 8889 if both spouses have HSAs. On a valid roster there are at most two persons, so exactly two and at least two HSA filers coincide (and > 0 vs >= 1 on integral Form 8889 counts coincide). All 2216 comparisons agree; no conclusion is asserted for invalid larger rosters. Evidence: triage/household.json, executable-triage-v2, 2216 comparisons, 2216 agreements; differences by return state {}.
- **household.ctc_ssn**: representation — i1040gi p. 17, Before you begin (and i1040s8812 p. 2) requires a work-valid SSN for you or your spouse, and an issued SSN/ITIN for the other spouse (amb.2025.ctc_spouse_itin_application). Both expressions require at least one work SSN and every filer to have work_ssn OR tin; the candidate uses >= 1 instead of > 0 on the integral work-SSN count. All 2216 comparisons agree. Evidence: triage/household.json, executable-triage-v2, 2216 comparisons, 2216 agreements; differences by return state {}.
- **household.taxpayer_work_ssn**: representation — Both expressions restrict the sum to person.role=taxpayer and person.work_ssn=true (i1040gi p. 18). The Form 1040 identification requirement is taxpayer-specific at this interface; a nonnegative integral count > 0 equals >= 1. All 2216 comparisons agree. Evidence: triage/household.json, executable-triage-v2, 2216 comparisons, 2216 agreements; differences by return state {}.
- **household.hoh_fails**: scope — i1040gi p. 14, Head of Household: "Check the 'Head of household' box only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies"; i1040gi p. 23; p501 p. 9; amb.2025.hoh_community_property. Both expressions test f1040.status == "hoh" and whether Test 1 or Test 2 is met (using <= 0 vs < 1 on integral person counts); the project reads household.hoh_eligible, which carries the cited household.hoh_community_property and household.hoh_absence refusals, whereas the candidate inlines the Boolean test without those refusals. All 4 observed differences are on incomplete/refused records from those scope gates, with zero completed-return differences. Evidence: triage/household.json, executable-triage-v2, 2216 comparisons, 2212 agreements; differences by return state {"incomplete": {"project-unknown": 1}, "refused": {"project-refuses": 3}}. Sample witnesses: {"id": "stage21.household.community_still_married", "kind": "fixture"}, {"id": "audit.household.hoh_community_property", "kind": "fixture"}.
- **household.widowed_2025**: model error — p501 p. 6 and i1040gi p. 13 allow married filing jointly when a spouse died in 2025 and the survivor did not remarry. This owner-selected refusal gate (BUG-0277) explicitly applies to "Filing as single or head of household although your spouse died in 2025" (status == "single" or status == "hoh", with spouse_died_2025 == true). The candidate adds an mfj branch (status == "mfj" and married == false and spouse_died_2025 == true), which wrongly turns a valid death-year joint return into a widowed_2025 failure on stage21.household.status_joint_death_year. Evidence: triage/household.json, executable-triage-v2, 2216 comparisons, 2215 agreements; differences by return state {"incomplete": {"value": 1}}. Sample witness: {"id": "stage21.household.status_joint_death_year", "kind": "fixture"}.
- **household.rdp_community_property**: model error — i1040gi p. 23, Community Property States, and p501 p. 6 describe the registered domestic partner community-income regime. The published gate explicitly applies to a nonjoint return in a community property state (status != "mfj" and community_property == true and rdp == true); the candidate tests household.rdp alone, dropping both applicability guards and demanding the rdp answer on joint and non-community-property returns where the interview does not ask it. All 1,607 observed differences are candidate-unknown (including 226 completed returns), not tax-value disagreements. Evidence: triage/household.json, executable-triage-v2, 2216 comparisons, 609 agreements; differences by return state {"completed": {"candidate-unknown": 226}, "incomplete": {"candidate-unknown": 796}, "refused": {"candidate-unknown": 585}}. Sample witnesses: {"id": "classm.f8889.1.deepseek", "kind": "fixture"}, {"id": "classm.f4952.1.deepseek", "kind": "fixture"}.
- **household.filing_status_conflict**: scope — i1040gi pp. 13–15 and p501 pp. 6–8. The published gate (BUG-0286) checks the marriage-status entry conflict (single with married == true, or mfj with married == false and spouse_died_2025 == false) and refuses scope.ready alongside the dedicated status gates (s3.mfs for married filing separately, household.widowed_2025 for single/HOH with spouse_died_2025, household.hoh_fails for HOH, and household.qss_fails for QSS). The candidate folds widowed_2025, mfs && !married, and qss && married into this single gate. On completed returns there are zero value differences and only 2 partial-record candidate-unknowns where household.married was withheld on a QSS return; the 128 value differences are all on already-refused returns (such as MFS returns refused by s3.mfs or death-year single/HOH returns refused by widowed_2025). Evidence: triage/household.json, executable-triage-v2, 2216 comparisons, 2048 agreements; differences by return state {"completed": {"candidate-unknown": 2}, "incomplete": {"candidate-unknown": 23}, "refused": {"candidate-unknown": 15, "value": 128}}. Sample witnesses: {"base": "classm.dependent.3.deepseek", "kind": "partial", "withheld": "household.married"}, {"base": "classm.f5695.2.deepseek", "kind": "partial", "withheld": "household.married"}.

### transcription — household.deepseek

- **household.persons**: model error — Form 1040 p. 1 has taxpayer and joint-return spouse entries separate from Dependents. This interface counts those filers; the candidate adds claimed dependents. Executable triage was unavailable for this entire reply because household.h_has_hoh_person fails schema and type validation (`triage/household.deepseek.json`, state invalid); this declaration is outside h_has_hoh_person's dependency closure and is ruled by reading against the source and interface. No sampled equivalence is claimed.
- **household.roster_bad**: model error — The interface tests whether taxpayer/spouse entries match Filing Status (Form 1040 p. 1), not whether dependents fail qualifying tests or lack TINs. The candidate substitutes a dependent-screening predicate and omits the filer-roster invariant. Executable triage was unavailable for this entire reply because household.h_has_hoh_person fails validation (`triage/household.deepseek.json`, state invalid); this line is outside h_has_hoh_person's closure and is ruled by reading. No sampled equivalence is claimed.
- **household.hsa_both**: representation — i8889 p. 4 says to complete separate Forms 8889 if both spouses have HSAs. On a valid roster there are at most two persons, so >= 2 and == 2 persons with >= 1 vs > 0 Forms 8889 express the same condition. Executable triage was unavailable for this entire reply because household.h_has_hoh_person fails validation (`triage/household.deepseek.json`, state invalid); this line does not depend on h_has_hoh_person and is ruled by reading. No sampled equivalence is claimed.
- **household.all_eic_ssn**: model error — i1040gi p. 40, Step 1, question 2 tests the filer and joint spouse SSNs, whereas qualifying-child SSNs are separately counted for the worksheet credit. The candidate requires every EIC child to have an SSN as part of this filer gate. Executable triage was unavailable for this entire reply because household.h_has_hoh_person fails validation (`triage/household.deepseek.json`, state invalid); this line is outside h_has_hoh_person's closure and is ruled by reading. No sampled equivalence is claimed.
- **household.all_tin**: model error — i1040gi p. 19, Step 5, question 1 concerns you and your spouse if filing jointly. The candidate adds dependent TIN eligibility to a filer-only public interface. Executable triage was unavailable for this entire reply because household.h_has_hoh_person fails validation (`triage/household.deepseek.json`, state invalid); this line is outside h_has_hoh_person's closure and is ruled by reading. No sampled equivalence is claimed.
- **household.ctc_ssn**: model error — i1040gi p. 17, Before you begin (and i1040s8812 p. 2) separates filer/spouse identification from the child SSN condition. The candidate folds the dependent-side CTC SSN condition into this filer-side interface and omits the other spouse's SSN/ITIN requirement on a joint return. Executable triage was unavailable for this entire reply because household.h_has_hoh_person fails validation (`triage/household.deepseek.json`, state invalid); this line is outside h_has_hoh_person's closure and is ruled by reading. No sampled equivalence is claimed.
- **household.taxpayer_work_ssn**: representation — i1040gi p. 18. Both expressions restrict the sum over person to person.role == "taxpayer" and person.work_ssn == true; the candidate compares the nonnegative integral count with >= 1 instead of > 0. Executable triage was unavailable for this entire reply because household.h_has_hoh_person fails validation (`triage/household.deepseek.json`, state invalid); this line does not depend on h_has_hoh_person and is ruled by reading. No sampled equivalence is claimed.
- **household.hoh_fails**: model error — Validation failure and merits: the candidate expression depends on helper household.h_has_hoh_person, which fails project schema and type validation (`triage/household.deepseek.json`, state invalid: "malformed expression (project schema): data/gt/0 must be string" and "comparison operands have incompatible types"). By reading, it also applies household.home_cost to Test 1 (i1040gi p. 14). This adjudicates the invalid dependency chain and the expression reading; no sampled equivalence is claimed.
- **household.qss_fails**: model error — i1040gi p. 15 Qualifying Surviving Spouse tests apply when QSS is selected. The candidate drops f1040.status == "qss" and reads household.qss_eligible unconditionally on every filing status. Executable triage was unavailable for this entire reply because household.h_has_hoh_person fails validation (`triage/household.deepseek.json`, state invalid); this line is outside h_has_hoh_person's closure and is ruled by reading. No sampled equivalence is claimed.
- **household.widowed_2025**: model error — p501 p. 6 allows joint filing after a spouse dies in 2025. This owner-selected refusal gate (BUG-0277) applies only to single/HOH selections (status == "single" or status == "hoh"), as the published label specifies. The candidate copies household.spouse_died_2025 without the status guard. Executable triage was unavailable for this entire reply because household.h_has_hoh_person fails validation (`triage/household.deepseek.json`, state invalid); this line is outside h_has_hoh_person's closure and is ruled by reading. No sampled equivalence is claimed.
- **household.cp_marriage_ended**: model error — i1040gi p. 23 community-income scope is implemented by the conjunction of nonjoint status (f1040.status != "mfj"), community-state residence, married == false and cp_married == true (BUG-0278). The candidate omits the f1040.status != "mfj" guard. Executable triage was unavailable for this entire reply because household.h_has_hoh_person fails validation (`triage/household.deepseek.json`, state invalid); this line is outside h_has_hoh_person's closure and is ruled by reading. No sampled equivalence is claimed.
- **household.rdp_community_property**: model error — i1040gi p. 23 and p501 p. 6 scope the registered domestic partner community-property refusal by f1040.status != "mfj" and community_property == true. The candidate omits the f1040.status != "mfj" guard. Executable triage was unavailable for this entire reply because household.h_has_hoh_person fails validation (`triage/household.deepseek.json`, state invalid); this line is outside h_has_hoh_person's closure and is ruled by reading. No sampled equivalence is claimed.
- **household.filing_status_conflict**: model error — Validation failure and merits: the candidate expression depends on helper household.h_has_hoh_person, which fails project schema and type validation (`triage/household.deepseek.json`, state invalid). By reading, it also conflates HOH/QSS qualification tests with the marriage/filing-status entry conflict gate (BUG-0286) and requires single filers to fail HOH/QSS tests. No sampled equivalence is claimed.

### render — household

- **qss_eligible**: scope — p501 p. 11, Qualifying Surviving Spouse, Kidnapped child, allows the kidnapped-child exception, which the owner explicitly kept outside this tool (BUG-0273, BUG-0276). The question names that exclusion and instructs the filer to answer No, and f1040.line12e then refuses the QSS return through household.qss_fails with a remedy naming the kidnapped-child rule of Pub. 501. The exclusion is a disclosed scope refusal, not a completed return under a wrong status.

### render — household.deepseek

- **test1_persons**: representation — i1040gi p. 14 Test 1 says "Your parent didn't have to live with you." dependent.hoh_test1 tests relationship == "parent", claimed == true and parent_home_paid == true; it imposes no nonresidency condition. parent_home_paid asks whether the home was the parent's main home, including death-year/rest-home cases (p501 p. 9). Its helper label describes the typical Test 1 route, but the actual input question and expression do not exclude a live-in parent.
- **test2_persons**: representation — i1040gi p. 14, Test 2, and p501 p. 9, Table 4. In this tool every person evaluated for Head of Household Test 2 (including an unmarried qualifying child who is not claimed as a dependent) is entered as an entry in the dependent collection with dependent.claimed == true or false, and dependent.hoh_test2 evaluates the unmarried qualifying child branch without requiring dependent.claimed == true. The model mistakes "dependent entry" (collection record) for "claimed dependent".
- **test2_absence_persons**: representation — i1040gi p. 14, Test 2, and p501 p. 9 (BUG-0267). As on test2_persons, the dependent collection holds every person evaluated for Test 2, including an unmarried qualifying child not claimed as a dependent; dependent.hoh_absence does not require dependent.claimed == true where Test 2 allows an unclaimed qualifying child.
- **test1_met**: representation — i1040gi p. 14, Test 1. Inherits test1_persons' objection to the helper label wording; dependent.hoh_test1 imposes no nonresidency restriction on a qualifying parent.
- **test2_met**: representation — i1040gi p. 14, Test 2. Inherits test2_persons' objection; the dependent collection includes unclaimed qualifying child entries evaluated by dependent.hoh_test2.
- **qss_eligible**: scope — p501 p. 11 allows the kidnapped-child exception, which the owner explicitly kept outside this tool (BUG-0273, BUG-0276). The question names that exclusion and f1040.line12e refuses through household.qss_fails with the kidnapped-child remedy.

## Render refresh on the final rendered English — 2026-11-01 (superseded subject)

The hh4 render batch ran before BUG-0286's `filing_status_conflict` gate and the widened spouse-death wording
reached `rendered/2025/household.md`, so those render logs reviewed a stale subject. The full suite's snapshot
rebuild regenerated the rendered English and `check_logs.py` reported that the household render logs had
reviewed an earlier rendering. The tree was regenerated (`npm run render`), the prior receipts archived under
`.transcription/archive/before-render-refresh-2026-11-01/` with a checked hash manifest, and the four render
reviews rerun under `claude-opus-5-5` and `deepseek-flash`. The transcription logs were unaffected. The render
counts in the hh4 entry above are superseded for household by this refresh.

Three render disagreements were ruled; both household render logs report 0 open.

Counts:
- Claude render household: scope 2.
- DeepSeek render household: scope 1.

### render — household

- **qss_eligible**: scope — p501 p. 11 allows the kidnapped-child exception, which the owner explicitly kept outside this tool (BUG-0273). The question names that exclusion, and `f1040.line12e` refuses through `household.qss_fails` with the kidnapped-child remedy. BUG-0276 limits the instruction to a kidnapping that kept the child away during 2025; the exclusion is not a claim that the IRS forbids QSS.
- **filing_status_conflict**: scope (both families) — i1040gi p. 14, Married Filing Separately: a separate return is refused for the whole return by `s3.mfs` on `scope.ready`, so a still-married filer who checks MFS never reaches line 12e and cannot produce the conflict the reviewer describes. The gate covers the two supported contradictions (Single with a year-end marriage; a joint return with no year-end marriage and no death in 2025); HOH and QSS have their own tests, and a joint death-year return stays supported. BUG-0286 records the entry check.

## Backlog round (superseded subject)
Subject after person-dep PENDING-9 (T-101, BUG-0350): new gates `household.ctc_disallowed_claim` (credit_disallowed and Schedule 8812 line 8 more than line 11) and `household.eic_disallowed_claim` (credit_disallowed and `eic.eligible`), used by the refusals of `s8812.line12` and `eic.credit`. Fresh replies of claude-opus-5-5, deepseek-flash (now valid, so executed) and gpt-6-astra.

Triage: `../triage/<stem>.json`, executable-triage-v2, rerun today with `tools/transcription/triage.py` (1,495 fixtures, 500 generated returns seed 20261026, partial records per form); every completed-return difference was enumerated with the witness cap lifted in a scratch run (`/tmp/adj-bklg-person-scope-household/`), and the printed amounts a helper could reach were checked where the ruling says so. `fixtures/2025/classm*.json` were rewritten by a concurrent class M run at 15:14 while this round was adjudicated; witnesses on `classm.*` cases may not rebuild identically from the current files. Full ruling text: `.transcription/proposed/bklg/<kind>.<stem>.json`.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | household.roster_bad | scope | 2,271/2,284 agree; 12 project-unknown, 1 project-refuses | The Boolean roster tests agree on complete age-screened records | Form 1040 p. 1 names the taxpayer and, on a joint return, spouse |
| claude | transcription | household.hoh_fails | scope | 2,279/2,284 agree; 3 project-refuses, 2 project-unknown | i1040gi p. 14, Head of Household: "Check the 'Head of household' box only if you are unmarried (or considered  | Both expressions test f1040.status == "hoh" and whether Test 1 or Test 2 is met (using <= 0 vs < 1 on integral person counts); the project reads household.hoh_eligible, ... |
| claude | transcription | household.rdp_community_property | model error | 633/2,284 agree; 1,651 candidate-unknown; completed: 219 candidate-unknown | i1040gi p. 23, Community Property States, and p501 p. 6 describe the registered domestic partner community-inc | The published gate explicitly applies to a nonjoint return in a community property state (status != "mfj" and community_property == true and rdp == true); the candidate ... |
| claude | transcription | household.hsa_both | representation | 2,284/2,284 agree | i8889 p. 4, "If you and your spouse each have separate HSAs, complete a separate Form 8889 for each" | Both count persons with at least one Form 8889 and test that the count is two (> 0 against >= 1 on an integral count). |
| claude | transcription | household.all_eic_ssn | representation | 2,284/2,284 agree | i1040gi p. 40, Step 1, question 2. "No person without a valid SSN" against "every person has a valid SSN": the |  |
| claude | transcription | household.all_tin | representation | 2,284/2,284 agree | i1040gi p. 19, Step 5, question 1 (an applied-for ITIN counts) | The reply counts persons with neither a TIN nor an application and tests zero; the project tests that every person has one or the other |
| claude | transcription | household.ctc_ssn | representation | 2,258/2,284 agree; 19 value, 7 candidate-unknown; completed: 1 value | i1040gi p. 17, Before you begin, "only one spouse is required to have a valid SSN ... The other spouse must ha | The reply requires person.tin of every filer; the project accepts person.tin or person.work_ssn |
| claude | transcription | household.taxpayer_work_ssn | model error | 2,267/2,284 agree; 17 value; completed: 3 value | i1040gi pp. 101, 106 and 110 (Schedule 1-A: the taxpayer's own valid SSN, and on a joint return the spouse who | The published line is the taxpayer's own answer ("Do you have ...", role taxpayer), read by s1a.tip_ssn and s1a.ot_ssn only on a non-joint return and by ... |
| claude | transcription | household.widowed_2025 | model error | 2,283/2,284 agree; 1 value | p501 p. 6 and i1040gi p. 13 allow married filing jointly when a spouse died in 2025 and the survivor did not r | This owner-selected refusal gate (BUG-0277) explicitly applies to "Filing as single or head of household although your spouse died in 2025" (status == "single" or status ... |
| claude | transcription | household.filing_status_conflict | scope | 2,122/2,284 agree; 140 value, 22 candidate-unknown | i1040gi pp. 13-15 and p501 pp. 6-8 | The published gate (BUG-0286) checks the marriage-entry conflicts of the single and joint statuses; the reply also flags a single return with a 2025 death (refused by ... |
| claude | transcription | household.ctc_disallowed_claim | model error | 2,262/2,284 agree; 14 candidate-unknown, 7 project-refuses, 1 value; completed: 2 candidate-unknown, 1 value | i1040s8812 p. 2, "you must attach Form 8862 to your tax return to claim the CTC, ACTC, or ODC unless an except | The candidate copies household.credit_disallowed, so the gate is true, and Schedule 8812 line 12 refuses, whenever the answer is Yes, also on a return that claims no ... |
| claude | transcription | household.eic_disallowed_claim | model error | 2,255/2,284 agree; 21 candidate-unknown, 6 project-refuses, 2 value; completed: 2 candidate-unknown, 1 value | i1040gi p. 43, "You must file Form 8862 if your EIC for a year after 1996 was reduced or disallowed ..." (the  | The candidate copies household.credit_disallowed, so the earned income credit refuses on a Yes answer also when Steps 1 to 5 are not passed and no credit is claimed ... |
| deepseek | transcription | household.persons | model error | 1,298/2,284 agree; 805 value, 138 candidate-refuses, 43 candidate-unknown; completed: 201 value | Form 1040 p. 1 has taxpayer and joint-return spouse entries separate from Dependents | This interface counts those filers; the candidate adds claimed dependents |
| deepseek | transcription | household.roster_bad | model error | 2,202/2,284 agree; 50 value, 23 candidate-unknown, 8 candidate-refuses, 1 project-refuses | The interface tests whether taxpayer/spouse entries match Filing Status (Form 1040 p. 1), not whether dependen | The candidate substitutes a dependent-screening predicate and omits the filer-roster invariant |
| deepseek | transcription | household.all_eic_ssn | model error | 1,988/2,284 agree; 138 candidate-refuses, 105 candidate-unknown, 53 value; completed: 12 value | i1040gi p. 40, Step 1, question 2 tests the filer and joint spouse SSNs, whereas qualifying-child SSNs are sep | The candidate requires every EIC child to have an SSN as part of this filer gate |
| deepseek | transcription | household.all_tin | model error | 2,139/2,284 agree; 138 candidate-refuses, 7 candidate-unknown | i1040gi p. 19, Step 5, question 1 concerns you and your spouse if filing jointly | The candidate adds dependent TIN eligibility to a filer-only public interface |
| deepseek | transcription | household.ctc_ssn | model error | 1,693/2,284 agree; 460 candidate-unknown, 131 candidate-refuses; completed: 111 candidate-unknown | i1040gi p. 17, Before you begin (and i1040s8812 p. 2) separates filer/spouse identification from the child SSN | The candidate folds the dependent-side CTC SSN condition into this filer-side interface and omits the other spouse's SSN/ITIN requirement on a joint return |
| deepseek | transcription | household.widowed_2025 | model error | 2,263/2,284 agree; 20 candidate-unknown, 1 value; completed: 4 candidate-unknown | p501 p. 6 allows joint filing after a spouse dies in 2025 | This owner-selected refusal gate (BUG-0277) applies only to single/HOH selections (status == "single" or status == "hoh"), as the published label specifies |
| deepseek | transcription | household.rdp_community_property | model error | 633/2,284 agree; 1,651 candidate-unknown; completed: 219 candidate-unknown | i1040gi p. 23 and p501 p. 6 scope the registered domestic partner community-property refusal by f1040.status ! | The candidate omits the f1040.status != "mfj" guard |
| deepseek | transcription | household.qss_fails | model error | 661/2,284 agree; 1,623 candidate-unknown; completed: 195 candidate-unknown | i1040gi p. 15 Qualifying Surviving Spouse tests apply when QSS is selected | The candidate drops f1040.status == "qss" and reads household.qss_eligible unconditionally on every filing status |
| deepseek | transcription | household.cp_marriage_ended | model error | 2,233/2,284 agree; 49 candidate-unknown, 2 value; completed: 12 candidate-unknown | i1040gi p. 23, Community Property States (BUG-0278) | The reply copies household.cp_married and drops the conditions the project applies (not married at year end, community property state, not a joint return), so it needs ... |
| deepseek | transcription | household.hsa_both | representation | 2,284/2,284 agree | i8889 p. 4 | Two or more persons with a Form 8889 against exactly two: the same on a valid roster (at most two persons) |
| deepseek | transcription | household.taxpayer_work_ssn | model error | 2,267/2,284 agree; 17 value; completed: 3 value | as the Claude family's reply: it counts either spouse for the taxpayer's own SSN answer, which s1a.line36a_sen | Reclassified from representation: the reply changed. |
| deepseek | transcription | household.hoh_fails | model error | 602/2,284 agree; 1,546 value, 68 candidate-refuses, 61 candidate-unknown, 5 project-refuses, 2 project-unknown; completed: 236 value, 8 candidate-unknown | i1040gi p. 14, Head of household, "Check the 'Head of household' box only if ..." | The reply drops the test that head of household was checked, so it is true for every non-HOH filer without a qualifying person (classm.f4952.2.deepseek, a joint return: ... |
| deepseek | transcription | household.filing_status_conflict | model error | 1,993/2,284 agree; 218 value, 58 candidate-unknown, 15 candidate-refuses; completed: 1 value | i1040gi pp. 13-15 | The reply folds its own head of household and qualifying surviving spouse tests into the marriage-entry gate, inheriting household.hoh_fails's errors: generated 381, a ... |
| deepseek | transcription | household.ctc_disallowed_claim | model error | 2,262/2,284 agree; 14 candidate-unknown, 7 project-refuses, 1 value; completed: 2 candidate-unknown, 1 value | i1040s8812 p. 2, "you must attach Form 8862 to your tax return to claim the CTC, ACTC, or ODC unless an except | The candidate copies household.credit_disallowed, so the gate is true, and Schedule 8812 line 12 refuses, whenever the answer is Yes, also on a return that claims no ... |
| deepseek | transcription | household.eic_disallowed_claim | model error | 2,255/2,284 agree; 21 candidate-unknown, 6 project-refuses, 2 value; completed: 2 candidate-unknown, 1 value | i1040gi p. 43, "You must file Form 8862 if your EIC for a year after 1996 was reduced or disallowed ..." (the  | The candidate copies household.credit_disallowed, so the earned income credit refuses on a Yes answer also when Steps 1 to 5 are not passed and no credit is claimed ... |
| gpt | transcription | household.roster_bad | scope | 2,271/2,284 agree; 12 project-unknown, 1 project-refuses | Form 1040 p. 1 names the taxpayer and, on a joint return, the spouse | The reply's roster test is the project's (one taxpayer; a spouse only on a joint return); the project also carries household.roster_ok's under-16 refusal ... |
| gpt | transcription | household.hsa_both | representation | 2,280/2,284 agree; 4 project-unknown | i8889 p. 4 | The reply adds "joint return", which on a valid roster is implied by two persons each with a Form 8889; the only differences are refused or incomplete records on which ... |
| gpt | transcription | household.all_tin | model error | 2,280/2,284 agree; 2 candidate-refuses, 2 value | i1040gi p. 19, Step 5, question 1, "(Answer 'Yes' if you are applying for an ITIN on or before the due date of | The reply drops the applied-for ITIN and uses the issued-number rule of p. 17, which is the child tax credit's (household.ctc_ssn); the line feeds the credit for other ... |
| gpt | transcription | household.taxpayer_work_ssn | scope | 2,282/2,284 agree; 2 candidate-refuses | i1040gi p. 18 | Exactly one taxpayer with a work SSN against at least one: the same on a valid roster; the only differences are the two invalid-roster fixtures refused by ... |
| gpt | transcription | household.rdp_community_property | model error | 633/2,284 agree; 1,651 candidate-unknown; completed: 219 candidate-unknown | i1040gi p. 23 and p501 p. 6 | As the other families: the reply copies household.rdp and drops the community-state and non-joint conditions, asking the answer where the interview does not. |
| gpt | transcription | household.filing_status_conflict | scope | 1,984/2,284 agree; 213 value, 70 candidate-unknown, 17 candidate-refuses | i1040gi pp. 13-15 | The reply folds the head of household, death-year single/HOH, MFS and QSS conflicts into the marriage-entry gate; those have their own cited refusals ... |
| gpt | transcription | household.ctc_disallowed_claim | model error | 2,262/2,284 agree; 14 candidate-unknown, 7 project-refuses, 1 value; completed: 2 candidate-unknown, 1 value | i1040s8812 p. 2, "you must attach Form 8862 to your tax return to claim the CTC, ACTC, or ODC unless an except | The candidate copies household.credit_disallowed, so the gate is true, and Schedule 8812 line 12 refuses, whenever the answer is Yes, also on a return that claims no ... |
| gpt | transcription | household.eic_disallowed_claim | model error | 2,255/2,284 agree; 21 candidate-unknown, 6 project-refuses, 2 value; completed: 2 candidate-unknown, 1 value | i1040gi p. 43, "You must file Form 8862 if your EIC for a year after 1996 was reduced or disallowed ..." (the  | The candidate copies household.credit_disallowed, so the earned income credit refuses on a Yes answer also when Steps 1 to 5 are not passed and no credit is claimed ... |
| claude | render | qss_eligible | scope | render MISMATCH | p501 p. 11, Kidnapped child | The owner kept the kidnapped-child exception outside the tool (BUG-0273, BUG-0276); the question tells that filer to answer No and f1040.line12e then refuses through ... |
| deepseek | render | hsa_step1_sum | model error | render MISMATCH | i8889 p. 7, Line 6, Steps 1 and 2 | The helper is not the line 6 amount: it adds the two spouses' Step 1 limits so that f8889.allocation_bad can test that both refigured the same limit (f8889.step1_x2 ... |
| deepseek | render | hoh_eligible | scope | render MISMATCH | p501 p. 9; i1040gi p. 23, Community Property States | A filer married for part of 2025 in a community property state who is not filing jointly is refused for the whole return by household.cp_marriage_ended at Form 1040 line ... |
| deepseek | render | filing_status_conflict | scope | render MISMATCH | i1040gi p. 14, Married Filing Separately; p501 p. 6 | A separate return is refused for the whole return by s3.mfs on scope.ready, and a single or head of household return with a 2025 death by household.widowed_2025, so the ... |
| deepseek | render | ctc_disallowed_claim | scope | render MISMATCH | i1040s8812 p. 2, Form 8862 may be required | Post-fix rerun. Line 12 positive need not mean a claimed credit (line 14, line 27); refusal only, the residual over-refusal accepted (low) in BUG-0350's review correction; household.findings.md L3. |
| deepseek | render | qss_eligible | scope | render MISMATCH | p501 p. 11, Kidnapped child | Post-fix rerun. As the Claude ruling: owner kept the kidnapped-child exception outside the tool (BUG-0273, BUG-0276); f1040.line12e refuses through household.qss_fails. |

Counts: Claude transcription model error 5, representation 4, scope 3 (12); deepseek transcription model error 14, representation 1 (15); gpt transcription model error 4, scope 3, representation 1 (8); Claude render scope 1; deepseek render scope 2, model error 1. All three families copy `household.credit_disallowed` for both new gates (the pre-package over-refusal); the project's narrowing matches i1040s8812 p. 2 and i1040gi p. 43, and the only completed-return difference is the package's regression `f2.t101.credit_disallowed_no_credit_claimed`. Reclassified: `household.taxpayer_work_ssn` (Claude and deepseek, representation to model error: either spouse counted). Errors introduced: none. Findings: none of medium or higher; lows in `.transcription/proposed/bklg/household.findings.md`.

Post-fix rerun (household.eic_disallowed_claim now also requires eic.line6 above zero, BUG-0350 review correction): 2 open deepseek render sections ruled from `.transcription/proposed/bklg/fx.render.household.deepseek.json`, scope 2. Triage rerun today for all three families (264 partial records, 2,259 comparisons): the gate's completed-return differences are the regressions f2.t101.credit_disallowed_no_credit_claimed and f2.t101.credit_disallowed_eic_zero (project false). The fix introduced no error (eic.line6 is the credit of Worksheet A and B, i1040gi p. 43); no finding.

## Refresh round

Subject after the refresh-round fixes BUG-0391 to BUG-0401 (for these forms: BUG-0392 `person.sav_claimed` asked whenever education expenses are paid; BUG-0394 `person.educator_expenses` exclusions; BUG-0398 `household.taxpayer_work_ssn` cites and the `dependent.dc_count` label; BUG-0393 `scope.other_income` disaster distributions), transcription prompt `source-only-computation-v3`. Fresh replies of claude-opus-5-5 and deepseek-flash. Rulings in `.transcription/proposed/rf/` (`transcription.<stem>.json`, `render.<stem>.json`); prior rulings reused where the line, the disagreement and the evidence are the same, re-checked against `.transcription/archive/before-catalog-refresh-2026-11-03/`.

Triage: `../triage/<stem>.json`, executable-triage-v2, rerun today with `tools/transcription/triage.py` (1,565 fixtures, 500 generated returns seed 20261026, partial records per form); every completed-return difference was enumerated with the witness cap lifted in a scratch run (`/tmp/adj-rf-pers/full/`), and witnesses were traced with `--explain` where a ruling names one.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | household.roster_bad | scope | 2,287/2,300 agree; 12 project-unknown, 1 project-refuses | f1040 p. 1, "If joint return, spouse's first name"; amb.2025.filer_under_16. | The roster test (one taxpayer; a spouse entry exactly on a joint return) is the project's; the project also carries household.roster_ok's under-16 refusal, which the reply bypasses. Every difference is that refusal (proj |
| claude | transcription | household.hsa_both | representation | 2,300/2,300 agree | i8889 p. 4, "If you and your spouse each have separate HSAs, complete a separate Form 8889 for each". | Both count persons with a Form 8889 and test for two (0 < n against 1 <= n on an integral count). No difference. |
| claude | transcription | household.all_eic_ssn | representation | 2,300/2,300 agree | i1040gi p. 40, Step 1, question 2. "No filer without a valid SSN" against "every filer has one": the same test. | No difference. |
| claude | transcription | household.all_tin | representation | 2,300/2,300 agree | i1040gi p. 19, Step 5, question 1 (an applied-for ITIN counts, as the project reads it). | The reply counts filers with neither a TIN nor an application and tests zero; same test. No difference. |
| claude | transcription | household.ctc_ssn | model error | 2,224/2,300 agree; 56 candidate-unknown, 20 value; completed: 5 candidate-unknown, 1 value | i1040gi p. 7, "If you are filing a joint return, only one spouse is required to have a valid SSN ... | The other spouse must have either an SSN or ITIN" (amb.2025.ctc_spouse_itin_application). The reply requires person.tin of every filer, also of one who answered person.work_ssn Yes (an SSN valid for employment is an SSN) |
| claude | transcription | household.taxpayer_work_ssn | representation | 2,300/2,300 agree | i1040gi pp. 101, 106 and 110 (Schedule 1-A: the taxpayer's own valid SSN). | The reply now counts only the taxpayer's entry, as the project (1 <= n against 0 < n on an integral count); the prior model error (either spouse) is gone. No difference. |
| claude | transcription | household.ctc_disallowed_claim | model error | 2,296/2,300 agree; 3 project-refuses, 1 candidate-unknown; completed: 1 candidate-unknown | i1040s8812 p. 2, "you must attach Form 8862 to your tax return to claim the CTC, ACTC, or ODC unless an exception applies". | The reply now gates the answer on at least one dependent passing its own inlined CTC or ODC test; the project gates on a credit surviving the phase-out (Schedule 8812 line 8 above line 11). A return whose line 11 removes |
| claude | transcription | household.eic_disallowed_claim | model error | 2,270/2,300 agree; 24 candidate-unknown, 3 value, 3 project-refuses; completed: 4 candidate-unknown, 2 value | i1040gi p. 43, "You must file Form 8862 if your EIC for a year after 1996 was reduced or disallowed" (with a claim of the credit). | As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): the reply copies household.credit_disallowed, so the EIC refuses on a Yes answer where no credit is claimed: completed f2.t101.credit_dis |
| claude | transcription | household.hoh_fails | scope | 2,296/2,300 agree; 3 project-refuses, 1 project-unknown | i1040gi p. 14, Head of Household; amb.2025.hoh_community_property. | As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): the same Test 1 / Test 2 check, the project reading household.hoh_eligible with its cited household.hoh_community_property and household. |
| claude | transcription | household.widowed_2025 | model error | 2,295/2,300 agree; 4 candidate-unknown, 1 value | p501 p. 6 and i1040gi p. 13 (a 2025 death allows a joint return). | As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): the reply adds a joint-return branch to the owner's single/HOH gate (BUG-0277), flagging a valid death-year joint return (stage21.househo |
| claude | transcription | household.rdp_community_property | model error | 611/2,300 agree; 1,689 candidate-unknown; completed: 262 candidate-unknown | i1040gi p. 23, Community Property States; p501 p. 6. | As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): the reply tests household.rdp alone, dropping the nonjoint and community-property guards, so it asks the answer on every return (262 comp |
| claude | transcription | household.filing_status_conflict | scope | 2,142/2,300 agree; 130 value, 28 candidate-unknown | i1040gi pp. 13-15; p501 pp. 6-8. | As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): the reply also flags a 2025-death single return (refused by household.widowed_2025) and MFS while unmarried (MFS refused by s3.mfs on sco |
| deepseek | transcription | household.roster_bad | scope | 2,287/2,300 agree; 12 project-unknown, 1 project-refuses | f1040 p. 1; amb.2025.filer_under_16. | The reply now states the roster invariant (one taxpayer; a spouse entry exactly on a joint return), as the Claude reply; the class changes from model error. Every difference is the project's under-16 refusal through hous |
| deepseek | transcription | household.all_eic_ssn | model error | 2,157/2,300 agree; 84 candidate-unknown, 33 value, 25 candidate-refuses, 1 project-unknown; completed: 2 value | i1040gi p. 40, EIC Step 1, question 2 ("Do you, and your spouse if filing a joint return, have a valid SSN"). | As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): the reply also requires every EIC child to have an SSN in this filer gate (now with a disabled-child branch): completed generated 29 and  |
| deepseek | transcription | household.all_tin | model error | 2,228/2,300 agree; 70 value, 2 project-unknown | i1040gi p. 19, Step 5, question 1 concerns you and your spouse. | The reply adds every dependent's TIN to this filer-only test and drops person.itin_applied. Differences are on refused or incomplete records; none completed. |
| deepseek | transcription | household.ctc_ssn | model error | 2,226/2,300 agree; 73 candidate-refuses, 1 value | i1040gi p. 7, Before you begin (filer and spouse SSN rule); the child's SSN is a per-child test (dependent.ctc_child). | As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): the reply folds the child-side SSN test into this filer gate and drops the other spouse's SSN-or-ITIN condition. Differences are candidat |
| deepseek | transcription | household.ctc_disallowed_claim | model error | 2,277/2,300 agree; 16 candidate-unknown, 5 project-refuses, 2 value; completed: 4 candidate-unknown, 2 value | i1040s8812 p. 2, Form 8862 is needed to claim the credit. | As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): the reply copies household.credit_disallowed, refusing where no credit is claimed (completed f2.t101.credit_disallowed_no_credit_claimed  |
| deepseek | transcription | household.eic_disallowed_claim | model error | 2,270/2,300 agree; 24 candidate-unknown, 3 value, 3 project-refuses; completed: 4 candidate-unknown, 2 value | i1040gi p. 43, Form 8862 goes with a claim of the EIC. | As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): the reply copies household.credit_disallowed (completed f2.t101.credit_disallowed_no_credit_claimed and f2.t101.credit_disallowed_eic_zer |
| deepseek | transcription | household.hoh_fails | model error | 565/2,300 agree; 1,561 value, 105 candidate-unknown, 62 candidate-refuses, 5 project-refuses, 2 project-unknown; completed: 258 value, 26 candidate-unknown | i1040gi p. 14, "Check the 'Head of household' box only if ...". | As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): the reply drops the test that head of household was checked, so it is true for non-HOH filers without a qualifying person (258 completed  |
| deepseek | transcription | household.qss_fails | model error | 649/2,300 agree; 1,651 candidate-unknown; completed: 232 candidate-unknown | i1040gi p. 15, Qualifying Surviving Spouse. | As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): the reply drops f1040.status == "qss" and asks household.qss_eligible on every return (232 completed candidate-unknowns). |
| deepseek | transcription | household.widowed_2025 | model error | 2,233/2,300 agree; 66 candidate-unknown, 1 value; completed: 20 candidate-unknown | p501 p. 6 (joint filing allowed after a 2025 death); BUG-0277 gate applies to single/HOH only. | As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): the reply copies household.spouse_died_2025 without the status guard (20 completed candidate-unknowns). |
| deepseek | transcription | household.cp_marriage_ended | model error | 2,090/2,300 agree; 208 candidate-unknown, 2 value; completed: 64 candidate-unknown | i1040gi p. 23, Community Property States (BUG-0278). | As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): the reply copies household.cp_married without the project's conditions, asking it where the interview does not (64 completed candidate-un |
| deepseek | transcription | household.rdp_community_property | model error | 2,269/2,300 agree; 31 candidate-unknown; completed: 9 candidate-unknown | i1040gi p. 23; p501 p. 6. | As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): the reply omits the f1040.status != "mfj" guard, asking household.rdp on joint returns (9 completed candidate-unknowns). |
| deepseek | transcription | household.filing_status_conflict | model error | 2,018/2,300 agree; 191 value, 68 candidate-unknown, 23 candidate-refuses; completed: 2 value | i1040gi pp. 13-15. | As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): the reply folds its own HOH and QSS tests into the marriage-entry gate, inheriting household.hoh_fails's error: completed mutation.t2.eic |
| claude | render | qss_eligible | scope | render MISMATCH | p501 p. 11, Kidnapped child, "You may be eligible to file as a qualifying surviving spouse even if the child who qualifies you for this fili | The kidnapped-child rule is outside the tool by the owner's decision (BUG-0273, T-114): the question's No reaches household.qss_fails, whose remedy at f1040.line12e names the rule. As the prior ruling. Project stands. |
| claude | render | filing_status_conflict | scope | render MISMATCH | i1040gi p. 14, Married Filing Separately. | A separate return is refused for the whole return (s3.mfs on scope.ready), so an unmarried MFS filer never reaches this gate; the gate covers the single and joint contradictions (BUG-0286). As the prior ruling. Project s |
| deepseek | render | ctc_ssn | model error | render MISMATCH | i1040gi p. 7, "If you are filing a joint return, only one spouse is required to have a valid SSN in order to be eligible for the CTC and ACT | The other spouse must have either an SSN or ITIN" (amb.2025.ctc_spouse_itin_application). The helper is the filer-side test; the qualifying child's SSN valid for employment is tested per child in dependent.ctc_child, whi |
| deepseek | render | home_cost | model error | render MISMATCH | p501 p. 9, Keeping Up a Home, Note: "if you received Temporary Assistance to Needy Families (TANF) payments or other similar payments and us | Amounts paid out of funds received in the child's or qualifying person's name, such as Social Security, are considered paid by the child, not you. If the total amount you paid is more than the amount others paid, you mee |
| deepseek | render | hoh_community_property | scope | render MISMATCH | i1040gi p. 23. | The part-year community-property case is refused separately by household.cp_marriage_ended on f1040.line1a (BUG-0278); this gate covers the married HOH case. As the prior ruling. Project stands. |
| deepseek | render | test2_persons | representation | render MISMATCH | i1040gi p. 14, Test 2, items 2 to 4 (qualifying children who are not your dependent). | The dependent collection holds every person evaluated for Test 2, and dependent.hoh_test2 counts a qualifying child not claimed as a dependent (its derivation reads dependent.qualifying_child beside dependent.claimed), s |
| deepseek | render | test2_absence_persons | representation | render MISMATCH | i1040gi p. 14, Test 2; p501 p. 9 (BUG-0267). | As test2_persons and the prior ruling: dependent.hoh_absence does not require dependent.claimed where Test 2 allows an unclaimed qualifying child. Project stands. |
| deepseek | render | qss_eligible | scope | render MISMATCH | p501 p. 11, Kidnapped child (outside the tool, BUG-0273; the No reaches household.qss_fails with the remedy at f1040.line12e). | The repeated TANF statement is ruled on home_cost (p501 p. 9 Note). As the prior ruling. Project stands. |
| deepseek | render | filing_status_conflict | scope | render MISMATCH | i1040gi p. 14, Married Filing Separately. | MFS is refused for the whole return by s3.mfs on scope.ready; the gate covers the single and joint contradictions (BUG-0286). As the prior ruling. Project stands. |

Counts: claude transcription model error 5, representation 4, scope 3 (12); deepseek transcription model error 11, scope 1 (12); claude render scope 2 (2); deepseek render scope 3, model error 2, representation 2 (7). Errors introduced: none (BUG-0398 changed only the cites of `household.taxpayer_work_ssn`). Reclassified: Claude `household.taxpayer_work_ssn` (model error to representation: the reply now counts the taxpayer only) and `household.ctc_ssn` (representation to model error: the class M route-limited answers now complete records on which the reply asks `person.tin` of a filer with an SSN valid for employment; no amount differs); deepseek `household.roster_bad` (model error to scope: the reply now states the roster invariant). Findings: none.
