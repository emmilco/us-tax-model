# Adjudication — ssb

Method: `README.md` in this directory. Triage record: `../triage/ssb.deepseek.json`
(executable-triage-v1; 1,083 fixtures, 500 generated returns, seed 20261026, 168 partial records).
DeepSeek family only. Full ruling text is in the log and its sidecar.

## First adjudication (superseded subject)

| family | line | class | triage | deciding source | reason |
| --- | --- | --- | --- | --- | --- |
| deepseek | ssb.has_benefits | representation | 1,751/1,751 agree | i1040gi p. 31, Lines 6a and 6b | Both test the box 5 total; line 1 copies ssb.benefits. |
| deepseek | 6 | ambiguity | 1,738/1,751 agree; 11 candidate-unknown, 1 candidate-refuses, 1 project-refuses | i1040gi p. 32, line 6; p. 31, Exception | Reads Schedule 1 line 20 literally, the text at issue of amb.2025.ira_ssb_copy; the witnesses show the line 20 to line 9 cycle the register resolves. |
| deepseek | 8 | representation | 1,751/1,751 agree | i1040gi p. 32, line 8 | Same status amounts; guards grouped differently. |
| deepseek | 10 | representation | 1,751/1,751 agree | i1040gi p. 32, line 10 | Same status amounts; guards grouped differently. |
| deepseek | 16 | scope | 1,722/1,751 agree; 23 project-unknown, 5 project-refuses, 1 candidate-refuses | i1040gi p. 32, line 8; p. 31, Line 6c | Same computation; the project's lump-sum refusal sits on line 2, the candidate's on line 18, so line 6b refuses on both. |
| deepseek | 18 | model error | 529/1,751 agree; 986 candidate-unknown, 232 candidate-refuses, 4 project-refuses | i1040gi p. 31, Line 6c, "If any of your benefits are taxable" | No zero-benefit guard and an unconditional lump-sum refusal, so it asks the lump-sum election on every return. |

Findings: none. Project lines unchanged.

## Fix round 2

The subject after BUG-0249 reworded `ssb.terror_disability`: "for the September 11 attacks, any injury eligible for coverage
by the September 11 Victim Compensation Fund, whether or not you made a claim". No ssb expression changed. Both families
were reviewed. Triage is `../triage/ssb[.deepseek].json` (executable-triage-v2: 1,382 fixtures, 500 generated returns with
seed 20261026, 156 partial records from 40 bases, 2,038 comparisons). An uncapped scratch re-run gave the same counts. The
rulings are in `.transcription/proposed/fixr2/` (`transcription.ssb[.deepseek].json` and `render.ssb.json`).

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | ssb.has_benefits, 8, 10 | representation | 2,038/2,038 | i1040gi pp. 31-32 | Same tests and status amounts. |
| both | transcription | 6 | ambiguity (+ scope; claude + model error) | 10 completed candidate-unknown, all IRA returns with $0 benefits (cycle or line 18's screens); refusals ira.cov_gate / ira.less_gate | i1040gi pp. 31-32; amb.2025.ira_ssb_copy | Reads Schedule 1 line 20 literally. |
| claude | transcription | 9 | representation and scope | 312 completed project-unknown and 4 completed project-refuses, all $0 benefits (worksheet unused, line 18 $0); 65 values, all MFS-together on refused returns | i1040gi pp. 31-32 | No Form 1040 amount differs; MFS refused. |
| claude | transcription | 18 | model error and ambiguity | 198 completed candidate-unknown (f1040.tax_exempt_interest, $0 benefits), 4 cycle | i1040gi p. 31 | No zero-benefit guard. |
| deepseek | transcription | 8, 10 | model error and scope | 128 values, all MFS-together, refused | i1040gi p. 32, line 8 | $25,000 / $9,000 on a skipped line, unreachable. |
| deepseek | transcription | 18 | model error (+ scope) | 514 completed candidate-unknown (pub915 490), 4 completed candidate-refuses (pub915 supplied with $0 benefits) | i1040gi p. 31 | Pub. 915 screens asked of every return. |
| claude | render | 6 | scope | MISMATCH | i1040gi p. 98, line 12; amb.2025.ira_ssb_copy | Deduct-less election refused for the return by ira.less_gate (checked with benefits). |

The brief's check: the new wording is i1040gi p. 31's own rule ("injuries eligible for coverage ... are treated as
incurred as a direct result of the attack"). It is not wider than the source and not narrower, and the gate refuses as
before. Findings: none. Observation: without benefits the project's worksheet lines 2 to 17 show as awaiting the
Pub. 915 screens, which the interview does not ask. No amount is shown, line 18 is $0, and nothing is printed on Form
1040 from them.
