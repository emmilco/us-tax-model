# Class M hand-work — ny_tcw_first

`Tax computation worksheets 1, 7 and 12 (New York AGI of more than $107,650)` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/ny/2025/classm.deepseek.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-11-05 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt policy | worked-values-request-bound-v2 |
| system sha256 | 14a5e4eb8d846a6706a317abd7af9a45f1e53937087ad30bf4e35fe555725b8e |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 1b493134793326ad92ea1fde2f3334b2135f1cfb98c8fd0c816849553b2efe61 |
| cases | 2 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| ny_it201i-html | Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny) | 1 | cited sections: Tax computation worksheet 1; Tax computation worksheet 2; Tax computation worksheet 7; Tax computation—New York adjusted gross income of more than $107,650 | 63863fe461c33d052e26a67c87d000ed70b896c72437350880a9e1c680104982 | - | - |

## Lines

### case classm.ny_tcw_first.1 — prompt sha256 ee57a3f8c7bb789ed942b3ff8c6187d20c0848248c6faa6647a2754a050d58c7; branches: stop:false, line5:positive, line6:floor, tax#1

### classm.ny_tcw_first.1 — line3 — Multiply line 2 by the flat rate
Status: **DISAGREE**

Project: $2,105.00
Model: $2,105.13
Work: 38,275.00 x 0.055 = 2,105.125, rounded to 2,105.13

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Tax computation worksheet 1, line 3, "Multiply line 2 by 5.5% (0.055)": $38,275 x 0.055: exactly $2,105.125, which the project rounds half-up to $2,105.00; the model's $2,105.13 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### classm.ny_tcw_first.1 — stop — Is the line 1 amount $157,650 or more?
Status: **AGREE**

Value: no

### classm.ny_tcw_first.1 — line4 — Enter your New York State tax on the line 2 amount from the New York State tax r
Status: **DISAGREE**

Project: $1,773.00
Model: $1,772.63
Work: MFJ schedule: 1,202 + 5.5% x (38,275 - 27,900) = 1,772.625, rounded to 1,772.63

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Tax computation worksheet 1, line 4, the New York State tax rate schedule (married filing jointly) on $38,275: $1,202 plus 5.5% of the excess over $27,900: exactly $1,772.625, which the project rounds half-up to $1,773.00; the model's $1,772.63 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### classm.ny_tcw_first.1 — line5 — Subtract line 4 from line 3
Status: **DISAGREE**

Project: $332.00
Model: $332.50
Work: 2,105.13 - 1,772.63 = 332.50

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." Tax computation worksheet 1, line 5, "Subtract line 4 from line 3": with lines 3 and 4 each rounded where computed, $2,105 - $1,773 = $332; with cents kept, $2,105.125 - $1,772.625 = $332.50; the project's $332.00 follows from lines 3 and 4 rounded where computed; the model's $332.50 from the same lines in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### classm.ny_tcw_first.1 — line6 — Enter the excess of line 1 over $107,650
Status: **AGREE**

Value: $0.00

### classm.ny_tcw_first.1 — line8 — Multiply line 5 by line 7 (whole dollars)
Status: **AGREE**

Value: $0.00

### classm.ny_tcw_first.1 — line9_phased — Add lines 4 and 8
Status: **DISAGREE**

Project: $1,773.00
Model: $1,772.63
Work: 1,772.63 + 0.00 = 1,772.63

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), line 9, lines 4 and 8 ($0, line 6 being $0): the schedule on $38,275: exactly $1,772.625, which the project rounds half-up to $1,773.00; the model's $1,772.63 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### classm.ny_tcw_first.1 — tax — Add lines 4 and 8, or, at the Stop, the line 3 amount. Enter here and on line 39
Status: **DISAGREE**

Project: $1,773.00
Model: $1,772.63
Work: no stop; line 4 + line 8 = 1,772.63

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), line 9, lines 4 and 8 ($0, line 6 being $0): the schedule on $38,275: exactly $1,772.625, which the project rounds half-up to $1,773.00; the model's $1,772.63 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### case classm.ny_tcw_first.2 — prompt sha256 c0b32585412e0e798b32f08d858d65de2e4006b4250e477a0409cd9b3294c4f9; branches: stop:false, line5:floor, line6:positive, tax#1

### classm.ny_tcw_first.2 — line3 — Multiply line 2 by the flat rate
Status: **DISAGREE**

Project: $6,600.00
Model: $7,200.00
Work: Worksheet 7 for Single: 120,000.00 × 6% = 7,200.00

Ruling: scope; the case pairs the worksheet 1 binding of ny_tcw_first (flat rate ny.tcw.first.rate, 5.5%, given to the model as "(3) The worksheet's flat rate ... 5.5%") with a single filer, a combination no return takes: IT-201 routes a single filer to worksheet 7 (forms/ny/2025/ny_it201.yaml, ny_it201.tcw.w7, rate ny.tcw.first.rate6), whose line 3 reads "Multiply line 2 by 6% (0.06)" (IT-201-I web edition, Tax computation worksheet 7). With the rate the case supplies, the definition's line is the project's (line 3 = $120,000 x 5.5% = $6,600; line 4, the single schedule on $120,000, = $4,271 + 6% x $39,350 = $6,632; line 5 = max(0, $6,600 - $6,632) = $0, so lines 8 = $0 and 9 = tax = $6,632). The model applied worksheet 7's 6% instead of the supplied rate; under 6% its figures are worksheet 7's ($7,200, $568, 0.4070, $231, $6,863), which is what IT-201 computes for this return through ny_it201.tcw.w7. Neither side is evidence for the bound definition: the job is a construction artifact of classm-jobs (instance binding chosen independently of the filing status; tooling low in research/audits/ny/BUG-0424_lows.md). Dropped from the fixture. [dropped]

### classm.ny_tcw_first.2 — stop — Is the line 1 amount $157,650 or more?
Status: **AGREE**

Value: no

### classm.ny_tcw_first.2 — line4 — Enter your New York State tax on the line 2 amount from the New York State tax r
Status: **DISAGREE**

Project: $6,632.00
Model: $6,631.75
Work: Single NYS schedule on 120,000.00 = 6,631.75

Ruling: model error (arithmetic); IT-201-I (web edition), New York State tax rate schedule, "Single and married filing separately", over $80,650 but not over $215,400: "$4,271 plus 6% of the excess over $80,650"; on $120,000 that is $4,271 + $2,361.00 = $6,632.00 exactly, the project's. The model's $6,631.75 is not the schedule on $120,000 under any rounding. Recomputed from the source, not from the engine. Dropped from the fixture as not evidence. [dropped]

### classm.ny_tcw_first.2 — line5 — Subtract line 4 from line 3
Status: **DISAGREE**

Project: $0.00
Model: $568.25
Work: 7,200.00 − 6,631.75 = 568.25

Ruling: scope; the case pairs the worksheet 1 binding of ny_tcw_first (flat rate ny.tcw.first.rate, 5.5%, given to the model as "(3) The worksheet's flat rate ... 5.5%") with a single filer, a combination no return takes: IT-201 routes a single filer to worksheet 7 (forms/ny/2025/ny_it201.yaml, ny_it201.tcw.w7, rate ny.tcw.first.rate6), whose line 3 reads "Multiply line 2 by 6% (0.06)" (IT-201-I web edition, Tax computation worksheet 7). With the rate the case supplies, the definition's line is the project's (line 3 = $120,000 x 5.5% = $6,600; line 4, the single schedule on $120,000, = $4,271 + 6% x $39,350 = $6,632; line 5 = max(0, $6,600 - $6,632) = $0, so lines 8 = $0 and 9 = tax = $6,632). The model applied worksheet 7's 6% instead of the supplied rate; under 6% its figures are worksheet 7's ($7,200, $568, 0.4070, $231, $6,863), which is what IT-201 computes for this return through ny_it201.tcw.w7. Neither side is evidence for the bound definition: the job is a construction artifact of classm-jobs (instance binding chosen independently of the filing status; tooling low in research/audits/ny/BUG-0424_lows.md). Dropped from the fixture. [dropped]

### classm.ny_tcw_first.2 — line6 — Enter the excess of line 1 over $107,650
Status: **AGREE**

Value: $20,350.00

### classm.ny_tcw_first.2 — line8 — Multiply line 5 by line 7 (whole dollars)
Status: **DISAGREE**

Project: $0.00
Model: $231.00
Work: 568.25 × 0.4070 = 231.27775, rounded to whole dollars = 231.00

Ruling: scope; the case pairs the worksheet 1 binding of ny_tcw_first (flat rate ny.tcw.first.rate, 5.5%, given to the model as "(3) The worksheet's flat rate ... 5.5%") with a single filer, a combination no return takes: IT-201 routes a single filer to worksheet 7 (forms/ny/2025/ny_it201.yaml, ny_it201.tcw.w7, rate ny.tcw.first.rate6), whose line 3 reads "Multiply line 2 by 6% (0.06)" (IT-201-I web edition, Tax computation worksheet 7). With the rate the case supplies, the definition's line is the project's (line 3 = $120,000 x 5.5% = $6,600; line 4, the single schedule on $120,000, = $4,271 + 6% x $39,350 = $6,632; line 5 = max(0, $6,600 - $6,632) = $0, so lines 8 = $0 and 9 = tax = $6,632). The model applied worksheet 7's 6% instead of the supplied rate; under 6% its figures are worksheet 7's ($7,200, $568, 0.4070, $231, $6,863), which is what IT-201 computes for this return through ny_it201.tcw.w7. Neither side is evidence for the bound definition: the job is a construction artifact of classm-jobs (instance binding chosen independently of the filing status; tooling low in research/audits/ny/BUG-0424_lows.md). Dropped from the fixture. [dropped]

### classm.ny_tcw_first.2 — line9_phased — Add lines 4 and 8
Status: **DISAGREE**

Project: $6,632.00
Model: $6,862.75
Work: 6,631.75 + 231.00 = 6,862.75

Ruling: scope; the case pairs the worksheet 1 binding of ny_tcw_first (flat rate ny.tcw.first.rate, 5.5%, given to the model as "(3) The worksheet's flat rate ... 5.5%") with a single filer, a combination no return takes: IT-201 routes a single filer to worksheet 7 (forms/ny/2025/ny_it201.yaml, ny_it201.tcw.w7, rate ny.tcw.first.rate6), whose line 3 reads "Multiply line 2 by 6% (0.06)" (IT-201-I web edition, Tax computation worksheet 7). With the rate the case supplies, the definition's line is the project's (line 3 = $120,000 x 5.5% = $6,600; line 4, the single schedule on $120,000, = $4,271 + 6% x $39,350 = $6,632; line 5 = max(0, $6,600 - $6,632) = $0, so lines 8 = $0 and 9 = tax = $6,632). The model applied worksheet 7's 6% instead of the supplied rate; under 6% its figures are worksheet 7's ($7,200, $568, 0.4070, $231, $6,863), which is what IT-201 computes for this return through ny_it201.tcw.w7. Neither side is evidence for the bound definition: the job is a construction artifact of classm-jobs (instance binding chosen independently of the filing status; tooling low in research/audits/ny/BUG-0424_lows.md). Dropped from the fixture. [dropped]

### classm.ny_tcw_first.2 — tax — Add lines 4 and 8, or, at the Stop, the line 3 amount. Enter here and on line 39
Status: **DISAGREE**

Project: $6,632.00
Model: $6,862.75
Work: No Stop; use line 4 + line 8 = 6,862.75

Ruling: scope; the case pairs the worksheet 1 binding of ny_tcw_first (flat rate ny.tcw.first.rate, 5.5%, given to the model as "(3) The worksheet's flat rate ... 5.5%") with a single filer, a combination no return takes: IT-201 routes a single filer to worksheet 7 (forms/ny/2025/ny_it201.yaml, ny_it201.tcw.w7, rate ny.tcw.first.rate6), whose line 3 reads "Multiply line 2 by 6% (0.06)" (IT-201-I web edition, Tax computation worksheet 7). With the rate the case supplies, the definition's line is the project's (line 3 = $120,000 x 5.5% = $6,600; line 4, the single schedule on $120,000, = $4,271 + 6% x $39,350 = $6,632; line 5 = max(0, $6,600 - $6,632) = $0, so lines 8 = $0 and 9 = tax = $6,632). The model applied worksheet 7's 6% instead of the supplied rate; under 6% its figures are worksheet 7's ($7,200, $568, 0.4070, $231, $6,863), which is what IT-201 computes for this return through ny_it201.tcw.w7. Neither side is evidence for the bound definition: the job is a construction artifact of classm-jobs (instance binding chosen independently of the filing status; tooling low in research/audits/ny/BUG-0424_lows.md). Dropped from the fixture. [dropped]

## Raw responses

### classm.ny_tcw_first.1

```yaml
lines:
  - printed: "line3"
    value: "2105.13"
    work: "38,275.00 x 0.055 = 2,105.125, rounded to 2,105.13"
  - printed: "stop"
    value: "no"
    work: "line 1 is 54,325.00, which is less than 157,650"
  - printed: "line4"
    value: "1772.63"
    work: "MFJ schedule: 1,202 + 5.5% x (38,275 - 27,900) = 1,772.625, rounded to 1,772.63"
  - printed: "line5"
    value: "332.50"
    work: "2,105.13 - 1,772.63 = 332.50"
  - printed: "line6"
    value: "0.00"
    work: "line 1 is below 107,650, so the nonnegative excess is 0.00"
  - printed: "line8"
    value: "0.00"
    work: "line 7 = 0 / 50,000 = 0.0000; 332.50 x 0 = 0.00"
  - printed: "line9_phased"
    value: "1772.63"
    work: "1,772.63 + 0.00 = 1,772.63"
  - printed: "tax"
    value: "1772.63"
    work: "no stop; line 4 + line 8 = 1,772.63"
```

### classm.ny_tcw_first.2

```yaml
lines:
  - printed: "line3"
    value: "7,200.00"
    work: "Worksheet 7 for Single: 120,000.00 × 6% = 7,200.00"
  - printed: "stop"
    value: "no"
    work: "Line 1 is 128,000.00, not 157,650 or more"
  - printed: "line4"
    value: "6,631.75"
    work: "Single NYS schedule on 120,000.00 = 6,631.75"
  - printed: "line5"
    value: "568.25"
    work: "7,200.00 − 6,631.75 = 568.25"
  - printed: "line6"
    value: "20,350.00"
    work: "128,000.00 − 107,650.00 = 20,350.00"
  - printed: "line8"
    value: "231.00"
    work: "568.25 × 0.4070 = 231.27775, rounded to whole dollars = 231.00"
  - printed: "line9_phased"
    value: "6,862.75"
    work: "6,631.75 + 231.00 = 6,862.75"
  - printed: "tax"
    value: "6,862.75"
    work: "No Stop; use line 4 + line 8 = 6,862.75"
```
