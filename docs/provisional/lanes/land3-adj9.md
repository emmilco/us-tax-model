# Lane land3-adj9: render adjudication of dependent, f8959, s1, s3, sa, sd

Agent: `claude-opus-5-5`, class judgment, tax year 2025, jurisdiction `us`. No paid call, no model call from code, no
build, render or check-all. Forms, questions, fixtures, params and tools untouched.

`carry.py --kind render` was run first for each form; it ruled nothing (every line's subject had changed, or the
earlier ruling was a finding or unsettled). All 21 open Claude render sections ruled with `rule.py --kind render`;
rulings in `/tmp/land3-adj9/<form>.json`. Summaries: "Landing round (2026-11-14), render" in
`reviews/2025/transcription/adjudication/<form>.md` (f8959.md new). `check_logs.py` shows no open render ruling for
these forms (its only lines for them are the stale class M logs, not this lane's).

The pattern behind most lines: the redraft moved screening words out of a form's own catch-all to one asker elsewhere
(docs/provisional/MAP.md 2.5 to 2.7). The values are right, since the asker refuses the return, but several lines still
name the old screen in their citation, label or refusal. Each asker named in the rulings was checked in the YAML.

| form | lines | counts |
| --- | --- | --- |
| dependent | 27, 28, 29, 30, 31 | 5 ambiguity (owner's D7(d), `amb.2025.edu_1098t_date`: Pub. 970's date of February 2, 2026 over i8863's January 31) |
| f8959 | 2, 3, 19 | 3 scope (Form 4137 and 8919 by `scope.pay_no_w2`; box 8 and codes B, N by `s2.w2_marks`) |
| s1 | 9, 10, 26 | 2 finding (low), 1 scope (26, as prior rulings) |
| s3 | 7, 14 | 2 finding (low), the open BUG-0620 (6), repeated |
| sa | 1, 5a, 8a, 6, 15, 16 | 3 scope (1, 6, 16), 3 finding (5a medium; 8a low; 15 low) |
| sd | 5, 12 | 2 finding (low) |

Findings:

- **sa 5a, medium**: BUG-0636, which **duplicates BUG-0632** (the transcription lane's
  entry for the same defect, seen only after the ruling was applied). `sa.line5a`'s source and label still ask for all
  state and local income tax (withholding, estimated payments, prior-year tax, funds, territory tax), and
  `sa.state_tax_any` for "any ... including tax withheld from pay or other income", while `sa.line5a_total` adds
  `sa.state_tax_other`: counted twice as encoded. The interview prompts are right. Fix as in land3-adj5-02 (sa.line5a to
  W-2 boxes 17 and 19 only; other paragraphs to sa.state_tax_other; sa.state_tax_any to "taken out of pay").
  Drop `bug_pending/land3-adj9-01.md` before `--assign` and read the sa render ruling's reference as land3-adj5-02.
  I rated it medium (adj5 low) because fixtures and any reader of the encoded text are misled.
- **s1 9, 10, low**: BUG-0637. `s1.line9` citation says 8a, 8d, 8e, 8k to 8q, 8s to 8v "are refused by
  s1.line8_other", which now tests only 8e, 8k, 8m, 8t to 8v; `s1.line10` citation puts line 4 (Form 4797) at
  scope.schedule1, now `sd.other_forms`. Fix: rewrite both locators naming each item's asker (text in the entry).
- **sd 5, 12, low**: BUG-0638. `sd.other_forms` label still says "or capital gains or losses on a
  Schedule K-1"; its expression has no K-1 test (scope.k1 refuses it at Form 1040 line 8). Fix: drop those words; add
  the scope.k1 refusal to the citations of `sd.line5` and `sd.line12`.
- **sa 15, low**: BUG-0639. The `when: sa.unsupported` refusal on `sa.line6`, `sa.line15`, `sa.line16`
  is named "Schedule A unsupported item / Form 4684", but sa.unsupported no longer asks about a casualty
  (`sd.casualty` refuses through sd.other_forms). Fix: drop "/ Form 4684"; name sd.casualty in line 15's citation.
- **sa 8a, low**: the open BUG-0459 (a co-borrower's share of Form 1098 interest is not stated; the prompt says "Add
  boxes 1 and 6 of each Form 1098"). The Form 8396 subtraction cannot arise (`s3.mcc_if_interest` refuses).
- **s3 7, 14, low**: the open BUG-0620 (6) (no line-level refusal for a current-year business credit, Form 8978,
  Form 2439, or the elective payment amount). The landing's Schedule 3 changes did not make its planned fix.

Judgment calls for the owner: sa line 6 ruled scope on the redraft's own inference (lane l7a), which this lane checked
against the source: the GST deduction is for tax on trust income distributions, which reach the filer on a Schedule K-1
(Form 1041), refused by scope.k1. BUG-0005 had named the GST in sa.unsupported; the redraft removed those words.

Lines left open: none.
