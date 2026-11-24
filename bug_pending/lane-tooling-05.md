## BUG-NEW-lane-tooling-05 — Closure: BUG-1219 is fixed: a New York label whose line then names the federal form offers the federal line

- **Closes:** BUG-1219
- **Closure:** fixed
- **Caught by:** BUG-1219, recorded open; lane tooling of the 2026-11-24 wave (claude-opus-5-5, judgment).
- **Reproduced:** with --jurisdiction ny, transcribe.federal_labelled on IT-201 (2025) p. 2 lines 10 to 12 ('... 11 Rental real estate, royalties, partnerships, S corporations, trusts, etc. (submit copy of federal Schedule E, Form 1040) 11 ...', sources/ny/2025/ny_it201.cols.txt) returned {}: the phrase matches s1.line5's label, but the 50 words before it name no form of Schedule 1's and do not say 'federal'.
- **Change:** tools/transcription/transcribe.py: label_tail, the rest of a phrase's line (the words after it up to the next printed line number, a number not after 'form' or 'schedule', at most LABEL_TAIL = 15 words); federal_labelled credits an occurrence whose passage before it or whose tail names or implies the line's IRS form. On the IT-201 text the tail '(submit copy of federal Schedule E, Form 1040)' names Form 1040, one of Schedule 1's families, so s1.line5 is offered. test_ny_review.py: the IT-201 catalog lists s1.line5 and no longer reports it missing; label cases for a tail and for a line that ends before the next line's form name. tools/transcription/README.md says so.
- **Evidence:** across the New York documents only the ny_it201 federal catalog changes, by s1.line5 (test_ny_review.py, the catalog and prompt tests). The Schedule E lines are not offered: line 11's text names Schedule E as a form, not a Schedule E line, and line 12 ('Rental real estate included in line 11') is New York's own figure. The change applies at ny_it201's next transcription review (prompt changes apply prospectively); no review rerun here.
- **Fix lines:** none (tool change: tools/transcription/transcribe.py)
- **Tags:** tool, review-prompt, New York, transcription, fixed
