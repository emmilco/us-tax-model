# Render comparison — sales

The rendered English of every printed line of `Form 8949 and Schedule D — manually classified securities transactions` (`rendered/2025/sales.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 52fcec313b912a306525806a211cdc13937f210340d190810eb19cf434ced46d |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 913d7bd7361f8781fad6e9e34c411bbe6bd93d16fba1df2a3150b2913c23e7f2 |
| lines judged | 3 |
| match / mismatch / unclear / missing | 1 / 2 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8949 | 2025; printed date 2026-01-20 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 | cited pages | d3ddc2b91cf89087ca348ebb00dbd1c80bbc025fa4df1176753d25013f581a67 | 2, 3, 4, 5, 6, 7, 9, 10 | cabdc81a0677c0e4de4a89f9a71d328395c4cc839206ebadb56aeb54bf954b85 |
| i1040sd | 2025; printed date 2025-12-11 | 10, 11, 12 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 11, 12 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| f8949 | 2025; created 2025-05-05 | 1, 2 | whole document | f191f96ca2847b4c59875d5e1169f784a79b4d57f1f12d0196bd9bc2e7838e9d | - | cc308c3ff7751456647bed9c2855d077dcbd0a55469b57f9e8cccb6f4927f232 |

## Lines

### (e) — Column (e): reported basis if covered; correct basis otherwise
Status: **MISMATCH**

Restated: Choose — [helper "Basis reported to IRS" = true → helper "Basis shown on broker report"] [helper "Basis reported to IRS" = false → helper "Correct adjusted basis from records"]

Model: The restatement treats only A/D as 'Basis reported to IRS'; IRS column (e) says 'For covered securities, enter the basis shown on Form 1099-B or Form 1099-DA (or substitute statement) in column (e),' and Box G/J transactions also have basis reported to the IRS, so G/J would wrongly use correct basis instead of reported basis.

Ruling: open

### (g) — Column (g): net adjustments
Status: **MISMATCH**

Restated: Add helper "Basis correction in column (g)" and helper "Wash-sale adjustment in column (g)".

Model: The basis-correction helper is gated on 'Basis reported to IRS' being true only for A/D; for Box G/J with code B the IRS table says to 'enter the basis shown on Form 1099-B or Form 1099-DA (or substitute statement) in column (e), even though that basis is incorrect. Correct the error by entering an adjustment in column (g),' but the restatement would enter no basis correction.

Ruling: open

### (h) — Column (h): proceeds less basis plus adjustments
Status: **MATCH**

Model: IRS column (h) says to 'Subtract column (e) from column (d) and combine the result with column (g),' and the restatement subtracts column (e) from column (d) and adds column (g).

## Raw response

```yaml
lines:
  - key: "(e)"
    status: MISMATCH
    reason: "The restatement treats only A/D as 'Basis reported to IRS'; IRS column (e) says 'For covered securities, enter the basis shown on Form 1099-B or Form 1099-DA (or substitute statement) in column (e),' and Box G/J transactions also have basis reported to the IRS, so G/J would wrongly use correct basis instead of reported basis."
  - key: "(g)"
    status: MISMATCH
    reason: "The basis-correction helper is gated on 'Basis reported to IRS' being true only for A/D; for Box G/J with code B the IRS table says to 'enter the basis shown on Form 1099-B or Form 1099-DA (or substitute statement) in column (e), even though that basis is incorrect. Correct the error by entering an adjustment in column (g),' but the restatement would enter no basis correction."
  - key: "(h)"
    status: MATCH
    reason: "IRS column (h) says to 'Subtract column (e) from column (d) and combine the result with column (g),' and the restatement subtracts column (e) from column (d) and adds column (g)."
```
