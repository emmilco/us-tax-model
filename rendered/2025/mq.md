# Mid-quarter convention test for property placed in service in 2025

- Document: `mq` (worksheet, tax year 2025)
- Note: The 40% test of Pub. 946, figured once for the return (both spouses together on a joint return, amb.2025.mq_joint) over the business-use bases after section 179 and before the special allowance; compared exactly as 5 × fourth-quarter bases against 2 × all bases.

## (helper) — `mq.q4`

- **Authored helper label:** Depreciable bases of property placed in service October to December 2025
- **Encoded (NonNegDollars):** Add person.mq_q4 over every confirmed person entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.mq_q4","op":"sum_over"}`
- Cite: [p946] p. 34, Which Convention Applies?, Mid-quarter convention (amb.2025.mq_joint: both spouses together) (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `mq.total`

- **Authored helper label:** Depreciable bases of all property placed in service in 2025
- **Encoded (NonNegDollars):** Add person.mq_total over every confirmed person entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.mq_total","op":"sum_over"}`
- Cite: [p946] p. 34, Which Convention Applies?, Mid-quarter convention (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `mq.five`

- **Authored helper label:** Five
- **Encoded (Count):** Enter 5 (sc.count5).
- Expr: `{"op":"param","ref":"sc.count5"}`
- Cite: [p946] p. 34, Which Convention Applies?, "are more than 40% of the total" (40% = 2/5) (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `mq.two`

- **Authored helper label:** Two
- **Encoded (Count):** Enter 2 (sc.count2).
- Expr: `{"op":"param","ref":"sc.count2"}`
- Cite: [p946] p. 34, Which Convention Applies? (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `mq.q4x5`

- **Authored helper label:** Five times the October to December bases
- **Encoded (NonNegDollars):** Multiply helper "Depreciable bases of property placed in service October to December 2025" by the number on helper "Five".
- Expr: `{"amount":"mq.q4","count":"mq.five","op":"multiply_count"}`
- Cite: [p946] p. 34, Which Convention Applies? (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `mq.totalx2`

- **Authored helper label:** Two times all 2025 bases
- **Encoded (NonNegDollars):** Multiply helper "Depreciable bases of all property placed in service in 2025" by the number on helper "Two".
- Expr: `{"amount":"mq.total","count":"mq.two","op":"multiply_count"}`
- Cite: [p946] p. 34, Which Convention Applies? (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `mq.applies`

- **Authored helper label:** The mid-quarter convention applies: the October to December bases are more than 40% of all 2025 bases
- **Encoded (Bool):** helper "Five times the October to December bases" > helper "Two times all 2025 bases"
- Expr: `{"gt":["mq.q4x5","mq.totalx2"],"op":"test"}`
- Cite: [p946] p. 34, Which Convention Applies?, Mid-quarter convention, "are more than 40% of the total depreciable bases of all MACRS property you placed in service during the entire year" (For use in preparing 2025 returns; sha256 07fadfb2)
