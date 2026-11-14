# Interview length: what question order could save

Written by `node engine/dist/main.js interview-length --write` (engine/src/interview-length.ts; deterministic, no model calls).
Every return is walked in three orders, and each order must give the same status and values (it does; a difference fails the run):

- **static**: today's order (bank order, then key).
- **floor**: the least any order can ask, knowing the answers: the inputs the complete return's evaluation reads. An order that
  asks only those (the oracle walk) is run and asks exactly that many on every return, so the floor is attained, not just bounded.
- **expected**: an order that does not know the answers: at each step it asks the open question whose closed answer (false, 0,
  none) would make the most other open questions unreachable, weighted by the share answering no from `interview/2025/gate_frequencies.yaml`
  (0.5 where the file names no share), ties in bank order. It probes the evaluator; it never answers for the filer.

Only the evaluator's reachability hides a question, so these are the only savings open to order. A question asked in every order and
answered no or 0 is one only a missing gate (a formal-model change) could hide. **Closed** answers are false, 0 or an empty list.
The returns are synthetic (fixtures, generated returns, minimal returns), not real filers.

## Summary

Means are per complete return; refused returns are counted but not measured beyond static. *Saved* is the share of all static
questions in the group that the order does not ask.

| Returns | Complete | Refused | Not walkable | Static asked (mean) | Static max | Closed answers (mean, share) | Floor (mean) | Expected order (mean) | Saved at floor | Saved by expected |
|---|---|---|---|---|---|---|---|---|---|---|
| Stage 5 whole returns | 9 | 2 | 0 | 96.3 | 122 | 80.3 (83%) | 96.3 | 96.3 | 0% | 0% |
| generated returns | 3 | 9 | 0 | 144.7 | 172 | 112.0 (77%) | 144.7 | 144.7 | 0% | 0% |
| minimal returns | 13 | 0 | 0 | 84.2 | 88 | 81.5 (97%) | 84.2 | 84.2 | 0% | 0% |
| social-security profile fixtures | 15 | 6 | 0 | 13.2 | 15 | 8.4 (64%) | 13.2 | 13.2 | 0% | 0% |
| sales profile fixtures | 58 | 14 | 0 | 62.7 | 110 | 54.2 (86%) | 62.7 | 62.7 | 0% | 0% |
| stage4 profile fixtures | 69 | 62 | 0 | 81.6 | 122 | 72.7 (89%) | 81.4 | 81.6 | 0% | 0% |
| **full profile, Stage 5 and generated** | 12 | 11 | 0 | 108.4 | 172 | 88.3 (81%) | 108.4 | 108.4 | 0% | 0% |
| **all** | 167 | 93 | 0 | 71.0 | 172 | 62.3 (88%) | 71.0 | 71.0 | 0% | 0% |

## Closed answers no order avoids (missing-gate candidates)

Templates asked, read by the complete return and answered closed, on the full profile, listed when at least half of the 12 complete
Stage 5 and generated returns ask them closed (count of 13 complete minimal returns beside). *Kind*: `gate guard` is read by a gate's guard
(asking it is the gate working); `behind a gate` is already gated and its gate was open; `ungated` has no gate line above it, so only a
new gate in the formal model (one question whose no makes it unreachable) could hide it. *Share yes* is the situation's share of all
returns in `gate_frequencies.yaml` where the file names the template (- where it does not).

64 templates are asked and answered closed on every one of the 12 returns; 39 of them have a recorded share
yes below the rare-situation cut (0.05).

| Template | Kind | Share yes | Stage 5 and generated | Minimal |
|---|---|---|---|---|
| `$dependent` | ungated | 0.2937 | 12 | 13 |
| `$oi8z` | ungated | 0.0485 | 12 | 13 |
| `$retirement` | ungated | 0.2357 | 12 | 13 |
| `$sc` | ungated | 0.1898 | 12 | 13 |
| `f1040.line25b` | ungated | 0.2081 | 12 | 13 |
| `f1040.line25c_other` | ungated | 0.2081 | 12 | 13 |
| `f2441.benefits` | ungated | 0.012 | 12 | 13 |
| `f2441.care` | ungated | 0.045 | 12 | 13 |
| `f4952.line4g` | ungated | - | 12 | 13 |
| `f5695.part1_any` | ungated | 0.0252 | 12 | 13 |
| `f5695.part2_any` | ungated | 0.0252 | 12 | 13 |
| `f8863.paid` | ungated | 0.09 | 12 | 13 |
| `f8959.unsupported` | ungated | 0.006 | 12 | 13 |
| `household.community_property` | ungated | 0.2335 | 12 | 13 |
| `household.married` | ungated | 0.3656 | 12 | 13 |
| `household.spouse_died_2025` | ungated | 0.006 | 12 | 13 |
| `person.age65` | ungated | 0.1944 | 12 | 13 |
| `person.blind` | ungated | 0.004 | 12 | 13 |
| `person.educator_expenses` | ungated | 0.0237 | 12 | 13 |
| `person.rrta` | ungated | 0.0015 | 12 | 13 |
| `person.sav_trad` | ungated | 0.08 | 12 | 13 |
| `person.under16` | ungated | 0.005 | 12 | 13 |
| `person.x_other` | ungated | 0.006 | 12 | 13 |
| `qbi.carryforward` | ungated | 0.012 | 12 | 13 |
| `qbi.unsupported` | ungated | 0.005 | 12 | 13 |
| `refund.received` | ungated | 0.4 | 12 | 13 |
| `s1.alimony` | ungated | 0.0029 | 12 | 13 |
| `s1.cod_any` | ungated | 0.006 | 12 | 13 |
| `s1.gambling_winnings` | ungated | 0.03 | 12 | 13 |
| `s1.line8_other` | ungated | - | 12 | 13 |
| `s1.line8g` | ungated | - | 12 | 13 |
| `s1.line8h` | ungated | - | 12 | 13 |
| `s1.line8i` | ungated | - | 12 | 13 |
| `s1.line8j` | ungated | - | 12 | 13 |
| `s1.line8r` | ungated | - | 12 | 13 |
| `s1.uc_paid` | ungated | 0.0292 | 12 | 13 |
| `s179.line10` | ungated | 0.012 | 12 | 13 |
| `s1a.carloan` | ungated | 0.03 | 12 | 13 |
| `s1a.overtime` | ungated | 0.1471 | 12 | 13 |
| `s1a.tips` | ungated | 0.0195 | 12 | 13 |
| `s2.amt` | ungated | 0.0009 | 12 | 13 |
| `s2.other` | ungated | 0.008 | 12 | 13 |
| `s3.credit_bond` | ungated | 0.012 | 12 | 13 |
| `s3.disability_retired` | ungated | - | 12 | 13 |
| `s3.line10` | ungated | 0.0153 | 12 | 13 |
| `s3.repaid_income` | ungated | 0.002 | 12 | 13 |
| `sa.dependent` | ungated | 0.0469 | 12 | 13 |
| `sa.elect_itemize` | ungated | - | 12 | 13 |
| `sa.excluded_income` | ungated | 0.004 | 12 | 13 |
| `sa.line5c` | ungated | - | 12 | 13 |
| `sa.unsupported` | ungated | 0.01 | 12 | 13 |
| `scope.other_income` | ungated | 0.015 | 12 | 13 |
| `scope.other_line16` | ungated | 0.002 | 12 | 13 |
| `scope.schedule1` | ungated | 0.12 | 12 | 13 |
| `sd.carryover` | ungated | 0.045 | 12 | 13 |
| `sd.other_forms` | ungated | 0.025 | 12 | 13 |
| `ssb.benefits` | ungated | 0.1999 | 12 | 13 |
| `s3.adoption_any` | gate guard | 0.012 | 12 | 12 |
| `s3.ev` | gate guard | 0.012 | 12 | 12 |
| `s3.farmland` | gate guard | 0.002 | 12 | 12 |
| `s3.foreign_any` | gate guard | 0.002 | 12 | 12 |
| `s3.kerosene` | gate guard | 0.0019 | 12 | 12 |
| `s3.prior_other_forms` | gate guard | 0.012 | 12 | 12 |
| `sb.foreign_any` | gate guard | - | 12 | 12 |
| `$f1095a` | ungated | 0.085 | 11 | 13 |
| `sli.interest` | ungated | 0.08 | 11 | 13 |
| `$f8889` | ungated | 0.11 | 9 | 13 |
| `$sales` | ungated | 0.13 | 9 | 13 |
| `ftc.taxes` | ungated | 0.0734 | 9 | 13 |
| `sa.line5b` | ungated | - | 9 | 13 |
| `sa.line1` | ungated | - | 8 | 13 |
| `sa.line8a` | ungated | - | 8 | 13 |
| `div.any` | gate guard | - | 8 | 12 |
| `f4952.has_interest` | gate guard | 0.01 | 8 | 12 |
| `$interest` | ungated | 0.3441 | 7 | 13 |
| `sa.line5a` | ungated | - | 7 | 13 |
| `sa.gifts` | gate guard | 0.4 | 7 | 12 |
| `f1040.line26` | ungated | 0.0657 | 6 | 13 |

## Questions order could avoid

Templates asked in static order and not read by the complete return, by number of complete returns (all groups): the questions a
better order (or a nested `choose`) would not ask. On the full profile these are the templates interview-rules holds under
`walked_unused`; the slice profiles are not in its reach check.

| Template | Returns |
|---|---|
| `dependent.parent_home_paid` | 6 |
| `person.blind` | 4 |

## Per return

### Stage 5 whole returns

| Return | Status | Static | Closed | Floor | Expected |
|---|---|---|---|---|---|
| stage5.return.owed | complete | 107 | 87 | 107 | 107 |
| stage5.return.refund | complete | 86 | 77 | 86 | 86 |
| stage5.return.itemized | complete | 122 | 87 | 122 | 122 |
| stage5.refuse.screens | refused | 39 | 36 | - | - |
| stage5.refuse.other_income | refused | 43 | 40 | - | - |
| stage5.return.refund_f4952_screens_unused | complete | 86 | 77 | 86 | 86 |
| stage5.return.refund_f8960_unsupported_unused | complete | 86 | 77 | 86 | 86 |
| stage5.return.f8960_unsupported_agi_at_threshold | complete | 86 | 77 | 86 | 86 |
| stage5.return.refund_f8960_refund_unused | complete | 86 | 77 | 86 | 86 |
| stage5.return.refund_combat_pay_no_children | complete | 86 | 77 | 86 | 86 |
| stage5.return.itemized_f8960_allocation_unused | complete | 122 | 87 | 122 | 122 |

### generated returns

| Return | Status | Static | Closed | Floor | Expected |
|---|---|---|---|---|---|
| generated.0 | complete | 121 | 102 | 121 | 121 |
| generated.1 | refused | 139 | 96 | - | - |
| generated.2 | refused | 122 | 90 | - | - |
| generated.3 | refused | 148 | 114 | - | - |
| generated.4 | complete | 141 | 105 | 141 | 141 |
| generated.5 | refused | 118 | 80 | - | - |
| generated.6 | complete | 172 | 129 | 172 | 172 |
| generated.7 | refused | 152 | 103 | - | - |
| generated.8 | refused | 186 | 130 | - | - |
| generated.9 | refused | 178 | 127 | - | - |
| generated.10 | refused | 222 | 160 | - | - |
| generated.11 | refused | 124 | 91 | - | - |

### minimal returns

| Return | Status | Static | Closed | Floor | Expected |
|---|---|---|---|---|---|
| every gate closed | complete | 82 | 80 | 82 | 82 |
| div.any = true alone | complete | 88 | 85 | 88 | 88 |
| f4952.has_interest = true alone | complete | 84 | 81 | 84 | 84 |
| f8889.coverage_year = "family" alone | complete | 82 | 80 | 82 | 82 |
| f8889.coverage_year = "changed" alone | complete | 82 | 80 | 82 | 82 |
| s3.adoption_any = true alone | complete | 84 | 81 | 84 | 84 |
| s3.ev = true alone | complete | 85 | 82 | 85 | 85 |
| s3.farmland = true alone | complete | 83 | 80 | 83 | 83 |
| s3.foreign_any = true alone | complete | 86 | 83 | 86 | 86 |
| s3.kerosene = true alone | complete | 83 | 80 | 83 | 83 |
| s3.prior_other_forms = true alone | complete | 85 | 82 | 85 | 85 |
| sa.gifts = true alone | complete | 85 | 82 | 85 | 85 |
| sb.foreign_any = true alone | complete | 86 | 83 | 86 | 86 |

### social-security profile fixtures

| Return | Status | Static | Closed | Floor | Expected |
|---|---|---|---|---|---|
| ss.multi | complete | 15 | 9 | 15 | 15 |
| ss.base.below | complete | 15 | 9 | 15 | 15 |
| ss.base.exact | complete | 15 | 9 | 15 | 15 |
| ss.base.above | complete | 15 | 9 | 15 | 15 |
| ss.withheld.below | complete | 15 | 9 | 15 | 15 |
| ss.withheld.exact | complete | 15 | 9 | 15 | 15 |
| ss.withheld.above | complete | 15 | 9 | 15 | 15 |
| ss.single.exact | complete | 10 | 7 | 10 | 10 |
| ss.single.below | complete | 10 | 7 | 10 | 10 |
| ss.single.over | refused | 6 | 3 | - | - |
| ss.multi.over | refused | 7 | 3 | - | - |
| ss.tips | complete | 15 | 8 | 15 | 15 |
| ss.none | complete | 9 | 8 | 9 | 9 |
| ss.mfj | complete | 9 | 8 | 9 | 9 |
| ss.mfs | refused | 3 | 2 | - | - |
| ss.rrta | refused | 4 | 2 | - | - |
| ss.hoh | complete | 15 | 9 | 15 | 15 |
| ss.qss | complete | 15 | 9 | 15 | 15 |
| ss.other.components | refused | 15 | 6 | - | - |
| ss.person.separation | complete | 10 | 7 | 10 | 10 |
| ss.early.refusal | refused | 7 | 4 | - | - |

### sales profile fixtures

| Return | Status | Static | Closed | Floor | Expected |
|---|---|---|---|---|---|
| sales.carryover.short_term | complete | 66 | 54 | 66 | 66 |
| sales.official.gain | complete | 60 | 53 | 60 | 60 |
| sales.official.loss | complete | 60 | 53 | 60 | 60 |
| sales.official.adjustment | complete | 61 | 53 | 61 | 61 |
| sales.official.basis | complete | 61 | 53 | 61 | 61 |
| sales.adjust.A.B | complete | 61 | 53 | 61 | 61 |
| sales.adjust.A.W | complete | 61 | 53 | 61 | 61 |
| sales.adjust.A.BW | complete | 62 | 53 | 62 | 62 |
| sales.adjust.B.B | complete | 60 | 53 | 60 | 60 |
| sales.adjust.B.W | complete | 61 | 53 | 61 | 61 |
| sales.adjust.B.BW | complete | 61 | 53 | 61 | 61 |
| sales.adjust.D.B | complete | 61 | 53 | 61 | 61 |
| sales.adjust.D.W | complete | 61 | 53 | 61 | 61 |
| sales.adjust.D.BW | complete | 62 | 53 | 62 | 62 |
| sales.adjust.E.B | complete | 60 | 53 | 60 | 60 |
| sales.adjust.E.W | complete | 61 | 53 | 61 | 61 |
| sales.adjust.E.BW | complete | 61 | 53 | 61 | 61 |
| sales.refuse.wash_over_loss | refused | 56 | 48 | - | - |
| sales.adjust.A.W.equal_loss | complete | 61 | 53 | 61 | 61 |
| sales.adjust.D.BW.wash_within_corrected_loss | complete | 62 | 53 | 62 | 62 |
| sales.official.aggregate | complete | 61 | 53 | 61 | 61 |
| sales.official.two_aggregate | complete | 68 | 54 | 68 | 68 |
| sales.box.A | complete | 60 | 53 | 60 | 60 |
| sales.box.B | complete | 60 | 53 | 60 | 60 |
| sales.box.C | complete | 60 | 53 | 60 | 60 |
| sales.box.D | complete | 60 | 53 | 60 | 60 |
| sales.box.E | complete | 60 | 53 | 60 | 60 |
| sales.box.F | complete | 60 | 53 | 60 | 60 |
| sales.loss.single.0 | complete | 60 | 55 | 60 | 60 |
| sales.loss.mfs.0 | complete | 60 | 55 | 60 | 60 |
| sales.loss.single.1 | complete | 60 | 54 | 60 | 60 |
| sales.loss.mfs.1 | complete | 60 | 54 | 60 | 60 |
| sales.loss.single.149999 | complete | 60 | 54 | 60 | 60 |
| sales.loss.mfs.149999 | complete | 60 | 54 | 60 | 60 |
| sales.loss.single.150000 | complete | 60 | 54 | 60 | 60 |
| sales.loss.mfs.150000 | complete | 60 | 54 | 60 | 60 |
| sales.loss.single.150001 | complete | 60 | 54 | 60 | 60 |
| sales.loss.mfs.150001 | complete | 60 | 54 | 60 | 60 |
| sales.loss.single.299999 | complete | 60 | 54 | 60 | 60 |
| sales.loss.mfs.299999 | complete | 60 | 54 | 60 | 60 |
| sales.loss.single.300000 | complete | 60 | 54 | 60 | 60 |
| sales.loss.mfs.300000 | complete | 60 | 54 | 60 | 60 |
| sales.loss.single.300001 | complete | 60 | 54 | 60 | 60 |
| sales.loss.mfs.300001 | complete | 60 | 54 | 60 | 60 |
| sales.loss.single.700000 | complete | 60 | 54 | 60 | 60 |
| sales.loss.mfs.700000 | complete | 60 | 54 | 60 | 60 |
| sales.cents | complete | 66 | 56 | 66 | 66 |
| sales.no_sales | complete | 55 | 52 | 55 | 55 |
| sales.distribution | complete | 66 | 61 | 66 | 66 |
| sales.refuse.digital.G | refused | 50 | 47 | - | - |
| sales.refuse.digital.H | refused | 50 | 47 | - | - |
| sales.refuse.digital.I | refused | 50 | 47 | - | - |
| sales.refuse.digital.J | refused | 50 | 47 | - | - |
| sales.refuse.digital.K | refused | 50 | 47 | - | - |
| sales.refuse.digital.L | refused | 50 | 47 | - | - |
| sales.refuse.special | refused | 51 | 47 | - | - |
| sales.refuse.code | refused | 52 | 48 | - | - |
| sales.refuse.no_report_B | refused | 52 | 48 | - | - |
| sales.refuse.aggregate.eligibility | refused | 54 | 49 | - | - |
| sales.refuse.aggregate.basis | refused | 53 | 48 | - | - |
| sales.refuse.aggregate.adjustment | refused | 53 | 48 | - | - |
| sales.refuse.forms | refused | 48 | 46 | - | - |
| sales.select.sdtw.28pct | complete | 72 | 60 | 72 | 72 |
| sales.select.sdtw.1250 | complete | 72 | 60 | 72 | 72 |
| sales.select.zero_taxable | complete | 72 | 60 | 72 | 72 |
| sales.select.4952_zero | complete | 65 | 54 | 65 | 65 |
| sales.select.short_only | complete | 61 | 52 | 61 | 61 |
| sales.select.loss_dividend | complete | 71 | 60 | 71 | 71 |
| sales.select.loss_no_dividend | complete | 61 | 53 | 61 | 61 |
| sales.netting | complete | 67 | 54 | 67 | 67 |
| sales.mixed_columns | complete | 110 | 59 | 110 | 110 |
| sales.select.sdtw.election | complete | 65 | 54 | 65 | 65 |

### stage4 profile fixtures

| Return | Status | Static | Closed | Floor | Expected |
|---|---|---|---|---|---|
| stage4.mut.div_box3_basis_reconciled | complete | 79 | 72 | 79 | 79 |
| stage4.refuse.div.section1202 | refused | 74 | 67 | - | - |
| stage4.refuse.div.amt | refused | 73 | 67 | - | - |
| stage4.refuse.div.special | refused | 76 | 70 | - | - |
| stage4.refuse.div.inconsistent | refused | 80 | 73 | - | - |
| stage4.refuse.div.components | refused | 80 | 73 | - | - |
| stage4.refuse.div.overlapping | refused | 81 | 73 | - | - |
| stage4.refuse.div.basis | refused | 77 | 71 | - | - |
| stage4.interest.limited | complete | 86 | 77 | 86 | 86 |
| stage4.interest.exception | complete | 86 | 77 | 86 | 86 |
| stage4.interest.election | complete | 86 | 75 | 86 | 86 |
| stage4.4952.carryover_no_income | complete | 77 | 69 | 77 | 77 |
| stage4.f4952.line4a_taxable_interest_and_dividends | complete | 88 | 76 | 88 | 88 |
| stage4.refuse.4952.unsupported | refused | 70 | 62 | - | - |
| stage4.refuse.4952.alternative_allocation | refused | 71 | 63 | - | - |
| stage4.refuse.4952.election | refused | 72 | 65 | - | - |
| stage4.refuse.4952.bad_dividends | refused | 81 | 72 | - | - |
| stage4.refuse.4952.unsupported_with_carryover | refused | 70 | 62 | - | - |
| stage4.interest.short_term | complete | 78 | 68 | 78 | 78 |
| stage4.f4952.unused_unsupported | complete | 72 | 67 | 72 | 72 |
| stage4.f4952.unused_alternative_allocation | complete | 72 | 67 | 72 | 72 |
| stage4.base | complete | 72 | 67 | 72 | 72 |
| stage4.medicare.single.-1 | complete | 72 | 67 | 72 | 72 |
| stage4.medicare.single.0 | complete | 72 | 67 | 72 | 72 |
| stage4.medicare.single.100000 | complete | 72 | 67 | 72 | 72 |
| stage4.medicare.hoh.-1 | complete | 89 | 75 | 88 | 89 |
| stage4.medicare.hoh.0 | complete | 89 | 75 | 88 | 89 |
| stage4.medicare.hoh.100000 | complete | 89 | 75 | 88 | 89 |
| stage4.medicare.qss.-1 | complete | 71 | 65 | 71 | 71 |
| stage4.medicare.qss.0 | complete | 71 | 65 | 71 | 71 |
| stage4.medicare.qss.100000 | complete | 71 | 65 | 71 | 71 |
| stage4.medicare.mfs.-1 | refused | 60 | 55 | - | - |
| stage4.medicare.mfs.0 | refused | 60 | 55 | - | - |
| stage4.medicare.mfs.100000 | refused | 60 | 55 | - | - |
| stage4.medicare.mfj.-1 | refused | 48 | 43 | - | - |
| stage4.medicare.mfj.0 | refused | 48 | 43 | - | - |
| stage4.medicare.mfj.100000 | refused | 48 | 43 | - | - |
| stage4.medicare.withholding | complete | 72 | 67 | 72 | 72 |
| stage4.medicare.withholding_floor | complete | 72 | 67 | 72 | 72 |
| stage4.refuse.8959 | refused | 64 | 60 | - | - |
| stage4.niit.allocated | complete | 97 | 78 | 96 | 97 |
| stage4.niit.single.0 | complete | 82 | 75 | 82 | 82 |
| stage4.niit.single.100000 | complete | 84 | 77 | 84 | 84 |
| stage4.niit.hoh.0 | complete | 99 | 83 | 98 | 99 |
| stage4.niit.hoh.100000 | complete | 101 | 85 | 100 | 101 |
| stage4.niit.qss.0 | complete | 81 | 73 | 81 | 81 |
| stage4.niit.qss.100000 | complete | 83 | 75 | 83 | 83 |
| stage4.niit.mfj.0 | refused | 57 | 50 | - | - |
| stage4.niit.mfj.100000 | refused | 57 | 50 | - | - |
| stage4.niit.mfs.0 | refused | 70 | 63 | - | - |
| stage4.niit.mfs.100000 | refused | 72 | 65 | - | - |
| stage4.niit.standard_no_deduction | complete | 88 | 78 | 88 | 88 |
| stage4.refuse.8960.unsupported | refused | 73 | 67 | - | - |
| stage4.refuse.8960.refund | refused | 74 | 68 | - | - |
| stage4.niit.loss_floor | complete | 80 | 70 | 80 | 80 |
| stage4.refuse.niit.allocation | refused | 75 | 68 | - | - |
| stage4.refuse.8960.unsupported.simultaneous | refused | 73 | 67 | - | - |
| stage4.additional_taxes.combined | complete | 97 | 78 | 96 | 97 |
| stage4.official.medicare_example5 | refused | 48 | 43 | - | - |
| stage4.ftc.29999 | complete | 77 | 67 | 77 | 77 |
| stage4.ftc.30000 | complete | 77 | 67 | 77 | 77 |
| stage4.ftc.regular_limit | complete | 77 | 67 | 77 | 77 |
| stage4.refuse.ftc.limit | refused | 67 | 61 | - | - |
| stage4.refuse.ftc.passive | refused | 68 | 62 | - | - |
| stage4.refuse.ftc.statements | refused | 71 | 62 | - | - |
| stage4.refuse.ftc.eligible | refused | 71 | 62 | - | - |
| stage4.refuse.ftc.election | refused | 71 | 62 | - | - |
| stage4.mut.savers_claimed_dependent | refused | 59 | 53 | - | - |
| stage4.qbi.below | complete | 84 | 76 | 84 | 84 |
| stage4.qbi.exact | complete | 84 | 76 | 84 | 84 |
| stage4.qbi.above | complete | 84 | 76 | 84 | 84 |
| stage4.qbi.income_limit | complete | 82 | 74 | 82 | 82 |
| stage4.qbi.capital_limit | complete | 86 | 77 | 86 | 86 |
| stage4.refuse.qbi | refused | 72 | 66 | - | - |
| stage4.qbi.zero_income | complete | 72 | 68 | 72 | 72 |
| stage4.refuse.s2.amt | refused | 70 | 64 | - | - |
| stage4.refuse.s2.other | refused | 71 | 65 | - | - |
| stage4.refuse.s2.amt.simultaneous | refused | 70 | 64 | - | - |
| stage4.refuse.gift.sectionB | refused | 74 | 66 | - | - |
| stage4.salt.below | complete | 75 | 69 | 75 | 75 |
| stage4.salt.exact | complete | 75 | 69 | 75 | 75 |
| stage4.salt.phase | complete | 75 | 69 | 75 | 75 |
| stage4.salt.floor | complete | 74 | 68 | 74 | 74 |
| stage4.salt.above | complete | 74 | 68 | 74 | 74 |
| stage4.salt.mfs | refused | 62 | 56 | - | - |
| stage4.salt.mfs_floor | refused | 62 | 56 | - | - |
| stage4.salt.low_paid | complete | 74 | 68 | 74 | 74 |
| stage4.medical.below | complete | 72 | 66 | 72 | 72 |
| stage4.medical.above | complete | 72 | 66 | 72 | 72 |
| stage4.standard.single | complete | 74 | 66 | 74 | 74 |
| stage4.standard.hoh | complete | 91 | 74 | 90 | 91 |
| stage4.standard.qss | complete | 73 | 64 | 73 | 73 |
| stage4.standard.mfj | refused | 50 | 42 | - | - |
| stage4.standard.mfs | refused | 61 | 54 | - | - |
| stage4.standard.spouse_itemizes | refused | 59 | 53 | - | - |
| stage4.standard.itemized | complete | 73 | 67 | 73 | 73 |
| stage4.standard.elected | complete | 72 | 66 | 71 | 72 |
| stage4.gift.50000.false | complete | 77 | 69 | 77 | 77 |
| stage4.gift.500000.false | complete | 77 | 69 | 77 | 77 |
| stage4.gift.500001.true | complete | 78 | 69 | 78 | 78 |
| stage4.refuse.sa.unsupported | refused | 62 | 56 | - | - |
| stage4.refuse.sa.charity_limited | refused | 64 | 57 | - | - |
| stage4.refuse.sa.excluded_income | refused | 64 | 58 | - | - |
| stage4.refuse.standard.dependent | refused | 59 | 53 | - | - |
| stage4.refuse.dependent_itemizes | refused | 59 | 53 | - | - |
| stage4.refuse.standard.spouse_extra | refused | 60 | 54 | - | - |
| stage4.refuse.gift.special | refused | 72 | 64 | - | - |
| stage4.refuse.sa.unsupported.simultaneous | refused | 62 | 56 | - | - |
| stage4.deductions.combined | complete | 85 | 67 | 85 | 85 |
| audit.sa.negative_agi_medical | complete | 122 | 110 | 122 | 122 |
| audit.sa.negative_agi_medical_paid | complete | 122 | 109 | 122 | 122 |
| stage4.refuse.sb.unsupported | refused | 69 | 62 | - | - |
| stage4.refuse.sb.fbar_required | refused | 69 | 63 | - | - |
| stage4.refuse.sb.form8938 | refused | 70 | 64 | - | - |
| stage4.refuse.sb.line8 | refused | 71 | 65 | - | - |
| stage4.sb.foreign_no_filing | complete | 72 | 67 | 72 | 72 |
| stage4.refuse.sb.unsupported.simultaneous | refused | 69 | 62 | - | - |
| stage4.refuse.scope.schedule1 | refused | 40 | 35 | - | - |
| stage4.refuse.scope.credits | refused | 62 | 55 | - | - |
| stage4.refuse.scope.other_income | refused | 46 | 41 | - | - |
| stage4.refuse.scope.other_line16 | refused | 58 | 52 | - | - |
| stage4.refuse.married | refused | 60 | 55 | - | - |
| stage4.sdtw.special_rates | complete | 85 | 76 | 85 | 85 |
| stage4.sdtw.skip22 | complete | 86 | 76 | 85 | 86 |
| stage4.sdtw.skip32 | complete | 83 | 76 | 83 | 83 |
| stage4.sdtw.twenty_percent | complete | 85 | 76 | 85 | 85 |
| stage4.sdtw.lower_bracket | complete | 83 | 74 | 83 | 83 |
| stage4.sdtw.line12_takes_line9 | complete | 93 | 79 | 93 | 93 |
| stage4.mut.sdtw_28pct_no_1250 | complete | 85 | 77 | 85 | 85 |
| stage4.mut.sdtw_1250_line32_is_line1 | complete | 83 | 76 | 83 | 83 |
| stage4.feeders.shortloss | complete | 89 | 75 | 89 | 89 |

<!-- Hand-written findings below this line are kept when the tool rewrites the report. -->






## Findings (hand-written; tax year 2025, from the tables above as first written)

**What the numbers show (observation).**

- Today's order is at, or within 3 questions of, the floor on all 161 complete returns. On the full profile, the 12 complete Stage 5
  and generated returns ask a mean of 111.2 questions against a floor of 110.9. The only gap is generated.4: it asks 264 where the floor
  is 261, and the three extra questions are the Form 8962 templates interview-rules already holds under `walked_unused` (BUG-0487).
  On the slice profiles, 10 stage4 fixtures ask one question their slice targets do not read (`dependent.parent_home_paid`,
  `person.blind`). Across all returns, the floor is 0% below static (0.1% before rounding).
- The expected-pruning order, which does not know the answers, saves nothing on any return. In the one case where order matters
  (BUG-0487), the deciding value is Form 8962 line 5, a computed amount: no closed answer to a single question removes the three
  questions, so a one-step probe cannot see the saving.
- Most of the length is closed answers that are read. The complete returns answer 86% of their questions false, 0 or none (Stage 5
  82%; minimal returns 96%; the minimal "nothing at all" return asks about 80). On the full profile, 60 templates are asked and
  answered closed on every one of the 12 complete returns, and the evaluation reads every one of them. Of those 60,
  `gate_frequencies.yaml` puts 37 below the 5% rare-situation cut.

**What this suggests (interpretation; moderate credence).** Answer-dependent ordering (T-251) is not worth building to shorten
the federal interview as the model now stands. This is about as strong as a measurement here gets, because the floor is a bound,
not a sample: no order can ask fewer questions than the answered inputs the complete return reads, and the oracle order attains that
floor on every return. The reason is structural. Because conjunctions were rewritten as nested `choose`, the questions that
stay reachable are ones the evaluation reads. That leaves nothing for order to prune. The owner's "142 of 165 answered no" is real,
and it reproduces here at the same ratio (about 77 to 96% closed). It is a breadth problem: flat top-level screens, each read, each
asked of everyone. Fewer questions would take new umbrella gates in the formal model (for example, one "any of these rare
situations?" input whose no makes the rows below it unreachable), which is a model change under the gates design. It is not an
interview-layer change. Grouping those rows on rare-situation grids, as the design already proposes, would cut screens, but each row
would still be an answer.

**Limits.** These are synthetic returns, not real filers. The Stage 5 fixtures are hand-written scenarios, and 9 of the 12 generated
returns end refused, so only 3 complete generated returns are measured. Refused returns (92 of 253) are not measured beyond
static order. The no-order-can-avoid count is exact for these returns. How it generalizes to real filers rests on how well the
fixtures represent them, and that is not measured. The expected order is one heuristic among many. A smarter one cannot beat the
floor, which static order already reaches, so its absence does not change the conclusion.
