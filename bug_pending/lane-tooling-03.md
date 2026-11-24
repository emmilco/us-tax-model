## BUG-NEW-lane-tooling-03 — Closure: BUG-NEW-release-prep-03 is fixed: samples.confirmed_bugs takes a class's ids only when the class classes a defect or a real gap

- **Closes:** BUG-NEW-release-prep-03
- **Closure:** fixed
- **Caught by:** BUG-NEW-release-prep-03, recorded open; lane tooling of the 2026-11-24 wave (claude-opus-5-5, judgment).
- **Reproduced:** samples.confirmed_bugs({'class': 'no defect (as BUG-0123, already fixed)'}) returned {'BUG-0123'}. Ten ruling classes in reviews/ and .transcription/ name a bug id in a class that rules no defect ('no gate defect beyond BUG-1087 (low)', 'no gate defect; ... (BUG-0800)', 'As ruled for the earlier subject: ... BUG-0827 and BUG-0964 open', ...).
- **Change:** tools/transcription/samples.py: DEFECT_CLASS (a class beginning 'defect' or 'real gap', optionally after a severity: 'low defect: ...'); confirmed_bugs takes the ids of the ruling's class only when the class matches it, and applies the same test to a finding's class. The bug and bugs fields are unchanged. Self-test: test_a_class_ruling_no_defect_confirms_no_bug_it_names (test_samples.py). tools/README.md says so.
- **Evidence:** of the ids the no-defect classes name, the open ones (BUG-0620, BUG-0827, BUG-1087, BUG-1092) are all low, so the release gate's outcome on the current rulings is unchanged; test_samples.py 10 passed.
- **Fix lines:** none (tool change: tools/transcription/samples.py)
- **Tags:** tool, sampled reviews, release gate, fixed
