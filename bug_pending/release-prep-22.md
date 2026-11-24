## BUG-NEW-release-prep-22 — Closure: BUG-NEW-release-prep-20 is fixed

- **Closes:** BUG-NEW-release-prep-20
- **Closure:** fixed
- **Caught by:** release preparation 5 (release-prep-4, claude-opus-5-5, judgment), 2026-11-23, integrating mutation lanes A to H.
- **Resolution:** Mutation lanes A to D (stale and retargeted arguments: re-pinned after re-reading, rewritten, or removed where the mutant is now killed; the s8812.line18a contradiction resolved by completing the missing answers of classm.carloan.2 and mutation.t2.hoh_s1a_car, with the rate-0 sampling issue filed as BUG-NEW-release-prep-21) and lanes E to H (the remaining survivors: pinned arguments for household.hoh_missed_mfs.no.then1, ssb.line18.zero.then1 and f1116.line18_shown.line17.gt.0; hand-predicted fixtures for the others in eic.json, dependent.json, f8889.json, f8582.json, f8960.json and ny/2025/it201.json; BUG-NEW-lane-muta-01 and BUG-NEW-lane-mutf-01 filed, low).
- **Evidence:** node engine/dist/main.js mutate on the integrated tree, 2026-11-23 (46 min): 10392 mutants, surviving 462 (443 explained on every input, 11 on answered inputs only, 8 by open defects), 0 not yet explained, 0 stale arguments, 113 retargeted arguments rejected by the self-test with 0 problems, sampled check 0 problems; mutate --ny: 945 mutants, 53 survivors all explained, 0 problems.
- **Tags:** mutation, tools, release, fixed
