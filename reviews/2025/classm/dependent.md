# Class M hand-work — dependent

`Dependents — qualifying child and qualifying relative tests, per person listed` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-29 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt policy | worked-values-request-bound-v2 |
| system sha256 | 18ff9cfe094eedd0548bba02012b0ebf2a58d0606e834e3633432585b4192cb7 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | f3d0b09de8d82c0aa6d560f86701b6fbabeb1ac8854336934637128e13e11ca4 |
| cases | 7 |
| worked target scope | printed IRS lines |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 10, 14, 15, 17, 18, 19, 20, 21, 22, 41, 43, 44, 45, 46 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 15, 17, 18, 19, 20, 21, 22, 41, 43, 44, 45 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| p501 | 2025 returns; PDF created 2026-02-04 | 9, 13, 19 | cited pages | 6aca9108a08fb6d4725c630023df5e17084d92135c6607cd7c536e8e0c67f19b | 13, 19 | 2e0a281a7d3f73f1334d5f59a39a9fe4c393fd10dd6e6c6b1b8639c5ef038671 |
| p503 | For use in preparing 2025 returns | 3, 10 | cited pages | a1ff9e2c3120455f6049fc50f0af8c5b8160302c198162dede66b2c8a5640607 | 3, 10 | 44d87f0ddfd4f953ea02cf5cc31e203e754c88aa74627dac5a551f46c6bf65b9 |
| f1040s8812 | 2025; created 2025-07-30 | 1, 2 | whole document | 9b38295071c42fe489ec8f93e117b31eda11355b5a95e3fe388eeee69601c8c9 | - | 3525d47f51cb713591081610a862cae77eff08a8aa7e2064a96b15cee4fd5cb9 |
| i2441 | 2025 | 1, 3, 4 | cited pages | 361baee739cc7cb7b6a84c7412397cfba901c1a3e5f225a8077cb8716917887e | 1, 3, 4 | 3046d96b0769e20213f700deb20a0de9edc6a4572eda61bd70f5c8c88bc912ee |
| f2441 | 2025; created 2025-03-18 | 1, 2 | whole document | f39ca34d11c156e1ac55f4e2b5f16ef03c919773245cd7e50836e4c1555339c7 | - | 0e24fa891992674b84736c78565752c4a7d6f411fca4e24e5bb1307f239f60d6 |
| i8962 | 2025 | 8 | cited pages | 6b2be38425bc1a8b3073bfec01f18b7042e21187f37eec114ba185878be59976 | 8 | 11c5be397953d0f6bf8303148ac17e51c68c3cfed87cf2dc2de8a4173be5f309 |
| i8863 | 2025 | 1, 2, 3, 4, 9 | cited pages | 71d45c0b03b4521697e7f4fd52bbcc489d7dac6a3645b6d36f514ae5992e2e4d | 1, 3, 4, 9 | 6d486b4afb1f1647b7b99243cde905cf9def6b2813e5ed0bcb9925329c1e8a2b |
| f8863 | 2025 | 1, 2 | whole document | 8e2a766019b69e75af71e8da04f82a27534acb97f9ae4c2b72438a56d10d444e | - | 37bbeebd24c238e54a031ab21ac880feb5d8e9ce98f792e1b45d93e1bf8abc6c |

## Lines

### case classm.dependent.1 — prompt sha256 a0b18ba380d0619d0622d223d7e4f044e6bbcd2aeb9ae0f2e22d2028b00f1d90; branches: dependent.student:false, dependent.student:true, dependent.disabled:false, dependent.disabled:true, dependent.self_support:false, dependent.joint_return:false, dependent.citizen:true, dependent.canada_mexico:false, dependent.canada_mexico:true, dependent.married:false, dependent.tin:true, dependent.work_ssn:true, dependent.supported:true, dependent.other_claimant:false, dependent.divorced_rule:false, dependent.multiple_support:false, dependent.parent_home_paid:false, dependent.hoh_lived_half:true, dependent.dc_lived_half:true, dependent.qc_relationship:false, dependent.qc_relationship:true, dependent.younger:true, dependent.us_half:false, dependent.us_half:true, dependent.eic_ssn:false, dependent.eic_ssn:true, dependent.qc_age:true, dependent.lived_half:true, dependent.qualifying_child:false, dependent.qualifying_child:true, dependent.resident:true, dependent.qc_dependent:false, dependent.qc_dependent:true, dependent.qr_relationship:true, dependent.lawful:true, dependent.qr_income:false, dependent.qr_income:true, dependent.income_exception:false, dependent.qualifying_relative:false, dependent.qualifying_relative:true, dependent.qr_dependent:false, dependent.qr_dependent:true, dependent.claimed_no_tin:false, dependent.claimed:true, dependent.under_ctc_age:false, dependent.under_ctc_age:true, dependent.ctc_child:false, dependent.ctc_child:true, dependent.odc_person:false, dependent.odc_person:true, dependent.ctc_amount#0, dependent.ctc_amount#1, dependent.odc_amount#0, dependent.odc_amount#1, dependent.actc_amount#0, dependent.actc_amount#1, dependent.hoh_test2:true, dependent.hoh_test1:false, dependent.eic_child:false, dependent.eic_child:true, dependent.eic_ssn_child:false, dependent.eic_ssn_child:true, dependent.dc_child_all_year:false, dependent.dc_child_all_year:true, dependent.dc_age13:false, dependent.dc_under13:true, dependent.dc_child:false, dependent.dc_incapable:false, dependent.dc_incapable:true, dependent.dc_disabled_qp:false, dependent.dc_disabled_qp:true, dependent.dc_qp:false, dependent.dc_line2c:false, dependent.ptc_files:false, dependent.ptc_magi_counted#1, dependent.edu:false, dependent.edu:true, dependent.edu_1098t:false, dependent.edu_1098t:true, dependent.edu_student:false, dependent.edu_student:true, dependent.edu_adj#0, dependent.edu_adj#1, dependent.edu_over:false, dependent.edu_over_refused:false, dependent.edu_line23:false, dependent.edu_show24:false, dependent.edu_show24:true, dependent.edu_line24:false, dependent.edu_line24:true, dependent.edu_show25:false, dependent.edu_show25:true, dependent.edu_line25:false, dependent.edu_show26:false, dependent.edu_show26:true, dependent.edu_line26:false, dependent.edu_ein:false, dependent.edu_ein:true, dependent.edu_aoc:false, dependent.edu_aoc:true, dependent.edu_llc:false, dependent.edu_line27#0, dependent.edu_line27#1, dependent.edu_line28#0, dependent.edu_line28#1, dependent.edu_line29#0, dependent.edu_line29#1, dependent.edu_line30#0, dependent.edu_line30#1, dependent.edu_line31#1

### classm.dependent.1 — dependent[dep_a].dc_line2d — Qualified expenses you incurred and paid in 2025 for the person listed in column
Status: **AGREE**

Value: $0.00

### classm.dependent.1 — dependent[dep_a].dc_line2c — Check here if the qualifying person was over age 12 and was disabled
Status: **AGREE**

Value: no

### classm.dependent.1 — dependent[dep_b].dc_line2d — Qualified expenses you incurred and paid in 2025 for the person listed in column
Status: **AGREE**

Value: $0.00

### classm.dependent.1 — dependent[dep_b].dc_line2c — Check here if the qualifying person was over age 12 and was disabled
Status: **AGREE**

Value: no

### classm.dependent.1 — dependent[dep_c].dc_line2d — Qualified expenses you incurred and paid in 2025 for the person listed in column
Status: **AGREE**

Value: $0.00

### classm.dependent.1 — dependent[dep_c].dc_line2c — Check here if the qualifying person was over age 12 and was disabled
Status: **AGREE**

Value: no

### case classm.dependent.2 — prompt sha256 aa9f41c6409139f3c05bcaa2af88a5e91f5384a405df3333975bcd577ad9b9b9; branches: dependent.student:false, dependent.student:true, dependent.disabled:false, dependent.self_support:false, dependent.joint_return:false, dependent.citizen:false, dependent.citizen:true, dependent.canada_mexico:false, dependent.canada_mexico:true, dependent.married:false, dependent.tin:true, dependent.work_ssn:false, dependent.work_ssn:true, dependent.supported:false, dependent.supported:true, dependent.other_claimant:false, dependent.divorced_rule:false, dependent.multiple_support:false, dependent.parent_home_paid:false, dependent.parent_home_paid:true, dependent.hoh_lived_half:true, dependent.dc_lived_half:true, dependent.qc_relationship:false, dependent.qc_relationship:true, dependent.younger:false, dependent.younger:true, dependent.us_half:true, dependent.eic_ssn:true, dependent.qc_age:false, dependent.qc_age:true, dependent.lived_half:true, dependent.qualifying_child:false, dependent.qualifying_child:true, dependent.resident:false, dependent.resident:true, dependent.qc_dependent:false, dependent.qc_dependent:true, dependent.qr_relationship:true, dependent.lawful:true, dependent.qr_income:false, dependent.qr_income:true, dependent.income_exception:false, dependent.qualifying_relative:false, dependent.qualifying_relative:true, dependent.qr_dependent:false, dependent.qr_dependent:true, dependent.claimed_no_tin:false, dependent.claimed:false, dependent.claimed:true, dependent.under_ctc_age:true, dependent.ctc_child:false, dependent.odc_person:false, dependent.odc_person:true, dependent.ctc_amount#1, dependent.odc_amount#0, dependent.odc_amount#1, dependent.actc_amount#1, dependent.hoh_test2:false, dependent.hoh_test2:true, dependent.hoh_test1:false, dependent.eic_child:false, dependent.eic_child:true, dependent.eic_ssn_child:false, dependent.eic_ssn_child:true, dependent.dc_child_all_year:false, dependent.dc_age13:false, dependent.dc_age13:true, dependent.dc_under13:true, dependent.dc_child:false, dependent.dc_child:true, dependent.dc_incapable:false, dependent.dc_disabled_qp:false, dependent.dc_qp:false, dependent.dc_line2c:false, dependent.ptc_files:false, dependent.ptc_magi_counted#1, dependent.edu:false, dependent.edu_1098t:false, dependent.edu_student:false, dependent.edu_adj#1, dependent.edu_over:false, dependent.edu_over_refused:false, dependent.edu_line23:false, dependent.edu_show24:false, dependent.edu_line24:false, dependent.edu_show25:false, dependent.edu_line25:false, dependent.edu_show26:false, dependent.edu_line26:false, dependent.edu_ein:false, dependent.edu_aoc:false, dependent.edu_llc:false, dependent.edu_line27#1, dependent.edu_line28#1, dependent.edu_line29#1, dependent.edu_line30#1, dependent.edu_line31#1

### classm.dependent.2 — dependent[dep_a].dc_line2d — Qualified expenses you incurred and paid in 2025 for the person listed in column
Status: **AGREE**

Value: $0.00

### classm.dependent.2 — dependent[dep_a].dc_line2c — Check here if the qualifying person was over age 12 and was disabled
Status: **AGREE**

Value: no

### classm.dependent.2 — dependent[dep_b].dc_line2d — Qualified expenses you incurred and paid in 2025 for the person listed in column
Status: **AGREE**

Value: $0.00

### classm.dependent.2 — dependent[dep_b].dc_line2c — Check here if the qualifying person was over age 12 and was disabled
Status: **AGREE**

Value: no

### classm.dependent.2 — dependent[dep_c].dc_line2d — Qualified expenses you incurred and paid in 2025 for the person listed in column
Status: **AGREE**

Value: $0.00

### classm.dependent.2 — dependent[dep_c].dc_line2c — Check here if the qualifying person was over age 12 and was disabled
Status: **AGREE**

Value: no

### case classm.dependent.3 — prompt sha256 43cd2604496b759d4699b4e0e7629a608ecd219cb2cfcc2965e357c0fa2cde29; branches: dependent.student:false, dependent.disabled:false, dependent.self_support:false, dependent.joint_return:false, dependent.citizen:true, dependent.canada_mexico:true, dependent.married:false, dependent.tin:true, dependent.work_ssn:true, dependent.supported:false, dependent.other_claimant:false, dependent.divorced_rule:false, dependent.multiple_support:false, dependent.parent_home_paid:false, dependent.hoh_lived_half:true, dependent.dc_lived_half:true, dependent.qc_relationship:true, dependent.younger:true, dependent.us_half:true, dependent.eic_ssn:true, dependent.qc_age:true, dependent.lived_half:true, dependent.qualifying_child:true, dependent.resident:true, dependent.qc_dependent:true, dependent.qr_relationship:true, dependent.lawful:true, dependent.qr_income:false, dependent.income_exception:false, dependent.qualifying_relative:false, dependent.qr_dependent:false, dependent.claimed_no_tin:false, dependent.claimed:true, dependent.under_ctc_age:true, dependent.ctc_child:true, dependent.odc_person:false, dependent.ctc_amount#0, dependent.odc_amount#1, dependent.actc_amount#0, dependent.hoh_test2:true, dependent.hoh_test1:false, dependent.eic_child:true, dependent.eic_ssn_child:true, dependent.dc_child_all_year:true, dependent.dc_age13:false, dependent.dc_under13:true, dependent.dc_child:false, dependent.dc_incapable:false, dependent.dc_disabled_qp:false, dependent.dc_qp:false, dependent.dc_line2c:false, dependent.ptc_files:false, dependent.ptc_magi_counted#1, dependent.edu:true, dependent.edu_1098t:true, dependent.edu_student:true, dependent.edu_adj#0, dependent.edu_over:false, dependent.edu_over_refused:false, dependent.edu_line23:false, dependent.edu_show24:true, dependent.edu_line24:true, dependent.edu_show25:true, dependent.edu_line25:true, dependent.edu_show26:false, dependent.edu_line26:false, dependent.edu_ein:true, dependent.edu_aoc:false, dependent.edu_llc:true, dependent.edu_line27#1, dependent.edu_line28#1, dependent.edu_line29#1, dependent.edu_line30#1, dependent.edu_line31#0

### classm.dependent.3 — dependent[dep_a].dc_line2d — Qualified expenses you incurred and paid in 2025 for the person listed in column
Status: **AGREE**

Value: $0.00

### classm.dependent.3 — dependent[dep_a].dc_line2c — Check here if the qualifying person was over age 12 and was disabled
Status: **AGREE**

Value: no

### case classm.dependent.4 — prompt sha256 56937170ab090837b926a6c76825c07bb8ed653ee0d09bae34a2e5de6ec1c524; branches: dependent.student:false, dependent.student:true, dependent.disabled:false, dependent.self_support:false, dependent.self_support:true, dependent.joint_return:false, dependent.joint_return:true, dependent.citizen:false, dependent.citizen:true, dependent.canada_mexico:false, dependent.married:false, dependent.tin:true, dependent.work_ssn:true, dependent.supported:true, dependent.other_claimant:false, dependent.divorced_rule:false, dependent.multiple_support:false, dependent.parent_home_paid:false, dependent.parent_home_paid:true, dependent.hoh_lived_half:true, dependent.dc_lived_half:true, dependent.qc_relationship:false, dependent.qc_relationship:true, dependent.younger:true, dependent.us_half:true, dependent.eic_ssn:true, dependent.qc_age:false, dependent.lived_half:true, dependent.qualifying_child:false, dependent.resident:false, dependent.resident:true, dependent.qc_dependent:false, dependent.qr_relationship:true, dependent.lawful:true, dependent.qr_income:true, dependent.income_exception:false, dependent.qualifying_relative:true, dependent.qr_dependent:false, dependent.qr_dependent:true, dependent.claimed_no_tin:false, dependent.claimed:false, dependent.claimed:true, dependent.under_ctc_age:false, dependent.ctc_child:false, dependent.odc_person:false, dependent.odc_person:true, dependent.ctc_amount#1, dependent.odc_amount#0, dependent.odc_amount#1, dependent.actc_amount#1, dependent.hoh_test2:false, dependent.hoh_test2:true, dependent.hoh_test1:false, dependent.hoh_test1:true, dependent.eic_child:false, dependent.eic_ssn_child:false, dependent.dc_child_all_year:false, dependent.dc_age13:false, dependent.dc_under13:true, dependent.dc_child:false, dependent.dc_incapable:false, dependent.dc_disabled_qp:false, dependent.dc_qp:false, dependent.dc_line2c:false, dependent.ptc_files:false, dependent.ptc_magi_counted#1, dependent.edu:false, dependent.edu_1098t:false, dependent.edu_student:false, dependent.edu_adj#1, dependent.edu_over:false, dependent.edu_over_refused:false, dependent.edu_line23:false, dependent.edu_show24:false, dependent.edu_line24:false, dependent.edu_show25:false, dependent.edu_line25:false, dependent.edu_show26:false, dependent.edu_line26:false, dependent.edu_ein:false, dependent.edu_aoc:false, dependent.edu_llc:false, dependent.edu_line27#1, dependent.edu_line28#1, dependent.edu_line29#1, dependent.edu_line30#1, dependent.edu_line31#1

### classm.dependent.4 — dependent[dep_a].dc_line2d — Qualified expenses you incurred and paid in 2025 for the person listed in column
Status: **AGREE**

Value: $0.00

### classm.dependent.4 — dependent[dep_a].dc_line2c — Check here if the qualifying person was over age 12 and was disabled
Status: **AGREE**

Value: no

### classm.dependent.4 — dependent[dep_b].dc_line2d — Qualified expenses you incurred and paid in 2025 for the person listed in column
Status: **AGREE**

Value: $0.00

### classm.dependent.4 — dependent[dep_b].dc_line2c — Check here if the qualifying person was over age 12 and was disabled
Status: **AGREE**

Value: no

### classm.dependent.4 — dependent[dep_c].dc_line2d — Qualified expenses you incurred and paid in 2025 for the person listed in column
Status: **AGREE**

Value: $0.00

### classm.dependent.4 — dependent[dep_c].dc_line2c — Check here if the qualifying person was over age 12 and was disabled
Status: **AGREE**

Value: no

### case classm.dependent.5 — prompt sha256 2513a6ebb3617303d934b3e38bd23184c39c79e4f0ef580eba717f80f4be6cd7; branches: dependent.student:false, dependent.disabled:false, dependent.self_support:false, dependent.joint_return:false, dependent.citizen:true, dependent.canada_mexico:false, dependent.married:false, dependent.tin:false, dependent.work_ssn:true, dependent.supported:true, dependent.other_claimant:false, dependent.divorced_rule:false, dependent.multiple_support:false, dependent.parent_home_paid:false, dependent.hoh_lived_half:true, dependent.dc_lived_half:true, dependent.qc_relationship:false, dependent.younger:false, dependent.us_half:true, dependent.eic_ssn:true, dependent.qc_age:false, dependent.lived_half:true, dependent.qualifying_child:false, dependent.resident:true, dependent.qc_dependent:false, dependent.qr_relationship:false, dependent.lawful:true, dependent.qr_income:true, dependent.income_exception:false, dependent.qualifying_relative:false, dependent.qr_dependent:false, dependent.claimed_no_tin:false, dependent.claimed:false, dependent.under_ctc_age:false, dependent.ctc_child:false, dependent.odc_person:false, dependent.ctc_amount#1, dependent.odc_amount#1, dependent.actc_amount#1, dependent.hoh_test2:false, dependent.hoh_test1:false, dependent.eic_child:false, dependent.eic_ssn_child:false, dependent.dc_child_all_year:false, dependent.dc_age13:false, dependent.dc_under13:true, dependent.dc_child:false, dependent.dc_incapable:false, dependent.dc_disabled_qp:false, dependent.dc_qp:false, dependent.dc_line2c:false, dependent.ptc_files:false, dependent.ptc_magi_counted#1, dependent.edu:false, dependent.edu_1098t:false, dependent.edu_student:false, dependent.edu_adj#1, dependent.edu_over:false, dependent.edu_over_refused:false, dependent.edu_line23:false, dependent.edu_show24:false, dependent.edu_line24:false, dependent.edu_show25:false, dependent.edu_line25:false, dependent.edu_show26:false, dependent.edu_line26:false, dependent.edu_ein:false, dependent.edu_aoc:false, dependent.edu_llc:false, dependent.edu_line27#1, dependent.edu_line28#1, dependent.edu_line29#1, dependent.edu_line30#1, dependent.edu_line31#1

### classm.dependent.5 — dependent[dep_a].dc_line2d — Qualified expenses you incurred and paid in 2025 for the person listed in column
Status: **AGREE**

Value: $0.00

### classm.dependent.5 — dependent[dep_a].dc_line2c — Check here if the qualifying person was over age 12 and was disabled
Status: **AGREE**

Value: no

### case classm.dependent.6 — prompt sha256 50abc4cfe07c753a5198f08c2d40b5483103c98c61e067a9fc6768e621606188; branches: dependent.student:false, dependent.student:true, dependent.disabled:false, dependent.self_support:false, dependent.joint_return:false, dependent.joint_return:true, dependent.citizen:true, dependent.canada_mexico:false, dependent.married:false, dependent.tin:true, dependent.work_ssn:true, dependent.supported:true, dependent.other_claimant:false, dependent.divorced_rule:false, dependent.multiple_support:false, dependent.parent_home_paid:false, dependent.parent_home_paid:true, dependent.hoh_lived_half:true, dependent.dc_lived_half:true, dependent.qc_relationship:true, dependent.younger:true, dependent.us_half:true, dependent.eic_ssn:true, dependent.qc_age:false, dependent.qc_age:true, dependent.lived_half:true, dependent.qualifying_child:false, dependent.qualifying_child:true, dependent.resident:true, dependent.qc_dependent:false, dependent.qc_dependent:true, dependent.qr_relationship:true, dependent.lawful:true, dependent.qr_income:true, dependent.income_exception:false, dependent.qualifying_relative:false, dependent.qualifying_relative:true, dependent.qr_dependent:false, dependent.qr_dependent:true, dependent.claimed_no_tin:false, dependent.claimed:true, dependent.under_ctc_age:false, dependent.under_ctc_age:true, dependent.ctc_child:false, dependent.ctc_child:true, dependent.odc_person:false, dependent.odc_person:true, dependent.ctc_amount#0, dependent.ctc_amount#1, dependent.odc_amount#0, dependent.odc_amount#1, dependent.actc_amount#0, dependent.actc_amount#1, dependent.hoh_test2:true, dependent.hoh_test1:false, dependent.eic_child:false, dependent.eic_child:true, dependent.eic_ssn_child:false, dependent.eic_ssn_child:true, dependent.dc_child_all_year:false, dependent.dc_child_all_year:true, dependent.dc_age13:false, dependent.dc_under13:true, dependent.dc_child:false, dependent.dc_incapable:false, dependent.dc_disabled_qp:false, dependent.dc_qp:false, dependent.dc_qp:true, dependent.dc_line2c:false, dependent.ptc_files:false, dependent.ptc_magi_counted#1, dependent.edu:false, dependent.edu_1098t:false, dependent.edu_student:false, dependent.edu_adj#1, dependent.edu_over:false, dependent.edu_over_refused:false, dependent.edu_line23:false, dependent.edu_show24:false, dependent.edu_line24:false, dependent.edu_show25:false, dependent.edu_line25:false, dependent.edu_show26:false, dependent.edu_line26:false, dependent.edu_ein:false, dependent.edu_aoc:false, dependent.edu_llc:false, dependent.edu_line27#1, dependent.edu_line28#1, dependent.edu_line29#1, dependent.edu_line30#1, dependent.edu_line31#1

### classm.dependent.6 — dependent[dep_a].dc_line2d — Qualified expenses you incurred and paid in 2025 for the person listed in column
Status: **AGREE**

Value: $1,480.00

### classm.dependent.6 — dependent[dep_a].dc_line2c — Check here if the qualifying person was over age 12 and was disabled
Status: **AGREE**

Value: no

### classm.dependent.6 — dependent[dep_b].dc_line2d — Qualified expenses you incurred and paid in 2025 for the person listed in column
Status: **DISAGREE**

Project: $250.00
Model: $0.00
Work: Age 25, not a student, not disabled: fails the qualifying child age test; can care for self, so not a 2441 qualifying person; enter 0

Ruling: representation; project retained; model value dropped from the fixture. Case inputs (fixtures/2025/classm.json, classm.dependent.6): f2441.care yes; dep_b is a child aged 25, not a student, not disabled, dc_incapable no, joint_return yes with married no, dc_paid $250.00. The project claims dep_b as a qualifying relative, but dc_child_all_year, dc_child and dc_disabled_qp are all no, so dependent.dc_qp is no; dependent.dc_line2d copies dc_paid and shows $250.00. The model's $0.00 is the source's reading (i2441 p. 3, Line 2, "Don't list a person on line 2 unless they are listed as an eligible person under Qualifying Person(s), earlier"). The $250.00 reaches nothing: f2441.paid_total (line 3) sums column (d) only where dc_qp is true, and the interview never asks dc_paid for a non-qualifying person (the where filter is evaluated before the field). The amount exists only because the generated return supplies an answer the interview does not ask; the same entry was ruled as classm.dependent.8 in Stage 19 rounds 1 and 2 (the case is renumbered) and at classm.dependent.5 in Stage 18. The expectation is dropped because the fixture would pin a value no interview return shows. [dropped]

### classm.dependent.6 — dependent[dep_b].dc_line2c — Check here if the qualifying person was over age 12 and was disabled
Status: **AGREE**

Value: no

### case classm.dependent.7 — prompt sha256 24adf3670298476245a1ebec9d05c3da57c92be9aaee26420050e4fab2cc1551; branches: dependent.student:false, dependent.disabled:false, dependent.self_support:false, dependent.joint_return:false, dependent.citizen:true, dependent.canada_mexico:false, dependent.married:false, dependent.tin:true, dependent.work_ssn:true, dependent.supported:true, dependent.other_claimant:false, dependent.divorced_rule:false, dependent.multiple_support:false, dependent.parent_home_paid:false, dependent.hoh_lived_half:true, dependent.dc_lived_half:true, dependent.qc_relationship:false, dependent.qc_relationship:true, dependent.younger:true, dependent.us_half:true, dependent.eic_ssn:true, dependent.qc_age:false, dependent.lived_half:true, dependent.qualifying_child:false, dependent.resident:true, dependent.qc_dependent:false, dependent.qr_relationship:true, dependent.lawful:true, dependent.qr_income:true, dependent.income_exception:false, dependent.qualifying_relative:true, dependent.qr_dependent:true, dependent.claimed_no_tin:false, dependent.claimed:true, dependent.under_ctc_age:false, dependent.ctc_child:false, dependent.odc_person:true, dependent.ctc_amount#1, dependent.odc_amount#0, dependent.actc_amount#1, dependent.hoh_test2:true, dependent.hoh_test1:false, dependent.eic_child:false, dependent.eic_ssn_child:false, dependent.dc_child_all_year:false, dependent.dc_age13:false, dependent.dc_under13:true, dependent.dc_child:false, dependent.dc_incapable:false, dependent.dc_disabled_qp:false, dependent.dc_qp:false, dependent.dc_line2c:false, dependent.ptc_files:false, dependent.ptc_magi_counted#1, dependent.edu:false, dependent.edu:true, dependent.edu_1098t:false, dependent.edu_1098t:true, dependent.edu_student:false, dependent.edu_student:true, dependent.edu_adj#0, dependent.edu_adj#1, dependent.edu_over:false, dependent.edu_over_refused:false, dependent.edu_line23:false, dependent.edu_line23:true, dependent.edu_show24:false, dependent.edu_line24:false, dependent.edu_line24:true, dependent.edu_show25:false, dependent.edu_line25:false, dependent.edu_show26:false, dependent.edu_line26:false, dependent.edu_ein:false, dependent.edu_ein:true, dependent.edu_aoc:false, dependent.edu_llc:false, dependent.edu_llc:true, dependent.edu_line27#1, dependent.edu_line28#1, dependent.edu_line29#1, dependent.edu_line30#1, dependent.edu_line31#0, dependent.edu_line31#1

### classm.dependent.7 — dependent[dep_a].dc_line2d — Qualified expenses you incurred and paid in 2025 for the person listed in column
Status: **AGREE**

Value: $0.00

### classm.dependent.7 — dependent[dep_a].dc_line2c — Check here if the qualifying person was over age 12 and was disabled
Status: **AGREE**

Value: no

### classm.dependent.7 — dependent[dep_b].dc_line2d — Qualified expenses you incurred and paid in 2025 for the person listed in column
Status: **AGREE**

Value: $0.00

### classm.dependent.7 — dependent[dep_b].dc_line2c — Check here if the qualifying person was over age 12 and was disabled
Status: **AGREE**

Value: no

## Raw responses

### classm.dependent.1

```yaml
```yaml
lines:
  - printed: "dependent[dep_a].dc_line2d"
    value: "0.00"
    work: "No care paid so you could work (Form 2441 answer no); qualified care expenses given = $0.00"
  - printed: "dependent[dep_a].dc_line2c"
    value: "no"
    work: "No care was paid, so Form 2441 line 2 has no entry; filer also says under age 13 when care was provided, so not 'over age 12'"
  - printed: "dependent[dep_b].dc_line2d"
    value: "0.00"
    work: "No care paid so you could work; qualified care expenses given = $0.00"
  - printed: "dependent[dep_b].dc_line2c"
    value: "no"
    work: "Age 8 and able to care for self; not over age 12 and disabled"
  - printed: "dependent[dep_c].dc_line2d"
    value: "0.00"
    work: "No care paid so you could work; qualified care expenses given = $0.00"
  - printed: "dependent[dep_c].dc_line2c"
    value: "no"
    work: "Not physically or mentally unable to care for self, so not disabled; no care was paid"
```
```

### classm.dependent.2

```yaml
```yaml
lines:
  - printed: "dependent[dep_a].dc_line2d"
    value: "0.00"
    work: "Filer paid no care expenses so they could work; qualified expenses given as $0.00"
  - printed: "dependent[dep_a].dc_line2c"
    value: "no"
    work: "Age 13 is over 12, but the person is able to care for themselves, so not disabled; box not checked"
  - printed: "dependent[dep_b].dc_line2d"
    value: "0.00"
    work: "No care expenses paid; qualified expenses $0.00 (also not a dependent: support test not met and gross income of $5,617 is not under $5,200)"
  - printed: "dependent[dep_b].dc_line2c"
    value: "no"
    work: "Age 3 is not over 12, and the person is able to care for themselves; box not checked"
  - printed: "dependent[dep_c].dc_line2d"
    value: "0.00"
    work: "No care expenses paid; qualified expenses $0.00 (also not younger than the filer, so fails the qualifying-child age test)"
  - printed: "dependent[dep_c].dc_line2c"
    value: "no"
    work: "Age 11 is not over 12, and the person is able to care for themselves; box not checked"
```
```

### classm.dependent.3

```yaml
```yaml
lines:
  - printed: "dependent[dep_a].dc_line2d"
    value: "0.00"
    work: "Sibling, age 4, lived with you 12 months: qualifying child and dependent under 13. Qualified care expenses incurred and paid in 2025 = $0.00."
  - printed: "dependent[dep_a].dc_line2c"
    value: "no"
    work: "Column (c) is checked only if the person was over age 12 and disabled. Age 4 and not unable to self-care, so no."
```
```

### classm.dependent.4

```yaml
```yaml
lines:
  - printed: "dependent[dep_a].dc_line2d"
    value: "0.00"
    work: "No care paid (Form 2441 answer no); qualified expenses given $0.00; not a qualifying person (age 40, able to care for self)"
  - printed: "dependent[dep_a].dc_line2c"
    value: "no"
    work: "Col (c) is checked only if over age 12 AND disabled; age 40 but physically/mentally able to care for self"
  - printed: "dependent[dep_b].dc_line2d"
    value: "0.00"
    work: "No care paid; qualified expenses given $0.00; not a qualifying person (age 86, able to care for self)"
  - printed: "dependent[dep_b].dc_line2c"
    value: "no"
    work: "Col (c) is checked only if over age 12 AND disabled; age 86 but not incapable of self-care"
  - printed: "dependent[dep_c].dc_line2d"
    value: "0.00"
    work: "No care paid; qualified expenses given $0.00; not a qualifying person (age 53, able to care for self)"
  - printed: "dependent[dep_c].dc_line2c"
    value: "no"
    work: "Col (c) is checked only if over age 12 AND disabled; age 53 but not incapable of self-care"
```
```

### classm.dependent.5

```yaml
```yaml
lines:
  - printed: "dependent[dep_a].dc_line2d"
    value: "0.00"
    work: "Filer paid no care expenses (Form 2441 answer no; expenses $0.00). dep_a is also not a qualifying person: a 26-year-old household member is not a qualifying child, and living 10 of 12 months fails the all-year test for a qualifying relative, so 0.00."
  - printed: "dependent[dep_a].dc_line2c"
    value: "no"
    work: "Col (c) requires over age 12 AND disabled. dep_a is over 12 (age 26) but able to care for themselves, so no."
```
```

### classm.dependent.6

```yaml
```yaml
lines:
  - printed: "dependent[dep_a].dc_line2d"
    value: "1480.00"
    work: "Sibling age 4 passes every qualifying child test, is your dependent and was under 13, so is a qualifying person; enter paid expenses of $1,480.00"
  - printed: "dependent[dep_a].dc_line2c"
    value: "no"
    work: "Not over age 12 and not disabled, so column (c) stays unchecked"
  - printed: "dependent[dep_b].dc_line2d"
    value: "0.00"
    work: "Age 25, not a student, not disabled: fails the qualifying child age test; can care for self, so not a 2441 qualifying person; enter 0"
  - printed: "dependent[dep_b].dc_line2c"
    value: "no"
    work: "Over age 12 but not physically or mentally unable to care for self, so not disabled; column (c) stays unchecked"
```
```

### classm.dependent.7

```yaml
```yaml
lines:
  - printed: "dependent[dep_a].dc_line2d"
    value: "0.00"
    work: "Not a qualifying person: age 49, so not a qualifying child under 13, and able to care for self. No care was paid in 2025 (Form 2441 answer is no). Enter 0."
  - printed: "dependent[dep_a].dc_line2c"
    value: "no"
    work: "Over age 12 but not physically or mentally unable to care for self, so not disabled. Box stays unchecked."
  - printed: "dependent[dep_b].dc_line2d"
    value: "0.00"
    work: "Parent who qualifies only as a qualifying relative and is able to care for self, so not a qualifying person. No care was paid in 2025. Enter 0."
  - printed: "dependent[dep_b].dc_line2c"
    value: "no"
    work: "Not physically or mentally unable to care for self, so not disabled. Box stays unchecked."
```
```
