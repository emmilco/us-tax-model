# royalty adjudication

Adjudication of the review logs of royalty (new form of the coverage expansion, lane x1-sche).

## Goal-1 round (2026-11-15)

Lane xrev-new (claude-opus-5-5, judgment, tax year 2025, jurisdiction us), worktree x1-sche (uncommitted). Whole-form reviews of a new form; rulings /tmp/xrev-new/royalty.tr.json, applied with rule.py; full text in the log and sidecar.

Evidence: .transcription/triage/2025/royalty.json (8 inputs; generated returns hold no royalty entry); forms/2025/royalty.yaml.

| family | kind | line | class | reason |
| --- | --- | --- | --- | --- |
| claude | transcription | royalty.income | representation | equivalent on executable triage (8 of 8 inputs agree, too few generated royalty entries for the mechanical rule): line 21 is line 4 less line 20, so the reply's line 4 less line 20 floored at zero (or its negation) is the proje... |
| claude | transcription | royalty.loss | representation | equivalent on executable triage (8 of 8 inputs agree, too few generated royalty entries for the mechanical rule): line 21 is line 4 less line 20, so the reply's line 4 less line 20 floored at zero (or its negation) is the proje... |
| claude | transcription | royalty.loss_abs | representation | equivalent on executable triage (8 of 8 inputs agree, too few generated royalty entries for the mechanical rule): line 21 is line 4 less line 20, so the reply's line 4 less line 20 floored at zero (or its negation) is the proje... |

Counts: representation 3. Findings: none.

## Goal-1 round (2026-11-15), render

Lane xrev-new (claude-opus-5-5, judgment, tax year 2025, jurisdiction us), worktree x1-sche (uncommitted). Whole-form reviews of a new form; rulings /tmp/xrev-new/royalty.render.json, applied with rule.py; full text in the log and sidecar. Evidence: the log's reasons, rendered/2025/royalty.md, the cited source, the form YAML.

| family | kind | line | class | reason |
| --- | --- | --- | --- | --- |
| claude | render | 4 | finding (medium) | the question allows 'the amount you were paid', which for an oil or gas royalty with producer-withheld taxes is the net payment, but i1040se Line 4 says 'Enter on line 4 the gross amount of royalty income, even if state or loca... |
| claude | render | 10 | finding (low) | royalty.amt10 asks all legal and professional fees, but i1040se Line 10: 'Do not deduct legal fees paid or incurred to defend or protect title to property, to recover property, or to develop or improve property. Instead, you mu... |
| claude | render | 19 | finding (low) | royalty.amt19 asks 'Other costs of it (not depletion)' without i1040se's exclusion 'Do not deduct the value of your own labor or amounts paid for capital investments or capital improvements' (BUG-0922). Folding expen... |

Counts: finding 3. Findings: BUG-0921 (medium, line 4 gross royalty), BUG-0922 (low, lines 10 and 19 capitalized costs).

## Goal-1 round (2026-11-15), class M

Claude class M (claude-opus-5-5): agree 5, disagree 0; cost $0.05. No open line; nothing to rule.
