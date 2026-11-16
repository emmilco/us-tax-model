# Completeness review, round 10 (xrr, release rerun after the xint integration): adjudication of the rinv family

Family `rinv` (forms `sb`, `div`, `interest`, `sd`, `qdcg`, `qdcg_amount`, `f4952`, `f8960`, `clcw`, `clcw_next_year`, `ftc`,
`f1116`, `f1116col`, `f1116sb`, `f1116sbyr`, `gift`, `sales`, `tax_on_amount`), tax year 2025, us. Of the family's 34
completeness items, 11 were unruled at the current subjects: the new samples of `f1116` (5), `f1116col` (5) and `ftc` (1),
whose subjects changed since the xrel round. The other 23 items already carry a ruling at their current subject and were
not ruled again; no item is due or short. The rulings are in the fragment `/tmp/xrr/frag/rinv.completeness.json`, keys
`unruled:<form>#1.<n>`, each with the record's current `subject_sha`; the lead merges them. `xrr.py merge` (no `--write`)
refuses none of them. One fork, claude-opus-5-5, judgment.

The xrel rulings of the same forms (r9-xrel-inv) were leads only. Each claim was checked against the current lines
(`forms/2025/ftc.yaml`, `f1116.yaml`, `f1116col.yaml`, `sa.yaml`, `s3.yaml`), the interview wording
(`interview/2025/questions.yaml`) and its quote in `sources/2025/` (i1116, p514, cfr-26-1-904-4). Where a refusal or amount
mattered it was evaluated on copies of `fixtures/2025/f1116.json` cases resolved with `tools/fixture_inputs.py`
(inputs under `/tmp/xrr/rinv/`). The changes of this round (`ftc.needs1116` also tests `sa.excluded_income`; separate
returns supported) do not alter any of these rulings; the married-filing-separately exception ceiling is $197,300 as the
source states.

## Counts

| Form | Claims | Real gap | Covered | Out of scope | Presentation | Wrong |
|---|---|---|---|---|---|---|
| f1116 | 5 | 0 | 0 | 4 | 1 | 0 |
| f1116col | 5 | 0 | 1 | 4 | 0 | 0 |
| ftc | 1 | 0 | 0 | 1 | 0 | 0 |
| **total** | 11 | 0 | 1 | 9 | 1 | 0 |

## Rulings

| Claim | Item | Class | Where |
|---|---|---|---|
| f1116#1.1 | credit and deduction of the same year's foreign tax (i1116 p. 2; p514 p. 38) | out of scope | `sa.unsupported` |
| f1116#1.2 | accrual election, "Accrued" box (i1116 p. 18) | out of scope | `f1116.not_on_statement` |
| f1116#1.3 | tax paid to the U.S. Virgin Islands, Form 8689 (i1116 p. 2) | out of scope | `s3.virgin_islands_if_foreign` |
| f1116#1.4 | passive income bearing only a non-withholding foreign tax (Reg. 1.904-4(c)(3)) | out of scope | `f1116.not_on_statement` |
| f1116#1.5 | statement listing the line 3a and 3b expenses (i1116 p. 17) | presentation | none |
| f1116col#1.1 | qualified dividend adjustment and its exception (i1116 pp. 9-10) | out of scope | `f1116.adjust` |
| f1116col#1.2 | lines 2, 4b and 5 set to zero (i1116 pp. 17-18) | out of scope | `f1116.asset_method` |
| f1116col#1.3 | line 3c from lines 3a and 3b (i1116 p. 17) | covered | `f1116.line3c` |
| f1116col#1.4 | tax disallowed under section 901(k) in the grouping (Reg. 1.904-4(c)(3)) | out of scope | `f1116.tax_mismatch` |
| f1116col#1.5 | high-taxed income, HTKO columns (i1116 p. 11; Reg. 1.904-4(c)) | out of scope | `f1116.high_taxed` |
| ftc#1.1 | deduction instead of credit; additional treaty credit (i1116 p. 2) | out of scope | `sa.unsupported` |

## Findings

- **Credit and deduction (f1116#1.1, ftc#1.1).** `sa.foreign_tax_deduct` is asked of every filer with foreign tax; a Yes sets
  `sa.unsupported` and refuses the return (evaluated: `ftc.credit` and `s3.line1` refused at `sa.unsupported`). On a No,
  Schedule A line 6 is a constant zero and `f1116.line3a_itemized` reads only lines 4 and 5e, so no prepared return both
  credits and deducts the year's foreign tax. The treaty credit of ftc#1.1 concerns tax paid directly to the residence
  country: a No to `ftc.statements` refuses at `f1116.not_on_statement` (evaluated).
- **Accrual election (f1116#1.2).** Only tax withheld at source and reported on a payee statement reaches Form 1116; it is
  paid and accrued at withholding, so line 8 is the same on either basis. Directly paid tax refuses at
  `f1116.not_on_statement`. The checkbox is filing presentation.
- **U.S. Virgin Islands (f1116#1.3).** `s3.virgin_islands` is asked under `s3.foreign_any` (which names territory income);
  a Yes refuses the return at Schedule 3 line 14 (evaluated: `f1040.line24` and `line37` refused at
  `s3.virgin_islands_if_foreign`).
- **Grouping (f1116#1.4, f1116col#1.4, f1116col#1.5).** The claims that nothing allocates deductions to the groups or
  refuses high-taxed income are wrong: `f1116.exp_hi`/`exp_lo`, `net_hi`/`net_lo` and `limit_hi`/`limit_lo` test each group
  at 37 percent, and `f1116.high_taxed` refuses line 35 (fixture `f1116.c3_htko_over`, evaluated). A non-withholding foreign
  tax is not on a payee statement and refuses at `f1116.not_on_statement`; K-1 foreign taxes refuse in `k1p` and `k1s`. A
  section 901(k) tax left out of `ftc.taxes` but in the column's box 7 amount refuses at `f1116.tax_mismatch` (evaluated:
  ftc.taxes $500, column $600). The residue (a fund's box 7 treated as withholding tax; a column straddling 15 percent) is
  recorded in `amb.2025.f1116_high_taxed`.
- **Adjustments and zeroed lines (f1116col#1.1, #1.2).** The adjustment is computed from QDCG worksheet lines 5, 23 and 24
  (or the Schedule D Tax Worksheet) and refused at `f1116.adjust` when the exception fails (fixtures `c6_adjust_ceiling`,
  `c7_adjust_20000`, evaluated). Line 4b refuses at `f1116.asset_method`, line 2 at `f1116.itemized_unread` (fixtures
  `c4_asset_method`, `c4_state_income_tax`, evaluated); foreign capital gains and losses at `f1116.foreign_gain`; the AMT at
  `s2.amt`.
- **Line 3c (f1116col#1.3).** Defined on the form, not the column: `f1116.line3c` = `f1116.line3a` (standard deduction or
  Schedule A lines 4 and 5e) + `f1116.line3b` (Schedule 1 line 26 less line 21); the Schedule 1-A senior deduction enters
  neither. Covered.

No defect was found and no pending bug was filed.
