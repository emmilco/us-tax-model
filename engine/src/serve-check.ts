// Tests of the web UI server (`serve`), on synthetic returns in temporary directories: the returns-directory
// refusals, file modes, the Host and Origin checks, that the server and the CLI give the same state on the same
// log, that a rejected answer appends nothing, roster removal and re-adding, a consistency check served as a
// conflict, the forms a question names and their quoted purposes, the spouse phrase reworded as the filing status is
// answered and corrected (questions, sheet labels and, on a constructed form, a conflict's figure labels), and fixture interview paths replayed through the server against the fixtures' expected
// values.
import assert from "node:assert/strict";
import { spawn, spawnSync, type ChildProcess } from "node:child_process";
import { chmodSync, mkdirSync, mkdtempSync, readFileSync, readdirSync, rmSync, statSync, symlinkSync, writeFileSync } from "node:fs";
import { createServer, request } from "node:http";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { isDeepStrictEqual } from "node:util";
import { loadCanonical } from "./canonical.js";
import { interviewView, loadInterview, questionTemplate, replay, type Event, type InterviewData } from "./interview.js";
import { SPOUSE_PHRASE, SPOUSE_POSSESSIVE, STATUS_INPUT, personWording, spouseWording, type JointReturn } from "./spouse-wording.js";
import { templateKey } from "./branches.js";
import { renderValuesSheetText } from "./output.js";
import { loadFixtureCases } from "./fixture-inputs.js";
import { YEAR_ARGS } from "./year.js";
import type { CanonicalData, Inputs } from "./types.js";
import { mapPool, poolSize } from "./pool.js";
import { createApp, docNames, questionForms } from "./serve.js";
import { formResolver, namedDesignations, type FormEntry } from "./form-refs.js";

const MAIN = resolve(import.meta.dirname, "main.js");
const ROOT = resolve(import.meta.dirname, "../..");

/** A started `serve` child: its returns directory, its output so far and, once it has exited, how. */
interface Server { proc: ChildProcess; port: number; dir: string; output: string; exit: string | null }
const servers = new Map<number, Server>();

/** What is known of the server on a port, for a failed request's message: its directory, whether it has exited, and
 * the end of its output. */
function serverContext(port: number): string {
  const s = servers.get(port);
  if (!s) return `no server started on port ${port}`;
  const tail = s.output.trim().split("\n").slice(-20).join("\n");
  return `server on port ${port} (pid ${s.proc.pid}, --dir ${s.dir}) ${s.exit ? `exited (${s.exit})` : "still running"}; its output:\n${tail}`;
}

interface Reply { status: number; body: any }
// Each request opens its own connection (agent: false). With a keep-alive agent a request may be sent on an idle
// connection the server has already closed (its keepAliveTimeout, 5 seconds, passed while this process was blocked
// in spawnSync), and the server answers it with a reset.
function http(port: number, method: string, path: string, opts: { host?: string; origin?: string | null; body?: unknown } = {}): Promise<Reply> {
  const host = opts.host ?? `127.0.0.1:${port}`;
  const origin = opts.origin === undefined ? (method === "GET" ? null : `http://${host}`) : opts.origin;
  const payload = opts.body === undefined ? undefined : JSON.stringify(opts.body);
  return new Promise((done, fail) => {
    const failed = (e: Error) => fail(new Error(`${method} ${path} (Host ${host}) failed: ${e.message}; ${serverContext(port)}`, { cause: e }));
    const req = request({ host: "127.0.0.1", port, method, path, agent: false, headers: { Host: host, ...(origin ? { Origin: origin } : {}), ...(payload ? { "Content-Type": "application/json" } : {}) } }, (res) => {
      const chunks: Buffer[] = [];
      res.on("data", (c: Buffer) => chunks.push(c));
      res.on("error", failed);
      res.on("end", () => {
        if (!res.complete) return failed(new Error("the connection closed before the response was complete"));
        const text = Buffer.concat(chunks).toString("utf8");
        let body: unknown = text;
        try { body = JSON.parse(text); } catch { /* a static file */ }
        done({ status: res.statusCode ?? 0, body });
      });
    });
    req.on("error", failed);
    req.end(payload);
  });
}

function startServer(dir: string): Promise<Server> {
  const proc = spawn(process.execPath, [MAIN, ...YEAR_ARGS, "serve", "--dir", dir, "--port", "0"], { stdio: ["ignore", "pipe", "pipe"] });
  const server: Server = { proc, port: 0, dir, output: "", exit: null };
  return new Promise((done, fail) => {
    proc.stdout!.on("data", (d: Buffer) => {
      server.output += d;
      const m = server.output.match(/http:\/\/127\.0\.0\.1:(\d+)\//);
      if (m && server.port === 0) { server.port = Number(m[1]); servers.set(server.port, server); done(server); }
    });
    proc.stderr!.on("data", (d: Buffer) => { server.output += d; });
    proc.on("error", (e) => { server.exit = `spawn error: ${e.message}`; fail(new Error(`server for ${dir} did not start: ${e.message}`)); });
    proc.on("exit", (code, signal) => {
      server.exit = signal ? `signal ${signal}` : `code ${code}`;
      fail(new Error(`server for ${dir} exited (${server.exit}) before it was serving: ${server.output}`));
    });
  });
}

export async function serveChecks(): Promise<void> {
  const tmp = mkdtempSync(join(tmpdir(), "serve-check-"));
  let server: ChildProcess | undefined;
  const extra: Promise<Server>[] = [];
  let checks = 0;
  const ok = (cond: unknown, message: string) => { assert.ok(cond, message); checks++; };
  try {
    // The returns directory: required, existing, outside the repository (through symlinks), private.
    const refuse = (args: string[], pattern: RegExp) => {
      const p = spawnSync(process.execPath, [MAIN, ...YEAR_ARGS, "serve", ...args, "--port", "0"], { encoding: "utf8", timeout: 60_000 });
      ok(p.status !== 0 && pattern.test(p.stderr), `serve ${args.join(" ")}: expected a refusal matching ${pattern}, got ${p.status}: ${p.stderr.slice(0, 300)}`);
    };
    refuse([], /requires --dir/);
    refuse(["--dir", join(tmp, "missing")], /no such directory/);
    refuse(["--dir", join(ROOT, "engine")], /inside the repository/);
    symlinkSync(ROOT, join(tmp, "link"));
    refuse(["--dir", join(tmp, "link")], /inside the repository/);
    for (const mode of [0o750, 0o705]) {
      const d = join(tmp, `open-${mode.toString(8)}`);
      mkdirSync(d); chmodSync(d, mode);
      refuse(["--dir", d], /lets others read it/);
      ok(readdirSync(d).length === 0, "a refused directory is left empty");
    }

    const dir = join(tmp, "returns");
    mkdirSync(dir, { mode: 0o700 });
    // The fixture walks at the end are independent of one another and of everything before them, so they are
    // spread over several servers (each with its own returns directory, on a port the system picks); the others
    // start now, while the checks on the first run.
    for (let i = 1; i < poolSize(); i++) {
      const d = join(tmp, `returns-${i}`);
      mkdirSync(d, { mode: 0o700 });
      const starting = startServer(d);
      starting.catch(() => {}); // a failed start is reported where the walks await it, not as an unhandled rejection
      extra.push(starting);
    }
    const started = await startServer(dir);
    server = started.proc;
    const port = started.port;
    const get = (path: string, host?: string) => http(port, "GET", path, host ? { host } : {});
    const post = (path: string, body: unknown, opts: { host?: string; origin?: string | null } = {}) => http(port, "POST", path, { ...opts, body });

    // Host and Origin.
    ok((await get("/api/returns", `evil.example:${port}`)).status === 403, "a request for another Host is refused");
    ok((await get("/api/returns", `127.0.0.1:${port + 1}`)).status === 403, "a request for another port is refused");
    ok((await get("/api/returns", `localhost:${port}`)).status === 200, "localhost:<port> is accepted");
    ok((await post("/api/returns", { name: "x" }, { origin: "http://evil.example" })).status === 403, "a POST from another origin is refused");
    ok((await post("/api/returns", { name: "x" }, { origin: null })).status === 403, "a POST without an Origin is refused");
    ok((await post("/api/returns", { name: "x" }, { host: `localhost:${port}`, origin: `http://127.0.0.1:${port}` })).status === 403, "a POST whose Origin is not its Host is refused");
    ok(readdirSync(dir).length === 0, "refused requests create nothing");
    const page = await get("/");
    ok(page.status === 200 && /<title>/.test(page.body as string), "the page is served");
    ok((await get("/app.js")).status === 200, "the script is served");

    // Creating a return: mode 0600 in a 0700 directory; never overwritten.
    ok((await post("/api/returns", { name: "../escape" })).status === 400, "a name with a path is refused");
    const created = await post("/api/returns", { name: "synthetic" });
    ok(created.status === 201 && created.body.status === "incomplete", `create: ${JSON.stringify(created.body).slice(0, 200)}`);
    const log = join(dir, "synthetic.jsonl");
    ok((statSync(log).mode & 0o777) === 0o600, `the log is mode 0600, not ${(statSync(log).mode & 0o777).toString(8)}`);
    ok((statSync(dir).mode & 0o777) === 0o700, "the returns directory is mode 0700");
    const header = readFileSync(log, "utf8");
    ok((await post("/api/returns", { name: "synthetic" })).status === 409 && readFileSync(log, "utf8") === header, "an existing return is not overwritten");
    const listing = (await get("/api/returns")).body;
    ok(isDeepStrictEqual(listing.returns, ["synthetic"]) && /New York/.test(listing.scope) && listing.standingNotices.length > 0, "the returns are listed, with the scope and notices");

    // The CLI and the server give the same state on the same log.
    const data = loadCanonical();
    const config = loadInterview("ny");
    // Every document a question cites has a title for the page to show as its source.
    const untitled = [...new Set(config.questions.map((q) => q.cite.doc))].filter((doc) => typeof listing.docTitles?.[doc] !== "string");
    ok(untitled.length === 0, `every cited document has a title in the source catalogs; missing: ${untitled.join(", ")}`);
    // A document's designation is served beside its title: a federal form and a New York form carry theirs; a statute has none.
    ok(listing.docDesignations?.f1040 === "Form 1040" && listing.docTitles.f1040 === "U.S. Individual Income Tax Return"
      && listing.docDesignations.ny_it201 === "Form IT-201" && listing.docDesignations["usc-26-72"] === undefined
      && Object.keys(listing.docDesignations).every((doc) => typeof listing.docTitles[doc] === "string"),
      "designations are served for the documents that print one, each with a title");

    // The forms a question names: read from its wording by designation, lists and parent forms included.
    const named = (text: string) => namedDesignations(text).map((d) => d.designation);
    ok(isDeepStrictEqual(named("Forms 1099-INT and 1099-OID, or Form 2555 or Form 4563"), ["Form 1099-INT", "Form 1099-OID", "Form 2555", "Form 4563"]), "a list of forms names each");
    ok(isDeepStrictEqual(named("Schedules C, E, and F (Form 1040 or 1040-SR), and Schedule A (Form 8971)"),
      ["Schedule C (Form 1040)", "Schedule E (Form 1040)", "Schedule F (Form 1040)", "Schedule A (Form 8971)"]), "a list of schedules takes its parent form");
    ok(isDeepStrictEqual(named("Form 1040, Filing Status; Form 2441, Part II; Form 1040 line 16; Pub. 501"), ["Form 1040", "Form 2441", "Form 1040"]), "words after a form are not form numbers");
    const nyNumbers = ["IT-214", "IT-112-R", "IT-360.1", "IT-201", "IT-201-I"];
    const bare = (text: string) => namedDesignations(text, nyNumbers).map((d) => d.designation);
    ok(isDeepStrictEqual(named("Form IT-360.1, Form IT-360 and Form 1040."), ["Form IT-360.1", "Form IT-360", "Form 1040"]), "a dotted form number is one number");
    ok(isDeepStrictEqual(bare("File IT-214 or IT-112-R; see IT-360.1, IT-201-I, IT-2, W-2, IT-2140, IT-360.15, IT-214A, XIT-214."),
      ["Form IT-214", "Form IT-112-R", "Form IT-360.1", "Form IT-201-I"]), `a New York designation is found without "Form" only where catalogued: ${bare("File IT-214 or IT-112-R; see IT-360.1, IT-201-I, IT-2, W-2, IT-2140, IT-360.15, IT-214A, XIT-214.")}`);
    const entry = (id: string, designation: string): FormEntry => ({ id, designation });
    const resolve = formResolver([entry("a", "IT-214"), entry("b", "IT-112-R"), entry("c", "Form IT-360.1"), entry("d", "Form 1040"), entry("e", "SSA-1099")]);
    ok(isDeepStrictEqual(resolve(["Claim Form IT-214, IT-112-R and Form IT-360.1 (not IT-360), W-2, SSA-1099"]).map((r) => `${r.designation}=${r.id}`),
      ["IT-214=a", "IT-112-R=b", "Form IT-360.1=c"]), "a bare or dotted New York number resolves to its catalog entry; an uncatalogued bare number is not read as a form");
    const names = docNames(config.tax_year);
    const byQuestion = questionForms(config, names.forms);
    const formsOf = (input: string) => byQuestion.get(input)!.map((f) => `${f.designation}${f.id === null ? "?" : f.purpose ? "+" : ""}`);
    ok(isDeepStrictEqual(formsOf("scope.other_line16"), ["Form 1040", "Form 8814+", "Form 8615+", "Form 8621", "Form 8960+", "Form 4972+", "Form 8978+", "Schedule J (Form 1040)+"]),
      `scope.other_line16 names Schedule J (resolved to Schedule J (Form 1040)), Form 8621, held without a purpose, and Forms 8814 and 8960, glossed: ${formsOf("scope.other_line16")}`);
    ok(isDeepStrictEqual(formsOf("interest.penalty"), ["Form 1099-INT+", "Form 1099-OID+", "Schedule 1 (Form 1040)+"]), `a bare "Schedule 1" is Schedule 1 (Form 1040), the catalogs' only Schedule 1: ${formsOf("interest.penalty")}`);
    ok(formsOf("gift.special").includes("Schedule K-1?"), "a bare Schedule K-1, of three parent forms in the catalogs, stays unresolved");
    ok(isDeepStrictEqual(formsOf("ny_it2.state_withheld"), ["Form W-2", "Form IT-2+"]), `a New York question names Form W-2 and Form IT-2: ${formsOf("ny_it2.state_withheld")}`);
    // As served: only the forms the catalogs hold, each purpose the catalog's own.
    type Served = { designation: string; id: string; title?: string; purpose?: { text: string; doc: string; page: number } };
    const catalogEntry = (id: string) => names.forms.find((f) => f.id === id)!;
    ok(created.body.pending[0].input === "$person" && isDeepStrictEqual(created.body.pending[0].forms, []), "the first question, in plain words, names no form");
    const naming = created.body.pending.find((q: any) => q.input === "$f1095a");
    const namedForms = (naming?.forms ?? []) as Served[];
    ok(isDeepStrictEqual(namedForms.map((f) => f.id), ["f1095a"]) && namedForms[0]!.title === catalogEntry("f1095a").title && typeof namedForms[0]!.title === "string"
      && namedForms[0]!.purpose !== undefined && namedForms.every((f) => isDeepStrictEqual(f.purpose, catalogEntry(f.id).purpose)),
      `a question's forms are served with their titles and purposes: ${JSON.stringify(namedForms).slice(0, 300)}`);
    ok(created.body.pending.every((q: any) => Array.isArray(q.forms) && q.forms.every((f: any) => typeof f.id === "string")), "every pending question carries its catalogued forms");
    const cli = (args: string[], expectOk = true) => {
      const p = spawnSync(process.execPath, [MAIN, ...YEAR_ARGS, "interview", ...args, "--log", log], { encoding: "utf8", maxBuffer: 256 * 1024 * 1024 });
      assert.equal(p.status === 0, expectOk, `interview ${args.join(" ")}: ${p.stderr}`);
      return expectOk ? JSON.parse(p.stdout) : null;
    };
    const same = (served: any, label: string) => {
      const c = cli(["advance"]);
      for (const k of ["status", "refusal", "question", "reachableInputs", "scope", "notices", "values"]) ok(isDeepStrictEqual(served[k], c[k]), `${label}: ${k} differs between the server and the CLI`);
      const pending = served.pending.map(({ type: _t, values: _v, forms: _f, ...q }: any) => q);
      ok(isDeepStrictEqual(pending, c.pending), `${label}: pending differs between the server and the CLI`);
      const hints: Record<string, RegExp> = { Bool: /^true or false/, NonNegDollars: /^integer cents/, Dollars: /^integer cents, negative/, Count: /^a whole number/,
        Enum: /^one of: "/, Roster: /^(?:one of: \[|a JSON list of distinct entry keys)/ };
      ok(served.pending.every((q: any) => hints[q.type]!.test(q.entry) && /null asks for help$/.test(q.entry)), `${label}: the CLI's entry hint matches each input's type`);
      const events = readFileSync(log, "utf8").trim().split("\n").map((l) => JSON.parse(l) as Event);
      const view = interviewView(data, config, replay(config, events));
      ok(renderValuesSheetText(view.sheet) === c.sheet, `${label}: the structured sheet does not render to the CLI's text sheet`);
      const sections = JSON.parse(JSON.stringify(view.sheet.sections)) as typeof view.sheet.sections; // as served
      ok(isDeepStrictEqual([...served.sheets.federal, ...served.sheets.newYork], [...sections.filter((s) => !s.doc.startsWith("ny_")), ...sections.filter((s) => s.doc.startsWith("ny_"))]), `${label}: the served sheets are not the engine's sections`);
      ok(served.sheets.newYork.every((s: any) => s.doc.startsWith("ny_")) && served.sheets.federal.every((s: any) => !s.doc.startsWith("ny_")), `${label}: sheets split by jurisdiction`);
    };
    same(created.body, "new return");

    const nyCases = loadFixtureCases("ny", data).filter((c) => c.file === "it201.json");
    const federal = loadFixtureCases("federal", data);
    const answer = (name: string, input: string, value: unknown) => post(`/api/returns/${name}/answer`, { input, value });
    const unchanged = async (name: string, input: unknown, value: unknown, label: string, body?: unknown) => {
      const before = readFileSync(join(dir, `${name}.jsonl`), "utf8");
      const r = await post(`/api/returns/${name}/answer`, body ?? { input, value });
      ok(r.status === 400 && typeof r.body.error === "string", `${label}: expected 400, got ${r.status}`);
      ok(readFileSync(join(dir, `${name}.jsonl`), "utf8") === before, `${label}: a rejected answer changed the log`);
      return r.body.error as string;
    };

    // A synthetic New York return refused part-year: a help request, rejected answers, a provisional refusal that
    // becomes final once nothing is pending, and roster removal and re-adding.
    const base = nyCases.find((c) => c.id === "ny.refuse.part_year_state")!;
    let state = created.body;
    const first = state.pending[0].input;
    ok(first === "$person" && state.pending[0].type === "Roster", `the first question is the person roster, not ${first}`);
    ok(isDeepStrictEqual(state.pending[0].choices.map((c: any) => c.value), [["taxpayer"], ["taxpayer", "spouse"]]), "the person roster is a selector of two choices");
    ok(/^one of: \["taxpayer"\] \(Just me\)/.test(state.pending[0].entry), `the person roster's entry hint: ${state.pending[0].entry}`);
    state = (await answer("synthetic", first, null)).body;
    ok(state.pending[0].input === first && state.pending[0].helpRequested === true, "a help request leaves the question pending, marked");
    same(state, "help request");
    // Labels: only on a roster answer, one non-empty label for each listed entry.
    const labelled = (input: string, value: unknown, labels: unknown) => post("/api/returns/synthetic/answer", { input, value, labels });
    for (const [labels, what] of [[{}, "a missing label"], [{ taxpayer: " " }, "a blank label"], [{ taxpayer: "You", spouse: "x" }, "a label for an unlisted entry"], [["You"], "labels as a list"]] as const) {
      const before = readFileSync(log, "utf8");
      ok((await labelled("$person", ["taxpayer"], labels)).status === 400 && readFileSync(log, "utf8") === before, `${what} is refused and writes nothing`);
    }
    const choice = state.pending[0].choices[0];
    state = (await labelled("$person", choice.value, choice.labels)).body;
    ok(state.entryLabels["person[taxpayer]"] === "You", "the chosen answer's labels name the entry");
    ok(JSON.parse(readFileSync(log, "utf8").trim().split("\n").at(-1)!).labels?.taxpayer === "You", "the labels are saved on the roster answer's event");
    same(state, "person chosen with labels");
    await unchanged("synthetic", "$person", ["taxpayer", "taxpayer"], "duplicate roster keys");
    await unchanged("synthetic", "$person", ["tax payer"], "a roster key outside the key pattern");
    await unchanged("synthetic", "f1040.line1a", 100, "an unreachable input");
    await unchanged("synthetic", "no.such_input", 1, "an undeclared input");
    await unchanged("synthetic", undefined, undefined, "an answer without a value", { input: "$person" });
    let sawProvisional = false, steps = 0, checkedMid = false;
    for (;;) {
      const q = state.pending.find((p: any) => p.input in base.inputs && !state.answered.some((a: any) => a.input === p.input && a.value !== null));
      if (!q) break;
      if (q.type === "NonNegDollars" && !checkedMid) {
        await unchanged("synthetic", q.input, -1, "a negative amount");
        await unchanged("synthetic", q.input, 12.5, "a fractional amount");
        await unchanged("synthetic", q.input, "100", "an amount as text");
        checkedMid = true;
      }
      if (q.type === "Bool") ok(typeof base.inputs[q.input] === "boolean", `${q.input}: Bool metadata`);
      if (q.type === "Enum") ok(q.values.includes(base.inputs[q.input]), `${q.input}: the enum values include the answer`);
      const v = base.inputs[q.input];
      const r = q.type === "Roster" && Array.isArray(v)
        ? await labelled(q.input, v, Object.fromEntries((v as string[]).map((k, i) => [k, i === 0 ? "Acme Corp" : `Acme Corp ${i + 1}`])))
        : await answer("synthetic", q.input, v);
      assert.equal(r.status, 200, `${q.input}: ${JSON.stringify(r.body)}`);
      state = r.body;
      if (state.status === "refused" && state.pending.length > 0) {
        if (!sawProvisional) same(state, "provisional refusal");
        ok(state.refusalFinal === false, "a refusal with questions pending is provisional");
        sawProvisional = true;
      }
      assert.ok(++steps < 400, "the walk did not end");
    }
    ok(sawProvisional, "the walk passed a provisional refusal");
    ok(state.entryLabels["person[taxpayer].w2[emp_a]"] === "Acme Corp" && state.entryLabels["person[taxpayer].w2[emp_b]"] === "Acme Corp 2", "roster labels name their entries");
    ok(state.status === "refused" && state.pending.length === 0 && state.refusalFinal === true, `the refusal is final when nothing is pending (${state.status}, ${state.pending.length} pending)`);
    ok(state.refusal.gate === "ny_it201.gate.part_year_state", `refusal gate ${state.refusal.gate}`);
    same(state, "final refusal");
    for (const [key, expected] of Object.entries(base.expect ?? {})) if (key in state.values) ok(isDeepStrictEqual(state.values[key].value, expected), `${base.id}: ${key}`);

    // Corrections: clearing the refusal; then a roster entry removed and re-added, as the CLI does.
    const gate = "ny_it201.ask.state_resident";
    ok(base.inputs[gate] === false, "the synthetic return is refused as not a full-year resident");
    state = (await answer("synthetic", gate, true)).body;
    ok(state.status !== "refused" || state.refusal.gate !== "ny_it201.gate.part_year_state", "correcting the answer clears the refusal");
    const roster = "$w2@person[taxpayer]";
    const entries = base.inputs[roster] as string[];
    ok(entries.length >= 2, "the synthetic return has two employers");
    const full = state.values;
    state = (await answer("synthetic", roster, entries.slice(0, 1))).body;
    ok(!isDeepStrictEqual(state.values["f1040.line1a"], full["f1040.line1a"]), "removing an employer changes line 1a");
    ok(!state.answered.some((a: any) => a.input.includes(`w2[${entries[1]}]`)), "a removed entry's answers are inactive");
    same(state, "roster entry removed");
    state = (await answer("synthetic", roster, entries)).body;
    ok(isDeepStrictEqual(state.values, full), "re-adding the entry restores its answers");
    ok(state.changed.includes("f1040.line1a"), "the lines the answer changed are listed");
    same(state, "roster entry re-added");
    const reloaded = (await get("/api/returns/synthetic")).body;
    ok(isDeepStrictEqual(reloaded.changed, state.changed) && isDeepStrictEqual(reloaded.values, state.values), "a reload gives the same state and changed lines");
    // An answer written by the CLI is read by the server.
    cli(["answer", "--input", gate, "--value", "false"]);
    ok((await get("/api/returns/synthetic")).body.refusal?.gate === "ny_it201.gate.part_year_state", "the server reads the CLI's answer");
    cli(["answer", "--input", gate, "--value", "\"yes\""], false);

    // A consistency check is served as a conflict, not as an unsupported case: Form 8889 with self-only coverage on
    // December 1 and every eligible month a family month (stage11.hsa.self_full_year, its month answers changed).
    const hsaCase = federal.find((c) => c.id === "stage11.hsa.self_full_year")!;
    const hsa = "person[taxpayer].f8889[hsa].";
    const hsaInputs: Inputs = { ...hsaCase.inputs, [`${hsa}dec_coverage`]: "self_only", [`${hsa}months_eligible`]: 12, [`${hsa}months_family`]: 12 };
    writeFileSync(join(dir, "conflict.jsonl"), [{ version: 1, tax_year: config.tax_year, profile: "ny" }, ...Object.entries(hsaInputs).map(([input, value]) => ({ input, value }))]
      .map((e) => JSON.stringify(e)).join("\n") + "\n", { mode: 0o600 });
    const conflicted = (await get("/api/returns/conflict")).body;
    ok(conflicted.status === "refused" && conflicted.refusal?.gate === `${hsa}bad_months`, `the conflicting month answers refuse at the consistency check: ${JSON.stringify(conflicted.refusal).slice(0, 200)}`);
    const conflict = conflicted.conflicts?.find((c: any) => c.gate === `${hsa}bad_months`);
    ok(conflict && /month counts and the December 1 coverage do not fit together/.test(conflict.explanation) && !/cannot prepare/.test(conflict.explanation),
      `the refusal is served as a conflict with its explanation: ${JSON.stringify(conflicted.conflicts).slice(0, 300)}`);
    ok(isDeepStrictEqual(conflict.answers.map((a: any) => a.input).sort(), ["coverage_year", "dec_coverage", "months_eligible", "months_family"].map((k) => hsa + k))
      && conflict.answers.every((a: any) => a.value === hsaInputs[a.input] && typeof a.prompt === "string" && a.prompt !== "") && conflict.figures.length === 0,
      `the conflict names the four answers it reads (the coverage answer that asks for the months, and the months), with their answers and prompts: ${JSON.stringify(conflict.answers.map((a: any) => [a.input, a.value]))}`);
    ok((await get("/api/returns/synthetic")).body.conflicts.length === 0, "a scope refusal is not a conflict");

    // The spouse phrase is reworded for the return's filing status wherever question text is served (the next
    // question, the pending and answered lists; prompt and help), from the answers of that response: the stored
    // text while the status is unanswered, the joint reading once it is married filing jointly, the plain reading
    // once it is corrected to single. The log holds answers only, so nothing reworded is saved.
    const storedText = new Map<string, { prompt: string; help: string }>();
    for (const q of config.questions) if (!storedText.has(q.input)) storedText.set(q.input, q);
    const storedFor = (input: string) => storedText.get(questionTemplate(input))!;
    const phrased = (text: string) => text.includes(SPOUSE_PHRASE) || text.includes(SPOUSE_POSSESSIVE);
    /** Every question the state serves reads as its stored text reworded for `joint`; returns how many carry the phrase. */
    const servedAs = (s: any, joint: JointReturn, label: string): number => {
      const listed = [...s.pending, ...s.answered, ...(s.question ? [s.question] : [])];
      for (const q of listed) {
        assert.equal(q.prompt, spouseWording(storedFor(q.input).prompt, joint), `${label}: ${q.input} prompt`);
        assert.equal(q.help, spouseWording(storedFor(q.input).help, joint), `${label}: ${q.input} help`);
      }
      return listed.filter((q) => phrased(storedFor(q.input).prompt) || phrased(storedFor(q.input).help)).length;
    };
    // The sheet's line labels are reworded the same way: each served label is its form line's label reworded.
    const storedLabel = new Map(data.forms.flatMap((d) => d.lines.map((l) => [l.id, l.label] as const)));
    const sheetLines = (s: any): any[] => [...s.sheets.federal, ...s.sheets.newYork].flatMap((sec: any) => sec.lines);
    const labelsAs = (s: any, joint: JointReturn, label: string): number => {
      for (const l of sheetLines(s)) assert.equal(l.label, spouseWording(storedLabel.get(templateKey(l.key))!, joint), `${label}: the sheet label of ${l.key}`);
      return sheetLines(s).filter((l) => phrased(storedLabel.get(templateKey(l.key))!)).length;
    };
    let wording = (await post("/api/returns", { name: "wording" })).body;
    const once = wording.pending.find((q: any) => q.type === "Bool" && q.prompt.includes(SPOUSE_PHRASE));
    const possessive = wording.pending.find((q: any) => q.prompt.includes(SPOUSE_POSSESSIVE));
    const helped = wording.pending.find((q: any) => phrased(q.help));
    ok(once && possessive && helped && wording.pending.some((q: any) => q.input === STATUS_INPUT),
      "a new return has the filing status and spouse-phrased questions pending (both forms of the phrase, and one in a help text)");
    const shown = (s: any, input: string): string => { const q = [...s.pending, ...s.answered].find((x: any) => x.input === input); return `${q.prompt}\n${q.help}`; };
    const readings = new Map<string, Set<string>>([once, possessive, helped].map((q: any) => [q.input, new Set<string>()]));
    const read = (s: any) => { for (const [input, texts] of readings) texts.add(shown(s, input)); };
    ok(servedAs(wording, "unknown", "status unanswered") > 0 && once.prompt === storedFor(once.input).prompt, "with the filing status unanswered the stored text is served");
    read(wording);
    const sheetLine = sheetLines(wording).find((l) => l.label.includes(SPOUSE_PHRASE));
    ok(sheetLine && labelsAs(wording, "unknown", "status unanswered") > 0, "with the filing status unanswered the sheet shows a spouse-phrased label as stored");
    const labelReadings = new Set<string>([sheetLine.label]);
    const labelNow = (s: any): string => sheetLines(s).find((l) => l.key === sheetLine.key).label;
    wording = (await answer("wording", STATUS_INPUT, null)).body;
    ok(servedAs(wording, "unknown", "status help requested") > 0, "a help request on the filing status leaves the stored text");
    wording = (await answer("wording", STATUS_INPUT, "mfj")).body;
    ok(servedAs(wording, "joint", "status mfj") > 0 && shown(wording, once.input).includes("you or your spouse") && !phrased(shown(wording, once.input)),
      `married filing jointly serves the joint reading: ${shown(wording, once.input).slice(0, 200)}`);
    ok(shown(wording, possessive.input).includes("your or your spouse's"), `the possessive form's joint reading: ${shown(wording, possessive.input).slice(0, 200)}`);
    read(wording);
    ok(labelsAs(wording, "joint", "status mfj") > 0 && labelNow(wording) === sheetLine.label.replaceAll(SPOUSE_PHRASE, " or your spouse"), `the sheet label's joint reading: ${labelNow(wording).slice(0, 160)}`);
    labelReadings.add(labelNow(wording));
    wording = (await answer("wording", once.input, false)).body;
    ok(wording.answered.some((a: any) => a.input === once.input && a.prompt === spouseWording(storedFor(once.input).prompt, "joint")), "an answered question is listed in the joint reading");
    ok(isDeepStrictEqual((await get("/api/returns/wording")).body.answered, wording.answered), "a reload serves the same reading");
    wording = (await answer("wording", STATUS_INPUT, "single")).body;
    ok(servedAs(wording, "not-joint", "status single") > 0, "a corrected filing status serves the plain reading in every list");
    ok(wording.answered.some((a: any) => a.input === once.input && a.prompt === storedFor(once.input).prompt.replaceAll(SPOUSE_PHRASE, "")), "the answered question is re-read without the phrase");
    read(wording);
    ok(labelsAs(wording, "not-joint", "status single") > 0 && labelNow(wording) === sheetLine.label.replaceAll(SPOUSE_PHRASE, ""), `the sheet label's plain reading: ${labelNow(wording).slice(0, 160)}`);
    labelReadings.add(labelNow(wording));
    ok(labelReadings.size === 3, `the sheet label of ${sheetLine.key} read three ways (stored, joint, plain)`);
    ok([...readings.values()].every((texts) => texts.size === 3), `each question read three ways (stored, joint, plain): ${[...readings].map(([k, texts]) => `${k} ${texts.size}`).join(", ")}`);
    const wordingLog = readFileSync(join(dir, "wording.jsonl"), "utf8").trim().split("\n").map((l) => JSON.parse(l) as Record<string, unknown>);
    ok(wordingLog.slice(1).every((e) => isDeepStrictEqual(Object.keys(e).sort(), ["input", "value"])), "the log holds each answer's input and value, and no question text");

    // A conflict's figures carry line labels, reworded like the sheet's. No built consistency check reads a figured
    // line whose label carries the phrase, so this one is constructed: a small form served in this process, whose
    // check reads an answer and a fixed limit labelled with the phrase.
    const figureLabel = "Limit for you (or, on a joint return, your spouse) and your (or, on a joint return, your spouse's) dependents";
    const probeLine = (id: string, type: string, expr: object, extra: object = {}) => ({ id: `f1040.${id}`, printed: id, label: id, type, expr, cite: null, ...extra });
    const probeData = {
      forms: [{ id: "f1040", kind: "form", tax_year: config.tax_year, title: "Conflict figure test", lines: [
        probeLine("status", "Enum(filing_status)", { op: "input", source: "Filing status" }),
        probeLine("amount", "NonNegDollars", { op: "input", source: "Amount" }),
        probeLine("limit", "NonNegDollars", { op: "param", ref: "limit" }, { label: figureLabel }),
        probeLine("bad", "Bool", { op: "test", gt: ["f1040.amount", "f1040.limit"] }),
        probeLine("result", "NonNegDollars", { op: "copy", ref: "f1040.amount" }, { refuses: [{ when: "f1040.bad", form: "Amount over the limit", remedy: "Correct the amount", cite: null }] }),
      ] }],
      defs: [], tables: [], register: { entries: [] },
      params: { values: { limit: { type: "NonNegDollars", value: 100 } }, enums: { filing_status: data.params.enums["filing_status"]! } },
    } as unknown as CanonicalData;
    const probeConfig = { tax_year: config.tax_year, targets: ["f1040.result"], initial: {}, cite: null,
      questions: ["status", "amount"].map((id, order) => ({ input: `f1040.${id}`, prompt: id, help: "", order, cite: null })) } as unknown as InterviewData;
    const probeDir = join(tmp, "returns-figures");
    mkdirSync(probeDir, { mode: 0o700 });
    const probeApp = createApp(probeData, probeConfig, probeDir, { "f1040.bad": "The amount is more than the limit." });
    const probeServer = createServer((req, res) => probeApp(req, res, (probeServer.address() as { port: number }).port));
    await new Promise<void>((done) => probeServer.listen(0, "127.0.0.1", () => done()));
    try {
      const probePort = (probeServer.address() as { port: number }).port;
      const figureAs = async (name: string, status: string | null): Promise<any> => {
        const events = [{ version: 1, tax_year: config.tax_year, profile: "ny" }, { input: "f1040.amount", value: 200 }, ...(status ? [{ input: STATUS_INPUT, value: status }] : [])];
        writeFileSync(join(probeDir, `${name}.jsonl`), events.map((e) => JSON.stringify(e)).join("\n") + "\n", { mode: 0o600 });
        const s = (await http(probePort, "GET", `/api/returns/${name}`)).body;
        assert.equal(s.conflicts?.length, 1, `${name}: one conflict expected: ${JSON.stringify(s).slice(0, 300)}`);
        assert.deepEqual(s.conflicts[0].answers.map((a: any) => a.input), ["f1040.amount"], `${name}: the conflict's answers`);
        assert.equal(s.conflicts[0].figures.length, 1, `${name}: one figure expected`);
        return s.conflicts[0].figures[0];
      };
      const asStored = await figureAs("unanswered", null), asJoint = await figureAs("joint", "mfj"), asPlain = await figureAs("plain", "single");
      ok(asStored.line === "f1040.limit" && asStored.label === figureLabel, `a conflict's figure label is served as stored while the filing status is unanswered: ${asStored.label}`);
      ok(asJoint.label === "Limit for you or your spouse and your or your spouse's dependents", `a conflict's figure label in the joint reading: ${asJoint.label}`);
      ok(asPlain.label === "Limit for you and your dependents", `a conflict's figure label in the plain reading: ${asPlain.label}`);
    } finally { probeServer.close(); }

    // The opening. A couple answers one question: the choice records both roles and the joint status, the answered
    // list shows them under that answer, and they are changed only through it.
    const FRAME = "For this person (you, or your spouse on a joint return)";
    let opening = (await post("/api/returns", { name: "opening" })).body;
    const openingLog = join(dir, "opening.jsonl");
    const lastEvent = () => JSON.parse(readFileSync(openingLog, "utf8").trim().split("\n").at(-1)!) as { input: string; value: unknown; labels?: unknown; records?: { input: string; value: unknown; shown: string }[] };
    // The server and the command-line interview read the same log alike: the questions as shown, the refusal and its note,
    // and the recorded answers.
    const sameOpening = (served: any, label: string) => {
      const p = spawnSync(process.execPath, [MAIN, ...YEAR_ARGS, "interview", "advance", "--log", openingLog], { encoding: "utf8", maxBuffer: 256 * 1024 * 1024 });
      assert.equal(p.status, 0, `interview advance on the opening log: ${p.stderr}`);
      const c = JSON.parse(p.stdout);
      for (const k of ["status", "refusal", "refusalNote", "question", "reachableInputs", "values"]) ok(isDeepStrictEqual(served[k], c[k]), `${label}: ${k} differs between the server and the CLI`);
      ok(isDeepStrictEqual(served.pending.map(({ type: _t, values: _v, forms: _f, ...q }: any) => q), c.pending), `${label}: pending differs between the server and the CLI`);
      ok(isDeepStrictEqual(served.answered.flatMap((a: any) => (a.recorded ?? []).map((r: any) => ({ ...r, by: a.input }))).sort((a: any, b: any) => a.input.localeCompare(b.input)), c.recorded.map(({ input, value, by, shown }: any) => ({ input, value, shown, by }))),
        `${label}: the recorded answers differ between the server and the CLI: ${JSON.stringify(c.recorded)}`);
    };
    const person = opening.pending[0];
    ok(person.input === "$person" && person.prompt === "Who is this tax return for?" && isDeepStrictEqual(person.choices.map((c: any) => c.label), ["Just me", "Me and my husband or wife, together on one return"]),
      `the first question and its two choices: ${person.prompt} ${JSON.stringify(person.choices.map((c: any) => c.label))}`);
    ok(/the answer is one of/.test(await unchanged("opening", "$person", ["taxpayer", "second"], "a roster answer that is not a declared choice")), "a roster answer that is not a choice is refused with the choices");
    opening = (await post("/api/returns/opening/answer", { input: "$person", value: person.choices[1].value, labels: person.choices[1].labels })).body;
    ok(isDeepStrictEqual(lastEvent().records?.map((r) => [r.input, r.value]), [["person[taxpayer].role", "taxpayer"], ["person[spouse].role", "spouse"], ["f1040.status", "mfj"]]) && lastEvent().labels !== undefined,
      "the couple's choice is saved with its labels and the answers it records");
    ok(opening.answered.length === 1 && isDeepStrictEqual(opening.answered[0].recorded.map((r: any) => r.input), ["person[taxpayer].role", "person[spouse].role", "f1040.status"])
      && opening.answered[0].recorded.every((r: any) => typeof r.shown === "string" && r.shown !== ""), `the answered list shows what the choice recorded under it: ${JSON.stringify(opening.answered[0].recorded)}`);
    ok(!opening.pending.some((q: any) => q.input === STATUS_INPUT || q.input.endsWith(".role")), "a couple is asked neither the filing status nor a role");
    ok(opening.values[STATUS_INPUT].value.value === "mfj", "the joint status is on the return");
    for (const [key, value] of [[STATUS_INPUT, "single"], ["person[spouse].role", "taxpayer"]] as const) {
      ok(/was recorded by the answer to \$person .*change that answer to change it/.test(await unchanged("opening", key, value, `a direct answer to the recorded ${key}`)), `${key}: a recorded answer is changed through its choice`);
    }
    const framed = (s: any, who: string) => s.pending.filter((q: any) => q.input.includes(`person[${who}]`) && storedFor(q.input).prompt.startsWith(FRAME));
    ok(framed(opening, "taxpayer").length > 0 && framed(opening, "taxpayer").every((q: any) => q.frame === "About you" && q.prompt.startsWith("About you — "))
      && framed(opening, "spouse").length > 0 && framed(opening, "spouse").every((q: any) => q.frame === "About your spouse" && q.prompt.startsWith("About your spouse — ")),
      "on a couple's return each per-person question begins About you or About your spouse");
    ok(framed(opening, "spouse").every((q: any) => q.prompt === "About your spouse — " + personWording(storedFor(q.input).prompt.slice(FRAME.length + 3), "spouse") && q.help === personWording(spouseWording(storedFor(q.input).help, "joint"), "spouse"))
      && framed(opening, "spouse").some((q: any) => /^About your spouse — (Was|Does|Did|Is) your spouse /.test(q.prompt)),
      "a question asked of the spouse names the spouse and does not say you of them");
    ok([...opening.pending, ...opening.answered].every((q: any) => !q.prompt.includes(FRAME)), "the stored per-person frame is not served once the roles are recorded");
    sameOpening(opening, "the couple's return");
    // An unmarried pair: the existing consistency check, whose recorded status is reached through the first question.
    opening = (await answer("opening", "household.married", false)).body;
    opening = (await answer("opening", "household.spouse_died_2025", false)).body;
    const pairConflict = opening.conflicts.find((c: any) => c.gate === "household.filing_status_conflict");
    ok(pairConflict && isDeepStrictEqual(pairConflict.answers.map((a: any) => a.input), ["$person", "household.married", "household.spouse_died_2025"]),
      `two unmarried people filing together are shown the conflict, with the first question as the answer that set the status: ${JSON.stringify(opening.conflicts.map((c: any) => [c.gate, c.answers.map((a: any) => a.input)]))}`);
    // One person: the status is asked next, with labelled options in the bank's order and married filing jointly withheld.
    opening = (await post("/api/returns/opening/answer", { input: "$person", value: person.choices[0].value, labels: person.choices[0].labels })).body;
    const statusQ = opening.pending.find((q: any) => q.input === STATUS_INPUT);
    ok(opening.pending[0].input === STATUS_INPUT && statusQ.prompt === "Which of these fits you on December 31, 2025?" && isDeepStrictEqual(statusQ.value_order, ["mfs", "qss", "hoh", "single", "mfj"])
      && isDeepStrictEqual(statusQ.withheld, ["mfj"]) && Object.keys(statusQ.value_labels).length === 5 && statusQ.help !== "",
      `one person is asked the filing status next, without the joint status: ${JSON.stringify([opening.pending[0].input, statusQ?.value_order, statusQ?.withheld])}`);
    ok(isDeepStrictEqual(opening.answered.find((a: any) => a.input === "$person").recorded.map((r: any) => r.input), ["person[taxpayer].role"]) && !(STATUS_INPUT in opening.values && opening.values[STATUS_INPUT].value.kind !== "unknown"),
      "changing the choice withdraws the status the couple's choice recorded");
    ok(framed(opening, "taxpayer").length > 0 && framed(opening, "taxpayer").every((q: any) => q.frame === undefined && q.prompt === personWording(storedFor(q.input).prompt.slice(FRAME.length + 3), "taxpayer").replace(/^./, (c: string) => c.toUpperCase()))
      && !opening.pending.some((q: any) => q.input.includes("person[spouse]")), "on a one-person return a per-person question has no frame");
    opening = (await answer("opening", STATUS_INPUT, "mfs")).body;
    ok(opening.status === "refused" && opening.refusal.form === "Married filing separately" && /choose “Me and my husband or wife, together on one return”/.test(opening.refusalNote ?? ""),
      `married filing separately is refused with what the filer can do: ${opening.refusal?.gate} ${String(opening.refusalNote).slice(0, 80)}`);
    opening = (await answer("opening", STATUS_INPUT, "single")).body;
    ok(opening.refusalNote === null && opening.answered.find((a: any) => a.input === STATUS_INPUT).withheld?.[0] === "mfj", "the corrected status clears the note, and its answered question still withholds the joint status");
    sameOpening(opening, "one person's return");
    // A log answered when the roster, the status and each role were separate questions is served, its role answers
    // listed under the first question.
    writeFileSync(join(dir, "earlier.jsonl"), [{ version: 1, tax_year: config.tax_year, profile: "ny" }, { input: "$person", value: ["taxpayer", "spouse"], labels: { taxpayer: "You", spouse: "Your spouse" } },
      { input: STATUS_INPUT, value: "mfj" }, { input: "person[spouse].role", value: "spouse" }, { input: "person[taxpayer].role", value: "taxpayer" }].map((e) => JSON.stringify(e)).join("\n") + "\n", { mode: 0o600 });
    const earlier = (await get("/api/returns/earlier")).body;
    ok(isDeepStrictEqual(earlier.answered.map((a: any) => a.input), ["$person", STATUS_INPUT]) && isDeepStrictEqual(earlier.answered[0].recorded.map((r: any) => [r.input, r.value]), [["person[spouse].role", "spouse"], ["person[taxpayer].role", "taxpayer"]])
      && earlier.answered[0].recorded.every((r: any) => /^The entry/.test(r.shown)), `a log of the earlier questions lists its role answers under the first question: ${JSON.stringify(earlier.answered?.map((a: any) => [a.input, a.recorded]))}`);
    ok(earlier.values[STATUS_INPUT].value.value === "mfj" && framed(earlier, "spouse").length > 0
      && framed(earlier, "spouse").every((q: any) => q.frame === "About your spouse"), "and it is served with the same frames");

    // Fixture interview paths replayed through the server: the federal whole returns (the federal questions; their
    // fixtures have no New York answers) and a sample of the New York cases. Each walk answers the first pending
    // question the fixture answers, until none is left; every expected value the profile's targets reach must match.
    const fed = federal.filter((c) => c.walk === "full");
    const sample = [...nyCases.filter((_, i) => i % 9 === 0), ...nyCases.filter((c) => c.id.startsWith("ny.refuse.")).slice(0, 2)];
    const all = [...fed, ...sample];
    const walkers = [{ port }, ...(await Promise.all(extra))];
    const idle = walkers.map((_, i) => i);
    const counts = await mapPool(all, async (c, walk) => {
      const lane = idle.shift()!;
      try {
        const post2 = (path: string, body: unknown) => http(walkers[lane]!.port, "POST", path, { body });
        const name = `fx-${walk}`;
        let s = (await post2("/api/returns", { name })).body;
        for (let step = 0; ; step++) {
          assert.ok(step < 800, `${c.id}: the walk did not end`);
          const q = s.pending.find((p: any) => p.input in c.inputs && !s.answered.some((a: any) => a.input === p.input));
          if (!q) break;
          const r = await post2(`/api/returns/${name}/answer`, { input: q.input, value: c.inputs[q.input] });
          assert.equal(r.status, 200, `${c.id} ${q.input}: ${JSON.stringify(r.body)}`);
          s = r.body;
        }
        let compared = 0, unreached = 0;
        for (const [key, expected] of Object.entries(c.expect ?? {})) {
          if (!(key in s.values)) { unreached++; continue; }
          assert.deepEqual(s.values[key].value, expected, `${c.id}: ${key} through the server`);
          compared++;
        }
        return { compared, unreached };
      } finally { idle.push(lane); }
    }, walkers.length);
    const walks = all.length;
    const compared = counts.reduce((n, c) => n + c.compared, 0), unreached = counts.reduce((n, c) => n + c.unreached, 0);
    ok(compared > 0, "fixture values compared");
    console.log(`serve: ${checks} checks passed; ${walks} fixture paths replayed through the server (${fed.length} federal, ${sample.length} New York), ${compared} expected values matched, ${unreached} not reached by the profile's targets`);
  } finally {
    server?.kill();
    for (const p of extra) p.then((x) => x.proc.kill(), () => {});
    rmSync(tmp, { recursive: true, force: true });
  }
}
