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
