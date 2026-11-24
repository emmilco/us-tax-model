## BUG-NEW-lane-tooling-02 — Closure: BUG-1171 is fixed: rule.py --amend may set drop on a class M model-error or ambiguity ruling

- **Closes:** BUG-1171
- **Closure:** fixed
- **Caught by:** BUG-1171, recorded open; lane tooling of the 2026-11-24 wave (claude-opus-5-5, judgment).
- **Reproduced:** rule.amend with {"ruling": ..., "drop": true} on an applied ruling without drop exited 'changes whether the line is dropped; not an amendment' (tools/transcription/rule.py, amend).
- **Change:** tools/transcription/rule.py: --amend given {"ruling": "...", "drop": true} on a class M ruling of class model error or ambiguity that did not drop sets the drop flag in the sidecar entry, suffixes the log line [dropped] and removes the line from the class M fixture (drop_from_fixture, as when ruling with drop); drop on another kind or class, and clearing a drop, are refused. Self-test: test_amend_sets_drop_on_a_ruled_classm_model_error_or_ambiguity (test_review_tools.py). tools/transcription/README.md says so.
- **Evidence:** The three classm.f8889.3 spouse lines (7, 8, 12) need no re-ruling: the current f8889 class M log (reviews/2025/classm, f8889) rules them model error with drop (the reply that read the spouse as under 55), and fixtures/2025/classm.json case classm.f8889.3 has no expectation on them ('dropped after ruling' in its note). The ambiguity rulings without drop that BUG-1171 names are sidecar entries of an earlier reply, not sections of the current log, so --amend does not reach them and nothing reads them until a reply with that context returns.
- **Fix lines:** none (tool change: tools/transcription/rule.py)
- **Tags:** tool, class M, rulings, fixtures, fixed
