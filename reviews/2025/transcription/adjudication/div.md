# Adjudication — div

Method: `README.md` in this directory. Earlier rulings for div are only in the log sidecars (`../div[.deepseek].rulings.json`,
`../../render/div[.deepseek].rulings.json`); this summary starts with the backlog round.

## Backlog round

Subject after the p4-docs package, which links `amb.2025.div_gain_portions_disjoint` from `div.bad_special`. No expression
changed. The render reviews of 2026-11-03 (Claude and deepseek-flash) each have one open section. The transcription logs of
2026-11-02 have none. Rulings are in `.transcription/proposed/bklg/render.div[.deepseek].json`.

Counts:
- render div: ambiguity 1
- render div.deepseek: model error 1

| family | kind | lines | class |
| --- | --- | --- | --- |
| claude | render | bad_special | ambiguity |
| deepseek | render | unsupported | model error |

Findings: none. The new link matches the register's chosen reading (boxes 2b, 2c and 2d disjoint), which is what the Claude
render reviewer questioned.

## Landing round (2026-11-14)

Interview redraft (landing worktree), Claude line-scoped pass 50da04a040c2. Triage `.transcription/triage/2025/div.json` (executable-triage-v2, regenerated 2026-11-14 on the fresh build; not rerun). Rulings applied with `rule.py`; full text in the log and sidecar.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | div.box2b_if_capital_gain | representation | 2,916/2,974; 4 candidate-unknown, 54 project-unknown; no value | f1099div p. 5, Box 2b | Box 2b is a portion of box 2a; the reply drops the box 2a parent. |
| claude | transcription | div.box2d_if_capital_gain | representation | 2,916/2,974; 4 candidate-unknown, 54 project-unknown; no value | f1099div p. 5, Box 2d | As box 2b. |

Counts: representation 2 (2). Findings: none. Project lines unchanged.

## Landing round (2026-11-14), render

Lane land3-adj7 (claude-opus-5-5, judgment). Open lines of the Claude render log `.transcription/logs/2025/render/div.md`, ruled on the rendered English (`rendered/2025/div.md`), the form YAML and the cited source; the deepseek log is dormant and not ruled.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | render | bad_special | ambiguity | UNCLEAR; ambiguity register | f1099div p. 5, boxes 2b-2d; amb.2025.div_gain_portions_disjoint | The model objects only that disjointness is unstated, the register's text at issue; the chosen reading can only refuse an entry. |

Counts: claude render: ambiguity 1.

Findings: none. No line left open.
