# Validation policy — owner amendment, 2026-10-24

This amendment supersedes the mandatory human-reading and ten-ruling-sample requirements in
the 2026-10-22 integrity plan and later handoffs. The owner approved removing the recurring labor
commitment and adding non-authoritative online interpretation as soft evidence.

## Completion gates

1. Source reviews under Claude and deepseek-flash qualify under the existing provenance and noise
   rules. Pending or noisy reviews remain gaps; commentary cannot make an ineligible run qualify.
2. Expand blind Flash calculations to whole returns, including the previously selected blind cases.
   Add UsTaxes to the three integrated engines; investigate every unexplained difference and publish
   which lines each engine actually computes. Four engines remain the plan's target, not a current claim.
3. Correct every confirmed project defect, add a source-backed regression and broaden independent
   checks around the affected regime. If defects cluster, pause coverage until that investigation
   closes. The former automatic doubling of human packets is retired; it is not a substitute for fixes.
4. Finish citation precision, mutation-equivalence review/mechanization and the year-adoption rehearsal;
   refresh the evidence report and pass the full suite before claiming the corresponding milestones.

Human packets, highest-stakes-line reviews at future stages and the ten-ruling sample are optional.
The owner may supply them at any time. Engineering proceeds without waiting for them; owner decisions
are reserved for substantive scope choices or ambiguities requiring owner judgment, not routine work.

## Model authority — owner decision, 2026-11-01

The owner ranked the review models by authority. The ranking is about the evidence a model's reading
can carry; it is not a pin on any one run.

- **Superior to all the others:** `claude-fable-5-1`.
- **Interchangeable in authority:** `gpt-6-astra`, `claude-opus-5-5`, `gemini-4-argon`,
  `deepseek-v4.1-flash`, `gpt-6.1-sol`. A reading from any of these stands as a peer of the others.
- **Mechanical or advisory work only, nothing judgment-heavy:** `gemini-3`, `gpt-6-luna`,
  `gpt-6-terra`, `claude-sonnet`, `claude-haiku`.

A model's rank does not by itself qualify a review: the provenance, subject, noise and ruling rules
above still decide whether a run is evidence. The Claude family remains the required reviewer for the
standing logs; `deepseek-flash` and `gpt-6-astra` are optional peer families under `families.json`.
GPT-6 Astra runs through `codex exec` in an empty read-only scratch directory with `--ignore-user-config`;
any tool event in its stream fails the call, and the model codex actually used is read from its session
rollout (deleted after the fact, so the review's own receipt is the only retained copy).

## Existing human evidence

The owner completed item 2: fourteen saved answers, ten MATCH, three MISMATCH and one UNCLEAR.
The originals and pre-policy receipts are preserved with hashes under
`.transcription/archive/human-policy-before-optional-2026-10-24/`. Do not rewrite the verdicts or sign
them on the owner's behalf. Engineering responses are in `reviews/2025/human_findings.md`.

Unsigned, incomplete, stale or negative reviews earn no H credit and are reported as pending;
they do not fail unrelated validation or report generation. Record corruption, duplicate entries,
invalid reader identity and incorrect committed authorship remain hard failures. The new tool
version changes receipt hashes: existing readings become historical rather than being re-signed
or silently migrated. H requires a current MATCH and the named person's committed record.

## Secondary interpretation

Use online explanations to identify plausible readings, exceptions, examples and contradictions.
Record support and opposition, not just material agreeing with the current implementation.
Prefer attributable professional reasoning with a tax year, applicable facts and primary citations.
Practitioner forums can supply useful counterexamples; anonymous claims are leads to investigate.

For each reading record its affected project lines, competing interpretations, primary-source
anchors, author/publisher, URL, publication/update information, retrieval date, short captured
passage and hash, applicable year/facts, cited upstream sources, contrary material, conclusion and
remaining uncertainty. Several sites copying one explanation count as one source lineage.

Commentary can support a documented ambiguity choice, but cannot override an explicit archived
instruction or make the project claim legal authority. Apparent legal/instruction conflicts are
recorded for investigation. No vote-counting confidence score is introduced. Unreachable material
or search snippets alone do not substantiate an adjudication.

Soft evidence earns no numeric assertion, human credit, review qualification or scoreboard increase.
It remains separate from the official source manifest. Keep blind transcription and M requests
source-only; label any commentary-informed supplemental review distinctly. It adds no model or
network dependency to tax-return runtime. Records and the first worked research example are under
`research/secondary/`.

## Next work

The presentation changes and held age-at-care correction are implemented in the follow-up to
735e644, with original verdicts preserved. Repair BUG-0129's literal-unit comparison and audit
previous agreements before transcription qualification resumes; all transcription comparisons
are currently held. Literal-unit preservation and a read-only saved-reply comparison audit are now
implemented. The 2026-10-25 follow-up adds project-schema/reference/type validation and complete-input
request checks; current audits and sample results are in `reports/2025/transcription_audit.md`.
Qualified record migration/fresh requests, valid replacements and source adjudication remain.
Continue the other pending comparisons, broader calculations and engine work.
No human approval or completion of outstanding evidence milestones is inferred from this policy change.
