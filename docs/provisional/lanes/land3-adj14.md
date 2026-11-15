# Lane land3-adj14: last-round adjudication of sa and scope

Agent: claude-opus-5-5, judgment; tax year 2025, jurisdiction us. Worktree `.claude/worktrees/landing`. No build, no
paid review, no commit. Rulings in `/tmp/land3-adj14/` and applied with `tools/transcription/rule.py`; summaries
appended to `reviews/2025/transcription/adjudication/sa.md` and `scope.md`.

## sa

- Transcription (pass 51a9b88c8eed), 1 representation: line 16. 3,717 compared, no value difference. The differences
  come from the reply reading `sa.gambling_losses` without its winnings gate, and from where refusals sit. Without
  winnings, s1.line8b is 0, so both sides give 0.
- Render (pass e804cc14a78b), 3 scope:
  - Line 6 (GST): refused through `scope.k1` (a Schedule K-1 from Form 1041), as ruled in the previous round.
  - Line 15 (casualty): `sd.casualty` is asked of every filer and refuses through sd.other_forms. A refusal fixture
    exists in mutation.json, and the line's citation now names this refusal.
  - Line 16 (the other list items): refused by `sd.casualty`, `s3.repaid_income` and `sa.unsupported`.

## scope

- Transcription (pass 2eb39b30c079), 1 model error: `scope.schedule1`. This is the same pattern as the two earlier
  rulings today. The 59 value differences are all refused returns where the project says true and the reply says
  false (rental, clergy). The reply's extra CFC term changes nothing, because scope.other_line16 already refuses it.

## Findings

None. No line was left open. `check_logs.py` shows no open ruling for sa or scope.
