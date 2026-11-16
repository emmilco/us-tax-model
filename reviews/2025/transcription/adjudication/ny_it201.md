# Adjudication — ny_it201 (New York, 2025)

New York logs live under `.transcription/logs/ny/2025/`; this directory has no New York counterpart, so the
New York form's rounds are summarized here.

## Landing round (2026-11-14)

Lane land3-adj11 (claude-opus-5-5, judgment, tax year 2025, jurisdiction ny). Open lines of the Claude
transcription log `.transcription/logs/ny/2025/transcription/ny_it201.md`. `carry.py --jurisdiction ny` ruled
nothing; triage was rerun (`.transcription/triage/ny/2025/ny_it201.json`). The deepseek family is dormant and not
ruled.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | C | representation | log; triage (182 differing witnesses, all on refused returns); form YAML; sa.yaml | IT-201-I p. 5, Item C; owner decision B8 | The reply always asks the New York question; the project asks it after a federal No and takes a federal Yes, but a federal Yes refuses the federal return (sa.deduction refuses when sa.dependent), so on every completed return item C is the New York question. |
| claude | transcription | 1 | ambiguity | log; triage (48 value witnesses, all refused) | IT-201-I p. 2, Entering whole dollar amounts; `amb.ny.2025.whole_dollars` (C4) | The reply copies line 1z in cents; the project rounds half-up as entered, the chosen reading. |
| claude | transcription | 79 | representation | log; triage (no value difference on any return) | IT-201-I p. 23, Line 79 | The project asks about applying an overpayment only when line 77 is more than zero; without an overpayment there is nothing to apply. |

Counts: claude transcription: representation 2, ambiguity 1.

Findings: none. No line left open.

## Landing round (2026-11-14), render

Lane land3-adj11. Open lines of the Claude render log `.transcription/logs/ny/2025/render/ny_it201.md`, ruled on the
rendered English (`rendered/ny/2025/ny_it201.md`), the form YAML and the cited source.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | render | C | scope | MISMATCH; form YAML; sa.yaml; scope.yaml | IT-201-I p. 5, Item C | The spouse and dual-status cases the reply names come only through sa.dependent Yes, which refuses the federal return (and dual-status aliens are refused by the nonresident-alien screen); on completed returns item C is New York's own question. |
| claude | render | 53 | scope | MISMATCH; form YAML; scope.yaml | IT-201-I p. 15, Line 53 | UBT credit: Schedule C (asked) or partnership (scope.k1 refuses); accumulation distribution credit: a trust beneficiary's Schedule K-1 (scope.k1 refuses); part-year City child care credit: part-year City residents refused (ny_it201.gate.part_year_city). |

Counts: claude render: scope 2.

Findings: none. No line left open.

## Landing round (2026-11-14), class M

Lane land3-adj11. Open lines of the Claude class M log `.transcription/logs/ny/2025/classm/ny_it201.md` (6 cases;
98 disagreements, one already ruled; 97 ruled here, every one with `drop`, so the fixture
`fixtures/ny/2025/classm.json` no longer asserts the reply's value). `carry.py --kind classm` ruled nothing.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | classm | cases 1, 2, 3, 4, 6: (39) tax_table, (39) tax_low, 39, 44, 46, (47a), 47a, 49, 52, 54, 58, 61, 62, (80), 80 (75 lines) | interface gap | log; the case prompts (`.classm/classm.ny_it201.N.prompt.txt`, "Amounts given"); `engine/src/classm.ts` buildJob | 2025 New York State and City Tax Tables (`sources/ny/2025/ny_it201_tax_tables.txt`) | The prompt gave "this document, line (39)" and "(47a)" amounts, noted as the shared tax computation, that are the rate-schedule instances on the exact amount ($1,596 / $1,125 at $32,000); lines 39 and 47a read the Tax Tables, which the job neither gave nor included in the pages. The engine matches the published table rows in every case: 32,000 single $1,597 / $1,126; 12,000 MFJ $481 / $370; 36,900 single $1,866 / $1,313; 40,000 MFS $2,037 / $1,432; 64,950 MFJ $3,241 / $2,308. The reply is $1 off on 39 and 47a and on everything below. BUG-0641 (tool). |
| claude | classm | cases 1 to 5: (69a) stc_rr_low, stc_rr_excess_product, stc_rr_high, stc_rr; (chart) sut.top_product, sut.top (22 lines) | ambiguity | log; form YAML | IT-201-I web edition, NYC school tax credit rate-reduction tables; IT-201-I p. 18, Sales and use tax chart; `amb.ny.2025.whole_dollars` (C4) | The engine rounds each rate product half-up where it is computed; the reply carries cents on the helpers. Adding a whole-dollar base, or taking the smaller with $125, commutes with half-up rounding, so the printed lines agree (69a and 59 agree in every case). |

Counts: claude classm: interface gap 75, ambiguity 22.

Findings: BUG-0641 (low; tool, not the engine): class M jobs give a New York form's rate-schedule results
as unnamed "line (39)" / "(47a)" amounts and leave the Tax Table lookups to the model without the tables. No line left
open.

## Goal-1 round (2026-11-15)

Lane b1-adj-ny (claude-opus-5-5, judgment, tax year 2025, jurisdiction ny), in the B1 integration worktree. Open
lines of the Claude transcription log `.transcription/logs/ny/2025/transcription/ny_it201.md` (line-scoped pass
0d1ff4c91631). `carry.py --jurisdiction ny` carried nothing (each line, or what it reads, changed). The deepseek family
is dormant and not ruled.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | 1 | ambiguity | log; triage (3 value witnesses, all refused; other differences come from line 1's whole-return refusal gates, not the compared expression); form YAML | IT-201-I p. 2 and p. 7, Entering whole dollar amounts; `amb.ny.2025.whole_dollars` (C4) | The reply copies line 1z in cents; the project rounds half-up as entered, the chosen reading. As ruled 2026-11-04. |
| claude | transcription | (81) safe_harbor_100 | ambiguity | log; triage (4,606 of 4,608 agree; 2 witnesses, refused) | IT-201-I p. 23, Line 81; `amb.ny.2025.whole_dollars` (C4) | The project rounds the rate product once to the dollar; the reply keeps cents. |
| claude | transcription | (81) safe_harbor_110 | ambiguity | log; triage (4,606 of 4,608 agree; 2 witnesses, refused) | IT-201-I p. 23, Line 81; `amb.ny.2025.whole_dollars` (C4) | As safe_harbor_100; at most a 50-cent difference in the threshold. |

Counts: claude transcription: ambiguity 3.

Findings: none. No line left open.

## Goal-1 round (2026-11-15), render

Lane b1-adj-ny. Open line of the Claude render log `.transcription/logs/ny/2025/render/ny_it201.md` (pass
f0a2b74716ce), ruled on `rendered/ny/2025/ny_it201.md`, the form YAML and the cited source.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | render | 48 | finding (low) | MISMATCH; form YAML (gate.hh_city_mfs, hh_city_in_range, hh_city_by_status) | IT-201-I web edition, NYC household credit table 6, "federal adjusted gross income (see Note 4) total from both returns"; Note 2, "could be 0 or a negative amount" | The MFS refusal tests only this return's line 19 against $22,500, and MFS otherwise gets zero; a spouse's negative AGI can bring the total within the rows, where a credit is allowed. Sibling line 40 (table 3, gate.hh_state_mfs, $32,000) has the same defect. |

Counts: claude render: finding 1.

Findings: BUG-0762 (low; amount-affecting in a rare case): the MFS household credit gates should
also refuse when the spouse's federal AGI is negative. No line left open.
