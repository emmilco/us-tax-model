# Adjudication — sales

Method: `README.md` in this directory. Earlier rulings were made in the logs' sidecars (archived in
`.transcription/archive/before-fix-round2-2026-10-30/`), and no summary was kept for them.

## Fix round 2

The subject after BUG-0231 widened the `sales.special` question to cover shares of an exchange-traded fund or trust that
holds gold, silver, platinum or other metals. No sales expression changed. Both families were reviewed. Triage is
`../triage/sales[.deepseek].json` (executable-triage-v2: 1,382 fixtures, 500 generated returns with seed 20261026, 630
partial records from 40 bases, 2,245 comparisons). An uncapped scratch re-run gave the same counts. The rulings are in
`.transcription/proposed/fixr2/` (`transcription.sales[.deepseek].json` and `render.sales[.deepseek].json`).

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | (e) | model error, finding (F1), scope | 70 completed candidate-refuses on h_basis_uncoded (correct basis on a box A/D entry without code B: never asked); 29 completed candidate-unknown (special 28, aggregate_eligible 1) | i8949 p. 8, code B; i1040sd p. 11 | G/J refused by sales.digital; a consistency check on an unasked answer; F1 witnesses. |
| claude | transcription | (g) | model error, finding (F1), scope | as (e), plus 17 completed h_wash_excess (classm.s3.2 s3: wash loss $449 on a gain) | i8949 p. 10, code W | The source states no such limit (observation O1). |
| deepseek | transcription | (e), (g) | scope and finding (F1) | 7 values, all box G/J, refused; 28 completed candidate-unknown on special | f8949 p. 1; i1040sd p. 11 | G/J refused by sales.digital; F1 witnesses. |
| both | render | (e), (g) | scope | MISMATCH | f8949 p. 1; i8949 pp. 7-11 | Boxes G-L and codes other than B/W refused at sales.one (checked to Form 1040). |

Findings (`.transcription/proposed/fixr2/sales.findings.md`): F1 (SCREEN-UNANSWERED-PASSES, medium, predates the round):
when `sales.special` or `sales.aggregate_eligible` is unanswered (withheld or null), `sd.screen` evaluates false through the
engine's Count lower-bound shortcut, and the return completes as if the answer were no. O1 (observation): a wash-sale loss
entered on a gain sale is accepted. The brief's check: the BUG-0231 gloss matches i1040sd p. 11 ("metals"; a trust
"attributable to unrealized appreciation of collectibles"). It is not narrower than the source, and an over-reading can
only refuse.
