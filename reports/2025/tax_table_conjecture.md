# Tax Table midpoint conjecture — result for 2025

Method: for every band of `tax_table` and every filing-status column, compute the
exact rate-schedule tax (`rate_schedule`, Rev. Proc. 2024-40 section 3.01, with
qualifying surviving spouses aliased to the joint schedule) at the band's midpoint
(at_least + less_than) / 2, then round to whole dollars half-up. Compare with the
printed cell. This is the conjecture from `spec/spec.md` section 6.3, tested, not
assumed.

- Cells tested: 8248 (2062 bands x 4 columns)
- Matching cells: 8248
- Mismatching cells: 0

Result: the conjecture holds for every cell under the half-up whole-dollar rounding
rule. The rule is recorded for the test harness: `round_half_up_to_whole_dollars
(schedule_at(midpoint))`.
