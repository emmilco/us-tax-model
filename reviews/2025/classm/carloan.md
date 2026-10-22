# Class M hand-work — carloan

`Qualified passenger vehicle loan interest (Schedule 1-A, line 22) — one entry per loan` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-21 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| subject sha256 | cc26c87c99d39e951ff534294ae07ca18292256f6f40734aa0d469c4c89d71b9 |
| cases | 4 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 109, 110 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 109, 110 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| fr-2025-24154 | Federal Register Vol. 91, No. 1 (2026-01-02), proposed rules REG-113515-25 (Car Loan Interest Deduction), FR Doc. 2025-24154 | 20, 21, 22 | cited pages | eccaf8550a66615e5932726cb4e98cab002b31b9f13c5d4ffec11f0619af479e | 20, 21, 22 | 1bb1f46bab043ddeabc4cb276a0d67fa478ae7aa38088b47ecfae848df4954c9 |
| i1040sc | 2025 | 6 | pages named by another document's citation | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 6 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |

## Lines

### case classm.carloan.1 — prompt sha256 9a843b5bfeb12b8c188462acc95c24ec8d67926a564609df8b48842cd6056dd4; branches: carloan.requirements:true, carloan.vehicle:false, carloan.vehicle:true, carloan.eligible:false, carloan.eligible:true, carloan.mixed:false, carloan.mixed:true, carloan.nonqualifying_debt:floor, carloan.mixed_qualifying:positive, carloan.refi_whole:true, carloan.refi_qualifying:left, carloan.refi_qualifying:right, carloan.refi_nested:false, carloan.allocated#0, carloan.mixed_interest#0, carloan.mixed_interest#1, carloan.qpvli#0, carloan.qpvli#1, carloan.col_ii#0, carloan.col_iii:floor, carloan.col_iii:positive

### classm.carloan.1 — carloan[vin_1].eligible — The loan and the vehicle qualify
Status: **AGREE**

Value: yes

### classm.carloan.1 — carloan[vin_1].nonqualifying_debt — Nonqualifying amounts less the down payment applied first against them
Status: **AGREE**

Value: $0.00

### classm.carloan.1 — carloan[vin_1].mixed_qualifying — Part of the loan that is a specified passenger vehicle loan
Status: **DISAGREE**

Project: $15,244.00
Model: $0.00
Work: Not a mixed loan, so no mixed allocation is needed

Ruling: helper of a branch this entry does not take; project retained; model value dropped from the fixture. The loan financed nothing that does not qualify (carloan.mixed false), so carloan.mixed_interest is the whole interest and carloan.mixed_prorated, with the qualifying part it divides, is read by no line this entry reaches (proposed § 1.163-16(d)(2)(iii)(A) allocates only where part of the loan is not an SPVL); the project figures it whatever the branch. Its value is 15,244.00 less the nonqualifying debt 0.00 (4,723.00 less the 9,729.00 down payment, not below zero) = 15,244.00, the whole loan. allocated, qpvli and column (iii) agree (424.00, 318.00). Dropped from the fixture as not evidence. [dropped]

### classm.carloan.1 — carloan[vin_1].refi_qualifying — Part of the new loan that is a specified passenger vehicle loan
Status: **DISAGREE**

Project: $15,244.00
Model: $0.00
Work: Original loan, not a refinancing

Ruling: helper of a branch this entry does not take; project retained; model value dropped from the fixture. The loan is an original loan, so carloan.allocated reads carloan.mixed_interest and the refinancing helpers (proposed § 1.163-16(d)(4)) are read by no line this entry reaches; the project figures them whatever the branch. Its value is the smaller of the refinanced balance 37,593.00 and the loan 15,244.00 = 15,244.00. allocated and qpvli agree (424.00). Dropped from the fixture as not evidence. [dropped]

### classm.carloan.1 — carloan[vin_1].refi_nested — The refinanced loan was itself only partly a qualifying loan
Status: **AGREE**

Value: no

### classm.carloan.1 — carloan[vin_1].allocated — Interest allocated pro rata to the qualifying part of the loan
Status: **AGREE**

Value: $424.00

### classm.carloan.1 — carloan[vin_1].refi_interest — Interest times the qualifying part of the new loan divided by the new loan, the 
Status: **DISAGREE**

Project: $424.00
Model: $0.00
Work: Not a refinancing

Ruling: helper of a branch this entry does not take; project retained; model value dropped from the fixture. The loan is an original loan, so carloan.allocated reads carloan.mixed_interest and the refinancing helpers (proposed § 1.163-16(d)(4)) are read by no line this entry reaches; the project figures them whatever the branch. Its value is 424.00 x 15,244.00/15,244.00 (1.000000) = 424.00. allocated and qpvli agree (424.00). Dropped from the fixture as not evidence. [dropped]

### classm.carloan.1 — carloan[vin_1].mixed_interest — Interest times the qualifying part of the loan divided by the loan, the ratio ro
Status: **DISAGREE**

Project: $424.00
Model: $0.00
Work: Not a mixed loan

Ruling: model error; project retained. carloan.mixed_interest is the line carloan.allocated reads for an original loan; with carloan.mixed false it is the whole interest, 424.00 (the qualifying part is the whole loan, ratio 1.000000; proposed § 1.163-16(d)(2)(iii)(A)). The model wrote 0.00 for 'not a mixed loan' while entering 424.00 on allocated, which copies this line. Dropped from the fixture as not evidence. [dropped]

### classm.carloan.1 — carloan[vin_1].mixed_prorated — Interest times the qualifying part of the loan divided by the loan, the ratio ro
Status: **DISAGREE**

Project: $424.00
Model: $0.00
Work: Not a mixed loan

Ruling: helper of a branch this entry does not take; project retained; model value dropped from the fixture. The loan financed nothing that does not qualify (carloan.mixed false), so carloan.mixed_interest is the whole interest and carloan.mixed_prorated, with the qualifying part it divides, is read by no line this entry reaches (proposed § 1.163-16(d)(2)(iii)(A) allocates only where part of the loan is not an SPVL); the project figures it whatever the branch. Its value is 424.00 x 15,244.00/15,244.00 (1.000000) = 424.00. allocated and qpvli agree (424.00). Dropped from the fixture as not evidence. [dropped]

### classm.carloan.1 — carloan[vin_1].qpvli — Interest for this loan, Schedule 1-A
Status: **AGREE**

Value: $424.00

### classm.carloan.1 — carloan[vin_1].col_ii — Interest deducted on Schedule C (zero without a Schedule C)
Status: **AGREE**

Value: $106.00

### classm.carloan.1 — carloan[vin_1].col_iii — Qualified passenger vehicle loan interest less the amount in column (ii)
Status: **AGREE**

Value: $318.00

### classm.carloan.1 — carloan[vin_2].eligible — The loan and the vehicle qualify
Status: **AGREE**

Value: no

### classm.carloan.1 — carloan[vin_2].nonqualifying_debt — Nonqualifying amounts less the down payment applied first against them
Status: **AGREE**

Value: $0.00

### classm.carloan.1 — carloan[vin_2].mixed_qualifying — Part of the loan that is a specified passenger vehicle loan
Status: **DISAGREE**

Project: $75,615.00
Model: $0.00
Work: Not an APV, so no part of the loan is an SPVL

Ruling: representation; project retained; model value dropped from the fixture. The vehicle is not an applicable passenger vehicle, so the entry is not eligible and carloan.qpvli is zero by its eligibility choice (i1040gi p. 109); the project figures the allocation helpers whatever the eligibility, the model zeroed them. Its value is 75,615.00 less the nonqualifying debt 0.00 (7,445.00 less the 9,382.00 down payment, not below zero, proposed § 1.163-16(d)(2)(iii)(B)) = 75,615.00. The interest is 0.00 and every interest line and qpvli agree. Dropped from the fixture as not evidence. [dropped]

### classm.carloan.1 — carloan[vin_2].refi_qualifying — Part of the new loan that is a specified passenger vehicle loan
Status: **AGREE**

Value: $0.00

### classm.carloan.1 — carloan[vin_2].refi_nested — The refinanced loan was itself only partly a qualifying loan
Status: **AGREE**

Value: no

### classm.carloan.1 — carloan[vin_2].allocated — Interest allocated pro rata to the qualifying part of the loan
Status: **AGREE**

Value: $0.00

### classm.carloan.1 — carloan[vin_2].refi_interest — Interest times the qualifying part of the new loan divided by the new loan, the 
Status: **AGREE**

Value: $0.00

### classm.carloan.1 — carloan[vin_2].mixed_interest — Interest times the qualifying part of the loan divided by the loan, the ratio ro
Status: **AGREE**

Value: $0.00

### classm.carloan.1 — carloan[vin_2].mixed_prorated — Interest times the qualifying part of the loan divided by the loan, the ratio ro
Status: **AGREE**

Value: $0.00

### classm.carloan.1 — carloan[vin_2].qpvli — Interest for this loan, Schedule 1-A
Status: **AGREE**

Value: $0.00

### classm.carloan.1 — carloan[vin_2].col_ii — Interest deducted on Schedule C (zero without a Schedule C)
Status: **AGREE**

Value: $0.00

### classm.carloan.1 — carloan[vin_2].col_iii — Qualified passenger vehicle loan interest less the amount in column (ii)
Status: **AGREE**

Value: $0.00

### case classm.carloan.2 — prompt sha256 8ac3a46d43cdf94a201c4bd97c6d33f20e60257d68b06b86ba80b8684e24e1e1; branches: carloan.requirements:true, carloan.vehicle:true, carloan.eligible:true, carloan.mixed:false, carloan.nonqualifying_debt:positive, carloan.mixed_qualifying:positive, carloan.refi_whole:true, carloan.refi_qualifying:left, carloan.refi_nested:false, carloan.allocated#1, carloan.allocated#2, carloan.mixed_interest#0, carloan.qpvli#1, carloan.col_ii#1, carloan.col_iii:floor

### classm.carloan.2 — carloan[vin_1].eligible — The loan and the vehicle qualify
Status: **AGREE**

Value: yes

### classm.carloan.2 — carloan[vin_1].nonqualifying_debt — Nonqualifying amounts less the down payment applied first against them
Status: **DISAGREE**

Project: $6,458.00
Model: $0.00
Work: Loan did not finance nonqualifying amounts, so the down-payment allocation in 1.163-16(d)(2)(iii)(B) does not apply

Ruling: helper of a branch this entry does not take; project retained; model value dropped from the fixture. The loan is a refinancing, so carloan.allocated reads carloan.refi_interest, and the loan financed nothing that does not qualify (carloan.mixed false); the mixed-loan helpers are read by no line this entry reaches. The generated return answers mixed false yet gives a nonqualifying amount; the project figures the helper from the inputs as given, the model zeroed it. Its value is 8,969.00 less the 2,511.00 down payment = 6,458.00 (proposed § 1.163-16(d)(2)(iii)(B)). The interest is 0.00; allocated and qpvli agree (0.00). Dropped from the fixture as not evidence. [dropped]

### classm.carloan.2 — carloan[vin_1].mixed_qualifying — Part of the loan that is a specified passenger vehicle loan
Status: **DISAGREE**

Project: $31,177.00
Model: $0.00
Work: Not a mixed loan, so there is no allocation

Ruling: helper of a branch this entry does not take; project retained; model value dropped from the fixture. The loan is a refinancing, so carloan.allocated reads carloan.refi_interest, and the loan financed nothing that does not qualify (carloan.mixed false); the mixed-loan helpers are read by no line this entry reaches. The generated return answers mixed false yet gives a nonqualifying amount; the project figures the helper from the inputs as given, the model zeroed it. Its value is 37,635.00 less 6,458.00 = 31,177.00. The interest is 0.00; allocated and qpvli agree (0.00). Dropped from the fixture as not evidence. [dropped]

### classm.carloan.2 — carloan[vin_1].refi_qualifying — Part of the new loan that is a specified passenger vehicle loan
Status: **AGREE**

Value: $0.00

### classm.carloan.2 — carloan[vin_1].refi_nested — The refinanced loan was itself only partly a qualifying loan
Status: **AGREE**

Value: no

### classm.carloan.2 — carloan[vin_1].allocated — Interest allocated pro rata to the qualifying part of the loan
Status: **AGREE**

Value: $0.00

### classm.carloan.2 — carloan[vin_1].refi_interest — Interest times the qualifying part of the new loan divided by the new loan, the 
Status: **AGREE**

Value: $0.00

### classm.carloan.2 — carloan[vin_1].mixed_interest — Interest times the qualifying part of the loan divided by the loan, the ratio ro
Status: **AGREE**

Value: $0.00

### classm.carloan.2 — carloan[vin_1].mixed_prorated — Interest times the qualifying part of the loan divided by the loan, the ratio ro
Status: **AGREE**

Value: $0.00

### classm.carloan.2 — carloan[vin_1].qpvli — Interest for this loan, Schedule 1-A
Status: **AGREE**

Value: $0.00

### classm.carloan.2 — carloan[vin_1].col_ii — Interest deducted on Schedule C (zero without a Schedule C)
Status: **AGREE**

Value: $0.00

### classm.carloan.2 — carloan[vin_1].col_iii — Qualified passenger vehicle loan interest less the amount in column (ii)
Status: **AGREE**

Value: $0.00

### classm.carloan.2 — carloan[vin_2].eligible — The loan and the vehicle qualify
Status: **AGREE**

Value: yes

### classm.carloan.2 — carloan[vin_2].nonqualifying_debt — Nonqualifying amounts less the down payment applied first against them
Status: **DISAGREE**

Project: $2,987.00
Model: $0.00
Work: Loan did not finance nonqualifying amounts, so the down-payment allocation does not apply

Ruling: helper of a branch this entry does not take; project retained; model value dropped from the fixture. The loan passed to the filer by a borrower's death, so carloan.allocated reads carloan.mixed_interest, which for a loan that financed nothing that does not qualify (carloan.mixed false) is the whole interest; the mixed-loan helpers are read by no line this entry reaches. The generated return answers mixed false yet gives a nonqualifying amount; the project figures the helper from the inputs as given, the model zeroed it. Its value is 7,376.00 less the 4,389.00 down payment = 2,987.00 (proposed § 1.163-16(d)(2)(iii)(B)). The interest is 0.00; allocated and qpvli agree (0.00). Dropped from the fixture as not evidence. [dropped]

### classm.carloan.2 — carloan[vin_2].mixed_qualifying — Part of the loan that is a specified passenger vehicle loan
Status: **DISAGREE**

Project: $75,391.00
Model: $0.00
Work: Not a mixed loan, so there is no allocation

Ruling: helper of a branch this entry does not take; project retained; model value dropped from the fixture. The loan passed to the filer by a borrower's death, so carloan.allocated reads carloan.mixed_interest, which for a loan that financed nothing that does not qualify (carloan.mixed false) is the whole interest; the mixed-loan helpers are read by no line this entry reaches. The generated return answers mixed false yet gives a nonqualifying amount; the project figures the helper from the inputs as given, the model zeroed it. Its value is 78,378.00 less 2,987.00 = 75,391.00. The interest is 0.00; allocated and qpvli agree (0.00). Dropped from the fixture as not evidence. [dropped]

### classm.carloan.2 — carloan[vin_2].refi_qualifying — Part of the new loan that is a specified passenger vehicle loan
Status: **AGREE**

Value: $0.00

### classm.carloan.2 — carloan[vin_2].refi_nested — The refinanced loan was itself only partly a qualifying loan
Status: **AGREE**

Value: no

### classm.carloan.2 — carloan[vin_2].allocated — Interest allocated pro rata to the qualifying part of the loan
Status: **AGREE**

Value: $0.00

### classm.carloan.2 — carloan[vin_2].refi_interest — Interest times the qualifying part of the new loan divided by the new loan, the 
Status: **AGREE**

Value: $0.00

### classm.carloan.2 — carloan[vin_2].mixed_interest — Interest times the qualifying part of the loan divided by the loan, the ratio ro
Status: **AGREE**

Value: $0.00

### classm.carloan.2 — carloan[vin_2].mixed_prorated — Interest times the qualifying part of the loan divided by the loan, the ratio ro
Status: **AGREE**

Value: $0.00

### classm.carloan.2 — carloan[vin_2].qpvli — Interest for this loan, Schedule 1-A
Status: **AGREE**

Value: $0.00

### classm.carloan.2 — carloan[vin_2].col_ii — Interest deducted on Schedule C (zero without a Schedule C)
Status: **AGREE**

Value: $0.00

### classm.carloan.2 — carloan[vin_2].col_iii — Qualified passenger vehicle loan interest less the amount in column (ii)
Status: **AGREE**

Value: $0.00

### case classm.carloan.3 — prompt sha256 634ca97352b2fecda72c58cb6bad76e1a9121fab1f6e51059c1deeb0777d6d38; branches: carloan.requirements:true, carloan.vehicle:true, carloan.eligible:true, carloan.mixed:true, carloan.nonqualifying_debt:positive, carloan.mixed_qualifying:floor, carloan.refi_whole:true, carloan.refi_qualifying:right, carloan.refi_nested:false, carloan.allocated#0, carloan.mixed_interest#1, carloan.qpvli#1, carloan.col_ii#1, carloan.col_iii:floor

### classm.carloan.3 — carloan[vin_1].eligible — The loan and the vehicle qualify
Status: **AGREE**

Value: yes

### classm.carloan.3 — carloan[vin_1].nonqualifying_debt — Nonqualifying amounts less the down payment applied first against them
Status: **AGREE**

Value: $9,208.00

### classm.carloan.3 — carloan[vin_1].mixed_qualifying — Part of the loan that is a specified passenger vehicle loan
Status: **AGREE**

Value: $0.00

### classm.carloan.3 — carloan[vin_1].refi_qualifying — Part of the new loan that is a specified passenger vehicle loan
Status: **DISAGREE**

Project: $4,744.00
Model: $0.00
Work: Loan is original, not a refinancing; the refinancing limit in (d)(4) does not apply

Ruling: helper of a branch this entry does not take; project retained; model value dropped from the fixture. The loan is an original loan, so carloan.allocated reads carloan.mixed_interest (here the mixed-loan proration: 12,004.00 x 0.00/4,744.00 = 0.00, the 9,208.00 of nonqualifying amounts exceeding the 4,744.00 loan) and the refinancing helpers (proposed § 1.163-16(d)(4)) are read by no line this entry reaches; the project figures them whatever the branch. Its value is the smaller of the refinanced balance 40,387.00 and the loan 4,744.00 = 4,744.00. allocated and qpvli agree (0.00). Dropped from the fixture as not evidence. [dropped]

### classm.carloan.3 — carloan[vin_1].refi_nested — The refinanced loan was itself only partly a qualifying loan
Status: **AGREE**

Value: no

### classm.carloan.3 — carloan[vin_1].allocated — Interest allocated pro rata to the qualifying part of the loan
Status: **AGREE**

Value: $0.00

### classm.carloan.3 — carloan[vin_1].refi_interest — Interest times the qualifying part of the new loan divided by the new loan, the 
Status: **DISAGREE**

Project: $12,004.00
Model: $0.00
Work: Not a refinanced loan; no refinance allocation

Ruling: helper of a branch this entry does not take; project retained; model value dropped from the fixture. The loan is an original loan, so carloan.allocated reads carloan.mixed_interest (here the mixed-loan proration: 12,004.00 x 0.00/4,744.00 = 0.00, the 9,208.00 of nonqualifying amounts exceeding the 4,744.00 loan) and the refinancing helpers (proposed § 1.163-16(d)(4)) are read by no line this entry reaches; the project figures them whatever the branch. Its value is 12,004.00 x 4,744.00/4,744.00 (1.000000) = 12,004.00. allocated and qpvli agree (0.00). Dropped from the fixture as not evidence. [dropped]

### classm.carloan.3 — carloan[vin_1].mixed_interest — Interest times the qualifying part of the loan divided by the loan, the ratio ro
Status: **AGREE**

Value: $0.00

### classm.carloan.3 — carloan[vin_1].mixed_prorated — Interest times the qualifying part of the loan divided by the loan, the ratio ro
Status: **AGREE**

Value: $0.00

### classm.carloan.3 — carloan[vin_1].qpvli — Interest for this loan, Schedule 1-A
Status: **AGREE**

Value: $0.00

### classm.carloan.3 — carloan[vin_1].col_ii — Interest deducted on Schedule C (zero without a Schedule C)
Status: **AGREE**

Value: $0.00

### classm.carloan.3 — carloan[vin_1].col_iii — Qualified passenger vehicle loan interest less the amount in column (ii)
Status: **AGREE**

Value: $0.00

### case classm.carloan.4 — prompt sha256 c67a1aecfea1732bdebccf755fa61eabc2a78c93b62af29b7bd7a20c57e1c758; branches: carloan.requirements:false, carloan.requirements:true, carloan.vehicle:true, carloan.eligible:false, carloan.eligible:true, carloan.mixed:false, carloan.nonqualifying_debt:floor, carloan.mixed_qualifying:positive, carloan.refi_whole:true, carloan.refi_qualifying:left, carloan.refi_qualifying:right, carloan.refi_nested:false, carloan.allocated#0, carloan.allocated#1, carloan.mixed_interest#0, carloan.qpvli#0, carloan.qpvli#1, carloan.col_ii#1, carloan.col_iii:floor, carloan.col_iii:positive

### classm.carloan.4 — carloan[vin_1].eligible — The loan and the vehicle qualify
Status: **AGREE**

Value: no

### classm.carloan.4 — carloan[vin_1].nonqualifying_debt — Nonqualifying amounts less the down payment applied first against them
Status: **AGREE**

Value: $0.00

### classm.carloan.4 — carloan[vin_1].mixed_qualifying — Part of the loan that is a specified passenger vehicle loan
Status: **DISAGREE**

Project: $69,155.00
Model: $0.00
Work: Loan not eligible

Ruling: helper of a branch this entry does not take; project retained; model value dropped from the fixture. The loan is a refinancing, so carloan.allocated reads carloan.refi_interest and the mixed-loan helpers are read by no line this entry reaches; the loan also fails the loan requirements, so qpvli is zero by its eligibility choice. The project figures the helper whatever the branch: 69,155.00 less nonqualifying debt 0.00 = 69,155.00. The interest is 0.00; allocated and qpvli agree (0.00). Dropped from the fixture as not evidence. [dropped]

### classm.carloan.4 — carloan[vin_1].refi_qualifying — Part of the new loan that is a specified passenger vehicle loan
Status: **DISAGREE**

Project: $44,545.00
Model: $0.00
Work: Loan not eligible; the refinance SPVL limit is not reached

Ruling: representation; project retained; model value dropped from the fixture. The loan fails the loan requirements (carloan.requirements false), so carloan.qpvli is zero by its eligibility choice (i1040gi p. 109); the project figures the refinancing helpers whatever the eligibility, the model zeroed them. Its value is the smaller of the refinanced balance 44,545.00 and the loan 69,155.00 = 44,545.00 (proposed § 1.163-16(d)(4)). The interest is 0.00; refi_interest, allocated and qpvli agree (0.00). Dropped from the fixture as not evidence. [dropped]

### classm.carloan.4 — carloan[vin_1].refi_nested — The refinanced loan was itself only partly a qualifying loan
Status: **AGREE**

Value: no

### classm.carloan.4 — carloan[vin_1].allocated — Interest allocated pro rata to the qualifying part of the loan
Status: **AGREE**

Value: $0.00

### classm.carloan.4 — carloan[vin_1].refi_interest — Interest times the qualifying part of the new loan divided by the new loan, the 
Status: **AGREE**

Value: $0.00

### classm.carloan.4 — carloan[vin_1].mixed_interest — Interest times the qualifying part of the loan divided by the loan, the ratio ro
Status: **AGREE**

Value: $0.00

### classm.carloan.4 — carloan[vin_1].mixed_prorated — Interest times the qualifying part of the loan divided by the loan, the ratio ro
Status: **AGREE**

Value: $0.00

### classm.carloan.4 — carloan[vin_1].qpvli — Interest for this loan, Schedule 1-A
Status: **AGREE**

Value: $0.00

### classm.carloan.4 — carloan[vin_1].col_ii — Interest deducted on Schedule C (zero without a Schedule C)
Status: **AGREE**

Value: $0.00

### classm.carloan.4 — carloan[vin_1].col_iii — Qualified passenger vehicle loan interest less the amount in column (ii)
Status: **AGREE**

Value: $0.00

### classm.carloan.4 — carloan[vin_2].eligible — The loan and the vehicle qualify
Status: **AGREE**

Value: yes

### classm.carloan.4 — carloan[vin_2].nonqualifying_debt — Nonqualifying amounts less the down payment applied first against them
Status: **AGREE**

Value: $0.00

### classm.carloan.4 — carloan[vin_2].mixed_qualifying — Part of the loan that is a specified passenger vehicle loan
Status: **DISAGREE**

Project: $29,421.00
Model: $0.00
Work: Not a mixed loan, so the mixed allocation does not apply

Ruling: helper of a branch this entry does not take; project retained; model value dropped from the fixture. The loan financed nothing that does not qualify (carloan.mixed false), so carloan.mixed_interest is the whole interest and carloan.mixed_prorated, with the qualifying part it divides, is read by no line this entry reaches (proposed § 1.163-16(d)(2)(iii)(A) allocates only where part of the loan is not an SPVL); the project figures it whatever the branch. Its value is 29,421.00 less the nonqualifying debt 0.00 (2,066.00 less the 5,037.00 down payment, not below zero) = 29,421.00, the whole loan. allocated, qpvli and column (iii) agree (4,413.00). Dropped from the fixture as not evidence. [dropped]

### classm.carloan.4 — carloan[vin_2].refi_qualifying — Part of the new loan that is a specified passenger vehicle loan
Status: **DISAGREE**

Project: $29,421.00
Model: $0.00
Work: Original loan, not a refinancing

Ruling: helper of a branch this entry does not take; project retained; model value dropped from the fixture. The loan is an original loan, so carloan.allocated reads carloan.mixed_interest and the refinancing helpers (proposed § 1.163-16(d)(4)) are read by no line this entry reaches; the project figures them whatever the branch. Its value is the smaller of the refinanced balance 33,968.00 and the loan 29,421.00 = 29,421.00. allocated and qpvli agree (4,413.00). Dropped from the fixture as not evidence. [dropped]

### classm.carloan.4 — carloan[vin_2].refi_nested — The refinanced loan was itself only partly a qualifying loan
Status: **AGREE**

Value: no

### classm.carloan.4 — carloan[vin_2].allocated — Interest allocated pro rata to the qualifying part of the loan
Status: **AGREE**

Value: $4,413.00

### classm.carloan.4 — carloan[vin_2].refi_interest — Interest times the qualifying part of the new loan divided by the new loan, the 
Status: **DISAGREE**

Project: $4,413.00
Model: $0.00
Work: Original loan, not a refinancing

Ruling: helper of a branch this entry does not take; project retained; model value dropped from the fixture. The loan is an original loan, so carloan.allocated reads carloan.mixed_interest and the refinancing helpers (proposed § 1.163-16(d)(4)) are read by no line this entry reaches; the project figures them whatever the branch. Its value is 4,413.00 x 29,421.00/29,421.00 (1.000000) = 4,413.00. allocated and qpvli agree (4,413.00). Dropped from the fixture as not evidence. [dropped]

### classm.carloan.4 — carloan[vin_2].mixed_interest — Interest times the qualifying part of the loan divided by the loan, the ratio ro
Status: **DISAGREE**

Project: $4,413.00
Model: $0.00
Work: Not a mixed loan

Ruling: model error; project retained. carloan.mixed_interest is the line carloan.allocated reads for an original loan; with carloan.mixed false it is the whole interest, 4,413.00 (the qualifying part is the whole loan, ratio 1.000000; proposed § 1.163-16(d)(2)(iii)(A)). The model wrote 0.00 for 'not a mixed loan' while entering 4,413.00 on allocated, which copies this line. Dropped from the fixture as not evidence. [dropped]

### classm.carloan.4 — carloan[vin_2].mixed_prorated — Interest times the qualifying part of the loan divided by the loan, the ratio ro
Status: **DISAGREE**

Project: $4,413.00
Model: $0.00
Work: Not a mixed loan

Ruling: helper of a branch this entry does not take; project retained; model value dropped from the fixture. The loan financed nothing that does not qualify (carloan.mixed false), so carloan.mixed_interest is the whole interest and carloan.mixed_prorated, with the qualifying part it divides, is read by no line this entry reaches (proposed § 1.163-16(d)(2)(iii)(A) allocates only where part of the loan is not an SPVL); the project figures it whatever the branch. Its value is 4,413.00 x 29,421.00/29,421.00 (1.000000) = 4,413.00. allocated and qpvli agree (4,413.00). Dropped from the fixture as not evidence. [dropped]

### classm.carloan.4 — carloan[vin_2].qpvli — Interest for this loan, Schedule 1-A
Status: **AGREE**

Value: $4,413.00

### classm.carloan.4 — carloan[vin_2].col_ii — Interest deducted on Schedule C (zero without a Schedule C)
Status: **AGREE**

Value: $0.00

### classm.carloan.4 — carloan[vin_2].col_iii — Qualified passenger vehicle loan interest less the amount in column (ii)
Status: **AGREE**

Value: $4,413.00

## Raw responses

### classm.carloan.1

```yaml
```yaml
lines:
  - printed: "carloan[vin_1].eligible"
    value: "yes"
    work: "Original loan that meets the loan requirements; the vehicle is an APV"
  - printed: "carloan[vin_1].nonqualifying_debt"
    value: "0.00"
    work: "Loan finances no nonqualifying amounts; also 4,723 - 9,729 down payment < 0, so -0-"
  - printed: "carloan[vin_1].mixed_qualifying"
    value: "0.00"
    work: "Not a mixed loan, so no mixed allocation is needed"
  - printed: "carloan[vin_1].refi_qualifying"
    value: "0.00"
    work: "Original loan, not a refinancing"
  - printed: "carloan[vin_1].refi_nested"
    value: "no"
    work: "Not a refinancing"
  - printed: "carloan[vin_1].allocated"
    value: "424.00"
    work: "Entire loan is an SPVL; interest 424.00 is allocated in full"
  - printed: "carloan[vin_1].refi_interest"
    value: "0.00"
    work: "Not a refinancing"
  - printed: "carloan[vin_1].mixed_interest"
    value: "0.00"
    work: "Not a mixed loan"
  - printed: "carloan[vin_1].mixed_prorated"
    value: "0.00"
    work: "Not a mixed loan"
  - printed: "carloan[vin_1].qpvli"
    value: "424.00"
    work: "QPVLI = interest paid or accrued on the SPVL, 424.00"
  - printed: "carloan[vin_1].col_ii"
    value: "106.00"
    work: "Return has Schedule C; 106.00 deducted there"
  - printed: "carloan[vin_1].col_iii"
    value: "318.00"
    work: "424.00 - 106.00"
  - printed: "carloan[vin_2].eligible"
    value: "no"
    work: "Vehicle is not an applicable passenger vehicle"
  - printed: "carloan[vin_2].nonqualifying_debt"
    value: "0.00"
    work: "7,445 - 9,382 down payment applied first < 0, so -0-"
  - printed: "carloan[vin_2].mixed_qualifying"
    value: "0.00"
    work: "Not an APV, so no part of the loan is an SPVL"
  - printed: "carloan[vin_2].refi_qualifying"
    value: "0.00"
    work: "Original loan, not a refinancing"
  - printed: "carloan[vin_2].refi_nested"
    value: "no"
    work: "Not a refinancing"
  - printed: "carloan[vin_2].allocated"
    value: "0.00"
    work: "Ineligible; interest is 0.00"
  - printed: "carloan[vin_2].refi_interest"
    value: "0.00"
    work: "Not a refinancing"
  - printed: "carloan[vin_2].mixed_interest"
    value: "0.00"
    work: "Interest 0.00 times any ratio = 0.00; also ineligible"
  - printed: "carloan[vin_2].mixed_prorated"
    value: "0.00"
    work: "Interest 0.00 times any ratio = 0.00; also ineligible"
  - printed: "carloan[vin_2].qpvli"
    value: "0.00"
    work: "Not an APV, so the interest is not QPVLI"
  - printed: "carloan[vin_2].col_ii"
    value: "0.00"
    work: "No interest on this loan deducted on Schedule C"
  - printed: "carloan[vin_2].col_iii"
    value: "0.00"
    work: "0.00 - 0.00"
```
```

### classm.carloan.2

```yaml
```yaml
lines:
  - printed: "carloan[vin_1].eligible"
    value: "yes"
    work: "Loan meets requirements 1-5 (yes) and vehicle is an APV (yes); a refinancing keeps the first lien on the APV"
  - printed: "carloan[vin_1].nonqualifying_debt"
    value: "0.00"
    work: "Loan did not finance nonqualifying amounts, so the down-payment allocation in 1.163-16(d)(2)(iii)(B) does not apply"
  - printed: "carloan[vin_1].mixed_qualifying"
    value: "0.00"
    work: "Not a mixed loan, so there is no allocation"
  - printed: "carloan[vin_1].refi_qualifying"
    value: "0.00"
    work: "SPVL limited to the refinanced loan's outstanding balance at refinancing: smaller of 37,635.00 and 0.00 = 0.00 (1.163-16(d)(4))"
  - printed: "carloan[vin_1].refi_nested"
    value: "no"
    work: "All of the refinanced loan was an SPVL"
  - printed: "carloan[vin_1].allocated"
    value: "0.00"
    work: "Interest paid or accrued is 0.00, so the pro rata allocation is 0.00"
  - printed: "carloan[vin_1].refi_interest"
    value: "0.00"
    work: "0.00 x (0.00 / 37,635.00 = 0.000000) = 0.00"
  - printed: "carloan[vin_1].mixed_interest"
    value: "0.00"
    work: "Not a mixed loan, and interest is 0.00"
  - printed: "carloan[vin_1].mixed_prorated"
    value: "0.00"
    work: "Not a mixed loan, and interest is 0.00"
  - printed: "carloan[vin_1].qpvli"
    value: "0.00"
    work: "Interest paid or accrued in 2025 is 0.00"
  - printed: "carloan[vin_1].col_ii"
    value: "0.00"
    work: "The return has no Schedule C"
  - printed: "carloan[vin_1].col_iii"
    value: "0.00"
    work: "0.00 - 0.00 = 0.00"
  - printed: "carloan[vin_2].eligible"
    value: "yes"
    work: "Change in obligor by reason of death (1.163-16(d)(5)(ii)); the loan met the requirements and the vehicle is an APV"
  - printed: "carloan[vin_2].nonqualifying_debt"
    value: "0.00"
    work: "Loan did not finance nonqualifying amounts, so the down-payment allocation does not apply"
  - printed: "carloan[vin_2].mixed_qualifying"
    value: "0.00"
    work: "Not a mixed loan, so there is no allocation"
  - printed: "carloan[vin_2].refi_qualifying"
    value: "0.00"
    work: "Not a refinanced loan (the obligor changed by death)"
  - printed: "carloan[vin_2].refi_nested"
    value: "no"
    work: "Not a refinanced loan"
  - printed: "carloan[vin_2].allocated"
    value: "0.00"
    work: "Interest paid or accrued is 0.00"
  - printed: "carloan[vin_2].refi_interest"
    value: "0.00"
    work: "Not a refinanced loan, and interest is 0.00"
  - printed: "carloan[vin_2].mixed_interest"
    value: "0.00"
    work: "Not a mixed loan, and interest is 0.00"
  - printed: "carloan[vin_2].mixed_prorated"
    value: "0.00"
    work: "Not a mixed loan, and interest is 0.00"
  - printed: "carloan[vin_2].qpvli"
    value: "0.00"
    work: "Interest paid or accrued in 2025 is 0.00"
  - printed: "carloan[vin_2].col_ii"
    value: "0.00"
    work: "The return has no Schedule C"
  - printed: "carloan[vin_2].col_iii"
    value: "0.00"
    work: "0.00 - 0.00 = 0.00"
```
```

### classm.carloan.3

```yaml
```yaml
lines:
  - printed: "carloan[vin_1].eligible"
    value: "yes"
    work: "Loan meets the loan requirements (yes) and vehicle is an APV (yes)"
  - printed: "carloan[vin_1].nonqualifying_debt"
    value: "9208.00"
    work: "Down payment applied first against nonqualifying amounts (1.163-16(d)(2)(iii)(B)): 9,208.00 - 0.00 = 9,208.00"
  - printed: "carloan[vin_1].mixed_qualifying"
    value: "0.00"
    work: "Loan 4,744.00 - nonqualifying 9,208.00 = -4,464.00; negative, so -0-"
  - printed: "carloan[vin_1].refi_qualifying"
    value: "0.00"
    work: "Loan is original, not a refinancing; the refinancing limit in (d)(4) does not apply"
  - printed: "carloan[vin_1].refi_nested"
    value: "no"
    work: "Not a refinancing; and the filer answered that all of the refinanced loan was an SPVL"
  - printed: "carloan[vin_1].allocated"
    value: "0.00"
    work: "Pro rata allocation (d)(2)(iii)(A): 12,004.00 x (0.00 / 4,744.00) = 0.00"
  - printed: "carloan[vin_1].refi_interest"
    value: "0.00"
    work: "Not a refinanced loan; no refinance allocation"
  - printed: "carloan[vin_1].mixed_interest"
    value: "0.00"
    work: "12,004.00 x round(0.00 / 4,744.00, 6) = 12,004.00 x 0.000000 = 0.00"
  - printed: "carloan[vin_1].mixed_prorated"
    value: "0.00"
    work: "12,004.00 x round(0.00 / 4,744.00, 6) = 12,004.00 x 0.000000 = 0.00"
  - printed: "carloan[vin_1].qpvli"
    value: "0.00"
    work: "Eligible loan; QPVLI is limited to interest on the SPVL portion = 0.00"
  - printed: "carloan[vin_1].col_ii"
    value: "0.00"
    work: "The return has no Schedule C, so column (ii) is 0"
  - printed: "carloan[vin_1].col_iii"
    value: "0.00"
    work: "Line 22 column (iii): 0.00 - 0.00 = 0.00"
```
```

### classm.carloan.4

```yaml
```yaml
lines:
  - printed: "carloan[vin_1].eligible"
    value: "no"
    work: "Loan does not meet the loan requirements, so the interest is not QPVLI"
  - printed: "carloan[vin_1].nonqualifying_debt"
    value: "0.00"
    work: "Loan not eligible; nothing to allocate"
  - printed: "carloan[vin_1].mixed_qualifying"
    value: "0.00"
    work: "Loan not eligible"
  - printed: "carloan[vin_1].refi_qualifying"
    value: "0.00"
    work: "Loan not eligible; the refinance SPVL limit is not reached"
  - printed: "carloan[vin_1].refi_nested"
    value: "no"
    work: "All of the refinanced loan was an SPVL"
  - printed: "carloan[vin_1].allocated"
    value: "0.00"
    work: "Loan not eligible; interest paid is $0"
  - printed: "carloan[vin_1].refi_interest"
    value: "0.00"
    work: "Loan not eligible"
  - printed: "carloan[vin_1].mixed_interest"
    value: "0.00"
    work: "Loan not eligible"
  - printed: "carloan[vin_1].mixed_prorated"
    value: "0.00"
    work: "Loan not eligible"
  - printed: "carloan[vin_1].qpvli"
    value: "0.00"
    work: "Not QPVLI because the loan requirements are not met"
  - printed: "carloan[vin_1].col_ii"
    value: "0.00"
    work: "No Schedule C"
  - printed: "carloan[vin_1].col_iii"
    value: "0.00"
    work: "0.00 - 0.00 = 0.00"
  - printed: "carloan[vin_2].eligible"
    value: "yes"
    work: "Loan meets the requirements and the vehicle is an APV"
  - printed: "carloan[vin_2].nonqualifying_debt"
    value: "0.00"
    work: "Loan financed no nonqualifying amounts; also max(0, 2,066 - 5,037) = 0"
  - printed: "carloan[vin_2].mixed_qualifying"
    value: "0.00"
    work: "Not a mixed loan, so the mixed allocation does not apply"
  - printed: "carloan[vin_2].refi_qualifying"
    value: "0.00"
    work: "Original loan, not a refinancing"
  - printed: "carloan[vin_2].refi_nested"
    value: "no"
    work: "Original loan, not a refinancing"
  - printed: "carloan[vin_2].allocated"
    value: "4413.00"
    work: "Whole loan is an SPVL, so all 4,413.00 of interest is allocated to it"
  - printed: "carloan[vin_2].refi_interest"
    value: "0.00"
    work: "Original loan, not a refinancing"
  - printed: "carloan[vin_2].mixed_interest"
    value: "0.00"
    work: "Not a mixed loan"
  - printed: "carloan[vin_2].mixed_prorated"
    value: "0.00"
    work: "Not a mixed loan"
  - printed: "carloan[vin_2].qpvli"
    value: "4413.00"
    work: "All interest paid or accrued on the SPVL is QPVLI: 4,413.00"
  - printed: "carloan[vin_2].col_ii"
    value: "0.00"
    work: "No Schedule C, so the 1,103.00 entry is disregarded"
  - printed: "carloan[vin_2].col_iii"
    value: "4413.00"
    work: "4,413.00 - 0.00 = 4,413.00"
```
```
