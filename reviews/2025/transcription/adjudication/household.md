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

## Round 2

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
