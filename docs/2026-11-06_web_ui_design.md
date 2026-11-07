# T-236 web UI pilot: design

Status: approved by the owner 2026-11-06, with the second-pass addendum at the end (approved 2026-11-06).

## Goal

A locally hosted, single-user browser app on this Mac in which the owner walks the federal and New York 2025
interview with their real documents and checks every line against the filed return: when a line disagrees, the
owner can trace it, there and then, to the answer or rule that produced it. The pilot is judged on that
traceability, not on interview ergonomics. Out of scope for this pass: question ordering (T-251) and filled-form
PDFs (T-252), both due before the pilot closes.

## Owner decisions this design rests on

- Interview on the left, live values sheets on the right; completed values sheets at the end (2026-11-06).
- Refusals on an incomplete return are shown as provisional (T-248 decision, 2026-11-06); T-249 and T-250 stay open
  with no UI change.
- Node server; the build goes to one Opus agent after this design is approved (2026-11-06).
- Browser only on this Mac, not lab-server (T-236, 2026-11-04).
- No personal data is ever saved inside the project directory. The owner's answer logs live in
  `~/Documents/Tax-Interview/` (storage spec §5.3, 2026-11-06). They hold real amounts but no SSNs, account numbers or
  other identifying data, and agents may read them during the pilot. Tests still use synthetic returns in temporary
  directories (2026-11-06; supersedes the 2026-11-04 "agents never read the owner's data").
- The interview keeps offering pending questions after a refusal on an incomplete return (2026-11-06).

## Architecture

The UI is a client of the interview code (`engine/src/interview.ts`), as the CLI is. It holds no tax logic.

- **Server:** a new CLI command, `node engine/dist/main.js serve --dir <returns dir> [--port N]`, in
  `engine/src/serve.ts`. Node's built-in `http`, no new dependencies. It loads the canonical data once and keeps it
  in memory; each request replays the return's answer log, as the CLI does.
- **Page:** static files in a new top-level `ui/` (one HTML page, one script compiled from TypeScript with the
  engine's `tsc`, one stylesheet). No framework.
- **Profile:** `ny`, which asks the whole federal question set plus the New York questions and targets both
  returns. One log per return.

### Engine changes (small, shared with the CLI)

1. **One answer path.** The validation in `runInterview`'s `answer` branch (reachable-or-correction, `validateInputs`,
   evaluate the candidate before appending) moves into an exported `applyAnswer(data, config, events, input, value)`
   used by both the CLI and the server, so the two cannot drift.
2. **Pending questions after a refusal.** `interviewState` returns `question: null` once any target refuses, so today the
   interview stops at the first refusal. With eager refusals (T-248) a partial return can refuse in a way that later
   answers would clear. The state gains `pending`: the ordered list of questions still reachable (the list it already
   computes and takes the first item of). The CLI's `question` field is unchanged. The UI shows a refusal on an
   incomplete return as provisional and keeps offering `pending` questions. Only when none remain is the refusal
   final.
3. **Structured values sheet.** `renderValuesSheet` produces text. The UI needs the same content as data (form →
   entry → line: printed number, label, value, status, shown/hidden rule) so lines are clickable. The traversal is
   factored into a function returning that structure, and the text sheet becomes a rendering of it. One traversal
   means the UI and the text sheet cannot disagree about what is shown.
4. **Input metadata.** For each pending question the server attaches the input's type (from the input line's
   `ValueType`) and, for enums, the permitted values (from the params enums), so the page can choose a widget.

### API (JSON, 127.0.0.1 only)

| Route | Does |
|---|---|
| `GET /api/returns` | lists return logs in the returns directory |
| `POST /api/returns` `{name}` | starts a new log (profile `ny`, mode 0600, refuses an existing name) |
| `GET /api/returns/:name` | the state: status, pending questions with input metadata, refusal, structured sheets, values with derivations, answered inputs |
| `POST /api/returns/:name/answer` `{input, value}` | `applyAnswer`; returns the new state, or a 400 with the validation message (nothing appended) |

### The page

- **Left: interview.** The current question (first of `pending`): prompt, help, citation, and a widget by type:
  yes/no for Bool, select for enums, a dollars-and-cents field for money (converted to integer cents; a blank field
  is never sent as zero), an integer field for counts, and a list editor for rosters (entry keys validated against
  the engine's key pattern). "I don't know / need help" sends `null` (help requested), as the CLI does. Below it,
  the answered questions in order; clicking one reopens it for correction (a new log event).
- **Right: values sheets.** Federal and New York, by form, from the structured sheet: line number, label, value,
  status (value / unknown / refused). Lines changed by the last answer are highlighted. Clicking a line opens its
  derivation: operation, citation, operands with their values (each clickable), guards not taken, notes, and the
  answers it depends on, each a link that reopens that question.
- **Refusals.** On an incomplete return a refusal is labelled "provisional: later answers may clear it" (banner and
  line). On a complete return, or once nothing is pending, it is shown as final, with its gate, the form that can't be
  prepared, the remedy and the citation.
- **Standing notices and scope sentence** shown on every page, as the CLI shows them.

## Data handling

- Returns directory: `--dir` is required, with no default. The server refuses a directory inside the repository
  (resolved through symlinks), so personal data cannot land in the project. The owner runs it with
  `--dir ~/Documents/Tax-Interview`; tests pass a temporary directory. Logs are created mode 0600, and the server
  refuses a directory that is group- or world-accessible.
- The server binds 127.0.0.1 only. Because a page on another site can make the browser send requests to localhost
  (DNS rebinding), it rejects any request whose `Host` is not `127.0.0.1:<port>` or `localhost:<port>`, and any POST
  whose `Origin` is not the same origin.
- The UI asks for no identifying data (the SSN questions in the question banks ask true/false about validity, never for the number; none ask for a
  name or account number); the owner
  enters none in free-text roster keys.

## Testing (synthetic returns only)

- **Server tests** (Node, in `check-all`, fast tier): start the server on a temp dir; drive a synthetic return
  through the API. The CLI and the server must give identical states on the same log. Check that a rejected answer
  appends nothing, that roster removal and re-adding behave as the CLI does, that wrong Host and Origin are refused,
  and that file modes are 0700/0600.
- **Equivalence on existing paths:** replay the federal and New York fixtures' interview paths through the server
  and require the same final values as `test-fixtures`.
- **Browser smoke test**, on the `tools/human_review/test_browser.mjs` pattern (separately launched headless Chrome
  over the DevTools protocol, no new dependency): answer through the page, correct an earlier answer, open a
  derivation, and see a provisional refusal become final. It runs by hand, not in `check-all`, as the packet test does.
- Commit tier: the changes touch `engine/src` (not the full-tier paths), so fast tier.

## Out of scope for this pass

Question ordering (T-251), filled PDFs (T-252), printing, multiple users, lab-server or phone access, comparing
against the filed return inside the app (the owner compares by eye), and tax years other than 2025.

## Addendum: second pass (owner, 2026-11-06)

The owner's first use found that the question bank is written for the command line: entry syntax in the wording
("Answer true or false", "Money is integer cents", JSON lists), raw entry keys asked of the user, and citations that
read as instructions for what to type (the first question, `$person`, asks for keys while its citation quotes the 1040's
name lines, so a typed name is rejected). This pass fixes the presentation; it changes no tax logic.

1. **Entry syntax out of the wording.** Sentences that only state how to type an answer are removed from the
   question bank's prompts and help; substance in the same sentence stays. Each client states entry syntax from the
   input's type instead: the CLI's question gains an `entry` hint (for example "true or false", "integer cents, e.g.
   620000", "one of: single, mfj, ..."), and the page's widget needs none. A check in `check-all` fails when a prompt
   or help text states entry syntax again.
2. **Selector rule.** Any input with a fixed set of possible answers is a selector, never a text box: yes/no inputs,
   enums, and `$person`, presented as "Just me" / "Me and my spouse (joint return)" and stored as the usual keys.
   Bounded counts (months 0 to 12, percentages) become selectors once their ranges are recorded in the data, which
   the review in T-253 does.
3. **Determined inputs are not asked.** An input whose answer follows from other answers (`person.role` equals its
   entry's key) is answered by the page automatically, shown in the answered list as set automatically, and never
   presented as a question.
4. **Roster labels.** Open rosters (employers, payers, sales, dependents, ...) are entered as an "Add" list of labels the
   owner types (for example "Acme Corp"). The page derives each entry key from its label (lowercase, non-alphanumerics
   to `_`, a numeric suffix on collision) and shows labels, not keys, everywhere. Labels are saved in the answer log, on
   the roster answer's event as a `labels` map from key to label; replay ignores the field. Logs are outside the
   repository, so labels never enter it. The help keeps each roster's meaning (for `$w2`, one entry per distinct
   employer).
5. **Citations as sources.** A question's citation is shown under "Source", labelled as the form line or instruction
   the question comes from, never as instructions for what to type.

The review of every question's accepted values against its cited instructions (bounded ranges, inputs whose type
looks wrong, such as `scveh.placed_date` and `person.sep_rate` as counts) is T-253, after this pass and before the owner
resumes the interview with real data.

## Standing rules for the interview layer (owner, 2026-11-06)

The interview may only word, format, order, group and label; it never sets an input, and only the formal model's
reachability makes a question disappear. The rules, their enforcement and the rare-situation pages are in
`docs/2026-11-06_formal_gates_design.md`, which governs this UI from here on.
