# Class M hand-work — carloan

`Qualified passenger vehicle loan interest (Schedule 1-A, line 22) — one entry per loan` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-27 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt policy | worked-values-request-bound-v2 |
| system sha256 | 18ff9cfe094eedd0548bba02012b0ebf2a58d0606e834e3633432585b4192cb7 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 2e12660cf7d2fc26623d642095e0432ae4dfb7cff88953b848eaff3e1bf90f08 |
| cases | 3 |
| worked target scope | printed IRS lines |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 23, 109, 110 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 23, 109, 110 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| fr-2025-24154 | Federal Register Vol. 91, No. 1 (2026-01-02), proposed rules REG-113515-25 (Car Loan Interest Deduction), FR Doc. 2025-24154 | 20, 21, 22, 23 | cited pages | eccaf8550a66615e5932726cb4e98cab002b31b9f13c5d4ffec11f0619af479e | 20, 21, 22, 23 | 1bb1f46bab043ddeabc4cb276a0d67fa478ae7aa38088b47ecfae848df4954c9 |
| i1040sc | 2025 | 6 | pages named by another document's citation | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 6 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |

## Lines

### case classm.carloan.1 — prompt sha256 f8611817b9130fa784b050ecf88f5af9df42875a22cd03d265b893b701eee07e; branches: carloan.requirements:false, carloan.requirements:true, carloan.vehicle:true, carloan.eligible:false, carloan.eligible:true, carloan.mixed:false, carloan.mixed:true, carloan.nonqualifying_debt:floor, carloan.nonqualifying_debt:positive, carloan.mixed_qualifying:floor, carloan.mixed_qualifying:positive, carloan.refi_whole:true, carloan.refi_qualifying:left, carloan.refi_qualifying:right, carloan.refi_nested:false, carloan.allocated#0, carloan.allocated#1, carloan.mixed_interest#0, carloan.mixed_interest#1, carloan.qpvli#0, carloan.qpvli#1, carloan.sc_interest#1, carloan.sc_mixed#0, carloan.sc_mixed#1, carloan.sc_allocated#0, carloan.sc_allocated#1, carloan.col_ii#0, carloan.col_ii#1, carloan.col_iii:floor

### classm.carloan.1 — carloan[vin_1].col_ii — QPVLI deducted elsewhere on your return (the qualifying part of the interest ded
Status: **AGREE**

Value: $0.00

### classm.carloan.1 — carloan[vin_1].col_iii — Qualified passenger vehicle loan interest less the amount in column (ii)
Status: **AGREE**

Value: $0.00

### classm.carloan.1 — carloan[vin_2].col_ii — QPVLI deducted elsewhere on your return (the qualifying part of the interest ded
Status: **AGREE**

Value: $0.00

### classm.carloan.1 — carloan[vin_2].col_iii — Qualified passenger vehicle loan interest less the amount in column (ii)
Status: **AGREE**

Value: $0.00

### case classm.carloan.2 — prompt sha256 704f7df2fc3771094030215ba5f959fd4ba17b7ca908b45d55a7cc134ad5c8a8; branches: carloan.requirements:true, carloan.vehicle:false, carloan.vehicle:true, carloan.eligible:false, carloan.eligible:true, carloan.mixed:false, carloan.nonqualifying_debt:floor, carloan.nonqualifying_debt:positive, carloan.mixed_qualifying:positive, carloan.refi_whole:true, carloan.refi_qualifying:right, carloan.refi_nested:false, carloan.allocated#1, carloan.allocated#2, carloan.mixed_interest#0, carloan.qpvli#0, carloan.qpvli#1, carloan.sc_interest#1, carloan.sc_mixed#0, carloan.sc_allocated#1, carloan.sc_allocated#2, carloan.col_ii#0, carloan.col_ii#1, carloan.col_iii:floor, carloan.col_iii:positive

### classm.carloan.2 — carloan[vin_1].col_ii — QPVLI deducted elsewhere on your return (the qualifying part of the interest ded
Status: **AGREE**

Value: $0.00

### classm.carloan.2 — carloan[vin_1].col_iii — Qualified passenger vehicle loan interest less the amount in column (ii)
Status: **AGREE**

Value: $5,073.00

### classm.carloan.2 — carloan[vin_2].col_ii — QPVLI deducted elsewhere on your return (the qualifying part of the interest ded
Status: **AGREE**

Value: $0.00

### classm.carloan.2 — carloan[vin_2].col_iii — Qualified passenger vehicle loan interest less the amount in column (ii)
Status: **AGREE**

Value: $0.00

### case classm.carloan.3 — prompt sha256 ec79dc706eab485047a25d83924189f18e4d4864193c01009ecb5765a7def24d; branches: carloan.requirements:true, carloan.vehicle:true, carloan.eligible:true, carloan.mixed:false, carloan.nonqualifying_debt:floor, carloan.mixed_qualifying:positive, carloan.refi_whole:true, carloan.refi_qualifying:left, carloan.refi_nested:false, carloan.allocated#1, carloan.mixed_interest#0, carloan.qpvli#1, carloan.sc_interest#0, carloan.sc_mixed#0, carloan.sc_allocated#1, carloan.col_ii#1, carloan.col_iii:positive

### classm.carloan.3 — carloan[vin_1].col_ii — QPVLI deducted elsewhere on your return (the qualifying part of the interest ded
Status: **DISAGREE**

Project: $551.52
Model: $551.51
Work: Refi SPVL share capped at old balance: 3,151/12,278; QPVLI part of Sch C interest = 2,149 × 3,151/12,278 = 551.51

Ruling: ambiguity; amb.2025.carloan_ratio_places (chosen: ratio rounded half-up to six places; recorded alternatives: exact ratio, three places); model value dropped from the fixture. fr-2025-24154 p. 21, proposed § 1.163-16(d)(2)(iii)(A): "payments of interest and principal are allocated to the portion of the indebtedness described in paragraph (d)(2)(i) ... and the portion ... described in paragraph (d)(2)(ii) ... on a pro rata basis", and (d)(4): "A taxpayer allocates principal and interest between the amount of the new loan that is an SPVL and the remaining portion of the indebtedness on a pro rata basis" -- no rounding of the ratio is given. The model worked 2,149 x 3,151/12,278 with the exact ratio (551.5148, $551.51), the register's second reading; the project rounds the ratio to 0.256638 (2,149 x 0.256638 = 551.5151, $551.52). The proration itself (column (ii) is the QPVLI part of the Schedule C interest, fr-2025-24154 p. 23, proposed § 1.163-16(g)(1): "Independently deductible interest is limited to interest that is QPVLI ... and that is otherwise deductible by the taxpayer as a different type of interest"; (g)(2): the QPVLI "is reduced to the extent that the taxpayer deducts that independently deductible interest as non-QPVLI") agrees, so the BUG-0175 reading is confirmed on this refinanced loan. Dropped as the non-chosen reading. [dropped]

### classm.carloan.3 — carloan[vin_1].col_iii — Qualified passenger vehicle loan interest less the amount in column (ii)
Status: **DISAGREE**

Project: $1,654.54
Model: $1,654.55
Work: QPVLI = 8,596 × 3,151/12,278 = 2,206.06; minus col (ii) 551.51 = 1,654.55

Ruling: ambiguity; amb.2025.carloan_ratio_places (chosen: ratio rounded half-up to six places; recorded alternatives: exact ratio, three places); model value dropped from the fixture. i1040gi p. 110, Line 22: "On line 22, column (iii), enter the total amount of the QPVLI paid or accrued on the loan during the taxable year minus the amount on line 22, column (ii)." The model's QPVLI $2,206.06 equals the project's (8,596 x 0.256638 = 2,206.0602; exact 2,206.0593); the one-cent difference is column (ii) under the exact ratio ($551.51 against $551.52), so $1,654.55 is the register's exact-ratio reading and the project's $1,654.54 the chosen one. Dropped as the non-chosen reading. [dropped]

## Raw responses

### classm.carloan.1

```yaml
```yaml
lines:
  - printed: "carloan[vin_1].col_ii"
    value: "0.00"
    work: "No Schedule C, and the loan fails the loan requirements, so there is no QPVLI; 0.00"
  - printed: "carloan[vin_1].col_iii"
    value: "0.00"
    work: "Loan does not meet requirements, so QPVLI = 0; interest paid also 0.00; 0.00 - 0.00 = 0.00"
  - printed: "carloan[vin_2].col_ii"
    value: "0.00"
    work: "No Schedule C; interest deducted elsewhere = 0.00"
  - printed: "carloan[vin_2].col_iii"
    value: "0.00"
    work: "Interest paid or accrued in 2025 = 0.00, so QPVLI 0.00 - col (ii) 0.00 = 0.00"
```
```

### classm.carloan.2

```yaml
lines:
  - printed: "carloan[vin_1].col_ii"
    value: "0.00"
    work: "The return has no Schedule C, so none of the $1,268.00 is deducted elsewhere; column (ii) is 0."
  - printed: "carloan[vin_1].col_iii"
    value: "5073.00"
    work: "Death obligor change keeps it an SPVL; it meets the loan requirements, is an APV and is all qualifying, so QPVLI is $5,073.00 - 0 = $5,073.00."
  - printed: "carloan[vin_2].col_ii"
    value: "0.00"
    work: "Not an applicable passenger vehicle, so there is no QPVLI and nothing is deducted elsewhere."
  - printed: "carloan[vin_2].col_iii"
    value: "0.00"
    work: "Not an APV, so it is not an SPVL; QPVLI is 0 - 0 = 0 (interest paid was also $0.00)."
```

### classm.carloan.3

```yaml
```yaml
lines:
  - printed: "carloan[vin_1].col_ii"
    value: "551.51"
    work: "Refi SPVL share capped at old balance: 3,151/12,278; QPVLI part of Sch C interest = 2,149 × 3,151/12,278 = 551.51"
  - printed: "carloan[vin_1].col_iii"
    value: "1654.55"
    work: "QPVLI = 8,596 × 3,151/12,278 = 2,206.06; minus col (ii) 551.51 = 1,654.55"
```
```
