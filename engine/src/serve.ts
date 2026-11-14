// The web UI's server: `serve --dir <returns dir> [--port N] [--vetting <verdict file>] [--log-connections]`. A local, single-user client of the interview, as the
// CLI is: each request replays a return's answer log with the `ny` profile (federal and New York) and answers go
// through `applyAnswer`. It serves the page in ui/ and a JSON API, on 127.0.0.1 only.
//
//   GET  /api/returns                 the return logs in the returns directory, and each source document's title
//   POST /api/returns {name}          starts a log <name>.jsonl (mode 0600; an existing name is refused)
//   GET  /api/returns/:name           the return's state; question text and line labels are as shown to the filer (the
//                                     spouse phrase reworded for the filing status answered); each question carries `forms`, the forms its prompt and
//                                     help name that the catalogs hold, with designation, title and purpose; and
//                                     `conflicts`, each refusal whose gate is a consistency check
//                                     (interview/<year>/conflict_checks.yaml) with its explanation and the answers and
//                                     figures the gate reads
//   POST /api/returns/:name/answer {input, value[, labels]}
//                                     (labels: a roster answer's label for each entry key, kept in the log)
//                                     appends the answer and returns the new state, or 400 with the reason
//   GET  /api/vetting                 every question the profile can ask as a card (vetting.ts), each with the owner's
//                                     record and whether it is stale, the records of questions no longer asked, and
//                                     the counts
//   POST /api/vetting {id, digest[, verdict][, note]}
//                                     saves a verdict (up, down or none) or a note on the question as shown (`digest`
//                                     is the card's; 409 when the wording has changed since) and returns the record and
//                                     the counts; 500 with the reason when the file could not be written
//
// The page at /vet (ui/vet.html) is the client of the vetting routes. Verdicts are saved in the repository's tracked
// verdict file whatever the returns directory is (`--vetting <file>` names another file, for tests).
// The returns directory holds personal data, so it must lie outside the repository and be private to its owner.
// Requests whose Host is not this server (DNS rebinding) and POSTs from another origin are refused.
import { createServer, type IncomingMessage, type Server, type ServerResponse } from "node:http";
import type { Socket } from "node:net";
import { appendFileSync, existsSync, readFileSync, readdirSync, realpathSync, statSync, writeFileSync } from "node:fs";
import { join, relative, resolve, sep } from "node:path";
import { isDeepStrictEqual } from "node:util";
import { CANON_DIR, loadCanonical } from "./canonical.js";
import { applyAnswer, inputMeta, interviewView, loadInterview, questionTemplate, recordedTemplates, replay, replayState, withheldValues, type Event, type InterviewData, type JsonDerivation } from "./interview.js";
import { templateKey } from "./branches.js";
import { jointReturn, shownFor, spouseWording } from "./spouse-wording.js";
import { standingNotices, type SheetSection } from "./output.js";
import { formResolver, type FormEntry, type FormRef, type Purpose } from "./form-refs.js";
import type { CanonicalData } from "./types.js";
import { NOTE_MAX, VERDICTS_FILE, applyChange, judgedOf, loadVerdicts, stamp, vettingCards, vettingCounts, vettingState, writeVerdicts, type Card, type Verdict } from "./vetting.js";

export const PROFILE = "ny";
const ROOT = resolve(import.meta.dirname, "../..");
const NAME = /^[A-Za-z0-9][A-Za-z0-9_-]{0,63}$/;
const MAX_BODY = 1 << 20;

/** The checkouts a returns directory must not lie in: this one and, for a linked worktree, its main checkout. */
function repositoryRoots(): string[] {
  const roots = [realpathSync(ROOT)];
  const dotGit = join(ROOT, ".git");
  if (existsSync(dotGit) && statSync(dotGit).isFile()) {
    const m = readFileSync(dotGit, "utf8").match(/^gitdir:\s*(.+)$/m);
    const gitdir = m ? resolve(ROOT, m[1]!.trim()) : null;
    const at = gitdir ? gitdir.lastIndexOf(`${sep}.git${sep}worktrees${sep}`) : -1;
    if (gitdir && at >= 0 && existsSync(gitdir.slice(0, at))) roots.push(realpathSync(gitdir.slice(0, at)));
  }
  return roots;
}

/** The returns directory, resolved through symlinks. Throws when it is missing, lies inside the repository or is
 * accessible to its group or others. */
export function checkReturnsDir(dir: string): string {
  if (!existsSync(dir)) throw new Error(`${dir}: no such directory; create it with mkdir -m 700`);
  const real = realpathSync(dir);
  if (!statSync(real).isDirectory()) throw new Error(`${dir}: not a directory`);
  for (const root of repositoryRoots()) {
    if (real === root || real.startsWith(root + sep)) throw new Error(`${dir}: inside the repository (${root}); personal data must not be saved in the project`);
  }
  const mode = statSync(real).mode & 0o777;
  if (mode & 0o077) throw new Error(`${dir}: mode ${mode.toString(8)} lets others read it; use chmod 700`);
  return real;
}

/** Each source document's printed title and designation (the form, schedule or publication number as printed), by
 * id, from the year's source catalogs (tools/sources/<year>.json and tools/sources/ny/<year>.json;
 * tools/check_source_titles.py checks each against the archived document), and the entries that carry a designation,
 * with a form's quoted purpose where the catalog gives one. A document with none is absent. */
export function docNames(year: number): { titles: Record<string, string>; designations: Record<string, string>; forms: FormEntry[] } {
  const titles: Record<string, string> = {};
  const designations: Record<string, string> = {};
  const forms: FormEntry[] = [];
  for (const path of [join(ROOT, "tools", "sources", `${year}.json`), join(ROOT, "tools", "sources", "ny", `${year}.json`)]) {
    if (!existsSync(path)) continue;
    for (const e of JSON.parse(readFileSync(path, "utf8")) as { id: string; title?: string; designation?: string; form_purpose?: Purpose }[]) {
      if (e.title) titles[e.id] = e.title;
      if (e.designation) {
        designations[e.id] = e.designation;
        forms.push({ id: e.id, designation: e.designation, ...(e.title ? { title: e.title } : {}), ...(e.form_purpose ? { purpose: e.form_purpose } : {}) });
      }
    }
  }
  return { titles, designations, forms };
}

/** The forms each question names, by question input template, in order of first mention in its prompt, then its
 * help; a named form the catalogs do not hold has a null id. */
export function questionForms(config: InterviewData, forms: FormEntry[]): Map<string, FormRef[]> {
  const resolve = formResolver(forms);
  const out = new Map<string, FormRef[]>();
  for (const q of config.questions) if (!out.has(q.input)) out.set(q.input, resolve([q.prompt, q.help ?? ""]));
  return out;
}

/** The refusal gates that are consistency checks, by gate line, each with its explanation
 * (interview/<year>/conflict_checks.yaml, checked and written by the build); empty when the build wrote none. */
export function loadConflicts(dir: string = CANON_DIR): Record<string, string> {
  const path = join(dir, "conflicts.json");
  return existsSync(path) ? (JSON.parse(readFileSync(path, "utf8")) as { conflicts: Record<string, string> }).conflicts : {};
}

/** A figured line a conflict reads that stands for many answers, shown as the figure rather than every answer. */
const FIGURE_ABOVE = 6;

/** What a consistency check reads, from its derivation: the answered inputs among its operands, and through each
 * figured operand that rests on at most FIGURE_ABOVE answers, those answers; a figured operand resting on more, or on
 * none (a fixed amount), is listed as a figure. In order of first use; nothing is computed, only derivations read. */
export function conflictReads(values: Record<string, JsonDerivation>, gate: string, isAnswered: (key: string) => boolean): { inputs: string[]; figures: string[] } {
  const memo = new Map<string, string[]>();
  const reach = (key: string): string[] => {
    const known = memo.get(key);
    if (known) return known;
    memo.set(key, []);
    const d = values[key];
    let out: string[] = [];
    if (d?.op === "input") out = isAnswered(key) ? [key] : [];
    else if (d) out = [...new Set(d.operands.filter((o) => o.ref in values).flatMap((o) => reach(o.ref)))];
    memo.set(key, out);
    return out;
  };
  const inputs: string[] = [];
  const figures: string[] = [];
  for (const { ref } of values[gate]?.operands ?? []) {
    if (!(ref in values) || figures.includes(ref)) continue;
    if (values[ref]!.op === "input") { if (isAnswered(ref) && !inputs.includes(ref)) inputs.push(ref); continue; }
    const under = reach(ref);
    if (under.length === 0 || under.length > FIGURE_ABOVE) figures.push(ref);
    else for (const k of under) if (!inputs.includes(k)) inputs.push(k);
  }
  return { inputs, figures };
}

class HttpError extends Error { constructor(readonly status: number, message: string) { super(message); } }

/** Lines changed between two evaluations: the keys whose value differs or that only one of them has. */
function changedKeys(before: Record<string, { value: unknown }> | null, after: Record<string, { value: unknown }>): string[] {
  if (!before) return [];
  const keys = new Set([...Object.keys(before), ...Object.keys(after)]);
  return [...keys].filter((k) => !isDeepStrictEqual(before[k]?.value, after[k]?.value)).sort();
}

export function createApp(data: CanonicalData, config: InterviewData, dir: string, conflictChecks: Record<string, string> = loadConflicts(), verdictsFile: string = VERDICTS_FILE) {
  const names = docNames(config.tax_year);
  const lineById = new Map([...data.forms, ...data.defs].flatMap((d) => d.lines.map((l) => [l.id, l] as const)));
  const formsOf = questionForms(config, names.forms);
  const formsFor = (key: string) => (formsOf.get(questionTemplate(key)) ?? []).filter((f) => f.id !== null);
  const logPath = (name: string) => {
    if (!NAME.test(name)) throw new HttpError(400, "a return name is 1 to 64 letters, digits, '_' or '-', starting with a letter or digit");
    return join(dir, `${name}.jsonl`);
  };
  const readLog = (name: string): Event[] => {
    const path = logPath(name);
    if (!existsSync(path)) throw new HttpError(404, `no return named ${name}`);
    const events = readFileSync(path, "utf8").trim().split("\n").map((l) => JSON.parse(l) as Event);
    if ((events[0]?.profile ?? "social-security") !== PROFILE) throw new HttpError(400, "interview profile does not match log");
    return events;
  };

  /** The state the page shows: the interview view, each pending question with what its answer is, the answered
   * questions in the order first answered, the federal and New York sheets, and the lines the last answer changed.
   * The answered questions' prompts and help, and a conflict's figure labels, are reworded for the return's filing
   * status as the pending questions and the sheet's labels are (spouse-wording.ts), from the same answers, so
   * every list reads alike. */
  const state = (name: string, events: Event[], view: ReturnType<typeof interviewView>, previous: ReturnType<typeof interviewView> | null) => {
    const replayed = replayState(config, events);
    const inputs = replayed.inputs;
    const firstAnswered: string[] = [];
    for (const e of events.slice(1)) if (!firstAnswered.includes(e.input!)) firstAnswered.push(e.input!);
    const joint = jointReturn(inputs);
    const bankQuestion = (key: string) => config.questions.find((q) => q.input === questionTemplate(key));
    // The answers that go with a roster question's answer and have no question of their own: what its choice recorded,
    // and, on a log answered when they were asked, the answers given then. Each is shown under that question and is
    // changed by changing its answer.
    const neverAsked = recordedTemplates(config);
    const recorderOf = (key: string): string | undefined => replayed.recorded[key]?.by ?? (bankQuestion(key) ? undefined : neverAsked.get(questionTemplate(key)));
    const recordedBy = (roster: string) => Object.keys(inputs).filter((key) => recorderOf(key) === roster && inputs[key] !== null).map((key) => {
      const declared = config.questions.find((q) => q.input === roster)?.choices?.flatMap((c) => c.records ?? []).find((r) => r.input === key && r.value === inputs[key]);
      return { input: key, value: inputs[key], shown: replayed.recorded[key]?.shown ?? declared?.shown ?? `${key}: ${String(inputs[key])}` };
    });
    const answered = firstAnswered.filter((key) => key in inputs && bankQuestion(key) && !replayed.recorded[key]).map((key) => {
      const q = shownFor(bankQuestion(key)!, key, inputs);
      const withheld = withheldValues(config, inputs, key);
      const recorded = q.choices ? recordedBy(key) : [];
      return { input: key, value: inputs[key], prompt: q.prompt, help: q.help, order: q.order, cite: q.cite, ...(q.frame ? { frame: q.frame } : {}),
        ...(q.choices ? { choices: q.choices } : {}), ...(q.value_labels ? { value_labels: q.value_labels } : {}), ...(q.value_order ? { value_order: q.value_order } : {}),
        ...(withheld.length ? { withheld } : {}), ...(recorded.length ? { recorded } : {}), ...inputMeta(data, key), forms: formsFor(key) };
    });
    // Each listed entry's label, by entry path (`person[taxpayer].w2[acme_corp]`), from its roster's latest labelled answer.
    const entryLabels: Record<string, string> = {};
    for (const [rk, keys] of Object.entries(inputs)) {
      if (!rk.startsWith("$") || !Array.isArray(keys)) continue;
      const labels = events.findLast((e) => e.input === rk && e.labels)?.labels ?? {};
      const [coll, parent] = rk.slice(1).split("@") as [string, string | undefined];
      for (const k of keys as string[]) if (labels[k]) entryLabels[`${parent ? parent + "." : ""}${coll}[${k}]`] = labels[k];
    }
    // Each refusal among the values whose gate is a consistency check, as a conflict: its explanation, the answers
    // the gate reads (as the answered list gives them) and the figured lines it reads that stand for many answers.
    const conflicts = [...new Set(Object.values(view.values).flatMap((d) => d.value.kind === "refusal" && templateKey(d.value.gate) in conflictChecks ? [d.value.gate] : []))]
      .sort().map((gate) => {
        const reads = conflictReads(view.values, gate, (key) => inputs[key] !== undefined && inputs[key] !== null);
        return {
          gate, explanation: conflictChecks[templateKey(gate)]!,
          // An answer a choice recorded is changed through the question that recorded it.
          answers: [...new Set(reads.inputs.map((key) => recorderOf(key) ?? key))].flatMap((key) => answered.filter((a) => a.input === key)),
          figures: reads.figures.map((line) => {
            const l = lineById.get(templateKey(line));
            return { line, printed: l?.printed ?? "", label: l ? spouseWording(l.label, joint).split("\n")[0]! : line, value: view.values[line]!.value };
          }),
        };
      });
    const { sheet, ...rest } = view;
    const isNy = (s: SheetSection) => s.doc.startsWith("ny_");
    return {
      name, ...rest,
      pending: view.pending.map((q) => ({ ...q, ...inputMeta(data, q.input), forms: formsFor(q.input) })),
      refusalFinal: view.refusal !== null && view.pending.length === 0,
      conflicts,
      standingNotices: standingNotices(),
      sheets: { federal: sheet.sections.filter((s) => !isNy(s)), newYork: sheet.sections.filter(isNy) },
      answered,
      entryLabels,
      changed: changedKeys(previous?.values ?? null, view.values),
    };
  };

  const getState = (name: string) => {
    const events = readLog(name);
    const view = interviewView(data, config, replay(config, events));
    const previous = events.length > 1 ? interviewView(data, config, replay(config, events.slice(0, -1))) : null;
    return state(name, events, view, previous);
  };

  const blank = interviewView(data, config, replay(config, [{ version: 1, tax_year: config.tax_year }]));
  const api = (method: string, parts: string[], body: unknown): [number, unknown] => {
    if (parts.length === 0) {
      if (method === "GET") {
        return [200, { returns: readdirSync(dir).filter((f) => f.endsWith(".jsonl")).map((f) => f.slice(0, -6)).filter((n) => NAME.test(n)).sort(),
          scope: blank.scope, notices: blank.notices, standingNotices: standingNotices(), docTitles: names.titles, docDesignations: names.designations }];
      }
      if (method === "POST") {
        const name = (body as { name?: unknown } | null)?.name;
        if (typeof name !== "string") throw new HttpError(400, "POST /api/returns needs {name}");
        const path = logPath(name);
        try {
          writeFileSync(path, JSON.stringify({ version: 1, tax_year: config.tax_year, profile: PROFILE }) + "\n", { flag: "wx", mode: 0o600 });
        } catch (e) {
          if ((e as NodeJS.ErrnoException).code === "EEXIST") throw new HttpError(409, `a return named ${name} already exists`);
          throw e;
        }
        return [201, getState(name)];
      }
    } else if (parts.length === 1 && method === "GET") {
      return [200, getState(parts[0]!)];
    } else if (parts.length === 2 && parts[1] === "answer" && method === "POST") {
      const name = parts[0]!;
      const events = readLog(name);
      const b = body as { input?: unknown; value?: unknown; labels?: unknown } | null;
      if (!b || typeof b.input !== "string" || !("value" in b)) throw new HttpError(400, "an answer is {input, value} or, for a roster, {input, value, labels}");
      let applied;
      try { applied = applyAnswer(data, config, events, b.input, b.value, b.labels); }
      catch (e) { throw new HttpError(400, (e as Error).message); }
      appendFileSync(logPath(name), JSON.stringify(applied.event) + "\n");
      return [200, state(name, [...events, applied.event], applied.after, applied.before)];
    }
    throw new HttpError(404, "no such route");
  };

  // The vetting routes. The cards are built on first use; the verdict file is read on every request, so the page
  // always shows what the file holds, and a save changes one record of the file as it is then.
  let cards: Card[] | null = null;
  const vetting = (method: string, body: unknown): [number, unknown] => {
    cards ??= vettingCards(data, config);
    const shownFile = relative(ROOT, verdictsFile);
    if (method === "GET") {
      const state = vettingState(cards, loadVerdicts(verdictsFile, config.tax_year));
      return [200, { ...state, counts: vettingCounts(state), file: shownFile.startsWith("..") ? verdictsFile : shownFile }];
    }
    if (method !== "POST") throw new HttpError(405, "method not allowed");
    const b = body as { id?: unknown; digest?: unknown; verdict?: unknown; note?: unknown } | null;
    const verdict = b?.verdict, note = b?.note;
    if (!b || typeof b.id !== "string" || typeof b.digest !== "string" || (verdict === undefined && note === undefined)
      || (verdict !== undefined && verdict !== "up" && verdict !== "down" && verdict !== "none") || (note !== undefined && typeof note !== "string"))
      throw new HttpError(400, "a vetting change is {id, digest} with verdict (up, down or none), note, or both");
    if (typeof note === "string" && note.length > NOTE_MAX) throw new HttpError(400, `a note can be at most ${NOTE_MAX} characters`);
    const card = cards.find((c) => c.id === b.id);
    if (!card) throw new HttpError(404, `the interview has no question ${b.id}`);
    if (card.digest !== b.digest) throw new HttpError(409, `the wording of ${b.id} has changed since the page loaded it; reload the page`);
    const file = loadVerdicts(verdictsFile, config.tax_year);
    const judged = judgedOf(data, config.questions.find((q) => q.input === card.id)!);
    const record = applyChange(file, card.id, judged, { ...(verdict === undefined ? {} : { verdict: verdict as Verdict }), ...(typeof note === "string" ? { note } : {}) }, stamp());
    try { writeVerdicts(verdictsFile, file); }
    catch (e) { throw new HttpError(500, `not saved: ${(e as Error).message}`); }
    return [200, { id: card.id, record, stale: record !== null && record.digest !== card.digest, counts: vettingCounts(vettingState(cards, file)) }];
  };

  const statics: Record<string, [string, string]> = {
    "/": ["ui/index.html", "text/html; charset=utf-8"],
    "/app.js": ["ui/dist/app.js", "text/javascript; charset=utf-8"],
    "/text.js": ["ui/dist/text.js", "text/javascript; charset=utf-8"],
    "/style.css": ["ui/style.css", "text/css; charset=utf-8"],
    "/vet": ["ui/vet.html", "text/html; charset=utf-8"],
    "/vet.js": ["ui/dist/vet.js", "text/javascript; charset=utf-8"],
    "/vet.css": ["ui/vet.css", "text/css; charset=utf-8"],
  };

  return (req: IncomingMessage, res: ServerResponse, port: number): void => {
    const send = (status: number, type: string, payload: string | Buffer) => {
      res.writeHead(status, {
        "Content-Type": type, "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff", "Referrer-Policy": "no-referrer",
        "Content-Security-Policy": "default-src 'self'; frame-ancestors 'none'; form-action 'none'; base-uri 'none'",
      });
      res.end(payload);
    };
    const fail = (status: number, message: string) => send(status, "application/json; charset=utf-8", JSON.stringify({ error: message }));
    const host = req.headers.host ?? "";
    if (host !== `127.0.0.1:${port}` && host !== `localhost:${port}`) return fail(403, "unexpected Host");
    const method = req.method ?? "GET";
    if (method !== "GET" && req.headers.origin !== `http://${host}`) return fail(403, "cross-origin request refused");
    const url = new URL(req.url ?? "/", `http://${host}`);
    if (!url.pathname.startsWith("/api/")) {
      const file = statics[url.pathname];
      if (!file) return fail(404, "not found");
      if (method !== "GET") return fail(405, "method not allowed");
      try { return send(200, file[1], readFileSync(join(ROOT, file[0]))); }
      catch { return fail(500, `${file[0]} is missing; run npm run compile`); }
    }
    const forVetting = url.pathname === "/api/vetting";
    if (!forVetting && url.pathname !== "/api/returns" && !url.pathname.startsWith("/api/returns/")) return fail(404, "no such route");
    const chunks: Buffer[] = [];
    let size = 0;
    req.on("data", (c: Buffer) => { size += c.length; if (size <= MAX_BODY) chunks.push(c); });
    req.on("end", () => {
      try {
        if (size > MAX_BODY) throw new HttpError(413, "request too large");
        let parts: string[] = [];
        if (!forVetting) {
          try { parts = url.pathname.slice("/api/returns".length).split("/").filter(Boolean).map(decodeURIComponent); }
          catch { throw new HttpError(400, "malformed path"); }
        }
        let body: unknown = null;
        if (method === "POST") {
          try { body = JSON.parse(Buffer.concat(chunks).toString("utf8")); } catch { throw new HttpError(400, "the request body is not JSON"); }
        }
        const [status, payload] = forVetting ? vetting(method, body) : api(method, parts, body);
        send(status, "application/json; charset=utf-8", JSON.stringify(payload));
      } catch (e) {
        if (e instanceof HttpError) fail(e.status, e.message);
        else fail(500, (e as Error).message);
      }
    });
  };
}

/** `--log-connections` (for test-serve): one stderr line per event of each connection, keyed by the client's port
 * (`conn <client port> +<ms since accepted> <event>`): accepted, the request, the response's status, a socket error
 * or a client error, and the close. Also the server's timeouts at the start, and each stall of the event loop over
 * a second, which delays every connection. A test that meets a failed request reads these lines for its port. */
function logConnections(server: Server): void {
  const opened = new Map<number, number>();
  const say = (port: number | undefined, what: string) => {
    const t0 = port === undefined ? undefined : opened.get(port);
    console.error(`conn ${port ?? "?"} +${t0 === undefined ? "?" : Date.now() - t0}ms ${what}`);
  };
  console.error(`connections: headersTimeout ${server.headersTimeout} ms, requestTimeout ${server.requestTimeout} ms, keepAliveTimeout ${server.keepAliveTimeout} ms, timeout ${server.timeout} ms`);
  server.on("connection", (socket) => {
    const port = socket.remotePort;
    if (port !== undefined) opened.set(port, Date.now());
    say(port, "accepted");
    socket.on("error", (e: NodeJS.ErrnoException) => say(port, `socket error ${e.code ?? e.message}`));
    socket.on("close", (hadError) => say(port, `closed${hadError ? " after an error" : ""}`));
  });
  server.on("request", (req: IncomingMessage, res: ServerResponse) => {
    const port = req.socket.remotePort;
    say(port, `request ${req.method} ${req.url} (Connection: ${req.headers.connection ?? "-"})`);
    res.on("finish", () => say(port, `response ${res.statusCode} sent`));
    res.on("close", () => { if (!res.writableFinished) say(port, "response closed before it was sent"); });
  });
  // A listener replaces the default handling, which this repeats: a reset socket is destroyed, any other is answered 400.
  server.on("clientError", (e: NodeJS.ErrnoException, socket) => {
    say((socket as Socket).remotePort, `client error ${e.code ?? e.message}`);
    if (e.code === "ECONNRESET" || !socket.writable) socket.destroy();
    else socket.end("HTTP/1.1 400 Bad Request\r\nConnection: close\r\n\r\n");
  });
  let last = Date.now();
  setInterval(() => {
    const now = Date.now();
    if (now - last > 1500) console.error(`event loop stalled ${now - last - 500} ms`);
    last = now;
  }, 500).unref();
}

export async function runServe(args: string[]): Promise<void> {
  const arg = (name: string) => { const i = args.indexOf(name); return i < 0 ? undefined : args[i + 1]; };
  const dirArg = arg("--dir");
  if (!dirArg) throw new Error("serve requires --dir <returns directory> (outside the repository, mode 700)");
  const port = Number(arg("--port") ?? "8791");
  if (!Number.isInteger(port) || port < 0 || port > 65535) throw new Error("--port must be a port number");
  const dir = checkReturnsDir(resolve(dirArg));
  const vettingArg = arg("--vetting");
  const handler = createApp(loadCanonical(), loadInterview(PROFILE), dir, undefined, vettingArg === undefined ? undefined : resolve(vettingArg));
  const server = createServer((req, res) => handler(req, res, (server.address() as { port: number }).port));
  if (args.includes("--log-connections")) logConnections(server);
  await new Promise<void>((done, fail) => { server.once("error", fail); server.listen(port, "127.0.0.1", () => done()); });
  const actual = (server.address() as { port: number }).port;
  console.log(`serving http://127.0.0.1:${actual}/ (returns in ${dir}; profile ${PROFILE}; stop with Ctrl-C)`);
}
