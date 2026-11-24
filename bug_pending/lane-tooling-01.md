## BUG-NEW-lane-tooling-01 — Closure: BUG-1170 is fixed: siblings.py --check tests the review refresh only of the entries the tree under test adds or changes

- **Closes:** BUG-1170
- **Closure:** fixed
- **Caught by:** BUG-1170, recorded open; lane tooling of the 2026-11-24 wave (claude-opus-5-5, judgment).
- **Reproduced:** in a shared clone with HEAD at ed6c46ea and the tree of 25e48ec0 (integration 4), its reviews/ reset to ed6c46ea's (the int4 working state before its reviews were rerun), built: siblings.py --check failed BUG-1125, BUG-1126 and BUG-1128 (and BUG-1069) with 'no review log changed since <commit>^ for sibling form(s)'. Commit ed6c46ea, which added BUG-1125 to BUG-1128, changes no file under forms/2025, so on ed6c46ea itself no review was due; the later form changes of int4 made those entries' sibling forms due.
- **Change:** tools/siblings.py: the review-refresh test (review_logs_due) runs only for an entry under test (under_test: an entry measured from HEAD, or a committed pending entry whose file the working tree changes), measured from HEAD; a committed entry keeps the verdict of the commit that added it. The Fix-lines, Siblings-checked and omitted-sibling tests are unchanged. Self-test: under_test cases in siblings.py --self-test. tools/README.md (Bug inventory) says so.
- **Evidence:** the same reproduction with the changed siblings.py: no committed entry fails; the 22 entries the int4 tree adds over HEAD are still checked against their sibling forms' logs. siblings.py --self-test ok; --check passes on this tree.
- **Fix lines:** none (tool change: tools/siblings.py)
- **Tags:** tool, siblings, verification, fixed
