# Standing screen review — adjudication brief (2026-10-30)

Repository: /Users/elliotmilco/Documents/GitHub/tax-formalization. A screen is a yes/no input that lines name as a refusal
gate (`tools/transcription/screen_review.py`): yes refuses the gated lines, no computes them (usually with the screened
amounts at zero). Under T-088 every screen must have a current review whose findings are ruled. 52 screens were just
re-reviewed (`reviews/2025/screens/screen_review.json`, raw prompts and responses in `.transcription/screens/`).

## Read first
- `reviews/2025/screens/screen_review.md`: the T-008 adjudication (six rounds, disposition per screen). Its standard binds:
  NARROW (a truthful no lets an unsupported case compute, usually as zero) is the dangerous direction; WIDE (a yes
  refuses a case the tool computes) is safe and accepted; UNCLEAR is wording a filer could read either way. A finding
  covered by a sibling screen gating the same lines, or by a derived refusal, is not a defect. Reuse its reasoning where
  a finding repeats a ruled one, but re-check against the current YAML: screens have been reworded since.
- `reviews/2025/transcription/adjudication/README.md` for the general method.

## Per finding, decide
- **defect (NARROW or UNCLEAR that lets an unsupported case through):** quote the IRS text (doc, page from
  `sources/2025/<doc>.cols.txt`, pages split by form feed, page N = element N-1), show the case and what the tool would
  compute, propose the minimal rewording or added screen; mark `"bug": "PENDING-<group>-<n>"`.
- **covered:** a sibling screen or derived refusal gating the same lines catches it; name the gate id and check in the YAML
  that it gates those lines.
- **accepted WIDE:** a refusal of something the tool computes; safe.
- **model error:** misread the IRS text or the question.
- **out of scope / presentation.**

Evaluate a scenario if it decides a case: `node engine/dist/main.js eval --inputs f.json --json` (read-only).

## Deliverables (your group only)
1. `reviews/2025/screens/adjudication/group<K>.json`: `{"unruled:<screen>": {"reason": "<one-line disposition>",
   "findings": [{"n": <index in the screen's findings>, "kind": "NARROW|WIDE|UNCLEAR", "class": "...", "evidence": "..."}],
   "bugs": ["PENDING-..."]}}` for every screen in your group (every finding classed).
2. `reviews/2025/screens/adjudication/group<K>.md`: a table per screen (finding; class; deciding source; reason) and,
   for each PENDING defect, a section with the quote, the case, the effect and the proposed fix.

## Rules
Write only your two files. No edits to forms, fixtures, logs, BUG_INVENTORY, TASKS or the screen records; no model calls,
no check-all, no git writes. Scratch in `/tmp/adj-screens-g<K>/`. Other agents adjudicate the other groups concurrently.
Final reply under 250 words: counts per class, each PENDING defect in one line with severity, uncertainties.
