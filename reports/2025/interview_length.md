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
| Stage 5 whole returns | 9 | 2 | 0 | 91.1 | 116 | 74.1 (81%) | 91.1 | 91.1 | 0% | 0% |
| generated returns | 3 | 9 | 0 | 158.3 | 258 | 106.3 (67%) | 158.3 | 158.3 | 0% | 0% |
| minimal returns | 7 | 0 | 0 | 79.1 | 83 | 75.6 (95%) | 79.1 | 79.1 | 0% | 0% |
| social-security profile fixtures | 16 | 5 | 0 | 11.3 | 13 | 6.3 (55%) | 11.3 | 11.3 | 0% | 0% |
| sales profile fixtures | 58 | 14 | 0 | 62.7 | 110 | 54.2 (86%) | 62.7 | 62.7 | 0% | 0% |
| stage4 profile fixtures | 69 | 62 | 0 | 73.5 | 112 | 64.6 (88%) | 73.4 | 73.5 | 0% | 0% |
| **full profile, Stage 5 and generated** | 12 | 11 | 0 | 107.9 | 258 | 82.2 (76%) | 107.9 | 107.9 | 0% | 0% |
| **all** | 162 | 92 | 0 | 66.3 | 258 | 56.9 (86%) | 66.2 | 66.3 | 0% | 0% |

## Closed answers no order avoids (missing-gate candidates)

Templates asked, read by the complete return and answered closed, on the full profile, listed when at least half of the 12 complete
Stage 5 and generated returns ask them closed (count of 7 complete minimal returns beside). *Kind*: `gate guard` is read by a gate's guard
(asking it is the gate working); `behind a gate` is already gated and its gate was open; `ungated` has no gate line above it, so only a
new gate in the formal model (one question whose no makes it unreachable) could hide it. *Share yes* is the situation's share of all
returns in `gate_frequencies.yaml` where the file names the template (- where it does not).

57 templates are asked and answered closed on every one of the 12 returns; 34 of them have a recorded share
yes below the rare-situation cut (0.05).

| Template | Kind | Share yes | Stage 5 and generated | Minimal |
|---|---|---|---|---|
| `$dependent` | ungated | 0.2937 | 12 | 7 |
| `$oi8z` | ungated | 0.0485 | 12 | 7 |
| `$retirement` | ungated | 0.2357 | 12 | 7 |
| `f1040.line25b` | ungated | 0.2081 | 12 | 7 |
| `f1040.line25c_other` | ungated | 0.2081 | 12 | 7 |
| `f2441.benefits` | ungated | 0.012 | 12 | 7 |
| `f2441.care` | ungated | 0.045 | 12 | 7 |
| `f4952.line4g` | ungated | - | 12 | 7 |
| `f5695.part1_any` | ungated | 0.0252 | 12 | 7 |
| `f5695.part2_any` | ungated | 0.0252 | 12 | 7 |
| `f8863.paid` | ungated | 0.09 | 12 | 7 |
| `f8959.unsupported` | ungated | 0.006 | 12 | 7 |
| `household.community_property` | ungated | 0.2335 | 12 | 7 |
| `household.married` | ungated | 0.3656 | 12 | 7 |
| `household.spouse_died_2025` | ungated | 0.006 | 12 | 7 |
| `person.age65` | ungated | 0.1944 | 12 | 7 |
| `person.blind` | ungated | 0.004 | 12 | 7 |
| `person.educator_expenses` | ungated | 0.0237 | 12 | 7 |
| `person.rrta` | ungated | 0.0015 | 12 | 7 |
| `person.sav_trad` | ungated | 0.08 | 12 | 7 |
| `person.under16` | ungated | 0.005 | 12 | 7 |
| `person.x_other` | ungated | 0.006 | 12 | 7 |
| `qbi.carryforward` | ungated | 0.012 | 12 | 7 |
| `qbi.unsupported` | ungated | 0.005 | 12 | 7 |
| `refund.received` | ungated | 0.4 | 12 | 7 |
| `s1.alimony` | ungated | 0.0029 | 12 | 7 |
| `s1.cod_any` | ungated | 0.006 | 12 | 7 |
| `s1.gambling_winnings` | ungated | 0.03 | 12 | 7 |
| `s1.line8_other` | ungated | - | 12 | 7 |
| `s1.line8g` | ungated | - | 12 | 7 |
| `s1.line8h` | ungated | - | 12 | 7 |
| `s1.line8i` | ungated | - | 12 | 7 |
| `s1.line8j` | ungated | - | 12 | 7 |
| `s1.line8r` | ungated | - | 12 | 7 |
| `s1.uc_paid` | ungated | 0.0292 | 12 | 7 |
| `s179.line10` | ungated | 0.012 | 12 | 7 |
| `s1a.carloan` | ungated | 0.03 | 12 | 7 |
| `s1a.overtime` | ungated | 0.1471 | 12 | 7 |
| `s1a.tips` | ungated | 0.0195 | 12 | 7 |
| `s2.amt` | ungated | 0.0009 | 12 | 7 |
| `s2.other` | ungated | 0.008 | 12 | 7 |
| `s3.line10` | ungated | 0.0153 | 12 | 7 |
| `s3.line12` | ungated | 0.0019 | 12 | 7 |
| `s3.line14` | ungated | 0.002 | 12 | 7 |
| `sa.dependent` | ungated | 0.0469 | 12 | 7 |
| `sa.elect_itemize` | ungated | - | 12 | 7 |
| `sa.excluded_income` | ungated | 0.004 | 12 | 7 |
| `sa.line5c` | ungated | - | 12 | 7 |
| `sa.unsupported` | ungated | 0.01 | 12 | 7 |
| `scope.credits` | ungated | 0.012 | 12 | 7 |
| `scope.other_income` | ungated | 0.015 | 12 | 7 |
| `scope.other_line16` | ungated | 0.002 | 12 | 7 |
| `scope.schedule1` | ungated | 0.12 | 12 | 7 |
| `sd.carryover` | ungated | 0.045 | 12 | 7 |
| `sd.other_forms` | ungated | 0.025 | 12 | 7 |
| `ssb.benefits` | ungated | 0.1999 | 12 | 7 |
| `sb.foreign_any` | gate guard | - | 12 | 6 |
| `$f1095a` | ungated | 0.085 | 11 | 7 |
| `$sc` | ungated | 0.1898 | 11 | 7 |
| `sli.interest` | ungated | 0.08 | 11 | 7 |
| `$f8889` | ungated | 0.11 | 9 | 7 |
| `$sales` | ungated | 0.13 | 9 | 7 |
| `ftc.taxes` | ungated | 0.0734 | 9 | 7 |
| `sa.line5b` | ungated | - | 9 | 7 |
| `sa.line1` | ungated | - | 8 | 7 |
| `sa.line8a` | ungated | - | 8 | 7 |
| `div.any` | gate guard | - | 8 | 6 |
| `f4952.has_interest` | gate guard | 0.01 | 8 | 6 |
| `$interest` | ungated | 0.3441 | 7 | 7 |
| `sa.line5a` | ungated | - | 7 | 7 |
| `sa.gifts` | gate guard | 0.4 | 7 | 6 |
| `f1040.line26` | ungated | 0.0657 | 6 | 7 |

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
| stage5.return.owed | complete | 102 | 81 | 102 | 102 |
| stage5.return.refund | complete | 81 | 71 | 81 | 81 |
| stage5.return.itemized | complete | 116 | 80 | 116 | 116 |
| stage5.refuse.screens | refused | 40 | 35 | - | - |
| stage5.refuse.other_income | refused | 45 | 41 | - | - |
| stage5.return.refund_f4952_screens_unused | complete | 81 | 71 | 81 | 81 |
| stage5.return.refund_f8960_unsupported_unused | complete | 81 | 71 | 81 | 81 |
| stage5.return.f8960_unsupported_agi_at_threshold | complete | 81 | 71 | 81 | 81 |
| stage5.return.refund_f8960_refund_unused | complete | 81 | 71 | 81 | 81 |
| stage5.return.refund_combat_pay_no_children | complete | 81 | 71 | 81 | 81 |
| stage5.return.itemized_f8960_allocation_unused | complete | 116 | 80 | 116 | 116 |

### generated returns

| Return | Status | Static | Closed | Floor | Expected |
|---|---|---|---|---|---|
| generated.0 | complete | 112 | 90 | 112 | 112 |
| generated.1 | refused | 101 | 72 | - | - |
| generated.2 | refused | 130 | 83 | - | - |
| generated.3 | refused | 139 | 102 | - | - |
| generated.4 | complete | 258 | 143 | 258 | 258 |
| generated.5 | refused | 75 | 42 | - | - |
| generated.6 | complete | 105 | 86 | 105 | 105 |
| generated.7 | refused | 77 | 55 | - | - |
| generated.8 | refused | 149 | 104 | - | - |
| generated.9 | refused | 101 | 72 | - | - |
| generated.10 | refused | 216 | 147 | - | - |
| generated.11 | refused | 123 | 82 | - | - |

### minimal returns

| Return | Status | Static | Closed | Floor | Expected |
|---|---|---|---|---|---|
| every gate closed | complete | 77 | 74 | 77 | 77 |
| div.any = true alone | complete | 83 | 79 | 83 | 83 |
| f4952.has_interest = true alone | complete | 79 | 75 | 79 | 79 |
| f8889.coverage_year = "family" alone | complete | 77 | 74 | 77 | 77 |
| f8889.coverage_year = "changed" alone | complete | 77 | 74 | 77 | 77 |
| sa.gifts = true alone | complete | 80 | 76 | 80 | 80 |
| sb.foreign_any = true alone | complete | 81 | 77 | 81 | 81 |

### social-security profile fixtures

| Return | Status | Static | Closed | Floor | Expected |
|---|---|---|---|---|---|
| ss.multi | complete | 13 | 7 | 13 | 13 |
| ss.base.below | complete | 13 | 7 | 13 | 13 |
| ss.base.exact | complete | 13 | 7 | 13 | 13 |
| ss.base.above | complete | 13 | 7 | 13 | 13 |
| ss.withheld.below | complete | 13 | 7 | 13 | 13 |
| ss.withheld.exact | complete | 13 | 7 | 13 | 13 |
| ss.withheld.above | complete | 13 | 7 | 13 | 13 |
| ss.single.exact | complete | 8 | 5 | 8 | 8 |
| ss.single.below | complete | 8 | 5 | 8 | 8 |
| ss.single.over | refused | 6 | 3 | - | - |
| ss.multi.over | refused | 7 | 3 | - | - |
| ss.tips | complete | 13 | 6 | 13 | 13 |
| ss.none | complete | 7 | 6 | 7 | 7 |
| ss.mfj | complete | 7 | 6 | 7 | 7 |
| ss.mfs | refused | 3 | 2 | - | - |
| ss.rrta | refused | 4 | 2 | - | - |
| ss.hoh | complete | 13 | 7 | 13 | 13 |
| ss.qss | complete | 13 | 7 | 13 | 13 |
| ss.other.components | complete | 13 | 4 | 13 | 13 |
| ss.person.separation | complete | 8 | 5 | 8 | 8 |
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
| stage4.mut.div_box3_basis_reconciled | complete | 71 | 64 | 71 | 71 |
| stage4.refuse.div.section1202 | refused | 66 | 59 | - | - |
| stage4.refuse.div.amt | refused | 65 | 59 | - | - |
| stage4.refuse.div.special | refused | 68 | 62 | - | - |
| stage4.refuse.div.inconsistent | refused | 72 | 65 | - | - |
| stage4.refuse.div.components | refused | 72 | 65 | - | - |
| stage4.refuse.div.overlapping | refused | 73 | 65 | - | - |
| stage4.refuse.div.basis | refused | 69 | 63 | - | - |
| stage4.interest.limited | complete | 78 | 69 | 78 | 78 |
| stage4.interest.exception | complete | 78 | 69 | 78 | 78 |
| stage4.interest.election | complete | 78 | 67 | 78 | 78 |
| stage4.4952.carryover_no_income | complete | 69 | 61 | 69 | 69 |
| stage4.f4952.line4a_taxable_interest_and_dividends | complete | 80 | 68 | 80 | 80 |
| stage4.refuse.4952.unsupported | refused | 62 | 54 | - | - |
| stage4.refuse.4952.alternative_allocation | refused | 63 | 55 | - | - |
| stage4.refuse.4952.election | refused | 64 | 57 | - | - |
| stage4.refuse.4952.bad_dividends | refused | 73 | 64 | - | - |
| stage4.refuse.4952.unsupported_with_carryover | refused | 62 | 54 | - | - |
| stage4.interest.short_term | complete | 70 | 60 | 70 | 70 |
| stage4.f4952.unused_unsupported | complete | 64 | 59 | 64 | 64 |
| stage4.f4952.unused_alternative_allocation | complete | 64 | 59 | 64 | 64 |
| stage4.base | complete | 64 | 59 | 64 | 64 |
| stage4.medicare.single.-1 | complete | 64 | 59 | 64 | 64 |
| stage4.medicare.single.0 | complete | 64 | 59 | 64 | 64 |
| stage4.medicare.single.100000 | complete | 64 | 59 | 64 | 64 |
| stage4.medicare.hoh.-1 | complete | 81 | 67 | 80 | 81 |
| stage4.medicare.hoh.0 | complete | 81 | 67 | 80 | 81 |
| stage4.medicare.hoh.100000 | complete | 81 | 67 | 80 | 81 |
| stage4.medicare.qss.-1 | complete | 63 | 57 | 63 | 63 |
| stage4.medicare.qss.0 | complete | 63 | 57 | 63 | 63 |
| stage4.medicare.qss.100000 | complete | 63 | 57 | 63 | 63 |
| stage4.medicare.mfs.-1 | refused | 59 | 54 | - | - |
| stage4.medicare.mfs.0 | refused | 59 | 54 | - | - |
| stage4.medicare.mfs.100000 | refused | 59 | 54 | - | - |
| stage4.medicare.mfj.-1 | refused | 39 | 34 | - | - |
| stage4.medicare.mfj.0 | refused | 39 | 34 | - | - |
| stage4.medicare.mfj.100000 | refused | 39 | 34 | - | - |
| stage4.medicare.withholding | complete | 64 | 59 | 64 | 64 |
| stage4.medicare.withholding_floor | complete | 64 | 59 | 64 | 64 |
| stage4.refuse.8959 | refused | 56 | 52 | - | - |
| stage4.niit.allocated | complete | 89 | 70 | 88 | 89 |
| stage4.niit.single.0 | complete | 74 | 67 | 74 | 74 |
| stage4.niit.single.100000 | complete | 76 | 69 | 76 | 76 |
| stage4.niit.hoh.0 | complete | 91 | 75 | 90 | 91 |
| stage4.niit.hoh.100000 | complete | 93 | 77 | 92 | 93 |
| stage4.niit.qss.0 | complete | 73 | 65 | 73 | 73 |
| stage4.niit.qss.100000 | complete | 75 | 67 | 75 | 75 |
| stage4.niit.mfj.0 | refused | 48 | 41 | - | - |
| stage4.niit.mfj.100000 | refused | 48 | 41 | - | - |
| stage4.niit.mfs.0 | refused | 69 | 62 | - | - |
| stage4.niit.mfs.100000 | refused | 71 | 64 | - | - |
| stage4.niit.standard_no_deduction | complete | 80 | 70 | 80 | 80 |
| stage4.refuse.8960.unsupported | refused | 65 | 59 | - | - |
| stage4.refuse.8960.refund | refused | 66 | 60 | - | - |
| stage4.niit.loss_floor | complete | 72 | 62 | 72 | 72 |
| stage4.refuse.niit.allocation | refused | 67 | 60 | - | - |
| stage4.refuse.8960.unsupported.simultaneous | refused | 65 | 59 | - | - |
| stage4.additional_taxes.combined | complete | 89 | 70 | 88 | 89 |
| stage4.official.medicare_example5 | refused | 39 | 34 | - | - |
| stage4.ftc.29999 | complete | 69 | 59 | 69 | 69 |
| stage4.ftc.30000 | complete | 69 | 59 | 69 | 69 |
| stage4.ftc.regular_limit | complete | 69 | 59 | 69 | 69 |
| stage4.refuse.ftc.limit | refused | 59 | 53 | - | - |
| stage4.refuse.ftc.passive | refused | 60 | 54 | - | - |
| stage4.refuse.ftc.statements | refused | 63 | 54 | - | - |
| stage4.refuse.ftc.eligible | refused | 63 | 54 | - | - |
| stage4.refuse.ftc.election | refused | 63 | 54 | - | - |
| stage4.mut.savers_claimed_dependent | refused | 50 | 44 | - | - |
| stage4.qbi.below | complete | 76 | 68 | 76 | 76 |
| stage4.qbi.exact | complete | 76 | 68 | 76 | 76 |
| stage4.qbi.above | complete | 76 | 68 | 76 | 76 |
| stage4.qbi.income_limit | complete | 74 | 66 | 74 | 74 |
| stage4.qbi.capital_limit | complete | 78 | 69 | 78 | 78 |
| stage4.refuse.qbi | refused | 64 | 58 | - | - |
| stage4.qbi.zero_income | complete | 64 | 60 | 64 | 64 |
| stage4.refuse.s2.amt | refused | 62 | 56 | - | - |
| stage4.refuse.s2.other | refused | 63 | 57 | - | - |
| stage4.refuse.s2.amt.simultaneous | refused | 62 | 56 | - | - |
| stage4.refuse.gift.sectionB | refused | 66 | 58 | - | - |
| stage4.salt.below | complete | 67 | 61 | 67 | 67 |
| stage4.salt.exact | complete | 67 | 61 | 67 | 67 |
| stage4.salt.phase | complete | 67 | 61 | 67 | 67 |
| stage4.salt.floor | complete | 66 | 60 | 66 | 66 |
| stage4.salt.above | complete | 66 | 60 | 66 | 66 |
| stage4.salt.mfs | refused | 61 | 55 | - | - |
| stage4.salt.mfs_floor | refused | 61 | 55 | - | - |
| stage4.salt.low_paid | complete | 66 | 60 | 66 | 66 |
| stage4.medical.below | complete | 64 | 58 | 64 | 64 |
| stage4.medical.above | complete | 64 | 58 | 64 | 64 |
| stage4.standard.single | complete | 66 | 58 | 66 | 66 |
| stage4.standard.hoh | complete | 83 | 66 | 82 | 83 |
| stage4.standard.qss | complete | 65 | 56 | 65 | 65 |
| stage4.standard.mfj | refused | 41 | 33 | - | - |
| stage4.standard.mfs | refused | 60 | 53 | - | - |
| stage4.standard.spouse_itemizes | refused | 58 | 52 | - | - |
| stage4.standard.itemized | complete | 64 | 58 | 64 | 64 |
| stage4.standard.elected | complete | 64 | 58 | 63 | 64 |
| stage4.gift.50000.false | complete | 69 | 61 | 69 | 69 |
| stage4.gift.500000.false | complete | 69 | 61 | 69 | 69 |
| stage4.gift.500001.true | complete | 70 | 61 | 70 | 70 |
| stage4.refuse.sa.unsupported | refused | 53 | 47 | - | - |
| stage4.refuse.sa.charity_limited | refused | 55 | 48 | - | - |
| stage4.refuse.sa.excluded_income | refused | 55 | 49 | - | - |
| stage4.refuse.standard.dependent | refused | 50 | 44 | - | - |
| stage4.refuse.dependent_itemizes | refused | 50 | 44 | - | - |
| stage4.refuse.standard.spouse_extra | refused | 59 | 53 | - | - |
| stage4.refuse.gift.special | refused | 64 | 56 | - | - |
| stage4.refuse.sa.unsupported.simultaneous | refused | 53 | 47 | - | - |
| stage4.deductions.combined | complete | 76 | 58 | 76 | 76 |
| audit.sa.negative_agi_medical | complete | 112 | 100 | 112 | 112 |
| audit.sa.negative_agi_medical_paid | complete | 112 | 99 | 112 | 112 |
| stage4.refuse.sb.unsupported | refused | 61 | 54 | - | - |
| stage4.refuse.sb.fbar_required | refused | 61 | 55 | - | - |
| stage4.refuse.sb.form8938 | refused | 62 | 56 | - | - |
| stage4.refuse.sb.line8 | refused | 63 | 57 | - | - |
| stage4.sb.foreign_no_filing | complete | 64 | 59 | 64 | 64 |
| stage4.refuse.sb.unsupported.simultaneous | refused | 61 | 54 | - | - |
| stage4.refuse.scope.schedule1 | refused | 38 | 33 | - | - |
| stage4.refuse.scope.credits | refused | 59 | 53 | - | - |
| stage4.refuse.scope.other_income | refused | 45 | 40 | - | - |
| stage4.refuse.scope.other_line16 | refused | 57 | 51 | - | - |
| stage4.refuse.married | refused | 59 | 54 | - | - |
| stage4.sdtw.special_rates | complete | 77 | 68 | 77 | 77 |
| stage4.sdtw.skip22 | complete | 78 | 68 | 77 | 78 |
| stage4.sdtw.skip32 | complete | 75 | 68 | 75 | 75 |
| stage4.sdtw.twenty_percent | complete | 77 | 68 | 77 | 77 |
| stage4.sdtw.lower_bracket | complete | 75 | 66 | 75 | 75 |
| stage4.sdtw.line12_takes_line9 | complete | 85 | 71 | 85 | 85 |
| stage4.mut.sdtw_28pct_no_1250 | complete | 77 | 69 | 77 | 77 |
| stage4.mut.sdtw_1250_line32_is_line1 | complete | 75 | 68 | 75 | 75 |
| stage4.feeders.shortloss | complete | 81 | 67 | 81 | 81 |

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
