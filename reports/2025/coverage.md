# Branch coverage — all stage fixtures

Which fixture case takes each choose-guard. Def lines appear per instance binding;
because guard predicates depend only on the bound amount, each def's guards are
covered once across instances rather than once per instance.

## f1040.line16 (2 guards)
- guard 0: qdcg.handworked.single, qdcg.gate.cgd, qdcg.sd.side, qdcg.l5.floor0, qdcg.l16.floor0, qdcg.20pct, qdcg.l7.picks.line1, qdcg.mfj.ceilings, qdcg.mfs.ceilings, qdcg.hoh.ceilings, qdcg.qss.ceilings, qdcg.tcw.through.line22, qdcg.table.minimum.regression
- guard 1: table.band.first, table.band.mid, table.band.last, switch.below, switch.exact, tcw.single.b1, tcw.single.b2, tcw.single.b3, tcw.single.b4, tcw.single.b5, tcw.single.seam.103350, tcw.single.seam.250525, tcw.single.seam.626350, tcw.mfj.b1, tcw.mfj.b2, tcw.mfj.b3, tcw.mfj.b4, tcw.mfj.b5, tcw.mfs.b1, tcw.mfs.b2, tcw.mfs.b3, tcw.mfs.b4, tcw.mfs.b5, tcw.hoh.b1, tcw.hoh.b2, tcw.hoh.b3, tcw.hoh.b4, tcw.hoh.b5, tcw.qss.b1, tcw.qss.b2, example.official, tcw.single.bound1.plus99c, tcw.single.bound2.plus99c, tcw.single.bound3.plus99c, tcw.single.bound4.plus99c, tcw.mfj.bound1.plus99c, tcw.mfj.bound2.plus99c, tcw.mfj.bound3.plus99c, tcw.mfj.bound4.plus99c, tcw.mfs.bound1.plus99c, tcw.mfs.bound2.plus99c, tcw.mfs.bound3.plus99c, tcw.mfs.bound4.plus99c, tcw.hoh.bound1.plus99c, tcw.hoh.bound2.plus99c, tcw.hoh.bound3.plus99c, tcw.hoh.bound4.plus99c

## person.credit (2 guards)
- guard 0: ss.multi, ss.base.above, ss.withheld.below, ss.withheld.exact, ss.withheld.above, ss.tips, ss.hoh, ss.qss, ss.other.components
- guard 1: ss.base.below, ss.base.exact, ss.single.exact, ss.single.below, ss.none, ss.person.separation, ss.person.separation

## qdcg.line3 (2 guards)
- guard 0: qdcg.sd.side
- guard 1: qdcg.handworked.single, qdcg.gate.cgd, qdcg.l5.floor0, qdcg.l16.floor0, qdcg.20pct, qdcg.l7.picks.line1, qdcg.mfj.ceilings, qdcg.mfs.ceilings, qdcg.hoh.ceilings, qdcg.qss.ceilings, qdcg.tcw.through.line22, qdcg.table.minimum.regression

## tax_on_amount.tax [root|inst:tax_on_amount#{"amount":"f1040.line15","status":"f1040.status"}.tax] (2 guards)
- guard 0: table.band.first, table.band.mid, table.band.last, switch.below, example.official
- guard 1: switch.exact, tcw.single.b1, tcw.single.b2, tcw.single.b3, tcw.single.b4, tcw.single.b5, tcw.single.seam.103350, tcw.single.seam.250525, tcw.single.seam.626350, tcw.mfj.b1, tcw.mfj.b2, tcw.mfj.b3, tcw.mfj.b4, tcw.mfj.b5, tcw.mfs.b1, tcw.mfs.b2, tcw.mfs.b3, tcw.mfs.b4, tcw.mfs.b5, tcw.hoh.b1, tcw.hoh.b2, tcw.hoh.b3, tcw.hoh.b4, tcw.hoh.b5, tcw.qss.b1, tcw.qss.b2, tcw.single.bound1.plus99c, tcw.single.bound2.plus99c, tcw.single.bound3.plus99c, tcw.single.bound4.plus99c, tcw.mfj.bound1.plus99c, tcw.mfj.bound2.plus99c, tcw.mfj.bound3.plus99c, tcw.mfj.bound4.plus99c, tcw.mfs.bound1.plus99c, tcw.mfs.bound2.plus99c, tcw.mfs.bound3.plus99c, tcw.mfs.bound4.plus99c, tcw.hoh.bound1.plus99c, tcw.hoh.bound2.plus99c, tcw.hoh.bound3.plus99c, tcw.hoh.bound4.plus99c

## tax_on_amount.undefined [root|inst:tax_on_amount#{"amount":"f1040.line15","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.hoh.result] (0 guards)

## tax_on_amount.undefined [root|inst:tax_on_amount#{"amount":"f1040.line15","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.mfj.result] (0 guards)

## tax_on_amount.undefined [root|inst:tax_on_amount#{"amount":"f1040.line15","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.mfs.result] (0 guards)

## tax_on_amount.undefined [root|inst:tax_on_amount#{"amount":"f1040.line15","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.single.result] (0 guards)

## tax_on_amount.tax [root|inst:tax_on_amount#{"amount":"f1040.line15","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.tax] (2 guards)
- guard 0: switch.exact, tcw.single.b1, tcw.single.b2, tcw.single.b3, tcw.single.b4, tcw.single.b5, tcw.single.seam.103350, tcw.single.seam.250525, tcw.single.seam.626350, tcw.single.bound1.plus99c, tcw.single.bound2.plus99c, tcw.single.bound3.plus99c, tcw.single.bound4.plus99c
- guard 1: tcw.mfj.b1, tcw.mfj.b2, tcw.mfj.b3, tcw.mfj.b4, tcw.mfj.b5, tcw.mfj.bound1.plus99c, tcw.mfj.bound2.plus99c, tcw.mfj.bound3.plus99c, tcw.mfj.bound4.plus99c

## tax_on_amount.tax [root|inst:tax_on_amount#{"amount":"qdcg.line1","status":"f1040.status"}.tax] (2 guards)
- guard 0: table.band.first, table.band.mid, table.band.last, switch.below, example.official, qdcg.handworked.single, qdcg.gate.cgd, qdcg.sd.side, qdcg.l5.floor0, qdcg.l16.floor0, qdcg.l7.picks.line1, qdcg.mfs.ceilings, qdcg.hoh.ceilings, qdcg.qss.ceilings, qdcg.table.minimum.regression
- guard 1: switch.exact, tcw.single.b1, tcw.single.b2, tcw.single.b3, tcw.single.b4, tcw.single.b5, tcw.single.seam.103350, tcw.single.seam.250525, tcw.single.seam.626350, tcw.mfj.b1, tcw.mfj.b2, tcw.mfj.b3, tcw.mfj.b4, tcw.mfj.b5, tcw.mfs.b1, tcw.mfs.b2, tcw.mfs.b3, tcw.mfs.b4, tcw.mfs.b5, tcw.hoh.b1, tcw.hoh.b2, tcw.hoh.b3, tcw.hoh.b4, tcw.hoh.b5, tcw.qss.b1, tcw.qss.b2, qdcg.20pct, qdcg.mfj.ceilings, qdcg.tcw.through.line22, tcw.single.bound1.plus99c, tcw.single.bound2.plus99c, tcw.single.bound3.plus99c, tcw.single.bound4.plus99c, tcw.mfj.bound1.plus99c, tcw.mfj.bound2.plus99c, tcw.mfj.bound3.plus99c, tcw.mfj.bound4.plus99c, tcw.mfs.bound1.plus99c, tcw.mfs.bound2.plus99c, tcw.mfs.bound3.plus99c, tcw.mfs.bound4.plus99c, tcw.hoh.bound1.plus99c, tcw.hoh.bound2.plus99c, tcw.hoh.bound3.plus99c, tcw.hoh.bound4.plus99c

## tax_on_amount.undefined [root|inst:tax_on_amount#{"amount":"qdcg.line1","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.hoh.result] (0 guards)

## tax_on_amount.undefined [root|inst:tax_on_amount#{"amount":"qdcg.line1","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.mfj.result] (0 guards)

## tax_on_amount.undefined [root|inst:tax_on_amount#{"amount":"qdcg.line1","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.mfs.result] (0 guards)

## tax_on_amount.undefined [root|inst:tax_on_amount#{"amount":"qdcg.line1","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.single.result] (0 guards)

## tax_on_amount.tax [root|inst:tax_on_amount#{"amount":"qdcg.line1","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.tax] (2 guards)
- guard 0: switch.exact, tcw.single.b1, tcw.single.b2, tcw.single.b3, tcw.single.b4, tcw.single.b5, tcw.single.seam.103350, tcw.single.seam.250525, tcw.single.seam.626350, qdcg.20pct, qdcg.tcw.through.line22, tcw.single.bound1.plus99c, tcw.single.bound2.plus99c, tcw.single.bound3.plus99c, tcw.single.bound4.plus99c
- guard 1: tcw.mfj.b1, tcw.mfj.b2, tcw.mfj.b3, tcw.mfj.b4, tcw.mfj.b5, qdcg.mfj.ceilings, tcw.mfj.bound1.plus99c, tcw.mfj.bound2.plus99c, tcw.mfj.bound3.plus99c, tcw.mfj.bound4.plus99c

## tax_on_amount.tax [root|inst:tax_on_amount#{"amount":"qdcg.line5","status":"f1040.status"}.tax] (2 guards)
- guard 0: qdcg.handworked.single, qdcg.gate.cgd, qdcg.sd.side, qdcg.l5.floor0, qdcg.l16.floor0, qdcg.20pct, qdcg.l7.picks.line1, qdcg.mfs.ceilings, qdcg.hoh.ceilings, qdcg.qss.ceilings, qdcg.table.minimum.regression
- guard 1: qdcg.mfj.ceilings, qdcg.tcw.through.line22

## tax_on_amount.undefined [root|inst:tax_on_amount#{"amount":"qdcg.line5","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.mfj.result] (0 guards)

## tax_on_amount.undefined [root|inst:tax_on_amount#{"amount":"qdcg.line5","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.single.result] (0 guards)

## tax_on_amount.tax [root|inst:tax_on_amount#{"amount":"qdcg.line5","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.tax] (2 guards)
- guard 0: qdcg.tcw.through.line22
- guard 1: qdcg.mfj.ceilings

## Gates and arithmetic branches

- f1040.gate.qdcg_applies false: table.band.first, table.band.mid, table.band.last, switch.below, switch.exact, tcw.single.b1, tcw.single.b2, tcw.single.b3, tcw.single.b4, tcw.single.b5, tcw.single.seam.103350, tcw.single.seam.250525, tcw.single.seam.626350, tcw.mfj.b1, tcw.mfj.b2, tcw.mfj.b3, tcw.mfj.b4, tcw.mfj.b5, tcw.mfs.b1, tcw.mfs.b2, tcw.mfs.b3, tcw.mfs.b4, tcw.mfs.b5, tcw.hoh.b1, tcw.hoh.b2, tcw.hoh.b3, tcw.hoh.b4, tcw.hoh.b5, tcw.qss.b1, tcw.qss.b2, example.official, tcw.single.bound1.plus99c, tcw.single.bound2.plus99c, tcw.single.bound3.plus99c, tcw.single.bound4.plus99c, tcw.mfj.bound1.plus99c, tcw.mfj.bound2.plus99c, tcw.mfj.bound3.plus99c, tcw.mfj.bound4.plus99c, tcw.mfs.bound1.plus99c, tcw.mfs.bound2.plus99c, tcw.mfs.bound3.plus99c, tcw.mfs.bound4.plus99c, tcw.hoh.bound1.plus99c, tcw.hoh.bound2.plus99c, tcw.hoh.bound3.plus99c, tcw.hoh.bound4.plus99c
- f1040.gate.qdcg_applies true: qdcg.handworked.single, qdcg.gate.cgd, qdcg.sd.side, qdcg.l5.floor0, qdcg.l16.floor0, qdcg.20pct, qdcg.l7.picks.line1, qdcg.mfj.ceilings, qdcg.mfs.ceilings, qdcg.hoh.ceilings, qdcg.qss.ceilings, qdcg.tcw.through.line22, qdcg.table.minimum.regression
- person.rrta false: ss.multi, ss.base.below, ss.base.exact, ss.base.above, ss.withheld.below, ss.withheld.exact, ss.withheld.above, ss.single.exact, ss.single.below, ss.single.over, ss.multi.over, ss.tips, ss.none, ss.hoh, ss.qss, ss.other.components, ss.person.separation, ss.early.refusal
- person.rrta true: ss.rrta
- person.over false: ss.multi, ss.base.below, ss.base.exact, ss.base.above, ss.withheld.below, ss.withheld.exact, ss.withheld.above, ss.single.exact, ss.single.below, ss.tips, ss.none, ss.hoh, ss.qss, ss.other.components, ss.person.separation
- person.over true: ss.single.over, ss.multi.over, ss.early.refusal
- person.eligible false: ss.base.below, ss.base.exact, ss.single.exact, ss.single.below, ss.none, ss.person.separation
- person.eligible true: ss.multi, ss.base.above, ss.withheld.below, ss.withheld.exact, ss.withheld.above, ss.tips, ss.hoh, ss.qss, ss.other.components
- person.excess floor: ss.withheld.below, ss.withheld.exact
- person.excess positive: ss.multi, ss.base.above, ss.withheld.above, ss.tips, ss.hoh, ss.qss, ss.other.components
- qdcg.schedule_d_filed false: qdcg.handworked.single, qdcg.gate.cgd, qdcg.l5.floor0, qdcg.l16.floor0, qdcg.20pct, qdcg.l7.picks.line1, qdcg.mfj.ceilings, qdcg.mfs.ceilings, qdcg.hoh.ceilings, qdcg.qss.ceilings, qdcg.tcw.through.line22, qdcg.table.minimum.regression
- qdcg.schedule_d_filed true: qdcg.sd.side
- qdcg.line5 floor: qdcg.l5.floor0, qdcg.l16.floor0, qdcg.20pct
- qdcg.line5 positive: qdcg.handworked.single, qdcg.gate.cgd, qdcg.sd.side, qdcg.l7.picks.line1, qdcg.mfj.ceilings, qdcg.mfs.ceilings, qdcg.hoh.ceilings, qdcg.qss.ceilings, qdcg.tcw.through.line22, qdcg.table.minimum.regression
- qdcg.line7 left: table.band.first, table.band.mid, example.official, qdcg.l5.floor0, qdcg.l16.floor0, qdcg.l7.picks.line1, qdcg.hoh.ceilings, qdcg.qss.ceilings
- qdcg.line7 right: table.band.last, switch.below, switch.exact, tcw.single.b1, tcw.single.b2, tcw.single.b3, tcw.single.b4, tcw.single.b5, tcw.single.seam.103350, tcw.single.seam.250525, tcw.single.seam.626350, tcw.mfj.b1, tcw.mfj.b2, tcw.mfj.b3, tcw.mfj.b4, tcw.mfj.b5, tcw.mfs.b1, tcw.mfs.b2, tcw.mfs.b3, tcw.mfs.b4, tcw.mfs.b5, tcw.hoh.b1, tcw.hoh.b2, tcw.hoh.b3, tcw.hoh.b4, tcw.hoh.b5, tcw.qss.b1, tcw.qss.b2, qdcg.handworked.single, qdcg.gate.cgd, qdcg.sd.side, qdcg.20pct, qdcg.mfj.ceilings, qdcg.mfs.ceilings, qdcg.tcw.through.line22, tcw.single.bound1.plus99c, tcw.single.bound2.plus99c, tcw.single.bound3.plus99c, tcw.single.bound4.plus99c, tcw.mfj.bound1.plus99c, tcw.mfj.bound2.plus99c, tcw.mfj.bound3.plus99c, tcw.mfj.bound4.plus99c, tcw.mfs.bound1.plus99c, tcw.mfs.bound2.plus99c, tcw.mfs.bound3.plus99c, tcw.mfs.bound4.plus99c, tcw.hoh.bound1.plus99c, tcw.hoh.bound2.plus99c, tcw.hoh.bound3.plus99c, tcw.hoh.bound4.plus99c, qdcg.table.minimum.regression
- qdcg.line8 left: qdcg.handworked.single, qdcg.gate.cgd, qdcg.sd.side, qdcg.l5.floor0, qdcg.l16.floor0, qdcg.20pct, qdcg.l7.picks.line1, qdcg.mfs.ceilings, qdcg.hoh.ceilings, qdcg.qss.ceilings
- qdcg.line8 right: qdcg.mfj.ceilings, qdcg.tcw.through.line22, qdcg.table.minimum.regression
- qdcg.line10 left: qdcg.l5.floor0, qdcg.l16.floor0, qdcg.20pct
- qdcg.line10 right: qdcg.handworked.single, qdcg.gate.cgd, qdcg.sd.side, qdcg.l7.picks.line1, qdcg.mfj.ceilings, qdcg.mfs.ceilings, qdcg.hoh.ceilings, qdcg.qss.ceilings, qdcg.tcw.through.line22, qdcg.table.minimum.regression
- qdcg.line14 left: table.band.first, table.band.mid, table.band.last, switch.below, switch.exact, tcw.single.b1, tcw.single.b2, tcw.single.b3, tcw.single.b4, tcw.single.seam.103350, tcw.single.seam.250525, tcw.mfj.b1, tcw.mfj.b2, tcw.mfj.b3, tcw.mfs.b1, tcw.mfs.b2, tcw.mfs.b3, tcw.hoh.b1, tcw.hoh.b2, tcw.hoh.b3, tcw.hoh.b4, tcw.qss.b1, tcw.qss.b2, example.official, qdcg.handworked.single, qdcg.gate.cgd, qdcg.sd.side, qdcg.l5.floor0, qdcg.l16.floor0, qdcg.l7.picks.line1, qdcg.mfj.ceilings, qdcg.mfs.ceilings, qdcg.hoh.ceilings, qdcg.qss.ceilings, qdcg.tcw.through.line22, tcw.single.bound1.plus99c, tcw.single.bound2.plus99c, tcw.single.bound3.plus99c, tcw.mfj.bound1.plus99c, tcw.mfj.bound2.plus99c, tcw.mfj.bound3.plus99c, tcw.mfs.bound1.plus99c, tcw.mfs.bound2.plus99c, tcw.mfs.bound3.plus99c, tcw.hoh.bound1.plus99c, tcw.hoh.bound2.plus99c, tcw.hoh.bound3.plus99c, qdcg.table.minimum.regression
- qdcg.line14 right: tcw.single.b5, tcw.single.seam.626350, tcw.mfj.b4, tcw.mfj.b5, tcw.mfs.b4, tcw.mfs.b5, tcw.hoh.b5, qdcg.20pct, tcw.single.bound4.plus99c, tcw.mfj.bound4.plus99c, tcw.mfs.bound4.plus99c, tcw.hoh.bound4.plus99c
- qdcg.line16 floor: qdcg.l5.floor0, qdcg.l16.floor0, qdcg.l7.picks.line1, qdcg.hoh.ceilings, qdcg.qss.ceilings
- qdcg.line16 positive: qdcg.handworked.single, qdcg.gate.cgd, qdcg.sd.side, qdcg.20pct, qdcg.mfj.ceilings, qdcg.mfs.ceilings, qdcg.tcw.through.line22, qdcg.table.minimum.regression
- qdcg.line17 left: qdcg.handworked.single, qdcg.gate.cgd, qdcg.sd.side, qdcg.l5.floor0, qdcg.l16.floor0, qdcg.l7.picks.line1, qdcg.mfj.ceilings, qdcg.mfs.ceilings, qdcg.hoh.ceilings, qdcg.qss.ceilings, qdcg.tcw.through.line22, qdcg.table.minimum.regression
- qdcg.line17 right: qdcg.20pct
- qdcg.line25 left: qdcg.handworked.single, qdcg.gate.cgd, qdcg.sd.side, qdcg.l5.floor0, qdcg.l16.floor0, qdcg.20pct, qdcg.l7.picks.line1, qdcg.mfj.ceilings, qdcg.mfs.ceilings, qdcg.hoh.ceilings, qdcg.qss.ceilings, qdcg.tcw.through.line22
- qdcg.line25 right: qdcg.table.minimum.regression
- s3.married false: table.band.first, table.band.mid, table.band.last, switch.below, switch.exact, tcw.single.b1, tcw.single.b2, tcw.single.b3, tcw.single.b4, tcw.single.b5, tcw.single.seam.103350, tcw.single.seam.250525, tcw.single.seam.626350, tcw.hoh.b1, tcw.hoh.b2, tcw.hoh.b3, tcw.hoh.b4, tcw.hoh.b5, tcw.qss.b1, tcw.qss.b2, qdcg.handworked.single, qdcg.gate.cgd, qdcg.sd.side, qdcg.l5.floor0, qdcg.l16.floor0, qdcg.20pct, qdcg.l7.picks.line1, qdcg.hoh.ceilings, qdcg.qss.ceilings, qdcg.tcw.through.line22, tcw.single.bound1.plus99c, tcw.single.bound2.plus99c, tcw.single.bound3.plus99c, tcw.single.bound4.plus99c, tcw.hoh.bound1.plus99c, tcw.hoh.bound2.plus99c, tcw.hoh.bound3.plus99c, tcw.hoh.bound4.plus99c, ss.multi, ss.base.below, ss.base.exact, ss.base.above, ss.withheld.below, ss.withheld.exact, ss.withheld.above, ss.single.exact, ss.single.below, ss.single.over, ss.multi.over, ss.tips, ss.none, ss.rrta, ss.hoh, ss.qss, ss.other.components, ss.person.separation, qdcg.table.minimum.regression, ss.early.refusal
- s3.married true: tcw.mfj.b1, tcw.mfj.b2, tcw.mfj.b3, tcw.mfj.b4, tcw.mfj.b5, tcw.mfs.b1, tcw.mfs.b2, tcw.mfs.b3, tcw.mfs.b4, tcw.mfs.b5, example.official, qdcg.mfj.ceilings, qdcg.mfs.ceilings, tcw.mfj.bound1.plus99c, tcw.mfj.bound2.plus99c, tcw.mfj.bound3.plus99c, tcw.mfj.bound4.plus99c, tcw.mfs.bound1.plus99c, tcw.mfs.bound2.plus99c, tcw.mfs.bound3.plus99c, tcw.mfs.bound4.plus99c, ss.mfj, ss.mfs
- w2.over false: ss.multi, ss.base.below, ss.base.exact, ss.base.above, ss.withheld.below, ss.withheld.exact, ss.withheld.above, ss.single.exact, ss.single.below, ss.multi.over, ss.tips, ss.hoh, ss.qss, ss.other.components, ss.person.separation
- w2.over true: ss.single.over, ss.multi.over, ss.early.refusal

## Evidence by line

Synthetic regressions are not class B; independent human hand-work remains pending.

| Line | Evidence labels observed |
| --- | --- |
| f1040.status | A, B, C, synthetic-regression |
| f1040.line3a | A, B, C, synthetic-regression |
| f1040.line7a | A, B, C, synthetic-regression |
| f1040.line15 | A, B, C, synthetic-regression |
| f1040.gate.qdcg_applies | A, B, C, synthetic-regression |
| f1040.line16 | A, B, C, synthetic-regression |
| f1040.line31 | A, C, synthetic-regression |
| person.rrta | synthetic-regression |
| person.employers | synthetic-regression |
| person.overcount | synthetic-regression |
| person.over | synthetic-regression |
| person.wages | synthetic-regression |
| person.withheld | synthetic-regression |
| person.eligible | synthetic-regression |
| person.excess | synthetic-regression |
| person.zero | synthetic-regression |
| person.credit | synthetic-regression |
| qdcg.schedule_d_filed | B, C, synthetic-regression |
| qdcg.schedule_d_net_gain | C |
| qdcg.line1 | A, B, C, synthetic-regression |
| qdcg.line2 | A, B, C, synthetic-regression |
| qdcg.line3 | B, C, synthetic-regression |
| qdcg.line4 | B, C, synthetic-regression |
| qdcg.line5 | B, C, synthetic-regression |
| qdcg.line6 | A, B, C, synthetic-regression |
| qdcg.line7 | A, B, C, synthetic-regression |
| qdcg.line8 | B, C, synthetic-regression |
| qdcg.line9 | B, C, synthetic-regression |
| qdcg.line10 | B, C, synthetic-regression |
| qdcg.line11 | B, C, synthetic-regression |
| qdcg.line12 | B, C, synthetic-regression |
| qdcg.line13 | A, B, C, synthetic-regression |
| qdcg.line14 | A, B, C, synthetic-regression |
| qdcg.line15 | B, C, synthetic-regression |
| qdcg.line16 | B, C, synthetic-regression |
| qdcg.line17 | B, C, synthetic-regression |
| qdcg.line18 | B, C, synthetic-regression |
| qdcg.line19 | B, C, synthetic-regression |
| qdcg.line20 | B, C, synthetic-regression |
| qdcg.line21 | B, C, synthetic-regression |
| qdcg.line22 | B, C, synthetic-regression |
| qdcg.line23 | B, C, synthetic-regression |
| qdcg.line24 | A, B, C, synthetic-regression |
| qdcg.line25 | B, C, synthetic-regression |
| s3.married | A, B, C, synthetic-regression |
| s3.line9 | synthetic-regression |
| s3.line10 | synthetic-regression |
| s3.line11 | A, C, synthetic-regression |
| s3.line12 | synthetic-regression |
| s3.line14 | synthetic-regression |
| s3.line15 | A, C, synthetic-regression |
| w2.box3 | synthetic-regression |
| w2.box7 | synthetic-regression |
| w2.box4 | synthetic-regression |
| w2.wages | synthetic-regression |
| w2.one | synthetic-regression |
| w2.over | synthetic-regression |
| amount | See bound instances above |
| status | See bound instances above |
| below_boundary | See bound instances above |
| table_tax | See bound instances above |
| worksheet_tax | See bound instances above |
| tax | See bound instances above |
| amount | See bound instances above |
| status | See bound instances above |
| single.row1.product | See bound instances above |
| single.row1.tax | See bound instances above |
| single.row2.product | See bound instances above |
| single.row2.tax | See bound instances above |
| single.row3.product | See bound instances above |
| single.row3.tax | See bound instances above |
| single.row4.product | See bound instances above |
| single.row4.tax | See bound instances above |
| single.row5.product | See bound instances above |
| single.row5.tax | See bound instances above |
| single.result | See bound instances above |
| mfj.row1.product | See bound instances above |
| mfj.row1.tax | See bound instances above |
| mfj.row2.product | See bound instances above |
| mfj.row2.tax | See bound instances above |
| mfj.row3.product | See bound instances above |
| mfj.row3.tax | See bound instances above |
| mfj.row4.product | See bound instances above |
| mfj.row4.tax | See bound instances above |
| mfj.row5.product | See bound instances above |
| mfj.row5.tax | See bound instances above |
| mfj.result | See bound instances above |
| mfs.row1.product | See bound instances above |
| mfs.row1.tax | See bound instances above |
| mfs.row2.product | See bound instances above |
| mfs.row2.tax | See bound instances above |
| mfs.row3.product | See bound instances above |
| mfs.row3.tax | See bound instances above |
| mfs.row4.product | See bound instances above |
| mfs.row4.tax | See bound instances above |
| mfs.row5.product | See bound instances above |
| mfs.row5.tax | See bound instances above |
| mfs.result | See bound instances above |
| hoh.row1.product | See bound instances above |
| hoh.row1.tax | See bound instances above |
| hoh.row2.product | See bound instances above |
| hoh.row2.tax | See bound instances above |
| hoh.row3.product | See bound instances above |
| hoh.row3.tax | See bound instances above |
| hoh.row4.product | See bound instances above |
| hoh.row4.tax | See bound instances above |
| hoh.row5.product | See bound instances above |
| hoh.row5.tax | See bound instances above |
| hoh.result | See bound instances above |
| tax | See bound instances above |