# Class M hand-work — ny_rs

`New York State tax rate schedule` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/ny/2025/classm.deepseek.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-11-05 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt policy | worked-values-request-bound-v2 |
| system sha256 | 14a5e4eb8d846a6706a317abd7af9a45f1e53937087ad30bf4e35fe555725b8e |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 3181afbaf71c22ff099ebe7419d24bca028e1c111785640bc777a5d8d4ab87e4 |
| cases | 29 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| ny_it201i-html | Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny) | 1 | cited sections: New York State tax rate schedule | 63863fe461c33d052e26a67c87d000ed70b896c72437350880a9e1c680104982 | - | - |
| ny_it201i | Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20 | 4 | cited pages | 05f677379d60faca0da08ac2dc171a937cf56878f73956511975c1dcc48aeff9 | 4 | 460f67bd9e14ac9d7ed2e001426510569307546a5c2cf0a97784808e2678eeaf |

## Lines

### case classm.ny_rs.1 — prompt sha256 bf1746cd52bbec8a34c03077f43327c874cea02776322a6c8fecd67fe0354cb3; branches: mfj.b4.excess:positive, mfj.result#3, tax#1

### classm.ny_rs.1 — tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project: $1,773.00
Model: $1,772.63
Work: MFJ bracket: $1,202 + 5.5% × ($38,275 − $27,900) = $1,202 + $570.625 = $1,772.63

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse", the bracket for line 38 of $38,275: $1,202 plus 5.5% of the excess over $27,900: exactly $1,772.625, which the project rounds half-up to $1,773.00; the model's $1,772.63 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### case classm.ny_rs.2 — prompt sha256 03c0795a1430cdaed4a46d078024027e73edbaaf864b5ebcacd1036ae1bd1070; branches: single.b4.excess:positive, single.result#3, tax#0

### classm.ny_rs.2 — tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project: $1,596.00
Model: $1,595.50
Work: Single schedule: $600 + 5.5% × ($32,000 − $13,900) = $600 + $995.50 = $1,595.50

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), New York State tax rate schedule, "Single and married filing separately", the bracket for line 38 of $32,000: $600 plus 5.5% of the excess over $13,900: exactly $1,595.50, which the project rounds half-up to $1,596.00; the model's $1,595.50 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### case classm.ny_rs.3 — prompt sha256 e95ca8a9381b09ce235b134b1e5ed28592ff11b9c4737044fe0997b149c87772; branches: hoh.b1.excess:floor, hoh.result#0, tax#4

### classm.ny_rs.3 — tax — The tax from the schedule for the filing status
Status: **AGREE**

Value: $0.00

### case classm.ny_rs.4 — prompt sha256 d571801ba920886cb2feb914159a77a27bb36dd7c8fe3d9498341b8449f7111d; branches: mfj.b5.excess:positive, mfj.result#4, tax#2

### classm.ny_rs.4 — tax — The tax from the schedule for the filing status
Status: **AGREE**

Value: $10,860.00

### case classm.ny_rs.5 — prompt sha256 a9beff01378641e5e467fd4524b583198ee0dbcbef18677b1082a7bcfb68e10a; branches: single.b5.excess:positive, single.result#4, tax#3

### classm.ny_rs.5 — tax — The tax from the schedule for the filing status
Status: **AGREE**

Value: $6,632.00

### case classm.ny_rs.6 — prompt sha256 791947164458b1588bd6291a32305b888caa4f2a95afc9c83dec273004c1a0f7; branches: mfj.b1.excess:floor, mfj.result#0, tax#1

### classm.ny_rs.6 — tax — The tax from the schedule for the filing status
Status: **AGREE**

Value: $0.00

### case classm.ny_rs.7 — prompt sha256 206e333ea866cfe2ee8fc6f93bfe8a9ccae954513760ac44fbb24bd96ead9cc7; branches: mfj.b3.excess:positive, mfj.result#2, tax#1

### classm.ny_rs.7 — tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project: $1,049.00
Model: $1,049.45
Work: MFJ bracket over $23,600 but not over $27,900: $976 + 5.25% × ($24,999 − $23,600) = $976 + $73.45 = $1,049.45.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse", the bracket for line 38 of $24,999: $976 plus 5.25% of the excess over $23,600: exactly $1,049.4475, which the project rounds half-up to $1,049.00; the model's $1,049.45 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### case classm.ny_rs.8 — prompt sha256 dc390b50f8a0b4ab6c984aaa5f57f03180d8dc4c3033c8328f9845a40bbc9ee9; branches: hoh.b4.excess:positive, hoh.result#3, tax#4

### classm.ny_rs.8 — tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project: $1,126.00
Model: $1,126.45
Work: HOH bracket $20,900–$107,650: $901 + 5.5% × ($24,999 − $20,900) = $901 + $225.445 = $1,126.445, rounded to $1,126.45.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), New York State tax rate schedule, "Head of household", the bracket for line 38 of $24,999: $901 plus 5.5% of the excess over $20,900: exactly $1,126.445, which the project rounds half-up to $1,126.00; the model's $1,126.45 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### case classm.ny_rs.9 — prompt sha256 edb95f794a28ccebf9422062d44bacadbb93c7c6a659f4f353c67ab203de16f0; branches: single.b6.excess:positive, single.result#5, tax#0

### classm.ny_rs.9 — tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project: $12,356.00
Model: $12,356.07
Work: Single schedule: $12,356 + 6.85% × ($215,401 − $215,400) = $12,356 + $0.0685 = $12,356.07

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), New York State tax rate schedule, "Single and married filing separately", the bracket for line 38 of $215,401: $12,356 plus 6.85% of the excess over $215,400: exactly $12,356.0685, which the project rounds half-up to $12,356.00; the model's $12,356.07 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### case classm.ny_rs.10 — prompt sha256 c0a352228de0762cbaa019ddacd01ecccff005e3b3094eb1016deccaf1a8cc09; branches: single.b7.excess:positive, single.result#6, tax#0

### classm.ny_rs.10 — tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project: $71,413.00
Model: $71,413.10
Work: Single schedule: 71,413 + 9.65% × (1,077,551 − 1,077,550) = 71,413.0965, rounded to 71,413.10

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), New York State tax rate schedule, "Single and married filing separately", the bracket for line 38 of $1,077,551: $71,413 plus 9.65% of the excess over $1,077,550: exactly $71,413.0965, which the project rounds half-up to $71,413.00; the model's $71,413.10 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### case classm.ny_rs.11 — prompt sha256 173629e57a33e049a68498364834b4df6cc933280ffcfa1e96201b7fe5c40659; branches: single.b8.excess:positive, single.result#7, tax#0

### classm.ny_rs.11 — tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project: $449,929.00
Model: $449,929.10
Work: Single schedule: $449,929 + 10.3% × ($5,000,001 − $5,000,000) = $449,929.103, rounded to $449,929.10

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), New York State tax rate schedule, "Single and married filing separately", the bracket for line 38 of $5,000,001: $449,929 plus 10.3% of the excess over $5,000,000: exactly $449,929.103, which the project rounds half-up to $449,929.00; the model's $449,929.10 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### case classm.ny_rs.12 — prompt sha256 d48f11da8cff8c7812827113653030485038e397ae5b1098024ea93707e13d08; branches: single.b9.excess:positive, single.result#8, tax#0

### classm.ny_rs.12 — tax — The tax from the schedule for the filing status
Status: **AGREE**

Value: $2,618,929.00

### case classm.ny_rs.13 — prompt sha256 afb25b72908a76c1b114612a51c7a72f15ae18e64cc194ef14cfda02975f1f12; branches: mfj.b6.excess:positive, mfj.result#5, tax#1

### classm.ny_rs.13 — tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project: $18,252.00
Model: $18,252.07
Work: MFJ bracket: $18,252 + 6.85% × ($323,201 − $323,200) = $18,252 + $0.0685 = $18,252.07

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse", the bracket for line 38 of $323,201: $18,252 plus 6.85% of the excess over $323,200: exactly $18,252.0685, which the project rounds half-up to $18,252.00; the model's $18,252.07 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### case classm.ny_rs.14 — prompt sha256 3dab8f5eefd7e338d3851c6d63e0c4fa33b8027640c0b3289183b54e8968b2a3; branches: mfj.b7.excess:positive, mfj.result#6, tax#1

### classm.ny_rs.14 — tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project: $143,754.00
Model: $143,754.10
Work: MFJ bracket over $2,155,350: $143,754 + 9.65% × ($2,155,351 − $2,155,350) = $143,754.0965, rounded to $143,754.10

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse", the bracket for line 38 of $2,155,351: $143,754 plus 9.65% of the excess over $2,155,350: exactly $143,754.0965, which the project rounds half-up to $143,754.00; the model's $143,754.10 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### case classm.ny_rs.15 — prompt sha256 cae9b22fae60f38e7f187de6ae4fede57a2debfc9bbab20cd9626ae1e04310c9; branches: mfj.b8.excess:positive, mfj.result#7, tax#1

### classm.ny_rs.15 — tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project: $418,263.00
Model: $418,263.10
Work: MFJ schedule: 418,263 + 10.3% × (5,000,001 − 5,000,000) = 418,263.10

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse", the bracket for line 38 of $5,000,001: $418,263 plus 10.3% of the excess over $5,000,000: exactly $418,263.103, which the project rounds half-up to $418,263.00; the model's $418,263.10 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### case classm.ny_rs.16 — prompt sha256 2d74ca3c851604fac0d54411ec783c9953dae3ead87d3e25cf6529e91d8eeb9b; branches: hoh.b5.excess:positive, hoh.result#4, tax#4

### classm.ny_rs.16 — tax — The tax from the schedule for the filing status
Status: **AGREE**

Value: $5,813.00

### case classm.ny_rs.17 — prompt sha256 e60bc295b2e7dd918a102881c37de158f29f1ee7175aad237d1b5657b7026fad; branches: hoh.b6.excess:positive, hoh.result#5, tax#4

### classm.ny_rs.17 — tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project: $15,371.00
Model: $15,371.07
Work: Head of household bracket over $269,300: $15,371 + 6.85% × ($269,301 − $269,300) = $15,371.07

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), New York State tax rate schedule, "Head of household", the bracket for line 38 of $269,301: $15,371 plus 6.85% of the excess over $269,300: exactly $15,371.0685, which the project rounds half-up to $15,371.00; the model's $15,371.07 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### case classm.ny_rs.18 — prompt sha256 b4739548a518216e9eed628148676d7a82825794ac3e9be6e13fe771241049e3; branches: hoh.b7.excess:positive, hoh.result#6, tax#4

### classm.ny_rs.18 — tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project: $107,651.00
Model: $107,651.10
Work: Head of household schedule: $107,651 + 9.65% × ($1,616,451 − $1,616,450) = $107,651.0965, rounded to $107,651.10

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), New York State tax rate schedule, "Head of household", the bracket for line 38 of $1,616,451: $107,651 plus 9.65% of the excess over $1,616,450: exactly $107,651.0965, which the project rounds half-up to $107,651.00; the model's $107,651.10 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### case classm.ny_rs.19 — prompt sha256 1ab90162f3bdf6fb3971ba5817c4a49e47ae5b724e58e854a93a9686b82961dd; branches: hoh.b8.excess:positive, hoh.result#7, tax#4

### classm.ny_rs.19 — tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project: $434,163.00
Model: $434,163.10
Work: HOH schedule over $5,000,000: 434,163 + 10.3% × $1 = 434,163.103, rounded to 434,163.10

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), New York State tax rate schedule, "Head of household", the bracket for line 38 of $5,000,001: $434,163 plus 10.3% of the excess over $5,000,000: exactly $434,163.103, which the project rounds half-up to $434,163.00; the model's $434,163.10 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### case classm.ny_rs.20 — prompt sha256 f3e1257f226cdd3e169ecc72cb60dac8586ccc01d7e6a77cc697b45747f3df23; branches: hoh.b2.excess:positive, hoh.result#1, tax#4

### classm.ny_rs.20 — tax — The tax from the schedule for the filing status
Status: **AGREE**

Value: $566.00

### case classm.ny_rs.21 — prompt sha256 2bec0b13d443bf18638ec5aac672fc0349b572f7a18dd15c5ec82470527a27da; branches: single.b1.excess:positive, single.result#0, tax#3

### classm.ny_rs.21 — tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project: $308.00
Model: $307.52
Work: Married filing separately schedule: 4% of line 38; $7,688.00 × 4% = $307.52

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), New York State tax rate schedule, "Single and married filing separately", the bracket for line 38 of $7,688: 4% of the amount: exactly $307.52, which the project rounds half-up to $308.00; the model's $307.52 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### case classm.ny_rs.22 — prompt sha256 8f37bfe3b1ad52ec5007e8f43ba8a0ecef5553f11e01a9d8c0c6ccd1cd4ec9f7; branches: single.b2.excess:positive, single.result#1, tax#3

### classm.ny_rs.22 — tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project: $484.00
Model: $483.51
Work: Married filing separately bracket $8,500–$11,700: $340 + 4.5% × ($11,689 − $8,500) = $483.505, rounded to $483.51

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), New York State tax rate schedule, "Single and married filing separately", the bracket for line 38 of $11,689: $340 plus 4.5% of the excess over $8,500: exactly $483.505, which the project rounds half-up to $484.00; the model's $483.51 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### case classm.ny_rs.23 — prompt sha256 cf80c8eaf63bb2b08164538d94ccbadedd09e3c74dd04b3af94f1d3f685c3b76; branches: single.b3.excess:positive, single.result#2, tax#3

### classm.ny_rs.23 — tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project: $589.00
Model: $588.53
Work: MFS schedule: $484 + 5.25% × ($13,691 − $11,700) = $484 + $104.5275 = $588.5275, rounded to $588.53.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), New York State tax rate schedule, "Single and married filing separately", the bracket for line 38 of $13,691: $484 plus 5.25% of the excess over $11,700: exactly $588.5275, which the project rounds half-up to $589.00; the model's $588.53 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### case classm.ny_rs.24 — prompt sha256 d81be4ec606c404dbc71a5e51b35eb9287573b2e6ca47fa0e11ccbd024c555ab; branches: mfj.b2.excess:positive, mfj.result#1, tax#1

### classm.ny_rs.24 — tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project: $934.00
Model: $933.50
Work: MFJ schedule: $686 plus 4.5% of ($22,650 - $17,150) = $686 + $247.50 = $933.50

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse", the bracket for line 38 of $22,650: $686 plus 4.5% of the excess over $17,150: exactly $933.50, which the project rounds half-up to $934.00; the model's $933.50 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### case classm.ny_rs.25 — prompt sha256 01766c6de770bfda65ce05e4176535bb52f581ae5423134c820e97fd0422910c; branches: hoh.b3.excess:positive, hoh.result#2, tax#4

### classm.ny_rs.25 — tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project: $880.00
Model: $879.52
Work: HOH schedule: $730 + 5.25% × ($20,498 − $17,650) = $879.52

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), New York State tax rate schedule, "Head of household", the bracket for line 38 of $20,498: $730 plus 5.25% of the excess over $17,650: exactly $879.52, which the project rounds half-up to $880.00; the model's $879.52 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### case classm.ny_rs.26 — prompt sha256 b526051134a25cd597420592f60e479ccec9b3fb82f2b8463204bf3f57bb9bb6; branches: mfj.b9.excess:positive, mfj.result#8, tax#1

### classm.ny_rs.26 — tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project: $2,532,763.00
Model: $2,532,762.56
Work: MFJ schedule: 2,478,263 + 10.9% × (25,499,996 − 25,000,000) = 2,478,263 + 54,499.564 = 2,532,762.564, rounded to cents.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse", the bracket for line 38 of $25,499,996: $2,478,263 plus 10.9% of the excess over $25,000,000: exactly $2,532,762.564, which the project rounds half-up to $2,532,763.00; the model's $2,532,762.56 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### case classm.ny_rs.27 — prompt sha256 7b6028a2886f054ad1835ac0e987c4254af5f5b3661e4154747da850654c69cd; branches: hoh.b9.excess:positive, hoh.result#8, tax#4

### classm.ny_rs.27 — tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project: $2,548,663.00
Model: $2,548,662.56
Work: HOH bracket over $25,000,000: $2,494,163 + 10.9% × ($25,499,996 − $25,000,000) = $2,548,662.56

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), New York State tax rate schedule, "Head of household", the bracket for line 38 of $25,499,996: $2,494,163 plus 10.9% of the excess over $25,000,000: exactly $2,548,662.564, which the project rounds half-up to $2,548,663.00; the model's $2,548,662.56 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### case classm.ny_rs.28 — prompt sha256 ea1ff5a44aaaeb2fe728b439a29abe053b5630df137e5f17aa13ef0eb3b92d4f; branches: mfj.b1.excess:positive, mfj.result#0, tax#1

### classm.ny_rs.28 — tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project: $0.00
Model: $0.48
Work: Married filing jointly: line 38 $12.00 is over $0 but not over $17,150, so tax = 4% × $12.00 = $0.48.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse", the bracket for line 38 of $12: 4% of the amount: exactly $0.48, which the project rounds half-up to $0.00; the model's $0.48 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### case classm.ny_rs.29 — prompt sha256 254b4369abc00e1c75c96158601a8340c761736b0671f02b08727e5a5945362a; branches: hoh.b1.excess:positive, hoh.result#0, tax#4

### classm.ny_rs.29 — tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project: $0.00
Model: $0.48
Work: Head of household: line 38 $12.00 is in $0–$12,800 bracket; tax = 4% × $12.00 = $0.48.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), New York State tax rate schedule, "Head of household", the bracket for line 38 of $12: 4% of the amount: exactly $0.48, which the project rounds half-up to $0.00; the model's $0.48 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

## Raw responses

### classm.ny_rs.1

```yaml
lines:
  - printed: "tax"
    value: "1772.63"
    work: "MFJ bracket: $1,202 + 5.5% × ($38,275 − $27,900) = $1,202 + $570.625 = $1,772.63"
```

### classm.ny_rs.2

```yaml
lines:
  - printed: "tax"
    value: "1595.50"
    work: "Single schedule: $600 + 5.5% × ($32,000 − $13,900) = $600 + $995.50 = $1,595.50"
```

### classm.ny_rs.3

```yaml
lines:
  - printed: "tax"
    value: "0.00"
    work: "Head of household schedule: line 38 over $0 but not over $12,800, tax is 4% of line 38; 4% × $0.00 = $0.00."
```

### classm.ny_rs.4

```yaml
lines:
  - printed: "tax"
    value: "10860.00"
    work: "Qualifying surviving spouse bracket: $8,553 + 6% × ($200,000 − $161,550) = $8,553 + $2,307 = $10,860."
```

### classm.ny_rs.5

```yaml
lines:
  - printed: "tax"
    value: "6632.00"
    work: "Married filing separately schedule: $4,271 + 6% × ($120,000 − $80,650) = $6,632.00"
```

### classm.ny_rs.6

```yaml
lines:
  - printed: "tax"
    value: "0.00"
    work: "Married filing jointly schedule: 4% of line 38; 4% × $0.00 = $0.00."
```

### classm.ny_rs.7

```yaml
lines:
  - printed: "tax"
    value: "1049.45"
    work: "MFJ bracket over $23,600 but not over $27,900: $976 + 5.25% × ($24,999 − $23,600) = $976 + $73.45 = $1,049.45."
```

### classm.ny_rs.8

```yaml
lines:
  - printed: "tax"
    value: "1126.45"
    work: "HOH bracket $20,900–$107,650: $901 + 5.5% × ($24,999 − $20,900) = $901 + $225.445 = $1,126.445, rounded to $1,126.45."
```

### classm.ny_rs.9

```yaml
lines:
  - printed: "tax"
    value: "12356.07"
    work: "Single schedule: $12,356 + 6.85% × ($215,401 − $215,400) = $12,356 + $0.0685 = $12,356.07"
```

### classm.ny_rs.10

```yaml
lines:
  - printed: "tax"
    value: "71413.10"
    work: "Single schedule: 71,413 + 9.65% × (1,077,551 − 1,077,550) = 71,413.0965, rounded to 71,413.10"
```

### classm.ny_rs.11

```yaml
lines:
  - printed: "tax"
    value: "449929.10"
    work: "Single schedule: $449,929 + 10.3% × ($5,000,001 − $5,000,000) = $449,929.103, rounded to $449,929.10"
```

### classm.ny_rs.12

```yaml
lines:
  - printed: "tax"
    value: "2618929.00"
    work: "$26,000,000 exceeds $25,000,000; tax = $2,509,929 + 10.9% × $1,000,000 = $2,618,929"
```

### classm.ny_rs.13

```yaml
lines:
  - printed: "tax"
    value: "18252.07"
    work: "MFJ bracket: $18,252 + 6.85% × ($323,201 − $323,200) = $18,252 + $0.0685 = $18,252.07"
```

### classm.ny_rs.14

```yaml
lines:
  - printed: "tax"
    value: "143754.10"
    work: "MFJ bracket over $2,155,350: $143,754 + 9.65% × ($2,155,351 − $2,155,350) = $143,754.0965, rounded to $143,754.10"
```

### classm.ny_rs.15

```yaml
lines:
  - printed: "tax"
    value: "418263.10"
    work: "MFJ schedule: 418,263 + 10.3% × (5,000,001 − 5,000,000) = 418,263.10"
```

### classm.ny_rs.16

```yaml
lines:
  - printed: "tax"
    value: "5813.00"
    work: "HOH schedule: $5,672 + 6% × ($110,000 − $107,650) = $5,672 + $141 = $5,813.00"
```

### classm.ny_rs.17

```yaml
lines:
  - printed: "tax"
    value: "15371.07"
    work: "Head of household bracket over $269,300: $15,371 + 6.85% × ($269,301 − $269,300) = $15,371.07"
```

### classm.ny_rs.18

```yaml
lines:
  - printed: "tax"
    value: "107651.10"
    work: "Head of household schedule: $107,651 + 9.65% × ($1,616,451 − $1,616,450) = $107,651.0965, rounded to $107,651.10"
```

### classm.ny_rs.19

```yaml
lines:
  - printed: "tax"
    value: "434163.10"
    work: "HOH schedule over $5,000,000: 434,163 + 10.3% × $1 = 434,163.103, rounded to 434,163.10"
```

### classm.ny_rs.20

```yaml
lines:
  - printed: "tax"
    value: "566.00"
    work: "HOH schedule: $512 + 4.5% × ($14,000 − $12,800) = $512 + $54 = $566.00"
```

### classm.ny_rs.21

```yaml
lines:
  - printed: "tax"
    value: "307.52"
    work: "Married filing separately schedule: 4% of line 38; $7,688.00 × 4% = $307.52"
```

### classm.ny_rs.22

```yaml
lines:
  - printed: "tax"
    value: "483.51"
    work: "Married filing separately bracket $8,500–$11,700: $340 + 4.5% × ($11,689 − $8,500) = $483.505, rounded to $483.51"
```

### classm.ny_rs.23

```yaml
lines:
  - printed: "tax"
    value: "588.53"
    work: "MFS schedule: $484 + 5.25% × ($13,691 − $11,700) = $484 + $104.5275 = $588.5275, rounded to $588.53."
```

### classm.ny_rs.24

```yaml
lines:
  - printed: "tax"
    value: "933.50"
    work: "MFJ schedule: $686 plus 4.5% of ($22,650 - $17,150) = $686 + $247.50 = $933.50"
```

### classm.ny_rs.25

```yaml
lines:
  - printed: "tax"
    value: "879.52"
    work: "HOH schedule: $730 + 5.25% × ($20,498 − $17,650) = $879.52"
```

### classm.ny_rs.26

```yaml
lines:
  - printed: "tax"
    value: "2532762.56"
    work: "MFJ schedule: 2,478,263 + 10.9% × (25,499,996 − 25,000,000) = 2,478,263 + 54,499.564 = 2,532,762.564, rounded to cents."
```

### classm.ny_rs.27

```yaml
lines:
  - printed: "tax"
    value: "2548662.56"
    work: "HOH bracket over $25,000,000: $2,494,163 + 10.9% × ($25,499,996 − $25,000,000) = $2,548,662.56"
```

### classm.ny_rs.28

```yaml
lines:
  - printed: "tax"
    value: "0.48"
    work: "Married filing jointly: line 38 $12.00 is over $0 but not over $17,150, so tax = 4% × $12.00 = $0.48."
```

### classm.ny_rs.29

```yaml
lines:
  - printed: "tax"
    value: "0.48"
    work: "Head of household: line 38 $12.00 is in $0–$12,800 bracket; tax = 4% × $12.00 = $0.48."
```
