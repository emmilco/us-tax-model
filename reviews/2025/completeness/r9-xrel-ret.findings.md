# Completeness review, round 9 (xrel, sampled release reviews): adjudication of the ret family

Family `ret` (forms `retirement`, `ira`, `f8606`, `f5329`, `ssb`, `sli`, `f8889`, `f8853c`, `f8959`). 23 claims were
unruled at the B1 plus expansion tree (`.claude/worktrees/xint`); `f8853c` had none. The rulings are in the fragment
`/tmp/xrel/frag/ret.completeness.json`, keys `unruled:<form>#1.<n>`, each with the record's current `subject_sha`; the
lead merges them into `rulings.json`. `xrel.py merge` (no `--write`) refuses none of them. The three real gaps that cite
a pending bug (`BUG-NEW-…`) fail the gate until the numbered-bug pass, which is accepted for tonight.

Earlier rulings of these forms were leads only. Each claim was checked against the current lines (`forms/2025/*.yaml`,
`rendered/2025/*.md`), the interview wording (`interview/2025/questions.yaml`) and the quoted source. Four claims that
turn on a refusal were evaluated with `node engine/dist/main.js --year 2025 eval` on copies of current fixtures with one
input changed (`/tmp/xrel/ret/ev.py`): f8889#1.1, f8959#1.1, ira#1.2 and ssb#1.1. Three earlier rulings no longer hold
because of B1:
- f8606#1.1 was a real gap (BUG-0402, reservist repayment). The repayment is now refused for the whole return by
  `scope.other_income`.
- ira#1.4 was out of scope by `s3.mfs`. Separate returns are now in scope, so it is ruled presentation.
- f8889#1.2 relied on S corporation filers being refused elsewhere. Schedule K-1 (Form 1120-S) is now in scope (`k1s`),
  so it is ruled a real gap.

## Counts

| Form | Claims | Real gap | Covered | Out of scope | Presentation | Wrong |
|---|---|---|---|---|---|---|
| f5329 | 4 | 0 | 0 | 3 | 0 | 1 |
| f8606 | 2 | 0 | 1 | 1 | 0 | 0 |
| f8889 | 5 | 2 | 1 | 1 | 1 | 0 |
| f8959 | 1 | 0 | 0 | 1 | 0 | 0 |
| ira | 4 | 0 | 1 | 2 | 1 | 0 |
| retirement | 5 | 3 | 0 | 0 | 2 | 0 |
| sli | 1 | 1 | 0 | 0 | 0 | 0 |
| ssb | 1 | 0 | 0 | 1 | 0 | 0 |
| **total** | 23 | 6 | 3 | 9 | 4 | 1 |

Pending bugs filed: BUG-0877 (f8889, low) and BUG-0878 (retirement, low). Also cited:
BUG-0871 (retirement#1.2; BUG-0880, filed by the false-no adjudication, duplicates it) and
BUG-0881 (sli#1.1).

## f5329 (subject fb900ebb)

| Claim | Item | Class | Where |
|---|---|---|---|
| #1.1 | l2: exception conditions and dollar limits | wrong | Caps are in `person.x_cap09`/`x_cap19`/`x_c05`/`x_c22`/`x_c23` → `person.x_limited_sum`. Conditions are in the `retirement.exception` question, and `retirement.wrong_kind` refuses a mismatched plan type. The 3-year emergency bar is refused by `retirement.early_screen`. Only the birth/adoption statement is left, and it is an attachment. |
| #1.2 | l1: earnings on withdrawn excess IRA contributions (exception 21) | out of scope (`retirement.special`) | A code 8/P Form 1099-R is refused by `retirement.ira_returned_if_ira` → `retirement.special`, and as code `other` by `retirement.bad_code`. |
| #1.3 | must: taxable Roth distribution, code other than 1 | out of scope (`retirement.bad_code`) | Roth non-Q and code J are refused. Must-file only decides whether the form is attached. |
| #1.4 | l47: HSA excess withdrawn by the due date | out of scope (`f8889.excess_withdrawn`) | The question covers withdrawals through the extended due date. The 6-month window falls on an amended return. |

## f8606 (subject 2a93dc6c)

| Claim | Item | Class | Where |
|---|---|---|---|
| #1.1 | line1: SEP/SIMPLE, recharacterization, limit, reservist repayment, returned contributions | covered (`person.ira_trad`) | Exclusions are in `person.ira_trad`'s question and help. `person.ira_excess` and `person.ira_over_limit` refuse. `scope.reservist_repaid` → `scope.other_income` refuses Form 1040. |
| #1.2 | files: Roth or inherited Roth distribution, stand-alone filing | out of scope (`retirement.bad_code`) | Roth non-Q is refused. Inherited traditional basis is the open BUG-0871. The stand-alone form needs no Form 1040. |

## f8889 (subject 58083581)

| Claim | Item | Class | Where |
|---|---|---|---|
| #1.1 | line13: prior-year excess | out of scope (`person.x_other`) | Evaluated: `stage11.hsa.self_full_year` + `x_hsa_prior_excess` refuses `f1040.line24`. |
| #1.2 | line2: cash only; 2% S corporation shareholder | real gap, BUG-0877 | Cash only is now in the help (BUG-0678). Open: the 2% shareholder-employee's contribution is left off line 2. |
| #1.3 | medical: LTC premium age limit, late excess withdrawal, rollover-funded HSA establishment date | real gap, BUG-0877 | The LTC limit and the establishment date are missing. The late-withdrawal case is unreachable (BUG-0678). |
| #1.4 | fsa: grace-period coverage with a zero balance | covered (`f8889.fsa`) | The help now carries the zero-balance rule. |
| #1.5 | coverage: line 1 checkbox | presentation | The coverage answers figure the amounts. The box changes none. |

## f8959 (subject d8e69b49)

| Claim | Item | Class | Where |
|---|---|---|---|
| #1.1 | line19: W-2 box 12 codes B and N | out of scope (`s2.other`) | `s2.w2_marks` names codes B and N. Evaluated: `stage4.base` + `s2.w2_marks` refuses `s2.line21` and `f1040.line24`. |

## ira (subject 04dc191c)

| Claim | Item | Class | Where |
|---|---|---|---|
| #1.1 | line11a: 2024-deducted contributions, rollovers, trustee fees | covered (`person.ira_trad`) | The question and help exclude all three. |
| #1.2 | over_comp: contributions over the dollar limit | out of scope (`person.ira_over_limit`) | Evaluated: fixture `stage16.refuse.person.ira_over_limit` refuses `s1.line20`. |
| #1.3 | excl_gate: Form 8815, excluded adoption benefits | out of scope (`sb.unsupported`) | Adoption benefits are refused by `scope.other_income`. |
| #1.4 | line20: MFS lived-apart checkbox | presentation | MFS is in scope now. The answer is used, but no line produces the box. No amount changes. |

## retirement (subject 39901ba6)

| Claim | Item | Class | Where |
|---|---|---|---|
| #1.1 | disability: plan without disability retirement | real gap, BUG-0878 | Wages or pension line, which changes earned income for EIC. |
| #1.2 | ira_basis: inherited IRA basis | real gap, BUG-0871 | Already filed by the people fork. |
| #1.3 | not_beneficiary: surviving spouse treating the IRA as own | real gap, BUG-0878 | A code 4 distribution under 59½ escapes the 10% tax. |
| #1.4 | has_rollover: rollover statement | presentation | Attachment. The amount is asked. |
| #1.5 | exception: exception 19 statement | presentation | Attachment. The cap is applied. |

## sli (subject 2bfcd5aa)

| Claim | Item | Class | Where |
|---|---|---|---|
| #1.1 | unqualified_any: category 3 dependents, degree program, eligible student and institution | real gap, BUG-0881 | The help names category 3 and the degree program (the claim read only the prompt). Nothing asks about an eligible institution or eligible student. Low, filed with the false-no finding. |

## ssb (subject e9b895df)

| Claim | Item | Class | Where |
|---|---|---|---|
| #1.1 | ira_covered: spouse-only coverage | out of scope (`ira.cov_gate`) | Evaluated: `stage16.ira.i10` + `ira_work_plan`, with `ssb.ira_covered` false, refuses `f1040.line6b`. |
