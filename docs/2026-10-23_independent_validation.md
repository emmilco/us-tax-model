# Independent validation continuation — 2026-10-23

## Superseding owner amendment — 2026-10-24

The owner completed item2 and approved optional human packets/ruling samples plus separately
recorded online commentary as soft evidence. `2026-10-24_validation_policy.md` controls over the
historical waiting/freeze requirements below. BUG-0127 separates optional evidence eligibility
from record-integrity failures; all original owner logs remain byte-for-byte unchanged. Compile,
57 review-tool tests, 16 isolated human-path tests, log validation and the skip audit pass.
The evidence report now regenerates: 198/1515 (13.1%), H0/B0/M2=44/E163, overlapping counts.
This credits recorded numeric lines, not complete forms; Form2441's three blank STOP outputs
remain gaps. No new full-suite green marker is claimed. Four presentation tasks remain recorded
in `reviews/2025/human_findings.md`; no new owner sitting is required. The first commentary
corroboration record is `research/secondary/2025-standard-deduction.md` and earns no evidence credit.

## Historical run record — superseded by the amendment above

The remaining sections preserve prior run states and decisions. Their references to mandatory owner
samples, waiting for the packet, frozen definitions or a stale scoreboard describe the earlier policy.
They do not reinstate those conditions. Current requirements are in `2026-10-24_validation_policy.md`.

## Owner correction and resumption

The owner corrected the model choice: use `deepseek-flash`, not `deepseek-v4-pro`, for future
second-family runs. The initial batch used Pro and remains labeled as such. Both remaining Pro batch
sessions (53487 and 76369) were interrupted with exit 130. The owner then resumed work with Flash.
455 Pro artifacts were preserved with SHA-256 hashes under
`.transcription/archive/pro-before-flash-2026-10-23/`. The Flash transport reported `deepseek-flash`.
The 110-job Flash transcription/render run completed with no transport or parser failures, using
provider-default reasoning and output allowances. Summary: `.transcription/deepseek-flash-full-summary.json`.
Exact request receipts prevent reusing a Pro answer as Flash output. Existing source rulings can
persist only when both the precise disagreement and its recorded review context are unchanged
(BUG-0121). The earlier run history below describes
Pro work, not a Flash qualification.

BUG-0115 pins Flash in `families.json`: a Pro network call is rejected before keychain access,
and a Pro log cannot qualify under the Flash selection.

## Current continuation — 2026-10-24

Latest source-context work: BUG-0124 adds Schedule 3's omitted i1040gi p.117; BUG-0125 follows
scoped glossary dependencies and supplies their source pages; BUG-0126 adds i1116 p.25's
regular-tax definition. All 57 offline review-tool tests pass. Flash's final Schedule 3 transcription
now agrees on excess withholding; its other four differences are documented representation guards
and a redundant zero floor. The five focused Flash render reruns and both families' final s3/ftc
reruns completed without transport/parser failures. Refreshed render objections are resolved with
cited scope/input limits; no unsupported case is credited as a supported calculation.

Source adjudication also covers carloan, ftc, retirement, f8889, f8959 and f4952, with evaluator
witnesses or explicit exclusions retained beside the raw reviews. f4952 transcription remains
ineligible above the noise ceiling; retirement has four open transcription differences. Focused
Flash retries fix tipjob's undefined parameter, otjob's malformed guard and W-2's missing EE code.
The W-2 alternative matches on 1152 supported complete-input combinations. New W-2 Flash hand-work
matches all 39 numeric results in a return with three W-2s; the primary and Flash case prompts have
the same SHA-256. These are synthetic worked values, not a new human review or whole-return run.

The updated second-family report contains 112 form-kind pairs: 37 eligible, 73 pending and two
with no judged lines. All required Claude logs are current and have no open ruling; the global
check still fails on the owner's unresolved human findings. All fourteen active packet receipts
are unchanged. Default citations have zero findings; 301 strict locator segments remain unfinished.
The evidence scoreboard stays explicitly stale and DeepSeek remains optional.
The full 1065-case CLI run passed 1060 and identified five refusal-citation metadata differences
from the new FTC locator. After updating only those expected citation strings, all five pass a
targeted CLI rerun; numeric expectations, inputs, gates and remedies are unchanged. This verifies
the cases across the full run and focused rerun, without claiming a fresh check-all green marker.
The local review server responds HTTP 200 on item 2.

Form2441's three missing line29 numeric outputs are STOP cases. Flash explicitly computes
$3000−$5000, $3000−$3500 and $3000−$4300, then leaves each value blank. The project normalizes
that path to a nonnegative zero. No explicit owner ruling on the presentation convention was found;
the blanks stay SKIPPED, and the form remains pending. Calling these unworked arithmetic would
be inaccurate. The raw answers and this analysis are recorded in `.classm/f2441-current-summary.json`.

Three Flash source findings are applied: BUG-0117 adds the foreign provider's not-required-to-obtain
TIN condition; BUG-0119 includes all qualified 2025 incurred care expenses regardless of payment
date; BUG-0120 limits current-year forfeitures/carryforwards to line 12, excluding prior-year amounts
used during the grace period. Both families' affected render reviews now accept lines 15 and 16.
The dcprov reruns agree on every line. Main build/render and citations pass. Three hand-derived
boundary regressions were added for line 14; before the new class M samples were written, all
1058 CLI fixtures passed. After the new worked-value fixtures, all 1064 CLI cases pass. The fourteen
active item-2 receipts still exactly match their pre-fix hashes.
The review server was restarted at the owner's request; saved logs were preserved and its read/save
validation endpoints were checked. The owner has not reported completion of the packet.

BUG-0121 repairs automatic ruling reuse. A changed input question can leave canonical expressions
unchanged while invalidating a source rationale. New rulings bind the reviewed subject, prompt,
sources, system and request settings; class M binds every case prompt. Historical unbound rulings
remain records but cannot be reused automatically. All 43 offline review-tool regressions pass.
The old f2441 line-16 ruling's false payment-year premise is explicitly corrected in the current log
and sidecar, with the former artifacts retained.

The current Flash f2441 transcription has five confirmed model-error lines among 37 judgments,
including a missing qualifying-person filter that changes a one-child $3000 limit to $6000 when
there are older nonqualifying dependents. It exceeds the 10% noise ceiling and stays ineligible;
four other rulings remain open. Its render review has two source-adjudicated model-error objections
about earned-income benefits (2/36), five scoped objections, and no open ruling. The confirmed
source findings remain valid irrespective of a later review's eligibility. No family promotion,
owner ruling sample or new human reading credit is claimed.

BUG-0122 addresses a sampling gap exposed by the first refreshed class M run: all four selected
returns had no active care form. The review tools now seed the random corpus with non-M fixture
facts for the requested documents, never the expected values, and require a declared filing flag
to be true. The selector also includes positive own money inputs when buildable. An offline
regression with one random draw finds six active cases, including nonzero carry-in and forfeiture.
Fresh Claude and Flash worked-value runs completed over six active cases. Claude has 138 numeric
agreements, 64 skipped lines and two line-30 owner-ambiguity disputes; both disputed model amounts
are excluded from fixtures. Flash has 151 numeric agreements, 53 skipped lines and no numeric
disagreements. Its form-level M qualification remains pending because it skipped three required
line-29 results. Skipped lines earn no assertion, are not disputes/findings and cannot dilute noise.
Earlier unfiled-form samples are archived.

BUG-0123 separates blanks from numeric zero. The archive audit removed 220 false M assertions and
reclassified 298 historical log sections without changing raw replies, inputs or any remaining
expected value. Originals and hashes are under `.classm/archive/blank-assertions-2026-10-24/`.
The current audit finds no remaining skipped numeric assertion. All 52 offline review-tool tests,
the active-case sampling regression and all 1064 CLI fixtures pass. Citations have zero findings;
the 305 strict locator segments remain unfinished. Required Claude review logs are current and
have no open rulings. The global log check still fails on the owner's unresolved human findings;
those verdicts remain untouched. For the same reason, the evidence-report generator refuses to
refresh its older snapshot. Its stale status is now explicit; no new scoreboard or H credit is claimed.

The remaining full-run disagreements, owner ruling sample, whole-return class M, UsTaxes adapter,
strict citation cleanup and mutation mechanization remain separate unfinished plan work. The
BUG-0111 age-at-care patch stays staged until the owner finishes the active packet. Its fixture
hunk was rebased on the new boundary cases; a refreshed isolated build, all 1066 CLI fixtures and
the six age/timing checks pass. Current parsed M results and blockers are also saved in
`.classm/f2441-current-summary.json`.

## Work completed during the Flash run

- BUG-0111's checkbox correction is staged in `docs/patches/BUG-0111.patch`, with
  `BUG-0111-check.mjs` for six age/timing checks after applying it in an isolated copy. The isolated
  build and 1057 CLI fixtures pass. Registering the new question would refresh the owner's current
  packet receipts, so the active forms and interview bank remain untouched.
- BUG-0116 removes eight dead mutation exemptions and nine hidden prose fallbacks. All eight
  mutants were re-probed and killed by fixtures. The complete mutation run remains 2278 mutants,
  235 checker kills, 1915 fixture kills and 128 equivalent survivors (94.4% raw, 100% adjusted).
  The nine surviving copy-chain cases still have mechanical proofs. Independent review and further
  mechanization remain unfinished; the tables now contain 15 prose and 57 conditional entries.
- Flash QDCGT's only disagreement is ruled representation with the p. 38 source and completed-return
  routing proof. Flash's initial mid-quarter test wrongly rounds a strict 40% comparison: annual
  basis $1000.02 and Q4 basis $400.01 expose it. That one-line run exceeds the noise limit and earns
  no assertion. Its artifacts are archived separately. The Flash maximum-reasoning retry corrected
  aggregation but retained the rounded comparison, so it is also ruled model error and remains
  ineligible. Do not lower the noise rule or substitute Pro.
- Flash found a new input-wording omission, BUG-0117: the foreign care-provider LAFCP choice omits
  the requirement that the provider is not required to get a U.S. taxpayer ID. Archived i2441 p. 3
  confirms it; Claude and Pro had accepted the wording. The correction is queued for the end of
  the batch, followed by both families' affected transcription/render reviews. Unlike BUG-0111,
  this changes no interview-bank entry; item-2 receipt hashes have been saved for an explicit
  before/after check.
- BUG-0118 accelerates local project YAML reads with the installed safe LibYAML loader, falling
  back to the Python safe loader. Raw model-response validation is unchanged. All form/parameter
  parses compare equal; a profiled dcprov prompt falls from 13.003 to 1.248 seconds with identical
  SHA-256 0e7bf3057ba87b13a2085b564b7f106b152aa0dfc92f6718406535201c369c57.
  All 37 offline review-tool regression tests pass.

The owner asked work to continue while he completes the human reading. Coverage expansion remains
paused. Human logs are his work: do not rewrite their verdicts, infer completion from partial saves,
or relabel them as model work. No source form, parameter or human-reading tool is changed in this
batch, so the active packet receipts remain current.

## Machinery repaired

- BUG-0106: `compare_families.py` now implements decision 12: disputes explicitly ruled model error
  divided by the second family's judged lines, no more than ten percent per form-kind run. Correct
  findings and representation/scope/ambiguity rulings are not noise. Raw agreement is diagnostic.
  Missing/invalid/duplicate lines, open/unclassified rulings, old subjects/sources, a wrong model or
  a pre-independence-policy transcription keep the review pending. Required families enforce this
  gate; optional pending reviews remain visible.
- BUG-0107: computed targets, exported helpers, collection fields and cross-form catalogs omit
  project-written labels and expressions. Shared ids, printed markers, types, input questions,
  screening interfaces and year parameters remain, and are acknowledged as shared interfaces.
  The policy is `source-only-computation-v2`. Exact ids are requested consistently; the input
  interface is explicitly closed.
- BUG-0108: transcription/render/class M cached responses are bound to exact user prompt, system prompt,
  requested model, policy and explicit reasoning effort. Dry runs write previews. Legacy unbound
  responses cannot acquire new provenance. `rerun_all.py --resume` tries this validation and makes
  a fresh request when reuse fails; progress is saved after each completed job, in completion order.
  Class M rebuilds current jobs on reuse as well: changed supplied amounts require fresh work, and
  dry runs preserve live request receipts and fixtures. This does not rerun or requalify old class M logs.
- BUG-0109: an exact published definition id can be namespace-qualified in the response. Only those
  aliases are normalized; unknown helpers remain untouched and conflicting aliases fail. The raw
  response and its actual request remain unchanged. This is not arithmetic normalization.
- `families.load(kind)` accepts optional `by_kind` overrides. When promoting DeepSeek for
  transcription/render, class M can remain optional until its separate work has been done. Do not
  silently require 48 class M logs as a side effect of promoting the other two kinds.
- `tools/transcription/test_review_tools.py` is an offline check-all step. It covers noise boundaries,
  provenance, blinding, interface normalization and per-kind family requirements.
- BUG-0110: unexpected line keys keep a review pending and are excluded from the noise denominator;
  extra agreements cannot dilute errors on requested lines.
- BUG-0112: raw response parsing now rejects duplicate keys/ids, invalid verdicts and missing reasons
  before a conflicting judgment can disappear in a lookup map.
- BUG-0113: direct connection resets now use the same bounded retry policy as wrapped URL failures.
- BUG-0114: an explicit output budget is request-bound; length-truncated responses are preserved but
  rejected on both fresh calls and reuse. The largest documents need 131072 tokens to leave room
  for a final answer after reasoning. Timeouts grow with the allowance. All 34 offline tests pass.

## Live pilot

The existing keychain credential works; the connection check returned model `deepseek-v4-pro`.
No key was printed, written to a file or put into an environment variable. Calls remain fixed-prompt
over public archived IRS text, parsed as data at predetermined paths, with no model tools.

Eight calls (transcription/render of qdcg, sa, se and tcw) completed with no transport or parser
failures. Seven produced disagreements. The run summary is
`.transcription/deepseek-pilot-summary.json`. Its counts describe each job at completion; later
normalization/rulings can change the current logs. Raw requests, responses and request receipts are
under `.transcription/`; the committed review logs are under `reviews/2025/{transcription,render}/`.

The first Schedule SE response used `se.line13` rather than `line13`. It has been re-compared with
the namespace correction, using its original saved prompt and request receipt, not a newly built
request. Its current result is DISAGREE rather than the original MISSING.

A second, two-call transcription pilot for se and qdcg uses `--reasoning-effort max` and the clarified
closed-input contract. Summary: `.transcription/deepseek-closed-input-summary.json`. Earlier raw
responses are retained under `.transcription/pilot-before-closed-input-retry/`. The API's documented
effort options and limits were checked at
[DeepSeek Chat Completions](https://api-docs.deepseek.com/api/create-chat-completion/) on 2026-10-23.

## Rulings and unresolved work

BUG-0111 is a confirmed new second-family finding: Form 2441 line 2(c) uses year-end age instead
of age when care was provided. A disabled qualifying child turning 13 can be checked even if all
care preceded the birthday. The `stage15.f2441.s8` reproduction and required before/after fixtures
are recorded in the inventory. It changes a displayed checkbox, not a tax amount. The form fix is
staged in `docs/patches/BUG-0111.patch`. In an isolated copy the build and all 1057 CLI fixtures
pass, including paired before/after-birthday regressions. Six targeted checks also cover age 12,
age 14, no disability and an unanswered timing question; monetary results remain unchanged.
Item 2's form dependencies exclude dependent, but every receipt includes the whole interview
question bank. Registering the new input therefore refreshes those receipts. The patch stays
separate while the owner reads; the active forms and bank remain unchanged. The separate line 2(d)
objection is the already recorded owner ambiguity `amb.2025.dc_line30` (Stage 15 decision 6/T-048),
not a new model error or an assertion that the literal per-person column matches.

The tcw transcription's only difference was explicit versus implicit first-row $100,000 bounds.
Removing only those bounds, collapsing singleton conjunctions and re-sorting alternatives made
the expanded trees identical. IRS i1040gi p. 80 first rows and p. 33 method selection, plus the sole
caller `tax_on_amount`, establish the valid domain. Recorded as representation, not model noise,
in the DeepSeek log and sidecar. Source data was retained.

Other pilot differences still need source-based rulings. The first se transcription introduced
inputs for farm/optional/church/tip/wage sources excluded by the supported slice and did not encode
the under-$400 stop as the project does. Do not dismiss that as a namespace issue or count the
pending response as an assertion. The stronger rerun resolved the input/scope failure after the
shared IR conventions were made explicit. The final se difference is a zero floor inside a positive
branch; removing only those six repeated floors makes the expanded trees identical. It is ruled
representation with the source and branch proof recorded. QDCGT's three final differences are also
ruled representation: positive status-keyed constants with redundant floors, and the min/floor
identity plus the supported no-Schedule-D routing. Partial/unknown-entry semantics are not claimed
proved by that ruling.

The two carloan render objections and eight f2441 render objections have cited scope rulings.
They identify actual wider IRS cases (Schedule E/F interest; statutory/clergy income; Form 8978;
self-employed care plans; MFS) that the completed-return flow refuses elsewhere. Each ruling names
the source and enforcing screens and explicitly avoids a standalone-line correctness claim on an
excluded return. These rulings still await the owner's sample under item 1.3.

The sa render review objects to the negative-AGI floor on printed line 2. That is already the
explicit ambiguity `amb.2025.sa_medical_negative_agi`, introduced for BUG-0094; its status says the
owner's decision is not recorded. Do not silently overturn the chosen floor, call the objection
model error, or claim the ambiguity is human-approved. This needs resolution after the owner review.

The owner's partial human log flags the per-box addition because those increment amounts are not
printed literally in the displayed chart. This is a source-presentation concern to investigate with
him when he reports completion; his saved MISMATCH must remain his. The calculation may need to be
shown explicitly as the difference between chart rows/base amounts. No fix is claimed yet.

The full 55-form transcription and render batches have returned with resumable request receipts.
Progress is saved in `.transcription/deepseek-transcription-full-summary.json` and
`.transcription/deepseek-render-full-summary.json`. Transcriptions use explicit maximum reasoning;
render reviews use the provider default. Render has all 55 logs after the s1a connection retry.
The initial transcription batch had four failures: dependent malformed YAML, s2 peer reset,
and sc/scveh empty final answers after spending all 65536 output tokens on reasoning. Dependent
has succeeded on a fresh call; s2/sc retries are underway, and scveh has a 131072-token retry.
Earlier failed raw responses are retained in separate `.transcription/` subdirectories.
Next: finish the remaining retries and adjudicate differences;
promote the family only when current logs qualify and the owner's ruling sample is complete.
The dependent transcription returned malformed YAML in its first full-run response; it remains
saved for investigation and requires a fresh call, not a hand-edited response passed off as model output.
The evidence scoreboard still has no second-family source-reading column: transcription/render
results are kept in `second_family.md`, not conflated with class M worked-value assertions. Wiring
that separate source-reading evidence remains work to do. Then continue UsTaxes, class M, mutation
equivalences and strict citations under the integrity plan.
