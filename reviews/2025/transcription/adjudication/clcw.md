# Adjudication — clcw

Method: `README.md` in this directory. New in Stage 20 (the Capital Loss Carryover Worksheet, i1040sd p. 10); no
earlier rounds.

## Stage 20, round 1 (superseded subject)

Fresh reviews of 2026-10-27 (claude-opus-5-5 and deepseek-flash). Both transcriptions agree on all 13 printed lines
(`../triage/clcw[.deepseek].json`: "no candidate lines"), and the class M logs have no open line. Only the renderings of
line 1 are open. Full ruling text: `.transcription/proposed/stage20/render.clcw[.deepseek].json`.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | render | 1 | ambiguity | UNCLEAR, line 15 = line 11 − line 14 not shown; 1040-NR omitted | i1040sd p. 10, line 1; 2024 Form 1040 p. 1, line 15 (not given); amb.2025.clcw_line1_signed | The recorded reading; the defining page was not given; 1040-NR is outside the tool. |
| deepseek | render | 1 | ambiguity | UNCLEAR, same | as Claude | As Claude. |

Read against i1040sd p. 10 and p550 pp. 102–103, including amb.2025.clcw_line1_signed, amb.2025.clcw_line2_printed and the
spouse screen. Lines 1–13 follow the worksheet. Line 5 is shown and zero when 2024 line 7 is not a loss ("enter -0- on
line 5 and go to line 9"). Lines 6–8 and 9–13 are hidden as their go-to instructions say. The joint/separate cases of
p. 10 and p550 p. 103 are refused by `clcw.spouse_screen`. Canceled debt excluded in 2025 is refused by
`s1.cod_unsupported`. Two problems were found by reading. They are not in any open section.

Findings: two, in `.transcription/proposed/stage20/clcw.findings.md`. F1 (low): the worksheet shows lines 1–7 with
amounts when p. 10's applicability test fails ("Otherwise, you don't have any carryovers"), e.g. a fully deducted $2,000
loss (`stage20.mut.line21_below_limit`). F2 (low to medium): `clcw.bad` accepts a line 21 loss below what any 2024 return
can show (zero after a Yes gate). With a $5,000 loss this gives a $5,000 carryover in place of $2,000.

## Stage 20, round 2

Fresh reviews of 2026-10-27, after the fixes of this file's round-1 findings: BUG-0185 (`clcw.applies` hides lines
1–5 and gates `clcw.show_st` and `clcw.show_lt`) and BUG-0186 (`clcw.bad` also refuses an entry below
`clcw.prior_floor`, the smaller of the line 16 loss and $1,500, param `clcw.prior_limit_mfs`). The first-round logs are
archived in `.transcription/archive/stage20-clcw-before-findings-fixes-2026-10-27/`. Both transcriptions agree and no
class M or deepseek render line is open; only the Claude render of line 1 is. Full ruling text:
`.transcription/proposed/stage20/render.clcw.json`.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | render | 1 | ambiguity | UNCLEAR, line 15 = line 11 − line 14 not shown; 1040-NR omitted | i1040sd p. 10, line 1; 2024 Form 1040 p. 1, line 15 (not given); amb.2025.clcw_line1_signed | As round 1. |

Fixes checked against the source. `clcw.applies` is p. 10's test, (a) line 21 smaller than the line 16 loss, or (b)
line 11 less line 14 below zero. Re-evaluating the round-1 witness `stage20.mut.line21_below_limit` now hides the
worksheet. `clcw.prior_floor` is right for any 2024 status: a correct line 21 is the smaller of the line 16 loss and
$3,000, or $1,500 if married filing separately. The $0 entry of round-1 F2 is now refused on line 2. Observation, not
ruled: `node engine/dist/main.js eval`, which evaluates every line, prints the 13 worksheet lines as UNKNOWN on a return
answering No to `sd.carryover`, because `clcw.applies` does not test the gate. The interview's demand-driven targets
should not reach them; not checked.

Findings: none new; round-1 F1 and F2 are fixed.
