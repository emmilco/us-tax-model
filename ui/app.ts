// The page of the web UI: a client of the server's JSON API (engine/src/serve.ts). It computes nothing about the
// return: every value, status, refusal and question comes from the engine. Left, the interview; right, the federal
// and New York values sheets, each line opening its derivation.

type Cite = { doc: string; locator: string; revision?: string };
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
interface Question { input: string; prompt: string; help: string; cite: Cite; helpRequested?: boolean; type: string; values?: string[]; choices?: Choice[]; value?: unknown }
interface SheetLine { key: string; printed: string; label: string; value: Value; status: string; shown: boolean; notes: string[] }
interface Section { doc: string; title: string; entry: string | null; lines: SheetLine[] }
interface State {
  name: string; status: "incomplete" | "complete" | "refused"; refusal: (Value & { kind: "refusal" }) | null; refusalFinal: boolean;
  pending: Question[]; answered: Question[]; scope: string; notices: string; standingNotices: string[];
  values: Record<string, Derivation>; sheets: { federal: Section[]; newYork: Section[] }; changed: string[];
  entryLabels: Record<string, string>;
}
interface Listing { returns: string[]; scope: string; notices: string; standingNotices: string[] }

const KEY = /^[a-zA-Z0-9_-]+$/;
let state: State | null = null;
let reopened: string | null = null; // an answered question reopened for correction, or a pending one chosen
let sheetTab: "federal" | "newYork" = "federal";
let trail: string[] = []; // the derivations opened, most recent last
let lineIndex = new Map<string, { line: SheetLine; section: Section }>();

const $ = <T extends HTMLElement>(id: string) => document.getElementById(id) as T;
function el(tag: string, attrs: Record<string, string> = {}, ...children: (Node | string | null | undefined)[]): HTMLElement {
  const e = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) {
    if (k === "class") e.className = v; else e.setAttribute(k, v);
  }
  for (const c of children) if (c !== null && c !== undefined) e.append(c);
  return e;
}

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
    case "bool": return v.value ? "true" : "false";
    case "enum": return v.value;
    case "rate": return `${v.num}/${v.den}`;
    case "refusal": return `REFUSED: ${v.form}`;
    case "unknown": return `UNKNOWN (${v.reason})`;
  }
}
function fmtAnswer(q: Question, value: unknown): string {
  if (value === null) return "help requested";
  if (q.type === "Dollars" || q.type === "NonNegDollars") return fmtMoney(value as number);
  if (q.type === "Bool") return value ? "yes" : "no";
  if (q.type === "Roster") {
    const keys = value as string[];
    const choice = q.choices?.find((c) => c.value.length === keys.length && c.value.every((k, i) => k === keys[i]));
    if (choice) return choice.label;
    return keys.length ? keys.map((k) => entryLabel(rosterEntryPath(q.input, k)) ?? k).join(", ") : "none";
  }
  return String(value);
}
function citeText(c: Cite | null): string {
  return c ? `${c.doc}, ${c.locator}${c.revision ? ` (${c.revision})` : ""}` : "";
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

// ---- the returns ----

async function loadListing(selected: string | null): Promise<void> {
  const listing = await api<Listing>("GET", "/api/returns");
  renderNotices(listing.scope, listing.notices, listing.standingNotices);
  const select = $<HTMLSelectElement>("return-select");
  select.replaceChildren(el("option", { value: "" }, listing.returns.length ? "open a return…" : "no returns yet"));
  for (const name of listing.returns) select.append(el("option", { value: name }, name));
  select.value = selected ?? "";
}
async function openReturn(name: string): Promise<void> {
  reopened = null; trail = [];
  state = await api<State>("GET", `/api/returns/${encodeURIComponent(name)}`);
  render();
}
function renderNotices(scope: string, notices: string, standing: string[]): void {
  $("scope").textContent = scope;
  $("notices").replaceChildren(el("p", {}, notices), ...standing.map((n) => el("p", {}, n)));
}

// ---- rendering ----

function render(): void {
  if (!state) return;
  $("return-name").textContent = state.name;
  renderNotices(state.scope, state.notices, state.standingNotices);
  lineIndex = new Map();
  for (const section of [...state.sheets.federal, ...state.sheets.newYork]) for (const line of section.lines) lineIndex.set(line.key, { line, section });
  renderBanner();
  renderQuestion();
  renderAnswered();
  renderSheet();
  renderDerivation();
}

function refusalBlock(r: Value & { kind: "refusal" }, final: boolean): HTMLElement {
  return el("span", {},
    el("strong", {}, final ? "Refused (final). " : "Refused, provisional: later answers may clear it. "),
    `This tool cannot prepare ${r.form}. ${r.remedy} `,
    el("span", { class: "mono" }, `Trigger: ${r.gate}. `),
    `Source: ${citeText(r.cite)}.`);
}
function renderBanner(): void {
  const s = state!;
  const b = $("status-banner");
  b.hidden = false;
  b.className = `banner ${s.status}`;
  if (s.status === "refused" && s.refusal) b.replaceChildren(refusalBlock(s.refusal, s.refusalFinal),
    s.refusalFinal ? "" : ` ${s.pending.length} question${s.pending.length === 1 ? "" : "s"} still pending.`);
  else if (s.status === "complete") b.textContent = "Complete: every target line is computed; no questions pending.";
  else b.textContent = `Incomplete: ${s.pending.length} question${s.pending.length === 1 ? "" : "s"} pending.`;
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

function renderQuestion(): void {
  const panel = $("question-panel");
  const current = currentQuestion();
  if (!current) {
    panel.replaceChildren(el("div", { class: "question" }, el("p", { class: "prompt" }, "No questions are pending."),
      el("p", { class: "help" }, "Click an answered question below to correct it, or a line on the right to see how it was derived.")));
    return;
  }
  const { q, correcting } = current;
  const errorLine = el("p", { class: "field-error", id: "field-error" });
  const submit = async (value: unknown, labels?: Record<string, string>) => {
    errorLine.textContent = "";
    try {
      state = await api<State>("POST", `/api/returns/${encodeURIComponent(state!.name)}/answer`, labels ? { input: q.input, value, labels } : { input: q.input, value });
      reopened = null;
      render();
    } catch (e) { errorLine.textContent = `Not saved: ${(e as Error).message}`; }
  };
  const answered = state!.answered.find((a) => a.input === q.input);
  const current_value = answered ? answered.value : undefined;
  const widget = el("div", { class: "widget" });
  const invalid = (m: string) => { errorLine.textContent = m; };
  if (q.type === "Bool") {
    const yes = el("button", { class: current_value === true ? "primary" : "", "data-answer": "yes" }, "Yes");
    const no = el("button", { class: current_value === false ? "primary" : "", "data-answer": "no" }, "No");
    yes.onclick = () => void submit(true);
    no.onclick = () => void submit(false);
    widget.append(yes, no);
  } else if (q.type === "Enum") {
    const select = el("select", { id: "answer-input" }, el("option", { value: "" }, "choose…"), ...(q.values ?? []).map((v) => el("option", { value: v }, v))) as HTMLSelectElement;
    if (typeof current_value === "string") select.value = current_value;
    const ok = el("button", { class: "primary", id: "answer-submit" }, "Save");
    ok.onclick = () => { if (!select.value) invalid("Choose a value."); else void submit(select.value); };
    widget.append(select, ok);
  } else if (q.type === "Dollars" || q.type === "NonNegDollars" || q.type === "Count") {
    const money = q.type !== "Count";
    const input = el("input", { type: "text", id: "answer-input", inputmode: money ? "decimal" : "numeric", autocomplete: "off",
      placeholder: money ? "dollars and cents, e.g. 1,234.56" : "a whole number" }) as HTMLInputElement;
    if (typeof current_value === "number") input.value = money ? (current_value / 100).toFixed(2) : String(current_value);
    const ok = el("button", { class: "primary", id: "answer-submit" }, "Save");
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
    ok.onclick = go;
    input.onkeydown = (e) => { if (e.key === "Enter") go(); };
    widget.append(money ? el("span", {}, "$") : "", input, ok);
  } else if (q.type === "Roster" && q.choices) {
    // A roster with a fixed set of answers is a selector.
    const keys = Array.isArray(current_value) ? current_value as string[] : null;
    q.choices.forEach((c, i) => {
      const chosen = keys !== null && c.value.length === keys.length && c.value.every((k, j) => k === keys[j]);
      const b = el("button", { class: chosen ? "primary" : "", "data-choice": String(i) }, c.label);
      b.onclick = () => void submit(c.value, c.labels);
      widget.append(b);
    });
  } else if (q.type === "Roster") {
    // An open roster: the user types a label per entry; the page derives each new entry's key from its label, and an
    // existing entry keeps its key (and the answers under it) when its label is edited.
    const rows = el("div", { id: "roster" });
    const addRow = (label = "", key = "") => {
      const input = el("input", { type: "text", value: label, placeholder: "a name you will recognize, e.g. Acme Corp", autocomplete: "off", "data-key": key }) as HTMLInputElement;
      const remove = el("button", {}, "Remove");
      const row = el("div", { class: "roster-row" }, input, remove);
      remove.onclick = () => row.remove();
      rows.append(row);
    };
    const existing = Array.isArray(current_value) ? current_value as string[] : [];
    if (existing.length) existing.forEach((k) => addRow(entryLabel(rosterEntryPath(q.input, k)) ?? k, k)); else addRow();
    const add = el("button", { id: "roster-add" }, "Add");
    add.onclick = () => { addRow(); (rows.lastElementChild?.querySelector("input") as HTMLInputElement | null)?.focus(); };
    const ok = el("button", { class: "primary", id: "answer-submit" }, existing.length ? "Save list" : "Save list (empty if none)");
    ok.onclick = () => {
      const entries = [...rows.querySelectorAll("input")].map((i) => ({ label: (i as HTMLInputElement).value.trim(), key: (i as HTMLInputElement).dataset.key ?? "" }))
        .filter((e) => e.label !== "" || e.key !== "");
      if (entries.some((e) => e.label === "")) { invalid("Give each entry a label, or remove it."); return; }
      if (entries.some((e) => e.label.length > 200)) { invalid("A label can be at most 200 characters."); return; }
      const taken = new Set(entries.map((e) => e.key).filter((k) => k !== ""));
      const keys = entries.map((e) => e.key || keyFor(e.label, taken));
      if (keys.some((k) => !KEY.test(k))) { invalid("Could not make an entry key from a label."); return; }
      void submit(keys, Object.fromEntries(keys.map((k, i) => [k, entries[i]!.label])));
    };
    widget.append(rows, add, ok,
      el("p", { class: "muted" }, "Labels are saved in your answer log, outside the project. Do not enter account numbers or social security numbers."));
    widget.classList.add("roster");
  } else {
    widget.append(`This input's type (${q.type}) has no widget.`);
  }
  const help = el("button", { id: "need-help" }, "I don't know / need help");
  help.onclick = () => void submit(null);
  const actions = el("div", { class: "actions" }, help);
  if (reopened) {
    const back = el("button", {}, "Back to the next question");
    back.onclick = () => { reopened = null; render(); };
    actions.append(back);
  }
  const about = entryContext(q.input);
  panel.replaceChildren(el("div", { class: "question", "data-input": q.input },
    correcting ? el("p", { class: "correcting" }, `Correcting your answer (now: ${fmtAnswer(q, current_value)}). A correction is a new entry in the log.`) : null,
    about ? el("p", { class: "about" }, `About: ${about}`) : null,
    el("p", { class: "prompt" }, q.prompt),
    q.help ? el("p", { class: "help" }, q.help) : null,
    q.helpRequested ? el("p", { class: "note" }, "You asked for help with this question; it stays unanswered until you answer it.") : null,
    widget, errorLine, actions,
    el("div", { class: "source" }, el("span", { class: "source-label" }, "Source"),
      el("span", {}, ` — the form line or instruction this question comes from: ${citeText(q.cite)}`)),
    el("p", { class: "key" }, displayKey(q.input))));
  const focus = panel.querySelector("#answer-input, .widget button, .roster-row input") as HTMLElement | null;
  focus?.focus();
}

function renderAnswered(): void {
  const s = state!;
  $("answered-count").textContent = `(${s.answered.length})`;
  $("answered").replaceChildren(...s.answered.map((a) => {
    const link = el("button", { class: "link", "data-input": a.input, title: a.input }, a.prompt.length > 110 ? a.prompt.slice(0, 107) + "…" : a.prompt);
    link.onclick = () => reopen(a.input);
    return el("li", {}, link, el("span", { class: "value" }, fmtAnswer(a, a.value)), el("div", { class: "mono muted" }, displayKey(a.input)));
  }));
}

function reopen(input: string): void {
  reopened = input;
  renderQuestion();
  $("question-panel").scrollIntoView({ block: "start" });
}

function statusTag(line: { status: string }): HTMLElement | null {
  if (line.status === "refused") return el("span", { class: "tag" }, state!.refusalFinal ? "refused" : "refused, provisional");
  if (line.status === "unknown") return el("span", { class: "tag" }, "unknown");
  return null;
}

function renderSheet(): void {
  const s = state!;
  for (const b of document.querySelectorAll<HTMLButtonElement>(".tabs [data-sheet]")) b.setAttribute("aria-selected", String(b.dataset.sheet === sheetTab));
  const changed = new Set(s.changed);
  const only = $<HTMLInputElement>("changed-only").checked;
  const out: HTMLElement[] = [];
  for (const section of s.sheets[sheetTab]) {
    const lines = section.lines.filter((l) => l.shown && (!only || changed.has(l.key)));
    if (!lines.length && only) continue;
    const rows = lines.map((l) => el("tr", { "data-key": l.key, class: `${l.status}${changed.has(l.key) ? " changed" : ""}` },
      el("td", { class: "printed" }, l.printed), el("td", {}, l.label), el("td", { class: "value" }, fmtValue(l.value), statusTag(l))));
    out.push(el("div", { class: "section" }, el("h3", {}, sectionTitle(section)), el("table", { class: "lines" }, el("tbody", {}, ...rows))));
  }
  if (!out.length) out.push(el("p", { class: "muted" }, only ? "No line on this sheet changed with the last answer." : "Nothing evaluated yet."));
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
  $("derivation").scrollIntoView({ block: "start" });
}

function renderDerivation(): void {
  const box = $("derivation");
  const s = state!;
  const key = trail.at(-1);
  if (!key || !s.values[key]) { box.hidden = true; box.replaceChildren(); return; }
  const d = s.values[key]!;
  const where = lineIndex.get(key);
  const refLink = (ref: string) => {
    if (!(ref in s.values)) return el("span", { class: "mono" }, ref);
    const b = el("button", { class: "link mono", "data-ref": ref }, displayKey(ref));
    b.onclick = () => openDerivation(ref);
    return b;
  };
  const deps = dependsOn(key).map((input) => {
    const a = s.answered.find((q) => q.input === input);
    const p = s.pending.find((q) => q.input === input);
    if (!a && !p) return el("li", { class: "mono" }, displayKey(input));
    const b = el("button", { class: "link", "data-input": input }, a ? `${a.prompt.slice(0, 90)}${a.prompt.length > 90 ? "…" : ""}` : `not yet answered: ${p!.prompt.slice(0, 80)}…`);
    b.onclick = () => reopen(input);
    return el("li", {}, b, a ? el("span", { class: "mono" }, ` = ${fmtAnswer(a, a.value)}`) : null, el("div", { class: "mono muted" }, displayKey(input)));
  });
  const close = el("button", {}, "Close");
  close.onclick = () => { trail = []; renderDerivation(); };
  const back = el("button", {}, "Back");
  back.onclick = () => { trail.pop(); renderDerivation(); };
  const valueText = d.value.kind === "refusal" ? refusalBlock(d.value, s.refusalFinal) : el("span", { class: "mono" }, fmtValue(d.value));
  box.hidden = false;
  box.replaceChildren(
    el("div", { class: "bar" }, el("h3", {}, where ? `${sectionTitle(where.section)}, line ${where.line.printed}` : key), trail.length > 1 ? back : null, close),
    where ? el("p", {}, where.line.label) : "",
    el("dl", {},
      el("dt", {}, "line"), el("dd", { class: "mono" }, displayKey(key)),
      el("dt", {}, "value"), el("dd", {}, valueText, s.changed.includes(key) ? el("span", { class: "tag" }, "changed by the last answer") : null),
      el("dt", {}, "operation"), el("dd", { class: "mono" }, d.op),
      el("dt", {}, "source"), el("dd", {}, citeText(d.cite) || "none"),
      el("dt", {}, "operands"), el("dd", {}, d.operands.length ? el("ul", {}, ...d.operands.map((o) => el("li", {}, refLink(o.ref), el("span", { class: "mono" }, ` = ${fmtValue(o.value)}`)))) : "none"),
      el("dt", {}, "guards not taken"), el("dd", {}, d.guardsNotTaken.length ? el("ul", {}, ...d.guardsNotTaken.map((g) => el("li", { class: "mono" }, `${g.guard} = ${fmtValue(g.value)}`))) : "none"),
      el("dt", {}, "notes"), el("dd", {}, d.notes.length ? el("ul", {}, ...d.notes.map((n) => el("li", {}, n))) : "none"),
      el("dt", {}, "answers it depends on"), el("dd", {}, deps.length ? el("ul", { id: "depends-on" }, ...deps) : "none")));
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
    if (name) await openReturn(name);
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
  for (const b of document.querySelectorAll<HTMLButtonElement>(".tabs [data-sheet]")) {
    b.addEventListener("click", () => { sheetTab = b.dataset.sheet as "federal" | "newYork"; if (state) renderSheet(); });
  }
  $("changed-only").addEventListener("change", () => { if (state) renderSheet(); });
  $("sheet").addEventListener("click", (e) => {
    const row = (e.target as HTMLElement).closest("tr[data-key]") as HTMLElement | null;
    if (row) { trail = []; openDerivation(row.dataset.key!); }
  });
  window.addEventListener("hashchange", () => void route());
  void route();
});
