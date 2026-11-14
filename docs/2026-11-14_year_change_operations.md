# Year changes as operations (T-256 phase 1, charter section 7 item 1)

Design written 2026-11-14 by a judgment-class agent (claude-opus-5-5), year 2025, jurisdiction us, before the
tool was built. It replaces the way a prepared year change is kept: today a full copy of a 2025 form plus a line
diff (`research/ty2026/forms-proposed/`), which decays unnoticed as the 2025 form changes
(`docs/2026-11-09_ty2026_rollover_measurement.md`, H10: 2 of 10 hunks of `sa.diff` stopped applying within five
days). Here each change is a set of operations keyed by line id, kept as data, applied mechanically at adoption,
and checked against the current forms on every commit.

## 1. Where the operations live

`changes/<year>/<form>.yaml` holds the operations that take the definitions of `<year> - 1` to `<year>`, one file
per form they act on (`changes/2026/f1040.yaml` acts on `forms/2025/f1040.yaml`); a new form has its own file.
New York, when it has operations, uses `changes/ny/<year>/` (the charter's `<kind>/ny/<year>/` convention). The
build does not read them; `tools/year_changes.py` does.

```yaml
changes:
  tax_year: 2026          # the year the operations produce
  form: f1040             # the form they act on (or the new form a file adds)
  entries:
  - change: C-PRI-02      # the change-map entry (research/ty2026/changes.md)
    evidence:             # where the new year says so: archived document, PDF page, quote printed there
    - {doc: f1040, page: 3, quote: "13a Additional deductions from Schedule 1-A, line 44"}
    verified: draft       # draft: rests on an IRS draft; final: checked against a final edition
    operations:
    - set: {line: f1040.line13b, field: printed, from: 13b, to: 13a}
    - set: {line: f1040.line13b, field: label, from: "...line 38", to: "...line 44"}
```

An entry is one change of the change map for one form: its evidence and its operations. Several operations share
one entry's evidence, so the evidence is stated once.

## 2. Operation kinds

| Kind | Fields | What it does |
|---|---|---|
| `add_line` | `after`, `line` | inserts a whole new line after the line `after` (an existing line or one an earlier operation adds) |
| `remove_line` | `line` | removes a line |
| `set` | `line`, `field`, `from`, `to` | replaces one field of a line: `printed` (a line moved to another printed number), `label`, `expr` or a key path inside it (`expr.take`, `expr.of`, `expr.ref` for a parameter reference), `cite` or `cite.locator`, `refuses`, `type`, `ambiguity`, `gated_by`, `shown_when`, `note`. `from: null` means the field is absent; `to: null` removes it |
| `add_form` | `form` | a new form file (its whole document) |
| `set_form` | `field`, `from`, `to` | a form-level field (`title`, `note`) |
| `add_question` | `input`, `like` or `after`, `entry` | the question-bank entry of a new input: placed after the bank entry of `like` (whose entry it copies, then overrides with `entry`, and whose place in every profile it takes) or `after` |
| `remove_question` | `input` | the bank entry of an input that goes, and its place in the profiles |
| `set_question` | `input`, `field`, `from`, `to` | one field of a bank entry (`help`, `prompt`) |

Ids survive renumbering (spec 4.3), so a line that moves to another printed number is a `set` of `printed`, never
a new line. `field` is a path of mapping keys; a list is replaced whole (a sum's `of`), so an operation never
depends on a list position.

## 3. What "applies" means

The operations of a year are applied in memory, file by file and in order, to the previous year's forms, question
bank and profiles. Each fails, naming its file, change, position, kind and line, when:

- **gone:** its line, form or `after` anchor does not exist (a renamed line shows as gone; the closest existing ids
  are suggested);
- **stale:** the field's current value is not `from` (the text it expects to replace has changed); the current
  value is shown beside `from`;
- **already applied:** the current value is already `to`, or an added line, form or question already exists;
- **collision:** two operations set the same field or a field and a path inside it, an operation acts on a line
  another removes, or two add the same id;
- **dangling:** after all operations, a line an operation added or changed reads a line id that does not exist, or
  any line, question, profile, refusal note, conflict check or coverage row still names a line an operation
  removed;
- **gated read:** a line an operation added or changed reads a gated input other than through its gate line (the
  formal gates rule, `engine/src/gates.ts`, which the build would otherwise report only at adoption);
- **input without question:** a new input (an added line, or a line set to `op: input`) has no question, or a
  question is left for a line that is no longer an input;
- **evidence:** a cited document is not in the new year's archive, a quote is not printed on its page (either text
  layer, normalized as `tools/citations.py` does; the page where it is printed is named if there is one), or an
  entry is marked `final` while a document it cites is still a draft.

Two things are reported without failing: the parameters the operations read that `params/<from>.yaml` does not
define (the meeting point with the parameter lane, below), and entries marked `draft` whose documents are all final
now (to verify and mark `final`).

## 4. The check, adoption and the tools that follow a form change

**Check.** `tools/year_changes.py --check` (check-all step `year_changes`, fast and full tiers, wave 1) applies the
operations of the year after the run's year to that year's forms and fails on any failure above. It reads 62 form
files, the bank and profiles (about 0.5 s with the C YAML loader) and the archived pages its evidence cites. It
belongs in the fast tier: any change to `forms/`, `interview/` or `changes/` needs it; a docs-tier commit cannot
change its result. `--against <dir>` runs the same check, read-only, on another tree's `forms/<year>`,
`interview/<year>` and `params/<year>.yaml` (an exported branch). `--self-test` plants every failure above in a
small synthetic tree, and checks that applying to files keeps every untouched line block byte-for-byte and
yields the same data as applying in memory.

**Adoption.** `year_diff.py --adopt` checks the operations against the from-year first and refuses to adopt when
any fails. It then copies and relocates as before, and applies the operations to the copied files: an operation's
values are written for the new year's text, so they replace the relocated values of the fields they set, and
their new lines are not relocated. A file is edited block by block (a line, a bank entry); every block no
operation touches stays as the copy wrote it.

**Fixtures.** `fixtures_year.py` re-evaluates every case on the adopted definitions, so an operation needs nothing
from it. A new input needs a test-data default (`fixtures/<year>/defaults.json`); the check names new inputs, and
adding their defaults at adoption is left to `fixtures_year.py` (not built here).

**Question bank.** `add_question`, `remove_question` and `set_question` are the bank side of an input that comes or
goes; the check enforces that every new input has a question and no question outlives its input.

**Citations.** Page moves of unchanged citations remain `citations.py --relocate`'s; an operation sets a citation
only when its words change (a quote no longer printed, a line number in the locator), and its value is written for
the new year's pages.

**Review carry.** `year_carry.py` decides which reviewed lines carry by comparing each line's year-normalized
subject and cited text across the two trees. The operations are the declared list of what changed: every line an
operation adds, sets or reads through a changed line has a different subject, so it is reviewed; a line whose key
differs but that no operation touches changed through year normalization or its cited text, which is what
`year_carry.py` reports on its own. A cross-check of the two lists is left for when a year is adopted.

**Other lanes.** Parameters, enum values and tables live in `params/` and `tables/` and are not operations: a
`set` of `expr.ref` changes which parameter a line reads, never a parameter's value. The check lists the
parameters operations read that the from-year does not define; the parameter lane's 2026 file must define them, and
at adoption they are checked against it. Year-free ids (another lane) rename 2025 ids; an operation naming a
renamed id fails as gone, which is the intended signal. New York has no operations yet; the tool takes
`--jurisdiction ny` through `tools/jurisdiction.py` like the other year tools.

## 5. The 135 changes of the preparation, by operation kind

Each change-map entry of `research/ty2026/changes.md` was classified by the operations it needs (an entry may need
several) and by what it needs outside them. Counts are of entries.

| Kind | Entries | | Outside the operations | Entries |
|---|---:|---|---|---:|
| `set` of `expr` (a rule) | 35 | | parameters, enum values, tables (other lanes) | 34 |
| `set` of `label` | 33 | | no change to the encoding | 10 |
| `add_line` | 28 | | year literals (year-free ids lane, `--adopt`'s list) | 10 |
| `set` of `cite` (requoted) | 28 | | not encoded (refused or outside scope) | 9 |
| `set` of `printed` (renumbering) | 16 | | page moves only (`--relocate`) | 7 |
| `add_question` | 12 | | ambiguity register entries | 4 |
| `remove_line` | 9 | | waiting for a 2026 source | 2 |
| `remove_question` | 5 | | | |
| `set_question` (help text) | 3 | | | |
| `set` of `refuses` | 2 | | | |
| `add_form`, `set_form` | 1, 1 | | | |

83 entries need at least one operation; 63 of them are expressed wholly by operations, and 20 also need a
parameter (15), a register entry (4) or a year literal (2). 52 need no operation: 19 are parameters only, 10 change
nothing, 9 are not encoded, 8 are year literals or page moves, 2 wait for a source. **No change of the 135 needs a
kind of operation not listed in section 2.** What operations cannot express is everything kept outside the form
files: the four entries that add or re-rule ambiguity register entries (C-PRI-15 `amb.2026.gift_floor_base`,
C-SCHED-28, C-CRED-02, C-CRED-05), the enum value C-PEOP-05 adds (`early_exception: e24`, in `params/`), and the
amounts. The register is id-keyed and could take the same treatment; it is left out here (section 7).

The classification is a reading of each entry's kind, touched ids and notes, not of the 2026 text; the per-entry
list is in `changes/2026/README.md`.

## 6. The preparation converted

The proposals in `research/ty2026/forms-proposed/` (Form 1040, Schedule A, Form W-2, the Schedule C vehicle lines
and the new Schedule 3-A) are converted to operations against the 2025 forms on `main`, by comparing each proposal
with the 2025 file it was copied from (its blob is named in its `.diff`) line id by line id, and re-basing each
difference on the current form. Where the current form moved since 2026-11-04, the operation is mended and the
mend recorded in the entry. The proposals stay in `research/` as the record of the preparation.

## 7. Left out

- The ambiguity register (`ambiguities/<year>.yaml`): no operation adds or changes an entry.
- Enum values and parameter values: other lanes (section 4).
- Defaults of new inputs in `fixtures/<year>/defaults.json`, and the other places a new input reaches
  (`engine/src/generate.ts`, `tools/engines/generate_cases.py`, the input contracts): named by the check, not
  written.
- Whether an applied tree builds: the check is structural (references, gates, questions, evidence), not the
  build; types and guard exhaustiveness are checked by the build at adoption. A full build of the applied tree on
  every commit would cost a scratch year (manifest, parameters) and minutes; it is the adoption's step.
- An operation authoring aid that writes operations from an edited copy of a form: the conversion of section 6
  used a one-off comparison; the tool's `--record` mode does the same for one form.
