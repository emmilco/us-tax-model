# Schedule B (Form 1116) — one earlier year's foreign tax carried into 2025

- Document: `f1116sbyr` (form, tax year 2025)
- Collection: keyed entries; [i1116sb] p. 1, Line 1. Foreign tax carryover from the prior tax year, "Enter on line 1 the amounts from the appropriate columns of line 8 of the prior year Schedule B." (Rev. December 2022 (printed 'Instructions for Schedule B (Form 1116) (Rev. 12-2022)', Dec 29, 2022); current irs-pdf edition, not year-specific; the IRS had posted no 2025 edition; sha256 84d287be)
- Note: One entry per earlier year whose unused passive category foreign tax is carried into 2025, as line 8 of the 2024 Schedule B (Form 1116) shows it (on a joint return, both spouses' amounts for the year together).

## (helper) — `f1116sbyr.year`

- **Authored helper label:** The earlier tax year the unused foreign tax comes from (the 10th to the 1st preceding tax year)
- **Encoded (Enum(ftc_carry_year)):** Input — The tax year this unused foreign tax comes from: one of the ten years before 2025, by its column on the 2024 Schedule B (Form 1116)
- Expr: `{"op":"input","source":"The tax year this unused foreign tax comes from: one of the ten years before 2025, by its column on the 2024 Schedule B (Form 1116)"}`
- Cite: [i1116sb] p. 1, Line 1. Foreign tax carryover from the prior tax year, "For example, enter on line 1, column (i) of the current year Schedule B the amount from line 8, column (ii) of the prior year Schedule B." (Rev. December 2022 (printed 'Instructions for Schedule B (Form 1116) (Rev. 12-2022)', Dec 29, 2022); current irs-pdf edition, not year-specific; the IRS had posted no 2025 edition; sha256 84d287be)

## (helper) — `f1116sbyr.amount`

- **Authored helper label:** Foreign tax from that year carried into 2025 (line 8 of the 2024 Schedule B (Form 1116), passive category, in that year's column)
- **Encoded (NonNegDollars):** Input — The foreign tax from that year carried into 2025: line 8 of the 2024 Schedule B (Form 1116) for passive category income, in that year's column (on a joint return, both spouses' amounts together)
- Expr: `{"op":"input","source":"The foreign tax from that year carried into 2025: line 8 of the 2024 Schedule B (Form 1116) for passive category income, in that year's column (on a joint return, both spouses' amounts together)"}`
- Cite: [i1116sb] p. 1, Line 1. Foreign tax carryover from the prior tax year, "Enter on line 1 the amounts from the appropriate columns of line 8 of the prior year Schedule B." (Rev. December 2022 (printed 'Instructions for Schedule B (Form 1116) (Rev. 12-2022)', Dec 29, 2022); current irs-pdf edition, not year-specific; the IRS had posted no 2025 edition; sha256 84d287be)
