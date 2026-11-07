// The web UI's server: `serve --dir <returns dir> [--port N]`. A local, single-user client of the interview, as the
// CLI is: each request replays a return's answer log with the `ny` profile (federal and New York) and answers go
// through `applyAnswer`. It serves the page in ui/ and a JSON API, on 127.0.0.1 only.
//
//   GET  /api/returns                 the return logs in the returns directory, and each source document's title
//   POST /api/returns {name}          starts a log <name>.jsonl (mode 0600; an existing name is refused)
//   GET  /api/returns/:name           the return's state
//   POST /api/returns/:name/answer {input, value[, labels]}
//                                     (labels: a roster answer's label for each entry key, kept in the log)
//                                     appends the answer and returns the new state, or 400 with the reason
//
// The returns directory holds personal data, so it must lie outside the repository and be private to its owner.
// Requests whose Host is not this server (DNS rebinding) and POSTs from another origin are refused.
import { createServer, type IncomingMessage, type ServerResponse } from "node:http";
import { appendFileSync, existsSync, readFileSync, readdirSync, realpathSync, statSync, writeFileSync } from "node:fs";
import { join, resolve, sep } from "node:path";
import { isDeepStrictEqual } from "node:util";
import { loadCanonical } from "./canonical.js";
import { applyAnswer, inputMeta, interviewView, loadInterview, questionTemplate, replay, type Event, type InterviewData } from "./interview.js";
import { standingNotices, type SheetSection } from "./output.js";
import type { CanonicalData } from "./types.js";

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

/** Each source document's printed title, by id, from the year's source catalogs (tools/sources-<year>.json and
 * tools/sources-ny-<year>.json; tools/check_source_titles.py checks each against the archived document). */
export function docTitles(year: number): Record<string, string> {
  const titles: Record<string, string> = {};
  for (const name of [`sources-${year}.json`, `sources-ny-${year}.json`]) {
    const path = join(ROOT, "tools", name);
    if (!existsSync(path)) continue;
    for (const e of JSON.parse(readFileSync(path, "utf8")) as { id: string; title?: string }[]) if (e.title) titles[e.id] = e.title;
  }
  return titles;
}

class HttpError extends Error { constructor(readonly status: number, message: string) { super(message); } }

/** Lines changed between two evaluations: the keys whose value differs or that only one of them has. */
function changedKeys(before: Record<string, { value: unknown }> | null, after: Record<string, { value: unknown }>): string[] {
  if (!before) return [];
  const keys = new Set([...Object.keys(before), ...Object.keys(after)]);
  return [...keys].filter((k) => !isDeepStrictEqual(before[k]?.value, after[k]?.value)).sort();
}

export function createApp(data: CanonicalData, config: InterviewData, dir: string) {
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
   * questions in the order first answered, the federal and New York sheets, and the lines the last answer changed. */
  const state = (name: string, events: Event[], view: ReturnType<typeof interviewView>, previous: ReturnType<typeof interviewView> | null) => {
    const inputs = replay(config, events);
    const firstAnswered: string[] = [];
    for (const e of events.slice(1)) if (!firstAnswered.includes(e.input!)) firstAnswered.push(e.input!);
    const question = (key: string) => config.questions.find((q) => q.input === questionTemplate(key))!;
    const answered = firstAnswered.filter((key) => key in inputs).map((key) => {
      const q = question(key);
      return { input: key, value: inputs[key], prompt: q.prompt, help: q.help, order: q.order, cite: q.cite,
        ...(q.choices ? { choices: q.choices } : {}), ...inputMeta(data, key) };
    });
    // Each listed entry's label, by entry path (`person[taxpayer].w2[acme_corp]`), from its roster's latest labelled answer.
    const entryLabels: Record<string, string> = {};
    for (const [rk, keys] of Object.entries(inputs)) {
      if (!rk.startsWith("$") || !Array.isArray(keys)) continue;
      const labels = events.findLast((e) => e.input === rk && e.labels)?.labels ?? {};
      const [coll, parent] = rk.slice(1).split("@") as [string, string | undefined];
      for (const k of keys as string[]) if (labels[k]) entryLabels[`${parent ? parent + "." : ""}${coll}[${k}]`] = labels[k];
    }
    const { sheet, ...rest } = view;
    const isNy = (s: SheetSection) => s.doc.startsWith("ny_");
    return {
      name, ...rest,
      pending: view.pending.map((q) => ({ ...q, ...inputMeta(data, q.input) })),
      refusalFinal: view.refusal !== null && view.pending.length === 0,
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
  const titles = docTitles(config.tax_year);
  const api = (method: string, parts: string[], body: unknown): [number, unknown] => {
    if (parts.length === 0) {
      if (method === "GET") {
        return [200, { returns: readdirSync(dir).filter((f) => f.endsWith(".jsonl")).map((f) => f.slice(0, -6)).filter((n) => NAME.test(n)).sort(),
          scope: blank.scope, notices: blank.notices, standingNotices: standingNotices(), docTitles: titles }];
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

  const statics: Record<string, [string, string]> = {
    "/": ["ui/index.html", "text/html; charset=utf-8"],
    "/app.js": ["ui/dist/app.js", "text/javascript; charset=utf-8"],
    "/style.css": ["ui/style.css", "text/css; charset=utf-8"],
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
    if (url.pathname !== "/api/returns" && !url.pathname.startsWith("/api/returns/")) return fail(404, "no such route");
    const chunks: Buffer[] = [];
    let size = 0;
    req.on("data", (c: Buffer) => { size += c.length; if (size <= MAX_BODY) chunks.push(c); });
    req.on("end", () => {
      try {
        if (size > MAX_BODY) throw new HttpError(413, "request too large");
        let parts: string[];
        try { parts = url.pathname.slice("/api/returns".length).split("/").filter(Boolean).map(decodeURIComponent); }
        catch { throw new HttpError(400, "malformed path"); }
        let body: unknown = null;
        if (method === "POST") {
          try { body = JSON.parse(Buffer.concat(chunks).toString("utf8")); } catch { throw new HttpError(400, "the request body is not JSON"); }
        }
        const [status, payload] = api(method, parts, body);
        send(status, "application/json; charset=utf-8", JSON.stringify(payload));
      } catch (e) {
        if (e instanceof HttpError) fail(e.status, e.message);
        else fail(500, (e as Error).message);
      }
    });
  };
}

export async function runServe(args: string[]): Promise<void> {
  const arg = (name: string) => { const i = args.indexOf(name); return i < 0 ? undefined : args[i + 1]; };
  const dirArg = arg("--dir");
  if (!dirArg) throw new Error("serve requires --dir <returns directory> (outside the repository, mode 700)");
  const port = Number(arg("--port") ?? "8791");
  if (!Number.isInteger(port) || port < 0 || port > 65535) throw new Error("--port must be a port number");
  const dir = checkReturnsDir(resolve(dirArg));
  const handler = createApp(loadCanonical(), loadInterview(PROFILE), dir);
  const server = createServer((req, res) => handler(req, res, (server.address() as { port: number }).port));
  await new Promise<void>((done, fail) => { server.once("error", fail); server.listen(port, "127.0.0.1", () => done()); });
  const actual = (server.address() as { port: number }).port;
  console.log(`serving http://127.0.0.1:${actual}/ (returns in ${dir}; profile ${PROFILE}; stop with Ctrl-C)`);
}
