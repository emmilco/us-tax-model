# Form 8283 — groups of similar noncash property

- Document: `gift` (form, tax year 2025)
- Collection: keyed entries; [i8283] pp. 1–3, Who Must File and Which Sections To Complete; f8283 Section A (December 2025; printed date 2026-01-30; sha256 2de015f7)
- Note: Group similar property across donees before testing $5,000. Values are supplied from valuation records; this does not determine fair market value or produce a completed signed Form 8283. Dates, descriptions and donee details remain in underlying records.

## (helper) — `gift.deduction`

- **Authored helper label:** Deduction before income limits for this item or group of similar items across all donees, after required valuation/basis reductions
- **Encoded (NonNegDollars):** Input — Deduction before income limits for this item or group of similar items (items of the same general category or type, such as coin collections, paintings, books, clothing, jewelry, nonpublicly traded stock, land or buildings) across all donees, after required valuation/basis reductions. Leave out clothing and household items not in good used condition or better, and any single gift of $250 or more for which you do not have a contemporaneous written acknowledgment from the organization
- Expr: `{"op":"input","source":"Deduction before income limits for this item or group of similar items (items of the same general category or type, such as coin collections, paintings, books, clothing, jewelry, nonpublicly traded stock, land or buildings) across all donees, after required valuation/basis reductions. Leave out clothing and household items not in good used condition or better, and any single gift of $250 or more for which you do not have a contemporaneous written acknowledgment from the organization"}`
- Cite: [i8283] pp. 1–3, Who Must File and Which Sections To Complete; f8283 Section A; p. 3, Similar Items of Property, "Similar items of property are items of the same general category or type, such as coin collections, paintings, books, clothing, jewelry, nonpublicly traded stock, land, or buildings."; i1040sca p. 11, Contributions of clothing and household items, "A deduction for these contributions will be allowed only if the items are in good used condition or better"; Gifts of $250 or more (December 2025; printed date 2026-01-30; sha256 2de015f7)

## (helper) — `gift.public_securities`

- **Authored helper label:** Is this group publicly traded securities (listed on a recognized stock exchange whose quotations are published daily, regularly traded on a national or regional over-the-counter market, or mutual fund shares quoted daily in a national newspaper of general circulation)?
- **Encoded (Bool):** Input — Is this group publicly traded securities? A security is generally publicly traded if it is (a) listed on a recognized stock exchange whose quotations are published daily, (b) regularly traded on a national or regional over-the-counter market, or (c) mutual fund shares quoted daily in a national newspaper of general circulation. Answer No for privately held stock, LLC or partnership interests, for stock that is neither listed on a recognized stock exchange nor regularly traded over the counter, even if it has a ticker symbol, and for securities subject to restrictions that materially affect their value to you or prevent them from being freely traded.
- Expr: `{"op":"input","source":"Is this group publicly traded securities? A security is generally publicly traded if it is (a) listed on a recognized stock exchange whose quotations are published daily, (b) regularly traded on a national or regional over-the-counter market, or (c) mutual fund shares quoted daily in a national newspaper of general circulation. Answer No for privately held stock, LLC or partnership interests, for stock that is neither listed on a recognized stock exchange nor regularly traded over the counter, even if it has a ticker symbol, and for securities subject to restrictions that materially affect their value to you or prevent them from being freely traded."}`
- Cite: [i8283] pp. 1–3, Who Must File and Which Sections To Complete; f8283 Section A; p. 9, Securities, "A security is generally considered to be publicly traded if the security is (a) listed on a recognized stock exchange whose quotations are published daily; (b) regularly traded on a national or regional over-the-counter market; or (c) quoted daily in a national newspaper of general circulation in the case of mutual fund shares" and "Nonpublicly traded securities may include, but are not limited to, privately held stock or shares in an entity such as an S corporation or a C corporation, privately held Limited Liability Company (LLC) membership, or privately held partnership interest"; cfr-26-1-170a-13 p. 12, Publicly traded securities, "shall not be considered publicly traded securities if— (1) The securities are subject to any restrictions that materially affect the value of the securities to the donor or prevent the securities from being freely traded" (December 2025; printed date 2026-01-30; sha256 2de015f7)

## (helper) — `gift.special`

- **Authored helper label:** Does this group need an appraisal or other special treatment: any of the following?

  - a noncash contribution reaching you through a Schedule K-1
  - vehicles
  - pass-through entity interests
  - intellectual property
  - inventory
  - conservation or partial interests
  - property with restrictions on its use
  - property other than qualified appreciated stock given to a private nonoperating foundation
  - stock given to a private nonoperating foundation, where you and your family have contributed more than 10% of the value of the corporation's outstanding stock
  - taxidermy property that you prepared, stuffed or mounted, or paid to have prepared, stuffed or mounted
  - tangible personal property held more than 1 year and worth more than its cost or other basis, that the charity puts to an unrelated use
  - a clothing or household item over $500 not in good used condition
  - property subject to a debt, such as a mortgage
- **Encoded (Bool):** Input — Does this group need an appraisal or other special treatment: any of the following?

  - a noncash contribution reaching you through a Schedule K-1
  - vehicles
  - pass-through entity interests
  - intellectual property
  - inventory
  - conservation or partial interests
  - property with restrictions on its use
  - property other than qualified appreciated stock given to a private nonoperating foundation
  - stock given to a private nonoperating foundation, where you and your family have contributed more than 10% of the value of the corporation's outstanding stock
  - taxidermy property that you prepared, stuffed or mounted, or paid to have prepared, stuffed or mounted
  - tangible personal property held more than 1 year and worth more than its cost or other basis, that the charity puts to an unrelated use
  - a clothing or household item over $500 not in good used condition
  - property subject to a debt, such as a mortgage
- Expr: `{"op":"input","source":"Does this group need an appraisal or other special treatment: any of the following?\n\n- a noncash contribution reaching you through a Schedule K-1\n- vehicles\n- pass-through entity interests\n- intellectual property\n- inventory\n- conservation or partial interests\n- property with restrictions on its use\n- property other than qualified appreciated stock given to a private nonoperating foundation\n- stock given to a private nonoperating foundation, where you and your family have contributed more than 10% of the value of the corporation's outstanding stock\n- taxidermy property that you prepared, stuffed or mounted, or paid to have prepared, stuffed or mounted\n- tangible personal property held more than 1 year and worth more than its cost or other basis, that the charity puts to an unrelated use\n- a clothing or household item over $500 not in good used condition\n- property subject to a debt, such as a mortgage"}`
- Cite: [i8283] pp. 1–3, Who Must File and Which Sections To Complete; f8283 Section A; p. 3, Similar Items of Property, "Similar items of property are items of the same general category or type, such as coin collections, paintings, books, clothing, jewelry, nonpublicly traded stock, land, or buildings."; p. 9, Securities, "A security is generally considered to be publicly traded if the security is (a) listed on a recognized stock exchange whose quotations are published daily"; p. 1, "Make any required reductions to the amount of the contributions before you determine if you must file Form 8283"; p. 3, Section B, "Include in Section B only items (or groups of similar items) for which you claimed a deduction of more than $5,000"; cfr-26-1-170a-13 p. 3, Deductions in excess of $5,000 for certain charitable contributions of property, "if the amount claimed or reported as a deduction under section 170 with respect to such item exceeds $5,000" (a group over $5,000 is refused by gift.section_b from gift.deduction); p526 p. 19, Capital Gain Property, "Capital gain property includes capital assets held more than 1 year", Exceptions, "you must reduce the FMV by any amount that would have been long-term capital gain if you had sold the property for its FMV", items 1, "The property (other than qualified appreciated stock) is contributed to certain private nonoperating foundations", and 5, "tangible personal property (defined earlier) that: a. Is put to an unrelated use (defined later) by the charity"; p526 p. 18, Giving Property That Has Decreased in Value, "your deduction is limited to its FMV" and "Common examples of property that decrease in value include clothing, furniture, appliances, and cars" (no reduction is left to make on such property, so the unrelated-use item asks only of property held more than 1 year and worth more than its basis); p526 p. 19, Contributions to private nonoperating foundations, "stock in a corporation doesn’t count as qualified appreciated stock to the extent you and your family contributed more than 10% of the value of all the outstanding stock in the corporation"; p526 p. 12, Taxidermy Property, "your deduction is limited to your basis in the property or its FMV, whichever is less. This applies if you prepared, stuffed, or mounted the property or paid or incurred the cost of preparing, stuffing, or mounting the property"; p526 p. 12, Property Subject to a Debt, "If you contribute property subject to a debt (such as a mortgage), you must reduce the FMV of the property by" (December 2025; printed date 2026-01-30; sha256 2de015f7)

## (helper) — `gift.over_5000`

- **Authored helper label:** The deduction for this item or group is more than $5,000
- **Encoded (Bool):** helper "Deduction before income limits for this item or group of similar items across all donees, after required valuation/basis reductions" > $5,000
- Expr: `{"gt":["gift.deduction",{"const":500000}],"op":"test"}`
- Cite: [i8283] pp. 1–3, Who Must File and Which Sections To Complete; f8283 p. 1, Section B, "for which you claimed a deduction of more than $5,000 per item or group (except contributions reportable in Section A)" (December 2025; printed date 2026-01-30; sha256 2de015f7)

## (helper) — `gift.not_public`

- **Authored helper label:** This group is not publicly traded securities
- **Encoded (Bool):** helper "Is this group publicly traded securities (listed on a recognized stock exchange whose quotations are published daily, regularly traded on a national or regional over-the-counter market, or mutual fund shares quoted daily in a national newspaper of general circulation)?" = false
- Expr: `{"eq":["gift.public_securities",{"const":false}],"op":"test"}`
- Cite: [i8283] pp. 1–3, Who Must File and Which Sections To Complete; f8283 p. 1, Section A, "Also list publicly traded securities and certain other property even if the deduction is more than $5,000" (December 2025; printed date 2026-01-30; sha256 2de015f7)

## (helper) — `gift.no`

- **Authored helper label:** Year parameter sa.no (no)
- **Encoded (Bool):** Enter false (sa.no).
- Expr: `{"op":"param","ref":"sa.no"}`
- Cite: [i8283] pp. 1–3, Who Must File and Which Sections To Complete; f8283 Section A (December 2025; printed date 2026-01-30; sha256 2de015f7)

## (helper) — `gift.section_b`

- **Authored helper label:** Appraisal threshold: non-publicly-traded group over $5,000
- **Encoded (Bool):** Choose — [helper "The deduction for this item or group is more than $5,000" = true → helper "This group is not publicly traded securities"] [helper "The deduction for this item or group is more than $5,000" = false → helper "Year parameter sa.no (no)"]
- Expr: `{"alternatives":[{"guard":{"eq":["gift.over_5000",{"const":true}],"op":"test"},"then":"gift.not_public"},{"guard":{"eq":["gift.over_5000",{"const":false}],"op":"test"},"then":"gift.no"}],"op":"choose"}`
- Cite: [i8283] pp. 1–3, Who Must File and Which Sections To Complete; f8283 p. 1, Section A, "Also list publicly traded securities and certain other property even if the deduction is more than $5,000", Section B, "for which you claimed a deduction of more than $5,000 per item or group (except contributions reportable in Section A)" (December 2025; printed date 2026-01-30; sha256 2de015f7)

## (helper) — `gift.allowed`

- **Authored helper label:** Amount from gift.deduction
- **Encoded (NonNegDollars):** Enter the amount from helper "Deduction before income limits for this item or group of similar items across all donees, after required valuation/basis reductions".
- **Refusal:** when gift.special is true, cannot complete Form 8283 special treatment. This contribution requires unsupported appraisal or special-property treatment. Cite: [i8283] pp. 1–3, Who Must File and Which Sections To Complete; f8283 Section A (December 2025; printed date 2026-01-30; sha256 2de015f7)
- **Refusal:** when gift.section_b is true, cannot complete Form 8283 Section B. A group of similar items over $5,000 requires Section B and a qualified appraisal; publicly traded securities are excepted. Cite: [i8283] pp. 1–3, Who Must File and Which Sections To Complete; f8283 Section A (December 2025; printed date 2026-01-30; sha256 2de015f7)
- Expr: `{"from":"gift.deduction","op":"copy"}`
- Cite: [i8283] pp. 1–3, Who Must File and Which Sections To Complete; f8283 Section A (December 2025; printed date 2026-01-30; sha256 2de015f7)
