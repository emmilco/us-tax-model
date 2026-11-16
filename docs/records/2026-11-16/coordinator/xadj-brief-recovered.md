# ORIGINAL BRIEF (2026-11-16T00:36:58.739Z)

Lane xadj: round-2 reviews and adjudication of the coverage-expansion merge's changed shared forms, in /Users/elliotmilco/Documents/GitHub/tax-formalization/.claude/worktrees/xint.
Model: claude-opus-5-5
Class: judgment
Year: 2025
Jurisdiction: us

Read project CLAUDE.md, tools/README.md (review rerun guards), /tmp/b1-adj-brief.md (adjudication method incl. the render and class M OVERRIDE paragraphs; paths there name nx-b1 — here it is xint), and docs/provisional/lanes/xint.md section "check_logs on the candidate" (the stale list). Lane notes of each expansion lane (docs/provisional/lanes/x1-*.md, x2-*.md, mfs-*.md) say what changed in each form and why. Do not edit forms; no check_all; no model calls from code except the review tools. Another lane (xrel) runs the sampled release reviews in the same worktree at the same time: do not touch reviews/completeness, reviews/*/screens or false-no files.

1. Run the reviews (Claude only): `PYENV_VERSION=3.13.6 python3 tools/transcription/rerun_all.py --kinds transcription,render,classm --forms dependent,eic,f1040,f2441,f8863,f8889,f8959,f8960,f8962,ftc,household,ira,oi8z,person,refund,retirement,s1,s1a,s2,s3,s8812,sa,sales,scope,sd,se,sli,ssb,tipjob,f1116,f8919 --jobs 12 --approve-cost 150 --summary /tmp/xadj-summary.json` (dry-run first to see the plan; line-scoped by default; "whole" where the tool demands). classm.py now writes fixtures/2025/classm.json under a lock, so parallel class M is safe in this tree. qdcg_amount (a new def with no logs, unread until Form 8615): check whether check_logs requires logs for it (read check_logs.py); if so, run its transcription (and whatever else is required) directly.
2. Adjudicate: as soon as a form's reviews finish, rule its open lines. Fan out with Opus forks (5–7), grouped by family (e.g. household/dependent/eic/s8812; f1040/s1/s1a/oi8z/sli/sa; s2/s3/se/f8959/f8960; credits f2441/f8863/f8889/f8962/ftc/f1116; retirement/ira/person/ssb/refund; sales/sd/tipjob/f8919/scope), each fork only its forms; one class M rule/carry at a time per form is fine now that writes are locked, but keep forks on disjoint forms. Many disagreements will be the expansion's intended changes (MFS now computed; new lines) or old rulings that dismissed MFS differences "on refused returns" — decide each on the source. Findings: medium/high ones need a fix — report them to the coordinator immediately via your report (do not fix forms); lows wait. Goal-1 round sections in reviews/2025/transcription/adjudication/<form>.md.
3. Finish with check_logs.py (federal and --jurisdiction ny): report every remaining line.
Deadline: report by 22:00 (it is 19:40); send an interim report at 21:00 with medium/high findings so far.

# ORIGINAL BRIEF ()

Lane xadj: round-2 reviews and adjudication of the coverage-expansion merge's changed shared forms, in /Users/elliotmilco/Documents/GitHub/tax-formalization/.claude/worktrees/xint.
Model: claude-opus-5-5
Class: judgment
Year: 2025
Jurisdiction: us

Read project CLAUDE.md, tools/README.md (review rerun guards), /tmp/b1-adj-brief.md (adjudication method incl. the render and class M OVERRIDE paragraphs; paths there name nx-b1 — here it is xint), and docs/provisional/lanes/xint.md section "check_logs on the candidate" (the stale list). Lane notes of each expansion lane (docs/provisional/lanes/x1-*.md, x2-*.md, mfs-*.md) say what changed in each form and why. Do not edit forms; no check_all; no model calls from code except the review tools. Another lane (xrel) runs the sampled release reviews in the same worktree at the same time: do not touch reviews/completeness, reviews/*/screens or false-no files.

1. Run the reviews (Claude only): `PYENV_VERSION=3.13.6 python3 tools/transcription/rerun_all.py --kinds transcription,render,classm --forms dependent,eic,f1040,f2441,f8863,f8889,f8959,f8960,f8962,ftc,household,ira,oi8z,person,refund,retirement,s1,s1a,s2,s3,s8812,sa,sales,scope,sd,se,sli,ssb,tipjob,f1116,f8919 --jobs 12 --approve-cost 150 --summary /tmp/xadj-summary.json` (dry-run first to see the plan; line-scoped by default; "whole" where the tool demands). classm.py now writes fixtures/2025/classm.json under a lock, so parallel class M is safe in this tree. qdcg_amount (a new def with no logs, unread until Form 8615): check whether check_logs requires logs for it (read check_logs.py); if so, run its transcription (and whatever else is required) directly.
2. Adjudicate: as soon as a form's reviews finish, rule its open lines. Fan out with Opus forks (5–7), grouped by family (e.g. household/dependent/eic/s8812; f1040/s1/s1a/oi8z/sli/sa; s2/s3/se/f8959/f8960; credits f2441/f8863/f8889/f8962/ftc/f1116; retirement/ira/person/ssb/refund; sales/sd/tipjob/f8919/scope), each fork only its forms; one class M rule/carry at a time per form is fine now that writes are locked, but keep forks on disjoint forms. Many disagreements will be the expansion's intended changes (MFS now computed; new lines) or old rulings that dismissed MFS differences "on refused returns" — decide each on the source. Findings: medium/high ones need a fix — report them to the coordinator immediately via your report (do not fix forms); lows wait. Goal-1 round sections in reviews/2025/transcription/adjudication/<form>.md.
3. Finish with check_logs.py (federal and --jurisdiction ny): report every remaining line.
Deadline: report by 22:00 (it is 19:40); send an interim report at 21:00 with medium/high findings so far.

# MESSAGE (2026-11-16T01:49:23.781Z)

Coordinator (20:50): to avoid a second review round later, apply B1's last delta to xint BEFORE you review f2441, s1 or s2 (their logs in xint are still from this afternoon): `git -C /Users/elliotmilco/Documents/GitHub/tax-formalization/.claude/worktrees/xint apply --3way /tmp/b1w1.patch` (it applies cleanly: citation locators gaining instruction pages on f2441 lines 19/24/27, s1.line3, s2.line2; rulings in reviews/2025/{instruction_cites,limits,operands,signs}.json; a source title; tier_paths READERS; a review-tools test fix). Do it at a point where no rerun_all/classm run of yours is in flight (between batches), then build + render before reviewing f2441/s1/s2 (and any form whose render you have not run yet). If f2441/s1/s2 were already reviewed when you read this, apply it anyway and rerun only their changed lines (line-scoped). Tell me when applied.

# MESSAGE ()

Coordinator (20:50): to avoid a second review round later, apply B1's last delta to xint BEFORE you review f2441, s1 or s2 (their logs in xint are still from this afternoon): `git -C /Users/elliotmilco/Documents/GitHub/tax-formalization/.claude/worktrees/xint apply --3way /tmp/b1w1.patch` (it applies cleanly: citation locators gaining instruction pages on f2441 lines 19/24/27, s1.line3, s2.line2; rulings in reviews/2025/{instruction_cites,limits,operands,signs}.json; a source title; tier_paths READERS; a review-tools test fix). Do it at a point where no rerun_all/classm run of yours is in flight (between batches), then build + render before reviewing f2441/s1/s2 (and any form whose render you have not run yet). If f2441/s1/s2 were already reviewed when you read this, apply it anyway and rerun only their changed lines (line-scoped). Tell me when applied.

# MESSAGE (2026-11-16T01:50:18.831Z)

Coordinator: thanks. (1) Apply b1w1 between batches as you plan. (2) qdcg_amount: the integrator is removing it from tonight's merge (lands with Form 8615) — ignore it. (3) The 11 forms whose classm-jobs fail: the integrator is investigating the cause now in a scratch copy; hold those 11 class M runs until I tell you it's fixed (keep everything else going).

# MESSAGE ()

Coordinator: thanks. (1) Apply b1w1 between batches as you plan. (2) qdcg_amount: the integrator is removing it from tonight's merge (lands with Form 8615) — ignore it. (3) The 11 forms whose classm-jobs fail: the integrator is investigating the cause now in a scratch copy; hold those 11 class M runs until I tell you it's fixed (keep everything else going).

# MESSAGE (2026-11-16T02:02:22.342Z)

Coordinator: class M can build again in xint — cause was heap exhaustion in classm-jobs (the merged forms pushed the big documents over 8 GB); the integrator raised classm.py's job-building heap to 16 GB (JOBS_HEAP_MB). Release the 11 held class M forms (eic, f1040, f8889, person, s1, s2, s3, s8812, sa, sli, ssb). Each build peaks near 10 GB and job building already serialises on the jobs lock, so at most one builds at a time; keep the class M driver at ≤3 concurrent runs. Continue as planned with b1w1 at the batch boundary.

# MESSAGE ()

Coordinator: class M can build again in xint — cause was heap exhaustion in classm-jobs (the merged forms pushed the big documents over 8 GB); the integrator raised classm.py's job-building heap to 16 GB (JOBS_HEAP_MB). Release the 11 held class M forms (eic, f1040, f8889, person, s1, s2, s3, s8812, sa, sli, ssb). Each build peaks near 10 GB and job building already serialises on the jobs lock, so at most one builds at a time; keep the class M driver at ≤3 concurrent runs. Continue as planned with b1w1 at the batch boundary.

# MESSAGE (2026-11-16T02:02:57.481Z)

Coordinator: since subjects exclude citations, b1w1 does not stale any review — do NOT force-rerun f2441/s1/s2 transcription or render for it (the owner asked for no ceremonial reruns). Do not rerun f2441 class M. Holding s1/s2 class M until b1w1 is applied is fine (their excerpts read the cited pages); then run them once.

# MESSAGE ()

Coordinator: since subjects exclude citations, b1w1 does not stale any review — do NOT force-rerun f2441/s1/s2 transcription or render for it (the owner asked for no ceremonial reruns). Do not rerun f2441 class M. Holding s1/s2 class M until b1w1 is applied is fine (their excerpts read the cited pages); then run them once.

# MESSAGE (2026-11-16T02:41:24.562Z)

Coordinator: decision on your two mediums — the integrator reverts line 8u to the pre-tonight refusal in xint now (fixes -b-01 at the cause and restores -b-02's premise). HOLD class M for s1, s1a and sa until I say the revert is built (keep the rest of the queue going). Afterwards rerun s1 transcription + render line-scoped (its lines changed) and adjudicate; s1/s1a/sa class M then run once.

# MESSAGE ()

Coordinator: decision on your two mediums — the integrator reverts line 8u to the pre-tonight refusal in xint now (fixes -b-01 at the cause and restores -b-02's premise). HOLD class M for s1, s1a and sa until I say the revert is built (keep the rest of the queue going). Afterwards rerun s1 transcription + render line-scoped (its lines changed) and adjudicate; s1/s1a/sa class M then run once.

# MESSAGE (2026-11-16T02:42:09.719Z)

Coordinator: continue past 22:00 — finish the s1 work after the revert, then report once when everything is ruled (no separate 22:00 report needed; a one-line status is enough if useful).

# MESSAGE ()

Coordinator: continue past 22:00 — finish the s1 work after the revert, then report once when everything is ruled (no separate 22:00 report needed; a one-line status is enough if useful).

# MESSAGE (2026-11-16T02:43:01.947Z)

Coordinator: d-01 (MEDIUM) will be fixed by the integrator together with the 8u revert (ftc.needs1116 gains sa.excluded_income). After I say "built": rerun ftc transcription + render line-scoped as well as s1, and adjudicate. d-02 (low) waits. The D3 election question stays recorded as an ambiguity and goes on the owner's list.

# MESSAGE ()

Coordinator: d-01 (MEDIUM) will be fixed by the integrator together with the 8u revert (ftc.needs1116 gains sa.excluded_income). After I say "built": rerun ftc transcription + render line-scoped as well as s1, and adjudicate. d-02 (low) waits. The D3 election question stays recorded as an ambiguity and goes on the owner's list.

