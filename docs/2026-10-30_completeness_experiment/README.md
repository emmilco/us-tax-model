# Completeness-review experiment (2026-10-30)

The cheapest test named in `docs/2026-10-30_mitigation_strategy_pressure_test.md` section 5, item 1: can an isolated
model, given a whole instruction section and the encoding of that section, find operative rules that nothing encodes?

- **Tree:** `0186a66^` (`ac69196`), the commit before BUG-0095 to BUG-0097 were recorded.
- **Sections:** i1040gi pp. 17–22, "Dependents, Qualifying Child for Child Tax Credit, and Credit for Other Dependents"
  (`call1`), and pp. 40–48, "Lines 27a, 27b, and 27c — Earned Income Credit" (`call2`), by heading range, from that
  tree's `sources/2025/i1040gi.cols.txt`.
- **Encoding given:** every line of `dependent`, `household` and `person` (call 1) and `eic`, `dependent` and
  `household` (call 2) at that tree: id, printed marker, label, input question, refusals and citation.
- **Model:** `claude -p --setting-sources "" --model claude-opus-5-5 --system-prompt sys.txt`, file and shell tools
  disallowed; prompts in `call1.txt`, `call2.txt`; replies in `call1.out`, `call2.out`. No prompt names a bug.

Result: 29 claims (13 and 16). The governing sentences of BUG-0097 (EIC claims 1 and 2) and BUG-0095 (dependents
claims 9 and 10, the latter rated "mainly presentation") were found, and BUG-0195, recorded nine days later in Stage 19,
was found exactly (EIC claim 4). The sections were chosen because bugs were known to be there. Precision is measured by
the adjudication in `adjudication.md`.
