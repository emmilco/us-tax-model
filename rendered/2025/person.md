# Excess Social Security credit — separately per person

- Document: `person` (worksheet, tax year 2025)
- Collection: keyed entries; [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)
- Note: Helper worksheet. Wages means boxes 3 plus 7 under approved interpretation amb.2025.ss_wages. Independent lines may compute while credit and dependent totals are refused.

## rrta — `person.rrta`

- **Authored helper label:** Do any wage statements report railroad retirement compensation or taxes (W-2 box 14)?
- **Encoded (Bool):** Input — Do any wage statements report railroad retirement compensation or taxes (W-2 box 14)?
- Expr: `{"op":"input","source":"Do any wage statements report railroad retirement compensation or taxes (W-2 box 14)?"}`
- Cite: [iw2w3] pp. 12–13, Railroad employers: RRTA compensation and taxes in box 14; boxes 3–7 are not used for RRTA (2025; printed date 2025-02-19; sha256 bfecbc99)

## employers — `person.employers`

- **Authored helper label:** Total w2.one for this person
- **Encoded (Count):** Add w2.one over every confirmed w2 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"w2","field":"w2.one","op":"sum_over"}`
- Cite: [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)

## overcount — `person.overcount`

- **Authored helper label:** Number of employers that withheld more than the limit
- **Encoded (Count):** Add w2.one over every confirmed w2 entry for which helper "Did this employer withhold more than $10,918.20?" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"w2","field":"w2.one","op":"sum_over","where":{"eq":["w2.over",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)

## over — `person.over`

- **Authored helper label:** Any employer withheld more than the limit
- **Encoded (Bool):** line overcount > 0 (a count)
- Expr: `{"gt":["person.overcount",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)

## wages — `person.wages`

- **Authored helper label:** Total w2.wages for this person
- **Encoded (NonNegDollars):** Add w2.wages over every confirmed w2 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Interpretation: amb.2025.ss_wages
- Expr: `{"collection":"w2","field":"w2.wages","op":"sum_over"}`
- Cite: [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)

## withheld — `person.withheld`

- **Authored helper label:** Total w2.box4 for this person
- **Encoded (NonNegDollars):** Add w2.box4 over every confirmed w2 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"w2","field":"w2.box4","op":"sum_over"}`
- Cite: [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.box1`

- **Authored helper label:** Total W-2 box 1 for this person
- **Encoded (NonNegDollars):** Add w2.box1 over every confirmed w2 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"w2","field":"w2.box1","op":"sum_over"}`
- Cite: [f1040] Form 1040 (2025), line 1a (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `person.box2`

- **Authored helper label:** Total W-2 box 2 for this person
- **Encoded (NonNegDollars):** Add w2.box2 over every confirmed w2 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"w2","field":"w2.box2","op":"sum_over"}`
- Cite: [f1040] Form 1040 (2025), line 25a (2025; created 2025-09-05; sha256 3d31c226)

## eligible — `person.eligible`

- **Authored helper label:** More than one employer and total social security wages over $176,100
- **Encoded (Bool):** line employers > 1 (a count) and line wages > $176,100 (ss.base)
- Expr: `{"all":[{"gt":["person.employers",{"const":1,"type":"Count"}],"op":"test"},{"gt":["person.wages",{"param":"ss.base"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)

## excess — `person.excess`

- **Authored helper label:** Withholding above $10,918.20, if any
- **Encoded (NonNegDollars):** Subtract $10,918.20 (ss.limit) from line withheld. If zero or less, enter -0-.
- Expr: `{"from":"person.withheld","op":"subtract_floor0","take":{"param":"ss.limit"}}`
- Cite: [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)

## zero — `person.zero`

- **Authored helper label:** No excess credit
- **Encoded (NonNegDollars):** Enter $0 (ss.zero).
- Expr: `{"op":"param","ref":"ss.zero"}`
- Cite: [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)

## credit — `person.credit`

- **Authored helper label:** Excess social security tax withheld, figured separately for this person
- **Encoded (NonNegDollars):** Choose — [line eligible = true → line excess] [line eligible = false → line zero]
- **Refusal:** when person.rrta is true, cannot complete Schedule 3 line 11 (RRTA path). This stage handles Social Security only. Use the railroad retirement instructions; excess Tier 2 tax uses Form 843 rather than Form 1040. Cite: [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when person.over is true, cannot complete Form 843. An employer withheld more than $10,918.20. Ask that employer to adjust the tax. If the employer does not adjust the overcollection, you can file a refund claim using Form 843. This tool cannot complete the credit until the overcollection is resolved. Cite: [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"alternatives":[{"guard":{"eq":["person.eligible",{"const":true}],"op":"test"},"then":"person.excess"},{"guard":{"eq":["person.eligible",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.medicare5`

- **Authored helper label:** Total W-2 box 5 for this person
- **Encoded (NonNegDollars):** Add w2.box5 over every confirmed w2 entry, within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when person.rrta is true, cannot complete Form 8959 RRTA computation. RRTA compensation is outside the supported wage-only path. Cite: [f8959] Form 8959 (2025), lines 1–24; i8959 pp. 1–3 (2025; created 2025-04-30; sha256 13e64004)
- Expr: `{"collection":"w2","field":"w2.box5","op":"sum_over"}`
- Cite: [f8959] Form 8959 (2025), lines 1–24; i8959 pp. 1–3 (2025; created 2025-04-30; sha256 13e64004)

## (helper) — `person.medicare6`

- **Authored helper label:** Total W-2 box 6 for this person
- **Encoded (NonNegDollars):** Add w2.box6 over every confirmed w2 entry, within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when person.rrta is true, cannot complete Form 8959 RRTA computation. RRTA compensation is outside the supported wage-only path. Cite: [f8959] Form 8959 (2025), lines 1–24; i8959 pp. 1–3 (2025; created 2025-04-30; sha256 13e64004)
- Expr: `{"collection":"w2","field":"w2.box6","op":"sum_over"}`
- Cite: [f8959] Form 8959 (2025), lines 1–24; i8959 pp. 1–3 (2025; created 2025-04-30; sha256 13e64004)
