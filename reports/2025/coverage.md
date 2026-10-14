# Branch coverage — Stage 1 fixtures

Which fixture case takes each choose-guard. Def lines appear per instance binding;
because guard predicates depend only on the bound amount, each def's guards are
covered once across instances rather than once per instance.

## f1040.line16 (2 guards)
- guard 0: qdcg.handworked.single, qdcg.gate.cgd, qdcg.sd.side, qdcg.l5.floor0, qdcg.l16.floor0, qdcg.20pct, qdcg.l7.picks.line1, qdcg.mfj.ceilings, qdcg.mfs.ceilings, qdcg.hoh.ceilings, qdcg.qss.ceilings, qdcg.tcw.through.line22
- guard 1: table.band.first, table.band.mid, table.band.last, switch.below, switch.exact, tcw.single.b1, tcw.single.b2, tcw.single.b3, tcw.single.b4, tcw.single.b5, tcw.single.seam.103350, tcw.single.seam.250525, tcw.single.seam.626350, tcw.mfj.b1, tcw.mfj.b2, tcw.mfj.b3, tcw.mfj.b4, tcw.mfj.b5, tcw.mfs.b1, tcw.mfs.b2, tcw.mfs.b3, tcw.mfs.b4, tcw.mfs.b5, tcw.hoh.b1, tcw.hoh.b2, tcw.hoh.b3, tcw.hoh.b4, tcw.hoh.b5, tcw.qss.b1, tcw.qss.b2, example.official, tcw.single.bound1.plus99c, tcw.single.bound2.plus99c, tcw.single.bound3.plus99c, tcw.single.bound4.plus99c, tcw.mfj.bound1.plus99c, tcw.mfj.bound2.plus99c, tcw.mfj.bound3.plus99c, tcw.mfj.bound4.plus99c, tcw.mfs.bound1.plus99c, tcw.mfs.bound2.plus99c, tcw.mfs.bound3.plus99c, tcw.mfs.bound4.plus99c, tcw.hoh.bound1.plus99c, tcw.hoh.bound2.plus99c, tcw.hoh.bound3.plus99c, tcw.hoh.bound4.plus99c

## qdcg.line3 (2 guards)
- guard 0: qdcg.sd.side
- guard 1: qdcg.handworked.single, qdcg.gate.cgd, qdcg.l5.floor0, qdcg.l16.floor0, qdcg.20pct, qdcg.l7.picks.line1, qdcg.mfj.ceilings, qdcg.mfs.ceilings, qdcg.hoh.ceilings, qdcg.qss.ceilings, qdcg.tcw.through.line22

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
- guard 0: table.band.first, table.band.mid, table.band.last, switch.below, example.official, qdcg.handworked.single, qdcg.gate.cgd, qdcg.sd.side, qdcg.l5.floor0, qdcg.l16.floor0, qdcg.l7.picks.line1, qdcg.mfs.ceilings, qdcg.hoh.ceilings, qdcg.qss.ceilings
- guard 1: switch.exact, tcw.single.b1, tcw.single.b2, tcw.single.b3, tcw.single.b4, tcw.single.b5, tcw.single.seam.103350, tcw.single.seam.250525, tcw.single.seam.626350, tcw.mfj.b1, tcw.mfj.b2, tcw.mfj.b3, tcw.mfj.b4, tcw.mfj.b5, tcw.mfs.b1, tcw.mfs.b2, tcw.mfs.b3, tcw.mfs.b4, tcw.mfs.b5, tcw.hoh.b1, tcw.hoh.b2, tcw.hoh.b3, tcw.hoh.b4, tcw.hoh.b5, tcw.qss.b1, tcw.qss.b2, qdcg.20pct, qdcg.mfj.ceilings, qdcg.tcw.through.line22, tcw.single.bound1.plus99c, tcw.single.bound2.plus99c, tcw.single.bound3.plus99c, tcw.single.bound4.plus99c, tcw.mfj.bound1.plus99c, tcw.mfj.bound2.plus99c, tcw.mfj.bound3.plus99c, tcw.mfj.bound4.plus99c, tcw.mfs.bound1.plus99c, tcw.mfs.bound2.plus99c, tcw.mfs.bound3.plus99c, tcw.mfs.bound4.plus99c, tcw.hoh.bound1.plus99c, tcw.hoh.bound2.plus99c, tcw.hoh.bound3.plus99c, tcw.hoh.bound4.plus99c

## tax_on_amount.undefined [root|inst:tax_on_amount#{"amount":"qdcg.line1","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.hoh.result] (0 guards)

## tax_on_amount.undefined [root|inst:tax_on_amount#{"amount":"qdcg.line1","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.mfj.result] (0 guards)

## tax_on_amount.undefined [root|inst:tax_on_amount#{"amount":"qdcg.line1","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.mfs.result] (0 guards)

## tax_on_amount.undefined [root|inst:tax_on_amount#{"amount":"qdcg.line1","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.single.result] (0 guards)

## tax_on_amount.tax [root|inst:tax_on_amount#{"amount":"qdcg.line1","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.tax] (2 guards)
- guard 0: switch.exact, tcw.single.b1, tcw.single.b2, tcw.single.b3, tcw.single.b4, tcw.single.b5, tcw.single.seam.103350, tcw.single.seam.250525, tcw.single.seam.626350, qdcg.20pct, qdcg.tcw.through.line22, tcw.single.bound1.plus99c, tcw.single.bound2.plus99c, tcw.single.bound3.plus99c, tcw.single.bound4.plus99c
- guard 1: tcw.mfj.b1, tcw.mfj.b2, tcw.mfj.b3, tcw.mfj.b4, tcw.mfj.b5, qdcg.mfj.ceilings, tcw.mfj.bound1.plus99c, tcw.mfj.bound2.plus99c, tcw.mfj.bound3.plus99c, tcw.mfj.bound4.plus99c

## tax_on_amount.tax [root|inst:tax_on_amount#{"amount":"qdcg.line5","status":"f1040.status"}.tax] (2 guards)
- guard 0: qdcg.handworked.single, qdcg.gate.cgd, qdcg.sd.side, qdcg.l5.floor0, qdcg.l16.floor0, qdcg.20pct, qdcg.l7.picks.line1, qdcg.mfs.ceilings, qdcg.hoh.ceilings, qdcg.qss.ceilings
- guard 1: qdcg.mfj.ceilings, qdcg.tcw.through.line22

## tax_on_amount.undefined [root|inst:tax_on_amount#{"amount":"qdcg.line5","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.mfj.result] (0 guards)

## tax_on_amount.undefined [root|inst:tax_on_amount#{"amount":"qdcg.line5","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.single.result] (0 guards)

## tax_on_amount.tax [root|inst:tax_on_amount#{"amount":"qdcg.line5","status":"f1040.status"}|inst:tcw#{"amount":"amount","status":"status"}.tax] (2 guards)
- guard 0: qdcg.tcw.through.line22
- guard 1: qdcg.mfj.ceilings
