# Render comparison — scope

The rendered English of every printed line of `Proof-of-concept scope screening` (`rendered/2025/scope.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 530aaef764a12ad61d91e53c9e0fc9ab160e1335d925077ef80178e922627424 |
| lines judged | 6 |
| match / mismatch / unclear / missing | 6 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 |
| --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 |
| i1040gi | 2025; printed date 2026-02-25 | 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 |

## Lines

### schedule1 — Any income or adjustment requiring Schedule 1, including a taxable state/local tax refund?
Status: **MATCH**

Model: Form 1040 line 8 ('Additional income from Schedule 1, line 10') and line 10 ('Adjustments to income from Schedule 1, line 26') draw on Schedule 1. This input asks whether any such item exists, and the refusal excludes Schedule 1. The given text does not mention the state/local refund example, but it only illustrates the question.

### schedule1a — Any deduction claimed on Schedule 1-A, including tips, overtime, car-loan interest or enha
Status: **MATCH**

Model: Form 1040 line 13b is 'Additional deductions from Schedule 1-A, line 38'. The input flags any Schedule 1-A deduction, and the refusal excludes it. The listed examples are not in the given text but do not change what the screen asks.

### credits — Any dependent or other credit outside the simple foreign tax credit and excess Social Secu
Status: **MATCH**

Model: Form 1040 lines 19 (Schedule 8812), 20 and 31 (Schedule 3), and 27a–30 carry dependent and other credits. The input flags any credit beyond the two the program supports, and the refusal names Schedule 8812 and other credit forms. Excess social security credit is Schedule 3 line 11 in the instructions given; the foreign tax credit is not described in the text, so that carve-out is taken as the program's stated scope.

### other_income — Any retirement, Social Security, nonresident or other income/return treatment outside wage
Status: **MATCH**

Model: The label lists Form 1040 lines 1b–1h correctly: household wages and tips not on W-2, Medicaid waiver payments, dependent care benefits, adoption benefits, Form 8919 wages and other earned income. It also covers retirement (4a–5b) and social security (6a–6d) income. The input screens all of these out, and the refusal names the additional income and return forms.

### other_line16 — Any additional Form 1040 line 16 tax, including Forms 8814, 4972, 8615 or a section 962 el
Status: **MATCH**

Model: Form 1040 line 16 reads 'Tax (see instructions). Check if any from Form(s): 1 8814 2 4972 3'. The input flags any additional line 16 tax, and the refusal excludes it. Forms 8615 and the section 962 election are not named in the given text but fall under box 3 'other'.

### ready — All declared scope screens passed
Status: **MATCH**

Model: This helper is meant to mean 'all declared scope screens passed'. It is constant true, so its meaning rests entirely on the refusals, which name each screen and the form excluded. The married refusal is consistent with the instruction for line 11: 'Figure this amount separately for you and your spouse.' Note that the given screens do not ask about Schedule 2 amounts (Form 1040 lines 17 and 23); whether those are handled elsewhere cannot be judged from this text.

## Raw response

```yaml
```yaml
lines:
  - key: "schedule1"
    status: MATCH
    reason: "Form 1040 line 8 ('Additional income from Schedule 1, line 10') and line 10 ('Adjustments to income from Schedule 1, line 26') draw on Schedule 1. This input asks whether any such item exists, and the refusal excludes Schedule 1. The given text does not mention the state/local refund example, but it only illustrates the question."
  - key: "schedule1a"
    status: MATCH
    reason: "Form 1040 line 13b is 'Additional deductions from Schedule 1-A, line 38'. The input flags any Schedule 1-A deduction, and the refusal excludes it. The listed examples are not in the given text but do not change what the screen asks."
  - key: "credits"
    status: MATCH
    reason: "Form 1040 lines 19 (Schedule 8812), 20 and 31 (Schedule 3), and 27a–30 carry dependent and other credits. The input flags any credit beyond the two the program supports, and the refusal names Schedule 8812 and other credit forms. Excess social security credit is Schedule 3 line 11 in the instructions given; the foreign tax credit is not described in the text, so that carve-out is taken as the program's stated scope."
  - key: "other_income"
    status: MATCH
    reason: "The label lists Form 1040 lines 1b–1h correctly: household wages and tips not on W-2, Medicaid waiver payments, dependent care benefits, adoption benefits, Form 8919 wages and other earned income. It also covers retirement (4a–5b) and social security (6a–6d) income. The input screens all of these out, and the refusal names the additional income and return forms."
  - key: "other_line16"
    status: MATCH
    reason: "Form 1040 line 16 reads 'Tax (see instructions). Check if any from Form(s): 1 8814 2 4972 3'. The input flags any additional line 16 tax, and the refusal excludes it. Forms 8615 and the section 962 election are not named in the given text but fall under box 3 'other'."
  - key: "ready"
    status: MATCH
    reason: "This helper is meant to mean 'all declared scope screens passed'. It is constant true, so its meaning rests entirely on the refusals, which name each screen and the form excluded. The married refusal is consistent with the instruction for line 11: 'Figure this amount separately for you and your spouse.' Note that the given screens do not ask about Schedule 2 amounts (Form 1040 lines 17 and 23); whether those are handled elsewhere cannot be judged from this text."
```
```
