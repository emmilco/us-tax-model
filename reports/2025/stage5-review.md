# Stage 5 review packet

Stage 5 completes the single-person return: Form 1040 lines 1a–37 computed end to end — income, AGI, the standard-or-itemized choice, QBI, taxable income, tax through the QDCG/SDTW/table paths, Schedule 2 and 3 integration, payments, and refund/amount owed. AGI and taxable income are no longer supplied. The full interview (`--profile full`) walks this return; the three synthetic cases below double as the calculator-entry cases for the whole-return differential.

## Review against archived sources

Compare the three values sheets with the Form 1040 facsimile (sources/2025/f1040.txt, pages 1–2) for line labels and arithmetic, and with i1040gi for the instruction text: lines 1a–11b on pp. 23–34, the deduction lines on pp. 34–36, and the line 25–37 instructions. The QDCG and SDTW worksheets were reviewed at Stages 1 and 4; Stage 5 changes only what feeds them. Check that lines 13b, 19, 27a–30 refuse when their screens fire and that the scope screens propagate: a refused screen must refuse lines 8/10/13b/16/19 and everything downstream.

## Concrete checks

Case `stage5.return.owed` (two employers): wages 120,000.00 + interest 1,200.00 + ordinary dividends 2,000.00 (of which 1,500.00 qualified; line 3a is a component of line 3b, not an addend of line 9) = total income 123,200.00; standard deduction 15,750.00; taxable income 107,450.00; QDCG path with 1,500.00 preferential: tax on 105,950.00 at the 2025 single rates = 17,651.00 + 24% × 2,600.00 = 18,275.00, plus 15% × 1,500.00 = 225.00, total 18,500.00; withheld 17,000.00; amount owed 1,500.00. The sheet reports exactly these.

Case `stage5.return.refund` (one employer): wages 130,000.00; taxable income 114,250.00; tax = 17,651.00 + 24% × 10,900.00 = 20,267.00; withheld 20,000.00 plus 2,000.00 estimated = 22,000.00; overpaid 1,733.00, refunded 1,733.00.

Case `stage5.return.itemized`: total income 102,500.00 = wages 90,000.00 + interest 1,000.00 + ordinary dividends 4,000.00 (of which 2,000.00 qualified) + capital gain 7,500.00 (a 6,000.00 long-term sale plus 1,500.00 of distributions); itemized deductions 27,300.00 = state and local taxes 10,000.00 + mortgage interest 10,000.00 + cash gifts 5,000.00 + noncash gift 800.00 + investment interest 1,500.00 (medical 3,000.00 is zero after the 7.5% floor); AGI 102,500.00; QBI deduction 60.00 (20% of the 300.00 section 199A dividends); taxable income 75,140.00; QDCG tax 10,777.00 = Tax Table on 65,640.00 ordinary (9,352.00) plus 15% × 9,500.00 (1,425.00); the 120.00 foreign tax credit reduces it (Form 1040 line 20) to 10,657.00; withheld 10,000.00; amount owed 657.00.

- [stage5.return.owed](stage5.return.owed.txt)
- [stage5.return.refund](stage5.return.refund.txt)
- [stage5.return.itemized](stage5.return.itemized.txt)

## Migration record

Every fixture that supplied `f1040.line15` or `sa.agi` was migrated to real income inputs that reproduce the fixture’s intended value: 178 cases reconstructed with an income entry (one W-2 employer), verified against the original anchors; 79 cases (refusals, the Stage 2 cohort) kept answers only; three cases fund their target through an offsetting cash-gift deduction instead of wages (qdcg.l5.floor0, qdcg.20pct, stage4.sdtw.skip22); one case needed a manual anchor correction (stage4.ftc.regular_limit, whose credit limit is tested against a zero tax). The `qdcg.table.minimum.regression` fixture moved from stage2.json to stage1.json because the Stage 2 finite-domain check enumerates every Boolean in each fixture and its chain now reaches the whole return. The sales interview profile gained the base-chain questions its targets now reach (22 blocks copied from the Stage 4 profile); the Stage 4 profile gained w2.box1. Interview walk caps in the integration checks were raised (50 → 150 steps) to match the deeper chain.

## Limits and evidence

Return-wide whole-dollar rounding remains deferred (standing ambiguity; exact cents throughout). Lines 25b, 25c, 26, 35a and 36 are supplied elections or totals read from the filer’s records; nothing else on the return is supplied. The estimated tax penalty is not computed — the output states that the IRS will figure it. Joint and MFS returns are refused; Form 1116 and the other deferrals are unchanged from Stage 4. No human hand-work or source reading is claimed (spec 3, requirement 11); the independent constructions of spec 6.5 stand in for them. The whole-return differential (class C) is prepared — entry sheets at reports/2025/differential.<case>.md, records go to fixtures/2025/differential/. These two cases were corrected under BUG-0001 (BUG_INVENTORY.md), which an engine comparison caught. See evidence.md for per-line class coverage, and mutation.md, coverage.md, evaluator_agreement.md for the generated verification evidence.
