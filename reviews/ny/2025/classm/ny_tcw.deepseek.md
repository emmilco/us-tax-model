# Class M hand-work — ny_tcw

`Tax computation worksheets 2–5, 8–10, 13–15 (New York AGI of more than $107,650)` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/ny/2025/classm.deepseek.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-11-05 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt policy | worked-values-request-bound-v2 |
| system sha256 | 14a5e4eb8d846a6706a317abd7af9a45f1e53937087ad30bf4e35fe555725b8e |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | e300036124ef29f704b3082a7b9d4a0eb23bc96d6c20130f91827a9e54ce8283 |
| cases | 2 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| ny_it201i-html | Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny) | 1 | cited sections: Tax computation worksheet 2; Tax computation—New York adjusted gross income of more than $107,650 | 63863fe461c33d052e26a67c87d000ed70b896c72437350880a9e1c680104982 | - | - |

## Lines

### case classm.ny_tcw.1 — prompt sha256 f529258fd381e9fb01ea7ef9d0aaf5c02f40fc33f4f38386b77dcc2f02166174; branches: line6:floor, line7:left

### classm.ny_tcw.1 — line3 — Enter your New York State tax on the line 2 amount from the New York State tax r
Status: **DISAGREE**

Project: $1,773.00
Model: $1,772.63
Work: MFJ schedule: $1,202 + 5.5% × ($38,275 − $27,900) = $1,772.63

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), Tax computation worksheet 2, line 3, the New York State tax rate schedule (married filing jointly) on $38,275: $1,202 plus 5.5% of the excess over $27,900: exactly $1,772.625, which the project rounds half-up to $1,773.00; the model's $1,772.63 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### classm.ny_tcw.1 — line6 — Enter the excess of line 1 over the worksheet's amount
Status: **AGREE**

Value: $0.00

### classm.ny_tcw.1 — line7 — Enter the lesser of line 6 or $50,000
Status: **AGREE**

Value: $0.00

### classm.ny_tcw.1 — line9 — Multiply line 5 by line 8 (whole dollars)
Status: **AGREE**

Value: $0.00

### classm.ny_tcw.1 — tax — Add lines 3, 4, and 9. Enter here and on line 39.
Status: **DISAGREE**

Project: $2,106.00
Model: $2,105.63
Work: $1,772.63 + $333.00 + $0.00 = $2,105.63

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." Tax computation worksheet 2, line 10 (tax), "Add lines 3, 4, and 9": $1,773 (line 3 rounded where computed, $1,772.625 exactly) + $333 + $0 (line 1 does not exceed $161,550) = $2,106, the project's; the model's $2,105.63 adds line 3 in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### case classm.ny_tcw.2 — prompt sha256 23f42a884eb962f20fc2231ab35154fe215de4e077f2e11620ac893762948308; branches: line6:positive, line7:right

### classm.ny_tcw.2 — line3 — Enter your New York State tax on the line 2 amount from the New York State tax r
Status: **DISAGREE**

Project: $12,356.00
Model: $11,784.00
Work: MFJ tax rate schedule on $215,400 = $11,784.00

Ruling: scope; the case pairs the worksheet 2 binding of ny_tcw (the married-filing-jointly amounts: line 1 excess measured over $161,550, Recapture Base $333, Incremental Benefit $807, ny.tcw.mfj.w2.*) with a single filer, a combination no return takes (IT-201 routes single filers to worksheets 7 to 10). Line 3 is "Enter your New York State tax on the line 2 amount from the New York State tax rate schedule", which the definition reads for the case's filing status: the single schedule on $215,400 is $4,271 + 6% x $134,750 = $12,356 (IT-201-I web edition, New York State tax rate schedule, "Single and married filing separately"), and tax = $12,356 + $333 + $807 x 1.0000 = $13,496, the project's. The model read the worksheet as worksheet 2 and took the joint schedule ($8,553 + 6% x $53,850 = $11,784; tax $12,924), right for a joint filer. Neither side is evidence for the bound definition: the job is a construction artifact of classm-jobs (instance binding chosen independently of the filing status; tooling low in research/audits/ny/BUG-0424_lows.md). Dropped from the fixture. [dropped]

### classm.ny_tcw.2 — line6 — Enter the excess of line 1 over the worksheet's amount
Status: **AGREE**

Value: $61,850.00

### classm.ny_tcw.2 — line7 — Enter the lesser of line 6 or $50,000
Status: **AGREE**

Value: $50,000.00

### classm.ny_tcw.2 — line9 — Multiply line 5 by line 8 (whole dollars)
Status: **AGREE**

Value: $807.00

### classm.ny_tcw.2 — tax — Add lines 3, 4, and 9. Enter here and on line 39.
Status: **DISAGREE**

Project: $13,496.00
Model: $12,924.00
Work: 11,784 + 333 + 807 = 12,924

Ruling: scope; the case pairs the worksheet 2 binding of ny_tcw (the married-filing-jointly amounts: line 1 excess measured over $161,550, Recapture Base $333, Incremental Benefit $807, ny.tcw.mfj.w2.*) with a single filer, a combination no return takes (IT-201 routes single filers to worksheets 7 to 10). Line 3 is "Enter your New York State tax on the line 2 amount from the New York State tax rate schedule", which the definition reads for the case's filing status: the single schedule on $215,400 is $4,271 + 6% x $134,750 = $12,356 (IT-201-I web edition, New York State tax rate schedule, "Single and married filing separately"), and tax = $12,356 + $333 + $807 x 1.0000 = $13,496, the project's. The model read the worksheet as worksheet 2 and took the joint schedule ($8,553 + 6% x $53,850 = $11,784; tax $12,924), right for a joint filer. Neither side is evidence for the bound definition: the job is a construction artifact of classm-jobs (instance binding chosen independently of the filing status; tooling low in research/audits/ny/BUG-0424_lows.md). Dropped from the fixture. [dropped]

## Raw responses

### classm.ny_tcw.1

```yaml
lines:
  - printed: "line3"
    value: "1772.63"
    work: "MFJ schedule: $1,202 + 5.5% × ($38,275 − $27,900) = $1,772.63"
  - printed: "line6"
    value: "0.00"
    work: "$54,325 − $161,550 = -$107,225, so excess is 0.00"
  - printed: "line7"
    value: "0.00"
    work: "Lesser of line 6 ($0.00) or $50,000 = 0.00"
  - printed: "line9"
    value: "0.00"
    work: "$807 × (0.00 / $50,000 = 0.0000) = 0.00"
  - printed: "tax"
    value: "2105.63"
    work: "$1,772.63 + $333.00 + $0.00 = $2,105.63"
```

### classm.ny_tcw.2

```yaml
lines:
  - printed: "line3"
    value: "11784.00"
    work: "MFJ tax rate schedule on $215,400 = $11,784.00"
  - printed: "line6"
    value: "61850.00"
    work: "223,400 - 161,550 = 61,850"
  - printed: "line7"
    value: "50000.00"
    work: "lesser of 61,850 or 50,000 = 50,000"
  - printed: "line9"
    value: "807.00"
    work: "807 × (50,000 / 50,000) = 807"
  - printed: "tax"
    value: "12924.00"
    work: "11,784 + 333 + 807 = 12,924"
```
