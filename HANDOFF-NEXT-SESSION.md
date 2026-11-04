# Round 2 and the tooling batch — 2026-11-04

**State:** the tooling batch is f27d71d (T-218 carry-over, T-219 line-scoped reviews, T-220 yield, T-225, T-228 and
the P5 rows). Round 2 is the commit after it:
- the review-tool rows T-223 (ruling stamps), T-224 (mechanical model-error rulings), T-226 (BUG-0411), T-227 (foreign interfaces);
- the engine rows T-206 (class M selection on route branches) and T-213's input check (BUG-0412);
- the form pass: every BUG-0402 low (BUG-0408), T-216 (BUG-0409), T-215 (BUG-0410), the NUA refusal (BUG-0413), T-201 and T-207;
- the first real line-scoped review round on the 17 changed forms, with completeness and screens, all adjudicated.

Round 2 cost $41.12 in paid calls (90 calls); the yield report has an exact-join table from now on.

**Decisions taken under the standing instruction (Elliot can reverse):**
- T-191: the `bracket_schedule` op form stays in the frozen vocabulary.
- T-181 and T-208: left open as coverage expansion.
- Stale DeepSeek transcription logs of ineligible changed forms are archived (`.transcription/archive/stale-deepseek-transcription-2026-11-04/`), not rerun.
- `--lines auto` records a verified line-subject table for a pre-table log with no stale line, with no model call.
- Sibling-form review evidence comes from a line-scoped review of the sibling lines alone (f1040, f8863).

**Owner questions:** T-232 (`expect_shown`, a fixture-schema and spec change); whether transcription reviews should stop running on wording-only changes (round 2: $20.48 for 0 findings; completeness $6.70 for 1 medium and 12 lows).

**After the round-2 commit (T-094):** every form is now completeness-reviewed. f4952 and f8880 use their printed instructions; person is reviewed
whole, with the prompt limit raised to 700k characters. Cost $2.23; 2 more lows were added to BUG-0414's list.

**Round 3 (after the T-094 commit):**
- every BUG-0414 low is fixed (BUG-0415), and round 3's own lows are fixed too (BUG-0416);
- T-232 is done with no schema change: source-predicted gate values on class A and synthetic regression cases, plus 10 new synthetic cases, kill 138 of the 145 display-condition mutants, and a new rule (conjunctPrefix) proves 5 more equivalent;
- T-231 and T-196 were closed by cost decision;
- the two rare sales lows (BUG-0417) and the findings of the sales reviews after them are fixed (BUG-0418); the last sales completeness review found nothing that isn't refused elsewhere.

Paid calls this round: $36.85 (70 calls).

**Next:** T-217 after 2026-11-06 15:49; the owner question on transcription for wording-only changes; coverage expansion stays last.

---

# Backlog and refresh rounds — 2026-11-03

**Owner decisions (2026-11-03):**
1. Inference cost: use inference only where it adds evidence (CLAUDE.md, "Inference cost"). Review and adjudicate only forms whose content changed; review-prompt changes apply prospectively; Sonnet for mechanical agent work; every paid call is logged in `.transcription/costs.jsonl` and every agent run in `research/costs/agent_runs.jsonl`. Tooling to build: T-218 (mechanical carry-over of repeat rulings), T-219 (line-scoped reviews), T-220 (findings per dollar), T-221 (noise comparison of the archived v3 replies).
2. The transcription catalog is a subset chosen from the IRS source (prompt policy `source-only-computation-v3`, BUG-0390), with the T-163 `shown_when` note.

**State:** commit 0a43f15 integrated eight parallel packages (BUG-0341 to BUG-0390). The refresh-round commit after it fixed T-212, T-210, T-175, T-211, T-214, T-205 and the T-101 remainder (BUG-0391 to BUG-0401), recorded the refresh lows as BUG-0402 (T-222), and reran and adjudicated the 17 changed forms only; the 45 unchanged forms keep their v2 logs, and their v3 replies are archived for T-221. GPT-6 Astra is at codex's usage limit until 2026-11-06 15:49 (T-217); its stale logs are archived in `.transcription/archive/stale-gpt-logs-2026-11-03/`.

**Next:** T-218, T-220 and T-219 (T-221 closed by the owner: the measurement would not change a decision), then T-222 and the remaining open rows; T-217 after 2026-11-06. Coverage expansion stays last.

---

# F1 and T-176 integration — 2026-11-03

**Owner decisions (2026-11-03), on the F1 owner questions:**
1. The dependency and EIC tie-breaker refusals stay when the other person is a non-taxpayer (no exception in p501 pp. 15-17; a refusal cannot give a wrong answer).
2. T-113's "or filer" means the filer who is the student; a filer with only an applied-for ITIN claiming the lifetime learning credit for a student with an issued number is not refused (i8863 Table 1).
3. T-104's question covers a child kidnapped before 2025 and still missing at some time in 2025.

**State:** T-176 (BUG-0325, fixed by BUG-0328) is on `main`. The F1 cloud batch (T-104 to T-113, T-153, T-154, T-167, T-168; BUG-0329 to BUG-0337, open BUG-0338 and BUG-0339) is integrated on this branch with its DeepSeek reviews rerun locally. Next: integrate `claude/t159-mutation` (tier 1 shipped; tier 2 still gated with 114 unexplained survivors), then T-178 to T-185 and the remaining backlog.

---

---

Older entries (2026-10-31 to 2026-11-03) are in [handoffs/HANDOFF-NEXT-SESSION-ARCHIVE-2026-11.md](handoffs/HANDOFF-NEXT-SESSION-ARCHIVE-2026-11.md).
