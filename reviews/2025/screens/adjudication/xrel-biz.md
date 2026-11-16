# Screen and false-no adjudication, release sample (xrel, family biz)

Ruled by the biz fork (claude-opus-5-5, judgment) with eight sub-lanes (L1 to L8), each checking quotes against `sources/2025/*.cols.txt`, the form YAML, the interview wording and, where an amount mattered, engine evals on fixture copies under `/tmp/xrel/biz/`. The fork merged duplicates (one bug per defect), checked a sample of rulings (s179.mfs still refuses a separate-return election; the home equity part of the interest finding is refused by sa.mortgage_other_use and was removed from BUG-0777), and filed the pending bugs. Fragments: `/tmp/xrel/frag/biz.<tool>.json`; `xrel.py merge` (validate only) prints no REFUSED line. `rulings.json` was not edited.

## Screens

Samples: 32. Findings: 97. Classes: covered 20, accepted WIDE 18, defect 15, presentation 13, accepted residual 11, out of scope 10, model error 7, open residual 3.

| sample | findings (n: class) | disposition |
|---|---|---|
| `gate:asset.claims_bonus#1` | 0: out of scope; 1: out of scope; 2: out of scope; 3: accepted WIDE | no gate defect; 60%, QPP and specified-plant cases are refused before the gate, WIDE accepted |
| `gate:asset.industry#1` | 0: covered; 1: defect (BUG-0791); 2: open residual (BUG-0791); 3: presentation | defect (low): the industry tick asks about the business, so item-defined reuse/recycling property owned outside a recycling business skips the refusal; energy property covered by the class question |
| `gate:asset.listed#1` | 0: out of scope; 1: open residual (BUG-0565); 2: open residual (BUG-0565); 3: out of scope; 4: presentation; 5: defect (BUG-0790); 6: accepted WIDE | defect (medium): the redraft wording narrows listed entertainment property to "equipment" with camera and recording examples, dropping communication equipment and property such as a boat; other … |
| `gate:asset.placed_this_year#1` | 0: model error; 1: model error; 2: model error | no gate defect; the three findings read the gate as inverted from the review prompt's polarity text (BUG-0800) |
| `gate:rental.has_advertising#1` | 0: covered; 1: covered; 2: presentation | no gate defect; royalty and bare-label readings are answered by the roster and the group heading; one wording point |
| `gate:rental.has_commissions#1` | 0: covered; 1: accepted WIDE | no gate defect; the heading asks what was paid in 2025; the purchase-commission Yes is accepted WIDE |
| `gate:rental.has_insurance#1` | 0: defect (BUG-0787); 1: defect (BUG-0787) | defect: the 2025 part of a premium prepaid in an earlier year is excluded (low); the Line 9 citation points to no text (low) |
| `gate:rental.has_legal#1` | 0: covered; 1: covered; 2: covered; 3: defect (BUG-0776) | no gate defect; the tick names tax preparation and royalties are asked elsewhere; the amount question omits the capitalization exclusion (low) |
| `gate:rental.has_management#1` | 0: covered; 1: covered; 2: accepted WIDE | no gate defect; the heading asks about paying; royalties are asked elsewhere; the Yes without a 2025 amount is accepted WIDE |
| `gate:rental.has_mortgage#1` | 0: covered; 1: presentation; 2: accepted WIDE | no gate defect; findings answered by the sibling tick, a refusal or the interview wording |
| `gate:rental.has_other#1` | 0: presentation; 1: covered; 2: accepted residual | no gate defect; findings answered by the interview tick, a refusal or a low residual |
| `gate:rental.has_other_interest#1` | 0: covered; 1: covered | no gate defect; findings answered by the interview tick and the gated question |
| `gate:rental.has_repairs#1` | 0: covered; 1: covered | no gate defect; maintenance is asked by the neighbouring tick |
| `gate:rental.has_supplies#1` | 0: presentation; 1: defect (BUG-0788) | no gate defect; one low citation defect (the gate cites a page with no Line 15 text) |
| `gate:rental.has_taxes#1` | 0: out of scope; 1: presentation | no gate defect; the royalty case is another document; the label is the review prompt's |
| `gate:rental.has_utilities#1` | 0: accepted residual; 1: accepted residual; 2: accepted WIDE | no gate defect; telephone-only costs reach the deduction through "Other costs of renting it"; low wording residual |
| `gate:rental.prior_any#1` | 0: defect (BUG-0785); 1: presentation; 2: accepted WIDE | defect: a spouse's separate earlier return is not named (low) |
| `gate:rental.short_stays#1` | 0: out of scope; 1: presentation | no gate defect; one class per entry; year-crossing stays are wording |
| `gate:s179.prior_form_if_before#1` | 0: accepted residual; 1: accepted residual; 2: accepted WIDE | no gate defect; the findings are wording points on the parent scope.business_before, low |
| `gate:sc.employees#1` | 0: out of scope; 1: accepted residual | no gate defect; self-employed dependent care contributions are refused by sc.special, former-employee payments a low residual |
| `gate:sc.goods#1` | 0: covered; 1: covered; 2: accepted WIDE | no gate defect; the page tick names goods bought or made to sell |
| `gate:sc.travel_meals#1` | 0: accepted residual; 1: accepted residual; 2: accepted residual; 3: accepted WIDE | no gate defect; findings are low wording residuals of 'paid for' |
| `gate:scveh.others_use#1` | 0: covered; 1: accepted residual; 2: accepted residual | no gate defect; investment use is refused by scveh.investment, the rest are low residuals |
| `gate:scveh.placed_this_year#1` | 0: model error; 1: model error; 2: model error; 3: covered | no gate defect; the three NARROW findings misread the gate's polarity (model error) |
| `rental.not_at_risk#1` | 0: defect (BUG-0781); 1: model error; 2: defect (BUG-0781); 3: accepted WIDE; 4: defect (BUG-0781) | defect: at-risk question reaches only nonrecourse loans from non-lenders (low) |
| `rental.not_for_profit#1` | 0: accepted WIDE; 1: accepted WIDE | no gate defect; both readings err wide (refusal) |
| `rental.part_home#1` | 0: defect (BUG-0782); 1: defect (BUG-0782); 2: accepted WIDE | defect: part-of-property refusal misses a part the filer uses otherwise or lived in earlier in 2025 (low) |
| `rental.prior_not_active#1` | 0: defect (BUG-0783); 1: out of scope; 2: accepted WIDE; 3: presentation | defect: earlier-year test omits the 10% ownership bar (low) |
| `rental.services#1` | 0: accepted WIDE; 1: accepted WIDE; 2: defect (BUG-0784) | defect: services provided through a manager may be answered No (low) |
| `rental.stay7#1` | 0: covered; 1: out of scope | no gate defect; services covered by rental.services; one class of property per entry |
| `rental.under_tenth#1` | 0: accepted WIDE; 1: defect (BUG-0783); 2: presentation | defect: 10% test has no 'at any time' (low) |
| `rental.vehicle#1` | 0: presentation; 1: presentation | no gate defect; wording only |

## False-no

Samples: 29. Findings: 145. Classes: covered 40, accepted residual 35, presentation 25, defect 20, out of scope 12, open residual 7, model error 5, accepted WIDE 1.

| sample | findings (n: class) | disposition |
|---|---|---|
| `gate:asset.claims_bonus#1` | 0: out of scope; 1: out of scope; 2: covered; 3: model error; 4: open residual (BUG-0565); 5: out of scope | no gate defect; 60% and QPP cases refused before the gate, election-out wording covered, fiscal year recorded (BUG-0565), spouse transfer refused |
| `gate:asset.industry#1` | 0: covered; 1: defect (BUG-0791); 2: open residual (BUG-0791); 3: presentation; 4: open residual (BUG-0791); 5: model error; 6: presentation | defect (low): BUG-0791, item-defined reuse/recycling property (and, recorded, gathering lines, transmission property and racetracks) owned outside the named businesses skips the … |
| `gate:asset.listed#1` | 0: out of scope; 1: defect (BUG-0790); 2: open residual (BUG-0565); 3: open residual (BUG-0565); 4: presentation | defect (medium): BUG-0790, listed entertainment property narrowed to camera and recording "equipment"; vehicles refused, pre-2018 peripherals and operator condition recorded (BUG-0565), … |
| `gate:asset.placed_this_year#1` | 0: model error; 1: covered; 2: covered; 3: covered | no gate defect; the inverted-gate finding is the review prompt's polarity text (BUG-0800); qualified-use and conversion cases covered |
| `gate:asset.software#1` | 0: presentation; 1: presentation; 2: presentation; 3: out of scope | no gate defect; software wording lows (custom code, licences, separately stated software) recorded as presentation; acquired-business software out of scope |
| `gate:rental.has_advertising#1` | 0: defect (BUG-0786); 1: covered; 2: presentation; 3: presentation; 4: covered | defect: accrual-method expenses are not asked (low); the other findings are covered or wording |
| `gate:rental.has_cleaning#1` | 0: presentation; 1: presentation; 2: defect (BUG-0786); 3: covered | defect: accrual-method expenses are not asked (low); the rest is wording or covered |
| `gate:rental.has_commissions#1` | 0: out of scope; 1: presentation; 2: covered | no gate defect on the archived sources; the lease-term commission rule is not archived; the platform fee is wording |
| `gate:rental.has_insurance#1` | 0: defect (BUG-0787); 1: presentation; 2: covered; 3: presentation; 4: defect (BUG-0788) | defect: the 2025 part of a premium prepaid in an earlier year is not asked (low); the Line 9 citation names no text (low); the rest is wording |
| `gate:rental.has_legal#1` | 0: covered; 1: presentation; 2: covered; 3: covered; 4: presentation; 5: defect (BUG-0776) | no false no; the tick names tax preparation; the capitalization exclusion is missing from the amount question (low) |
| `gate:rental.has_loss#1` | 0: model error; 1: defect (BUG-0781); 2: defect (BUG-0781); 3: defect (BUG-0781); 4: defect (BUG-0781); 5: defect (BUG-0781); 6: open residual (BUG-0781); 7: presentation | defect: at-risk question reaches only nonrecourse loans from non-lenders (low) |
| `gate:rental.has_management#1` | 0: presentation; 1: presentation; 2: covered; 3: defect (BUG-0786); 4: covered | defect: accrual-method expenses are not asked (low); fees kept from rent and co-host fees are wording |
| `gate:rental.has_mortgage#1` | 0: covered; 1: covered; 2: accepted residual; 3: covered; 4: accepted residual; 5: covered; 6: presentation | no gate defect; the false-no case is answered by the sibling tick and a refusal; the rest are presentation, refused or low residuals |
| `gate:rental.has_other#1` | 0: presentation; 1: covered; 2: accepted residual; 3: accepted residual | no gate defect; findings presentation, refused, optional, or low |
| `gate:rental.has_other_interest#1` | 0: covered; 1: covered; 2: covered; 3: accepted residual; 4: accepted residual; 5: presentation | no gate defect; findings answered by the tick wording or refusals; two low residuals |
| `gate:rental.has_repairs#1` | 0: covered; 1: accepted residual; 2: defect (BUG-0789); 3: covered | defect (shared with other expense gates): an expense a tenant paid is counted in rent but not asked as an expense; the rest covered or low |
| `gate:rental.has_supplies#1` | 0: covered; 1: accepted residual; 2: accepted residual; 3: defect (BUG-0788) | no gate defect; findings covered by the neighbouring tick or low; the citation defect is the one filed from the screen sample |
| `gate:rental.has_taxes#1` | 0: out of scope; 1: covered; 2: defect (BUG-0789) | defect (shared with other expense gates): a tax the tenant paid is counted in rent but not asked as an expense; the rest out of scope or refused |
| `gate:rental.has_utilities#1` | 0: accepted residual; 1: out of scope; 2: defect (BUG-0789); 3: accepted residual | defect (shared): a utility the tenant paid and deducted from rent is in rent but not asked as an expense; the rest low or another document |
| `gate:rental.prior_and_active#1` | 0: defect (BUG-0783); 1: out of scope; 2: covered; 3: covered; 4: accepted WIDE | defect: earlier-year test omits the 10% ownership bar (low) |
| `gate:rental.prior_any#1` | 0: defect (BUG-0785); 1: covered; 2: covered; 3: presentation; 4: defect (BUG-0785) | defect: spouse's separate return and a grouped activity can drop a carryover (low) |
| `gate:rental.short_stays#1` | 0: out of scope; 1: covered; 2: presentation; 3: presentation | no gate defect; one class per entry; the counting terms are defined |
| `gate:s179.prior_form_if_before#1` | 0: accepted residual; 1: accepted residual; 2: accepted residual; 3: covered | no gate defect; Form 2106 carryovers are outside the tool, the rest are low wording residuals on the parent |
| `gate:sc.employees#1` | 0: accepted residual; 1: accepted residual; 2: accepted residual; 3: accepted residual; 4: out of scope; 5: presentation | no gate defect; 'people it paid wages to' takes 2025 payments to former employees, self dependent care is refused by sc.special |
| `gate:sc.goods#1` | 0: covered; 1: covered; 2: accepted residual; 3: accepted residual | no gate defect; the tick 'Goods it bought or made to sell' takes the destroyed-goods case, the rest are low residuals |
| `gate:sc.travel_meals#1` | 0: accepted residual; 1: accepted residual; 2: accepted residual; 3: accepted residual; 4: accepted residual; 5: accepted residual | no gate defect; low wording residuals of 'it paid for' |
| `gate:scveh.others_use#1` | 0: covered; 1: accepted residual; 2: accepted residual; 3: accepted residual; 4: accepted residual | no gate defect; investment use is refused by scveh.investment, the rest are low residuals |
| `gate:scveh.placed_this_year#1` | 0: model error; 1: covered; 2: out of scope; 3: open residual (BUG-0792); 4: accepted residual; 5: covered; 6: accepted residual; 7: accepted residual | no gate defect; finding 0 misreads the gate's polarity; one open residual on prior_low_use's own wording (conversion-year proration) |
| `gate:scveh.smr_always#1` | 0: accepted residual; 1: covered; 2: accepted residual; 3: covered | no gate defect; the help covers any earlier year, the fleet bar is asked separately |

## Notes

- The review prompt shows the form wording ("For this rental property — X") where the filer sees ticks under "Did you pay any of these for this rental in 2025?"; many bare-label findings are presentation for that reason.
- Several placed_this_year findings are model errors from the prompt's polarity text (already pending as BUG-0800).
- Not filed (fork's judgment, presentation): the carloan note says to name each loan by VIN but the `$carloan` prompt says "for example by its lender"; the VIN changes no amount.

## Pending bugs filed by this fork

| id | severity | title |
|---|---|---|
| BUG-0775 | medium | rental: a home converted to a rental in 2025 deducts the whole year's expenses, because main-home days are left out of the expense division |
| BUG-0776 | low | rental cost questions do not exclude capitalized legal fees and capital purchases |
| BUG-0777 | low | rental mortgage interest is not allocated by the use of the loan proceeds |
| BUG-0778 | low | rental: a Worksheet 5-1 carryover from an earlier year is neither asked nor refused |
| BUG-0779 | low | rental: Form 8582 exceptions 3 to 6 (incidental rentals, business-hours use) and dealer property are not screened |
| BUG-0780 | low | sc.special names the lease inclusion amount only by its official term |
| BUG-0781 | low | Rental at-risk question reaches only nonrecourse loans from non-lenders |
| BUG-0782 | low | Part-of-property refusal misses a part the filer uses otherwise or lived in earlier in 2025 |
| BUG-0783 | low | Rental 10% ownership test: no 'at any time' in 2025, and not asked for the year a held-back loss arose |
| BUG-0784 | low | Rental services question can be answered No when a manager provides the services |
| BUG-0785 | low | Held-back rental loss question omits the spouse's separate earlier return and a grouped activity |
| BUG-0786 | low | rental expenses ask only what was paid in 2025; an accrual-method landlord's expenses incurred for 2025 are not asked |
| BUG-0787 | low | rental insurance: the 2025 part of a premium prepaid in an earlier year is excluded by the gate and the amount question |
| BUG-0788 | low | rental citations name Line 8, Line 9 (and Line 15) instructions that i1040se does not have |
| BUG-0789 | medium | Rental expenses a tenant paid are counted in rent but not asked as expenses |
| BUG-0790 | medium | asset.listed: the redraft prompt narrows listed entertainment property to camera and recording "equipment", so a boat or communication equipment used 50% or less is depreciated instead of refused |
| BUG-0791 | low | asset.industry asks about the business, so item-defined property (reuse and recycling equipment, a gas gathering line, transmission property, a race track) owned outside the named businesses skips the asset.industry_item refusal |
| BUG-0792 | low | The earlier-year low-use question does not prorate the business use of the year a vehicle was converted from personal use |
