# Transcription expression audit — 2026-10-25

## Current HSA source/availability correction after 1b75a3b — 2026-10-26

BUG-0138 is repaired with an explicit supplied-figure consistency check, shared by TypeScript
and Lean. An unanswered consistency check may be unperformed, with a derivation note, while
its expression independently determines the amount. It cannot default an input, suppress a
refused gate, or replace mandatory eligibility/scope answers. Source input wording and generated
monthly calendars now account for spouse-attributed family coverage. Existing owner decisions
about last-month and catchup treatment are retained.

Both current source transcriptions pass expression/refusal validation and all seventeen pinned
source cases. The authored implementation and Lean also pass. The cases include zero/positive
distributions, genuinely missing answers, supplied rollover contradictions, mandatory screens,
and one/two spouse HSAs. Reference answers stay host-side. Eight source-derived numeric
regressions are ordinary engineering tests and earn no M/B/engine credit.

A draft case dictated intermediate scope-screen placement (BUG-0140). Its twelve artifacts are
archived and actual corrected requests were issued. The old fourteen-of-fifteen Claude result
and invalid Flash reply are historical, not current seventeen-case results. All intermediate
wording, calendar and worked-target requests likewise retain their actual request hashes.

| Current read-only audit | Count |
| --- | ---: |
| Verified saved source replies | 95 |
| Passing current expression/refusal checks | 36 |
| Requests with every current global question | 2 |
| Unverified Claude prompts | 15 |
| Legacy-limited verified receipts | 23 |

The stricter refusal boundary (BUG-0139) rejects four former type passes: Flash g28/s2 and both
tipjob replies. The global HSA wording change makes other older full-question contexts stale;
that is not a count of new tax errors. The replay diagnostic flags231 earlier agreements under
the current checker. The JSON is `.transcription/hsa-final-audit.json`. All source qualification
remains held pending verified migration/fresh requests and source/interface adjudication.

The worked-review repair requests printed IRS outputs while retaining helper-branch selection.
The first change kept identical four cases/facts/branches and reduced432 helper-heavy fields to90
printed outputs. Both families matched90, but those facts had only zero distributions and the
request included unnecessary internal validation totals. Those earlier runs are archived.
The strengthened five-case selection reaches97 branches versus87, with none lost, includes a
positive-distribution/tax case, and withholds derived HSA Step1/share totals and split counts
(BUG-0143). Current requests ask for105 printed values. Claude matches105; Flash matches98 and
uses inactive agreed-allocation figures despite allocation=equal in one case. The seven wrong
values are dropped explicitly, with source-derived arithmetic in their rulings. They remain
visible as7/105=6.7% model noise, within the existing10% per-run limit. There are no representation
rulings in the new native run. This does not complete roadmap1.5 for other legacy/helper-only
records, and the finite HSA source bank is not a whole-form proof.

113 offline review tests and the separate consistency/calendar and seeded-job checks pass.
The original owner readings are unchanged; no new human packet is required. The numeric
scoreboard is regenerated separately by check-all; these source-bank checks create no credit.

## Current adapter separation and replacements after 0ef4912

Internal div.screen is now checked as project plumbing, not a blind IRS quantity. Twenty-one
host-only engineering cases cover accepted zero/nonzero inputs, scope/component refusals,
missing answers and propagation through sixteen direct worksheet copies. It is explicitly
excluded from source agreement/noise counts; the original dividend replies/rulings remain
unchanged. An adapter-only document earns no source assertion and makes no new model request.
The registry does not exempt other helpers or supply adapter behavior to source prompts.

| Current audit | Count |
| --- | ---: |
| Verified replies | 95 |
| Passing expression checks | 39 |
| Complete current question wording | 31 |
| Unverified Claude prompts | 15 |
| Legacy-limited verified receipts | 23 |

Eight fresh source-only requests cover f4952/f8889/f8959/mq under both selected families.
All four Claude replies pass types; Flash passes f8959/mq and fails f4952/f8889. Both mq replies
agree; the Medicare differences use the same printed filing-status threshold table. HSA rulings
preserve the owner's existing last-month/catchup choices and keep partial-input handling pending.
Flash's f4952 line4d omits positive short-term gains; its interpretation of f4952.election also
shows that the target must distinguish the full line4g amount from its allocated gain portion.
That meaning gap is not clean model-only tax noise. No candidate is repaired into agreement.

The current JSON is `.transcription/adapter-audit-current.json`; 195 older AGREE rows become
DISAGREE under replay. Counts vary with replaced requests and are not tax-bug totals. All 37
pre-batch artifacts are hashed under `.transcription/archive/before-adapter-contracts-2026-10-25/`.
Actual requests/replies remain bound to their own hashes. No authored form or numeric fixture
changes in this batch; no additional human review is required. The global hold remains.

### Confirmed project gap: zero HSA distributions (BUG-0138 / T-065)

The diagnostic source facts are deliberately minimal, not copied from project outputs:

```json
{
  "$person": ["sample"],
  "$f8889@person[sample]": ["hsa"],
  "f1040.status": "single",
  "person[sample].f8889[hsa].unsupported": false,
  "person[sample].f8889[hsa].line14a": 0
}
```

No rollover, medical-use, exception or taxable-part answer is supplied. i8889 p.8 lines14b/15
include only distributed dollars; p.9 taxes only taxable distributions. With zero distributions,
all these amounts are zero. The fixed interpreter observes:

| Candidate | line14b | line15 | line16 | line17b |
| --- | --- | --- | --- | --- |
| Current project | unknown: rollover | zero | zero | zero |
| Fresh Claude | unknown: rollover | unknown: medical | unknown: rollover | unknown: line17a |
| Fresh Flash | not evaluated: invalid IR | not evaluated | not evaluated | not evaluated |

The project consistency gate is evaluated before line14b's zero branch and asks for an answer
that the branch does not need. This is an actual project partial-output defect, alongside model
availability gaps; the witness establishes no incorrect final tax liability. T-065 must retain
rejection of contradictory supplied amounts when correcting the unnecessary dependency.
The saved diagnostic is `.transcription/hsa-zero-distribution-source-witness.json`. Neither
actual model request contained this case; it is diagnostic only, not a passing case receipt or
numeric evidence. Correct the project gate, add source regressions and refresh affected reviews.

## Current partial-input batch after acad366

The corrected source-based bank supplies ten synthetic fact records to the dependent transcriber,
with reference answers and rationale withheld. A separate fixed interpreter checks only validated
declarative IR; it never runs model-generated code or commands. Logs bind the policy, full bank
hash, actual request inclusion and observed outcomes. These are finite interface examples with no
H/B/M/engine credit, not a whole-form correctness proof.

The current Claude reply passes all ten corrected cases. Current Flash has an invalid root-collection
sum inside a dependent entry, so no contract cases are evaluated. The earlier draft Flash four-case
pass belongs to a different archived request. Two draft negative records inherited contradictory
qualified-expense facts (BUG-0136); corrected requests set those no-care records to zero and care=false.
The draft bank and actual artifacts are preserved, not relabeled. A diagnostic of the earlier
acad366 Claude reply on the corrected bank passes five cases and records that its request did not
include the cases.

| Current audit | Count |
| --- | ---: |
| Verified replies | 91 |
| Passing expression checks | 35 |
| Complete current question wording | 23 |
| Unverified Claude prompts | 19 |
| Legacy-limited verified receipts | 23 |

Four more unusable Claude records—div, ftc, gift and otjob—now have fresh, verified replacements,
with matching Flash runs. Nine of the ten current replacement replies pass expression checks.
The current JSON is `.transcription/partial-input-audit-current.json`. Its 210 lost old agreements
remain a replay diagnostic rather than a count of tax bugs or a scoreboard change.

Both dividend replies guess an internal adapter quantity that the IRS does not define. BUG-0135 /
T-064 records that source-interface gap; the explicit ruling category blocks qualification without
counting it as model-only noise. The tax-credit primary instruction confirms the shared minimum
rule, while a separate bounded witness rejects Flash's unnecessary Form1116 refusal when foreign
tax is zero and no election is made. Source rulings do not imply general partial-input equivalence
outside the declared bank. The existing care-benefit presentation ambiguity remains unchanged.

Pre-batch originals are hashed under `.transcription/archive/before-partial-input-cases-2026-10-25/`
(45 files); draft-case originals are under
`.transcription/archive/partial-input-draft-before-coherence-fix-2026-10-25/` (bank plus ten artifacts).
The source-case implementation and blinding details are in
`tools/transcription/input_contracts/README.md`. The global qualification hold remains; no human
packet is required and no authored tax formula or numeric fixture changed.

## Current replacement batch after 45876d2

Twelve fresh source-only requests covered dependent, se, tcw, tax_on_amount, sb and tipjob under both selected models. Eleven pass expression checks. All 30 disputed rows are adjudicated with explicit source/domain limits; passing types alone does not resolve the dependent care interface. A separate Flash asset probe uses seven valid declared table references but fails other syntax/type checks and retains 15 optional open disputes.

| Family | Verified replies | Passing expression checks | Complete question text | Legacy-limited receipts | Unverified records |
| --- | ---: | ---: | ---: | ---: | ---: |
| claude | 32 | 11 | 7 | 23 | 23 |
| deepseek | 55 | 20 | 8 | 0 | 0 |

Five previously unusable Claude records now have actual fresh replacements: se, sb, tax_on_amount, tcw and tipjob. The remaining 23 unverified Claude prompts still fail their recorded hashes. No old receipt was relabeled or upgraded. The twelve-reply batch audit verifies all twelve saved requests and replays their current judgments without changes; that is provenance/replay validation, not twelve qualified source reviews.

BUG-0133 adds table interface metadata and expression syntax without authored computations or table cells. The final prompt schema filters the implemented-atom catalog; the batch and asset probe used the earlier full-schema version and retain their actual requests. BUG-0134/T-063 distinguishes complete question wording from conditional input availability. Both dependent care replies require timing answers on age paths where the guided interview does not ask them. These are not clean model-only noise tests.

The current audit JSON is `.transcription/schema-catalog-audit-current.json` (87 verified replies, 31 expression passes, 15 complete question-text requests, 23 unverified records). It flags 210 old AGREE rows under stricter replay; the earlier 211 was a different request/log snapshot, not a tax-bug count or evidence-score change. Twenty-three receipts remain legacy-limited.

Originals are hashed under `.transcription/archive/before-schema-catalog-2026-10-25/` (57 files) and `.transcription/archive/before-schema-asset-probe-2026-10-25/` (four files). The standalone batch audit is `.transcription/schema-catalog-batch-audit.json`. All requests remain source-only; no candidate expression was executed or repaired into agreement. The global transcription hold remains and no further human packet is required.

## Baseline recorded in 45876d2

T-062 / BUG-0129 remains open. This audit diagnoses saved model replies; it does not qualify reviews, migrate receipts or change numeric evidence.

| Family | Verified/recompared replies | Passing expression checks | Former AGREE rows now DISAGREE | Legacy-limited receipts |
| --- | ---: | ---: | ---: | ---: |
| claude | 27 | 6 | 92 | 23 |
| deepseek | 55 | 20 | 119 | 0 |

Of the 82 verified replies, 4 contain the complete current filer-input questions. A passing type check alone cannot repair truncated input meanings or incomplete provenance.

The other 28 Claude records could not be verified/recompared: 27 saved prompts differ from their recorded hashes, and se has conflicting ids after definition-namespace normalization. These remain gaps; no original request or response was silently corrected.

The adapter checks the project expression schema and the build’s existing reference/type rules. It replaces only the reviewed document, preserves published inputs, rejects added inputs and changed result types, and does not borrow missing computed helpers from that document. Candidate expressions are never executed. Passing these checks does not certify guard exhaustiveness, citations, source interpretation or tax correctness.

Four fresh, full-context source-only sample requests used Claude Opus 5.5 and deepseek-flash, once per model for dcprov and dependent. Both dcprov replies pass and agree on two results. Claude’s dependent reply passes expression checks but retains source/interface omissions. Flash’s dependent reply fails on bare Boolean ids used as tests and an invalid collection binding. Each dependent reply has 12 disputes; all are adjudicated with explicit limits, and both remain pending.

Original sample artifacts (18 files) are preserved with SHA-256 hashes under `.transcription/archive/before-expression-validation-2026-10-25/`. Fresh request policies and metadata retain the values actually used. The read-only audit JSON is `.transcription/expression-type-audit-current.json`; the earlier literal-only audit and intermediate expression audit remain separate historical snapshots. Audit exit 1 reports the 28 unresolved records.

Next: verify/replay usable original requests, replace incomplete/unverified requests, obtain valid replacements for rejected expressions, and adjudicate the remaining source differences. Both families must have current passing expression checks and verified complete input context before qualification; the global hold remains until migration/adjudication is complete. No further human packet is required.
