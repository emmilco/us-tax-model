# Parameters, tax year 2025

## Enums

- `dependent_relationship`: child, sibling, sibling_descendant, parent, parent_relative, in_law, household_member, other — [i1040gi] pp. 17 and 19, Who Qualifies as Your Dependent, Steps 1 and 4: child is a son, daughter, stepchild, foster child or a descendant of any of them; sibling is a brother, sister, stepbrother, stepsister, half brother or half sister, or a son or daughter of a brother, sister, half brother or half sister (Step 4 lists step siblings but not their children); sibling_descendant is any other descendant of a sibling, including a step sibling's child (a qualifying child relationship under Step 1, and a Step 4 relative only as a household member who lived with you all year); parent is a father or mother; parent_relative is an ancestor or sibling of a parent (a Step 4 relative, but not the parent of Head of Household Test 1); in_law is a step-parent or an in-law; household_member is any other person who lived with you all year (2025; printed date 2026-02-25; sha256 482e9c48)
- `filing_status`: single, mfj, mfs, hoh, qss — [f1040] Form 1040, Filing Status (checkboxes) (2025; created 2025-09-05; sha256 3d31c226)
- `sales_box`: A, B, C, D, E, F, G, H, I, J, K, L — [f8949] Parts I and II, checkbox classifications (2025; created 2025-05-05; sha256 27451389)
- `sales_code`: none, B, W, BW, other — [i8949] pp. 7–11, columns (e) through (h), codes B and W (2025; printed date 2026-01-20; sha256 f077991c)
- `sales_route`: detail, aggregate — [i1040sd] p. 10, lines 1a and 8a (2025; printed date 2025-12-11; sha256 650643a6)

## Values

| Parameter | Type | Value | Cite |
| --- | --- | --- | --- |
| `actc.earned_floor` | NonNegDollars | $2,500 | [f1040s8812] Schedule 8812 (2025), line 19, "Is the amount on line 18a more than $2,500?" (2025; created 2025-07-30; sha256 6936462d) |
| `actc.per_child` | NonNegDollars | $1,700 | [f1040s8812] Schedule 8812 (2025), line 16b, "x $1,700" (2025; created 2025-07-30; sha256 6936462d) |
| `actc.rate` | Rate | 15% (0.15) | [f1040s8812] Schedule 8812 (2025), line 20, "Multiply the amount on line 19 by 15% (0.15)" (2025; created 2025-07-30; sha256 6936462d) |
| `actc.three_children` | NonNegDollars | $5,100 | [f1040s8812] Schedule 8812 (2025), after line 20, "On line 16b, is the amount $5,100 or more?" (2025; created 2025-07-30; sha256 6936462d) |
| `ctc.age_limit` | Count | 17 | [i1040gi] p. 18, Step 3, "Was the child under age 17 at the end of 2025?" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `ctc.per_child` | NonNegDollars | $2,200 | [f1040s8812] Schedule 8812 (2025), line 5, "Multiply line 4 by $2,200" (2025; created 2025-07-30; sha256 6936462d) |
| `ctc.phaseout_rate` | Rate | 5% (0.05) | [f1040s8812] Schedule 8812 (2025), line 11, "Multiply line 10 by 5% (0.05)" (2025; created 2025-07-30; sha256 6936462d) |
| `ctc.threshold` | NonNegDollars | single $200,000; mfj $400,000; mfs $200,000; hoh $200,000; qss $200,000 | [f1040s8812] Schedule 8812 (2025), line 9, "Married filing jointly—$400,000; All other filing statuses—$200,000" (2025; created 2025-07-30; sha256 6936462d) |
| `dependent.one` | Count | 1 | [f1040s8812] Schedule 8812 (2025), lines 4 and 6, "Number of qualifying children" and "Number of other dependents" (2025; created 2025-07-30; sha256 6936462d) |
| `eic.earned_amount0` | NonNegDollars | $8,490 | [rp-2024-40] section 3.06(1), Earned Income Amount, none (Rev. Proc. 2024-40; 2025 adjusted items; released 2024-10; sha256 4de9db6b) |
| `eic.earned_amount1` | NonNegDollars | $12,730 | [rp-2024-40] section 3.06(1), Earned Income Amount, one qualifying child (Rev. Proc. 2024-40; 2025 adjusted items; released 2024-10; sha256 4de9db6b) |
| `eic.earned_amount2` | NonNegDollars | $17,880 | [rp-2024-40] section 3.06(1), Earned Income Amount, two qualifying children (Rev. Proc. 2024-40; 2025 adjusted items; released 2024-10; sha256 4de9db6b) |
| `eic.earned_amount3` | NonNegDollars | $17,880 | [rp-2024-40] section 3.06(1), Earned Income Amount, three or more qualifying children (Rev. Proc. 2024-40; 2025 adjusted items; released 2024-10; sha256 4de9db6b) |
| `eic.investment_limit` | NonNegDollars | $11,950 | [i1040gi] p. 40, Step 2, question 2, "Is your investment income more than $11,950?" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `eic.limit0.joint` | NonNegDollars | $26,214 | [i1040gi] p. 40, Step 1, question 1, and p. 42, Step 5, question 3: "($26,214 if married filing jointly)" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `eic.limit0.other` | NonNegDollars | $19,104 | [i1040gi] p. 40, Step 1, question 1, and p. 42, Step 5, question 3: "No children ... less than $19,104" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `eic.limit1.joint` | NonNegDollars | $57,554 | [i1040gi] p. 40, Step 1, question 1, and p. 42, Step 5, question 3: "($57,554 if married filing jointly)" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `eic.limit1.other` | NonNegDollars | $50,434 | [i1040gi] p. 40, Step 1, question 1, and p. 42, Step 5, question 3: "1 child ... less than $50,434" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `eic.limit2.joint` | NonNegDollars | $64,430 | [i1040gi] p. 40, Step 1, question 1, and p. 42, Step 5, question 3: "($64,430 if married filing jointly)" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `eic.limit2.other` | NonNegDollars | $57,310 | [i1040gi] p. 40, Step 1, question 1, and p. 42, Step 5, question 3: "2 children ... less than $57,310" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `eic.limit3.joint` | NonNegDollars | $68,675 | [i1040gi] p. 40, Step 1, question 1, and p. 42, Step 5, question 3: "($68,675 if married filing jointly)" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `eic.limit3.other` | NonNegDollars | $61,555 | [i1040gi] p. 40, Step 1, question 1, and p. 42, Step 5, question 3: "3 or more children ... less than $61,555" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `eic.maximum0` | NonNegDollars | $649 | [rp-2024-40] section 3.06(1), Maximum Amount of Credit, none (Rev. Proc. 2024-40; 2025 adjusted items; released 2024-10; sha256 4de9db6b) |
| `eic.maximum1` | NonNegDollars | $4,328 | [rp-2024-40] section 3.06(1), Maximum Amount of Credit, one qualifying child (Rev. Proc. 2024-40; 2025 adjusted items; released 2024-10; sha256 4de9db6b) |
| `eic.maximum2` | NonNegDollars | $7,152 | [rp-2024-40] section 3.06(1), Maximum Amount of Credit, two qualifying children (Rev. Proc. 2024-40; 2025 adjusted items; released 2024-10; sha256 4de9db6b) |
| `eic.maximum3` | NonNegDollars | $8,046 | [rp-2024-40] section 3.06(1), Maximum Amount of Credit, three or more qualifying children (Rev. Proc. 2024-40; 2025 adjusted items; released 2024-10; sha256 4de9db6b) |
| `eic.table_start` | NonNegDollars | $1 | [i1040gi] p. 49, 2025 Earned Income Credit (EIC) Table, first row "At least 1 But less than 50" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `eic.ws_threshold0.joint` | NonNegDollars | $17,730 | [i1040gi] p. 46, Worksheet A, line 5, "($17,730 if married filing jointly)" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `eic.ws_threshold0.other` | NonNegDollars | $10,620 | [i1040gi] p. 46, Worksheet A, line 5, "No qualifying children ... less than $10,620" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `eic.ws_threshold1.joint` | NonNegDollars | $30,470 | [i1040gi] p. 46, Worksheet A, line 5, "($30,470 if married filing jointly)" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `eic.ws_threshold1.other` | NonNegDollars | $23,350 | [i1040gi] p. 46, Worksheet A, line 5, "1 or more qualifying children ... less than $23,350" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `ftc.limit` | NonNegDollars | single $300; mfj $600; mfs $300; hoh $300; qss $300 | [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; line 20 regular tax (2025; printed date 2025-12-23; sha256 6998cf8c) |
| `medicare.additional_rate` | Rate | 9/1000 | [f8959] Form 8959 (2025), lines 1–24; i8959 pp. 1–3 (2025; created 2025-04-30; sha256 13e64004) |
| `medicare.regular_rate` | Rate | 145/10000 | [f8959] Form 8959 (2025), lines 1–24; i8959 pp. 1–3 (2025; created 2025-04-30; sha256 13e64004) |
| `medicare.threshold` | NonNegDollars | single $200,000; mfj $250,000; mfs $125,000; hoh $200,000; qss $200,000 | [f8959] Form 8959 (2025), lines 1–24; i8959 pp. 1–3 (2025; created 2025-04-30; sha256 13e64004) |
| `niit.rate` | Rate | 38/1000 | [i8960] p. 2 thresholds; Form 8960 line 17 (2025; printed date 2026-02-04; sha256 b10fbb23) |
| `niit.threshold` | NonNegDollars | single $200,000; mfj $250,000; mfs $125,000; hoh $200,000; qss $250,000 | [i8960] p. 2 thresholds; Form 8960 line 17 (2025; printed date 2026-02-04; sha256 b10fbb23) |
| `odc.per_dependent` | NonNegDollars | $500 | [f1040s8812] Schedule 8812 (2025), line 7, "Multiply line 6 by $500" (2025; created 2025-07-30; sha256 6936462d) |
| `ordinary.table_boundary` | Dollars | $100,000 | [i1040gi] Instructions for Form 1040, line 16 (Tax Table or Tax Computation Worksheet) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `qbi.rate` | Rate | 1/5 | [f8995] Form 8995 (2025), lines 1–17; i8995 pp. 3–4 (2025; created 2025-09-12; sha256 55380ad2) |
| `qbi.threshold` | NonNegDollars | single $197,300; mfj $394,600; mfs $197,300; hoh $197,300; qss $197,300 | [f8995] Form 8995 (2025), lines 1–17; i8995 pp. 3–4 (2025; created 2025-09-12; sha256 55380ad2) |
| `qc.age_limit` | Count | 19 | [i1040gi] p. 17, Step 1, "Under age 19 at the end of 2025 and younger than you" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `qc.student_age_limit` | Count | 24 | [i1040gi] p. 17, Step 1, "Under age 24 at the end of 2025, a full-time student" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `qdcg.fifteen_rate_ceiling` | Dollars | single $533,400; mfj $600,050; mfs $300,000; hoh $566,700; qss $600,050 | [i1040gi] QDCGT worksheet, line 13 (2025; printed date 2026-02-25; sha256 482e9c48) |
| `qdcg.rate_15` | Rate | 15% (0.15) | [i1040gi] QDCGT worksheet, line 18 (2025; printed date 2026-02-25; sha256 482e9c48) |
| `qdcg.rate_20` | Rate | 20% (0.20) | [i1040gi] QDCGT worksheet, line 21 (2025; printed date 2026-02-25; sha256 482e9c48) |
| `qdcg.zero_rate_ceiling` | Dollars | single $48,350; mfj $96,700; mfs $48,350; hoh $64,750; qss $96,700 | [i1040gi] QDCGT worksheet, line 6 (2025; printed date 2026-02-25; sha256 482e9c48) |
| `qr.gross_income_limit` | NonNegDollars | $5,200 | [i1040gi] p. 19, Step 4, "Who had gross income of less than $5,200 in 2025" (2025; printed date 2026-02-25; sha256 482e9c48) |
| `sa.half` | Rate | 1/2 | [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12) |
| `sa.medical_rate` | Rate | 75/1000 | [f1040sa] Schedule A (2025), line 3 (2025; created 2025-11-20; sha256 c14acf34) |
| `sa.salt_base` | NonNegDollars | $40,000 | [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12) |
| `sa.salt_floor` | NonNegDollars | $10,000 | [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12) |
| `sa.salt_rate` | Rate | 3/10 | [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12) |
| `sa.salt_threshold` | NonNegDollars | single $500,000; mfj $500,000; mfs $250,000; hoh $500,000; qss $500,000 | [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12) |
| `sa.standard_base` | NonNegDollars | single $15,750; mfj $31,500; mfs $15,750; hoh $23,625; qss $31,500 | [i1040gi] pp. 34–35, line 12e and Standard Deduction Chart (2025; printed date 2026-02-25; sha256 482e9c48) |
| `sa.standard_extra` | NonNegDollars | single $2,000; mfj $1,600; mfs $1,600; hoh $2,000; qss $1,600 | [i1040gi] pp. 34–35, line 12e and Standard Deduction Chart (2025; printed date 2026-02-25; sha256 482e9c48) |
| `sales.one` | Count | 1 | [i8949] pp. 7–11, columns (e) through (h), codes B and W (2025; printed date 2026-01-20; sha256 f077991c) |
| `sales.zero` | NonNegDollars | $0 | [i8949] pp. 7–11, columns (e) through (h), codes B and W (2025; printed date 2026-01-20; sha256 f077991c) |
| `sd.loss_limit` | Dollars | single -$3,000; mfj -$3,000; mfs -$1,500; hoh -$3,000; qss -$3,000 | [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b) |
| `sdtw.ordinary_ceiling` | NonNegDollars | single $197,300; mfj $394,600; mfs $197,300; hoh $197,300; qss $394,600 | [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6) |
| `sdtw.rate15` | Rate | 15% (0.15) | [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6) |
| `sdtw.rate20` | Rate | 20% (0.20) | [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6) |
| `sdtw.rate25` | Rate | 25% (0.25) | [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6) |
| `sdtw.rate28` | Rate | 28% (0.28) | [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6) |
| `ss.base` | NonNegDollars | $176,100 | [i1040gi] p. 117, Schedule 3 line 11; independently confirmed iw2w3 p. 18 (2025; printed date 2026-02-25; sha256 482e9c48) |
| `ss.limit` | NonNegDollars | $10,918.20 | [i1040gi] p. 117, Schedule 3 line 11; independently confirmed iw2w3 p. 18 (2025; printed date 2026-02-25; sha256 482e9c48) |
| `ss.one` | Count | 1 | [i1040gi] p. 117, Schedule 3 line 11, more than one employer (2025; printed date 2026-02-25; sha256 482e9c48) |
| `ss.zero` | NonNegDollars | $0 | [i1040gi] p. 117, Schedule 3 line 11, amount withheld in excess (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.hoh.b1.rate` | Rate | 22% (0.22) | [i1040gi] TCW Section D, row 1 (multiply by 22%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.hoh.b1.subtract` | Dollars | $6,825 | [i1040gi] TCW Section D, row 1 (subtraction amount $6,825.00) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.hoh.b1.upper` | Dollars | $103,350 | [i1040gi] TCW Section D, row 1 (not over $103,350) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.hoh.b2.rate` | Rate | 24% (0.24) | [i1040gi] TCW Section D, row 2 (multiply by 24%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.hoh.b2.subtract` | Dollars | $8,892 | [i1040gi] TCW Section D, row 2 (subtraction amount $8,892.00) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.hoh.b2.upper` | Dollars | $197,300 | [i1040gi] TCW Section D, row 2 (not over $197,300) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.hoh.b3.rate` | Rate | 32% (0.32) | [i1040gi] TCW Section D, row 3 (multiply by 32%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.hoh.b3.subtract` | Dollars | $24,676 | [i1040gi] TCW Section D, row 3 (subtraction amount $24,676.00) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.hoh.b3.upper` | Dollars | $250,500 | [i1040gi] TCW Section D, row 3 (not over $250,500) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.hoh.b4.rate` | Rate | 35% (0.35) | [i1040gi] TCW Section D, row 4 (multiply by 35%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.hoh.b4.subtract` | Dollars | $32,191 | [i1040gi] TCW Section D, row 4 (subtraction amount $32,191.00) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.hoh.b4.upper` | Dollars | $626,350 | [i1040gi] TCW Section D, row 4 (not over $626,350) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.hoh.b5.rate` | Rate | 37% (0.37) | [i1040gi] TCW Section D, row 5 (multiply by 37%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.hoh.b5.subtract` | Dollars | $44,718 | [i1040gi] TCW Section D, row 5 (subtraction amount $44,718.00) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfj.b1.rate` | Rate | 22% (0.22) | [i1040gi] TCW Section B, row 1 (multiply by 22%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfj.b1.subtract` | Dollars | $10,172 | [i1040gi] TCW Section B, row 1 (subtraction amount $10,172.00) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfj.b1.upper` | Dollars | $206,700 | [i1040gi] TCW Section B, row 1 (not over $206,700) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfj.b2.rate` | Rate | 24% (0.24) | [i1040gi] TCW Section B, row 2 (multiply by 24%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfj.b2.subtract` | Dollars | $14,306 | [i1040gi] TCW Section B, row 2 (subtraction amount $14,306.00) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfj.b2.upper` | Dollars | $394,600 | [i1040gi] TCW Section B, row 2 (not over $394,600) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfj.b3.rate` | Rate | 32% (0.32) | [i1040gi] TCW Section B, row 3 (multiply by 32%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfj.b3.subtract` | Dollars | $45,874 | [i1040gi] TCW Section B, row 3 (subtraction amount $45,874.00) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfj.b3.upper` | Dollars | $501,050 | [i1040gi] TCW Section B, row 3 (not over $501,050) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfj.b4.rate` | Rate | 35% (0.35) | [i1040gi] TCW Section B, row 4 (multiply by 35%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfj.b4.subtract` | Dollars | $60,905.50 | [i1040gi] TCW Section B, row 4 (subtraction amount $60,905.50) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfj.b4.upper` | Dollars | $751,600 | [i1040gi] TCW Section B, row 4 (not over $751,600) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfj.b5.rate` | Rate | 37% (0.37) | [i1040gi] TCW Section B, row 5 (multiply by 37%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfj.b5.subtract` | Dollars | $75,937.50 | [i1040gi] TCW Section B, row 5 (subtraction amount $75,937.50) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfs.b1.rate` | Rate | 22% (0.22) | [i1040gi] TCW Section C, row 1 (multiply by 22%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfs.b1.subtract` | Dollars | $5,086 | [i1040gi] TCW Section C, row 1 (subtraction amount $5,086.00) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfs.b1.upper` | Dollars | $103,350 | [i1040gi] TCW Section C, row 1 (not over $103,350) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfs.b2.rate` | Rate | 24% (0.24) | [i1040gi] TCW Section C, row 2 (multiply by 24%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfs.b2.subtract` | Dollars | $7,153 | [i1040gi] TCW Section C, row 2 (subtraction amount $7,153.00) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfs.b2.upper` | Dollars | $197,300 | [i1040gi] TCW Section C, row 2 (not over $197,300) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfs.b3.rate` | Rate | 32% (0.32) | [i1040gi] TCW Section C, row 3 (multiply by 32%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfs.b3.subtract` | Dollars | $22,937 | [i1040gi] TCW Section C, row 3 (subtraction amount $22,937.00) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfs.b3.upper` | Dollars | $250,525 | [i1040gi] TCW Section C, row 3 (not over $250,525) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfs.b4.rate` | Rate | 35% (0.35) | [i1040gi] TCW Section C, row 4 (multiply by 35%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfs.b4.subtract` | Dollars | $30,452.75 | [i1040gi] TCW Section C, row 4 (subtraction amount $30,452.75) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfs.b4.upper` | Dollars | $375,800 | [i1040gi] TCW Section C, row 4 (not over $375,800) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfs.b5.rate` | Rate | 37% (0.37) | [i1040gi] TCW Section C, row 5 (multiply by 37%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.mfs.b5.subtract` | Dollars | $37,968.75 | [i1040gi] TCW Section C, row 5 (subtraction amount $37,968.75) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.single.b1.rate` | Rate | 22% (0.22) | [i1040gi] TCW Section A, row 1 (multiply by 22%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.single.b1.subtract` | Dollars | $5,086 | [i1040gi] TCW Section A, row 1 (subtraction amount $5,086.00) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.single.b1.upper` | Dollars | $103,350 | [i1040gi] TCW Section A, row 1 (not over $103,350) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.single.b2.rate` | Rate | 24% (0.24) | [i1040gi] TCW Section A, row 2 (multiply by 24%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.single.b2.subtract` | Dollars | $7,153 | [i1040gi] TCW Section A, row 2 (subtraction amount $7,153.00) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.single.b2.upper` | Dollars | $197,300 | [i1040gi] TCW Section A, row 2 (not over $197,300) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.single.b3.rate` | Rate | 32% (0.32) | [i1040gi] TCW Section A, row 3 (multiply by 32%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.single.b3.subtract` | Dollars | $22,937 | [i1040gi] TCW Section A, row 3 (subtraction amount $22,937.00) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.single.b3.upper` | Dollars | $250,525 | [i1040gi] TCW Section A, row 3 (not over $250,525) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.single.b4.rate` | Rate | 35% (0.35) | [i1040gi] TCW Section A, row 4 (multiply by 35%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.single.b4.subtract` | Dollars | $30,452.75 | [i1040gi] TCW Section A, row 4 (subtraction amount $30,452.75) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.single.b4.upper` | Dollars | $626,350 | [i1040gi] TCW Section A, row 4 (not over $626,350) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.single.b5.rate` | Rate | 37% (0.37) | [i1040gi] TCW Section A, row 5 (multiply by 37%) (2025; printed date 2026-02-25; sha256 482e9c48) |
| `tcw.single.b5.subtract` | Dollars | $42,979.75 | [i1040gi] TCW Section A, row 5 (subtraction amount $42,979.75) (2025; printed date 2026-02-25; sha256 482e9c48) |
