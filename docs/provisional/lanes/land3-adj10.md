# Lane land3-adj10: adjudication of scope and s2 after the scope-hole fixes

Agent: claude-opus-5-5, judgment; tax year 2025, jurisdiction us. Worktree `.claude/worktrees/landing`. Not committed. No
paid review call and no model call from code. Rulings text in `/tmp/land3-adj10/`.

Triage records were newer than the transcription logs, so triage was not rerun; carry (transcription and render) ruled
nothing.

## scope

- Transcription (pass b8c2e2325e96): 1 model error (`scope.schedule1`, same pattern as the earlier landing ruling;
  the ungated `scope.nol` agrees).
- Render (pass 1b4bf43be4e1): 8 interface gap, 1 finding.
  - interface gap: armed_forces, pay_no_w2, w2_marks, artist_official_if_w2, disaster_distribution, reforestation,
    passive_if_business_before, other_line16. Each objection is answered by a source the reviewer was not given
    (p590a, fw2/p525, p463, i8915f, i4562) or by a screen on another form (s2.w2_marks for W-2 box 8,
    retirement.disaster, sc.passive/scope.rental/scope.k1/scope.farm, the retirement lump-sum screen).
  - finding, medium: recovery, BUG-0640.

## s2

- Transcription: no open section.
- Render (pass 5a2c65cfce89): 1 interface gap (line 21: Forms 4137/8919 refused by scope.pay_no_w2 and
  person.se_screen; installment-sale interest by sd.sold_other / sd.installment).

## Findings

BUG-0640 (medium), `scope.recovery`. Source p525 p. 24: a recovery is of an amount "you deducted or took a
credit for", and Schedule 1 line 1 covers state and local income tax refunds. The question names only a deduction, so a
recovered credit is answered No and left off line 8z; and it excepts only a state refund, so a local income tax refund,
which the refund form prepares, is refused. Proposed fix (forms/2025/scope.yaml `scope.recovery` label and source;
bank tick at order 161 seq 6): "In 2025, were you (or, on a joint return, your spouse) paid back an amount whose
deduction or credit on an earlier year's return lowered your tax, other than a state or local income tax refund?";
tick "Paid back a deduction or credit that lowered your tax (not a state or local income tax refund)"; cite p525 p. 24.

## Left open

None.

## Residual edges noted in rulings (not findings)

- artist_official_if_w2: an official paid wholly in fees with no W-2 is not asked; the return is the one a No gives.
- disaster_distribution: a late-2025 repayment of a 2022 distribution goes on the 2025 Form 8915-F but is carried back;
  2025 tax unchanged.
- other_line16: a section 965(i) shareholder with no 2025 day of S corporation stock escapes scope.k1 (IRC 965(i), not
  in the archive).
