# Tasks

The one list of work that is known and not done. Spec section 11 states the
open scope items; `BUG_INVENTORY.md` records defects; the stage handoffs
describe where a stage stands. Anything that someone must remember to do
later lives here, with where it came from and what makes it due. Add a row
when a ruling, a review or a stage leaves something for later; set the status
when it is done and say in which commit.

| Id | Task | Source | Due when | Status |
| --- | --- | --- | --- | --- |
| T-001 | Class M hand-work: branch-covering inputs per worksheet worked by an isolated model on the archived pages, becoming class M fixtures; seed from `engine/src/generate.ts` and its branch report. Target the band where the worksheet tax exceeds the ordinary tax (`qdcg.line25:right`, `sdtw.line47:right`). | spec 6.5, design Stage 7 | Stage 7 done-when | done for the 15 non-collection documents (39 cases, `fixtures/2025/classm.json`); collections and definitions remain as T-015 |
| T-002 | Form 1040 line 1z: become the sum of lines 1a–1h (now line 1a alone behind the other-income screen). | transcription and render rulings, f1040 | lines 1b–1h come into scope | open |
| T-003 | Schedule D line filters: widen box tests to G–L and make `sd.filed` test the raw Form 1099-DIV boxes rather than the netted worksheet results. | transcription rulings sd; render rulings sd, sales | digital assets or carryovers come into scope | open |
| T-004 | Carryover sign convention: Schedule D lines 6 and 14, the 28% Rate Gain Worksheet line 5 and the Unrecaptured Section 1250 Gain Worksheet line 16 must subtract a positive carryover (the printed parentheses) or hold it negative. | transcription rulings sd, g28; render rulings g28, u1250 | capital loss carryovers come into scope | open |
| T-005 | Form 8995 line 8: encode the printed combination once line 7 can be nonzero (now pinned by the dividend-only slice). | transcription ruling f8995 | QBI beyond section 199A dividends comes into scope | open |
| T-006 | Ambiguity register candidate: the Form 1099-DIV consistency gate also tests that boxes 2b + 2c + 2d do not exceed box 2a, which assumes the portions are disjoint; the text says each is a portion of 2a and no more. Decide whether to register it or drop the sum test. | render ruling div | next ambiguity-register pass | open |
| T-007 | Transcription prompt grammar has no `refuses` construct, so refusal gates always surface as disagreements (four standing rulings). Add the construct and re-compare from saved responses. | transcription logs | next transcription rerun | open |
| T-008 | Scope screens: review every screen question against the instruction text of each line it stands in for, not only the lines it gates (the pattern of BUG-0004, 0005, 0006, 0008, 0010). | BUG_INVENTORY.md | before Stage 9 coverage work adds screens | open |
| T-009 | Render comparison: add shared-definition references (`"tax" of Tax on an amount ...`) to the glossary so the two QDCG lines that invoke it stop needing a representation ruling. | render rulings qdcg 22, 24 | next render rerun | open |
| T-010 | Stage 8 household architecture test: one dependent, qualifying-child tests, head of household, the child tax credit; stop condition more than one line in eight needing `opaque`. | design Stage 8 | after Stage 7 | open |
| T-011 | Stage 6 tax year 2026: refetch, year diff, rerun every construction. | design Stage 6 | IRS publishes the final 2026 documents | open |
| T-012 | Spec section 11 open items: Form 1116; filling official PDFs; capital loss carryover; married statuses for per-person rules; dependent credits; state returns after federal; the Form 6744 count; the lawyer questions in `research/04_legal_liability.md`. | spec 11 | per the coverage order of spec 2.4 | open |
| T-013 | Data-level properties still unchecked from spec 6.3: tax monotone in ordinary income within the QDCG and SDTW methods specifically (the current check raises wages across whichever method applies); the Lean proofs listed there beyond the evaluator agreement. | spec 6.3 | Stage 7 or when the Lean work resumes | open |
| T-014 | Printed-line labels on the 28% Rate Gain and Unrecaptured Section 1250 Gain worksheets (`g28`, `u1250`) are expression descriptions ("Amount from div.screen"), not the IRS wording the other forms carry; replace them with the page's words. | class M prompts, render logs | next pass over those worksheets | open |
| T-015 | Class M for collection documents (`person`, `w2`, `sales`, `gift`, `interest`) and shared definitions (`tcw`, `tax_on_amount`): the job builder skips them; per-entry and per-instance hand-work needs its own prompt shape. | classm-jobs | Stage 7 done-when | open |
| T-016 | Bound the Stage 2 interview check (`engine/src/interview-check.ts`, `checkInterview`) to the finite inputs the interview's targets can reach instead of every Boolean and enum input in the fixture; it enumerates the Cartesian product and a fixture with seventeen extra flags made it combinatorial. | Stage 8 build | before the next collection is added | open |
| T-017 | Lean lemmas for the `round` atom's `up` and `down` rules (idempotent, moves a value by less than one unit, matches the stated rule), as spec 6.3 lists for `round`; the definitions and the evaluator case exist, the proofs do not. | Stage 8, round atom | when the Lean work resumes | open |
| T-018 | Earned income credit: Form 1040 line 27a, the EIC table extractor and worksheets; spec 2.4 lists it with dependents, design Stage 8 left it out. | spec 2.4 | Stage 9 | open |
| T-019 | PolicyEngine-US does not treat the generated 17–23-year-old students as dependents of the unit; find the inputs its dependency test wants (or confirm the gap) so the credit for other dependents is compared rather than excluded. | engine differential, Stage 8 | next engine upgrade | open |

