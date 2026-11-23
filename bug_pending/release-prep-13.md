## BUG-NEW-release-prep-13 — A rental's taxes carried to Schedule A line 5b skip the non-deductible-charges question

- **Date:** 2026-11-23
- **Caught by:** the sampled reviews of the release run, adjudicated in release preparation 2 (claude-opus-5-5, judgment), 2026-11-23: completeness claim rental#1.4.
- **Source:** i1040sca p. 6, Line 5b: taxes 'assessed uniformly', not itemized service charges, not foreign real estate taxes, only what the lender actually paid, only taxes assessed before 2026, reduced by 2025 refunds.
- **Symptom:** rental.tax_personal carries the part of a rental's taxes not taken on Schedule E (personal-use days) to Schedule A line 5b, but sa.property_tax_other_any asks only about 'the real estate tax amount you entered' for sa.line5b. A service charge, a refund or a tax assessed after 2025 inside the rental's tax reaches line 5b unchecked; the rental.amt16 question excludes only improvement charges.
- **Where:** forms/2025/rental.yaml rental.tax_personal; forms/2025/sa.yaml sa.property_tax_other_any (its wording and readers).
- **Proposed fix:** Word sa.property_tax_other_any to cover 'that amount, or the taxes of a rental that was also your home', or ask the rental.amt16 help to leave out the same items.
- **Proposed fix lines:** sa.property_tax_other_any, rental.amt16
- **Severity:** low
- **Tags:** sa, rental, completeness review; open
