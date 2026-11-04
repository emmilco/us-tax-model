# Round 3 (2026-11-04): low findings for one batch entry, BUG-0417

Completeness lows are ruled `real gap` with `"bug": "BUG-0417"` in `reviews/2025/completeness/rulings.json`. Both
are rare Pub. 550 details. Proposed fix in brackets; fixed with the next sales pass (T-233).

| claim | source | gap [fix] |
| --- | --- | --- |
| sales#2 | p550 p. 88; i1040sd p. 6 | `sales.box` does not say the premium of an unexercised written option is short-term, that an expired purchased option is treated as sold on its expiration date, that a securities futures contract to sell gives short-term gain or loss, or the holding period of stock received in a demutualization [state them in `sales.box`]. |
| sales#4 | p550 p. 88 | `sales.wash_loss` gives the 30-day window; for a REMIC residual interest it is 6 months, and comparable taxable mortgage pool interests count as replacements [state it]. |
