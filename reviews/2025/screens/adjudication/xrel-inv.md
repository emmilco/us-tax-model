# Screen and false-no adjudication, xrel inv family (2026-11-15, sampled release reviews)

Family `inv`: forms `sb`, `div`, `interest`, `sd`, `qdcg`, `qdcg_amount`, `f4952`, `f8960`, `clcw`, `clcw_next_year`, `ftc`,
`f1116`, `f1116col`, `f1116sb`, `f1116sbyr`, `gift`, `sales` and `tax_on_amount`, tax year 2025, us. The samples are the
sampled release reviews at the B1 plus expansion tree (`.claude/worktrees/xint`). Rulings are in the fragments
`/tmp/xrel/frag/inv.screens.json` (24 samples) and `/tmp/xrel/frag/inv.false_no.json` (21 samples), each with its unit's
current `subject_sha`; the lead merges them. `xrel.py merge` (no `--write`) refuses none of them. Samples already ruled at
the current subject (5 screens, 1 false-no) were not ruled again. One fork, claude-opus-5-5, judgment.

Each finding was checked against the form YAML, the interview wording as asked (the bank prompt and help, which several
reviewers did not see: they saw a gate's label), and the cited source. Earlier rulings of the same units were leads only;
two of them no longer hold: the earlier div rulings relied on words of `div.any` ("dividends received without any form",
"nondividend distributions", "liquidation distributions") that the redraft removed. No ruling relies on the removed gate
`s3.mfs`; separate returns now reach `sb.nominee` (BUG-0832).

Common grounds used below: any Schedule K-1 is a Yes to `scope.k1` ("A Yes ends the interview here"), and K-3s are refused
(`k1p.r_b16`, `k1s.box14`); Form 8814 is refused by `scope.f8814` through `scope.other_line16`; foreign tax not on a U.S.
payee statement is refused by `f1116.not_on_statement`; the foreign trigger question as asked (`s3.foreign_any`) names "income
from a U.S. territory" and the spouse.

## Counts

| Tool | Samples | Findings | covered | accepted WIDE | accepted (minor, residual, no amount) | model error | presentation | out of scope | defect |
|---|---|---|---|---|---|---|---|---|---|
| screens | 24 | 88 | 22 | 24 | 11 | 1 | 2 | 14 | 14 |
| false-no | 21 | 119 | 25 | 1 | 42 | 5 | 1 | 17 | 28 |

"Accepted (minor, residual, no amount)" groups the classes `accepted (minor UNCLEAR)`, `accepted (minor UNCLEAR, leans WIDE)`,
`accepted residual` (the known foreign-tax residuals cite BUG-0620, as earlier rulings did), `accepted (no defect)` and
`accepted (no amount)`.

No gate computes a wrong condition. The defects are question wording that is narrower than the source or than the
question the gate opens, filed as six pending entries (below).

## Defects (pending, prefix xrelinv)

- **BUG-0830** (medium): `div.other_boxes` ("Look at your ... Forms 1099-DIV"; help "If you have no Form 1099-DIV,
  answer No") turns away a return of capital or liquidating distribution received without a form, and a share of a box 2b
  or 2d amount on a form in another person's name, which the box questions it opens count. Proposed fix: reword the question
  and replace the help. Units: div.other_boxes_if_dividends, div.has_return_of_capital, div.capital_gain_boxes,
  div.ordinary_boxes (false-no); div.any's two low residuals are recorded in the same entry.
- **BUG-0831** (low): the foreign gates (`sb.account_any`, `sb.asset_any`, `sb.trust_any`, `sb.company_any`) are
  narrower than the questions they open: indirect financial interests (over-50% entities, disregarded entities, grantor
  trusts), the trust control test, sales, loans, free use, intermediaries and past-tense connections, voting power,
  indirect or option holdings and territory companies. Proposed fix: carry the gated questions' widening words into the
  gates. Units: gate:sb.foreign_any, gate:sb.foreign_company_any, gate:sb.foreign_trust_any (both tools).
- **BUG-0832** (low): `sb.bonds_any`'s help excludes certificates of deposit, though a brokered CD can carry the
  accrued-interest, premium, market discount or OID adjustments `sb.bond_special` lists; `sb.nominee` speaks only of joint
  returns, and separate returns now reach it. Proposed fix: two help sentences.
- **BUG-0833** (medium): `f4952.line1`'s prompt "Leave out interest on a home loan" drops interest on a home equity
  loan whose money bought investments (the form's own source excludes only qualified residence interest); `f4952.carryover`
  asks only for line 7 of a 2024 Form 4952, missing a carryforward through a year without one. Proposed fix: reword both.
- **BUG-0834** (low): Form 1116 screens tied to an earlier Form 1116 or its estimate: `f1116.loss_accounts` misses a
  loss of a year without a Form 1116; a carryover created by a smaller actual carryback, a carryback without an estimate and
  a correction of the 2024 line 8 are not named (`ftc.carryover`, `f1116sb.changed`); `f1116sb.prior_year` is singular for a
  2025 joint couple after separate 2024 returns. Proposed fix: reword and add help.
- **BUG-0835** (low): `sd.sold_other` does not name oil, gas or mineral property, which `sd.business_property`
  (behind it) names and refuses. Proposed fix: name it in the gate.

The completeness rulings of the same family filed BUG-0827 to -03 (`reviews/2025/completeness/r9-xrel-inv.findings.md`).

### Screens

| Unit | Findings (n: class) | Disposition |
|---|---|---|
| `f1116.foreign_gain#1` | 0: covered; 1: covered | no gate defect; both NARROW are computed elsewhere |
| `f1116.loss_accounts#1` | 0: covered; 1: out of scope; 2: covered; 3: defect (BUG-0834); 4: defect (BUG-0834) | defect (low): the question is tied to an earlier Form 1116 |
| `f1116.redetermination#1` | 0: out of scope; 1: accepted (minor UNCLEAR); 2: accepted (minor UNCLEAR); 3: accepted WIDE | no gate defect; the K-3 case is refused, the rest minor or wide |
| `f1116.reduction#1` | 0: out of scope; 1: covered; 2: accepted WIDE | no gate defect: the K-3 case is refused and the boycott is named |
| `f1116sb.changed#1` | 0: defect (BUG-0834); 1: defect (BUG-0834); 2: accepted (minor UNCLEAR) | defect (low): a correction of the 2024 line 8 and a carryback without an estimate are not named |
| `f1116sb.split#1` | 0: covered | no gate defect |
| `f4952.alternative_allocation#1` | 0: covered; 1: accepted WIDE | no gate defect; as the earlier ruling |
| `f4952.unsupported#1` | 0: covered; 1: accepted WIDE; 2: accepted WIDE; 3: accepted (minor UNCLEAR, leans WIDE) | no gate defect; as the earlier ruling |
| `f8960.refund#1` | 0: covered; 1: accepted WIDE; 2: accepted (minor UNCLEAR, leans WIDE) | no gate defect; as the earlier ruling (rechecked) |
| `f8960.unsupported#1` | 0: covered; 1: out of scope; 2: out of scope; 3: out of scope; 4: accepted WIDE; 5: accepted WIDE; 6: accepted WIDE | no gate defect: each NARROW case is screened or refused by another question |
| `gift.special#1` | 0: accepted (minor UNCLEAR); 1: accepted WIDE | no gate defect: the question as asked is a list |
| `sales.special#1` | 0: accepted WIDE; 1: accepted WIDE; 2: accepted WIDE | no gate defect: WIDE |
| `sb.line8#1` | 0: accepted WIDE; 1: accepted WIDE | no gate defect: WIDE by design |
| `sd.f2439#1` | 0: covered; 1: covered; 2: covered; 3: accepted (minor UNCLEAR) | no gate defect: the other Schedule 3 line 13 items have their own questions |
| `gate:div.has_ordinary#1` | 0: out of scope; 1: covered; 2: covered | no gate defect; as the earlier ruling (rechecked) |
| `gate:f4952.has_interest#1` | 0: out of scope; 1: accepted (minor UNCLEAR); 2: accepted (minor UNCLEAR) | no gate defect: the K-1 case is refused; the rest minor |
| `gate:ftc.asked#1` | 0: out of scope; 1: out of scope; 2: accepted residual; 3: accepted WIDE | no gate defect: the K-1 and K-3 cases are refused |
| `gate:ftc.carryover_if_asked#1` | 0: presentation | no gate defect: no amount |
| `gate:ftc.has_tax#1` | 0: out of scope; 1: out of scope; 2: model error; 3: accepted WIDE | no gate defect: the deduction is not prepared; K-1 refused; territories asked |
| `gate:sb.bonds_any_if_income#1` | 0: covered; 1: presentation; 2: covered; 3: accepted (minor UNCLEAR); 4: defect (BUG-0832); 5: accepted WIDE; 6: accepted WIDE | defect (low): the help excludes certificates of deposit |
| `gate:sb.foreign_any#1` | 0: defect (BUG-0831); 1: defect (BUG-0831); 2: out of scope; 3: covered; 4: covered; 5: accepted WIDE | defect (low): the gates miss indirect financial interests |
| `gate:sb.foreign_company_any#1` | 0: defect (BUG-0831); 1: defect (BUG-0831); 2: accepted WIDE; 3: accepted WIDE | defect (low): votes and indirect holdings are not named |
| `gate:sb.foreign_trust_any#1` | 0: defect (BUG-0831); 1: defect (BUG-0831); 2: defect (BUG-0831); 3: defect (BUG-0831); 4: accepted WIDE | defect (low): the trust gate is narrower than line 8 |
| `gate:sd.sold_other#1` | 0: defect (BUG-0835); 1: covered; 2: covered; 3: covered; 4: out of scope; 5: accepted WIDE | defect (low): mineral property is not named in the gate |

### False-no

| Unit | Findings (n: class) | Disposition |
|---|---|---|
| `gate:div.any#1` | 0: accepted residual; 1: accepted residual; 2: accepted (minor UNCLEAR); 3: accepted (minor UNCLEAR); 4: accepted (minor UNCLEAR); 5: accepted (minor UNCLEAR); 6: out of scope | no defect of the gate beyond the box question's wording; K-1 and Form 8814 refused |
| `gate:div.capital_gain_boxes#1` | 0: defect (BUG-0830); 1: defect (BUG-0830); 2: accepted (no defect); 3: accepted (minor UNCLEAR); 4: out of scope | defect (medium): the box question excludes amounts without a form and shares of forms in another name |
| `gate:div.has_ordinary#1` | 0: covered; 1: out of scope; 2: out of scope; 3: covered; 4: covered | no gate defect; as the earlier ruling (rechecked against the current help) |
| `gate:div.has_return_of_capital#1` | 0: accepted (minor UNCLEAR); 1: accepted (minor UNCLEAR); 2: defect (BUG-0830) | defect (medium) through the parent question: BUG-0830 |
| `gate:div.ordinary_boxes#1` | 0: defect (BUG-0830); 1: defect (BUG-0830); 2: accepted (minor UNCLEAR) | defect (medium) in part: BUG-0830 |
| `gate:div.other_boxes_if_dividends#1` | 0: defect (BUG-0830); 1: accepted residual; 2: accepted (minor UNCLEAR); 3: defect (BUG-0830) | defect (medium): BUG-0830 |
| `gate:f1116col.has_div#1` | 0: accepted (no amount); 1: out of scope; 2: covered; 3: model error | no gate defect: no amount turns on the dividend/interest split; K-1 refused |
| `gate:f1116col.has_int#1` | 0: accepted (minor UNCLEAR); 1: out of scope; 2: out of scope; 3: model error; 4: out of scope | no gate defect: the cases are refused or minor |
| `gate:f1116sb.generated#1` | 0: out of scope; 1: covered; 2: accepted WIDE; 3: defect (BUG-0834); 4: accepted (minor UNCLEAR) | defect (low) in one reading; the rest refuse or are right |
| `gate:f4952.carryover_if_interest#1` | 0: defect (BUG-0833); 1: defect (BUG-0833); 2: accepted (minor UNCLEAR); 3: out of scope | defect (medium): the carryforward is asked only from a 2024 Form 4952 |
| `gate:f4952.has_interest#1` | 0: out of scope; 1: accepted (minor UNCLEAR); 2: accepted (minor UNCLEAR); 3: accepted (minor UNCLEAR); 4: defect (BUG-0833) | defect (medium) in the gated prompt: BUG-0833 item 1 |
| `gate:ftc.asked#1` | 0: out of scope; 1: out of scope; 2: accepted residual; 3: accepted residual | no gate defect: K-1 and K-3 refused; withholding a known residual |
| `gate:ftc.carryover_ask#1` | 0: accepted residual; 1: covered; 2: accepted residual; 3: accepted residual; 4: accepted residual | no gate defect; as the earlier ruling, rechecked |
| `gate:ftc.carryover_if_asked#1` | 0: defect (BUG-0834); 1: accepted (minor UNCLEAR); 2: model error; 3: covered; 4: covered; 5: accepted (minor UNCLEAR); 6: accepted (minor UNCLEAR) | defect (low) in one case: BUG-0834 item 2 |
| `gate:ftc.has_tax#1` | 0: out of scope; 1: model error; 2: accepted residual; 3: accepted residual; 4: out of scope; 5: accepted residual; 6: accepted (minor UNCLEAR) | no gate defect; as the earlier ruling, rechecked |
| `gate:sb.bonds_any_if_income#1` | 0: covered; 1: defect (BUG-0832); 2: covered; 3: covered; 4: accepted (minor UNCLEAR); 5: model error; 6: accepted (minor UNCLEAR) | defect (low) in part: BUG-0832 |
| `gate:sb.foreign_any#1` | 0: defect (BUG-0831); 1: defect (BUG-0831); 2: out of scope; 3: covered; 4: covered; 5: accepted (minor UNCLEAR); 6: covered; 7: defect (BUG-0831); 8: covered; 9: defect (BUG-0831); 10: covered | defect (low): BUG-0831 item 1 |
| `gate:sb.foreign_company_any#1` | 0: defect (BUG-0831); 1: defect (BUG-0831); 2: defect (BUG-0831); 3: covered | defect (low): BUG-0831 item 3 |
| `gate:sb.foreign_trust_any#1` | 0: defect (BUG-0831); 1: defect (BUG-0831); 2: defect (BUG-0831); 3: defect (BUG-0831); 4: defect (BUG-0831); 5: covered | defect (low): BUG-0831 item 2 |
| `gate:sb.has_income#1` | 0: defect (BUG-0832); 1: accepted (minor UNCLEAR); 2: accepted (minor UNCLEAR); 3: accepted (minor UNCLEAR); 4: defect (BUG-0832); 5: presentation; 6: covered; 7: covered; 8: accepted (minor UNCLEAR) | defect (low) in part: BUG-0832 |
| `gate:sd.sold_other#1` | 0: covered; 1: covered; 2: covered; 3: defect (BUG-0835); 4: covered; 5: out of scope; 6: accepted residual; 7: covered; 8: accepted (minor UNCLEAR) | defect (low) in part: BUG-0835 |

## Notes

- **Reviewer saw the label.** Several NARROW and FALSE_NO findings read a gate's label ("income tax ever paid to another
  country", "your foreign income") rather than the question as asked; these are ruled model error or covered with the
  question's words in the evidence.
- **One screen at a time.** sd.f2439's three NARROW findings name other Schedule 3 line 13 items; each has its own question
  (`s3.repaid_income`, `s3.section965`, `s3.section960c`, `s3.virgin_islands`, `s3.farmland_deferral`).
- **Not a defect: the foreign tax deduction.** ftc.has_tax's finding on non-creditable tax that could be deducted is out of
  scope: the deduction is elective and not prepared (`sa.foreign_tax_deduct`'s help says so), so leaving it out does not
  understate tax.
