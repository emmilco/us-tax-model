# Adjudication — sales

Method: `README.md` in this directory. Earlier rulings were made in the logs' sidecars (archived in
`.transcription/archive/before-fix-round2-2026-10-30/`), and no summary was kept for them.

## Fix round 2 (superseded subject)

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

## Backlog round

Fresh reviews of 2026-11-03 of the subject after the income package: PENDING-5 adds `sales.wash_over` and the entry-error
gate `sales.wash_bad`, refusing at `sales.w` when a code W loss is larger than the loss after the code B correction (owner's
decision 2026-11-01); PENDING-6 rewords `sales.special` (an interest in a partnership, S corporation or trust, including S
corporation stock, that holds collectibles or section 1250 property). Triage: `../triage/sales[.deepseek].json`, written
by triage.py this round (executable-triage-v2: 1,495 fixtures, 500 generated returns seed 20261026, 510 partial records
from 40 bases; 1,837 comparisons); every witness re-read from an uncapped scratch re-run, same counts. Class M log
(`../../classm/sales.md`, classm.sales.1, 9 lines): all agree, including a code W loss of $45 within a $24,250 loss.
Full ruling text: `.transcription/proposed/bklg/{transcription,render}.sales[.deepseek].json`.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | (e) | model error and scope | 1,423 agree; 44 completed candidate-refuses, all h_basis_bad (correct basis on a box A/D entry without code B: never asked; checked on classm.f1040.2 with it withheld) | i8949 p. 8, code B | A consistency check on an unasked answer; G/J refused by `sales.digital`. |
| claude | transcription | (g) | representation | 1,831 agree; 6 project-unknown on partials withholding box, proceeds or correct basis; none completed | i8949 p. 10, code W | The reply's h_wash_bad is the project's new gate within the interview. |
| deepseek | transcription | (e) | scope | 7 values, all box G/J on refused returns; 2 unknowns on a refused partial | f8949 p. 1, box G | G/J refused by `sales.digital`. |
| deepseek | transcription | (g) | scope | 3 project-refuses on `sales.wash_bad` (sales.refuse.wash_over_loss, generated 256, 310), refused by the reply at (h) | i8949 p. 10, code W | Same limit, one line later. |
| claude | render | (e), (g) | scope | MISMATCH; fixtures sales.refuse.digital.G and sales.refuse.code pass | f8949 p. 1; i8949 pp. 7-11 | Boxes G-L and codes other than B/W refused at `sales.one`. |

Package check: `sales.wash_over` equals column (h), so `sales.wash_bad` refuses exactly when (h) would exceed zero; a loss
equal to the wash amount is accepted (sales.adjust.A.W.equal_loss, (h) $0.00) and the code B correction counts
(sales.adjust.D.BW.wash_within_corrected_loss, (h) −$500.00), both evaluated. It refuses no allowable entry. The
`sales.special` wording matches i1040sd pp. 11-12 and can only refuse. The fix-round-2 finding F1 is fixed (BUG-0257): no
candidate-unknown is on a completed return now (29 before). O1 (a wash loss on a gain sale) is closed by `sales.wash_bad`.
Findings: none.

