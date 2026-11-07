# New York screen adjudication, gate lane D (2026-11-07)

Gate lane D gave six New York questions formal gates (`gated_by`), which brought them into the screen review
(BUG-0448). Each was reviewed once (Claude, `claude-opus-5-5`). Rulings are in `rulings.json` under
`unruled:<screen>` with each review's `prompt_sha`. Quotes were checked against `sources/ny/2025/ny_it201i.cols.txt`
(pp. 9, 15, 19, 23), and the wording the filer reads against `forms/ny/2025/ny_it201.yaml` and
`interview/ny/questions-2025.yaml`. Each question refuses on Yes.

| screen | verdict | findings (n: class) | disposition |
| --- | --- | --- | --- |
| `ny_it201.ask.dependent_care` | UNCLEAR | 0: out of scope / presentation | No defect. The question is IT-201-I p. 19 line 64 word for word, and it is reached only when the filer paid care or received benefits (`ny_it201.federal_care`). A filer with zero federal tax might read "qualify" as "got an amount" and answer No, losing a refundable credit; a paper filer faces the same words. Optional gloss: "even if your federal tax was zero". |
| `ny_it201.ask.gov_pension` | WIDE | 0, 1: accepted WIDE; 2: accepted (minor UNCLEAR) | No defect. The 457 and private-university/TIAA cases are refused for nothing. Agencies, instrumentalities and possessions read as "federal government" or "a U.S. territory"; the source itself says "certain public authorities, including". A filer 59 1/2 or older who wrongly answers No is still refused by `pension_exclusion`. |
| `ny_it201.ask.mctmt` | UNCLEAR | 0: accepted (minor UNCLEAR, leans WIDE); 1: defect | Gap, low: **BUG-0450**. Reading the two zones as combined only refuses more. Zone 2 is undefined in the question ("the suburban counties" in the help), so a filer with a business in, for example, Orange or Dutchess County may answer No and the MCTMT is omitted. |
| `ny_it201.ask.pension_exclusion` | WIDE | 0, 1, 2: accepted WIDE | No defect. Non-qualifying lump sums, QDRO and own-funds annuities, and income received before turning 59 1/2 are all refused for nothing. |
| `ny_it201.ask.refund_529` | NARROW | 0: low | Gap, low: **BUG-0449**. "Part of a refund" may draw No from a filer who wants the whole refund deposited (p. 23: "all or a portion"). The refund then goes to the filer and the election is lost; no tax amount is wrong, and no other question covers Form IT-195. |
| `ny_it201.ask.us_obligation_interest` | WIDE | 0: accepted WIDE; 1: out of scope / presentation; 2: scope: refused federally | No defect. A fund failing the 50% test is refused for nothing. The agency-obligation question is the source's own term ("bonds or other obligations of the U.S. government"), with nothing archived to sharpen it. Line 11 K-1 interest is refused federally by `scope.schedule1`. |

No form data was changed; the two gaps wait for a wording change to these questions, with their screen reviews
rerun then. No paid call was made in adjudication.
