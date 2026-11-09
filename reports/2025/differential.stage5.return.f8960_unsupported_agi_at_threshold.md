# Calculator entry sheet — stage5.return.f8960_unsupported_agi_at_threshold

Enter this case in FreeTaxUSA (2025) and OLT (2025), then read the lines below back into a record. Synthetic data only.

## Enter

| field | value |
| --- | --- |
| Estimated tax payments | 2000.00 |
| W-2 (emp_a) box 1 — wages, tips, other compensation | 200000.00 |
| W-2 (emp_a) box 2 — federal income tax withheld | 20000.00 |
| W-2 (emp_a) box 4 — social security tax withheld | 10918.20 |
| W-2 (emp_a) box 5 — Medicare wages and tips | 200000.00 |
| W-2 (emp_a) box 6 — Medicare tax withheld | 2900.00 |

Screening questions (answer No unless noted): Schedule 1 income, Schedule 1-A deductions, dependent/other credits, other income treatment, Form 1040 line 16 additional taxes, AMT, digital assets, foreign accounts.

| field | value |
| --- | --- |

## Read back (record each line the calculators show)

| line | description |
| --- | --- |
| f1040.line11a | Subtract line 10 from line 9. This is your adjusted gross income |
| f8960.line16 | Smaller of f8960.line12, f8960.line15 (zero when modified AGI is not more than the threshold, so that line 15 is zero) |
| f1040.line23 | Other taxes, including self-employment tax, from Schedule 2, line 21 |

## Record format

Save as `fixtures/2025/differential/<calculator>.stage5.return.f8960_unsupported_agi_at_threshold.json`:

```json
{
  "calculator": "FreeTaxUSA",
  "version": "2025, accessed YYYY-MM-DD",
  "case": "stage5.return.f8960_unsupported_agi_at_threshold",
  "values": {
    "f1040.line15": 0
  },
  "investigations": {}
}
```

Only include lines the calculator actually shows; absent lines are simply not compared. Any difference from the computed value needs a cited cause in `investigations`.
