# Class M hand-work — carloan

`Qualified passenger vehicle loan interest (Schedule 1-A, line 22) — one entry per loan` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-18 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| cases | 4 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 109, 110 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 109, 110 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| fr-2025-24154 | Federal Register Vol. 91, No. 1 (2026-01-02), proposed rules REG-113515-25 (Car Loan Interest Deduction), FR Doc. 2025-24154 | 20, 21, 22 | cited pages | eccaf8550a66615e5932726cb4e98cab002b31b9f13c5d4ffec11f0619af479e | 20, 21, 22 | 1bb1f46bab043ddeabc4cb276a0d67fa478ae7aa38088b47ecfae848df4954c9 |

## Lines

### case classm.carloan.1 — prompt sha256 4cf7fc00792d6d7efc3ddf98a38dfae169a37d159d9bf688470929af482a6545; branches: carloan.requirements:true, carloan.vehicle:true, carloan.eligible:true, carloan.mixed:true, carloan.nonqualifying_debt:positive, carloan.mixed_qualifying:positive, carloan.refi_whole:true, carloan.refi_qualifying:left, carloan.refi_nested:false, carloan.allocated#0, carloan.allocated#1, carloan.mixed_interest#1, carloan.col_iii#1

### classm.carloan.1 — carloan[vin_1].eligible — The loan and the vehicle qualify
Status: **AGREE**

Value: yes

### classm.carloan.1 — carloan[vin_1].refi_qualifying — Part of the new loan that is a specified passenger vehicle loan
Status: **AGREE**

Value: $24,033.00

### classm.carloan.1 — carloan[vin_1].refi_nested — The refinanced loan was itself only partly a qualifying loan
Status: **AGREE**

Value: no

### classm.carloan.1 — carloan[vin_1].allocated — Interest allocated pro rata to the qualifying part of the loan
Status: **AGREE**

Value: $0.00

### classm.carloan.1 — carloan[vin_1].refi_interest — Interest times the qualifying part of the new loan divided by the new loan, the 
Status: **AGREE**

Value: $0.00

### classm.carloan.1 — carloan[vin_1].col_iii — Interest for this loan, Schedule 1-A
Status: **AGREE**

Value: $0.00

### classm.carloan.1 — carloan[vin_2].eligible — The loan and the vehicle qualify
Status: **AGREE**

Value: yes

### classm.carloan.1 — carloan[vin_2].nonqualifying_debt — Nonqualifying amounts less the down payment applied first against them
Status: **AGREE**

Value: $1,518.00

### classm.carloan.1 — carloan[vin_2].mixed_qualifying — Part of the loan that is a specified passenger vehicle loan
Status: **AGREE**

Value: $52,670.00

### classm.carloan.1 — carloan[vin_2].allocated — Interest allocated pro rata to the qualifying part of the loan
Status: **AGREE**

Value: $0.00

### classm.carloan.1 — carloan[vin_2].mixed_interest — Interest times the qualifying part of the loan divided by the loan, the ratio ro
Status: **AGREE**

Value: $0.00

### classm.carloan.1 — carloan[vin_2].mixed_prorated — Interest times the qualifying part of the loan divided by the loan, the ratio ro
Status: **AGREE**

Value: $0.00

### classm.carloan.1 — carloan[vin_2].col_iii — Interest for this loan, Schedule 1-A
Status: **AGREE**

Value: $0.00

### case classm.carloan.2 — prompt sha256 2f73f2171a37d3b1a3d346a19313a4727bd64af5ec1cf0f1dff048702a28542d; branches: carloan.requirements:false, carloan.requirements:true, carloan.vehicle:true, carloan.eligible:false, carloan.eligible:true, carloan.mixed:false, carloan.allocated#2, carloan.mixed_interest#0, carloan.col_iii#0, carloan.col_iii#1

### classm.carloan.2 — carloan[vin_1].eligible — The loan and the vehicle qualify
Status: **AGREE**

Value: yes

### classm.carloan.2 — carloan[vin_1].allocated — Interest allocated pro rata to the qualifying part of the loan
Status: **AGREE**

Value: $6,066.00

### classm.carloan.2 — carloan[vin_1].mixed_interest — Interest times the qualifying part of the loan divided by the loan, the ratio ro
Status: **AGREE**

Value: $6,066.00

### classm.carloan.2 — carloan[vin_1].col_iii — Interest for this loan, Schedule 1-A
Status: **AGREE**

Value: $6,066.00

### classm.carloan.2 — carloan[vin_2].eligible — The loan and the vehicle qualify
Status: **AGREE**

Value: no

### classm.carloan.2 — carloan[vin_2].col_iii — Interest for this loan, Schedule 1-A
Status: **AGREE**

Value: $0.00

### case classm.carloan.3 — prompt sha256 a2ac6aed94cc716dc5e81f6b54c951d13f0c66a29394e3341422a857df5fe605; branches: carloan.requirements:true, carloan.vehicle:false, carloan.vehicle:true, carloan.eligible:false, carloan.eligible:true, carloan.refi_whole:true, carloan.refi_qualifying:right, carloan.refi_nested:false, carloan.allocated#1, carloan.col_iii#0, carloan.col_iii#1

### classm.carloan.3 — carloan[vin_1].eligible — The loan and the vehicle qualify
Status: **AGREE**

Value: yes

### classm.carloan.3 — carloan[vin_1].refi_qualifying — Part of the new loan that is a specified passenger vehicle loan
Status: **AGREE**

Value: $1,351.00

### classm.carloan.3 — carloan[vin_1].refi_nested — The refinanced loan was itself only partly a qualifying loan
Status: **AGREE**

Value: no

### classm.carloan.3 — carloan[vin_1].allocated — Interest allocated pro rata to the qualifying part of the loan
Status: **AGREE**

Value: $0.00

### classm.carloan.3 — carloan[vin_1].refi_interest — Interest times the qualifying part of the new loan divided by the new loan, the 
Status: **AGREE**

Value: $0.00

### classm.carloan.3 — carloan[vin_1].col_iii — Interest for this loan, Schedule 1-A
Status: **AGREE**

Value: $0.00

### classm.carloan.3 — carloan[vin_2].eligible — The loan and the vehicle qualify
Status: **AGREE**

Value: no

### classm.carloan.3 — carloan[vin_2].col_iii — Interest for this loan, Schedule 1-A
Status: **AGREE**

Value: $0.00

### case classm.carloan.4 — prompt sha256 b6558465ac07416e215065dbcaa502303115f4591fb408307a79dcd971c6c3bb; branches: carloan.requirements:true, carloan.vehicle:true, carloan.eligible:true, carloan.mixed:true, carloan.nonqualifying_debt:floor, carloan.mixed_qualifying:positive, carloan.allocated#0, carloan.mixed_interest#1, carloan.col_iii#1

### classm.carloan.4 — carloan[vin_1].eligible — The loan and the vehicle qualify
Status: **AGREE**

Value: yes

### classm.carloan.4 — carloan[vin_1].nonqualifying_debt — Nonqualifying amounts less the down payment applied first against them
Status: **AGREE**

Value: $0.00

### classm.carloan.4 — carloan[vin_1].mixed_qualifying — Part of the loan that is a specified passenger vehicle loan
Status: **AGREE**

Value: $80,000.00

### classm.carloan.4 — carloan[vin_1].allocated — Interest allocated pro rata to the qualifying part of the loan
Status: **AGREE**

Value: $0.00

### classm.carloan.4 — carloan[vin_1].mixed_interest — Interest times the qualifying part of the loan divided by the loan, the ratio ro
Status: **AGREE**

Value: $0.00

### classm.carloan.4 — carloan[vin_1].mixed_prorated — Interest times the qualifying part of the loan divided by the loan, the ratio ro
Status: **AGREE**

Value: $0.00

### classm.carloan.4 — carloan[vin_1].col_iii — Interest for this loan, Schedule 1-A
Status: **AGREE**

Value: $0.00

## Raw responses

### classm.carloan.1

```yaml
```yaml
lines:
  - printed: "carloan[vin_1].eligible"
    value: "yes"
    work: "Filer answered yes to both the loan requirements and the APV test."
  - printed: "carloan[vin_1].refi_qualifying"
    value: "24033.00"
    work: "Limited to the refinanced loan's outstanding balance: smaller of 59,969.00 or 24,033.00 = 24,033.00."
  - printed: "carloan[vin_1].refi_nested"
    value: "no"
    work: "All of the refinanced loan was a specified passenger vehicle loan, so it was not only partly qualifying."
  - printed: "carloan[vin_1].allocated"
    value: "0.00"
    work: "Pro rata allocation: 0.00 x 0.400757 = 0.00."
  - printed: "carloan[vin_1].refi_interest"
    value: "0.00"
    work: "Ratio 24,033/59,969 = 0.400757; 0.00 x 0.400757 = 0.00."
  - printed: "carloan[vin_1].col_iii"
    value: "0.00"
    work: "Qualifying interest 0.00 minus column (ii) amount 0.00 = 0.00."
  - printed: "carloan[vin_2].eligible"
    value: "yes"
    work: "Filer answered yes to both the loan requirements and the APV test."
  - printed: "carloan[vin_2].nonqualifying_debt"
    value: "1518.00"
    work: "Down payment applied first against nonqualifying amounts: 1,518.00 - 0.00 = 1,518.00."
  - printed: "carloan[vin_2].mixed_qualifying"
    value: "52670.00"
    work: "Loan minus nonqualifying debt: 54,188.00 - 1,518.00 = 52,670.00."
  - printed: "carloan[vin_2].allocated"
    value: "0.00"
    work: "Pro rata allocation: 0.00 x 0.971986 = 0.00."
  - printed: "carloan[vin_2].mixed_interest"
    value: "0.00"
    work: "Ratio 52,670/54,188 = 0.971986; 0.00 x 0.971986 = 0.00."
  - printed: "carloan[vin_2].mixed_prorated"
    value: "0.00"
    work: "Ratio 52,670/54,188 = 0.971986; 0.00 x 0.971986 = 0.00."
  - printed: "carloan[vin_2].col_iii"
    value: "0.00"
    work: "Qualifying interest 0.00 minus column (ii) amount 0.00 = 0.00."
```
```

### classm.carloan.2

```yaml
```yaml
lines:
  - printed: "carloan[vin_1].eligible"
    value: "yes"
    work: "Loan meets requirements; the obligor changed because of the previous obligor's death (Prop. Reg. 1.163-16(d)(5)(ii)); the vehicle is an APV"
  - printed: "carloan[vin_1].allocated"
    value: "6066.00"
    work: "No nonqualifying amounts were financed, so all interest of $6,066.00 goes to the qualifying part"
  - printed: "carloan[vin_1].mixed_interest"
    value: "6066.00"
    work: "6,066.00 x 1.000000 (the whole loan qualifies) = 6,066.00"
  - printed: "carloan[vin_1].col_iii"
    value: "6066.00"
    work: "QPVLI 6,066.00 minus col (ii) 0.00 deducted elsewhere = 6,066.00"
  - printed: "carloan[vin_2].eligible"
    value: "no"
    work: "The loan does not meet the loan requirements"
  - printed: "carloan[vin_2].col_iii"
    value: "0.00"
    work: "Not eligible, so no QPVLI; enter 0"
```
```

### classm.carloan.3

```yaml
lines:
  - printed: "carloan[vin_1].eligible"
    value: "yes"
    work: "Loan meets the loan requirements = yes and the vehicle is an APV = yes, so it qualifies"
  - printed: "carloan[vin_1].refi_qualifying"
    value: "1351.00"
    work: "Reg. 1.163-16(d)(4): SPVL part limited to outstanding balance of refinanced loan; smaller of 1,351.00 new loan and 32,081.00 = 1,351.00"
  - printed: "carloan[vin_1].refi_nested"
    value: "no"
    work: "Filer says all of the refinanced loan was an SPVL, so it was not only partly qualifying"
  - printed: "carloan[vin_1].allocated"
    value: "0.00"
    work: "Pro rata allocation: 0.00 interest x 1.000000 = 0.00"
  - printed: "carloan[vin_1].refi_interest"
    value: "0.00"
    work: "0.00 x (1,351.00 / 1,351.00 = 1.000000) = 0.00"
  - printed: "carloan[vin_1].col_iii"
    value: "0.00"
    work: "Col (iii) = QPVLI 0.00 minus col (ii) 0.00 = 0.00"
  - printed: "carloan[vin_2].eligible"
    value: "no"
    work: "Vehicle is not an applicable passenger vehicle, so the interest is not QPVLI"
  - printed: "carloan[vin_2].col_iii"
    value: "0.00"
    work: "Does not qualify, so no QPVLI: 0.00"
```

### classm.carloan.4

```yaml
lines:
  - printed: "carloan[vin_1].eligible"
    value: "yes"
    work: "The loan is original, meets the loan requirements, and the vehicle is an APV, so it qualifies"
  - printed: "carloan[vin_1].nonqualifying_debt"
    value: "0.00"
    work: "9,902.00 - 10,000.00 down payment applied first (Reg 1.163-16(d)(2)(iii)(B)) = -98.00; zero or less, enter -0-"
  - printed: "carloan[vin_1].mixed_qualifying"
    value: "80000.00"
    work: "80,000.00 loan - 0.00 nonqualifying debt = 80,000.00 SPVL portion"
  - printed: "carloan[vin_1].allocated"
    value: "0.00"
    work: "Pro rata: 0.00 interest x 80,000/80,000 (1.000000) = 0.00"
  - printed: "carloan[vin_1].mixed_interest"
    value: "0.00"
    work: "0.00 x round(80,000/80,000, 6) = 0.00 x 1.000000 = 0.00"
  - printed: "carloan[vin_1].mixed_prorated"
    value: "0.00"
    work: "0.00 x 1.000000 = 0.00"
  - printed: "carloan[vin_1].col_iii"
    value: "0.00"
    work: "QPVLI 0.00 - column (ii) 0.00 deducted elsewhere = 0.00"
```
