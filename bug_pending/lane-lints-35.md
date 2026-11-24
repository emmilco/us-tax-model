## BUG-NEW-lane-lints-35 — rec.medical: "your 2024 medical and dental bills" can be read to leave out a dependent's bills deducted on the 2024 Schedule A

- **Date:** 2026-11-24
- **Caught by:** the question review of 2026-11-24 (claude-opus-5-5), sample #1 on the reworded question, ruled in lane lints (claude-opus-5-5, judgment)
- **Source:** p525 p. 27, Worksheet 2, line 2, "Enter the total of all other Schedule A (Form 1040) refunds or reimbursements"
- **Symptom:** A filer whose insurer repaid in 2025 a dependent child's 2024 bills, deducted on the 2024 Schedule A, can leave the repayment out; the recovery is understated.
- **Where:** interview/2025/questions.yaml rec.medical (prompt).
- **Proposed fix:** Ask for the repayment of "the 2024 medical and dental bills you deducted on your 2024 Schedule A, including a dependent's".
- **Proposed fix lines:** rec.medical
- **Severity:** low
- **Tags:** recoveries, wording, question review; open
