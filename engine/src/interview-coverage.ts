// The situations the interview is known to handle, checked against the built interview (`interview-coverage`, in
// check-all). Deterministic and free: no model is called. A row (interview/<year>/coverage/<part>.yaml) names a
// situation as the answers a filer in it gives and the end the interview must come to; the check walks the built
// question tree with those answers, in the interview's own order, and fails naming the row when the tree does not end
// there.
//
// The walk. Each step reads the interview's next question from `interviewView` and answers it through `applyAnswer`,
// the path the page and the command-line interview answer through, so an answer the interview would reject is
// rejected here and whatever an answer records is recorded here. The walk ends, as a filer's does, at the first
// refusal or at completion; or earlier, at the question the row expects to be asked, or (a `records` row) once the
// row's own answers are all given.
//
// Where an answer comes from, in this order:
//   the row        its own `answers`, by the question's exact id as the answer log has it
//   a set          a named group of answers the file declares (`sets`) and the row `uses`
//   the background the answer the background return gave to the same kind of question (the same input template). The
//                  background return is interview-rules' minimal return (every question answered with its closed
//                  answer: no, zero, none, the first option; the other option where that one refuses), walked once per
//                  profile in bank order. It answers only the kinds of question it was itself asked. A question it
//                  never met was opened by the row's own answers, and the row must answer it
// The background never satisfies an expected end: a refusal met on a background answer fails the row, and so does an
// expected value the background supplied.
//
// A row fails when
//   - the walk does not end as `expect` says (another refusal, completion, another value, a `not_asked` question asked)
//   - the walk asks a question neither the row nor the background answers. The failure names the answer that opened
//     the question and says which it is: opened by an answer of the row, the row is incomplete; opened by a background
//     answer or open from the start, the tree asks this filer something the row's author did not expect
//   - an answer of the row is never asked (a stale row), or the interview rejects it
//   - the row names an id that does not exist: a question, a refusal gate, a set
// and the run fails when a set, or an answer of a set, is used by no row's walk, when two rows share an id, or when
// reports/<year>/interview_coverage.md is not what the rows produce (`--write` writes it).
//
//   interview-coverage [--write] [--rows FILE]... [--schema FILE] [--self-test]
//     --rows FILE   check these row files instead of interview/<year>/coverage/*.yaml (the report is then neither
//                   checked nor written)
//     --schema FILE the schema file holding `coverageFile` (default schema/data.schema.json)
import assert from "node:assert/strict";
import { existsSync, readdirSync, readFileSync, writeFileSync } from "node:fs";
import { join, relative, resolve } from "node:path";
import { Ajv2020 } from "ajv/dist/2020.js";
import { parse } from "yaml";
import { CANON_DIR, loadCanonical } from "./canonical.js";
import { templateKey } from "./branches.js";
import { applyAnswer, inputMeta, interviewView, loadInterview, questionTemplate, replay, type Event, type InterviewData } from "./interview.js";
import { bankOrder, minimalAnswers, walk } from "./interview-rules.js";
import { YEAR } from "./year.js";
import type { CanonicalData, Inputs } from "./types.js";

const ROOT = resolve(import.meta.dirname, "../..");
const ROWS_DIR = resolve(ROOT, "interview", String(YEAR), "coverage");
const REPORT = resolve(ROOT, "reports", String(YEAR), "interview_coverage.md");
const SCHEMA = resolve(ROOT, "schema", "data.schema.json");
const BOUND = 800;
const PROFILES = ["full", "ny"] as const;
type Profile = (typeof PROFILES)[number];

/** The end a row expects: exactly one of `asks`, `refused`, `records` and `proceeds`, and optionally `not_asked`. */
export interface Expect {
  /** This question is the interview's next question; the walk ends there. */
  asks?: string;
  /** The return is refused at this gate, on an answer of the row. */
  refused?: string;
  /** Once the row's own answers are given, these inputs hold these values without having been asked. */
  records?: Record<string, unknown>;
  /** The return is completed, and these inputs hold these values, given by the row or recorded, not by the background. */
  proceeds?: Record<string, unknown>;
  /** None of these questions is asked before the walk ends. */
  not_asked?: string[];
}
export interface Row { id: string; design: string; situation: string; replace_when?: string; profile?: Profile; uses?: string[]; answers?: Record<string, unknown>; expect: Expect }
export interface AnswerSet { says: string; answers: Record<string, unknown> }
export interface CoverageFile { tax_year: number; part: string; profile: Profile; sets?: Record<string, AnswerSet>; rows: Row[] }

/** One answer of a walk: the question's number in the walk, its id, the value and where the value came from
 * ("row", "set <name>" or "background"). */
export interface Step { n: number; input: string; value: unknown; from: string }
export type End =
  | { kind: "refused"; gate: string; form: string; remedy: string }
  | { kind: "complete" }
  | { kind: "asks"; input: string }
  | { kind: "answered" }
  | { kind: "unanswered"; input: string; openedBy: Step | null }
  | { kind: "rejected"; input: string; value: unknown; from: string; message: string }
  | { kind: "stuck"; message: string };
export interface RowWalk { steps: Step[]; end: End; inputs: Inputs }

/** The background return of a profile: its answers by input template, and its walk. */
export interface Background { answers: Map<string, unknown>; steps: Step[] }
export interface Ctx { data: CanonicalData; configs: Partial<Record<Profile, InterviewData>>; backgrounds: Partial<Record<Profile, Background>>; conflicts: Record<string, string> }

/** The background return: interview-rules' minimal return with every existence gate closed, walked in bank order. */
export function backgroundOf(data: CanonicalData, config: InterviewData, profile: Profile): Background {
  const w = walk(data, config, minimalAnswers(data, config, profile, null), bankOrder(config), BOUND, () => {});
  if (w.status !== "complete") throw new Error(`the background return of profile ${profile} ends ${w.status}, not complete`);
  const answers = new Map<string, unknown>();
  for (const e of w.events) {
    const t = questionTemplate(e.input);
    if (answers.has(t) && JSON.stringify(answers.get(t)) !== JSON.stringify(e.value)) throw new Error(`the background return of profile ${profile} gives two answers to ${t}`);
    answers.set(t, e.value);
  }
  return { answers, steps: w.events.map((e, i) => ({ n: i + 1, input: e.input, value: e.value, from: "background" })) };
}

function profileCtx(ctx: Ctx, profile: Profile): { config: InterviewData; background: Background } {
  const config = (ctx.configs[profile] ??= loadInterview(profile));
  const background = (ctx.backgrounds[profile] ??= backgroundOf(ctx.data, config, profile));
  return { config, background };
}

export function loadCtx(): Ctx {
  const path = join(CANON_DIR, "conflicts.json");
  const conflicts = existsSync(path) ? (JSON.parse(readFileSync(path, "utf8")) as { conflicts: Record<string, string> }).conflicts : {};
  return { data: loadCanonical(), configs: {}, backgrounds: {}, conflicts };
}

const same = (a: unknown, b: unknown): boolean => JSON.stringify(a) === JSON.stringify(b);

/** The answers a row gives beyond the background: its own, then those of the sets it uses (its own win). */
function givenOf(row: Row, sets: Record<string, AnswerSet>): Map<string, { value: unknown; from: string }> {
  const given = new Map<string, { value: unknown; from: string }>();
  for (const name of row.uses ?? []) for (const [k, value] of Object.entries(sets[name]?.answers ?? {})) given.set(k, { value, from: `set ${name}` });
  for (const [k, value] of Object.entries(row.answers ?? {})) given.set(k, { value, from: "row" });
  return given;
}

/** Walks the built interview as the row's filer: see the head of this file. */
export function walkRow(ctx: Ctx, row: Row, file: Pick<CoverageFile, "profile" | "sets">): RowWalk {
  const { config, background } = profileCtx(ctx, row.profile ?? file.profile);
  const given = givenOf(row, file.sets ?? {});
  const own = Object.keys(row.answers ?? {});
  const events: Event[] = [{ version: 1, tax_year: config.tax_year }];
  const steps: Step[] = [];
  const asked = new Set<string>();
  /** Each input's opener: the last answer given before the input was first reachable (null: reachable from the start). */
  const opener = new Map<string, Step | null>();
  let inputs = replay(config, events);
  let view = interviewView(ctx.data, config, inputs);
  for (;;) {
    const done = (end: End): RowWalk => ({ steps, end, inputs });
    if (steps.length > BOUND) return done({ kind: "stuck", message: "the walk did not end" });
    for (const k of view.reachableInputs) if (!opener.has(k)) opener.set(k, steps.at(-1) ?? null);
    if (row.expect.records && own.every((k) => asked.has(k))) return done({ kind: "answered" });
    if (view.status === "refused") {
      const r = view.refusal as { gate: string; form: string; remedy: string };
      return done({ kind: "refused", gate: r.gate, form: r.form, remedy: r.remedy });
    }
    if (view.status === "complete") return done({ kind: "complete" });
    const key = view.question?.input;
    if (key === undefined) return done({ kind: "stuck", message: "the return is incomplete and the interview has no question" });
    if (key === row.expect.asks) return done({ kind: "asks", input: key });
    const template = questionTemplate(key);
    const answer = given.get(key) ?? (background.answers.has(template) ? { value: background.answers.get(template), from: "background" } : undefined);
    if (!answer) return done({ kind: "unanswered", input: key, openedBy: opener.get(key) ?? null });
    let applied: ReturnType<typeof applyAnswer>;
    try { applied = applyAnswer(ctx.data, config, events, key, answer.value); } catch (e) {
      return done({ kind: "rejected", input: key, value: answer.value, from: answer.from, message: e instanceof Error ? e.message : String(e) });
    }
    events.push(applied.event);
    steps.push({ n: steps.length + 1, input: key, value: answer.value, from: answer.from });
    asked.add(key);
    inputs = applied.inputs;
    view = applied.after;
  }
}

const show = (v: unknown): string => JSON.stringify(v);
const stepText = (s: Step): string => `question ${s.n}, ${s.input} = ${show(s.value)} (${s.from === "row" ? "the row's answer" : s.from === "background" ? "a background answer" : `an answer of ${s.from}`})`;

function endText(end: End): string {
  switch (end.kind) {
    case "refused": return `was refused at ${end.gate} (${end.form})`;
    case "complete": return "completed the return";
    case "asks": return `asked ${end.input}`;
    case "answered": return "gave all the row's answers";
    case "unanswered": return `asked ${end.input}, which has no answer`;
    case "rejected": return `had the answer ${show(end.value)} to ${end.input} rejected: ${end.message}`;
    case "stuck": return end.message;
  }
}

/** The row's failures against its walk; empty when the walk ends as the row says. */
export function judge(row: Row, w: RowWalk): string[] {
  const out: string[] = [];
  const { end, steps, inputs } = w;
  const x = row.expect;
  const last = steps.at(-1);
  const stepOf = new Map(steps.map((s) => [s.input, s]));
  if (end.kind === "unanswered") {
    const by = end.openedBy;
    const template = questionTemplate(end.input);
    const hint = Object.keys(row.answers ?? {}).includes(template) && template !== end.input ? ` The row answers ${template}, which names no entry: use the question's exact id, ${end.input}.` : "";
    const which = by !== null && by.from !== "background"
      ? "The row's answers lead to it, so the row is incomplete: add the answer this situation's filer gives (or, if this filer should not meet the question, the tree is wrong to ask it)."
      : "No answer of the row leads to it directly, so the tree asks this filer something the row's author did not expect (if the question is right for this filer, add the answer to the row).";
    out.push(`the walk asks ${end.input} (after ${steps.length} answers), which the row does not answer and the background return is never asked. ${by === null ? "It is asked from the start." : `It was opened by ${stepText(by)}.`} ${which}${hint}`);
  } else if (end.kind === "rejected") {
    out.push(`the interview rejects the answer ${show(end.value)} to ${end.input} (${end.from === "row" ? "the row's answer" : end.from === "background" ? "a background answer" : `an answer of ${end.from}`}): ${end.message}`);
  } else if (end.kind === "stuck") {
    out.push(end.message);
  } else if (x.asks !== undefined) {
    if (end.kind !== "asks") out.push(`expected the question ${x.asks} to be asked; the walk ${endText(end)} first, after ${steps.length} answers${last ? ` (the last: ${stepText(last)})` : ""}`);
  } else if (x.refused !== undefined) {
    if (end.kind !== "refused") out.push(`expected a refusal at ${x.refused}; the walk ${endText(end)} after ${steps.length} answers`);
    else if (end.gate !== x.refused) out.push(`expected a refusal at ${x.refused}; the walk ${endText(end)} after ${steps.length} answers${last ? ` (the last: ${stepText(last)})` : ""}`);
    else if (last?.from === "background") out.push(`the refusal at ${end.gate} came on a background answer (${stepText(last)}): the background may not bring about a row's end. Give the row the answer its filer gives to ${last.input}`);
  } else if (x.records !== undefined) {
    if (end.kind !== "answered") out.push(`expected the row's answers to be given; the walk ${endText(end)} first`);
    else for (const [k, v] of Object.entries(x.records)) {
      const s = stepOf.get(k);
      if (s) out.push(`expected ${k} to be recorded without being asked; it was asked (${stepText(s)})`);
      else if (!(k in inputs)) out.push(`expected ${k} = ${show(v)} to be recorded; after the row's answers it has no value`);
      else if (!same(inputs[k], v)) out.push(`expected ${k} = ${show(v)} to be recorded; it holds ${show(inputs[k])}`);
    }
  } else if (x.proceeds !== undefined) {
    if (end.kind !== "complete") out.push(`expected the return to be completed; the walk ${endText(end)} after ${steps.length} answers${last ? ` (the last: ${stepText(last)})` : ""}`);
    else for (const [k, v] of Object.entries(x.proceeds)) {
      const s = stepOf.get(k);
      if (!(k in inputs)) out.push(`expected ${k} = ${show(v)} on the completed return; it has no value (the question was never asked)`);
      else if (!same(inputs[k], v)) out.push(`expected ${k} = ${show(v)} on the completed return; it holds ${show(inputs[k])}`);
      else if (s?.from === "background") out.push(`${k} = ${show(v)} was supplied by the background (${stepText(s)}): the background may not supply an expected value. Give the row that answer`);
    }
  }
  for (const k of x.not_asked ?? []) {
    const s = stepOf.get(k);
    if (s) out.push(`expected ${k} not to be asked; it was (${stepText(s)})`);
  }
  // A row's own answer the walk never asked for: reported once the walk has otherwise run its course.
  if (end.kind !== "unanswered" && end.kind !== "rejected" && end.kind !== "stuck") {
    const asked = new Set(steps.map((s) => s.input));
    const templates = new Map(steps.map((s) => [questionTemplate(s.input), s.input]));
    for (const k of Object.keys(row.answers ?? {})) {
      if (asked.has(k)) continue;
      const instance = templates.get(k);
      out.push(`the row's answer to ${k} is never asked before the walk ends (it ${endText(end)} after ${steps.length} answers): a stale answer, or one the tree no longer reaches.${instance && instance !== k ? ` The walk asked ${instance}: a row names the question's exact id.` : ""}`);
    }
  }
  return out;
}

/** The ids a file names that do not exist, by row; a row with any is not walked. */
export function idProblems(ctx: Ctx, file: CoverageFile): Map<string, string[]> {
  const out = new Map<string, string[]>();
  const gates = new Set<string>();
  for (const d of [...ctx.data.forms, ...ctx.data.defs]) for (const l of d.lines) for (const r of l.refuses ?? []) gates.add(r.when);
  const questions = (profile: Profile) => new Set(profileCtx(ctx, profile).config.questions.map((q) => q.input));
  const sets = file.sets ?? {};
  const unknownQuestion = (profile: Profile, key: string): boolean => !questions(profile).has(questionTemplate(key));
  // An input a choice records has no question of its own, so a held value is named by any input of the model.
  const unknownInput = (profile: Profile, key: string): boolean => {
    if (key.startsWith("$")) return unknownQuestion(profile, key);
    try { inputMeta(ctx.data, key); return false; } catch { return true; }
  };
  for (const row of file.rows) {
    const problems: string[] = [];
    const profile = row.profile ?? file.profile;
    for (const name of row.uses ?? []) if (!(name in sets)) problems.push(`uses the set ${name}, which the file does not declare`);
    const named: [string, string][] = [
      ...Object.keys(row.answers ?? {}).map((k) => ["answers", k] as [string, string]),
      ...(row.uses ?? []).flatMap((name) => Object.keys(sets[name]?.answers ?? {}).map((k) => [`the set ${name} answers`, k] as [string, string])),
      ...(row.expect.asks !== undefined ? [["expects to be asked", row.expect.asks] as [string, string]] : []),
      ...(row.expect.not_asked ?? []).map((k) => ["expects not to be asked", k] as [string, string]),
    ];
    const held: [string, string][] = [
      ...Object.keys(row.expect.records ?? {}).map((k) => ["expects recorded", k] as [string, string]),
      ...Object.keys(row.expect.proceeds ?? {}).map((k) => ["expects on the completed return", k] as [string, string]),
    ];
    for (const [what, k] of held) if (unknownInput(profile, k)) problems.push(`${what} ${k}, and the model has no input ${questionTemplate(k)}`);
    for (const [what, k] of named) if (unknownQuestion(profile, k)) problems.push(`${what} ${k}, and the ${profile} interview has no question ${questionTemplate(k)}`);
    if (row.expect.refused !== undefined && !gates.has(templateKey(row.expect.refused))) problems.push(`expects a refusal at ${row.expect.refused}, and no line refuses at a gate ${templateKey(row.expect.refused)}`);
    if (row.expect.asks !== undefined && row.expect.asks in (row.answers ?? {})) problems.push(`answers ${row.expect.asks}, the question it expects the walk to end at`);
    if (row.expect.asks !== undefined && (row.expect.not_asked ?? []).includes(row.expect.asks)) problems.push(`expects ${row.expect.asks} both asked and not asked`);
    if (row.expect.records !== undefined && !Object.keys(row.answers ?? {}).length) problems.push("expects recorded answers but gives no answer of its own for them to follow");
    if (problems.length) out.set(row.id, problems);
  }
  return out;
}

export interface RowResult { file: string; part: string; row: Row; profile: Profile; walk: RowWalk | null; problems: string[] }
export interface Run { results: RowResult[]; problems: string[] }

/** Checks row files already parsed and valid against the schema (`name` is how a file is named in a failure). */
export function checkFiles(ctx: Ctx, files: { name: string; file: CoverageFile }[]): Run {
  const results: RowResult[] = [];
  const problems: string[] = [];
  const seen = new Map<string, string>();
  for (const { name, file } of files) {
    if (file.tax_year !== YEAR) problems.push(`${name}: tax_year ${file.tax_year} is not the year checked, ${YEAR}`);
    const bad = idProblems(ctx, file);
    const setAsked = new Map(Object.keys(file.sets ?? {}).map((n) => [n, new Set<string>()] as [string, Set<string>]));
    const setUsed = new Set<string>();
    for (const row of file.rows) {
      const first = seen.get(row.id);
      if (first !== undefined) problems.push(`${name}: row ${row.id}: the id is also a row of ${first}`);
      seen.set(row.id, name);
      const profile = row.profile ?? file.profile;
      const idp = bad.get(row.id);
      if (idp) { results.push({ file: name, part: file.part, row, profile, walk: null, problems: idp.map((p) => `names an id that does not exist: ${p}`) }); continue; }
      const w = walkRow(ctx, row, file);
      for (const u of row.uses ?? []) setUsed.add(u);
      for (const s of w.steps) if (s.from.startsWith("set ")) setAsked.get(s.from.slice(4))?.add(s.input);
      results.push({ file: name, part: file.part, row, profile, walk: w, problems: judge(row, w) });
    }
    for (const [n, s] of Object.entries(file.sets ?? {})) {
      if (!setUsed.has(n)) { problems.push(`${name}: set ${n}: no row uses it`); continue; }
      for (const k of Object.keys(s.answers)) if (!setAsked.get(n)!.has(k)) problems.push(`${name}: set ${n}: its answer to ${k} is never asked in the walk of any row that uses the set (a stale answer)`);
    }
  }
  return { results, problems };
}

const schemaCache = new Map<string, (v: unknown) => string | null>();
/** The schema problem of a parsed row file, or null. */
export function schemaProblem(value: unknown, schemaPath = SCHEMA): string | null {
  let validate = schemaCache.get(schemaPath);
  if (!validate) {
    const schema = JSON.parse(readFileSync(schemaPath, "utf8")) as { $defs: Record<string, unknown>; $schema: string };
    if (!("coverageFile" in schema.$defs)) throw new Error(`${schemaPath} has no coverageFile definition`);
    const ajv = new Ajv2020({ allErrors: true, strict: false });
    const v = ajv.compile({ $schema: schema.$schema, $defs: schema.$defs, $ref: "#/$defs/coverageFile" });
    validate = (x) => (v(x) ? null : ajv.errorsText(v.errors).slice(0, 600));
    schemaCache.set(schemaPath, validate);
  }
  return validate(value);
}

function readFiles(paths: string[], schemaPath: string, problems: string[]): { name: string; file: CoverageFile }[] {
  const out: { name: string; file: CoverageFile }[] = [];
  for (const p of paths) {
    const name = relative(ROOT, p).startsWith("..") ? p : relative(ROOT, p);
    let value: unknown;
    try { value = parse(readFileSync(p, "utf8")); } catch (e) { problems.push(`${name}: not readable as YAML: ${e instanceof Error ? e.message : String(e)}`); continue; }
    const bad = schemaProblem(value, schemaPath);
    if (bad) { problems.push(`${name}: does not fit the schema (coverageFile): ${bad}`); continue; }
    out.push({ name, file: value as CoverageFile });
  }
  return out;
}

// ---- the report ----

function valueText(ctx: Ctx, profile: Profile, key: string, value: unknown): string {
  if (value === true) return "Yes";
  if (value === false) return "No";
  if (Array.isArray(value)) return value.length ? `the entries ${value.map((v) => `\`${String(v)}\``).join(", ")}` : "none";
  if (typeof value === "number" && !key.startsWith("$")) {
    const type = inputMeta(ctx.data, key).type;
    if (type === "Dollars" || type === "NonNegDollars") return `${value < 0 ? "-" : ""}$${(Math.abs(value) / 100).toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
  }
  if (typeof value === "string") {
    const label = profileCtx(ctx, profile).config.questions.find((q) => q.input === questionTemplate(key))?.value_labels?.[value];
    return label ? `\`${value}\` (${label})` : `\`${value}\``;
  }
  return `\`${show(value)}\``;
}

const cell = (s: string): string => s.replace(/\|/g, "\\|").replace(/\s*\n\s*/g, " ");
const firstLine = (s: string): string => s.split("\n")[0]!.trim();

function promptOf(ctx: Ctx, profile: Profile, key: string): string {
  return firstLine(profileCtx(ctx, profile).config.questions.find((q) => q.input === questionTemplate(key))?.prompt ?? "");
}

/** How a passing row's walk ended, as a sentence for the owner. */
function endSentence(ctx: Ctx, r: RowResult): string {
  const w = r.walk!;
  const x = r.row.expect;
  const not = x.not_asked?.length ? ` Not asked on the way: ${x.not_asked.map((k) => `\`${k}\``).join(", ")}.` : "";
  switch (w.end.kind) {
    case "refused": {
      const conflict = templateKey(w.end.gate) in ctx.conflicts;
      return `${conflict ? "Stopped as conflicting answers" : "Refused"} at \`${w.end.gate}\`: ${w.end.form}. ${w.end.remedy}${not}`;
    }
    case "asks": return `Asked next: \`${w.end.input}\`, “${promptOf(ctx, r.profile, w.end.input)}”${profileCtx(ctx, r.profile).background.answers.has(questionTemplate(w.end.input)) ? " (a question the background return is asked too)" : ""}.${not}`;
    case "answered": return `Recorded without being asked: ${Object.entries(x.records ?? {}).map(([k, v]) => `\`${k}\` = ${valueText(ctx, r.profile, k, v)}`).join(", ")}.${not}`;
    case "complete": return `The return is completed, with ${Object.entries(x.proceeds ?? {}).map(([k, v]) => `\`${k}\` = ${valueText(ctx, r.profile, k, v)}`).join(", ")}.${not}`;
    default: return endText(w.end);
  }
}

/** A walk's path: the row's and sets' answers in the order asked, each with its question number, and the background's
 * answers between them as a count. */
function pathText(ctx: Ctx, r: RowResult): string {
  const parts: string[] = [];
  let run = 0;
  const flush = () => { if (run) parts.push(`(${run} background ${run === 1 ? "answer" : "answers"})`); run = 0; };
  for (const s of r.walk!.steps) {
    if (s.from === "background") { run++; continue; }
    flush();
    parts.push(`${s.n}. \`${s.input}\` = ${valueText(ctx, r.profile, s.input, s.value)}${s.from === "row" ? "" : ` [${s.from}]`}`);
  }
  flush();
  return parts.join(" → ");
}

export function renderReport(ctx: Ctx, run: Run): string {
  const out: string[] = [];
  const rows = run.results;
  const today = rows.filter((r) => r.row.replace_when !== undefined);
  out.push(
    `# Situations the interview is known to handle (${YEAR})`,
    "",
    "Written by `node engine/dist/main.js interview-coverage --write` from the rows in `interview/" + YEAR + "/coverage/`; check-all fails when it is not current.",
    "No model is called. Each row names a situation as the answers a filer in it gives. The check walks the built interview with those answers, in the interview's own order, and the row passes only when the walk ends where the row says.",
    "",
    "How to read a path: the numbered answers are the row's own (or a named set's, marked), with the question's number in the walk. Every other question on the way was answered by the background return (the last section): the answer a filer with nothing to report gives to the same question. The background answers only the kinds of question it is itself asked; a question opened by the row's answers must be answered by the row. A refusal met on a background answer, or an expected value the background supplied, fails the row.",
    "",
    `${rows.length} rows: ${rows.filter((r) => !r.problems.length).length} pass, ${rows.filter((r) => r.problems.length).length} fail.${today.length ? ` ${today.length} of them are written against the interview as it stands before a redesigned part lands, and are marked for replacement.` : ""}`,
    "",
  );
  const parts = [...new Set(rows.map((r) => r.part))];
  for (const part of parts) {
    const mine = rows.filter((r) => r.part === part);
    out.push(`## ${part}`, "", `Rows: \`${mine[0]!.file}\`.`, "", "| Row | Design row | Situation | How the interview ends |", "|---|---|---|---|");
    for (const r of mine) out.push(`| \`${r.row.id}\`${r.row.replace_when !== undefined ? " †" : ""} | ${cell(r.row.design)} | ${cell(r.row.situation)} | ${cell(r.problems.length ? `**FAILS:** ${r.problems.join("; ")}` : endSentence(ctx, r))} |`);
    out.push("");
    if (mine.some((r) => r.row.replace_when !== undefined)) out.push("† Written against the interview as it stands; to be replaced: " + [...new Set(mine.flatMap((r) => (r.row.replace_when !== undefined ? [r.row.replace_when] : [])))].join("; ") + ".", "");
    out.push("Paths:", "");
    for (const r of mine) if (r.walk) out.push(`- \`${r.row.id}\`${r.profile === "full" ? "" : ` (profile ${r.profile})`}: ${pathText(ctx, r)}${r.walk.steps.length ? "" : "(no answer)"}`);
    out.push("");
  }
  for (const profile of PROFILES) {
    const b = ctx.backgrounds[profile];
    if (!b) continue;
    out.push(`## The background return${profile === "full" ? "" : ` (profile ${profile})`}`, "",
      `The ${b.steps.length} questions a filer with nothing to report is asked, in order, and the answer given to each: no, zero, none or the first option (the other option where that one refuses). It is the minimal return \`interview-rules\` checks to completion.`, "",
      "| # | Question | Answer |", "|---|---|---|");
    for (const s of b.steps) out.push(`| ${s.n} | \`${s.input}\` | ${cell(valueText(ctx, profile, s.input, s.value))} |`);
    out.push("");
  }
  return out.join("\n").replace(/\n+$/, "\n");
}

// ---- the command ----

export async function interviewCoverage(args: string[] = []): Promise<number> {
  if (args.includes("--self-test")) return selfTest();
  const option = (name: string): string[] => args.flatMap((a, i) => (a === name && args[i + 1] !== undefined ? [args[i + 1]!] : []));
  const given = option("--rows").map((p) => resolve(p));
  const schemaPath = option("--schema")[0] ?? SCHEMA;
  const own = !given.length;
  const paths = own ? (existsSync(ROWS_DIR) ? readdirSync(ROWS_DIR).filter((f) => f.endsWith(".yaml")).sort().map((f) => join(ROWS_DIR, f)) : []) : given;
  const problems: string[] = [];
  if (!paths.length) problems.push(`no row file in ${relative(ROOT, ROWS_DIR)}`);
  const t0 = performance.now();
  const ctx = loadCtx();
  const run = checkFiles(ctx, readFiles(paths, schemaPath, problems));
  problems.push(...run.problems);
  for (const r of run.results) for (const p of r.problems) problems.push(`${r.file}: row ${r.row.id}: ${p}`);
  const asked = run.results.reduce((a, r) => a + (r.walk?.steps.length ?? 0), 0);
  console.log(`  ${run.results.length} rows of ${paths.length} file(s) walked (${asked} answers, ${run.results.reduce((a, r) => a + (r.walk?.steps.filter((s) => s.from === "background").length ?? 0), 0)} of them the background's), ${((performance.now() - t0) / 1000).toFixed(1)} s`);
  if (own) {
    const text = renderReport(ctx, run);
    if (args.includes("--write")) { writeFileSync(REPORT, text); console.log(`  wrote ${relative(ROOT, REPORT)}`); }
    else if (!existsSync(REPORT) || readFileSync(REPORT, "utf8") !== text) problems.push(`${relative(ROOT, REPORT)} is not what the rows produce; run: node engine/dist/main.js interview-coverage --write`);
  }
  for (const p of problems) console.error(`  ${p}`);
  console.log(`interview-coverage: ${problems.length} problem(s)`);
  return problems.length ? 1 : 0;
}

/** Each kind of failure is found on a planted row, and the clean rows pass. The planted rows are written against the
 * background return's own questions, so they hold whatever the question bank asks beyond them. */
function selfTest(): number {
  // The schema: a well-formed file passes; each malformed one is refused.
  const ok = { tax_year: YEAR, part: "Self-test", profile: "full", rows: [{ id: "a", design: "none", situation: "A filer.", answers: { $person: ["taxpayer"] }, expect: { asks: "f1040.status" } }] };
  assert.equal(schemaProblem(ok), null);
  const broken = (edit: (f: Record<string, unknown> & { rows: Record<string, unknown>[] }) => void): string => { const f = structuredClone(ok) as never as Record<string, unknown> & { rows: Record<string, unknown>[] }; edit(f); return schemaProblem(f) ?? ""; };
  assert.notEqual(broken((f) => { delete f.rows[0]!["situation"]; }), "", "a row without a situation");
  assert.notEqual(broken((f) => { f.rows[0]!["expect"] = {}; }), "", "a row with no expected end");
  assert.notEqual(broken((f) => { f.rows[0]!["expect"] = { asks: "a.b", refused: "c.d" }; }), "", "a row with two expected ends");
  assert.notEqual(broken((f) => { f.rows[0]!["expect"] = { not_asked: ["a.b"] }; }), "", "a row with only not_asked");
  assert.notEqual(broken((f) => { f.rows[0]!["expect"] = { asks: "a.b", told: "x" }; }), "", "an unknown key in expect");
  assert.notEqual(broken((f) => { f.rows[0]!["id"] = "Row 1"; }), "", "an id that is not a plain identifier");
  assert.notEqual(broken((f) => { f["profile"] = "sales"; }), "", "a profile the check does not walk");

  const ctx = loadCtx();
  const { config, background } = profileCtx(ctx, "full");
  const bg = background.steps;
  assert.ok(bg.length > 5, "the background return asks questions");
  // Questions of the background return to plant rows on: a yes/no question whose yes refuses the return at once (the
  // refusing answer and its gate are read off the built interview), and the question asked after it.
  const refusing = bg.map((s, i) => ({ s, i })).filter(({ s }) => s.value === false).map(({ s, i }) => {
    const before: Inputs = Object.fromEntries(bg.slice(0, i).map((b) => [b.input, b.value]));
    const view = interviewView(ctx.data, config, { ...before, [s.input]: true });
    return view.status === "refused" && i + 1 < bg.length ? { input: s.input, next: bg[i + 1]!.input, gate: (view.refusal as { gate: string }).gate } : null;
  }).find((r) => r !== null);
  assert.ok(refusing, "the background return has a yes/no question whose yes refuses the return");
  const { input: Q, next: NEXT, gate: GATE } = refusing!;
  const first = bg[0]!;
  const file = (rows: Row[], sets?: Record<string, AnswerSet>): { name: string; file: CoverageFile }[] => [{ name: "planted.yaml", file: { tax_year: YEAR, part: "Self-test", profile: "full", ...(sets ? { sets } : {}), rows } }];
  const row = (id: string, answers: Record<string, unknown>, expect: Expect, more: Partial<Row> = {}): Row => ({ id, design: "none", situation: "A planted filer.", answers, expect, ...more });
  const problemsOf = (rows: Row[], sets?: Record<string, AnswerSet>): string => { const r = checkFiles(ctx, file(rows, sets)); return [...r.problems, ...r.results.flatMap((x) => x.problems.map((p) => `row ${x.row.id}: ${p}`))].join("\n"); };

  // Clean rows of each end the built interview can come to.
  const clean = [
    row("refuses", { [Q]: true }, { refused: GATE }),
    row("asks", { [Q]: false }, { asks: NEXT }),
    row("proceeds", { [Q]: false }, { proceeds: { [Q]: false } }),
    row("asks-first", {}, { asks: first.input, not_asked: [Q] }),
  ];
  assert.equal(problemsOf(clean), "", "the clean rows pass");
  const cleanRun = checkFiles(ctx, file(clean));
  const refusedWalk = cleanRun.results[0]!.walk!;
  assert.equal(refusedWalk.steps.at(-1)!.input, Q, "the walk ends at the first refusal");
  assert.ok(refusedWalk.steps.slice(0, -1).every((s) => s.from === "background") && refusedWalk.steps.at(-1)!.from === "row", "the answers before the row's are the background's");
  assert.equal(cleanRun.results[2]!.walk!.steps.length, bg.length, "a row that changes nothing walks the background return's questions");
  // A set's answers count as declared answers of the rows that use it.
  assert.equal(problemsOf([row("uses-set", {}, { refused: GATE }, { uses: ["yes"] })], { yes: { says: "The planted yes.", answers: { [Q]: true } } }), "");

  // 1. The walk does not end as expected: another refusal, completion in place of a refusal, another question first.
  assert.match(problemsOf([row("r", { [Q]: true }, { refused: "s3.mfs" })]), new RegExp(`row r: expected a refusal at s3\\.mfs; the walk was refused at ${GATE.replace(/[.[\]$]/g, "\\$&")}`));
  assert.match(problemsOf([row("r", { [Q]: false }, { refused: GATE })]), /row r: expected a refusal at .*; the walk completed the return/);
  assert.match(problemsOf([row("r", { [Q]: true }, { asks: NEXT })]), /row r: expected the question .* to be asked; the walk was refused at /);
  assert.match(problemsOf([row("r", { [Q]: true }, { proceeds: { [Q]: true } })]), /row r: expected the return to be completed; the walk was refused at /);
  assert.match(problemsOf([row("r", { [Q]: false }, { proceeds: { [Q]: true } })]), /row r: expected .* = true on the completed return; it holds false/);
  assert.match(problemsOf([row("r", { [Q]: false }, { asks: NEXT, not_asked: [first.input] })]), /row r: expected .* not to be asked; it was \(question 1,/);

  // 2. The walk asks a question the row gives no answer for. A roster the background leaves empty is given one entry;
  // the entry's questions are asked of this filer alone, and the failure names the answer that opened them.
  const roster = bg.find((s) => s.input.startsWith("$") && Array.isArray(s.value) && s.value.length === 0 && !config.questions.find((q) => q.input === questionTemplate(s.input))?.choices);
  assert.ok(roster, "the background return leaves an open roster empty");
  const opened = problemsOf([row("r", { [roster!.input]: ["planted"] }, { proceeds: { [roster!.input]: ["planted"] } })]);
  assert.match(opened, /row r: the walk asks .* \(after \d+ answers\), which the row does not answer and the background return is never asked\. It was opened by question \d+, .* = \["planted"\] \(the row's answer\)\. The row's answers lead to it, so the row is incomplete/);
  // The same from the other side: a question the background does not answer (planted: its answer is taken away) and
  // no answer of the row opened.
  const without: Ctx = { ...ctx, backgrounds: { full: { ...background, answers: new Map([...background.answers].filter(([t]) => t !== questionTemplate(NEXT))) } } };
  assert.match(checkFiles(without, file([row("r", { [Q]: false }, { proceeds: { [Q]: false } })])).results[0]!.problems.join("\n"), /the walk asks .*, which the row does not answer and the background return is never asked\. .* No answer of the row leads to it directly, so the tree asks this filer something the row's author did not expect/);

  // 3. A row's answer is never asked: the walk ends first, the entry does not exist, or the id is a template.
  assert.match(problemsOf([row("r", { [Q]: true, [NEXT]: bg.find((s) => s.input === NEXT)!.value }, { refused: GATE })]), /row r: the row's answer to .* is never asked before the walk ends \(it was refused at .*: a stale answer/);
  const personal = bg.find((s) => /^person\[taxpayer\]\./.test(s.input))!;
  assert.match(problemsOf([row("r", { [personal.input.replace("[taxpayer]", "[nobody]")]: personal.value }, { asks: Q })]), /row r: the row's answer to person\[nobody\]\..* is never asked/);
  assert.match(problemsOf([row("r", { [questionTemplate(personal.input)]: personal.value }, { proceeds: { [Q]: false }, }), ]), /row r: .*The walk asked person\[taxpayer\]\..*: a row names the question's exact id\./s);

  // 4. A row names an id that does not exist: a question (answered, expected, not expected), a gate, a set.
  assert.match(problemsOf([row("r", { "nosuch.question": true }, { asks: Q })]), /row r: names an id that does not exist: answers nosuch\.question, and the full interview has no question nosuch\.question/);
  assert.match(problemsOf([row("r", {}, { asks: "nosuch.question" })]), /names an id that does not exist: expects to be asked nosuch\.question/);
  assert.match(problemsOf([row("r", {}, { asks: Q, not_asked: ["nosuch.question"] })]), /names an id that does not exist: expects not to be asked nosuch\.question/);
  assert.match(problemsOf([row("r", { [Q]: true }, { refused: "nosuch.gate" })]), /names an id that does not exist: expects a refusal at nosuch\.gate, and no line refuses at a gate nosuch\.gate/);
  assert.match(problemsOf([row("r", {}, { asks: Q }, { uses: ["nosuch"] })]), /names an id that does not exist: uses the set nosuch/);
  assert.match(problemsOf([row("r", { [Q]: false }, { proceeds: { "nosuch.input": 1 } })]), /names an id that does not exist: expects on the completed return nosuch\.input, and the model has no input nosuch\.input/);

  // 5. The background does not satisfy an end. A refusal the background's own answer would bring about: the planted
  // background answers Q yes. An expected value only the background gave.
  const yesCtx: Ctx = { ...ctx, backgrounds: { full: { ...background, answers: new Map([...background.answers, [questionTemplate(Q), true]]) } } };
  const onBackground = checkFiles(yesCtx, file([row("r", { [first.input]: first.value }, { refused: GATE })]));
  assert.match(onBackground.results[0]!.problems.join("\n"), /the refusal at .* came on a background answer \(question \d+, .* = true \(a background answer\)\): the background may not bring about a row's end/);
  assert.match(problemsOf([row("r", { [first.input]: first.value }, { proceeds: { [Q]: false } })]), /= false was supplied by the background .*: the background may not supply an expected value/);

  // 6. An answer the interview rejects: a yes/no question given a number.
  assert.match(problemsOf([row("r", { [Q]: 7 }, { refused: GATE })]), /row r: the interview rejects the answer 7 to /);

  // 7. Recorded answers. An input held without being asked passes (a profile's initial answer stands in here for what
  // a choice records); one that was asked, one with another value and one with no value fail.
  const second = bg[1]!;
  const fixed = structuredClone(config);
  fixed.initial = { [second.input]: second.value };
  const fixedCtx: Ctx = { ...ctx, configs: { full: fixed }, backgrounds: { full: background } };
  const recorded = (expect: Expect) => checkFiles(fixedCtx, file([row("r", { [first.input]: first.value }, expect)])).results[0]!.problems.join("\n");
  assert.equal(recorded({ records: { [second.input]: second.value }, not_asked: [second.input] }), "");
  assert.match(recorded({ records: { [second.input]: "another" } }), /expected .* = "another" to be recorded; it holds /);
  assert.match(recorded({ records: { [Q]: false } }), /expected .* = false to be recorded; after the row's answers it has no value/);
  assert.match(problemsOf([row("r", { [first.input]: first.value, [second.input]: second.value }, { records: { [second.input]: second.value } })]), /expected .* to be recorded without being asked; it was asked \(question 2,/);
  assert.match(problemsOf([row("r", {}, { records: { [second.input]: second.value } })]), /expects recorded answers but gives no answer of its own/);

  // 8. The file as a whole: a repeated row id, a set no row uses, a set answer no walk asks, another year.
  assert.match(problemsOf([clean[0]!, clean[0]!]), /row refuses: the id is also a row of planted\.yaml/);
  assert.match(problemsOf([clean[0]!], { idle: { says: "Nobody.", answers: { [Q]: true } } }), /set idle: no row uses it/);
  assert.match(problemsOf([row("r", { [Q]: true }, { refused: GATE }, { uses: ["late"] })], { late: { says: "Too late.", answers: { [NEXT]: bg.find((s) => s.input === NEXT)!.value } } }), /set late: its answer to .* is never asked in the walk of any row that uses the set/);
  assert.match(checkFiles(ctx, [{ name: "planted.yaml", file: { tax_year: YEAR - 1, part: "Self-test", profile: "full", rows: [clean[0]!] } }]).problems.join("\n"), /tax_year .* is not the year checked/);

  // The report lists each row with its situation and its end, and a failing row as failing.
  const report = renderReport(ctx, checkFiles(ctx, file([...clean, row("stale", { [Q]: true }, { asks: NEXT }, { replace_when: "the planted part lands" })])));
  assert.ok(report.includes("| `refuses` | none | A planted filer. | Refused at `" + GATE + "`") || report.includes("| `refuses` | none | A planted filer. | Stopped as conflicting answers at `" + GATE + "`"), "the report gives a refused row's end");
  assert.ok(report.includes("| `stale` † | none | A planted filer. | **FAILS:**") && report.includes("to be replaced: the planted part lands"), "the report marks a failing row and a row to be replaced");
  assert.ok(report.includes("## The background return") && report.includes(`| 1 | \`${first.input}\` |`), "the report lists the background return");
  console.log(`interview-coverage self-test: passed (schema, 7 malformed files; on the built interview, planted on ${Q} and ${roster!.input}: clean rows of each end; a wrong end, 6 cases; an unanswered question, opened by a row's answer and not; a stale answer, 3 cases; an id that does not exist, 6 cases; an end the background brings about, 2 cases; a rejected answer; recorded answers, 5 cases; a repeated id, an unused set, a stale set answer, another year; the report)`);
  return 0;
}
