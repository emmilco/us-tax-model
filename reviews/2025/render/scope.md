# Render comparison — scope

The rendered English of every printed line of `Proof-of-concept scope screening` (`rendered/2025/scope.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-18 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | c14f4aae4153ad2f6fc5c018bf0778110e0bd1fd32e53aa21025e931b4850915 |
| lines judged | 6 |
| match / mismatch / unclear / missing | 4 / 0 / 2 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040gi | 2025; printed date 2026-02-25 | 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 117 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### schedule1 — Any income or adjustment requiring Schedule 1, including a taxable state or local tax refu
Status: **MATCH**

Model: Form 1040 line 8 takes "Additional income from Schedule 1, line 10" and line 10 takes "Adjustments to income from Schedule 1, line 26". A yes/no screen that refuses whenever any Schedule 1 item applies leaves out exactly what those lines bring in. The listed examples cannot be checked against Schedule 1 because its text is not given, but the general question covers them.

### schedule1a — Do you qualify for any Schedule 1-A deduction (qualified tips, qualified overtime compensa
Status: **MATCH**

Model: Form 1040 line 13b takes "Additional deductions from Schedule 1-A, line 38", and line 12d's "born before January 2, 1961" matches the age-based item in the question. Refusing whenever any Schedule 1-A deduction might apply is a valid narrowing. The specific Schedule 1-A categories cannot be checked from the text given.

### credits — Do you want to claim any credit other than the foreign tax credit claimed without Form 111
Status: **UNCLEAR**

Restated: Input — Do you want to claim any credit other than the foreign tax credit claimed without Form 1116, the excess social security credit, the child tax credit, the credit for other dependents, the additional child tax credit and the earned income credit, or do you have any other amount for Schedule 3 Part I (for example a Form 8978 adjustment)?

Model: The screen catches any "credit" and other amounts for Schedule 3 Part I. The instructions also list Part II amounts that are not credits, such as line 10 "Amount Paid With Request for Extension To File" and line 13d, the deferred "net 965 tax liability". These feed Schedule 3 line 15 and Form 1040 line 31, and neither this screen nor its refusal mentions them. The text given does not show whether the program handles them somewhere else.

Ruling: covered elsewhere; project retained. The screen is for credits; the Schedule 3 Part II amounts that are not credits are inputs of their own: line 10 (amount paid with a request for an extension, s3.line10) and line 14 (the total of lines 13a to 13z, s3.line14), so a filer answering no still enters them.

### other_income — Any nonresident alien status (you or your spouse, for any part of 2025) or other income or
Status: **UNCLEAR**

Restated: Input — Any nonresident alien status (you or your spouse, for any part of 2025) or other income or return treatment outside wages, interest, dividends, supported securities sales, Form 1099-R distributions and social security benefits, including wages or tips not on a Form W-2, Medicaid waiver payments (whether or not in Form W-2 box 1), dependent care or adoption benefits, other earned income (Form 1040 lines 1b-1h), or income or loss from a passive activity (including gain on selling an interest in one)?

Model: The screen names "Form 1040 lines 1b-1h" but not line 1i, "Nontaxable combat pay election", or line 6c, "If you elect to use the lump-sum election method". A filer could answer no even with one of these elections. Whether the catch-all "return treatment" is meant to cover them, and whether they would change a value the program computes (for example the EIC), cannot be judged from the text given.

Ruling: covered elsewhere; project retained. Line 1i (the nontaxable combat pay election) is screened by the combat pay questions where it matters (s8812.combat_pay and the EIC's combat pay refusal), and line 6c (the lump-sum election) is asked directly (ssb.lump_sum, which refuses the worksheet and checks line 6c).

### other_line16 — Any additional Form 1040 line 16 tax or filing, including filing Form 8814 (even with no t
Status: **MATCH**

Model: Form 1040 line 16 reads "Tax (see instructions). Check if any from Form(s): 1 8814 2 4972 3". The screen asks about any extra line 16 tax or filing, names Forms 8814 and 4972, and refuses. That leaves out everything except the basic tax computation, which is a valid narrowing.

### ready — All declared scope screens passed
Status: **MATCH**

Model: This is a constant true with refusals that name each excluded case. The Schedule 3 line 11 instruction says "Figure this amount separately for you and your spouse", so refusing married filing statuses ("Married filing jointly", "Married filing separately") is a valid narrowing. Each of the other refusals matches its screen.

## Raw response

```yaml
```yaml
lines:
  - key: "schedule1"
    status: MATCH
    reason: "Form 1040 line 8 takes \"Additional income from Schedule 1, line 10\" and line 10 takes \"Adjustments to income from Schedule 1, line 26\". A yes/no screen that refuses whenever any Schedule 1 item applies leaves out exactly what those lines bring in. The listed examples cannot be checked against Schedule 1 because its text is not given, but the general question covers them."
  - key: "schedule1a"
    status: MATCH
    reason: "Form 1040 line 13b takes \"Additional deductions from Schedule 1-A, line 38\", and line 12d's \"born before January 2, 1961\" matches the age-based item in the question. Refusing whenever any Schedule 1-A deduction might apply is a valid narrowing. The specific Schedule 1-A categories cannot be checked from the text given."
  - key: "credits"
    status: UNCLEAR
    reason: "The screen catches any \"credit\" and other amounts for Schedule 3 Part I. The instructions also list Part II amounts that are not credits, such as line 10 \"Amount Paid With Request for Extension To File\" and line 13d, the deferred \"net 965 tax liability\". These feed Schedule 3 line 15 and Form 1040 line 31, and neither this screen nor its refusal mentions them. The text given does not show whether the program handles them somewhere else."
  - key: "other_income"
    status: UNCLEAR
    reason: "The screen names \"Form 1040 lines 1b-1h\" but not line 1i, \"Nontaxable combat pay election\", or line 6c, \"If you elect to use the lump-sum election method\". A filer could answer no even with one of these elections. Whether the catch-all \"return treatment\" is meant to cover them, and whether they would change a value the program computes (for example the EIC), cannot be judged from the text given."
  - key: "other_line16"
    status: MATCH
    reason: "Form 1040 line 16 reads \"Tax (see instructions). Check if any from Form(s): 1 8814 2 4972 3\". The screen asks about any extra line 16 tax or filing, names Forms 8814 and 4972, and refuses. That leaves out everything except the basic tax computation, which is a valid narrowing."
  - key: "ready"
    status: MATCH
    reason: "This is a constant true with refusals that name each excluded case. The Schedule 3 line 11 instruction says \"Figure this amount separately for you and your spouse\", so refusing married filing statuses (\"Married filing jointly\", \"Married filing separately\") is a valid narrowing. Each of the other refusals matches its screen."
```
```
