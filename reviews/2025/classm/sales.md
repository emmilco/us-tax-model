# Class M hand-work — sales

`Form 8949 and Schedule D — manually classified securities transactions` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| cases | 1 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8949 | 2025; printed date 2026-01-20 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 | cited pages | d3ddc2b91cf89087ca348ebb00dbd1c80bbc025fa4df1176753d25013f581a67 | 2, 3, 4, 5, 6, 7, 9, 10 | cabdc81a0677c0e4de4a89f9a71d328395c4cc839206ebadb56aeb54bf954b85 |
| i1040sd | 2025; printed date 2025-12-11 | 10, 11, 12 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 11, 12 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| f8949 | 2025; created 2025-05-05 | 1, 2 | whole document | f191f96ca2847b4c59875d5e1169f784a79b4d57f1f12d0196bd9bc2e7838e9d | - | cc308c3ff7751456647bed9c2855d077dcbd0a55469b57f9e8cccb6f4927f232 |

## Lines

### case classm.sales.1 — prompt sha256 7fdc6a9376433a5cd00a8858b63137fa9bf2ba0cdac4637c42566fb998867442; branches: sales.special:false, sales.aggregate_eligible:true, sales.covered:false, sales.covered:true, sales.digital:false, sales.has_b:false, sales.has_b:true, sales.has_w:false, sales.has_w:true, sales.bad_code:false, sales.bad_aggregate:false, sales.e#0, sales.e#1, sales.adjust_b:false, sales.adjust_b:true, sales.b#0, sales.b#1, sales.w#0, sales.w#1

### classm.sales.1 — sales[s1].covered — Basis reported to IRS
Status: **AGREE**

Value: yes

### classm.sales.1 — sales[s1].digital — Digital asset box G–L
Status: **AGREE**

Value: no

### classm.sales.1 — sales[s1].has_b — Basis correction code B applies
Status: **AGREE**

Value: yes

### classm.sales.1 — sales[s1].has_w — Wash-sale code W applies
Status: **AGREE**

Value: yes

### classm.sales.1 — sales[s1].bad_code — Unsupported adjustment or code B without a broker basis report
Status: **AGREE**

Value: no

### classm.sales.1 — sales[s1].bad_aggregate — Aggregate route fails its eligibility conditions
Status: **AGREE**

Value: no

### classm.sales.1 — sales[s1].e — Column (e): reported basis if covered; correct basis otherwise
Status: **AGREE**

Value: $3,312.00

### classm.sales.1 — sales[s1].b_difference — Reported basis minus correct basis
Status: **AGREE**

Value: $-83,515.00

### classm.sales.1 — sales[s1].adjust_b — Correct reported basis in column (g)
Status: **AGREE**

Value: yes

### classm.sales.1 — sales[s1].b — Basis correction in column (g)
Status: **AGREE**

Value: $-83,515.00

### classm.sales.1 — sales[s1].w — Wash-sale adjustment in column (g)
Status: **AGREE**

Value: $214.00

### classm.sales.1 — sales[s1].g — Column (g): net adjustments
Status: **AGREE**

Value: $-83,301.00

### classm.sales.1 — sales[s1].before_adjustment — Proceeds less column (e)
Status: **AGREE**

Value: $42,540.00

### classm.sales.1 — sales[s1].h — Column (h): proceeds less basis plus adjustments
Status: **AGREE**

Value: $-40,761.00

### classm.sales.1 — sales[s2].covered — Basis reported to IRS
Status: **AGREE**

Value: yes

### classm.sales.1 — sales[s2].digital — Digital asset box G–L
Status: **AGREE**

Value: no

### classm.sales.1 — sales[s2].has_b — Basis correction code B applies
Status: **AGREE**

Value: no

### classm.sales.1 — sales[s2].has_w — Wash-sale code W applies
Status: **AGREE**

Value: no

### classm.sales.1 — sales[s2].bad_code — Unsupported adjustment or code B without a broker basis report
Status: **AGREE**

Value: no

### classm.sales.1 — sales[s2].bad_aggregate — Aggregate route fails its eligibility conditions
Status: **AGREE**

Value: no

### classm.sales.1 — sales[s2].e — Column (e): reported basis if covered; correct basis otherwise
Status: **AGREE**

Value: $64,748.00

### classm.sales.1 — sales[s2].adjust_b — Correct reported basis in column (g)
Status: **AGREE**

Value: no

### classm.sales.1 — sales[s2].b — Basis correction in column (g)
Status: **AGREE**

Value: $0.00

### classm.sales.1 — sales[s2].w — Wash-sale adjustment in column (g)
Status: **AGREE**

Value: $0.00

### classm.sales.1 — sales[s2].g — Column (g): net adjustments
Status: **AGREE**

Value: $0.00

### classm.sales.1 — sales[s2].before_adjustment — Proceeds less column (e)
Status: **AGREE**

Value: $-60,028.00

### classm.sales.1 — sales[s2].h — Column (h): proceeds less basis plus adjustments
Status: **AGREE**

Value: $-60,028.00

### classm.sales.1 — sales[s3].covered — Basis reported to IRS
Status: **AGREE**

Value: no

### classm.sales.1 — sales[s3].digital — Digital asset box G–L
Status: **AGREE**

Value: no

### classm.sales.1 — sales[s3].has_b — Basis correction code B applies
Status: **AGREE**

Value: no

### classm.sales.1 — sales[s3].has_w — Wash-sale code W applies
Status: **AGREE**

Value: no

### classm.sales.1 — sales[s3].bad_code — Unsupported adjustment or code B without a broker basis report
Status: **AGREE**

Value: no

### classm.sales.1 — sales[s3].bad_aggregate — Aggregate route fails its eligibility conditions
Status: **AGREE**

Value: no

### classm.sales.1 — sales[s3].e — Column (e): reported basis if covered; correct basis otherwise
Status: **AGREE**

Value: $16,567.00

### classm.sales.1 — sales[s3].adjust_b — Correct reported basis in column (g)
Status: **AGREE**

Value: no

### classm.sales.1 — sales[s3].b — Basis correction in column (g)
Status: **AGREE**

Value: $0.00

### classm.sales.1 — sales[s3].w — Wash-sale adjustment in column (g)
Status: **AGREE**

Value: $0.00

### classm.sales.1 — sales[s3].g — Column (g): net adjustments
Status: **AGREE**

Value: $0.00

### classm.sales.1 — sales[s3].before_adjustment — Proceeds less column (e)
Status: **AGREE**

Value: $-16,567.00

### classm.sales.1 — sales[s3].h — Column (h): proceeds less basis plus adjustments
Status: **AGREE**

Value: $-16,567.00

## Raw responses

### classm.sales.1

```yaml
```yaml
lines:
  - printed: "sales[s1].covered"
    value: "yes"
    work: "Box D is a long-term sale reported on Form 1099-B with basis reported to the IRS"
  - printed: "sales[s1].digital"
    value: "no"
    work: "Box D is not one of the digital asset boxes G–L"
  - printed: "sales[s1].has_b"
    value: "yes"
    work: "Code BW includes B"
  - printed: "sales[s1].has_w"
    value: "yes"
    work: "Code BW includes W"
  - printed: "sales[s1].bad_code"
    value: "no"
    work: "Codes B and W are supported; B has a broker basis report ($3,312.00) in box D"
  - printed: "sales[s1].bad_aggregate"
    value: "no"
    work: "Detail route was chosen, so the aggregate conditions are not tested"
  - printed: "sales[s1].e"
    value: "3312.00"
    work: "Covered security: column (e) is the reported basis of $3,312.00"
  - printed: "sales[s1].b_difference"
    value: "-83515.00"
    work: "3,312.00 - 86,827.00"
  - printed: "sales[s1].adjust_b"
    value: "yes"
    work: "Box D with code B: correct the basis in column (g)"
  - printed: "sales[s1].b"
    value: "-83515.00"
    work: "Worksheet line 2 > line 1, so line 3 = 83,515.00, entered as a negative"
  - printed: "sales[s1].w"
    value: "214.00"
    work: "Code W: nondeductible wash-sale loss entered as a positive number"
  - printed: "sales[s1].g"
    value: "-83301.00"
    work: "-83,515.00 + 214.00"
  - printed: "sales[s1].before_adjustment"
    value: "42540.00"
    work: "45,852.00 - 3,312.00"
  - printed: "sales[s1].h"
    value: "-40761.00"
    work: "42,540.00 + (-83,301.00)"
  - printed: "sales[s2].covered"
    value: "yes"
    work: "Box A: basis reported to the IRS"
  - printed: "sales[s2].digital"
    value: "no"
    work: "Box A is not one of the digital asset boxes G–L"
  - printed: "sales[s2].has_b"
    value: "no"
    work: "Code is none"
  - printed: "sales[s2].has_w"
    value: "no"
    work: "Code is none"
  - printed: "sales[s2].bad_code"
    value: "no"
    work: "No codes entered"
  - printed: "sales[s2].bad_aggregate"
    value: "no"
    work: "Covered box A, no codes, not collectibles, all Exception 1 conditions confirmed"
  - printed: "sales[s2].e"
    value: "64748.00"
    work: "Covered security: column (e) is the reported basis"
  - printed: "sales[s2].adjust_b"
    value: "no"
    work: "No code B"
  - printed: "sales[s2].b"
    value: "0.00"
    work: "No basis correction"
  - printed: "sales[s2].w"
    value: "0.00"
    work: "No code W"
  - printed: "sales[s2].g"
    value: "0.00"
    work: "No adjustments"
  - printed: "sales[s2].before_adjustment"
    value: "-60028.00"
    work: "4,720.00 - 64,748.00"
  - printed: "sales[s2].h"
    value: "-60028.00"
    work: "-60,028.00 + 0.00"
  - printed: "sales[s3].covered"
    value: "no"
    work: "Box F: not reported to the taxpayer on Form 1099-B"
  - printed: "sales[s3].digital"
    value: "no"
    work: "Box F is not one of the digital asset boxes G–L"
  - printed: "sales[s3].has_b"
    value: "no"
    work: "Code is none"
  - printed: "sales[s3].has_w"
    value: "no"
    work: "Code is none"
  - printed: "sales[s3].bad_code"
    value: "no"
    work: "No codes entered"
  - printed: "sales[s3].bad_aggregate"
    value: "no"
    work: "Detail route was chosen"
  - printed: "sales[s3].e"
    value: "16567.00"
    work: "Not covered: column (e) is the correct basis"
  - printed: "sales[s3].adjust_b"
    value: "no"
    work: "Not box A, D, G or J, and no code B"
  - printed: "sales[s3].b"
    value: "0.00"
    work: "No basis correction"
  - printed: "sales[s3].w"
    value: "0.00"
    work: "No code W"
  - printed: "sales[s3].g"
    value: "0.00"
    work: "No adjustments"
  - printed: "sales[s3].before_adjustment"
    value: "-16567.00"
    work: "0.00 - 16,567.00"
  - printed: "sales[s3].h"
    value: "-16567.00"
    work: "-16,567.00 + 0.00"
```
```
