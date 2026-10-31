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

## Fix round 5

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
