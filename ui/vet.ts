// The vetting page: every question the interview can ask, one at a time, with the owner's verdict (thumbs up or
// down) and note on each. A client of the server's vetting routes (engine/src/serve.ts): the cards, their wording,
// counts and records all come from the server (engine/src/vetting.ts), and every change is saved as it is made. What
// the page shows as a verdict or a saved note is what the server last confirmed; an unsaved note is marked as such.

import { api, button, el, longText } from "./text.js";

type Verdict = "up" | "down" | "none";
interface Offered { value: unknown; label: string }
interface Judged { prompt: string; help: string; type: string; options: Offered[] | null }
interface VerdictRecord { verdict: Verdict; note: string; changed: string; digest: string; judged: Judged }
interface Variant { who: string; prompt: string | null; help: string | null }
interface Question {
  id: string; digest: string; prompt: string; help: string; variants: Variant[]; stored: { prompt: string; help: string } | null;
  answer: { type: string; text: string; options: { label: string; value: unknown; withheld?: true }[] | null; entry: string | null };
  topic: string; scope: string; gate: { text: string; questions: { id: string; prompt: string }[] };
  words: { prompt: number; help: number; sentence: number }; long: boolean;
  record: VerdictRecord | null; stale: boolean;
}
interface Counts { total: number; up: number; down: number; stale: number; noted: number; skipped: number; orphans: number }
interface Listing { questions: Question[]; orphans: { id: string; record: VerdictRecord }[]; counts: Counts; file: string }
interface Saved { id: string; record: VerdictRecord | null; stale: boolean; counts: Counts }
type Filter = "all" | "unjudged" | "down" | "noted" | "long" | "stale";

const $ = <T extends HTMLElement>(id: string) => document.getElementById(id) as T;
let questions: Question[] = [];
let counts: Counts | null = null;
let file = "";
let at = 0;
let filter: Filter = "all";
/** Notes typed and not yet confirmed saved, by question id. */
const drafts = new Map<string, string>();
/** The saves in flight or waiting, one after another, so the file sees the changes in the order they were made. */
let queue: Promise<void> = Promise.resolve();
let noteTimer: number | undefined;
const NOTE_PAUSE = 700;

/** A verdict on the wording shown now: a stale record's verdict was given on other wording. */
const verdictOf = (q: Question): Verdict => (q.record && !q.stale ? q.record.verdict : "none");
const noteOf = (q: Question): string => drafts.get(q.id) ?? q.record?.note ?? "";
const MATCH: Record<Filter, (q: Question) => boolean> = {
  all: () => true,
  unjudged: (q) => verdictOf(q) === "none",
  down: (q) => verdictOf(q) === "down",
  noted: (q) => noteOf(q) !== "",
  long: (q) => q.long,
  stale: (q) => q.stale,
};
const localTime = (iso: string): string => new Date(iso).toLocaleString();

// ---- saving ----

/** The save indicator. A failure stays until a later save succeeds; it never reads as saved. */
function saveState(state: "idle" | "unsaved" | "saving" | "saved" | "failed", text: string, retry?: () => void): void {
  const line = $("save-state");
  line.dataset.state = state;
  line.replaceChildren(text, ...(retry ? [" ", button("Try again", { class: "link", id: "save-retry" }, retry)] : []));
}

/** Saves a change to a question: its verdict, its note, or both. The page's record of the question changes only when
 * the server confirms the save. */
function save(q: Question, change: { verdict?: Verdict; note?: string }): Promise<void> {
  saveState("saving", `Saving ${q.id}…`);
  const run = async () => {
    try {
      const r = await api<Saved>("POST", "/api/vetting", { id: q.id, digest: q.digest, ...change });
      q.record = r.record;
      q.stale = r.stale;
      counts = r.counts;
      if (change.note !== undefined && drafts.get(q.id) === change.note) drafts.delete(q.id);
      saveState("saved", `Saved ${q.id} at ${new Date().toLocaleTimeString()} in ${file}`);
    } catch (e) {
      saveState("failed", `NOT SAVED: ${q.id}: ${(e as Error).message}`, () => { void save(q, change).then(render); });
    }
  };
  queue = queue.then(run);
  return queue;
}

/** Saves the note being typed, if it differs from the saved one. */
function flushNote(): Promise<void> {
  window.clearTimeout(noteTimer);
  const q = questions[at];
  const draft = q ? drafts.get(q.id) : undefined;
  if (!q || draft === undefined) return queue;
  if (draft === (q.record?.note ?? "")) { drafts.delete(q.id); return queue; }
  return save(q, { note: draft }).then(renderStatus);
}

function setVerdict(verdict: Verdict): void {
  const q = questions[at];
  if (!q) return;
  window.clearTimeout(noteTimer);
  const draft = drafts.get(q.id);
  void save(q, { verdict, ...(draft !== undefined ? { note: draft } : {}) }).then(render);
}

// ---- moving ----

function show(index: number): void {
  if (index < 0 || index >= questions.length) return;
  void flushNote();
  at = index;
  history.replaceState(null, "", `#${encodeURIComponent(questions[at]!.id)}`);
  render();
  window.scrollTo(0, 0);
}
function step(by: 1 | -1): void {
  for (let i = at + by; i >= 0 && i < questions.length; i += by) if (MATCH[filter](questions[i]!)) return show(i);
  $("filter-count").textContent = `${matching()} match; none ${by > 0 ? "after" : "before"} this one`;
}
const matching = (): number => questions.filter(MATCH[filter]).length;
function firstUnjudged(): void {
  const i = questions.findIndex(MATCH.unjudged);
  if (i >= 0) show(i); else $("filter-count").textContent = "Every question has a verdict";
}
/** Goes to the question with this id, or the one question whose id contains it. */
function jump(text: string): boolean {
  const wanted = text.trim();
  let i = questions.findIndex((q) => q.id === wanted);
  if (i < 0 && wanted) {
    const found = questions.map((q, n) => (q.id.includes(wanted) ? n : -1)).filter((n) => n >= 0);
    if (found.length === 1) i = found[0]!;
  }
  if (i < 0) return false;
  show(i);
  return true;
}

// ---- the card ----

function part(title: string, id: string, ...children: (Node | string | null)[]): HTMLElement {
  return el("section", { class: "part", id }, el("h2", {}, title), ...children);
}
function variantBlocks(q: Question, pick: (v: Variant) => string | null, what: string): HTMLElement[] {
  return q.variants.filter((v) => pick(v) !== null).map((v, i) =>
    el("div", { class: "variant" }, el("h3", {}, v.who), longText(pick(v)!, "variant-text", `${what}-variant-${i}`, what, false)));
}
function recordLine(r: VerdictRecord): string {
  return `${r.verdict === "none" ? "No verdict" : `Thumbs ${r.verdict}`}${r.note ? `, with the note “${r.note}”` : ""} (${localTime(r.changed)})`;
}
function judgedDetails(j: Judged, summary: string): HTMLElement {
  return el("details", { class: "stored" }, el("summary", {}, summary),
    el("h3", {}, "Question"), el("p", { class: "as-stored" }, j.prompt),
    el("h3", {}, "Help"), el("p", { class: "as-stored" }, j.help || "(none)"),
    j.options ? el("h3", {}, "Answers offered") : null, j.options ? el("p", { class: "as-stored" }, j.options.map((o) => o.label).join("\n")) : null);
}

function renderStatus(): void {
  const c = counts;
  if (!c) return;
  const line = $("progress");
  line.textContent = `${at + 1} of ${c.total}; ${c.up} up, ${c.down} down, ${c.skipped} skipped${c.stale ? `, ${c.stale} stale` : ""}`;
  line.title = "Skipped: without a verdict on today's wording, and earlier in the order than the last question that has one.";
  $("filter-count").textContent = filter === "all" ? "" : `${matching()} match`;
  const q = questions[at];
  if (q && drafts.has(q.id) && $("save-state").dataset.state !== "failed" && $("save-state").dataset.state !== "saving") saveState("unsaved", "Note not saved yet…");
}

function render(): void {
  renderStatus();
  const q = questions[at];
  const card = $("card");
  if (!q) { card.replaceChildren(el("p", { class: "lede" }, "The interview has no questions.")); return; }
  const verdict = verdictOf(q);
  const tags = [q.long ? "long" : "", q.stale ? "stale" : "", MATCH[filter](q) ? "" : "not in the filter"].filter(Boolean);
  const stale = q.stale && q.record ? el("div", { class: "stale", id: "stale" },
    el("p", {}, el("strong", {}, "STALE. "), "The wording has changed since this was given, so it is not a verdict on what is shown now: ", recordLine(q.record), ". Give a verdict to judge today's wording."),
    judgedDetails(q.record.judged, "The wording that was judged")) : null;

  const options = q.answer.options
    ? el("ol", { class: "options", id: "answer-options" }, ...q.answer.options.map((o) => el("li", {}, o.label, o.withheld ? el("span", { class: "aside" }, " (not offered on a one-person return)") : null)))
    : null;
  const idLine = el("dd", { class: "qid-line", id: "question-id" },
    el("span", { class: "qid" }, el("code", { class: "qid-key" }, q.id)),
    button("Copy", { class: "quiet qid-copy", id: "question-id-copy", "aria-label": "Copy the question id" }, () => {
      void navigator.clipboard.writeText(q.id).then(() => { const b = $("question-id-copy"); b.textContent = "Copied"; setTimeout(() => { b.textContent = "Copy"; }, 1500); }, () => showError("Could not copy the id; select it instead."));
    }));
  const gate = el("dd", { id: "gate" }, q.gate.text, ...(q.gate.questions.length ? [":", el("ul", { class: "gate-questions" },
    ...q.gate.questions.map((g) => el("li", {}, button(g.id, { class: "link", "data-goto": g.id }, () => { jump(g.id); }), ` — ${g.prompt}`)))] : []));

  const note = el("textarea", { id: "note", rows: "3", spellcheck: "true", "aria-label": "Notes on this question", placeholder: "Notes (n)" }) as HTMLTextAreaElement;
  note.value = noteOf(q);
  note.addEventListener("input", () => {
    if (note.value === (q.record?.note ?? "")) drafts.delete(q.id); else drafts.set(q.id, note.value);
    saveState("unsaved", "Note not saved yet…");
    window.clearTimeout(noteTimer);
    noteTimer = window.setTimeout(() => void flushNote(), NOTE_PAUSE);
  });
  note.addEventListener("blur", () => void flushNote());
  const verdictButton = (v: "up" | "down", key: string) =>
    button(`Thumbs ${v} (${key})`, { id: `verdict-${v}`, class: `verdict ${v}${verdict === v ? " chosen" : ""}`, "aria-pressed": String(verdict === v) }, () => setVerdict(v));

  card.replaceChildren(el("article", { class: "vet-question", "data-id": q.id },
    el("p", { class: "position" }, `Question ${at + 1} of ${questions.length}`, ...tags.map((t) => el("span", { class: `tag ${t.split(" ")[0]}` }, t))),
    stale,
    el("div", { class: "vet-columns" },
      el("div", { class: "vet-main" },
        part("Question", "question-part", longText(q.prompt, "prompt-text", "question-text", "question", false), ...variantBlocks(q, (v) => v.prompt, "question")),
        part("Help", "help-part", q.help ? longText(q.help, "help-text", "help-text", "explanation", false) : el("p", { class: "none" }, "No help text."), ...variantBlocks(q, (v) => v.help, "explanation")),
        part("Answer", "answer-part", el("p", { id: "answer-text" }, q.answer.text), options,
          q.answer.entry ? el("p", { id: "answer-entry" }, `An entry is one of: ${q.answer.entry}`) : null)),
      part("Context", "context-part", el("dl", {},
        el("dt", {}, "Id"), idLine,
        el("dt", {}, "Belongs to"), el("dd", { id: "topic" }, q.topic),
        el("dt", {}, "Asked"), el("dd", { id: "scope" }, q.scope),
        el("dt", {}, "When"), gate,
        el("dt", {}, "Words"), el("dd", { id: "words" }, `question ${q.words.prompt}, help ${q.words.help}; longest sentence of the stored question ${q.words.sentence}${q.long ? " (long: over 40)" : ""}`)),
        q.stored ? judgedDetails({ prompt: q.stored.prompt, help: q.stored.help, type: q.answer.type, options: null }, "As stored in the question bank, before it is worded for the return") : null))),
    el("div", { class: "controls", id: "controls" },
      el("div", { class: "verdicts", role: "group", "aria-label": "Verdict" }, verdictButton("up", "u"), verdictButton("down", "d"),
        button("Clear (x)", { id: "verdict-clear", class: "quiet" }, () => setVerdict("none"))),
      note,
      el("div", { class: "moves" }, button("Previous (k)", { id: "prev" }, () => step(-1)), button("Next (j)", { id: "next", class: "primary" }, () => step(1)))));
}

function renderOrphans(orphans: Listing["orphans"]): void {
  const box = $("orphans");
  box.hidden = orphans.length === 0;
  box.replaceChildren(el("h2", {}, `Questions no longer in the interview (${orphans.length})`),
    el("p", { class: "lede" }, "Their verdicts and notes are kept in the file."),
    el("ul", {}, ...orphans.map((o) => el("li", { "data-id": o.id }, el("code", { class: "qid-key" }, o.id), ` — ${recordLine(o.record)}`, judgedDetails(o.record.judged, "The wording that was judged")))));
}

function showError(message: string | null): void {
  const e = $("error");
  e.hidden = message === null;
  e.textContent = message ?? "";
}

// ---- keys ----

function onKey(e: KeyboardEvent): void {
  if (e.metaKey || e.ctrlKey || e.altKey) return;
  const target = e.target as HTMLElement;
  if (target.matches("input, textarea, select")) {
    if (e.key === "Escape") target.blur();
    return;
  }
  const act: Record<string, () => void> = {
    u: () => setVerdict("up"), d: () => setVerdict("down"), x: () => setVerdict("none"),
    j: () => step(1), ArrowRight: () => step(1), k: () => step(-1), ArrowLeft: () => step(-1),
    n: () => $("note").focus(), f: firstUnjudged, g: () => $("jump-id").focus(),
  };
  const run = act[e.key];
  if (!run) return;
  e.preventDefault();
  run();
}

document.addEventListener("DOMContentLoaded", () => {
  void (async () => {
    try {
      const listing = await api<Listing>("GET", "/api/vetting");
      questions = listing.questions;
      counts = listing.counts;
      file = listing.file;
      $("ids").replaceChildren(...questions.map((q) => el("option", { value: q.id })));
      renderOrphans(listing.orphans);
      const wanted = decodeURIComponent(location.hash.slice(1));
      const start = wanted ? questions.findIndex((q) => q.id === wanted) : questions.findIndex(MATCH.unjudged);
      at = Math.max(0, start);
      saveState("idle", `Verdicts are saved in ${file}`);
      render();
    } catch (e) { showError((e as Error).message); }
  })();
  $<HTMLSelectElement>("filter").addEventListener("change", (e) => {
    filter = (e.target as HTMLSelectElement).value as Filter;
    const q = questions[at];
    if (q && !MATCH[filter](q)) {
      const next = questions.findIndex((x, i) => i > at && MATCH[filter](x));
      const first = next >= 0 ? next : questions.findIndex(MATCH[filter]);
      if (first >= 0) return show(first);
    }
    render();
  });
  $("first-unjudged").addEventListener("click", firstUnjudged);
  $("jump").addEventListener("submit", (e) => {
    e.preventDefault();
    const box = $<HTMLInputElement>("jump-id");
    if (jump(box.value)) { box.value = ""; box.blur(); showError(null); } else showError(`No question, or more than one, matches “${box.value.trim()}”.`);
  });
  document.addEventListener("keydown", onKey);
  window.addEventListener("hashchange", () => { jump(decodeURIComponent(location.hash.slice(1))); });
  window.addEventListener("beforeunload", (e) => { if (drafts.size > 0) e.preventDefault(); });
});
