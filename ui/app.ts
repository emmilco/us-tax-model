// The page of the web UI: a client of the server's JSON API (engine/src/serve.ts). It computes nothing about the
// return: every value, status, refusal and question comes from the engine. The current question is the page's centre,
// with its source beside it; the answered list, the values sheets with their derivations, and the scope and notices
// are views one tab away; a refusal's details open in a dialog from the status line.

type Cite = { doc: string; locator: string; revision?: string; quote?: string };
type Value =
  | { kind: "money"; cents: number }
  | { kind: "count"; value: number }
  | { kind: "bool"; value: boolean }
  | { kind: "enum"; value: string }
  | { kind: "rate"; num: number; den: number }
  | { kind: "refusal"; gate: string; form: string; remedy: string; cite: Cite }
  | { kind: "unknown"; reason: string; input?: string };
interface Derivation { value: Value; op: string; cite: Cite | null; operands: { ref: string; value: Value }[]; guardsNotTaken: { guard: string; value: Value }[]; notes: string[] }
interface Choice { label: string; value: string[]; labels: Record<string, string> }
interface FormRef { designation: string; id: string; title?: string; purpose?: { text: string; doc: string; page: number } }
interface Question { input: string; prompt: string; help: string; cite: Cite; helpRequested?: boolean; type: string; values?: string[]; choices?: Choice[]; value?: unknown; forms?: FormRef[] }
interface SheetLine { key: string; printed: string; label: string; value: Value; status: string; shown: boolean; notes: string[] }
interface Section { doc: string; title: string; entry: string | null; lines: SheetLine[] }
/** A refusal whose gate is a consistency check: answers that contradict each other, not an unsupported case. */
interface Conflict { gate: string; explanation: string; answers: Question[]; figures: { line: string; printed: string; label: string; value: Value }[] }
interface State {
  name: string; status: "incomplete" | "complete" | "refused"; refusal: (Value & { kind: "refusal" }) | null; refusalFinal: boolean;
  conflicts: Conflict[];
  pending: Question[]; answered: Question[]; scope: string; notices: string; standingNotices: string[];
  values: Record<string, Derivation>; sheets: { federal: Section[]; newYork: Section[] }; changed: string[];
  entryLabels: Record<string, string>;
}
interface Listing { returns: string[]; scope: string; notices: string; standingNotices: string[]; docTitles: Record<string, string>; docDesignations: Record<string, string> }
type View = "question" | "answered" | "return" | "about";

const KEY = /^[a-zA-Z0-9_-]+$/;
let state: State | null = null;
let reopened: string | null = null; // an answered question reopened for correction, or a pending one chosen
let view: View = "question";
let sheetTab: "federal" | "newYork" = "federal";
let trail: string[] = []; // the derivations opened, most recent last
let lineIndex = new Map<string, { line: SheetLine; section: Section }>();
let lastSaved: { prompt: string; answer: string; changed: number } | null = null;

const $ = <T extends HTMLElement>(id: string) => document.getElementById(id) as T;
function el(tag: string, attrs: Record<string, string> = {}, ...children: (Node | string | null | undefined)[]): HTMLElement {
  const e = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) {
    if (k === "class") e.className = v; else e.setAttribute(k, v);
  }
  for (const c of children) if (c !== null && c !== undefined) e.append(c);
  return e;
}
function button(label: string | Node, attrs: Record<string, string> = {}, onclick?: () => void): HTMLButtonElement {
  const b = el("button", { type: "button", ...attrs }, label) as HTMLButtonElement;
  if (onclick) b.onclick = onclick;
  return b;
}

/** Structured text (the build-checked subset of engine/src/text.ts: one-line paragraphs separated by blank lines, a
 * heading, a line ending in ":", directly above a list, "- " bullets and "  - " nested bullets) as its blocks: <p>,
 * and <h4> or <ul> for a list and its heading. Every piece of text is a text node, never markup. Plain text (no line
 * break) is one <p>. */
function textBlocks(text: string): HTMLElement[] {
  const blocks: HTMLElement[] = [];
  for (const chunk of text.split("\n\n")) {
    const lines = chunk.split("\n");
    const head = lines[0]!.startsWith("- ") ? null : lines.shift()!;
    if (lines.length === 0) { blocks.push(el("p", {}, head ?? "")); continue; }
    const list = el("ul");
    let item: HTMLElement | null = null;
    for (const line of lines) {
      if (line.startsWith("  - ") && item) {
        const sub = item.querySelector(":scope > ul") ?? item.appendChild(el("ul"));
        sub.append(el("li", {}, line.slice(4)));
      } else list.append(item = el("li", {}, line.replace(/^- /, "")));
    }
    // A heading stays with its list, so a fold never separates them.
    blocks.push(head === null ? list : el("div", { class: "text-list" }, el("h4", {}, head), list));
  }
  return blocks;
}
/** A label as HTML: plain text is one `tag` element, as always; structured text is `tag` (a <p> becomes a <div>)
 * holding its blocks. */
function richText(tag: string, attrs: Record<string, string>, text: string): HTMLElement {
  if (!text.includes("\n")) return el(tag, attrs, text);
  return el(tag === "p" ? "div" : tag, { ...attrs, class: `${attrs.class ?? ""} structured`.trim() }, ...textBlocks(text));
}
/** The first line of a question: how a structured question is named in a link. */
const firstLine = (text: string): string => text.split("\n")[0]!;

function fmtMoney(cents: number): string {
  const sign = cents < 0 ? "-" : "";
  const abs = Math.abs(cents);
  const d = Math.floor(abs / 100).toLocaleString("en-US");
  const rem = abs % 100;
  return rem === 0 ? `${sign}$${d}` : `${sign}$${d}.${String(rem).padStart(2, "0")}`;
}
function fmtValue(v: Value): string {
  switch (v.kind) {
    case "money": return fmtMoney(v.cents);
    case "count": return String(v.value);
    case "bool": return v.value ? "Yes" : "No";
    case "enum": return v.value;
    case "rate": return `${v.num}/${v.den}`;
    case "refusal": return `Refused: ${v.form}`;
    case "unknown": return "Unknown";
  }
}
function fmtAnswer(q: Question, value: unknown): string {
  if (value === null) return "help requested";
  if (q.type === "Dollars" || q.type === "NonNegDollars") return fmtMoney(value as number);
  if (q.type === "Bool") return value ? "Yes" : "No";
  if (q.type === "Roster") {
    const keys = value as string[];
    const choice = q.choices?.find((c) => c.value.length === keys.length && c.value.every((k, i) => k === keys[i]));
    if (choice) return choice.label;
    return keys.length ? keys.map((k) => entryLabel(rosterEntryPath(q.input, k)) ?? k).join(", ") : "none";
  }
  return String(value);
}
function plural(n: number, one: string, many = one + "s"): string { return `${n} ${n === 1 ? one : many}`; }

// ---- sources ----
// A citation names a document by its id (`i1040gi`) and a locator, which carries the page, line and the quoted
// passages. The page shows the document's designation and printed title (from the source catalogs, sent with the
// listing), every reference of the locator one per item, and the quoted words in ink.

let docTitles: Record<string, string> = {};
let docDesignations: Record<string, string> = {};
/** A document's name: "<designation> — <title>", the title alone when it has no designation or already contains
 * it, the id when the catalogs give no title. */
function docTitle(id: string): string {
  const title = docTitles[id], designation = docDesignations[id];
  if (!title) return id;
  return designation && !title.includes(designation) ? `${designation} — ${title}` : title;
}
function citeText(c: Cite | null): string {
  return c ? `${docTitle(c.doc)}, ${c.locator}` : "";
}
/** Splits a locator at the `; ` between its references, never inside a quoted passage or parentheses. */
function references(locator: string): string[] {
  const out: string[] = [];
  let depth = 0, quoted = false, start = 0;
  for (let i = 0; i < locator.length; i++) {
    const ch = locator[i]!;
    if (ch === '"') quoted = !quoted;
    else if (ch === "“") quoted = true;
    else if (ch === "”") quoted = false;
    else if (!quoted && ch === "(") depth++;
    else if (!quoted && ch === ")") depth = Math.max(0, depth - 1);
    else if (!quoted && depth === 0 && ch === ";" && locator[i + 1] === " ") { out.push(locator.slice(start, i)); start = i + 2; }
  }
  out.push(locator.slice(start));
  return out.filter((r) => r.trim() !== "");
}
/** A reference with its quoted passages set apart: the quoted words, marks included, in a `.quote` span. */
function referenceNode(ref: string): HTMLElement {
  const li = el("li");
  const re = /"[^"]*"|“[^”]*”/g;
  let at = 0;
  for (const m of ref.matchAll(re)) {
    if (m.index! > at) li.append(ref.slice(at, m.index));
    li.append(el("span", { class: "quote" }, m[0]));
    at = m.index! + m[0].length;
  }
  if (at < ref.length) li.append(ref.slice(at));
  return li;
}
function sourceBlock(c: Cite, inputKey: string): HTMLElement {
  return el("aside", { class: "source", "aria-labelledby": "source-heading" },
    el("h2", { id: "source-heading", class: "source-label" }, "Source"),
    el("p", { class: "doc" }, docTitle(c.doc)),
    c.quote ? el("blockquote", {}, c.quote) : null,
    el("ol", { class: "refs", id: "source-refs" }, ...references(c.locator).map(referenceNode)),
    el("p", { class: "meta" }, `${c.doc}${c.revision ? `, revision ${c.revision}` : ""}`),
    el("p", { class: "meta key", title: "The input this question answers" }, displayKey(inputKey)));
}

/** The forms a question names (found by the server in its prompt and help): each one's designation and printed
 * title, and the catalog's quoted statement of what it is for with that statement's source. More than two are shown
 * one line each, each expandable. A purpose's "•" items are shown as a list; the words are the source's. A purpose
 * quoted from the form itself (its recipient instructions) names its source by designation alone. */
function formsBlock(forms: FormRef[]): HTMLElement | null {
  if (!forms.length) return null;
  const open = forms.length <= 2;
  const items = forms.map((f) => {
    const name = f.title && !f.title.includes(f.designation) ? `${f.designation} — ${f.title}` : f.title ?? f.designation;
    if (!f.purpose) return el("li", { class: "form-gloss bare" }, el("span", { class: "form-name" }, name));
    const [lead, ...points] = f.purpose.text.split(/\s+•\s+/);
    const quote = el("blockquote", { class: "quote" }, el("p", {}, `“${lead!.replace(/^•\s*/, "")}${points.length ? "" : "”"}`),
      points.length ? el("ul", {}, ...points.map((t, i) => el("li", {}, i === points.length - 1 ? `${t}”` : t))) : null);
    const details = el("details", open ? { open: "" } : {},
      el("summary", {}, el("span", { class: "form-name" }, name)),
      quote,
      el("p", { class: "meta" }, `${f.purpose.doc === f.id ? f.designation : docTitle(f.purpose.doc)}, p. ${f.purpose.page}`));
    return el("li", { class: "form-gloss" }, details);
  });
  return el("section", { class: "forms-mentioned", "aria-labelledby": "forms-heading" },
    el("h3", { id: "forms-heading", class: "source-label" }, "Forms mentioned"),
    el("ul", { class: "form-glosses" }, ...items));
}

// ---- long text ----
// Question text is reviewed form data and is shown word for word, always in full. A long text is broken into
// paragraphs at sentence ends; a very long explanation shows its opening and an explicit control for the rest.

const ABBREV = /(?:\b(?:e\.g|i\.e|etc|p|pp|No|Nos|U\.S|St|vs|Inc|Corp|Co|Jr|Sr|Mr|Ms|Dr|sec|Sec|Pub|Rev|Proc|Reg|Regs|ch|art|cl|par|para|approx|v)\.)$/;
function sentences(text: string): string[] {
  const out: string[] = [];
  let start = 0;
  const re = /[.?!]["”’)]?\s+(?=["“(]?[A-Z0-9])/g;
  for (const m of text.matchAll(re)) {
    const end = m.index! + m[0].trimEnd().length;
    if (ABBREV.test(text.slice(start, m.index! + 1))) continue;
    out.push(text.slice(start, end));
    start = m.index! + m[0].length;
  }
  out.push(text.slice(start));
  return out.filter((s) => s !== "");
}
function paragraphs(text: string, target = 420): string[] {
  const out: string[] = [];
  let cur = "";
  for (const s of sentences(text)) {
    if (cur && cur.length + s.length > target) { out.push(cur); cur = s; } else cur = cur ? `${cur} ${s}` : s;
  }
  if (cur) out.push(cur);
  return out;
}
const LONG = 900;
const OPENING = 520;
/** A text as paragraphs (structured text as its blocks); with `fold`, past LONG characters, the opening paragraphs or
 * blocks and a control that shows the rest. */
function longText(text: string, cls: string, id: string, what: string, fold: boolean): HTMLElement {
  const box = el("div", { class: cls });
  const rest = el("div", { class: "rest", id: `${id}-rest`, hidden: "" });
  let shown = 0;
  if (text.includes("\n")) {
    box.classList.add("structured");
    const blocks = textBlocks(text);
    if (!fold || text.length <= LONG) { box.append(...blocks); return box; }
    blocks.forEach((b, i) => {
      const n = (b.textContent ?? "").length;
      if (i === 0 || shown + n <= OPENING) { box.append(b); shown += n; } else rest.append(b);
    });
  } else {
    const paras = paragraphs(text);
    if (!fold || text.length <= LONG) { box.append(...paras.map((p) => el("p", {}, p))); return box; }
    paras.forEach((p, i) => {
      if (i === 0 && p.length > LONG) {
        // One sentence longer than the limit: its opening words, then the remainder in the expandable part.
        const cut = p.lastIndexOf(" ", OPENING);
        box.append(el("p", {}, p.slice(0, cut), el("span", { class: "continues", "aria-hidden": "true" }, " …")));
        rest.append(el("p", { class: "continued" }, p.slice(cut + 1)));
        shown = OPENING;
      } else if (i === 0 || shown + p.length <= OPENING) { box.append(el("p", {}, p)); shown += p.length; }
      else rest.append(el("p", {}, p));
    });
  }
  if (!rest.childElementCount) return box;
  const remaining = text.length - shown;
  const label = `Read the rest of the ${what} (about ${(Math.max(1, Math.round(remaining / 100)) * 100).toLocaleString("en-US")} more characters)`;
  const toggle = button(label, { class: "expander", "aria-expanded": "false", "aria-controls": `${id}-rest` });
  toggle.onclick = () => {
    const open = rest.hidden === true;
    rest.hidden = !open;
    box.querySelector(".continues")?.toggleAttribute("hidden", open);
    toggle.setAttribute("aria-expanded", String(open));
    toggle.textContent = open ? `Show less of the ${what}` : label;
  };
  box.append(rest, toggle);
  return box;
}

// ---- entry labels ----
// Entry keys (`person[taxpayer].w2[acme_corp]`) are the engine's; the page shows the labels typed for them.

const SEGMENT = /([a-zA-Z0-9_]+)\[([a-zA-Z0-9_-]+)\]/g;
/** The entry path a roster's entry `key` has: `$w2@person[taxpayer]`, `acme` -> `person[taxpayer].w2[acme]`. */
function rosterEntryPath(roster: string, key: string): string {
  const [coll, parent] = roster.slice(1).split("@") as [string, string | undefined];
  return `${parent ? parent + "." : ""}${coll}[${key}]`;
}
function entryLabel(path: string): string | undefined { return state?.entryLabels[path]; }
/** The entries an input key or entry path lies in, as labels: `person[taxpayer].w2[acme].box1` -> "You › Acme Corp". */
function entryContext(key: string): string {
  const parts: string[] = [];
  const body = key.startsWith("$") ? key.split("@")[1] ?? "" : key;
  for (const m of body.matchAll(SEGMENT)) {
    const path = body.slice(0, m.index! + m[0].length);
    parts.push(entryLabel(path) ?? `${m[1]} ${m[2]}`);
  }
  return parts.join(" › ");
}
/** A line or input key with each entry key replaced by its label: `person[You].w2[Acme Corp].box1`. */
function displayKey(key: string): string {
  return key.replace(SEGMENT, (whole, coll: string, _k: string, offset: number) => {
    const label = entryLabel(key.slice(0, offset + whole.length).replace(/^\$[^@]*@/, ""));
    return label ? `${coll}[${label}]` : whole;
  });
}
/** Each line or input key inside a sentence, shown with its entries' labels. */
function labelKeys(text: string): string {
  return text.replace(/[$\w@.\[\]-]*\[[\w-]+\][$\w@.\[\]-]*/g, (k) => displayKey(k));
}
/** A sheet line's name: its form or entry, and its printed line number when it has one. */
function lineName(where: { line: SheetLine; section: Section }): string {
  const p = where.line.printed;
  return /^\(/.test(p) ? `${sectionTitle(where.section)} ${p}` : `${sectionTitle(where.section)}, line ${p}`;
}
/** A section title with its entry shown by labels. */
function sectionTitle(section: Section): string {
  if (!section.entry) return section.title;
  const base = section.title.slice(0, section.title.length - section.entry.length - 3);
  return `${base} — ${entryContext(section.entry)}`;
}
/** The entry key for a new label: lowercase, other characters to `_`, a numeric suffix when the key is taken. */
function keyFor(label: string, taken: Set<string>): string {
  const base = label.toLowerCase().replace(/[^a-z0-9]+/g, "_").replace(/^_+|_+$/g, "") || "entry";
  let key = base;
  for (let n = 2; taken.has(key); n++) key = `${base}_${n}`;
  taken.add(key);
  return key;
}

async function api<T>(method: string, path: string, body?: unknown): Promise<T> {
  const r = await fetch(path, { method, headers: body === undefined ? {} : { "Content-Type": "application/json" }, body: body === undefined ? null : JSON.stringify(body) });
  const payload = await r.json() as T & { error?: string };
  if (!r.ok) throw new Error(payload.error ?? `${r.status}`);
  return payload;
}
function showError(message: string | null): void {
  const e = $("error");
  e.hidden = message === null;
  e.textContent = message ?? "";
}

// ---- views ----

const VIEWS: View[] = ["question", "answered", "return", "about"];
function showView(next: View, focusPanel = false): void {
  view = next;
  for (const v of VIEWS) {
    const tab = $(`tab-${v}`);
    const selected = v === next;
    tab.setAttribute("aria-selected", String(selected));
    tab.tabIndex = selected ? 0 : -1;
    $(`panel-${v}`).hidden = !selected;
  }
  if (next === "return") $("derivation").scrollTop = 0;
  if (focusPanel) $(`panel-${next}`).focus({ preventScroll: true });
  window.scrollTo({ top: 0 });
}
/** Arrow keys, Home and End move between the tabs of a tablist, as the ARIA tabs pattern has it. */
function tabKeys(list: HTMLElement, activate: (tab: HTMLElement) => void): void {
  list.addEventListener("keydown", (e) => {
    const tabs = [...list.querySelectorAll<HTMLElement>("[role=tab]")];
    const i = tabs.indexOf(document.activeElement as HTMLElement);
    if (i < 0) return;
    const j = e.key === "ArrowRight" ? (i + 1) % tabs.length : e.key === "ArrowLeft" ? (i + tabs.length - 1) % tabs.length
      : e.key === "Home" ? 0 : e.key === "End" ? tabs.length - 1 : -1;
    if (j < 0) return;
    e.preventDefault();
    tabs[j]!.focus();
    activate(tabs[j]!);
  });
}

// ---- the returns ----

async function loadListing(selected: string | null): Promise<void> {
  const listing = await api<Listing>("GET", "/api/returns");
  docTitles = listing.docTitles ?? {};
  docDesignations = listing.docDesignations ?? {};
  renderNotices(listing.scope, listing.notices, listing.standingNotices);
  const select = $<HTMLSelectElement>("return-select");
  select.replaceChildren(el("option", { value: "" }, listing.returns.length ? "Open a return…" : "No returns yet"));
  for (const name of listing.returns) select.append(el("option", { value: name }, name));
  select.value = selected ?? "";
}
async function openReturn(name: string): Promise<void> {
  reopened = null; trail = []; lastSaved = null;
  state = await api<State>("GET", `/api/returns/${encodeURIComponent(name)}`);
  render();
}
function renderNotices(scope: string, notices: string, standing: string[]): void {
  $("scope").textContent = scope;
  $("notices").textContent = notices;
  $("standing").replaceChildren(...standing.map((n) => el("li", {}, n)));
}

// ---- rendering ----

function render(): void {
  if (!state) return;
  $("return-name").textContent = state.name;
  document.title = `${state.name}: 2025 return`;
  renderNotices(state.scope, state.notices, state.standingNotices);
  lineIndex = new Map();
  for (const section of [...state.sheets.federal, ...state.sheets.newYork]) for (const line of section.lines) lineIndex.set(line.key, { line, section });
  renderBanner();
  renderQuestion();
  renderAnswered();
  renderSheet();
  renderDerivation();
}
function renderEmpty(): void {
  $("status-banner").textContent = "No return open.";
  $("question-panel").replaceChildren(el("div", { class: "page narrow empty" },
    el("h2", {}, "Open a return to begin"),
    el("p", { class: "lede" }, "Choose a return from the list at the top right, or type a name for a new one and choose Start. Each return is a log of your answers, saved outside the project.")));
}

function refusalDetails(r: Value & { kind: "refusal" }, final: boolean): HTMLElement {
  return el("div", { class: "refusal" },
    el("h2", { id: "refusal-title" }, final ? "Refused (final)" : "Refused, provisional"),
    el("p", { class: "lede" }, final ? "No questions are pending, so this refusal stands." : "Later answers may clear it: questions are still pending, and the refusal is figured again after each answer."),
    el("dl", {},
      el("dt", {}, "Form this tool cannot prepare"), el("dd", {}, r.form),
      el("dt", {}, "What to do"), el("dd", {}, r.remedy),
      el("dt", {}, "Trigger"), el("dd", { class: "mono" }, r.gate),
      el("dt", {}, "Source"), el("dd", {}, citeText(r.cite))));
}
/** The conflict a refusal stands for, when its gate is a consistency check. */
function conflictOf(gate: string): Conflict | null {
  return state!.conflicts.find((c) => c.gate === gate) ?? null;
}
/** Every conflict among the answers: its explanation, and each answer it reads as a link that reopens the question
 * (a figure that stands for many answers opens its derivation). */
function conflictBlocks(): HTMLElement[] {
  return state!.conflicts.map((c, i) => {
    const answers = c.answers.map((a) => {
      const about = entryContext(a.input);
      return el("li", {},
        button(`${about ? about + ": " : ""}${shortPrompt(firstLine(a.prompt), 180)}`, { class: "link", "data-input": a.input, title: displayKey(a.input) }, () => reopen(a.input)),
        el("span", { class: "conflict-value" }, fmtAnswer(a, a.value)));
    });
    const figures = c.figures.map((f) => el("li", {},
      button(`${f.printed && !/^\(/.test(f.printed) ? f.printed + " " : ""}${shortPrompt(f.label, 110)}`, { class: "link", "data-ref": f.line, title: displayKey(f.line) }, () => {
        trail = [f.line]; renderDerivation(); renderSheet(); showView("return");
      }),
      el("span", { class: "conflict-value" }, fmtValue(f.value))));
    return el("section", { class: "conflict", ...(i === 0 ? { id: "conflict" } : {}), "aria-labelledby": `conflict-title-${i}` },
      el("h2", { id: `conflict-title-${i}` }, "These answers conflict"),
      el("p", {}, c.explanation),
      answers.length ? el("ul", { class: "conflict-answers" }, ...answers) : null,
      figures.length ? el("p", { class: "conflict-figures-head" }, "Figured from other answers:") : null,
      figures.length ? el("ul", { class: "conflict-answers" }, ...figures) : null,
      el("p", { class: "conflict-help" }, "Choose an answer to change it. The return is figured again after each answer."));
  });
}
function renderBanner(): void {
  const s = state!;
  const b = $("status-banner");
  const status = $("status");
  status.className = `status ${s.status}${s.status === "refused" ? (s.refusalFinal ? " final" : " provisional") : ""}`;
  const pending = plural(s.pending.length, "question");
  const conflict = s.status === "refused" && s.refusal ? conflictOf(s.refusal.gate) : null;
  if (conflict) {
    // Conflicting answers: neither unsupported nor provisional, whatever is still pending.
    status.className = "status conflicting";
    const review = button("Show the answers", { class: "link", id: "conflict-open" }, () => {
      reopened = null; renderQuestion(); showView("question");
      document.getElementById("conflict")?.scrollIntoView({ block: "start", behavior: "instant" });
    });
    b.replaceChildren(el("strong", {}, "These answers conflict."), el("span", { class: "status-form", title: conflict.explanation }, conflict.explanation), review);
  } else if (s.status === "refused" && s.refusal) {
    const r = s.refusal;
    const details = button("Details", { class: "link", id: "refusal-open" }, () => {
      $("refusal-body").replaceChildren(refusalDetails(r, s.refusalFinal));
      $<HTMLDialogElement>("refusal-dialog").showModal();
    });
    b.replaceChildren(el("strong", {}, s.refusalFinal ? "Refused (final)." : "Refused, provisional: later answers may clear it."),
      el("span", { class: "status-form", title: r.form }, `This tool cannot prepare ${r.form}.`),
      s.refusalFinal ? "" : el("span", {}, `${pending} still pending.`), details);
  } else if (s.status === "complete") b.textContent = "Complete: every target line is computed; no questions pending.";
  else b.textContent = `In progress: ${pending} pending.`;
}

function currentQuestion(): { q: Question; correcting: boolean } | null {
  const s = state!;
  if (reopened) {
    const a = s.answered.find((q) => q.input === reopened);
    if (a) return { q: a, correcting: true };
    const p = s.pending.find((q) => q.input === reopened);
    if (p) return { q: p, correcting: false };
    reopened = null;
  }
  return s.pending[0] ? { q: s.pending[0], correcting: false } : null;
}

function savedLine(): HTMLElement {
  const line = el("p", { class: "saved", id: "saved" });
  if (lastSaved) {
    const changed = lastSaved.changed;
    line.append(el("span", { class: "saved-text", title: lastSaved.prompt }, `Saved: ${lastSaved.answer} for “${lastSaved.prompt}”`));
    if (changed) line.append(" ", button(`${plural(changed, "line")} changed`, { class: "link" }, () => {
      $<HTMLInputElement>("changed-only").checked = true; renderSheet(); showView("return", true);
    }));
  }
  return line;
}

function renderQuestion(): void {
  const panel = $("question-panel");
  const current = currentQuestion();
  if (!current) {
    const s = state!;
    panel.replaceChildren(el("div", { class: "page narrow empty" }, savedLine(), ...conflictBlocks(),
      el("h2", { class: "prompt-text" }, s.status === "complete" ? "Every question is answered." : "No questions are pending."),
      el("p", { class: "lede" }, "You can change any answer from the Answered tab, or see how each line was figured under Your return so far.")));
    return;
  }
  const { q, correcting } = current;
  const errorLine = el("p", { class: "field-error", id: "field-error", role: "alert" });
  const submit = async (value: unknown, labels?: Record<string, string>) => {
    errorLine.textContent = "";
    try {
      state = await api<State>("POST", `/api/returns/${encodeURIComponent(state!.name)}/answer`, labels ? { input: q.input, value, labels } : { input: q.input, value });
      const saved = state.answered.find((a) => a.input === q.input);
      lastSaved = { prompt: shortPrompt(firstLine(q.prompt), 90), answer: saved ? fmtAnswer(saved, saved.value) : fmtAnswer(q, value), changed: state.changed.length };
      reopened = null;
      render();
    } catch (e) { errorLine.textContent = `Not saved: ${(e as Error).message}`; }
  };
  const answered = state!.answered.find((a) => a.input === q.input);
  const current_value = answered ? answered.value : undefined;
  const widget = el("div", { class: "widget" });
  const invalid = (m: string) => { errorLine.textContent = m; };
  const labelId = "prompt-heading";
  if (q.type === "Bool") {
    const group = el("div", { class: "choices", role: "group", "aria-labelledby": labelId });
    for (const [label, v] of [["Yes", true], ["No", false]] as const) {
      group.append(button(label, { class: `choice${current_value === v ? " chosen" : ""}`, "data-answer": label.toLowerCase(), "aria-pressed": String(current_value === v) }, () => void submit(v)));
    }
    widget.append(group);
  } else if (q.type === "Enum") {
    const select = el("select", { id: "answer-input", "aria-labelledby": labelId }, el("option", { value: "" }, "Choose…"), ...(q.values ?? []).map((v) => el("option", { value: v }, v))) as HTMLSelectElement;
    if (typeof current_value === "string") select.value = current_value;
    const ok = button("Save answer", { class: "primary", id: "answer-submit" }, () => { if (!select.value) invalid("Choose a value."); else void submit(select.value); });
    widget.append(el("div", { class: "entry" }, select, ok));
  } else if (q.type === "Dollars" || q.type === "NonNegDollars" || q.type === "Count") {
    const money = q.type !== "Count";
    const input = el("input", { type: "text", id: "answer-input", name: "answer", inputmode: money ? "decimal" : "numeric", autocomplete: "off", spellcheck: "false",
      "aria-labelledby": labelId, "aria-describedby": "field-error", placeholder: money ? "0.00" : "0" }) as HTMLInputElement;
    if (typeof current_value === "number") input.value = money ? (current_value / 100).toFixed(2) : String(current_value);
    const go = () => {
      const text = input.value.trim();
      if (text === "") { invalid(money ? "Enter an amount. If the box on your form is blank and that means zero, enter 0." : "Enter a number."); return; }
      if (!money) { if (!/^\d+$/.test(text)) invalid("Enter a whole number."); else void submit(Number(text)); return; }
      const m = text.replace(/[$\s]/g, "").match(/^(-)?(\d{1,3}(?:,\d{3})+|\d+)(?:\.(\d{1,2}))?$/);
      if (!m) { invalid("Enter dollars and cents, for example 1234.56."); return; }
      if (m[1] && q.type === "NonNegDollars") { invalid("This amount cannot be negative."); return; }
      const cents = Number(m[2]!.replaceAll(",", "")) * 100 + Number((m[3] ?? "").padEnd(2, "0") || "0");
      if (!Number.isSafeInteger(cents)) { invalid("That amount is too large."); return; }
      void submit(m[1] ? -cents : cents);
    };
    input.onkeydown = (e) => { if (e.key === "Enter") go(); };
    const field = el("div", { class: `amount${money ? " money" : ""}` }, money ? el("span", { class: "unit", "aria-hidden": "true" }, "$") : null, input);
    widget.append(el("div", { class: "entry" }, field, button("Save answer", { class: "primary", id: "answer-submit" }, go)),
      el("p", { class: "hint" }, money ? "Dollars and cents, for example 1,234.56. Enter 0 if the amount is zero." : "A whole number."));
  } else if (q.type === "Roster" && q.choices) {
    // A roster with a fixed set of answers is a selector.
    const keys = Array.isArray(current_value) ? current_value as string[] : null;
    const group = el("div", { class: "choices", role: "group", "aria-labelledby": labelId });
    q.choices.forEach((c, i) => {
      const chosen = keys !== null && c.value.length === keys.length && c.value.every((k, j) => k === keys[j]);
      group.append(button(c.label, { class: `choice${chosen ? " chosen" : ""}`, "data-choice": String(i), "aria-pressed": String(chosen) }, () => void submit(c.value, c.labels)));
    });
    widget.append(group);
  } else if (q.type === "Roster") {
    // An open roster: the user types a label per entry; the page derives each new entry's key from its label, and an
    // existing entry keeps its key (and the answers under it) when its label is edited.
    const rows = el("ol", { id: "roster", "aria-labelledby": labelId });
    const renumber = () => rows.querySelectorAll("li").forEach((li, i) => {
      li.querySelector("input")!.setAttribute("aria-label", `Entry ${i + 1} name`);
      li.querySelector("button")!.setAttribute("aria-label", `Remove entry ${i + 1}`);
    });
    const addRow = (label = "", key = "") => {
      const input = el("input", { type: "text", value: label, placeholder: "A name you will recognize, e.g. Acme Corp", autocomplete: "off", spellcheck: "false", "data-key": key }) as HTMLInputElement;
      const row = el("li", { class: "roster-row" }, input);
      row.append(button("Remove", { class: "quiet" }, () => { row.remove(); renumber(); }));
      rows.append(row);
      renumber();
    };
    const existing = Array.isArray(current_value) ? current_value as string[] : [];
    if (existing.length) existing.forEach((k) => addRow(entryLabel(rosterEntryPath(q.input, k)) ?? k, k)); else addRow();
    const add = button("Add another", { id: "roster-add", class: "quiet" }, () => { addRow(); (rows.lastElementChild?.querySelector("input") as HTMLInputElement | null)?.focus(); });
    const ok = button(existing.length ? "Save list" : "Save list (empty if none)", { class: "primary", id: "answer-submit" }, () => {
      const entries = [...rows.querySelectorAll("input")].map((i) => ({ label: (i as HTMLInputElement).value.trim(), key: (i as HTMLInputElement).dataset.key ?? "" }))
        .filter((e) => e.label !== "" || e.key !== "");
      if (entries.some((e) => e.label === "")) { invalid("Give each entry a name, or remove it."); return; }
      if (entries.some((e) => e.label.length > 200)) { invalid("A name can be at most 200 characters."); return; }
      const taken = new Set(entries.map((e) => e.key).filter((k) => k !== ""));
      const keys = entries.map((e) => e.key || keyFor(e.label, taken));
      if (keys.some((k) => !KEY.test(k))) { invalid("Could not make an entry key from a name."); return; }
      void submit(keys, Object.fromEntries(keys.map((k, i) => [k, entries[i]!.label])));
    });
    widget.append(rows, el("div", { class: "entry" }, add, ok),
      el("p", { class: "hint" }, "Names are saved in your answer log, outside the project. Do not enter account numbers or Social Security numbers."));
    widget.classList.add("roster");
  } else {
    widget.append(`This input's type (${q.type}) has no widget.`);
  }
  const help = button("I don’t know / need help", { id: "need-help", class: "quiet" }, () => void submit(null));
  const about = entryContext(q.input);
  const head: (HTMLElement | null)[] = [];
  if (correcting) {
    head.push(el("div", { class: "correcting" },
      el("span", {}, `Changing your answer (now: ${fmtAnswer(q, current_value)}). A change is a new entry in the log. `),
      button("Back to the next question", { class: "link", id: "back-next" }, () => { reopened = null; render(); })));
  } else if (reopened) {
    head.push(el("div", { class: "correcting" }, button("Back to the next question", { class: "link", id: "back-next" }, () => { reopened = null; render(); })));
  }
  const main = el("div", { class: "ask" },
    ...head,
    about ? el("p", { class: "about" }, `About: ${about}`) : null,
    el("h2", { class: "prompt-heading visually-hidden", id: labelId }, shortPrompt(firstLine(q.prompt), 160)),
    longText(q.prompt, "prompt-text", "prompt", "question", false),
    widget, errorLine,
    q.helpRequested ? el("p", { class: "note" }, "You asked for help with this question. It stays unanswered until you answer it.") : null,
    q.help ? el("section", { class: "help", "aria-label": "Explanation" }, longText(q.help, "help-text", "help", "explanation", true)) : null,
    formsBlock(q.forms ?? []),
    el("div", { class: "actions" }, help));
  panel.replaceChildren(savedLine(), ...conflictBlocks(), el("article", { class: "question", "data-input": q.input }, main, sourceBlock(q.cite, q.input)));
  if (view === "question") (panel.querySelector("#answer-input, .widget .choice, .roster-row input") as HTMLElement | null)?.focus({ preventScroll: true });
}
function shortPrompt(text: string, n: number): string {
  if (text.length <= n) return text;
  return text.slice(0, text.lastIndexOf(" ", n - 1)) + "…";
}

function renderAnswered(): void {
  const s = state!;
  $("answered-count").textContent = String(s.answered.length);
  $("answered").replaceChildren(...s.answered.map((a) => {
    const about = entryContext(a.input);
    const link = button(el("span", { class: "q" }, firstLine(a.prompt)), { class: "answered-q", "data-input": a.input, title: displayKey(a.input) }, () => reopen(a.input));
    if (about) link.prepend(el("span", { class: "about" }, about));
    return el("li", {}, link, el("span", { class: "value" }, fmtAnswer(a, a.value)));
  }));
}

function reopen(input: string): void {
  reopened = input;
  renderQuestion();
  showView("question");
  ($("question-panel").querySelector("#answer-input, .widget .choice, .roster-row input") as HTMLElement | null)?.focus({ preventScroll: true });
}

function statusTag(line: { status: string; value?: Value }): HTMLElement | null {
  if (line.status === "refused" && line.value?.kind === "refusal" && conflictOf(line.value.gate)) return el("span", { class: "tag" }, "conflicting answers");
  if (line.status === "refused") return el("span", { class: "tag" }, state!.refusalFinal ? "refused" : "refused, provisional");
  if (line.status === "unknown") return el("span", { class: "tag" }, "unknown");
  return null;
}

/** The order the page shows a sheet's sections in: the return itself (Form 1040, Form IT-201), then its schedules,
 * then the other forms, then worksheets and helper sections; the engine's order within each group. Display only: the
 * engine's sheet, and the text sheet rendered from it, keep their own order. */
const MAIN_RETURNS = new Set(["f1040", "ny_it201"]);
function sheetOrder(sections: Section[]): Section[] {
  const rank = (s: Section) => MAIN_RETURNS.has(s.doc) ? 0 : s.title.startsWith("Schedule ") ? 1 : s.title.startsWith("Form ") ? 2 : 3;
  return sections.map((s, i) => ({ s, i })).sort((a, b) => rank(a.s) - rank(b.s) || a.i - b.i).map(({ s }) => s);
}

function renderSheet(): void {
  const s = state!;
  for (const b of document.querySelectorAll<HTMLButtonElement>(".tabs [data-sheet]")) {
    const on = b.dataset.sheet === sheetTab;
    b.setAttribute("aria-selected", String(on)); b.tabIndex = on ? 0 : -1;
  }
  const changed = new Set(s.changed);
  const only = $<HTMLInputElement>("changed-only").checked;
  const open = trail.at(-1);
  const out: HTMLElement[] = [];
  for (const section of sheetOrder(s.sheets[sheetTab])) {
    const lines = section.lines.filter((l) => l.shown && (!only || changed.has(l.key)));
    if (!lines.length && only) continue;
    const rows = lines.map((l) => el("tr", { "data-key": l.key, class: `${l.status}${changed.has(l.key) ? " changed" : ""}${open === l.key ? " open" : ""}` },
      el("th", { class: `printed${/^\(/.test(l.printed) ? " aside" : ""}`, scope: "row" }, l.printed),
      el("td", { class: "label" }, button(firstLine(l.label), { class: "line-open", "aria-current": String(open === l.key) }), ...textBlocks(l.label).slice(1)),
      el("td", { class: "value", ...(l.value.kind === "unknown" ? { title: labelKeys(l.value.reason) } : {}) },
        l.value.kind === "refusal" ? null : fmtValue(l.value), l.value.kind === "refusal" ? statusTag(l) : null)));
    out.push(el("section", { class: "form" }, el("h3", {}, sectionTitle(section)),
      el("table", { class: "lines" }, el("tbody", {}, ...rows))));
  }
  if (!out.length) out.push(el("p", { class: "placeholder" }, only ? "No line on this sheet changed with the last answer." : "Nothing figured yet."));
  $("sheet").replaceChildren(...out);
}

/** The answers a line depends on: the inputs reached through its operands, and the rosters of their entries. */
function dependsOn(key: string): string[] {
  const s = state!;
  const seen = new Set<string>([key]);
  const queue = [key];
  const inputs = new Set<string>();
  while (queue.length) {
    const k = queue.shift()!;
    const d = s.values[k];
    if (!d) continue;
    if (d.op === "input") inputs.add(k);
    for (const o of d.operands) if (!seen.has(o.ref) && o.ref in s.values) { seen.add(o.ref); queue.push(o.ref); }
  }
  for (const k of [...inputs]) {
    for (const m of k.matchAll(/([a-zA-Z0-9_]+)\[([a-zA-Z0-9_-]+)\]/g)) {
      const parent = k.slice(0, m.index).replace(/\.$/, "");
      inputs.add(`$${m[1]}${parent ? "@" + parent : ""}`);
    }
  }
  return [...inputs].sort();
}

function openDerivation(key: string): void {
  trail.push(key);
  renderDerivation();
  renderSheet();
  $("derivation").focus({ preventScroll: true });
}

function renderDerivation(): void {
  const box = $("derivation");
  const s = state!;
  const key = trail.at(-1);
  if (!key || !s.values[key]) { box.hidden = true; $("derivation-empty").hidden = false; box.replaceChildren(); return; }
  const d = s.values[key]!;
  const where = lineIndex.get(key);
  const refLink = (ref: string) => {
    const where = lineIndex.get(ref);
    const name = where ? lineName(where) : displayKey(ref);
    if (!(ref in s.values)) return el("span", { class: "mono" }, name);
    return button(name, { class: "link", "data-ref": ref, title: displayKey(ref) }, () => openDerivation(ref));
  };
  const deps = dependsOn(key).map((input) => {
    const a = s.answered.find((q) => q.input === input);
    const p = s.pending.find((q) => q.input === input);
    if (!a && !p) return el("li", { class: "mono" }, displayKey(input));
    const about = entryContext(input);
    const b = button(`${about ? about + ": " : ""}${shortPrompt(firstLine((a ?? p)!.prompt), 110)}`, { class: "link", "data-input": input, title: displayKey(input) }, () => reopen(input));
    return el("li", {}, b, el("span", { class: "dep-value" }, a ? fmtAnswer(a, a.value) : "not yet answered"));
  });
  const close = button("Close", { class: "quiet" }, () => { trail = []; renderDerivation(); renderSheet(); });
  const back = button("Back", { class: "quiet", id: "derivation-back" }, () => { trail.pop(); renderDerivation(); renderSheet(); });
  const conflict = d.value.kind === "refusal" ? conflictOf(d.value.gate) : null;
  const valueText = conflict
    ? el("span", { class: "refused-value" }, `These answers conflict. ${conflict.explanation}`)
    : d.value.kind === "refusal"
    ? el("span", { class: "refused-value" }, `${s.refusalFinal ? "Refused (final)" : "Refused, provisional: later answers may clear it"}. This tool cannot prepare ${d.value.form}. ${d.value.remedy}`)
    : d.value.kind === "unknown"
      ? el("span", {}, el("span", { class: "figure unknown-value" }, "Unknown"), el("span", { class: "reason" }, labelKeys(d.value.reason)))
      : el("span", { class: "figure" }, fmtValue(d.value));
  const listOr = (items: HTMLElement[], none: string, attrs: Record<string, string> = {}) => items.length ? el("ul", attrs, ...items) : el("p", { class: "none" }, none);
  box.hidden = false;
  box.scrollTop = 0;
  $("derivation-empty").hidden = true;
  box.replaceChildren(...[
    el("div", { class: "derivation-bar" }, el("h2", {}, where ? lineName(where) : displayKey(key)),
      el("div", { class: "derivation-actions" }, trail.length > 1 ? back : null, close)),
    where ? richText("p", { class: "line-label" }, where.line.label) : null,
    el("p", { class: "derived-value" }, valueText, s.changed.includes(key) ? el("span", { class: "tag" }, "changed by the last answer") : null),
    el("dl", {},
      el("dt", {}, "Operation"), el("dd", { class: "mono" }, d.op),
      el("dt", {}, "Source"), el("dd", {}, citeText(d.cite) || "none")),
    el("h3", {}, "Lines it uses"),
    listOr(d.operands.map((o) => el("li", {}, refLink(o.ref), el("span", { class: "dep-value" }, fmtValue(o.value)))), "None."),
    el("h3", {}, "Answers it depends on"),
    listOr(deps, "None.", { id: "depends-on" }),
    d.guardsNotTaken.length ? el("h3", {}, "Conditions not taken") : null,
    d.guardsNotTaken.length ? el("ul", { class: "mono" }, ...d.guardsNotTaken.map((g) => el("li", {}, `${g.guard} = ${fmtValue(g.value)}`))) : null,
    d.notes.length ? el("h3", {}, "Notes") : null,
    d.notes.length ? el("ul", {}, ...d.notes.map((n) => el("li", {}, n))) : null,
    el("p", { class: "meta key" }, displayKey(key))].filter((n): n is HTMLElement => n !== null));
}

// ---- events ----

function selectedName(): string | null {
  const name = decodeURIComponent(location.hash.slice(1));
  return name ? name : null;
}
async function route(): Promise<void> {
  showError(null);
  const name = selectedName();
  try {
    await loadListing(name);
    if (name) await openReturn(name); else { state = null; renderEmpty(); }
  } catch (e) { showError((e as Error).message); }
}

document.addEventListener("DOMContentLoaded", () => {
  $("return-select").addEventListener("change", (e) => { const v = (e.target as HTMLSelectElement).value; if (v) location.hash = encodeURIComponent(v); });
  $("new-return").addEventListener("submit", (e) => {
    e.preventDefault();
    const name = $<HTMLInputElement>("new-name").value.trim();
    void api<State>("POST", "/api/returns", { name }).then(() => { $<HTMLInputElement>("new-name").value = ""; location.hash = encodeURIComponent(name); })
      .catch((err: Error) => showError(err.message));
  });
  for (const v of VIEWS) $(`tab-${v}`).addEventListener("click", () => showView(v));
  tabKeys($("view-tabs"), (tab) => showView(tab.id.slice(4) as View));
  const sheetTabs = document.querySelector<HTMLElement>(".tabs[role=tablist]")!;
  const pickSheet = (b: HTMLElement) => { sheetTab = b.dataset.sheet as "federal" | "newYork"; if (state) renderSheet(); };
  for (const b of sheetTabs.querySelectorAll<HTMLButtonElement>("[data-sheet]")) b.addEventListener("click", () => pickSheet(b));
  tabKeys(sheetTabs, pickSheet);
  $("changed-only").addEventListener("change", () => { if (state) renderSheet(); });
  $("sheet").addEventListener("click", (e) => {
    const row = (e.target as HTMLElement).closest("tr[data-key]") as HTMLElement | null;
    if (row) { trail = []; openDerivation(row.dataset.key!); }
  });
  $("derivation").tabIndex = -1;
  window.addEventListener("hashchange", () => void route());
  void route();
});
