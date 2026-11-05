# Form IT-2 (2025), Summary of W-2 Statements — one record per Form W-2

- Document: `ny_it2` (form, tax year 2025)
- Collection: keyed entries; [ny_it201i] p. 21, Lines 72, 73, and 74, "You must complete a W-2 record for each W-2 you receive, even if it does not show any New York State, New York City (NYC), or Yonkers wages or tax withheld." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 17a — `ny_it2.state_withheld`

- **IRS:** NYS income tax withheld
- **Encoded (NonNegDollars):** Input — New York State income tax withheld on this Form W-2 (box 17 for New York State; 0 if none)
- Expr: `{"op":"input","source":"New York State income tax withheld on this Form W-2 (box 17 for New York State; 0 if none)"}`
- Cite: [ny_it2] p. 1, W-2 Record 1, "Box 17a NYS income tax withheld" (Form IT-2 (2025), Summary of W-2 Statements; final 2025 edition (footer 'IT-2 (2025) (back)'); PDF modified 2025-09-26; sha256 45f6a7b5)

## 19 (Yonkers) — `ny_it2.yonkers_withheld`

- **IRS:** Local income tax withheld for Yonkers
- **Encoded (NonNegDollars):** Input — Form W-2 box 19, local income tax withheld for Yonkers (0 if none)
- Expr: `{"op":"input","source":"Form W-2 box 19, local income tax withheld for Yonkers (0 if none)"}`
- Cite: [ny_it2] p. 1, W-2 Record 1, "Box 19 Local income tax withheld" (Form IT-2 (2025), Summary of W-2 Statements; final 2025 edition (footer 'IT-2 (2025) (back)'); PDF modified 2025-09-26; sha256 45f6a7b5)

## (gate) — `ny_it2.yonkers_gate`

- **Authored helper label:** This W-2 shows Yonkers tax withheld
- **Encoded (Bool):** line 19 (Yonkers) > $0
- Expr: `{"gt":["ny_it2.yonkers_withheld",{"const":0}],"op":"test"}`
- Cite: [ny_it201i] p. 21, Lines 72, 73, and 74, "Enter on the appropriate line your total New York State, New York City, and Yonkers tax withheld from any of the following:" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## 17a (whole dollars) — `ny_it2.state_whole`

- **IRS:** NYS income tax withheld, in whole dollars
- **Encoded (NonNegDollars):** Round line 17a to the nearest multiple of (half up) $1.
- Expr: `{"of":"ny_it2.state_withheld","op":"round","rule":"half_up","unit":100}`
- Cite: [ny_it2] p. 2, Entering whole dollar amounts, "drop amounts below 50 cents and increase amounts from 50 to 99 cents to the next dollar" (Form IT-2 (2025), Summary of W-2 Statements; final 2025 edition (footer 'IT-2 (2025) (back)'); PDF modified 2025-09-26; sha256 45f6a7b5)

## 19 — `ny_it2.city_withheld`

- **IRS:** Local income tax withheld (New York City)
- **Encoded (NonNegDollars):** Input — Form W-2 box 19, local income tax withheld for New York City (0 if none)
- **Refusal:** when ny_it2.yonkers_gate is true, cannot complete Yonkers tax withheld (Form IT-201 line 74). Yonkers withholding means Yonkers tax may be owed, which is outside this tool. Cite: [ny_it201i] p. 17, Line 55: Yonkers resident income tax surcharge, "If you were a resident of Yonkers, did you enter an amount that is more than 0 on line 46?" (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)
- Expr: `{"op":"input","source":"Form W-2 box 19, local income tax withheld for New York City (0 if none)"}`
- Cite: [ny_it2] p. 1, W-2 Record 1, "Box 19 Local income tax withheld" (Form IT-2 (2025), Summary of W-2 Statements; final 2025 edition (footer 'IT-2 (2025) (back)'); PDF modified 2025-09-26; sha256 45f6a7b5)

## 19 (whole dollars) — `ny_it2.city_whole`

- **IRS:** Local income tax withheld (New York City), in whole dollars
- **Encoded (NonNegDollars):** Round line 19 to the nearest multiple of (half up) $1.
- Expr: `{"of":"ny_it2.city_withheld","op":"round","rule":"half_up","unit":100}`
- Cite: [ny_it2] p. 2, Entering whole dollar amounts, "drop amounts below 50 cents and increase amounts from 50 to 99 cents to the next dollar" (Form IT-2 (2025), Summary of W-2 Statements; final 2025 edition (footer 'IT-2 (2025) (back)'); PDF modified 2025-09-26; sha256 45f6a7b5)
