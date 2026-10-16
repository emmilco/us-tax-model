# Calculator entry sheet — stage5.return.itemized

Enter this case in FreeTaxUSA (2025) and OLT (2025), then read the lines below back into a record. Synthetic data only.

## Enter

| field | value |
| --- | --- |
| 1099-DIV box 1a — total ordinary dividends | 4000.00 |
| 1099-DIV box 1b — qualified dividends | 2000.00 |
| 1099-DIV box 2a — total capital gain distributions | 1500.00 |
| 1099-DIV box 5 — section 199A dividends | 300.00 |
| Investment interest expense paid (Form 4952 line 1) | 1500.00 |
| 1099-DIV box 7 — foreign tax paid | 120.00 |
| Medical and dental expenses paid | 3000.00 |
| State and local income taxes paid | 10000.00 |
| Home mortgage interest from Form 1098 | 10000.00 |
| Gifts to charity by cash or check | 5000.00 |
| W-2 (emp_a) box 1 — wages, tips, other compensation | 90000.00 |
| W-2 (emp_a) box 2 — federal income tax withheld | 10000.00 |
| W-2 (emp_a) box 3 — social security wages | 90000.00 |
| W-2 (emp_a) box 4 — social security tax withheld | 5580.00 |
| W-2 (emp_a) box 5 — Medicare wages and tips | 90000.00 |
| W-2 (emp_a) box 6 — Medicare tax withheld | 1305.00 |
| 1099-INT (bank_a) box 1 — taxable interest | 1000.00 |
| Sale (s1) — Form 8949 box (A–F) | D |
| Sale (s1) — routed detail or aggregate | detail |
| Sale (s1) — adjustment code | none |
| Sale (s1) — proceeds (Form 1099-B) | 16000.00 |
| Sale (s1) — cost or other basis | 10000.00 |
| Noncash gift (books) — fair market value | 800.00 |

Screening questions (answer No unless noted): Schedule 1 income, Schedule 1-A deductions, dependent/other credits, other income treatment, Form 1040 line 16 additional taxes, AMT, digital assets, foreign accounts.

| field | value |
| --- | --- |
| div.basis_reconciled | yes |
| ftc.all_passive | yes |
| ftc.statements | yes |
| ftc.eligible | yes |
| ftc.elect | yes |

## Read back (record each line the calculators show)

| line | description |
| --- | --- |
| f1040.line1a | Total amount from Form(s) W-2, box 1 |
| f1040.line1z | Add lines 1a through 1h |
| f1040.line2b | Taxable interest |
| f1040.line3a | Qualified dividends |
| f1040.line3b | Ordinary dividends |
| f1040.line7a | Capital gain or (loss). Attach Schedule D if required |
| f1040.line8 | Additional income from Schedule 1, line 10 |
| f1040.line9 | Add lines 1z, 2b, 3b, 4b, 5b, 6b, 7a, and 8. This is your total income |
| f1040.line10 | Adjustments to income from Schedule 1, line 26 |
| f1040.line11a | Subtract line 10 from line 9. This is your adjusted gross income |
| f1040.line11b | Amount from line 11a (adjusted gross income) |
| f1040.line12e | Standard deduction or itemized deductions (from Schedule A) |
| f1040.line13a | Qualified business income deduction from Form 8995 or Form 8995-A |
| f1040.line13b | Additional deductions from Schedule 1-A, line 38 |
| f1040.line14 | Add lines 12e, 13a, and 13b |
| f1040.line15 | Subtract line 14 from line 11b. If zero or less, enter -0-. This is your taxable income |
| f1040.line16 | Tax (see instructions). Check if any from Form(s): 1 8814 2 4972 3 |
| f1040.line17 | Amount from Schedule 2, line 3 |
| f1040.line18 | Add lines 16 and 17 |
| f1040.line19 | Child tax credit or credit for other dependents from Schedule 8812 |
| f1040.line20 | Amount from Schedule 3, line 8 |
| f1040.line21 | Add lines 19 and 20 |
| f1040.line22 | Subtract line 21 from line 18. If zero or less, enter -0- |
| f1040.line23 | Other taxes, including self-employment tax, from Schedule 2, line 21 |
| f1040.line24 | Add lines 22 and 23. This is your total tax |
| f1040.line25a | Federal income tax withheld from Form(s) W-2 |
| f1040.line25b | Federal income tax withheld from Form(s) 1099 |
| f1040.line25c | Federal income tax withheld from other forms (see instructions) |
| f1040.line25d | Add lines 25a through 25c |
| f1040.line26 | 2025 estimated tax payments and amount applied from 2024 return |
| f1040.line27a | Earned income credit (EIC) |
| f1040.line28 | Additional child tax credit (ACTC) from Schedule 8812 |
| f1040.line29 | American opportunity credit from Form 8863, line 8 |
| f1040.line30 | Refundable adoption credit from Form 8839, line 13 |
| f1040.line31 | Amount from Schedule 3, line 15 |
| f1040.line32 | Add lines 27a, 28, 29, 30, and 31. These are your total other payments and refundable credits |
| f1040.line33 | Add lines 25d, 26, and 32. These are your total payments |
| f1040.line34 | If line 33 is more than line 24, subtract line 24 from line 33. This is the amount you overpaid |
| f1040.line35a | Amount of line 34 you want refunded to you |
| f1040.line36 | Amount of line 34 you want applied to your 2026 estimated tax |
| f1040.line37 | Subtract line 33 from line 24. This is the amount you owe |
| s3.line8 | Add lines 1 through 4, 5a, 5b, and 7. Enter here and on Form 1040, line 20 |
| sa.deduction | Deduction selected for Form 1040 line 12e |
| sa.itemizes | Itemize if elected, required, or itemized total exceeds standard |
| qbi.deduction | Select Form 8995 or dividend-only Form 8995-A |

## Record format

Save as `fixtures/2025/differential/<calculator>.stage5.return.itemized.json`:

```json
{
  "calculator": "FreeTaxUSA",
  "version": "2025, accessed YYYY-MM-DD",
  "case": "stage5.return.itemized",
  "values": {
    "f1040.line15": 0
  },
  "investigations": {}
}
```

Only include lines the calculator actually shows; absent lines are simply not compared. Any difference from the computed value needs a cited cause in `investigations`.
