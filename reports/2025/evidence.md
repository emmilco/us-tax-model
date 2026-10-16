# Evidence coverage per line

Fixtures that assert each line, by evidence class. A — official IRS example. B — human hand-work (pending; marked where recorded). C — recorded value also confirmed by the independently written Lean reference evaluator (running evaluator agreement, reports/2025/evaluator_agreement.md); the external-calculator comparison is the Stage 5 differential and remains pending. R — recorded synthetic regression, no class claimed, human review pending.

## Form 1099-DIV — distribution components and scope screening

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| div.box2b | — | — | — | — |
| div.box2c | — | — | — | — |
| div.box2d | — | — | — | — |
| div.box2e | — | — | — | — |
| div.box2f | — | — | — | — |
| div.box3 | — | — | — | — |
| div.box4 | — | — | — | — |
| div.box6 | — | — | — | — |
| div.box9 | — | — | — | — |
| div.box10 | — | — | — | — |
| div.box12 | — | — | — | — |
| div.box13 | — | — | — | — |
| div.basis_reconciled | — | — | — | — |
| div.fatca | — | — | — | — |
| div.box1a | — | — | — | — |
| div.box1b | — | — | — | — |
| div.box2a | — | — | — | — |
| div.box5 | — | — | — | — |
| div.section1202 | — | — | — | — |
| div.amt | — | — | — | — |
| div.unsupported | — | — | — | — |
| div.bad_special | — | — | — | — |
| div.screen | — | — | — | — |
| div.bad_components | — | — | — | — |
| div.special_total | — | — | — | — |

Unasserted lines: div.box1a, div.box1b, div.box2a, div.box5, div.section1202, div.amt, div.unsupported, div.bad_special, div.screen, div.bad_components, div.special_total

## Form 1040 — selected lines (Stages 1–4)

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| f1040.status | 1 (example.official) | 1 (qdcg.handworked.single) | 57 | — |
| f1040.line1a | — | — | — | 3 |
| f1040.line1z | — | — | — | 3 |
| f1040.line2b | — | — | — | 3 |
| f1040.line3b | — | — | — | 3 |
| f1040.line3a | 1 (example.official) | 1 (qdcg.handworked.single) | 57 | 3 |
| f1040.line7a | 1 (example.official) | 1 (qdcg.handworked.single) | 57 | 62 |
| f1040.line8 | — | — | — | 5 |
| f1040.line9 | — | — | — | 5 |
| f1040.line10 | — | — | — | 4 |
| f1040.line11a | — | — | — | 5 |
| f1040.line11b | — | — | — | 3 |
| f1040.line12e | — | — | — | 3 |
| f1040.line13a | — | — | — | 3 |
| f1040.line13b | — | — | — | 4 |
| f1040.line14 | — | — | — | 3 |
| f1040.line15 | 1 (example.official) | 1 (qdcg.handworked.single) | 57 | 5 |
| f1040.gate.qdcg_applies | 1 (example.official) | 1 (qdcg.handworked.single) | 57 | 7 |
| f1040.gate.sdtw | — | — | — | 5 |
| f1040.non_sdtw_tax | — | — | — | — |
| f1040.line16 | 1 (example.official) | 1 (qdcg.handworked.single) | 57 | 10 |
| f1040.line17 | — | — | — | 3 |
| f1040.line18 | — | — | — | 3 |
| f1040.line19 | — | — | — | 4 |
| f1040.line20 | — | — | — | 3 |
| f1040.line21 | — | — | — | 4 |
| f1040.line22 | — | — | — | 4 |
| f1040.line23 | — | — | — | 3 |
| f1040.line24 | — | — | — | 4 |
| f1040.line25a | — | — | — | 3 |
| f1040.line25b | — | — | — | 3 |
| f1040.line25c | — | — | — | 3 |
| f1040.line25d | — | — | — | 3 |
| f1040.line26 | — | — | — | 3 |
| f1040.line27a | — | — | — | 4 |
| f1040.line28 | — | — | — | 4 |
| f1040.line29 | — | — | — | 3 |
| f1040.line30 | — | — | — | 3 |
| f1040.line31 | — | — | — | 24 |
| f1040.line32 | — | — | — | 4 |
| f1040.line33 | — | — | — | 4 |
| f1040.line34 | — | — | — | 3 |
| f1040.line35a | — | — | — | 3 |
| f1040.line36 | — | — | — | 3 |
| f1040.line37 | — | — | — | 4 |

Unasserted lines: f1040.non_sdtw_tax

## Form 4952 — supported investment-interest deduction and election

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| f4952.line1 | — | — | — | — |
| f4952.carryover | — | — | — | — |
| f4952.unsupported | — | — | — | — |
| f4952.alternative_allocation | — | — | — | — |
| f4952.line4a | — | — | — | — |
| f4952.line4g | — | — | — | — |
| f4952.zero | — | — | — | — |
| f4952.line2 | — | — | — | 4 |
| f4952.line3 | — | — | — | — |
| f4952.line4b | — | — | — | — |
| f4952.bad_dividends | — | — | — | — |
| f4952.line4c | — | — | — | — |
| f4952.line4d | — | — | — | 1 (stage4.interest.short_term) |
| f4952.line4e | — | — | — | 1 (stage4.interest.short_term) |
| f4952.line4f | — | — | — | 1 (stage4.interest.short_term) |
| f4952.election_limit | — | — | — | 1 (stage4.interest.short_term) |
| f4952.bad_election | — | — | — | — |
| f4952.election | — | — | — | 5 |
| f4952.line4h | — | — | — | — |
| f4952.line5 | — | — | — | 4 |
| f4952.line6 | — | — | — | — |
| f4952.line7 | — | — | — | 3 |
| f4952.line8 | — | — | — | 8 |
| f4952.exception | — | — | — | — |
| f4952.required | — | — | — | 7 |

Unasserted lines: f4952.line4a, f4952.zero, f4952.line3, f4952.line4b, f4952.bad_dividends, f4952.line4c, f4952.bad_election, f4952.line4h, f4952.line6, f4952.exception

## Form 8959 — wage-only Additional Medicare Tax

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| f8959.unsupported | — | — | — | — |
| f8959.zero | — | — | — | — |
| f8959.line1 | — | — | — | 2 (stage4.medicare.withholding, stage4.refuse.8959) |
| f8959.line2 | — | — | — | 2 (stage4.medicare.withholding, stage4.refuse.8959) |
| f8959.line3 | — | — | — | 2 (stage4.medicare.withholding, stage4.refuse.8959) |
| f8959.line8 | — | — | — | 2 (stage4.medicare.withholding, stage4.refuse.8959) |
| f8959.line14 | — | — | — | 2 (stage4.medicare.withholding, stage4.refuse.8959) |
| f8959.line23 | — | — | — | 2 (stage4.medicare.withholding, stage4.refuse.8959) |
| f8959.line4 | — | — | — | 1 (stage4.medicare.withholding) |
| f8959.line5 | — | — | — | 1 (stage4.medicare.withholding) |
| f8959.line6 | 1 (stage4.official.medicare_example5) | — | — | 16 |
| f8959.line7 | — | — | — | 1 (stage4.medicare.withholding) |
| f8959.line9 | — | — | — | 1 (stage4.medicare.withholding) |
| f8959.line10 | — | — | — | 1 (stage4.medicare.withholding) |
| f8959.line11 | — | — | — | 1 (stage4.medicare.withholding) |
| f8959.line12 | — | — | — | 1 (stage4.medicare.withholding) |
| f8959.line13 | — | — | — | 1 (stage4.medicare.withholding) |
| f8959.line15 | — | — | — | 1 (stage4.medicare.withholding) |
| f8959.line16 | — | — | — | 1 (stage4.medicare.withholding) |
| f8959.line17 | — | — | — | 1 (stage4.medicare.withholding) |
| f8959.line18 | — | — | — | 18 |
| f8959.line19 | — | — | — | 2 (stage4.medicare.withholding, stage4.refuse.8959) |
| f8959.line20 | — | — | — | 1 (stage4.medicare.withholding) |
| f8959.line21 | — | — | — | 1 (stage4.medicare.withholding) |
| f8959.line22 | — | — | — | 1 (stage4.medicare.withholding) |
| f8959.line24 | — | — | — | 4 |

Unasserted lines: f8959.zero

## Form 8960 — wage, interest, dividend and securities slice

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| f8960.unsupported | — | — | — | — |
| f8960.refund | — | — | — | — |
| f8960.allocated_taxes | — | — | — | — |
| f8960.zero | — | — | — | — |
| f8960.line1 | — | — | — | 3 |
| f8960.line2 | — | — | — | — |
| f8960.line3 | — | — | — | 3 |
| f8960.line4a | — | — | — | 3 |
| f8960.line4b | — | — | — | 3 |
| f8960.line5b | — | — | — | 3 |
| f8960.line5c | — | — | — | 3 |
| f8960.line6 | — | — | — | 3 |
| f8960.line7 | — | — | — | 3 |
| f8960.line9c | — | — | — | 3 |
| f8960.line10 | — | — | — | 3 |
| f8960.line4c | — | — | — | — |
| f8960.line5a | — | — | — | 1 (stage4.niit.loss_floor) |
| f8960.line5d | — | — | — | — |
| f8960.line8 | — | — | — | 2 (stage4.niit.allocated, stage4.additional_taxes.combined) |
| f8960.line9a | — | — | — | 3 |
| f8960.line9b | — | — | — | 3 |
| f8960.line9d | — | — | — | 1 (stage4.additional_taxes.combined) |
| f8960.line11 | — | — | — | 1 (stage4.additional_taxes.combined) |
| f8960.line12 | — | — | — | 3 |
| f8960.line13 | — | — | — | 3 |
| f8960.line14 | — | — | — | — |
| f8960.line15 | — | — | — | — |
| f8960.line16 | — | — | — | — |
| f8960.line17 | — | — | — | 19 |
| f8960.bad_allocation | — | — | — | — |

Unasserted lines: f8960.zero, f8960.line2, f8960.line4c, f8960.line5d, f8960.line14, f8960.line15, f8960.line16, f8960.bad_allocation

## Form 8995 — dividend-only simplified computation

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| f8995.line2 | — | — | — | — |
| f8995.line3 | — | — | — | — |
| f8995.line4 | — | — | — | — |
| f8995.line5 | — | — | — | — |
| f8995.line7 | — | — | — | — |
| f8995.line16 | — | — | — | — |
| f8995.line17 | — | — | — | — |
| f8995.line6 | — | — | — | — |
| f8995.line8 | — | — | — | — |
| f8995.line9 | — | — | — | — |
| f8995.line10 | — | — | — | — |
| f8995.line11 | — | — | — | — |
| f8995.line12 | — | — | — | — |
| f8995.line13 | — | — | — | — |
| f8995.line14 | — | — | — | — |
| f8995.line15 | — | — | — | 6 |

Unasserted lines: f8995.line2, f8995.line3, f8995.line4, f8995.line5, f8995.line7, f8995.line16, f8995.line17, f8995.line6, f8995.line8, f8995.line9, f8995.line10, f8995.line11, f8995.line12, f8995.line13, f8995.line14

## Form 8995-A — Part IV dividend-only computation

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| f8995a.line27 | — | — | — | — |
| f8995a.line29 | — | — | — | — |
| f8995a.line38 | — | — | — | — |
| f8995a.line40 | — | — | — | — |
| f8995a.line28 | — | — | — | — |
| f8995a.line30 | — | — | — | — |
| f8995a.line31 | — | — | — | — |
| f8995a.line32 | — | — | — | — |
| f8995a.line33 | — | — | — | — |
| f8995a.line34 | — | — | — | — |
| f8995a.line35 | — | — | — | — |
| f8995a.line36 | — | — | — | — |
| f8995a.line37 | — | — | — | — |
| f8995a.line39 | — | — | — | 6 |

Unasserted lines: f8995a.line27, f8995a.line29, f8995a.line38, f8995a.line40, f8995a.line28, f8995a.line30, f8995a.line31, f8995a.line32, f8995a.line33, f8995a.line34, f8995a.line35, f8995a.line36, f8995a.line37

## Foreign tax credit — election without Form 1116

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| ftc.taxes | — | — | — | — |
| ftc.all_passive | — | — | — | — |
| ftc.statements | — | — | — | — |
| ftc.eligible | — | — | — | — |
| ftc.elect | — | — | — | — |
| ftc.limit | — | — | — | — |
| ftc.zero | — | — | — | — |
| ftc.has_tax | — | — | — | 1 (stage4.base) |
| ftc.needs1116 | — | — | — | — |
| ftc.limited | — | — | — | — |
| ftc.credit | — | — | — | 9 |

Unasserted lines: ftc.limit, ftc.zero, ftc.needs1116, ftc.limited

## 28% Rate Gain Worksheet — distribution-only path

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| g28.line1 | — | — | — | — |
| g28.line2 | — | — | — | — |
| g28.line3 | — | — | — | — |
| g28.line5 | — | — | — | — |
| g28.line4 | — | — | — | — |
| g28.line6 | — | — | — | — |
| g28.combined | — | — | — | — |
| g28.line7 | — | — | — | 1 (stage4.feeders.shortloss) |

Unasserted lines: g28.line1, g28.line2, g28.line3, g28.line5, g28.line4, g28.line6, g28.combined

## Form 8283 — groups of similar noncash property

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| gift.deduction | — | — | — | — |
| gift.public_securities | — | — | — | — |
| gift.special | — | — | — | — |
| gift.section_b | — | — | — | — |
| gift.allowed | — | — | — | — |

Unasserted lines: gift.section_b, gift.allowed

## Schedule B — interest payer entries

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| interest.amount | — | — | — | — |

## Excess Social Security credit — separately per person

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| person.rrta | — | — | — | — |
| person.employers | — | — | — | — |
| person.overcount | — | — | — | — |
| person.over | — | — | — | — |
| person.wages | — | — | — | — |
| person.withheld | — | — | — | — |
| person.box1 | — | — | — | — |
| person.box2 | — | — | — | — |
| person.eligible | — | — | — | — |
| person.excess | — | — | — | — |
| person.zero | — | — | — | — |
| person.credit | — | — | — | — |
| person.medicare5 | — | — | — | — |
| person.medicare6 | — | — | — | — |

Unasserted lines: person.employers, person.overcount, person.over, person.wages, person.withheld, person.box1, person.box2, person.eligible, person.excess, person.zero, person.credit, person.medicare5, person.medicare6

## Section 199A dividend-only deduction and form selection

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| qbi.dividends | — | — | — | — |
| qbi.unsupported | — | — | — | — |
| qbi.zero | — | — | — | — |
| qbi.eligible | — | — | — | — |
| qbi.taxable_before | — | — | — | 2 (stage4.qbi.income_limit, stage4.qbi.zero_income) |
| qbi.net_capital_gain | — | — | — | — |
| qbi.threshold | — | — | — | — |
| qbi.use_8995a | — | — | — | 3 |
| qbi.deduction | — | — | — | 11 |

Unasserted lines: qbi.zero, qbi.eligible, qbi.net_capital_gain, qbi.threshold

## Qualified Dividends and Capital Gain Tax Worksheet—Line 16

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| qdcg.schedule_d_filed | — | 1 (qdcg.handworked.single) | 11 | — |
| qdcg.schedule_d_net_gain | — | — | 1 (qdcg.sd.side) | — |
| qdcg.line1 | 1 (example.official) | 1 (qdcg.handworked.single) | 57 | — |
| qdcg.line2 | 1 (example.official) | 1 (qdcg.handworked.single) | 57 | — |
| qdcg.line3 | — | 1 (qdcg.handworked.single) | 11 | 3 |
| qdcg.line4 | — | 1 (qdcg.handworked.single) | 11 | — |
| qdcg.line5 | — | 1 (qdcg.handworked.single) | 11 | — |
| qdcg.line6 | 1 (example.official) | 1 (qdcg.handworked.single) | 57 | — |
| qdcg.line7 | 1 (example.official) | 1 (qdcg.handworked.single) | 57 | — |
| qdcg.line8 | — | 1 (qdcg.handworked.single) | 11 | — |
| qdcg.line9 | — | 1 (qdcg.handworked.single) | 11 | — |
| qdcg.line10 | — | 1 (qdcg.handworked.single) | 11 | — |
| qdcg.line11 | — | 1 (qdcg.handworked.single) | 11 | — |
| qdcg.line12 | — | 1 (qdcg.handworked.single) | 11 | — |
| qdcg.line13 | 1 (example.official) | 1 (qdcg.handworked.single) | 57 | — |
| qdcg.line14 | 1 (example.official) | 1 (qdcg.handworked.single) | 57 | — |
| qdcg.line15 | — | 1 (qdcg.handworked.single) | 11 | — |
| qdcg.line16 | — | 1 (qdcg.handworked.single) | 11 | — |
| qdcg.line17 | — | 1 (qdcg.handworked.single) | 11 | — |
| qdcg.line18 | — | 1 (qdcg.handworked.single) | 11 | — |
| qdcg.line19 | — | 1 (qdcg.handworked.single) | 11 | — |
| qdcg.line20 | — | 1 (qdcg.handworked.single) | 11 | — |
| qdcg.line21 | — | 1 (qdcg.handworked.single) | 11 | — |
| qdcg.line22 | — | 1 (qdcg.handworked.single) | 11 | 1 (qdcg.table.minimum.regression) |
| qdcg.line23 | — | 1 (qdcg.handworked.single) | 11 | 1 (qdcg.table.minimum.regression) |
| qdcg.line24 | 1 (example.official) | 1 (qdcg.handworked.single) | 57 | 1 (qdcg.table.minimum.regression) |
| qdcg.line25 | — | 1 (qdcg.handworked.single) | 11 | 1 (qdcg.table.minimum.regression) |

## Schedule 2 — supported Additional Medicare Tax and NIIT

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| s2.amt | — | — | — | — |
| s2.other | — | — | — | — |
| s2.zero | — | — | — | — |
| s2.line2 | — | — | — | 3 |
| s2.line3 | — | — | — | 3 |
| s2.line11 | — | — | — | 1 (stage4.additional_taxes.combined) |
| s2.line12 | — | — | — | 1 (stage4.additional_taxes.combined) |
| s2.line21 | — | — | — | 4 |

Unasserted lines: s2.zero

## Schedule 3 — selected lines

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| s3.line1 | — | — | — | — |
| s3.zero | — | — | — | — |
| s3.line8 | — | — | — | 3 |
| s3.married | — | — | — | — |
| s3.line9 | — | — | — | — |
| s3.line10 | — | — | — | — |
| s3.line11 | — | — | — | 21 |
| s3.line12 | — | — | — | — |
| s3.line14 | — | — | — | — |
| s3.line15 | — | — | — | 21 |

Unasserted lines: s3.line1, s3.zero, s3.married

## Schedule A — supported itemized deductions and standard comparison

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| sa.unsupported | — | — | — | — |
| sa.charity_limited | — | — | — | — |
| sa.excluded_income | — | — | — | — |
| sa.dependent | — | — | — | — |
| sa.spouse_extra | — | — | — | — |
| sa.age65 | — | — | — | — |
| sa.blind | — | — | — | — |
| sa.spouse_itemizes | — | — | — | — |
| sa.elect_itemize | — | — | — | — |
| sa.agi | — | — | — | — |
| sa.line1 | — | — | — | — |
| sa.line5a | — | — | — | — |
| sa.line5b | — | — | — | — |
| sa.line5c | — | — | — | — |
| sa.line8a | — | — | — | — |
| sa.line11 | — | — | — | — |
| sa.zero | — | — | — | — |
| sa.line2 | — | — | — | — |
| sa.line3 | — | — | — | 1 (stage4.medical.below) |
| sa.line4 | — | — | — | 3 |
| sa.line5d | — | — | — | 1 (stage4.deductions.combined) |
| sa.saltbase | — | — | — | — |
| sa.saltfloor | — | — | — | — |
| sa.saltthreshold | — | — | — | — |
| sa.saltexcess | — | — | — | — |
| sa.saltreduction | — | — | — | — |
| sa.saltremaining | — | — | — | — |
| sa.saltfloor_applied | — | — | — | — |
| sa.salthalf | — | — | — | 1 (stage4.salt.mfs_floor) |
| sa.mfs | — | — | — | — |
| sa.saltlimit | — | — | — | — |
| sa.line5e | — | — | — | 9 |
| sa.line6 | — | — | — | 5 |
| sa.line8b | — | — | — | 4 |
| sa.line8c | — | — | — | 4 |
| sa.line13 | — | — | — | 4 |
| sa.line15 | — | — | — | 4 |
| sa.line16 | — | — | — | 4 |
| sa.line7 | — | — | — | 1 (stage4.deductions.combined) |
| sa.line8e | — | — | — | 1 (stage4.deductions.combined) |
| sa.line9 | — | — | — | 1 (stage4.deductions.combined) |
| sa.line10 | — | — | — | 1 (stage4.deductions.combined) |
| sa.line12 | 1 (stage4.refuse.gift.sectionB) | — | — | 9 |
| sa.form8283 | — | — | — | 3 |
| sa.line14 | — | — | — | 1 (stage4.deductions.combined) |
| sa.line17 | — | — | — | 5 |
| sa.standardbase | — | — | — | — |
| sa.extra | — | — | — | — |
| sa.extra_age65 | — | — | — | — |
| sa.extra_blind | — | — | — | — |
| sa.standardraw | — | — | — | — |
| sa.standard | — | — | — | 9 |
| sa.itemizes | — | — | — | 6 |
| sa.deduction | — | — | — | 7 |
| sa.mfs_spouse_itemizes | — | — | — | — |

Unasserted lines: sa.agi, sa.zero, sa.line2, sa.saltbase, sa.saltfloor, sa.saltthreshold, sa.saltexcess, sa.saltreduction, sa.saltremaining, sa.saltfloor_applied, sa.mfs, sa.saltlimit, sa.standardbase, sa.extra, sa.extra_age65, sa.extra_blind, sa.standardraw, sa.mfs_spouse_itemizes

## Form 8949 and Schedule D — manually classified securities transactions

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| sales.box | — | — | — | — |
| sales.route | — | — | — | — |
| sales.code | — | — | — | — |
| sales.special | — | — | — | — |
| sales.aggregate_eligible | — | — | — | — |
| sales.proceeds | — | — | — | — |
| sales.reported_basis | — | — | — | — |
| sales.correct_basis | — | — | — | — |
| sales.wash_loss | — | — | — | — |
| sales.covered | — | — | — | — |
| sales.digital | — | — | — | — |
| sales.has_b | — | — | — | — |
| sales.has_w | — | — | — | — |
| sales.bad_code | — | — | — | — |
| sales.bad_aggregate | — | — | — | — |
| sales.one | — | — | — | — |
| sales.zero | — | — | — | — |
| sales.e | — | — | — | — |
| sales.b_difference | — | — | — | — |
| sales.adjust_b | — | — | — | — |
| sales.b | — | — | — | — |
| sales.w | — | — | — | — |
| sales.g | 4 | — | — | 12 |
| sales.before_adjustment | — | — | — | — |
| sales.h | 4 | — | — | 12 |

Unasserted lines: sales.covered, sales.digital, sales.has_b, sales.has_w, sales.bad_code, sales.bad_aggregate, sales.one, sales.zero, sales.e, sales.b_difference, sales.adjust_b, sales.b, sales.w, sales.before_adjustment

## Schedule B — supported interest and ordinary dividends

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| sb.unsupported | — | — | — | — |
| sb.ordinary_dividends | — | — | — | — |
| sb.line7a | — | — | — | — |
| sb.fbar_required | — | — | — | — |
| sb.form8938 | — | — | — | — |
| sb.line8 | — | — | — | — |
| sb.zero | — | — | — | — |
| sb.line2 | — | — | — | 6 |
| sb.line3 | — | — | — | 6 |
| sb.line4 | — | — | — | 6 |
| sb.line6 | — | — | — | 5 |
| sb.partIII | — | — | — | 1 (stage4.sb.foreign_no_filing) |

Unasserted lines: sb.zero

## Proof-of-concept scope screening

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| scope.schedule1 | — | — | — | — |
| scope.schedule1a | — | — | — | — |
| scope.credits | — | — | — | — |
| scope.other_income | — | — | — | — |
| scope.other_line16 | — | — | — | — |
| scope.ready | — | — | — | 6 |

## Schedule D — securities sales and supplied distribution subtotals

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| sd.other_forms | — | — | — | — |
| sd.carryover | — | — | — | — |
| sd.distributions | — | — | — | — |
| sd.line18 | — | — | — | — |
| sd.line19 | — | — | — | — |
| sd.filing4952 | — | — | — | — |
| sd.investment_election | — | — | — | — |
| sd.count | — | — | — | 14 |
| sd.screen | — | — | — | — |
| sd.filed | — | — | — | 22 |
| sd.zero | — | — | — | — |
| sd.line1a.d | — | — | — | 15 |
| sd.line1a.e | — | — | — | 15 |
| sd.line1a.g | — | — | — | 15 |
| sd.line1a.h | — | — | — | 15 |
| sd.line1b.d | — | — | — | 15 |
| sd.line1b.e | — | — | — | 15 |
| sd.line1b.g | — | — | — | 15 |
| sd.line1b.h | — | — | — | 17 |
| sd.line2.d | — | — | — | 15 |
| sd.line2.e | — | — | — | 15 |
| sd.line2.g | — | — | — | 15 |
| sd.line2.h | — | — | — | 16 |
| sd.line3.d | — | — | — | 15 |
| sd.line3.e | — | — | — | 15 |
| sd.line3.g | — | — | — | 15 |
| sd.line3.h | — | — | — | 16 |
| sd.line8a.d | 2 (sales.official.aggregate, sales.official.two_aggregate) | — | — | 15 |
| sd.line8a.e | 2 (sales.official.aggregate, sales.official.two_aggregate) | — | — | 15 |
| sd.line8a.g | — | — | — | 15 |
| sd.line8a.h | 2 (sales.official.aggregate, sales.official.two_aggregate) | — | — | 15 |
| sd.line8b.d | — | — | — | 15 |
| sd.line8b.e | — | — | — | 15 |
| sd.line8b.g | — | — | — | 15 |
| sd.line8b.h | — | — | — | 16 |
| sd.line9.d | — | — | — | 15 |
| sd.line9.e | — | — | — | 15 |
| sd.line9.g | — | — | — | 15 |
| sd.line9.h | — | — | — | 16 |
| sd.line10.d | — | — | — | 15 |
| sd.line10.e | — | — | — | 15 |
| sd.line10.g | — | — | — | 15 |
| sd.line10.h | — | — | — | 16 |
| sd.line4 | — | — | — | 2 (sales.refuse.carryover, sales.refuse.forms) |
| sd.line5 | — | — | — | 2 (sales.refuse.carryover, sales.refuse.forms) |
| sd.line6 | — | — | — | 2 (sales.refuse.carryover, sales.refuse.forms) |
| sd.line11 | — | — | — | 2 (sales.refuse.carryover, sales.refuse.forms) |
| sd.line12 | — | — | — | 2 (sales.refuse.carryover, sales.refuse.forms) |
| sd.line14 | — | — | — | 2 (sales.refuse.carryover, sales.refuse.forms) |
| sd.line13 | — | — | — | — |
| sd.line7 | — | — | — | 2 (sales.netting, sales.mixed_columns) |
| sd.line15 | — | — | — | 3 |
| sd.line16 | — | — | — | 21 |
| sd.line17 | — | — | — | — |
| sd.line20 | — | — | — | — |
| sd.loss_limit | — | — | — | — |
| sd.limited_loss | — | — | — | — |
| sd.has_loss | — | — | — | — |
| sd.line21 | — | — | — | 18 |
| sd.line22 | — | — | — | 49 |
| sd.to1040 | — | — | — | — |
| sd.net_gain_raw | — | — | — | 1 (sales.loss.single.700000) |
| sd.net_gain | — | — | — | — |

Unasserted lines: sd.line18, sd.line19, sd.filing4952, sd.investment_election, sd.screen, sd.zero, sd.line13, sd.line17, sd.line20, sd.loss_limit, sd.limited_loss, sd.has_loss, sd.to1040, sd.net_gain

## Schedule D Tax Worksheet

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| sdtw.zero | — | — | — | — |
| sdtw.ordinary_ceiling | — | — | — | — |
| sdtw.after22 | — | — | — | 1 (stage4.sdtw.skip22) |
| sdtw.after32 | — | — | — | 1 (stage4.sdtw.skip32) |
| sdtw.use1250 | — | — | — | — |
| sdtw.use28 | — | — | — | — |
| sdtw.line1 | — | — | — | 1 (stage4.sdtw.special_rates) |
| sdtw.line2 | — | — | — | 1 (stage4.sdtw.special_rates) |
| sdtw.line3 | — | — | — | 1 (stage4.sdtw.special_rates) |
| sdtw.line4 | — | — | — | 1 (stage4.sdtw.special_rates) |
| sdtw.line5 | — | — | — | 2 (stage4.interest.election, stage4.sdtw.special_rates) |
| sdtw.line6 | — | — | — | 2 (stage4.interest.election, stage4.sdtw.special_rates) |
| sdtw.line7 | — | — | — | 1 (stage4.sdtw.special_rates) |
| sdtw.line8 | — | — | — | 1 (stage4.sdtw.special_rates) |
| sdtw.line9 | — | — | — | 1 (stage4.sdtw.special_rates) |
| sdtw.line10 | — | — | — | 1 (stage4.sdtw.special_rates) |
| sdtw.line11 | — | — | — | 1 (stage4.sdtw.special_rates) |
| sdtw.line12 | — | — | — | 1 (stage4.sdtw.special_rates) |
| sdtw.line13 | — | — | — | 1 (stage4.sdtw.special_rates) |
| sdtw.line14 | — | — | — | 1 (stage4.sdtw.special_rates) |
| sdtw.line15 | — | — | — | 1 (stage4.sdtw.special_rates) |
| sdtw.line16 | — | — | — | 1 (stage4.sdtw.special_rates) |
| sdtw.line17 | — | — | — | 2 (stage4.sdtw.special_rates, stage4.sdtw.skip22) |
| sdtw.line18 | — | — | — | 1 (stage4.sdtw.special_rates) |
| sdtw.line19 | — | — | — | 1 (stage4.sdtw.special_rates) |
| sdtw.line20 | — | — | — | 1 (stage4.sdtw.special_rates) |
| sdtw.line21 | — | — | — | 2 (stage4.sdtw.special_rates, stage4.sdtw.lower_bracket) |
| sdtw.line22 | — | — | — | 1 (stage4.sdtw.special_rates) |
| sdtw.raw23 | — | — | — | — |
| sdtw.line23 | — | — | — | 1 (stage4.sdtw.special_rates) |
| sdtw.raw24 | — | — | — | — |
| sdtw.line24 | — | — | — | 1 (stage4.sdtw.special_rates) |
| sdtw.raw25 | — | — | — | — |
| sdtw.line25 | — | — | — | 1 (stage4.sdtw.special_rates) |
| sdtw.raw26 | — | — | — | — |
| sdtw.line26 | — | — | — | 1 (stage4.sdtw.special_rates) |
| sdtw.raw27 | — | — | — | — |
| sdtw.line27 | — | — | — | 1 (stage4.sdtw.special_rates) |
| sdtw.raw28 | — | — | — | — |
| sdtw.line28 | — | — | — | 1 (stage4.sdtw.special_rates) |
| sdtw.raw29 | — | — | — | — |
| sdtw.line29 | — | — | — | 1 (stage4.sdtw.special_rates) |
| sdtw.raw30 | — | — | — | — |
| sdtw.line30 | — | — | — | 2 (stage4.sdtw.special_rates, stage4.sdtw.twenty_percent) |
| sdtw.raw31 | — | — | — | — |
| sdtw.line31 | — | — | — | 4 |
| sdtw.raw32 | — | — | — | — |
| sdtw.line32 | — | — | — | 1 (stage4.sdtw.special_rates) |
| sdtw.raw33 | — | — | — | — |
| sdtw.line33 | — | — | — | 3 |
| sdtw.raw34 | — | — | — | — |
| sdtw.line34 | — | — | — | 2 (stage4.sdtw.special_rates, stage4.sdtw.twenty_percent) |
| sdtw.raw35 | — | — | — | — |
| sdtw.line35 | — | — | — | 1 (stage4.sdtw.special_rates) |
| sdtw.raw36 | — | — | — | — |
| sdtw.line36 | — | — | — | 1 (stage4.sdtw.special_rates) |
| sdtw.raw37 | — | — | — | — |
| sdtw.line37 | — | — | — | 1 (stage4.sdtw.special_rates) |
| sdtw.raw38 | — | — | — | — |
| sdtw.line38 | — | — | — | 2 (stage4.sdtw.special_rates, stage4.sdtw.lower_bracket) |
| sdtw.raw39 | — | — | — | — |
| sdtw.line39 | — | — | — | 2 (stage4.sdtw.special_rates, stage4.sdtw.lower_bracket) |
| sdtw.raw40 | — | — | — | — |
| sdtw.line40 | — | — | — | 2 (stage4.sdtw.special_rates, stage4.sdtw.twenty_percent) |
| sdtw.raw41 | — | — | — | — |
| sdtw.line41 | — | — | — | 1 (stage4.sdtw.special_rates) |
| sdtw.raw42 | — | — | — | — |
| sdtw.line42 | — | — | — | 1 (stage4.sdtw.special_rates) |
| sdtw.raw43 | — | — | — | — |
| sdtw.line43 | — | — | — | 5 |
| sdtw.line44 | — | — | — | 3 |
| sdtw.line45 | — | — | — | 2 (stage4.sdtw.special_rates, stage4.sdtw.twenty_percent) |
| sdtw.line46 | — | — | — | 2 (stage4.sdtw.special_rates, stage4.sdtw.twenty_percent) |
| sdtw.line47 | — | — | — | 2 (stage4.sdtw.special_rates, stage4.sdtw.skip22) |

Unasserted lines: sdtw.zero, sdtw.ordinary_ceiling, sdtw.use1250, sdtw.use28, sdtw.raw23, sdtw.raw24, sdtw.raw25, sdtw.raw26, sdtw.raw27, sdtw.raw28, sdtw.raw29, sdtw.raw30, sdtw.raw31, sdtw.raw32, sdtw.raw33, sdtw.raw34, sdtw.raw35, sdtw.raw36, sdtw.raw37, sdtw.raw38, sdtw.raw39, sdtw.raw40, sdtw.raw41, sdtw.raw42, sdtw.raw43

## Unrecaptured Section 1250 Gain Worksheet — distribution-only path

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| u1250.line1 | — | — | — | — |
| u1250.line2 | — | — | — | — |
| u1250.line3 | — | — | — | — |
| u1250.line4 | — | — | — | — |
| u1250.line5 | — | — | — | — |
| u1250.line6 | — | — | — | — |
| u1250.line7 | — | — | — | — |
| u1250.line8 | — | — | — | — |
| u1250.line9 | — | — | — | — |
| u1250.line10 | — | — | — | — |
| u1250.line12 | — | — | — | — |
| u1250.line16 | — | — | — | — |
| u1250.line11 | — | — | — | — |
| u1250.line13 | — | — | — | — |
| u1250.line14 | — | — | — | — |
| u1250.line15 | — | — | — | — |
| u1250.combined | — | — | — | — |
| u1250.line17 | — | — | — | 1 (stage4.feeders.shortloss) |
| u1250.line18 | — | — | — | 1 (stage4.feeders.shortloss) |

Unasserted lines: u1250.line1, u1250.line2, u1250.line3, u1250.line4, u1250.line5, u1250.line6, u1250.line7, u1250.line8, u1250.line9, u1250.line10, u1250.line12, u1250.line16, u1250.line11, u1250.line13, u1250.line14, u1250.line15, u1250.combined

## Form W-2 — wage, withholding and Social Security boxes by employer

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| w2.box1 | — | — | — | — |
| w2.box2 | — | — | — | — |
| w2.box3 | — | — | — | — |
| w2.box7 | — | — | — | — |
| w2.box4 | — | — | — | — |
| w2.wages | — | — | — | — |
| w2.one | — | — | — | — |
| w2.over | — | — | — | — |
| w2.box5 | — | — | — | — |
| w2.box6 | — | — | — | — |

Unasserted lines: w2.wages, w2.one, w2.over

## Tax on an amount — Tax Table or Tax Computation Worksheet

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| amount | — | — | — | — |
| status | — | — | — | — |
| below_boundary | — | — | — | — |
| table_tax | — | — | — | — |
| worksheet_tax | — | — | — | — |
| tax | — | — | — | — |

Unasserted lines: below_boundary, table_tax, worksheet_tax, tax

## Tax Computation Worksheet—Line 16

| line | A | B | C | R |
| --- | --- | --- | --- | --- |
| amount | — | — | — | — |
| status | — | — | — | — |
| single.row1.product | — | — | — | — |
| single.row1.tax | — | — | — | — |
| single.row2.product | — | — | — | — |
| single.row2.tax | — | — | — | — |
| single.row3.product | — | — | — | — |
| single.row3.tax | — | — | — | — |
| single.row4.product | — | — | — | — |
| single.row4.tax | — | — | — | — |
| single.row5.product | — | — | — | — |
| single.row5.tax | — | — | — | — |
| single.result | — | — | — | — |
| mfj.row1.product | — | — | — | — |
| mfj.row1.tax | — | — | — | — |
| mfj.row2.product | — | — | — | — |
| mfj.row2.tax | — | — | — | — |
| mfj.row3.product | — | — | — | — |
| mfj.row3.tax | — | — | — | — |
| mfj.row4.product | — | — | — | — |
| mfj.row4.tax | — | — | — | — |
| mfj.row5.product | — | — | — | — |
| mfj.row5.tax | — | — | — | — |
| mfj.result | — | — | — | — |
| mfs.row1.product | — | — | — | — |
| mfs.row1.tax | — | — | — | — |
| mfs.row2.product | — | — | — | — |
| mfs.row2.tax | — | — | — | — |
| mfs.row3.product | — | — | — | — |
| mfs.row3.tax | — | — | — | — |
| mfs.row4.product | — | — | — | — |
| mfs.row4.tax | — | — | — | — |
| mfs.row5.product | — | — | — | — |
| mfs.row5.tax | — | — | — | — |
| mfs.result | — | — | — | — |
| hoh.row1.product | — | — | — | — |
| hoh.row1.tax | — | — | — | — |
| hoh.row2.product | — | — | — | — |
| hoh.row2.tax | — | — | — | — |
| hoh.row3.product | — | — | — | — |
| hoh.row3.tax | — | — | — | — |
| hoh.row4.product | — | — | — | — |
| hoh.row4.tax | — | — | — | — |
| hoh.row5.product | — | — | — | — |
| hoh.row5.tax | — | — | — | — |
| hoh.result | — | — | — | — |
| tax | — | — | — | — |

Unasserted lines: single.row1.product, single.row1.tax, single.row2.product, single.row2.tax, single.row3.product, single.row3.tax, single.row4.product, single.row4.tax, single.row5.product, single.row5.tax, single.result, mfj.row1.product, mfj.row1.tax, mfj.row2.product, mfj.row2.tax, mfj.row3.product, mfj.row3.tax, mfj.row4.product, mfj.row4.tax, mfj.row5.product, mfj.row5.tax, mfj.result, mfs.row1.product, mfs.row1.tax, mfs.row2.product, mfs.row2.tax, mfs.row3.product, mfs.row3.tax, mfs.row4.product, mfs.row4.tax, mfs.row5.product, mfs.row5.tax, mfs.result, hoh.row1.product, hoh.row1.tax, hoh.row2.product, hoh.row2.tax, hoh.row3.product, hoh.row3.tax, hoh.row4.product, hoh.row4.tax, hoh.row5.product, hoh.row5.tax, hoh.result, tax

Unasserted computed lines across all documents: 234. (Supplied input lines are excluded; their correctness rests on reading the source document. Intermediate lines listed as unasserted are still exercised transitively; their detectability is tracked in reports/2025/mutation.md.)
Asserted keys not matching a line id: qdcg.f1040.line15, qdcg.f1040.line3a, qdcg.f1040.status, f1040.qdcg.line25, qdcg.sd.distributions