# Class M hand-work — aqee

`Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-29 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt policy | worked-values-request-bound-v2 |
| system sha256 | 18ff9cfe094eedd0548bba02012b0ebf2a58d0606e834e3633432585b4192cb7 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | de4e8263156206529532493e4a29fd509c7e0cf2c9770de758f0a64796a51930 |
| cases | 2 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8863 | 2025 | 3, 4, 9 | cited pages | 71d45c0b03b4521697e7f4fd52bbcc489d7dac6a3645b6d36f514ae5992e2e4d | 3, 4, 9 | 6d486b4afb1f1647b7b99243cde905cf9def6b2813e5ed0bcb9925329c1e8a2b |
| f8863 | 2025 | 1, 2 | whole document | 8e2a766019b69e75af71e8da04f82a27534acb97f9ae4c2b72438a56d10d444e | - | 37bbeebd24c238e54a031ab21ac880feb5d8e9ce98f792e1b45d93e1bf8abc6c |

## Lines

### case classm.aqee.1 — prompt sha256 a3d40bb7f0f2c8deaf4b7743570830a7017e747899dfe9e0cef42d468f47e09e; branches: ws4_aoc:positive, line27:right, line28:positive, line28_zero:false, line30#1

### classm.aqee.1 — line27 — Adjusted qualified education expenses. Don't enter more than $4,000
Status: **AGREE**

Value: $4,000.00

### classm.aqee.1 — line28 — Subtract $2,000 from line 27. If zero or less, enter -0-
Status: **AGREE**

Value: $2,000.00

### classm.aqee.1 — line29 — Multiply line 28 by 25% (0.25)
Status: **AGREE**

Value: $500.00

### classm.aqee.1 — line28_zero — Line 28 is zero
Status: **AGREE**

Value: no

### classm.aqee.1 — line30 — If line 28 is zero, enter the amount from line 27. Otherwise, add $2,000 to the
Status: **AGREE**

Value: $2,500.00

### case classm.aqee.2 — prompt sha256 0dd6318b135df14b374ce6b8dfa8eac4920d1f2f9b9ce37e133578380999a756; branches: ws4_aoc:floor, line27:left, line28:floor, line28_zero:true, line30#0

### classm.aqee.2 — line27 — Adjusted qualified education expenses. Don't enter more than $4,000
Status: **AGREE**

Value: $0.00

### classm.aqee.2 — line28 — Subtract $2,000 from line 27. If zero or less, enter -0-
Status: **AGREE**

Value: $0.00

### classm.aqee.2 — line29 — Multiply line 28 by 25% (0.25)
Status: **AGREE**

Value: $0.00

### classm.aqee.2 — line28_zero — Line 28 is zero
Status: **AGREE**

Value: yes

### classm.aqee.2 — line30 — If line 28 is zero, enter the amount from line 27. Otherwise, add $2,000 to the
Status: **AGREE**

Value: $0.00

## Raw responses

### classm.aqee.1

```yaml
```yaml
lines:
  - printed: "line27"
    value: "4000.00"
    work: "Worksheet: 4,578 + 1,042 course materials (AOC) = 5,620 - 0 = 5,620; capped at $4,000"
  - printed: "line28"
    value: "2000.00"
    work: "4,000 - 2,000 = 2,000"
  - printed: "line29"
    value: "500.00"
    work: "2,000 x 0.25 = 500"
  - printed: "line28_zero"
    value: "no"
    work: "Line 28 is 2,000, not zero"
  - printed: "line30"
    value: "2500.00"
    work: "Line 28 not zero: 500 + 2,000 = 2,500"
```
```

### classm.aqee.2

```yaml
lines:
  - printed: "line27"
    value: "0.00"
    work: "Worksheet line 1 $5,000.00 + $0.00 = $5,000.00; line 4 = $5,000.00 - $5,000.00 = $0.00; not more than $4,000"
  - printed: "line28"
    value: "0.00"
    work: "$0.00 - $2,000 is zero or less, so enter -0-"
  - printed: "line29"
    value: "0.00"
    work: "$0.00 x 0.25 = $0.00"
  - printed: "line28_zero"
    value: "yes"
    work: "Line 28 is $0.00"
  - printed: "line30"
    value: "0.00"
    work: "Line 28 is zero, so enter line 27, $0.00"
```
