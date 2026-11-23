## BUG-NEW-release-prep-10 — Student loan interest someone else paid on the borrower's loan is not named as the borrower's, so it can be left out

- **Date:** 2026-11-23
- **Caught by:** the sampled reviews of the release run, adjudicated in release preparation 2 (claude-opus-5-5, judgment), 2026-11-23: false-no review of gate:sli.any_if_not_mfs, finding 0; screen review of the same gate, finding 0; completeness claim sli#1.3.
- **Source:** p970 p. 33, Interest paid by others: 'If you are the person legally obligated to make interest payments and someone else makes a payment of interest on your behalf, you are treated as receiving the payments from the other person and, in turn, paying the interest' (Example 2, a mother's gift).
- **Symptom:** The sli.any tick ('Paid interest on a student loan') and its help, and the sli.interest question, say nothing of payments made by another person. A borrower whose parent or employer (through W-2 box 1) paid the interest answers No, and the Schedule 1 line 21 deduction is lost.
- **Where:** interview/2025/questions.yaml sli.any (help) and sli.interest (help); forms/2025/sli.yaml sli.any.
- **Proposed fix:** Add to the sli.any help: 'Count interest someone else paid on a loan you owe, such as a parent's gift or an employer's payment added to your W-2 box 1; it counts as paid by you.'
- **Proposed fix lines:** sli.any, sli.interest
- **Severity:** low
- **Tags:** sli, interview, wording, sampled false-no review; open
