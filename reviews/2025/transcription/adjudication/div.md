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
