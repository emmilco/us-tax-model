# Transcription agreement — sa

Second transcription of `Schedule A — supported itemized deductions and standard comparison` by an isolated model (spec 6.5), compared line by line with `forms/2025/sa.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 08e88334b8c8b8832bc75e1375f87972f3935f6b44b50bad13b5e7ea233654df |
| subject sha256 | 36ce1c616030dac40534df9ae79be1177c7f0735aa1a3be78fd26fcb9b1ca301 |
| printed lines compared | 22 |
| agree / disagree / missing | 17 / 5 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040gi | 2025; printed date 2026-02-25 | 33, 34, 35 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 33, 34 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i1040sca | 2025; printed date 2025-12-08 | 7, 11 | cited pages | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | 11 | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
| p525 | 2025 | 33 | pages named by another document's citation | 7df495537860edb313c70301e591c2a0775567fab771e3d5f9bbb0cbccb69182 | 33 | 27f9e8c0836aae6360658725d1b0db69ecaf91bfa77998e1637b51f92b18df65 |

## Lines

### sa.age65 — Were you born before January 2, 1961?
Status: **DISAGREE**

Project:

```json
{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}], "test": "lt"}
```

Second:

```json
{"args": [{"const": 1}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}], "test": "le"}
```

Second transcription's note: Taken from your own person entry (person.age65), so the question is not asked twice.

Ruling: equivalent; project retained. Both test whether your own person entry answers yes to born before January 2, 1961: the project as a count above zero, the second as a count of at least one; a count is a whole number, so the tests agree (i1040gi p. 33, Line 12d, "If you or your spouse (if you are married and filing a joint return) were born before January 2, 1961").

### sa.agi — Form 1040 line 11b adjusted gross income
Status: **AGREE**

### sa.itemizes — Itemize if elected, required, or itemized total exceeds standard
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}
```

Second:

```json
{"args": [{"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}
```

Second transcription's note: 'Take the larger of your standard deduction or itemized deductions' does not say what to do when they are equal. Chosen: itemize only when line 17 is strictly larger, unless you elect to itemize or are required to. The deduction is the same either way.

Ruling: scope; project retained. After the fix of BUG-0084 both transcriptions count the age box only for a person who did not die in 2025 before reaching 65 (i1040gi p. 33, Line 12d, Death of spouse in 2025; p501 p. 23). The one difference left is the spouse-itemizes condition for married filing separately, which the project carries and the second omits; married filing separately is refused (s3.mfs), as ruled before. The tie (line 17 equal to the standard deduction) gives the same deduction either way, as the second's note says.

### sa.deduction — Deduction selected for Form 1040 line 12e
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, {"args": [{"line": "17"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}], "test": "le"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}, "then": {"line": "17"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"line": "17"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}], "test": "le"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": false}, {"ref": "person.died_before_65"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}], "test": "all"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}, {"guard": {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}, {"line": "17"}], "test": "lt"}], "test": "any"}, "then": {"line": "17"}}], "op": "choose"}
```

Ruling: scope; project retained. After the fix of BUG-0084 both transcriptions count the age box only for a person who did not die in 2025 before reaching 65 (i1040gi p. 33, Line 12d, Death of spouse in 2025; p501 p. 23). The one difference left is the spouse-itemizes condition for married filing separately (the project's standard deduction is zero when the spouse itemizes on a separate return), which the second omits; married filing separately is refused (s3.mfs), as ruled before.

### 2 — Amount from sa.agi
Status: **AGREE**

### 3 — Multiply sa.line2 by sa.medical_rate
Status: **AGREE**

### 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **AGREE**

### 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **AGREE**

### 5e — Smaller of sa.line5d, sa.saltlimit
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "5d"}, {"alternatives": [{"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"amount": {"of": [{"from": {"param": "sa.salt_base"}, "op": "subtract_floor0", "take": {"amount": {"from": {"ref": "f1040.line11b"}, "op": "subtract_floor0", "take": {"param": "sa.salt_threshold"}}, "op": "multiply_rate", "rate": {"param": "sa.salt_rate"}}}, {"param": "sa.salt_floor"}], "op": "larger_of"}, "op": "multiply_rate", "rate": {"param": "sa.half"}}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"of": [{"from": {"param": "sa.salt_base"}, "op": "subtract_floor0", "take": {"amount": {"from": {"ref": "f1040.line11b"}, "op": "subtract_floor0", "take": {"param": "sa.salt_threshold"}}, "op": "multiply_rate", "rate": {"param": "sa.salt_rate"}}}, {"param": "sa.salt_floor"}], "op": "larger_of"}}], "op": "choose"}], "op": "smaller_of"}
```

Second:

```json
{"of": [{"line": "5d"}, {"alternatives": [{"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"amount": {"of": [{"from": {"param": "sa.salt_base"}, "op": "subtract", "take": {"amount": {"from": {"ref": "f1040.line11b"}, "op": "subtract_floor0", "take": {"param": "sa.salt_threshold"}}, "op": "multiply_rate", "rate": {"param": "sa.salt_rate"}}}, {"param": "sa.salt_floor"}], "op": "larger_of"}, "op": "multiply_rate", "rate": {"param": "sa.half"}}}, {"guard": {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, "then": {"of": [{"from": {"param": "sa.salt_base"}, "op": "subtract", "take": {"amount": {"from": {"ref": "f1040.line11b"}, "op": "subtract_floor0", "take": {"param": "sa.salt_threshold"}}, "op": "multiply_rate", "rate": {"param": "sa.salt_rate"}}}, {"param": "sa.salt_floor"}], "op": "larger_of"}}], "op": "choose"}], "op": "smaller_of"}
```

Second transcription's note: Both the printed rule (AGI of $500,000 or less) and the State and Local Tax Deduction Worksheet (including its 'Before you begin' shortcut) are covered by line 10 of the worksheet: the smaller of line 5d and line 9 (half of line 9 if married filing separately). When line 6 of the worksheet is No, line 9 is $40,000, which gives the printed $40,000/$20,000 limit.

Ruling: equivalent representation; project retained. The second transcription applies the State and Local Tax Deduction Worksheet only when modified AGI exceeds $500,000 or income was excluded, and otherwise takes the $40,000 base directly; the project computes the worksheet unconditionally, where the reduction is zero at or below the threshold and the excluded-income case is refused (`sa.excluded_income`). Same value within scope (i1040sca p. 7).

### 6 — Amount from sa.zero
Status: **AGREE**

### 8b — Amount from sa.zero
Status: **AGREE**

### 8c — Amount from sa.zero
Status: **AGREE**

### 13 — Amount from sa.zero
Status: **AGREE**

### 15 — Amount from sa.zero
Status: **AGREE**

### 16 — Other—from list in instructions. List type and amount:
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"input": "s1.gambling_winnings"}, {"param": "sales.zero"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"param": "sales.zero"}, {"input": "s1.gambling_winnings"}], "test": "lt"}, "then": {"of": [{"input": "sa.gambling_losses"}, {"ref": "s1.line8b"}], "op": "smaller_of"}}], "op": "choose"}
```

Second:

```json
{"of": [{"input": "sa.gambling_losses"}, {"ref": "s1.line8b"}], "op": "smaller_of"}
```

Second transcription's note: Only gambling losses are computed: 'Gambling losses ... but only to the extent of gambling winnings reported on Schedule 1 (Form 1040), line 8b.' Every other item on the line 16 list, and a net qualified disaster loss, is screened out by sa.unsupported.

Ruling: equivalent; project retained. With no gambling winnings line 8b is zero, so the smaller of the losses and line 8b is zero, which the project writes as an explicit zero; with winnings both give the losses up to line 8b (i1040sca p. 11, Other Itemized Deductions, "Gambling losses ... but only to the extent of gambling winnings reported on Schedule 1 (Form 1040), line 8b"; decision D14). The project's guard asks the losses only of a filer with winnings.

### 7 — Add sa.line5e, sa.line6
Status: **AGREE**

### 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **AGREE**

### 9 — Amount from f4952.line8
Status: **AGREE**

### 10 — Add sa.line8e, sa.line9
Status: **AGREE**

### 12 — Total supported noncash donations before income limits
Status: **AGREE**

### 14 — Add sa.line11, sa.line12, sa.line13
Status: **AGREE**

### 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| sa.itemizes | sa.charity_limited, sa.dependent, sa.excluded_income, sa.spouse_extra, sa.unsupported | sa.spouse_extra |
| sa.deduction | sa.charity_limited, sa.dependent, sa.excluded_income, sa.spouse_extra, sa.unsupported | sa.spouse_extra |
| 5e | sa.excluded_income | - |
| 6 | sa.unsupported | - |
| 8b | sa.unsupported | - |
| 8c | sa.unsupported | - |
| 13 | sa.charity_limited | - |
| 15 | sa.unsupported | - |
| 16 | sa.unsupported | - |
| 7 | sa.excluded_income, sa.unsupported | - |
| 8e | sa.unsupported | - |
| 10 | sa.unsupported | - |
| 12 | sa.charity_limited | - |
| 14 | sa.charity_limited | - |
| 17 | sa.charity_limited, sa.excluded_income, sa.unsupported | - |

## Raw second transcription

```yaml
```yaml
lines:
  - id: sa.line2
    printed: "2"
    label: "Enter amount from Form 1040 or 1040-SR, line 11b"
    type: Dollars
    expr: {op: copy, from: sa.agi}
  - id: sa.line3
    printed: "3"
    label: "Multiply line 2 by 7.5% (0.075)"
    type: Dollars
    expr: {op: multiply_rate, amount: sa.line2, rate: {param: sa.medical_rate}}
    note: "Open: the text does not say what to do if line 2 (adjusted gross income) is negative. Chosen: the literal reading, so line 3 is line 2 times 7.5% with no floor at zero."
  - id: sa.line4
    printed: "4"
    label: "Subtract line 3 from line 1. If line 3 is more than line 1, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sa.line1, take: sa.line3}
  - id: sa.line5d
    printed: "5d"
    label: "Add lines 5a through 5c"
    type: NonNegDollars
    expr: {op: sum, of: [sa.line5a, sa.line5b, sa.line5c]}
  - id: sa.line5e
    printed: "5e"
    label: "Enter the smaller of line 5d or $40,000 ($20,000 if married filing separately). If Form 1040 or 1040-SR, line 11b is more than $500,000 ($250,000 if married filing separately), or if you completed Form 2555, Form 4563, or excluded income from Puerto Rico, see instructions"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sa.line5d, sa.saltlimit]}
    note: "Both the printed rule (AGI of $500,000 or less) and the State and Local Tax Deduction Worksheet (including its 'Before you begin' shortcut) are covered by line 10 of the worksheet: the smaller of line 5d and line 9 (half of line 9 if married filing separately). When line 6 of the worksheet is No, line 9 is $40,000, which gives the printed $40,000/$20,000 limit."
  - id: sa.line6
    printed: "6"
    label: "Other taxes. List type and amount:"
    type: NonNegDollars
    expr: {op: copy, from: sa.zero}
    refuses: [sa.unsupported]
  - id: sa.line8b
    printed: "8b"
    label: "Home mortgage interest not reported to you on Form 1098. See instructions if limited. If paid to the person from whom you bought the home, see instructions and show that person's name, identifying no., and address"
    type: NonNegDollars
    expr: {op: copy, from: sa.zero}
    refuses: [sa.unsupported]
  - id: sa.line8c
    printed: "8c"
    label: "Points not reported to you on Form 1098. See instructions for special rules"
    type: NonNegDollars
    expr: {op: copy, from: sa.zero}
    refuses: [sa.unsupported]
  - id: sa.line13
    printed: "13"
    label: "Carryover from prior year"
    type: NonNegDollars
    expr: {op: copy, from: sa.zero}
    refuses: [sa.charity_limited]
  - id: sa.line15
    printed: "15"
    label: "Casualty and theft loss(es) from a federally declared disaster (other than net qualified disaster losses). Attach Form 4684 and enter the amount from line 18 of that form. See instructions"
    type: NonNegDollars
    expr: {op: copy, from: sa.zero}
    refuses: [sa.unsupported]
  - id: sa.line16
    printed: "16"
    label: "Other—from list in instructions. List type and amount:"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sa.gambling_losses, s1.line8b]}
    refuses: [sa.unsupported]
    note: "Only gambling losses are computed: 'Gambling losses ... but only to the extent of gambling winnings reported on Schedule 1 (Form 1040), line 8b.' Every other item on the line 16 list, and a net qualified disaster loss, is screened out by sa.unsupported."
  - id: sa.line7
    printed: "7"
    label: "Add lines 5e and 6"
    type: NonNegDollars
    expr: {op: sum, of: [sa.line5e, sa.line6]}
  - id: sa.line8e
    printed: "8e"
    label: "Add lines 8a through 8c"
    type: NonNegDollars
    expr: {op: sum, of: [sa.line8a, sa.line8b, sa.line8c]}
  - id: sa.line9
    printed: "9"
    label: "Investment interest. Attach Form 4952 if required. See instructions"
    type: NonNegDollars
    expr: {op: copy, from: f4952.line8}
  - id: sa.line10
    printed: "10"
    label: "Add lines 8e and 9"
    type: NonNegDollars
    expr: {op: sum, of: [sa.line8e, sa.line9]}
  - id: sa.line12
    printed: "12"
    label: "Other than by cash or check. If you made any gift of $250 or more, see instructions. You must attach Form 8283 if over $500"
    type: NonNegDollars
    expr: {op: sum_over, collection: gift, field: gift.allowed}
    refuses: [sa.charity_limited]
  - id: sa.line14
    printed: "14"
    label: "Add lines 11 through 13"
    type: NonNegDollars
    expr: {op: sum, of: [sa.line11, sa.line12, sa.line13]}
  - id: sa.line17
    printed: "17"
    label: "Add the amounts in the far right column for lines 4 through 16. Also, enter this amount on Form 1040 or 1040-SR, line 12e"
    type: NonNegDollars
    expr: {op: sum, of: [sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16]}

  # ---- helpers referenced by the printed lines ----
  - id: sa.zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

  # ---- State and Local Tax Deduction Worksheet (Schedule A instructions, line 5e) ----
  - id: sa.h_salt1
    printed: "(helper)"
    label: "SALT Worksheet line 1. Enter $40,000"
    type: NonNegDollars
    expr: {op: param, ref: sa.salt_base}
  - id: sa.h_salt4
    printed: "(helper)"
    label: "SALT Worksheet line 4. Add lines 2 and 3e (line 2: Form 1040 or 1040-SR, line 11b)"
    type: Dollars
    expr: {op: copy, from: sa.agi}
    refuses: [sa.excluded_income]
    note: "Lines 3a to 3d (excluded Puerto Rico income and the Form 2555 and Form 4563 amounts) are not computed. A filer who has any of them is screened out by sa.excluded_income, so line 3e is zero and line 4 equals line 2."
  - id: sa.h_salt5
    printed: "(helper)"
    label: "SALT Worksheet line 5. Enter $500,000 ($250,000 if married filing separately)"
    type: NonNegDollars
    expr: {op: param, ref: sa.salt_threshold}
  - id: sa.h_salt6
    printed: "(helper)"
    label: "SALT Worksheet line 6. Is the amount on line 4 more than the amount on line 5? Yes. Subtract line 5 from line 4"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sa.h_salt4, take: sa.h_salt5}
    note: "When the answer is No, the worksheet skips lines 7 and 8 and enters line 1 on line 9. A zero here has the same effect: line 7 is 0, line 8 equals line 1, and line 9 is the larger of $40,000 and $10,000, which is line 1."
  - id: sa.h_salt7
    printed: "(helper)"
    label: "SALT Worksheet line 7. Multiply line 6 by 30% (0.30)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sa.h_salt6, rate: {param: sa.salt_rate}}
  - id: sa.h_salt8
    printed: "(helper)"
    label: "SALT Worksheet line 8. Subtract line 7 from line 1"
    type: Dollars
    expr: {op: subtract, from: sa.h_salt1, take: sa.h_salt7}
  - id: sa.h_salt_floor
    printed: "(helper)"
    label: "$10,000"
    type: NonNegDollars
    expr: {op: param, ref: sa.salt_floor}
  - id: sa.h_salt9
    printed: "(helper)"
    label: "SALT Worksheet line 9. Enter the larger of the amount on line 8 or $10,000"
    type: NonNegDollars
    expr: {op: larger_of, of: [sa.h_salt8, sa.h_salt_floor]}
  - id: sa.h_salt9_half
    printed: "(helper)"
    label: "Half the amount on line 9 (married filing separately)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: sa.h_salt9, rate: {param: sa.half}}
  - id: sa.h_mfs
    printed: "(helper)"
    label: "Married filing separately"
    type: Bool
    expr: {op: test, eq: [f1040.status, {const: "mfs"}]}
  - id: sa.saltlimit
    printed: "(helper)"
    label: "SALT Worksheet line 10 limit: the amount on line 9 (half the amount on line 9 if married filing separately)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [sa.h_mfs, {const: true}]}, then: sa.h_salt9_half}
        - {guard: {op: test, eq: [sa.h_mfs, {const: false}]}, then: sa.h_salt9}

  # ---- required intermediate values ----
  - id: sa.agi
    printed: "(helper)"
    label: "Form 1040 or 1040-SR, line 11b (adjusted gross income)"
    type: Dollars
    expr: {op: copy, from: f1040.line11b}
  - id: sa.h_taxpayer_age65_count
    printed: "(helper)"
    label: "Your entry, if you were born before January 2, 1961"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where: {op: test, all: [{op: test, eq: [person.role, {const: "taxpayer"}]}, {op: test, eq: [person.age65, {const: true}]}]}
  - id: sa.age65
    printed: "(helper)"
    label: "Were you born before January 2, 1961?"
    type: Bool
    expr: {op: test, ge: [sa.h_taxpayer_age65_count, {param: person.one}]}
    note: "Taken from your own person entry (person.age65), so the question is not asked twice."

  # ---- standard deduction (Form 1040 instructions, line 12e) ----
  - id: sa.h_age_boxes
    printed: "(helper)"
    label: "Number of 'born before January 2, 1961' boxes checked (you, and your spouse if filing jointly)"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where: {op: test, all: [{op: test, eq: [person.age65, {const: true}]}, {op: test, eq: [person.died_before_65, {const: false}]}]}
    note: "The instructions say not to check the spouse's box if the spouse was born before January 2, 1961, but died in 2025 before reaching age 65. For a taxpayer who died in 2025 they only point to Pub. 501. Chosen: apply the same exclusion to every person entry (person.died_before_65). The spouse boxes for married filing separately are screened out by sa.spouse_extra. The roster has a spouse entry only on a joint return, so no spouse box is counted for head of household."
  - id: sa.h_blind_boxes
    printed: "(helper)"
    label: "Number of 'blind' boxes checked (you, and your spouse if filing jointly)"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where: {op: test, eq: [person.blind, {const: true}]}
  - id: sa.h_std_base
    printed: "(helper)"
    label: "Standard deduction for the filing status (amounts listed to the left of Form 1040 line 12e)"
    type: NonNegDollars
    expr: {op: param, ref: sa.standard_base}
  - id: sa.h_std_extra
    printed: "(helper)"
    label: "Additional amount for each box checked, as built into the Standard Deduction Chart for People Who Were Born Before January 2, 1961, or Were Blind"
    type: NonNegDollars
    expr: {op: param, ref: sa.standard_extra}
    note: "The chart lists totals, not a per-box amount. Chosen: base amount plus a per-box amount ($2,000 single or head of household; $1,600 otherwise) times the number of boxes. This gives every chart row (for example, single with 1 box is $17,750 and married filing jointly with 4 boxes is $37,900)."
  - id: sa.h_std_age
    printed: "(helper)"
    label: "Additional amount for age boxes"
    type: NonNegDollars
    expr: {op: multiply_count, amount: sa.h_std_extra, count: sa.h_age_boxes}
  - id: sa.h_std_blind
    printed: "(helper)"
    label: "Additional amount for blindness boxes"
    type: NonNegDollars
    expr: {op: multiply_count, amount: sa.h_std_extra, count: sa.h_blind_boxes}
  - id: sa.h_std_full
    printed: "(helper)"
    label: "Standard deduction (amount to the left of line 12e, or the Standard Deduction Chart if any box on line 12d is checked)"
    type: NonNegDollars
    expr: {op: sum, of: [sa.h_std_base, sa.h_std_age, sa.h_std_blind]}
    refuses: [sa.dependent, sa.spouse_extra, sa.unsupported]
  - id: sa.h_standard
    printed: "(helper)"
    label: "Standard deduction; zero if married filing separately and your spouse itemizes (Exception 2)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [sa.spouse_itemizes, {const: true}]}, then: sa.zero}
        - {guard: {op: test, eq: [sa.spouse_itemizes, {const: false}]}, then: sa.h_std_full}
  - id: sa.itemizes
    printed: "(helper)"
    label: "Itemize if elected (line 18), required (spouse itemizes on a separate return), or itemized total exceeds standard"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [sa.elect_itemize, {const: true}]}
        - {op: test, eq: [sa.spouse_itemizes, {const: true}]}
        - {op: test, gt: [sa.line17, sa.h_standard]}
    note: "'Take the larger of your standard deduction or itemized deductions' does not say what to do when they are equal. Chosen: itemize only when line 17 is strictly larger, unless you elect to itemize or are required to. The deduction is the same either way."
  - id: sa.deduction
    printed: "(helper)"
    label: "Standard deduction or itemized deductions (from Schedule A) for Form 1040 line 12e"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [sa.itemizes, {const: true}]}, then: sa.line17}
        - {guard: {op: test, eq: [sa.itemizes, {const: false}]}, then: sa.h_standard}
```
```
