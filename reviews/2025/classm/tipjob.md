# Class M hand-work — tipjob

`Qualified Tips From More Than One Employer Worksheet (Schedule 1-A, line 4c) — one row per employer` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-19 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| cases | 1 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 101, 102, 103, 104 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 101, 102, 103, 104 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### case classm.tipjob.1 — prompt sha256 dcdaae5ccfff8be28ce8781270fbbd0286848d307ad1782f22d8777f34cff6f7; branches: tipjob.qualified:true, tipjob.mixed:false, tipjob.col_d:left

### classm.tipjob.1 — person[taxpayer].tipjob[tip_1].mixed — Some of this employer's tips are not qualified tips
Status: **AGREE**

Value: no

### classm.tipjob.1 — person[taxpayer].tipjob[tip_1].col_d — Enter the greater of column (b) or column (c)
Status: **AGREE**

Value: $25,295.00

### classm.tipjob.1 — person[taxpayer].tipjob[tip_2].mixed — Some of this employer's tips are not qualified tips
Status: **AGREE**

Value: no

### classm.tipjob.1 — person[taxpayer].tipjob[tip_2].col_d — Enter the greater of column (b) or column (c)
Status: **AGREE**

Value: $0.00

### classm.tipjob.1 — person[taxpayer].tipjob[tip_3].mixed — Some of this employer's tips are not qualified tips
Status: **AGREE**

Value: no

### classm.tipjob.1 — person[taxpayer].tipjob[tip_3].col_d — Enter the greater of column (b) or column (c)
Status: **AGREE**

Value: $1,480.00

## Raw responses

### classm.tipjob.1

```yaml
```yaml
lines:
  - printed: "person[taxpayer].tipjob[tip_1].mixed"
    value: "no"
    work: "Filer answered yes: all tips counted from this employer meet the qualified-tip tests, so none are non-qualified."
  - printed: "person[taxpayer].tipjob[tip_1].col_d"
    value: "25295.00"
    work: "Greater of col (b) 25,295.00 or col (c) 0.00 (no Form 4137 amount given) = 25,295.00. The MFS bar applies on Schedule 1-A, not on this worksheet."
  - printed: "person[taxpayer].tipjob[tip_2].mixed"
    value: "no"
    work: "Filer answered yes: all tips counted from this employer meet the qualified-tip tests, so none are non-qualified."
  - printed: "person[taxpayer].tipjob[tip_2].col_d"
    value: "0.00"
    work: "Greater of col (b) 0.00 or col (c) 0.00 = 0.00."
  - printed: "person[taxpayer].tipjob[tip_3].mixed"
    value: "no"
    work: "Filer answered yes: all tips counted from this employer meet the qualified-tip tests, so none are non-qualified."
  - printed: "person[taxpayer].tipjob[tip_3].col_d"
    value: "1480.00"
    work: "Greater of col (b) 1,480.00 or col (c) 0.00 = 1,480.00."
```
```
