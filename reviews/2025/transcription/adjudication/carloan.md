# Adjudication — carloan

Method: `README.md` in this directory.

## Round 4

Fresh reviews of 2026-10-27 (Claude claude-opus-5-5 and deepseek-flash) of the subject after BUG-0175. That fix makes
column (ii) the QPVLI part of the Schedule C interest: `carloan.sc_interest` prorated by the loan's qualifying ratio
(`sc_mixed`/`sc_refi` → `sc_allocated`), and zero for an ineligible loan. Triage records `../triage/carloan.json` and
`../triage/carloan.deepseek.json` (executable-triage-v2; 1,111 fixtures, 500 generated returns seed 20261026, 74 partial
records; 151 comparisons per line). The full ruling text is in `.transcription/proposed/round4/transcription.carloan[.deepseek].json`,
`render.carloan[.deepseek].json` and `classm.carloan.json`, and the findings are in `.transcription/proposed/round4/carloan.findings.md`.
Every review was given i1040gi pp. 23, 109–110, fr-2025-24154 pp. 20–23 and i1040sc p. 6. Those pages hold every
deciding sentence, so there is no page gap. Example 1's ending is on p. 24 and is not needed.

BUG-0175 check: the fix is right. (g)(1) admits to column (ii) only interest "that is QPVLI". (d)(2)(iii)(A) and (d)(4)
allocate every payment of interest pro rata, so the QPVLI part of the Schedule C interest is the qualifying ratio times
that interest. Refinanced and inherited loans use the same ratios as `carloan.qpvli`. The six-place ratio is
`amb.2025.carloan_ratio_places`. The Claude candidate independently encodes the same reading (to nine places).

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | 22(ii) | ambiguity; representation | 128/151; 2 value, 21 candidate-unknown (13 completed) | i1040gi p. 110 col (ii); fr-2025-24154 pp. 21, 23, (d)(2)(iii)(A), (d)(4), (g)(1) | Same proration; classm.carloan.3 $551.52 / $551.51 is the nine-place ratio (register); the rest is column (ii) supplied or needed without a Schedule C. |
| claude | transcription | 22(iii) | ambiguity; representation | 131/151; 2 value, 18 candidate-unknown | i1040gi p. 110 col (iii) | Follows column (ii): $1,654.54 / $1,654.55 ratio places; classm.carloan.2 column (ii) without a Schedule C. |
| deepseek | transcription | 22(ii) | model error | 114/151; 3 value, 34 candidate-unknown | fr-2025-24154 pp. 21, 23 | Smaller of the whole Schedule C interest and the QPVLI, not prorated (stage12.car.mixed_sc_interest_prorated $84.80 / $106.00). |
| deepseek | transcription | 22(iii) | model error | 106/151; 18 value, 27 candidate-unknown (17 completed) | fr-2025-24154 p. 21, (d)(2)(iii)(A) | Needs the amount financed on unmixed loans (stage12.car.basic); column (ii) unprorated ($254.40 / $233.20); three-place ratio (register). |
| claude | render | 22(ii) | scope | MISMATCH: Schedules E and F omitted | i1040gi p. 110; scope.schedule1 | E and F refused at Form 1040 lines 8 and 10; the English states the BUG-0175 proration correctly. |
| deepseek | render | 22(ii) | scope | MISMATCH: Schedules E and F omitted | i1040gi p. 110; scope.schedule1 | As the Claude render. |
| claude | classm | classm.carloan.3 — carloan[vin_1].col_ii | ambiguity (drop) | project $551.52 / model $551.51 | fr-2025-24154 p. 21 | Exact ratio, the register's alternative; proration agrees. |
| claude | classm | classm.carloan.3 — carloan[vin_1].col_iii | ambiguity (drop) | project $1,654.54 / model $1,654.55 | i1040gi p. 110 col (iii) | Same one-cent ratio difference through column (ii). |

Findings (low, no amount changes; `.transcription/proposed/round4/carloan.findings.md`): F1, the `carloan.qpvli` citation
still says column (ii) is outside the tool; F2, `amb.2025.carloan_ratio_places` does not name `carloan.sc_mixed_prorated`
and `carloan.sc_refi`. No reviewed return is misstated. A Schedule C interest entry larger than the loan's interest is
not screened, and no record reaches that case (uncertainty, not a finding).

## Round 1 (superseded subject)

Triage records (executable-triage-v1; 1,083 fixtures, 500 generated returns, seed 20261026, 77 partial records). Later
rulings before round 4 are archived in `.transcription/archive/before-round4-2026-10-27/`.

| family | line | class | triage | deciding source | reason |
| --- | --- | --- | --- | --- | --- |
| claude | 22(iii) | representation | 111/141 agree; 28 candidate-unknown, 2 value | i1040gi p. 110, line 22 column (ii) | Column (ii) can be nonzero only with a Schedule C inside scope (Schedules E and F refused by `scope.schedule1`); every difference is a return without one. |
| deepseek | 22(iii) | model error | 102/141 agree; 32 candidate-unknown, 4 project-unknown, 3 value | fr-2025-24154 p. 21, proposed § 1.163-16(d)(2)(iii)(A) | Prorates every loan, mixed or not, so it requires the amount financed on loans the text needs no allocation for. |

Findings: none. Project lines unchanged.
