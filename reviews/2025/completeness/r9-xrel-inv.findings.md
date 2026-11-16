# Completeness review, round 9 (xrel, sampled release reviews): adjudication of the inv family

Family `inv` (forms `sb`, `div`, `interest`, `sd`, `qdcg`, `qdcg_amount`, `f4952`, `f8960`, `clcw`, `clcw_next_year`, `ftc`,
`f1116`, `f1116col`, `f1116sb`, `f1116sbyr`, `gift`, `sales`, `tax_on_amount`). 32 claims were unruled at the B1 plus
expansion tree (`.claude/worktrees/xint`). The rulings are in the fragment `/tmp/xrel/frag/inv.completeness.json`, keys
`unruled:<form>#1.<n>`, each with the record's current `subject_sha`; the lead merges them into `rulings.json`.
`xrel.py merge` (no `--write`) refuses none of them; the four real gaps cite pending ids and fail the gate until they are
numbered, as expected.

Earlier rulings of these forms were leads only. Each claim was checked against the current lines (`forms/2025/*.yaml`), the
interview wording (`interview/2025/questions.yaml`), and its quote against `sources/2025/*.cols.txt`. No new evaluation was
needed: where an amount mattered, the line's formula or refusal settles it (for example `table_tax`'s joint column in
`tables/2025/tax_table.yaml`, `f4952.line4d` reading `sd.line16`).

## Counts

| Form | Claims | Real gap | Covered | Out of scope | Presentation | Wrong |
|---|---|---|---|---|---|---|
| clcw_next_year | 2 | 0 | 0 | 2 | 0 | 0 |
| f1116 | 5 | 0 | 0 | 4 | 1 | 0 |
| f1116col | 3 | 0 | 0 | 3 | 0 | 0 |
| f1116sb | 3 | 1 | 1 | 1 | 0 | 0 |
| f1116sbyr | 1 | 0 | 0 | 1 | 0 | 0 |
| f4952 | 1 | 0 | 1 | 0 | 0 | 0 |
| f8960 | 2 | 1 | 0 | 1 | 0 | 0 |
| ftc | 1 | 0 | 0 | 1 | 0 | 0 |
| gift | 3 | 0 | 1 | 0 | 2 | 0 |
| interest | 1 | 0 | 0 | 1 | 0 | 0 |
| qdcg | 2 | 0 | 0 | 2 | 0 | 0 |
| sales | 4 | 2 | 0 | 2 | 0 | 0 |
| sb | 2 | 0 | 0 | 0 | 2 | 0 |
| sd | 1 | 0 | 0 | 1 | 0 | 0 |
| tax_on_amount | 1 | 0 | 1 | 0 | 0 | 0 |
| **total** | 32 | 4 | 4 | 19 | 5 | 0 |

## Rulings

| Claim | Item | Class | Where |
|---|---|---|---|
| clcw_next_year#1.1 | canceled debt excluded in 2025 (i1040sd p. 10) | out of scope | `s1.cod_unsupported` |
| clcw_next_year#1.2 | joint-return carryover on a separate return (p550 p. 103) | out of scope | `clcw.spouse_screen`; the 2026 split changes no 2025 amount |
| f1116#1.1 | USVI tax, accrual election, section 909 release, section 960 (i1116 pp. 2, 18-19) | out of scope | `s3.virgin_islands`; `f1116.not_on_statement`; `scope.cfc` |
| f1116#1.2 | excess deductions between groups; non-withholding tax group (Reg. 1.904-4) | out of scope | ratable apportionment leaves nothing to reallocate; `f1116.not_on_statement` |
| f1116#1.3 | AMT special rules; Form 4952 line 4g dividends (i1116 pp. 9-10) | out of scope | `s2.amt`; the 4g case can only over-refuse |
| f1116#1.4 | treaty re-sourcing credit (i1116 p. 2) | out of scope | `f1116.not_on_statement` |
| f1116#1.5 | statement of lines 3a and 3b expenses | presentation | |
| f1116col#1.1 | qualified dividend adjustment, HTKO (i1116 pp. 9-11) | out of scope | `f1116.adjust`, `f1116.high_taxed` |
| f1116col#1.2 | lines 2, 4b, 5 (i1116 pp. 11, 17-18) | out of scope | `f1116.asset_method`, `f1116.itemized_unread` |
| f1116col#1.3 | group deductions; section 901(k) | out of scope | deductions are apportioned (`f1116.exp_hi/lo`); `f1116.tax_mismatch` |
| f1116sb#1.1 | carryover through a 2024 deduction or election year (i1116 p. 19, p514 p. 38) | **real gap** | BUG-0827 |
| f1116sb#1.2 | spouses' allocation cases (p514 p. 39) | covered | `f1116sb.split`; `f1116sbyr.amount` adds both spouses |
| f1116sb#1.3 | bankruptcy reduction of carryovers (p514 p. 38) | out of scope | `s1.cod_unsupported` |
| f1116sbyr#1.1 | Schedule B line 2 adjustments | out of scope | `f1116sb.changed_if_carry` |
| f4952#1.1 | capital loss carryovers in line 4d | covered | `f4952.line4d` (Schedule D line 16) |
| f8960#1.1 | foreign tax deducted, line 9b | out of scope | `sa.unsupported` |
| f8960#1.2 | section 6013(g)/(h) NIIT election (i8960 pp. 4, 7) | **real gap** | BUG-0828 |
| ftc#1.1 | deduction instead of credit; treaty credit | out of scope | `sa.unsupported`; `f1116.not_on_statement` |
| gift#1.1 | public securities claimed off-market (Reg. 1.170A-13(c)(7)(xi)) | covered | `gift.deduction` asks the sale value |
| gift#1.2 | statement of the reduction | presentation | |
| gift#1.3 | Section A details, $500 filing threshold | presentation | |
| interest#1.1 | market discount, CPDI, seller-financed interest | out of scope | `sb.unsupported_if_income` |
| qdcg#1.1 | Form 2555 footnote, line 2 | out of scope | `sa.excluded_income` |
| qdcg#1.2 | Form 2555 footnote, line 3; line 7b box | out of scope | `sa.excluded_income`; the box is a checkbox |
| sales#1.1 | section 1244 / 1242 ordinary loss | out of scope | `sd.small_business_stock` |
| sales#1.2 | trader mark-to-market; dealers | out of scope | `sd.trader_election` |
| sales#1.3 | gifted digital asset without donor's basis; unstated interest (p550 pp. 59-60) | **real gap** | BUG-0829 |
| sales#1.4 | gifted digital asset holding period (p550 p. 82); code T | **real gap** | BUG-0829 (code T: no amount) |
| sb#1.1 | line 1 payer list | presentation | |
| sb#1.2 | line 5 payer list | presentation | |
| sd#1.1 | 2025 separate return after a 2024 joint carryover | out of scope | `clcw.spouse_screen` |
| tax_on_amount#1.1 | qualifying surviving spouse column | covered | `table_tax` (joint column holds `qss`) |

## Defects filed (pending, prefix xrelinv)

- **BUG-0827** (low): a foreign tax carryover through a 2024 deduction or no-Form-1116 election year is entered
  from an older Schedule B without the reduction; `f1116sb.prior_year` is asked only when a carryover is generated. Proposed
  fix: ask it, or refuse, when a carryover is claimed.
- **BUG-0828** (low): a section 6013(g) joint return figures the NIIT on combined income with the joint threshold,
  without the NIIT election; `scope.nonresident` can be answered No for a spouse treated as resident. Proposed fix: name the
  election in `scope.nonresident`'s help, or a refusing question on Form 8960.
- **BUG-0829** (low): `sales.correct_basis` and `sales.box` omit the gifted-digital-asset rules (zero basis, holding
  period from receipt without the donor's records) and the unstated-interest reduction. Proposed fix: one bullet each.

## Notes

- **MFS.** `s3.mfs` is gone. sd#1.1 (whose earlier ruling relied on it) and clcw_next_year#1.2 rest on `clcw.spouse_screen`,
  which asks whether the 2024 joint return's figures go to a 2025 return that is not joint with the same spouse, and refuses.
- **Repeats.** clcw_next_year#1.1, f4952#1.1, f8960#1.1, ftc#1.1, gift#1.2-1.3, interest#1.1, sales#1.1-1.2 and
  tax_on_amount#1.1 repeat earlier rulings, each rechecked against the current lines.
