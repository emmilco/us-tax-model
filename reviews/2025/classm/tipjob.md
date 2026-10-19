# Class M hand-work — tipjob

`Qualified Tips From More Than One Employer Worksheet (Schedule 1-A, line 4c) — one row per employer` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-18 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| cases | 1 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 101, 102, 103, 104 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 101, 102, 103, 104 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### case classm.tipjob.1 — prompt sha256 091dca640be4c09d58b7eea8a4e5dc54f7b479eef1197ddd433a7863c4a44ffd; branches: tipjob.qualified:true, tipjob.mixed:false, tipjob.col_d:left

### classm.tipjob.1 — tipjob[tip_1].mixed — Some of this employer's tips are not qualified tips
Status: **AGREE**

Value: no

### classm.tipjob.1 — tipjob[tip_1].col_d — Enter the greater of column (b) or column (c)
Status: **AGREE**

Value: $30,000.00

### classm.tipjob.1 — tipjob[tip_2].mixed — Some of this employer's tips are not qualified tips
Status: **AGREE**

Value: no

### classm.tipjob.1 — tipjob[tip_2].col_d — Enter the greater of column (b) or column (c)
Status: **AGREE**

Value: $0.00

## Raw responses

### classm.tipjob.1

```yaml
lines:
  - printed: "tipjob[tip_1].mixed"
    value: "no"
    work: "Filer answered yes: all tips from this employer meet the qualified-tip tests, so none are non-qualified"
  - printed: "tipjob[tip_1].col_d"
    value: "30000.00"
    work: "Greater of col (b) 30,000.00 or col (c) 0.00 (no Form 4137 amount given) = 30,000.00"
  - printed: "tipjob[tip_2].mixed"
    value: "no"
    work: "Filer answered yes: all tips from this employer meet the qualified-tip tests, so none are non-qualified"
  - printed: "tipjob[tip_2].col_d"
    value: "0.00"
    work: "Greater of col (b) 0.00 or col (c) 0.00 (no Form 4137 amount given) = 0.00"
```
