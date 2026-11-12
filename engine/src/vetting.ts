// The owner's vetting of the interview's questions: every question the page's profile can ask, one card each, with
// the owner's verdict (thumbs up, thumbs down or none) and note on it. The server (serve.ts) serves the cards at
// `/vet` and saves verdicts through this module; `vetting-report` lists them for whoever acts on them.
//
// A card shows the question as the interview page words it. The wording is the engine's own: `shownAt`
// (interview-words.ts), which applies `shownFor` (spouse-wording.ts), at three sets of answers made by answering
// "who is this return for" as the bank's own choices record it:
//
//   one person       the one-person choice and the filing status single, asked of the taxpayer's entry (the card's main text)
//   joint            the couple's choice (which records married filing jointly), asked of the taxpayer's entry
//   spouse's entry   the couple's choice, asked of the spouse's entry (questions asked of a person or beneath one)
//
// The words are counted by the words tool's functions (`words`, `longestSentence`); a question is long when its
// stored prompt has a sentence of more than LONG_SENTENCE words, as reports/<year>/interview_words.md counts them.
//
// Verdicts are kept in a tracked file, reviews/<year>/owner_vetting/verdicts.json, one record per question id. A
// record holds what was judged (the stored prompt, help, answer type and answers offered) and its digest, so a verdict
// stays tied to the wording it was given on: when the stored wording differs from what a record judged the record is
// stale, and a record whose id the interview no longer asks is an orphan. Neither is ever dropped or applied to other
// wording. The file is written with sorted keys and a fixed layout, through a temporary file renamed into place.
//
//   vetting-report [--write] [--file <verdicts.json>] [--self-test]
//     --write       writes reports/<year>/owner_vetting.md (written on demand; no check requires it to be current)
import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { chmodSync, closeSync, existsSync, fsyncSync, mkdirSync, mkdtempSync, openSync, readFileSync, readdirSync, renameSync, rmSync, unlinkSync, writeFileSync, writeSync } from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join, relative, resolve } from "node:path";
import { loadCanonical } from "./canonical.js";
import { gatesOf, readsOf } from "./gates.js";
import { answerEvent, askOrder, inputMeta, interviewView, loadInterview, offeredValues, questionTemplate, replayState, withheldValues, type AnswerEvent, type InterviewData } from "./interview.js";
import { longestSentence, shownAt, words } from "./interview-words.js";
import { STATUS_INPUT } from "./spouse-wording.js";
import { YEAR } from "./year.js";
import type { CanonicalData, FormDoc, Inputs, Line } from "./types.js";

const ROOT = resolve(import.meta.dirname, "../..");
/** The tracked verdict file of the year, and the report written from it. */
export const VERDICTS_FILE = resolve(ROOT, "reviews", String(YEAR), "owner_vetting", "verdicts.json");
const REPORT = resolve(ROOT, "reports", String(YEAR), "owner_vetting.md");
/** The profile the page asks, which is the profile vetted. */
const PROFILE = "ny";
/** A sentence of more words than this makes a question long. */
export const LONG_SENTENCE = 40;
/** A gate figured from more answers than this is not spelled out on a card. */
const GATE_ANSWERS = 4;
/** The characters of another question's first line a card gives when it names that question. */
const NAMED_PROMPT = 140;
export const NOTE_MAX = 20_000;

// ---- what is judged, and its digest ----

/** One answer offered with a question: the value saved and the label shown. */
export interface Offered { value: unknown; label: string }
/** What a verdict is given on, as the question bank stores it: the prompt (a form line's label where the bank gives
 * no wording of its own), the help, the answer type and the answers offered, in the order shown (an enum's values
 * with their labels, a fixed roster's choices; null where the filer types the answer or it is Yes or No). */
export interface Judged { prompt: string; help: string; type: string; options: Offered[] | null }

type Stored = InterviewData["questions"][number];

export function judgedOf(data: CanonicalData, q: Stored): Judged {
  const meta = inputMeta(data, q.input);
  const options: Offered[] | null =
    meta.type === "Enum" ? offeredValues(meta.values!, q.value_order).map((v) => ({ value: v, label: q.value_labels?.[v] ?? v }))
    : meta.type === "Roster" && q.choices ? q.choices.map((c) => ({ value: c.value, label: c.label }))
    : null;
  return { prompt: q.prompt, help: q.help ?? "", type: meta.type, options };
}

/** A value with every object's keys in order, so its JSON does not depend on how it was built. */
function sorted(value: unknown): unknown {
  if (Array.isArray(value)) return value.map(sorted);
  if (value && typeof value === "object") return Object.fromEntries(Object.keys(value).sort().map((k) => [k, sorted((value as Record<string, unknown>)[k])]));
  return value;
}
/** The file form of a value: keys sorted, two-space indent, one trailing newline. */
export function stableJson(value: unknown): string {
  return JSON.stringify(sorted(value), null, 2) + "\n";
}
/** The digest of what is judged: SHA-256 of its JSON with sorted keys. */
export function digestOf(judged: Judged): string {
  return createHash("sha256").update(JSON.stringify(sorted(judged))).digest("hex");
}

// ---- the verdict file ----

export type Verdict = "up" | "down" | "none";
/** One question's record: the verdict, the note, when either last changed (UTC), and what was judged with its digest. */
export interface VerdictRecord { verdict: Verdict; note: string; changed: string; digest: string; judged: Judged }
export interface VerdictFile { version: 1; tax_year: number; records: Record<string, VerdictRecord> }

const VERDICTS: readonly string[] = ["up", "down", "none"];
function recordProblem(r: unknown): string | null {
  if (!r || typeof r !== "object" || Array.isArray(r)) return "not an object";
  const x = r as Record<string, unknown>;
  if (typeof x["verdict"] !== "string" || !VERDICTS.includes(x["verdict"])) return "verdict is not up, down or none";
  if (typeof x["note"] !== "string") return "note is not text";
  if (typeof x["changed"] !== "string" || !/^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ$/.test(x["changed"])) return "changed is not a UTC time to the second";
  const j = x["judged"] as Record<string, unknown> | null;
  if (!j || typeof j !== "object" || typeof j["prompt"] !== "string" || typeof j["help"] !== "string" || typeof j["type"] !== "string"
    || !(j["options"] === null || (Array.isArray(j["options"]) && j["options"].every((o) => o && typeof o === "object" && typeof (o as Offered).label === "string" && "value" in o)))) return "judged is not {prompt, help, type, options}";
  if (x["digest"] !== digestOf(j as unknown as Judged)) return "digest is not the digest of judged";
  return null;
}

/** The verdict file at `path`; an absent file is one with no records. Throws, naming the record, when the file is not
 * a verdict file of this tax year or a record's digest is not that of what it says was judged. */
export function loadVerdicts(path: string, taxYear: number): VerdictFile {
  if (!existsSync(path)) return { version: 1, tax_year: taxYear, records: {} };
  let file: VerdictFile;
  try { file = JSON.parse(readFileSync(path, "utf8")) as VerdictFile; }
  catch (e) { throw new Error(`${path}: not JSON (${(e as Error).message})`); }
  if (!file || typeof file !== "object" || file.version !== 1 || file.tax_year !== taxYear || !file.records || typeof file.records !== "object" || Array.isArray(file.records))
    throw new Error(`${path}: not a verdict file of tax year ${taxYear} ({version: 1, tax_year, records})`);
  for (const [id, r] of Object.entries(file.records)) {
    const problem = recordProblem(r);
    if (problem) throw new Error(`${path}: record ${id}: ${problem}`);
  }
  return file;
}

/** Writes the file whole or not at all: the text goes to a temporary file beside it, is flushed, and is renamed over
 * it. A failure leaves the file as it was and removes the temporary file. */
export function writeVerdicts(path: string, file: VerdictFile): void {
  mkdirSync(dirname(path), { recursive: true });
  const tmp = `${path}.${process.pid}.tmp`;
  try {
    const fd = openSync(tmp, "w", 0o644);
    try { writeSync(fd, stableJson(file)); fsyncSync(fd); } finally { closeSync(fd); }
    renameSync(tmp, path);
  } catch (e) {
    try { unlinkSync(tmp); } catch { /* it was never created */ }
    throw e;
  }
}

/** A time as records keep it: UTC, to the second. */
export function stamp(now: Date = new Date()): string {
  return now.toISOString().slice(0, 19) + "Z";
}

/** A change to one question's record, applied in place; returns the record, or null when none is left.
 *  - `verdict` given: the verdict is on `current`, the wording shown now, so the record is tied to it.
 *  - only `note` given: the note changes and the record stays tied to what it judged, so a stale verdict stays
 *    stale until a verdict is given on the wording shown now; a new record is tied to `current`.
 * A record with no verdict and an empty note is removed. */
export function applyChange(file: VerdictFile, id: string, current: Judged, change: { verdict?: Verdict; note?: string }, now: string): VerdictRecord | null {
  const old = file.records[id];
  const note = change.note ?? old?.note ?? "";
  const verdict = change.verdict ?? old?.verdict ?? "none";
  if (verdict === "none" && note === "") { delete file.records[id]; return null; }
  const judged = change.verdict !== undefined || !old ? current : old.judged;
  const record: VerdictRecord = { verdict, note, changed: now, digest: digestOf(judged), judged: structuredClone(judged) };
  file.records[id] = record;
  return record;
}

// ---- the cards ----

/** A wording of a question other than the card's main one, where it differs: the prompt and help that differ. */
export interface Variant { who: string; prompt: string | null; help: string | null }
/** An answer offered, as a card lists it; `withheld` when a one-person return is not offered it. */
export interface CardOption { label: string; value: unknown; withheld?: true }
/** An earlier question a gate is figured from. */
export interface GateQuestion { id: string; prompt: string }
export interface Card {
  id: string;
  /** The digest of what a verdict on this card judges (`judgedOf`). */
  digest: string;
  /** The question and help as a one-person return is shown them, and the other wordings that differ. */
  prompt: string;
  help: string;
  variants: Variant[];
  /** The prompt and help as stored, where the main wording differs from them. */
  stored: { prompt: string; help: string } | null;
  /** The sort of answer in plain words, the answers offered, and for a list the filer builds, what an entry is. */
  answer: { type: string; text: string; options: CardOption[] | null; entry: string | null };
  /** The form or topic the question belongs to: the title of its form and, where the line is printed with a number
   * or a name, that. */
  topic: string;
  /** How often it is asked: once per return, per person or per entry of a list. */
  scope: string;
  /** What the engine can say of when it is asked. */
  gate: { text: string; questions: GateQuestion[] };
  /** Words of the main prompt and help, and of the stored prompt's longest sentence. */
  words: { prompt: number; help: number; sentence: number };
  long: boolean;
}

const firstLine = (text: string): string => text.split("\n")[0]!;

/** The answers of a return after "who is this return for" is answered with the bank's choice of `people` entries, as
 * `answerEvent` records it; a one-person return's filing status is single. Null when the bank has no such choice. */
function returnOf(config: InterviewData, people: 1 | 2): Inputs | null {
  const header = { version: 1, tax_year: config.tax_year };
  const blank = replayState(config, [header]);
  const choice = config.questions.find((q) => q.input === "$person")?.choices?.find((c) => c.value.length === people);
  if (!choice) return null;
  const event: AnswerEvent = answerEvent(config, blank, "$person", choice.value, choice.labels);
  const inputs = replayState(config, [header, event]).inputs;
  return STATUS_INPUT in inputs ? inputs : { ...inputs, [STATUS_INPUT]: "single" };
}

/** The key a question's input has in a return: its template with an entry key for each collection it lies in
 * (`person[taxpayer].w2[entry].box1`), the person's entry being `person`; and the collections, outermost first. */
function keyOf(forms: Map<string, FormDoc>, formId: string, id: string, person: string): { key: string; chain: FormDoc[] } {
  const chain: FormDoc[] = [];
  const roster = id.startsWith("$");
  for (let f = forms.get(roster ? forms.get(formId)?.collection?.parent ?? "" : formId); f?.collection; f = forms.get(f.collection.parent ?? "")) chain.unshift(f);
  const path = chain.map((f) => `${f.id}[${f.id === "person" ? person : f.collection!.implicit ?? "entry"}]`).join(".");
  const key = roster ? (path ? `${id}@${path}` : id) : path ? `${path}.${id.slice(formId.length + 1)}` : id;
  if (questionTemplate(key) !== id) throw new Error(`${id}: the key ${key} is not a key of this question`);
  return { key, chain };
}

/** How often a question is asked, from the collections its input lies in. `listName` names a list. */
function scopeOf(chain: FormDoc[], listName: (collection: string) => string): string {
  const inner = chain.at(-1);
  if (!inner) return "Once per return";
  // A collection with one implicit entry per parent entry is asked as often as its parent.
  if (inner.collection!.implicit) return scopeOf(chain.slice(0, -1), listName);
  if (inner.id === "person") return "Once per person on the return";
  const parent = chain.at(-2);
  const within = !parent ? "" : parent.id === "person" ? "; each person on the return has their own list" : `; a list within each entry of ${listName(parent.id)}`;
  return `Once per entry of the list ${listName(inner.id)}${within}`;
}

/** The sort of answer a type takes, in plain words. */
function answerText(type: string, fixed: boolean): string {
  switch (type) {
    case "Bool": return "Yes or No";
    case "NonNegDollars": return "A dollar amount, zero or more";
    case "Dollars": return "A dollar amount, which may be negative";
    case "Count": return "A whole number";
    case "Date": return "A date";
    case "Text": return "Text";
    case "Enum": return "One choice from a list";
    case "Roster": return fixed ? "One choice from a list" : "A list the filer builds, naming each entry";
    default: return `A value of the type ${type}`;
  }
}

/** For each gated input, what its gate is figured from: the bank's questions reached from the gate's guards through
 * figured lines, or null where that cannot be read off the expressions (a sum over a list's entries or a definition
 * instance on the way, whose reads are not line references) or is more than GATE_ANSWERS questions. */
function gateQuestions(data: CanonicalData, asked: Set<string>): Map<string, { line: string; questions: string[] | null }> {
  const lines = new Map<string, Line>([...data.forms, ...data.defs].flatMap((d) => d.lines.map((l) => [l.id, l] as const)));
  const opaque = (l: Line) => /"op":"sum_over"|"def":/.test(JSON.stringify(l.expr));
  const out = new Map<string, { line: string; questions: string[] | null }>();
  for (const g of gatesOf(data)) {
    const found = new Set<string>(), seen = new Set<string>();
    let whole = true;
    const visit = (ref: string): void => {
      if (seen.has(ref)) return;
      seen.add(ref);
      const l = lines.get(ref);
      if (!l) return; // a constant of a test, not a line
      if (l.expr.op === "input") { if (asked.has(ref)) found.add(ref); else whole = false; return; }
      if (opaque(l)) { whole = false; return; }
      for (const r of readsOf(l)) visit(r);
    };
    for (const r of g.guardRefs) visit(r);
    out.set(g.input, { line: g.line, questions: whole && found.size > 0 && found.size <= GATE_ANSWERS ? [...found].sort() : null });
  }
  return out;
}

/** Every question of the profile as a card, in the interview's asking order (`askOrder`). */
export function vettingCards(data: CanonicalData, config: InterviewData): Card[] {
  const forms = new Map(data.forms.map((f) => [f.id, f] as const));
  const formOfLine = new Map(data.forms.flatMap((f) => f.lines.map((l) => [l.id, f] as const)));
  const lineById = new Map(data.forms.flatMap((f) => f.lines.map((l) => [l.id, l] as const)));
  const asked = new Set(config.questions.map((q) => q.input));
  const gates = gateQuestions(data, asked);
  // A bank with no choice of who the return is for is worded as stored, from the profile's initial answers.
  const initial = replayState(config, [{ version: 1, tax_year: config.tax_year }]).inputs;
  const one = returnOf(config, 1) ?? initial, two = returnOf(config, 2);
  // The questions open before anything else is answered, and once only who the return is for (and, for one person,
  // the filing status) is: by template, for each of the two returns.
  const open = (inputs: Inputs) => new Set(interviewView(data, config, inputs).pending.map((q) => questionTemplate(q.input)));
  const blank = open(initial);
  const openOne = open(one), openTwo = two ? open(two) : new Set<string>();
  // And on the one-person return with one entry in every list a filer builds and nothing else answered: a question of
  // a list's entry that is pending there is asked of an entry as soon as it is listed.
  const listed: Inputs = { ...one };
  for (const f of data.forms) if (f.collection && !f.collection.implicit && f.id !== "person") listed[keyOf(forms, f.id, `$${f.id}`, "taxpayer").key] = ["entry"];
  const openListed = open(listed);
  const formOf = (id: string): FormDoc => {
    const form = forms.get(id.startsWith("$") ? id.slice(1) : formOfLine.get(id)?.id ?? "");
    if (!form) throw new Error(`${id}: no form holds this input`);
    return form;
  };
  // Another question as a card names it: the first line of its prompt as a one-person return is shown it, cut at a word.
  const promptOf = (id: string): string => {
    const line = firstLine(shownAt(data, config, one, keyOf(forms, formOf(id).id, id, "taxpayer").key).prompt);
    return line.length <= NAMED_PROMPT ? line : line.slice(0, line.lastIndexOf(" ", NAMED_PROMPT)) + " \u2026";
  };
  // A list as a card names it: its roster question's id and, where the profile asks it, that question.
  const listName = (collection: string): string => (asked.has(`$${collection}`) ? `$${collection} (\u201c${promptOf(`$${collection}`)}\u201d)` : `$${collection}`);

  return [...config.questions].sort(askOrder).map((q): Card => {
    const roster = q.input.startsWith("$");
    const form = formOf(q.input);
    const { key, chain } = keyOf(forms, form.id, q.input, "taxpayer");
    const judged = judgedOf(data, q);
    const main = shownAt(data, config, one, key);
    const variants: Variant[] = [];
    const differing = (who: string, s: { prompt: string; help: string }) => {
      const v: Variant = { who, prompt: s.prompt === main.prompt ? null : s.prompt, help: s.help === main.help ? null : s.help };
      if (v.prompt !== null || v.help !== null) variants.push(v);
    };
    if (two) {
      if (chain.some((f) => f.id === "person")) differing("Asked about the spouse, on a joint return", shownAt(data, config, two, keyOf(forms, form.id, q.input, "spouse").key));
      differing(chain.some((f) => f.id === "person") ? "Asked about the filer, on a joint return" : "On a joint return", shownAt(data, config, two, key));
    }
    const withheld = judged.type === "Enum" ? withheldValues(config, one, key) : [];
    const options: CardOption[] | null =
      judged.type === "Bool" ? null
      : judged.options ? judged.options.map((o) => ({ label: o.label, value: o.value, ...(typeof o.value === "string" && withheld.includes(o.value) ? { withheld: true as const } : {}) }))
      : null;
    const line = lineById.get(q.input);
    const gate = gates.get(q.input);
    const gateInfo: Card["gate"] =
      gate?.questions ? { text: `Asked only after an earlier answer: its gate (${gate.line}) is figured from`, questions: gate.questions.map((id) => ({ id, prompt: promptOf(id) })) }
      : gate ? { text: `Asked only in some cases (its gate is ${gate.line})`, questions: [] }
      : blank.has(q.input) ? { text: "Open from the start: it is pending before anything is answered", questions: [] }
      : openOne.has(q.input) || openTwo.has(q.input) ? { text: `Open once who the return is for is answered${openOne.has(q.input) && openTwo.has(q.input) ? "" : openOne.has(q.input) ? " (one person; not on a joint return)" : " (a joint return; not for one person)"}`, questions: [] }
      : !roster && chain.some((f) => f.id !== "person" && !f.collection!.implicit) && openListed.has(q.input) ? { text: "Asked of an entry as soon as it is listed: it is pending when the lists have entries and nothing else is answered", questions: [] }
      : { text: "Asked only in some cases", questions: [] };
    const sentence = longestSentence(q.prompt);
    return {
      id: q.input, digest: digestOf(judged), prompt: main.prompt, help: main.help, variants,
      stored: main.prompt === q.prompt && main.help === (q.help ?? "") ? null : { prompt: q.prompt, help: q.help ?? "" },
      answer: { type: judged.type, text: answerText(judged.type, !!q.choices), options, entry: roster && !q.choices ? form.title : null },
      topic: !line?.printed || line.printed.startsWith("(") ? form.title : `${form.title}, ${/^\d/.test(line.printed) ? "line " : ""}${line.printed}`,
      scope: scopeOf(chain, listName),
      gate: gateInfo,
      words: { prompt: words(main.prompt), help: words(main.help), sentence },
      long: sentence > LONG_SENTENCE,
    };
  });
}

// ---- cards with their records ----

export interface VettedCard extends Card { record: VerdictRecord | null; stale: boolean }
export interface VettingState {
  questions: VettedCard[];
  /** The records whose question the interview no longer asks, by id. */
  orphans: { id: string; record: VerdictRecord }[];
}

/** Each card with its record, stale when the record judged other wording than the card's; and the orphans. */
export function vettingState(cards: Card[], file: VerdictFile): VettingState {
  const ids = new Set(cards.map((c) => c.id));
  return {
    questions: cards.map((c) => {
      const record = file.records[c.id] ?? null;
      return { ...c, record, stale: record !== null && record.digest !== c.digest };
    }),
    orphans: Object.keys(file.records).filter((id) => !ids.has(id)).sort().map((id) => ({ id, record: file.records[id]! })),
  };
}

/** The counts of a progress line: verdicts on the wording shown now, stale records, questions with no record, and
 * the questions skipped (without a verdict on today's wording, before the last question that has one). */
export function vettingCounts(state: VettingState): { total: number; up: number; down: number; stale: number; noted: number; skipped: number; orphans: number } {
  const judged = (q: VettedCard) => q.record !== null && !q.stale && q.record.verdict !== "none";
  const last = state.questions.findLastIndex(judged);
  return {
    total: state.questions.length,
    up: state.questions.filter((q) => judged(q) && q.record!.verdict === "up").length,
    down: state.questions.filter((q) => judged(q) && q.record!.verdict === "down").length,
    stale: state.questions.filter((q) => q.stale).length,
    noted: state.questions.filter((q) => q.record?.note).length,
    skipped: state.questions.slice(0, Math.max(0, last)).filter((q) => !judged(q)).length,
    orphans: state.orphans.length,
  };
}

// ---- the report ----

const quote = (text: string): string[] => text.split("\n").map((l) => (l ? `> ${l}` : ">"));
function judgedBlock(j: Judged): string[] {
  const answers = j.options ? `${j.type}: ${j.options.map((o) => `“${o.label}”`).join("; ")}` : j.type;
  return ["Question judged:", "", ...quote(j.prompt), "", ...(j.help ? ["Help judged:", "", ...quote(j.help), ""] : ["No help.", ""]), `Answer: ${answers}`, ""];
}
function entry(id: string, r: VerdictRecord, extra: string[] = []): string[] {
  return [`### \`${id}\``, "", `Verdict: ${r.verdict === "none" ? "none" : `thumbs ${r.verdict}`}, last changed ${r.changed}.`, "",
    ...(r.note ? ["Note:", "", ...quote(r.note), ""] : ["No note.", ""]), ...extra, ...judgedBlock(r.judged)];
}

/** The report for whoever acts on the verdicts: the counts, the thumbs-down questions with their notes, the notes on
 * thumbs-up questions and on questions with no verdict, then the stale records and the orphans; each with its id and
 * the wording judged. Questions are in asking order, orphans by id. */
export function renderVettingReport(state: VettingState, from: string): string {
  const c = vettingCounts(state);
  const current = state.questions.filter((q) => q.record && !q.stale);
  const section = (title: string, lede: string, entries: string[][]): string[] =>
    [`## ${title}`, "", lede, "", ...(entries.length ? entries.flat() : ["None.", ""])];
  const differs = (q: VettedCard): string => {
    const now = { prompt: q.stored?.prompt ?? q.prompt, help: q.stored?.help ?? q.help }, was = q.record!.judged;
    const parts = [now.prompt !== was.prompt ? "the question" : "", now.help !== was.help ? "the help" : "", q.answer.type !== was.type ? "the answer type" : ""].filter(Boolean);
    return `Today's wording differs in ${parts.length ? parts.join(", ") : "the answers offered"}.`;
  };
  return [
    "# Owner vetting of the interview's questions",
    "",
    `Written by \`node engine/dist/main.js vetting-report --write\` (engine/src/vetting.ts) from \`${from}\`, the verdicts the owner`,
    "gave on the vetting page (`/vet` of `serve`; interview/README.md, \"Vetting the questions\"). It is written on demand and is as current",
    "as its last writing. Each entry gives the wording the verdict was given on, as the question bank stored it.",
    "",
    "## Counts",
    "",
    `- Questions the interview can ask: ${c.total}`,
    `- Thumbs up: ${c.up}`,
    `- Thumbs down: ${c.down}`,
    `- Without a verdict on today's wording: ${c.total - c.up - c.down}`,
    `- Questions with a note: ${c.noted}`,
    `- Stale records (given on earlier wording): ${c.stale}`,
    `- Records of questions no longer in the interview: ${c.orphans}`,
    "",
    ...section("Thumbs down", "Each question marked thumbs down on today's wording.", current.filter((q) => q.record!.verdict === "down").map((q) => entry(q.id, q.record!))),
    ...section("Notes on thumbs-up questions", "Each question marked thumbs up that has a note.", current.filter((q) => q.record!.verdict === "up" && q.record!.note).map((q) => entry(q.id, q.record!))),
    ...section("Notes without a verdict", "Each question with a note and no verdict.", current.filter((q) => q.record!.verdict === "none").map((q) => entry(q.id, q.record!))),
    ...section("Stale records", "The question's wording has changed since the verdict or note was given; it is not a verdict on today's wording.", state.questions.filter((q) => q.stale).map((q) => entry(q.id, q.record!, [differs(q), ""]))),
    ...section("Questions no longer in the interview", "Records whose question id the interview no longer asks.", state.orphans.map((o) => entry(o.id, o.record))),
  ].join("\n").replace(/\n+$/, "\n");
}

export function vettingReport(args: string[] = []): number {
  if (args.includes("--self-test")) return selfTest();
  const at = args.indexOf("--file");
  const path = at < 0 ? VERDICTS_FILE : resolve(args[at + 1] ?? "");
  const config = loadInterview(PROFILE);
  const state = vettingState(vettingCards(loadCanonical(), config), loadVerdicts(path, config.tax_year));
  const from = relative(ROOT, path);
  const text = renderVettingReport(state, from.startsWith("..") ? path : from);
  if (args.includes("--write")) { mkdirSync(dirname(REPORT), { recursive: true }); writeFileSync(REPORT, text); console.log(`  wrote ${REPORT}`); } else console.log(text);
  const c = vettingCounts(state);
  console.log(`vetting-report: ${c.total} questions; ${c.up} up, ${c.down} down, ${c.stale} stale, ${c.orphans} no longer in the interview`);
  return 0;
}

// ---- self-test ----

/** The digest, the file form, the record rules, staleness and orphans, the atomic write and the report on planted
 * cases; and the cards of the built bank: one per question, in asking order, each key a key of its question. */
function selfTest(): number {
  let checks = 0;
  const ok = (cond: unknown, message: string) => { assert.ok(cond, message); checks++; };
  const judged: Judged = { prompt: "Do you have a cat?", help: "Any cat.", type: "Enum", options: [{ value: "a", label: "A" }, { value: "b", label: "B" }] };
  const d = digestOf(judged);
  ok(/^[0-9a-f]{64}$/.test(d), "a digest is a SHA-256");
  ok(digestOf({ options: structuredClone(judged.options), type: "Enum", help: "Any cat.", prompt: "Do you have a cat?" }) === d, "the digest does not depend on key order");
  const changes: [string, Judged][] = [
    ["the prompt", { ...judged, prompt: "Do you have a cat? " }], ["the help", { ...judged, help: "" }], ["the type", { ...judged, type: "Bool" }],
    ["an option's label", { ...judged, options: [{ value: "a", label: "A" }, { value: "b", label: "Bee" }] }],
    ["an option's value", { ...judged, options: [{ value: "a", label: "A" }, { value: "c", label: "B" }] }],
    ["the options' order", { ...judged, options: [judged.options![1]!, judged.options![0]!] }], ["no options", { ...judged, options: null }],
  ];
  for (const [what, j] of changes) ok(digestOf(j) !== d, `changing ${what} changes the digest`);
  ok(stableJson({ b: 1, a: { d: [{ z: 1, y: 2 }], c: null } }) === '{\n  "a": {\n    "c": null,\n    "d": [\n      {\n        "y": 2,\n        "z": 1\n      }\n    ]\n  },\n  "b": 1\n}\n', "the file form has sorted keys, a two-space indent and a trailing newline");

  // The record rules.
  const file: VerdictFile = { version: 1, tax_year: 1999, records: {} };
  const t1 = stamp(new Date(Date.UTC(1999, 0, 2, 3, 4, 5, 678))), t2 = "1999-01-03T00:00:00Z";
  ok(t1 === "1999-01-02T03:04:05Z", "a time is kept in UTC to the second");
  ok(applyChange(file, "q.a", judged, { verdict: "none" }, t1) === null && !("q.a" in file.records), "no verdict and no note leaves no record");
  const up = applyChange(file, "q.a", judged, { verdict: "up" }, t1)!;
  ok(up.verdict === "up" && up.note === "" && up.changed === t1 && up.digest === d && isSame(up.judged, judged), "a verdict records what was judged and its digest");
  const noted = applyChange(file, "q.a", judged, { note: "why" }, t2)!;
  ok(noted.verdict === "up" && noted.note === "why" && noted.changed === t2, "a note keeps the verdict");
  ok(applyChange(file, "q.a", judged, { verdict: "down" }, t2)!.note === "why", "a changed verdict keeps the note");
  const reworded: Judged = { ...judged, prompt: "Do you own a cat?" };
  const stillStale = applyChange(file, "q.a", reworded, { note: "why, again" }, t2)!;
  ok(stillStale.digest === d && stillStale.verdict === "down" && stillStale.note === "why, again", "a note alone leaves a record tied to the wording its verdict was given on");
  ok(applyChange(file, "q.a", reworded, { verdict: "down" }, t2)!.digest === digestOf(reworded), "a verdict ties the record to the wording shown now");
  ok(applyChange(file, "q.a", reworded, { verdict: "none" }, t2)!.verdict === "none" && file.records["q.a"]!.note === "why, again", "a cleared verdict keeps a record that has a note");
  ok(applyChange(file, "q.a", reworded, { note: "" }, t2) === null && Object.keys(file.records).length === 0, "and clearing the note too removes the record");
  ok(applyChange(file, "q.b", judged, { note: "only a note" }, t1)!.verdict === "none", "a note without a verdict is a record");

  // Stale and orphaned records, the counts and the report.
  const card = (id: string, j: Judged): Card => ({ id, digest: digestOf(j), prompt: j.prompt, help: j.help, variants: [], stored: null,
    answer: { type: j.type, text: "", options: null, entry: null }, topic: "", scope: "", gate: { text: "", questions: [] }, words: { prompt: 0, help: 0, sentence: 0 }, long: false });
  const cards = ["q.a", "q.b", "q.c", "q.d", "q.e"].map((id) => card(id, { ...judged, prompt: `${id}?` }));
  const planted: VerdictFile = { version: 1, tax_year: 1999, records: {} };
  applyChange(planted, "q.a", { ...judged, prompt: "q.a?" }, { verdict: "up", note: "fine\nreally" }, t1);
  applyChange(planted, "q.b", { ...judged, prompt: "q.b, as it was?" }, { verdict: "down", note: "old wording" }, t1);
  applyChange(planted, "q.d", { ...judged, prompt: "q.d?" }, { verdict: "down", note: "unanswerable" }, t2);
  applyChange(planted, "q.gone", judged, { verdict: "down" }, t1);
  const state = vettingState(cards, planted);
  ok(isSame(state.questions.map((q) => [q.id, q.record?.verdict ?? null, q.stale]), [["q.a", "up", false], ["q.b", "down", true], ["q.c", null, false], ["q.d", "down", false], ["q.e", null, false]]),
    "a record that judged other wording is stale; one that judged this wording is not");
  ok(isSame(state.orphans.map((o) => o.id), ["q.gone"]), "a record of an id that is not asked is an orphan");
  ok(isSame(vettingCounts(state), { total: 5, up: 1, down: 1, stale: 1, noted: 3, skipped: 2, orphans: 1 }), `a stale verdict counts as neither up nor down, and the questions passed over are skipped: ${JSON.stringify(vettingCounts(state))}`);
  const report = renderVettingReport(state, "verdicts.json");
  const part = (title: string) => report.slice(report.indexOf(`## ${title}\n`)).split(/\n## /)[0]!;
  ok(report.endsWith("\n") && !report.endsWith("\n\n"), "the report ends with one newline");
  ok(/`q\.d`[\s\S]*> unanswerable[\s\S]*> q\.d\?/.test(part("Thumbs down")) && !part("Thumbs down").includes("q.b"), "thumbs down lists the question with its note and the wording judged, and no stale record");
  ok(/`q\.a`[\s\S]*> fine\n> really/.test(part("Notes on thumbs-up questions")), "a thumbs-up note is listed, each line quoted");
  ok(/`q\.b`[\s\S]*differs in the question[\s\S]*> q\.b, as it was\?/.test(part("Stale records")), "a stale record is listed with the wording it judged and what differs");
  ok(part("Questions no longer in the interview").includes("`q.gone`") && part("Notes without a verdict").includes("None."), "an orphan is listed; an empty section says so");

  // The file: absent, written, read back, refused when malformed; a failed write leaves it as it was.
  const tmp = mkdtempSync(join(tmpdir(), "vetting-self-test-"));
  try {
    const path = join(tmp, "deep", "verdicts.json");
    ok(isSame(loadVerdicts(path, 1999), { version: 1, tax_year: 1999, records: {} }), "an absent file has no records");
    writeVerdicts(path, planted);
    const text = readFileSync(path, "utf8");
    ok(text === stableJson(planted) && isSame(loadVerdicts(path, 1999), planted), "the file is written in its stable form and read back");
    ok(isSame(readdirSync(dirname(path)), ["verdicts.json"]), "no temporary file is left beside it");
    writeVerdicts(path, planted);
    ok(readFileSync(path, "utf8") === text, "writing the same records writes the same bytes");
    assert.throws(() => loadVerdicts(path, 2000), /not a verdict file of tax year 2000/); checks++;
    chmodSync(dirname(path), 0o500);
    try {
      assert.throws(() => writeVerdicts(path, { ...planted, records: {} })); checks++;
      ok(readFileSync(path, "utf8") === text && isSame(readdirSync(dirname(path)), ["verdicts.json"]), "a failed write leaves the file whole and no temporary file");
    } finally { chmodSync(dirname(path), 0o700); }
    const edited = structuredClone(planted);
    edited.records["q.a"]!.judged.prompt = "edited by hand";
    writeFileSync(path, stableJson(edited));
    assert.throws(() => loadVerdicts(path, 1999), /record q\.a: digest is not the digest of judged/); checks++;
    writeFileSync(path, "{ truncated");
    assert.throws(() => loadVerdicts(path, 1999), /not JSON/); checks++;
  } finally { rmSync(tmp, { recursive: true, force: true }); }

  // The built bank: every question has one card, in asking order, worded by the engine for each of the three returns.
  const data = loadCanonical(), config = loadInterview(PROFILE);
  const built = vettingCards(data, config);
  ok(built.length === config.questions.length && new Set(built.map((c) => c.id)).size === built.length, "one card per question of the profile");
  ok(isSame(built.map((c) => c.id), [...config.questions].sort(askOrder).map((q) => q.input)), "the cards are in asking order");
  ok(built.filter((c) => c.long).length === config.questions.filter((q) => longestSentence(q.prompt) > LONG_SENTENCE).length, "a long card is a question the words report counts as long");
  ok(built.every((c) => !c.answer.text.startsWith("A value of the type")), "every answer type has plain words");
  const by = (id: string) => built.find((c) => c.id === id)!;
  ok(by("$person").answer.options!.length === 2 && by("$person").answer.text === "One choice from a list" && by("$person").scope === "Once per return", "who the return is for is one choice of two, asked once");
  const status = by(STATUS_INPUT);
  ok(status.answer.options!.some((o) => o.value === "mfj" && o.withheld) && status.answer.options!.filter((o) => o.withheld).length === 1, "the filing statuses are all listed, married filing jointly marked as not offered to one person");
  const blind = by("person.blind");
  ok(!blind.prompt.startsWith("For this person") && !blind.prompt.startsWith("About") && blind.scope === "Once per person on the return", `a question asked of a person has no frame on a one-person return: ${blind.prompt.slice(0, 60)}`);
  ok(blind.variants.some((v) => v.prompt?.startsWith("About your spouse \u2014 ")) && blind.variants.some((v) => v.prompt?.startsWith("About you \u2014 ")), "and its spouse's-entry and joint wordings are given");
  ok(blind.stored?.prompt.startsWith("For this person"), "with the stored wording, which differs");
  const w2 = by("$w2");
  ok(w2.answer.text.startsWith("A list the filer builds") && w2.answer.entry === data.forms.find((f) => f.id === "w2")!.title && w2.scope === "Once per person on the return", "a list the filer builds says what an entry is");
  ok(by("w2.box1").scope.startsWith("Once per entry of the list $w2 (") && by("w2.box1").scope.endsWith("each person on the return has their own list"), `a question of a list's entry says so: ${by("w2.box1").scope}`);
  const gated = built.filter((c) => c.gate.questions.length > 0);
  ok(gated.length > 0 && gated.every((c) => c.gate.questions.every((g) => g.id !== c.id && by(g.id) !== undefined)), "a named gate question is another question of the profile");
  console.log(`vetting self-test: ${checks} checks passed; ${built.length} cards, ${built.filter((c) => c.long).length} long, ${gated.length} with their gate's questions named`);
  return 0;
}

function isSame(a: unknown, b: unknown): boolean {
  try { assert.deepStrictEqual(a, b); return true; } catch { return false; }
}
