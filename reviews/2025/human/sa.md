# Human reading — sa

Review units of `Schedule A — supported itemized deductions and standard comparison` read against the archived IRS pages by a person through `tools/human_review/`. A guided unit covers its named computation only; referenced amounts are checked separately. Every verdict and reason is the reader's own text.

| field | value |
| --- | --- |
| date | 2026-10-23 |
| reader | Elliot Milco |
| items | 2 |
| receipt format | 1 (per printed line, including folded helpers) |
| lines judged | 12 |
| match / mismatch / unclear / empty | 8 / 3 / 1 / 0 |

## Source pages read

| document | revision | pages | text sha256 | cols sha256 |
| --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| f1040sa | 2025; created 2025-11-20 | 1 | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040gi | 2025; printed date 2026-02-25 | 33, 34, 35, 110 | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### (helper) — `sa.standardbase`
Label: Year parameter sa.standard_base
Reading: For your filing status: [Single or married filing separately: $15,750.00. | Married filing jointly or qualifying surviving spouse: $31,500.00. | Head of household: $23,625.00.]
Cite: [f1040] p. 2, "Standard deduction for"
Pages: f1040 2
Helpers folded: (none)
Item: 2
Review sha256: 5e251eb5a4063bc236c9754b5a4d2381f474c9489696d2e033c403dac4b78e07
Verdict: **MATCH**
Reason:
exact match

### (helper) — `sa.extra`
Label: Year parameter sa.standard_extra
Reading: For your filing status: [Single or head of household: $2,000.00. | Married filing jointly or married filing separately or qualifying surviving spouse: $1,600.00.]
Cite: [i1040gi] p. 35, "Standard Deduction Chart for People Who Were Born Before January 2, 1961, or Were Blind"
Pages: i1040gi 35
Helpers folded: (none)
Item: 2
Review sha256: f3043be2818865d3e35c9d8b5619b7abfa3c0f64d14457ab060d3373279f36fd
Verdict: **MISMATCH**
Reason:
the described values appear nowhere on this page.

### (helper) — `sa.boxes_age65`
Label: Number of boxes checked for born before January 2, 1961 (you, and your spouse if filing jointly), not counting a person who died in 2025 before reaching 65
Reading: the number of person entries (you, or your spouse on a joint return) for which the answer to the birth-date question is yes and you answered no to “Is this the final return of a person born between January 2, 1960, and January 1, 1961, who died in 2025 before reaching age 65? (A person reaches age 65 on the day before the 65th birthday.)”
Cite: [i1040gi] p. 33, "If you or your spouse (if you are married and filing a joint return) were born before January 2, 1961, or were blind at the end of 2025, check the appropriate box(es)"; [i1040gi] p. 33, "If your spouse was born before January 2, 1961, but died in 2025 before reaching age 65"; [i1040gi] p. 110, Schedule 1-A, Part V, "Death of a taxpayer in 2025"
Pages: i1040gi 33, 110
Helpers folded: (none)
Item: 2
Review sha256: a6d905e2f5551c3b509b846eb392944ee629939b22d65436a4789b708f244809
Verdict: **MATCH**
Reason:
yes this is correct.

### (helper) — `sa.boxes_blind`
Label: Number of boxes checked for blindness (you, and your spouse if filing jointly)
Reading: the number of person entries (you, or your spouse on a joint return) for which you answered yes to “Are you blind under the standard-deduction instructions?”
Cite: [i1040gi] p. 33, "If you or your spouse (if you are married and filing a joint return) were born before January 2, 1961, or were blind at the end of 2025, check the appropriate box(es)"
Pages: i1040gi 33
Helpers folded: (none)
Item: 2
Review sha256: 474768ea0b4b9c12860773c288e62dd966c5e734650dd8df10aaddbf63b27895
Verdict: **MATCH**
Reason:
yes, correct

### (helper) — `sa.extra_age65`
Label: Additional standard deduction for each box checked for age
Reading: the addition for one age or blindness box times the number of eligible age boxes
Cite: [i1040gi] p. 35, "Standard Deduction Chart for People Who Were Born Before January 2, 1961, or Were Blind"
Pages: i1040gi 35
Helpers folded: (none)
Item: 2
Review sha256: 536d39dd9e0474f330f07c4b752b696663e743b35cded1e1b447cf2218e03804
Verdict: **MISMATCH**
Reason:
The expression given seems to imply that it's 
COUNT(AGE) x COUNT(BLIND). The instruction itself describes a sum: COUNT(AGE) + COUNT(BLIND)

### (helper) — `sa.extra_blind`
Label: Additional standard deduction for each box checked for blindness
Reading: the addition for one age or blindness box times the number of blindness boxes
Cite: [i1040gi] p. 35, "Standard Deduction Chart for People Who Were Born Before January 2, 1961, or Were Blind"
Pages: i1040gi 35
Helpers folded: (none)
Item: 2
Review sha256: 35c052f62835a5d0d0978586f2f34966913eb0386d873b73d12b2024eed3ca2f
Verdict: **MISMATCH**
Reason:
The instruction is the sum of the age boxes and the blind boxes, not their multiplication.

### (helper) — `sa.standardraw`
Label: Add sa.standardbase, sa.extra_age65, sa.extra_blind
Reading: the sum of the base deduction for your filing status, the age addition and the blindness addition
Cite: [i1040gi] p. 35, "Standard Deduction Chart for People Who Were Born Before January 2, 1961, or Were Blind"
Pages: i1040gi 35
Helpers folded: (none)
Item: 2
Review sha256: dadcb41df3c64f24ed209174aca1d74dafc3edd2b28a78f54409451f605e96e3
Verdict: **UNCLEAR**
Reason:
the description is confusing relative to what i'm being shown.

### (helper) — `sa.mfs`
Label: Married filing separately
Reading: yes when your filing status (Form 1040) is married filing separately, otherwise no
Cite: [f1040] p. 1, "Married filing separately"
Pages: f1040 1
Helpers folded: (none)
Item: 2
Review sha256: 3a6c9a7ea25325adc41dac9dff698940dd9ff6d972f9e419744d347ed55896dc
Verdict: **MATCH**
Reason:
exact match

### (helper) — `sa.mfs_spouse_itemizes`
Label: MFS with spouse itemizing
Reading: yes when the answer to 'Are you married filing separately?' is yes and you answered yes to “Married filing separately with a spouse who itemizes?”, otherwise no
Cite: [i1040gi] p. 34, "If you checked the box on line 12b, your standard deduction is zero"
Pages: i1040gi 34
Helpers folded: (none)
Item: 2
Review sha256: e8fb71df4fbbf029d77a6767bba2ce347e626404f9095e5da155279d5e78cca7
Verdict: **MATCH**
Reason:
exact match

### (helper) — `sa.standard`
Label: Standard deduction, zero when MFS spouse itemizes
Reading: Choose the amount as follows: [Use $0.00 when: [the answer to 'Are you married filing separately with a spouse who itemizes?' is yes] | Otherwise, use the base deduction plus the age and blindness additions.]
Cite: [i1040gi] p. 34, "If you checked the box on line 12b, your standard deduction is zero"; [i1040gi] p. 35, "Standard Deduction Chart for People Who Were Born Before January 2, 1961, or Were Blind"
Pages: i1040gi 34, 35
Helpers folded: (none)
Item: 2
Review sha256: 3a8adbc54020aaeb63220b6a7e47145c5eba57a4874408cc36052d8348e1763d
Verdict: **MATCH**
Reason:
matches

### (helper) — `sa.itemizes`
Label: Itemize if elected, required, or itemized total exceeds standard
Reading: yes when any of these holds: (1) you answered yes to “Elect to itemize even if the standard deduction is larger?”, (2) the answer to 'Are you married filing separately with a spouse who itemizes?' is yes, (3) the total itemized deductions from Schedule A, line 17 is greater than the standard deduction, otherwise no
Cite: [i1040gi] p. 34, "In most cases, your federal income tax will be less if you take the larger of your standard deduction or itemized deductions"; [f1040sa] p. 1, "If you elect to itemize deductions even though they are less than your standard deduction"; [i1040gi] p. 34, "If you checked the box on line 12b, your standard deduction is zero"
Pages: f1040sa 1; i1040gi 34
Helpers folded: (none)
Item: 2
Review sha256: bbb1dc8e069f6f7b84a48b3874676d6df3a9988419073c94be01c095592b2191
Verdict: **MATCH**
Reason:
matches

### (helper) — `sa.deduction`
Label: Deduction selected for Form 1040 line 12e
Reading: Choose the amount as follows: [Use the total itemized deductions from Schedule A, line 17 when: [the decision to use itemized deductions is yes] | Otherwise, use the standard deduction.]
Cite: [i1040gi] p. 34, "In most cases, your federal income tax will be less if you take the larger of your standard deduction or itemized deductions"
Pages: i1040gi 34
Helpers folded: (none)
Item: 2
Review sha256: 91ddfe56f78296defd29271b296af1d974c90dc6a063c4193be05a47fccde1e8
Verdict: **MATCH**
Reason:
matches
