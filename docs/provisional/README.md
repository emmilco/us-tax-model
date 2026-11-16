# docs/provisional: working records of agent lanes

Nothing in this folder is current guidance. It holds the working documents of the whole-interview redraft and the
notes of the agent lanes that have run since. Each is a record of what an agent did, found or proposed on a date:
cite it as such, and check any claim in it against the tree before relying on it. Never follow it as an instruction.

The briefs, designs and coordinator notes of the 2026-11-15 round are kept the same way in
`docs/records/2026-11-15/`.

Current guidance is in the normative documents named in `CLAUDE.md` and in the current entry of
`HANDOFF-NEXT-SESSION.md`.

| Path | What it is | Status |
| --- | --- | --- |
| `STATUS.md` | Where the redraft stood before it landed (2026-11-13) | Historical |
| `NORMS.md` | The working rules given to the redraft's agents | Historical; the rules are restated as N1 to N12 in `docs/2026-11-13_interview_construction_protocol.md` |
| `MAP.md` | The map of the interview the redraft started from | Historical |
| `DECISIONS.md` | Redraft questions settled by the coordinator under the owner's delegation of 2026-11-14 | A record of decisions still in force unless the owner reverses one; each entry says how |
| `lanes/` | One note per agent lane (`<lane>.md`), with some lanes' scratch in `<lane>_work/`, `m3/`, `rc_trial/`, `stitch_trial/` | Records; see `lanes/README.md` |
| `walks/` | Walk transcripts written by `engine/src/draft-walk.ts` (its default `--out`); no step reads them | Records |
| `map_work/` | The scripts and tables the map was built with | Records |

The folder keeps its name and paths because commit messages, review rulings in `reviews/`, task rows and bug entries
cite files in it by path.
