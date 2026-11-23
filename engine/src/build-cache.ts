// Reuse of a passing build, or a passing check step, whose inputs are unchanged. The build is below; the steps
// (engine commands that check and write nothing) under "the steps".
//
// `node engine/dist/main.js build` checks the model sources and writes canonical/<year>/. Its result is a function of
// what it reads, so a build that passed, recorded with everything it read, can stand for a new build whose reads all
// give what they gave then. This module records the reads and keeps such records:
//
// - The reads. Imported first by main.ts, before any module that reads a file, it replaces every function of node:fs
//   (and node:fs/promises) when the command is `build` or a step, and in every worker thread and node child process
//   of such a run (a worker module imports it first; a node child loads it through NODE_OPTIONS=--import), each of
//   which records under an id it is given and is expected to (collect). The sync functions the engine uses record a probe of the path they
//   are given, made from what the call returned: the bytes of a file read (readFileSync; openSync for reading), the
//   entries and their types of a directory listed (readdirSync), whether a path exists (existsSync), the type, size and
//   modification time of a path stat'ed (statSync, lstatSync), a real path (realpathSync). Any other read (a form of
//   those calls the probe cannot repeat, any other function of node:fs or node:fs/promises, a module loaded from
//   outside the code below) marks the run untraceable; writes are recorded by path. Calls by descriptor pass: a
//   descriptor comes only from an open, and node's module loader reads the code by descriptor.
// - The context. The record holds the code (every file of engine/dist and node_modules, package.json and
//   package-lock.json), the Node version and platform, the root and working directory, the command line, the tax year
//   and the environment, less the variables of IGNORED_ENV, which set only how many workers a pool starts or name the
//   check-all run (the build's output is the same for every worker count: interview-paths --self-test).
// - The record. A build that passed, read nothing untraceable and wrote only under canonical/<year>/ is stored in the
//   git directory of the worktree (build-cache/): its context digest, its probes, its printed stats and the files it
//   wrote (content-addressed blobs). The newest KEEP records are kept.
// - Reuse. A later build with the same context whose every probe gives the recorded value now is that build: it
//   prints the recorded stats and a line saying so, and leaves canonical/<year>/ as the recorded build wrote it
//   (rewritten from the blobs when it differs). Nothing is checked twice: what the build would read is what it read.
//
// BUILD_CACHE selects the mode: use (the default) reuses a matching record and otherwise builds and stores one;
// verify (the default when ENGINE_CACHE=verify, as tools/release.sh runs) always builds, and a stored record whose
// probes hold must have given the same stats and files, or the build fails naming the difference; off reads and
// stores nothing.
//
//   node engine/dist/main.js build-cache --self-test    the probes, the record and its reuse, in a temporary folder
import fs from "node:fs";
import { isUtf8 } from "node:buffer";
import { createHash } from "node:crypto";
import { registerHooks, syncBuiltinESMExports } from "node:module";
import { tmpdir } from "node:os";
import { basename, isAbsolute, join, relative, resolve, sep } from "node:path";
import { fileURLToPath } from "node:url";
import cp from "node:child_process";
import { randomUUID } from "node:crypto";
import wt, { isMainThread } from "node:worker_threads";

const ROOT = resolve(import.meta.dirname, "../..");
const KEEP = 4;
const VERSION = 1;
/** Variables that set only a pool's worker count or name the check-all run around the build, and this module's own. */
export const IGNORED_ENV = new Set(["BUILD_WORKERS", "TEST_WORKERS", "INTERVIEW_WORKERS", "MUTATE_WORKERS", "SELF_TEST_WORKERS",
  "CHECK_ALL_MAX_RUNS", "CHECK_ALL_SLOT", "CHECK_ALL_SLOT_DIR", "CHECK_ALL_PREFLIGHT", "BUILD_CACHE", "BUILD_CACHE_DIR",
  "ENGINE_TRACE_DIR", "ENGINE_TRACE_ID", "_", "SHLVL", "OLDPWD", "PWD"]);

// The functions of node:fs as they were, for this module's own use: a call through one does not record, nor do the
// calls node:fs makes inside it (readFileSync calls readSync).
let depth = 0;
const quiet = <F extends (...a: never[]) => unknown>(f: F): F => function (this: unknown, ...a: Parameters<F>) {
  depth++;
  try { return f.apply(this, a); } finally { depth--; }
} as F;
const real = Object.fromEntries(Object.entries({
  readFileSync: fs.readFileSync, readdirSync: fs.readdirSync, existsSync: fs.existsSync, statSync: fs.statSync,
  lstatSync: fs.lstatSync, realpathSync: fs.realpathSync, writeFileSync: fs.writeFileSync, mkdirSync: fs.mkdirSync,
  rmSync: fs.rmSync, renameSync: fs.renameSync, mkdtempSync: fs.mkdtempSync, unlinkSync: fs.unlinkSync, utimesSync: fs.utimesSync,
}).map(([k, f]) => [k, quiet(f as (...a: never[]) => unknown)])) as unknown as Pick<typeof fs, "readFileSync" | "readdirSync" | "existsSync" |
  "statSync" | "lstatSync" | "realpathSync" | "writeFileSync" | "mkdirSync" | "rmSync" | "renameSync" | "mkdtempSync" | "unlinkSync" | "utimesSync">;

type Kind = "content" | "list" | "exists" | "stat" | "lstat" | "real";
interface Trace { on: boolean; probes: Map<string, string>; writes: Set<string>; untraceable: Set<string>; expects: Set<string>; scratch: Set<string> }
const trace: Trace = { on: false, probes: new Map(), writes: new Set(), untraceable: new Set(), expects: new Set(), scratch: new Set() };
// A traced run's descendants (worker threads, node child processes) record into the folder ENGINE_TRACE_DIR names, each
// under the id ENGINE_TRACE_ID it was started with; the run expects a record of every id it gave out.
const TRACE_DIR = "ENGINE_TRACE_DIR";
const TRACE_ID = "ENGINE_TRACE_ID";

const sha = (data: string | Buffer): string => createHash("sha256").update(data).digest("hex");
const code = (e: unknown): string => `error:${(e as { code?: string }).code ?? "unknown"}`;
const typeOf = (s: { isFile(): boolean; isDirectory(): boolean; isSymbolicLink(): boolean }): string =>
  s.isFile() ? "f" : s.isDirectory() ? "d" : s.isSymbolicLink() ? "l" : "o";

/** What a probe of `kind` on the absolute path `path` gives now. */
export function probeValue(kind: Kind, path: string): string {
  try {
    switch (kind) {
      case "content": return `sha256:${sha(real.readFileSync(path))}`;
      case "list": return JSON.stringify(real.readdirSync(path, { withFileTypes: true }).map((d) => [d.name, typeOf(d)]));
      case "exists": return String(real.existsSync(path));
      case "stat": { const s = real.statSync(path); return `${typeOf(s)}:${s.size}:${s.mtimeMs}`; }
      case "lstat": { const s = real.lstatSync(path); return `${typeOf(s)}:${s.size}:${s.mtimeMs}`; }
      case "real": return real.realpathSync(path);
    }
  } catch (e) { return code(e); }
}

function pathOf(p: unknown): string | null {
  if (typeof p === "string") return resolve(p);
  if (p instanceof URL) return p.protocol === "file:" ? fileURLToPath(p) : null;
  if (Buffer.isBuffer(p)) return resolve(p.toString("utf8"));
  return null;
}

/** Record a probe of `p`: `value` when the read's own result gives it, else what the probe gives now. */
function probe(kind: Kind, p: unknown, what: string, value?: string): void {
  if (!trace.on) return;
  const path = pathOf(p);
  if (path === null) { trace.untraceable.add(`${what} of a descriptor or non-file URL`); return; }
  const key = `${kind}\0${path}`;
  if (!trace.probes.has(key)) trace.probes.set(key, value ?? probeValue(kind, path));
}

type Fn = (...a: unknown[]) => unknown;
type Stat = { isFile(): boolean; isDirectory(): boolean; isSymbolicLink(): boolean; size: number; mtimeMs: number };
/** The recording form of a read of node:fs: the probe is made from what the read itself returned (or the error it threw),
 * so that the recorded value is what the build read. A form of the call whose result the probe cannot be made from
 * (another encoding, a recursive listing, a write flag) marks the run untraceable. */
function reader(name: string, f: Fn): Fn {
  const record = (kind: Kind, p: unknown, run: () => { value: string; result: unknown }): unknown => {
    let out: { value: string; result: unknown };
    try { out = run(); } catch (e) { probe(kind, p, name, code(e)); throw e; }
    probe(kind, p, name, out.value);
    return out.result;
  };
  const untraceable = (self: unknown, a: unknown[]): unknown => { trace.untraceable.add(`fs.${name} in a form not recorded`); return f.apply(self, a); };
  switch (name) {
    case "readFileSync": return function (this: unknown, ...a: unknown[]) {
      if (!trace.on) return f.apply(this, a);
      const o = a[1];
      const enc = typeof o === "string" ? o : (o as { encoding?: string } | undefined)?.encoding ?? null;
      const flag = typeof o === "object" && o !== null ? (o as { flag?: string }).flag : undefined;
      if ((flag !== undefined && flag !== "r") || (enc !== null && enc !== "utf8" && enc !== "utf-8")) return untraceable(this, a);
      return record("content", a[0], () => {
        const buf = f.call(this, a[0]) as Buffer;
        // Only valid UTF-8 decodes to the same text by either path; other bytes are read as the call reads them.
        if (enc !== null && !isUtf8(buf)) return { value: "untraceable", result: untraceable(this, a) };
        return { value: `sha256:${sha(buf)}`, result: enc === null ? buf : buf.toString("utf8") };
      });
    };
    case "readdirSync": return function (this: unknown, ...a: unknown[]) {
      if (!trace.on) return f.apply(this, a);
      const o = a[1];
      const opts = (typeof o === "string" ? { encoding: o } : o ?? {}) as { encoding?: string | null; withFileTypes?: boolean; recursive?: boolean };
      if (opts.recursive || (opts.encoding != null && opts.encoding !== "utf8" && opts.encoding !== "utf-8")) return untraceable(this, a);
      return record("list", a[0], () => {
        const entries = f.call(this, a[0], { withFileTypes: true }) as fs.Dirent[];
        return { value: JSON.stringify(entries.map((d) => [d.name, typeOf(d)])), result: opts.withFileTypes ? entries : entries.map((d) => d.name) };
      });
    };
    case "existsSync": return function (this: unknown, ...a: unknown[]) {
      if (!trace.on) return f.apply(this, a);
      return record("exists", a[0], () => { const r = f.apply(this, a) as boolean; return { value: String(r), result: r }; });
    };
    case "statSync": case "lstatSync": return function (this: unknown, ...a: unknown[]) {
      if (!trace.on) return f.apply(this, a);
      const o = a[1] as { throwIfNoEntry?: boolean; bigint?: boolean } | undefined;
      if (o?.bigint) return untraceable(this, a);
      return record(name === "statSync" ? "stat" : "lstat", a[0], () => {
        const s = f.apply(this, a) as Stat | undefined;
        return { value: s === undefined ? "error:ENOENT" : `${typeOf(s)}:${s.size}:${s.mtimeMs}`, result: s };
      });
    };
    case "realpathSync": return function (this: unknown, ...a: unknown[]) {
      if (!trace.on) return f.apply(this, a);
      // node's require passes an options object holding its cache; any form that returns the path as text is recorded.
      const o = a[1];
      const enc = typeof o === "string" ? o : o === undefined || o === null ? undefined : (o as { encoding?: string | null }).encoding;
      if (enc != null && enc !== "utf8" && enc !== "utf-8") return untraceable(this, a);
      return record("real", a[0], () => { const r = f.apply(this, a) as string; return { value: r, result: r }; });
    };
  }
  throw new Error(`build cache: no reader for fs.${name}`);
}

function wrote(p: unknown, what: string): void {
  if (!trace.on) return;
  const path = pathOf(p);
  if (path === null) trace.untraceable.add(`${what} to a descriptor`); else trace.writes.add(path);
}

const READS = new Set(["readFileSync", "readdirSync", "existsSync", "statSync", "lstatSync", "realpathSync"]);
const WRITES = new Set(["writeFileSync", "appendFileSync", "mkdirSync", "rmSync", "rmdirSync", "unlinkSync", "copyFileSync", "cpSync",
  "symlinkSync", "truncateSync", "chmodSync", "utimesSync"]);

const DESCRIPTOR = /^(read|readv|write|writev|close|fstat|fsync|fdatasync|ftruncate|futimes|fchmod|fchown)Sync$/;

let installed = false;
/** Replace the functions of node:fs and node:fs/promises with recording ones (they record only while the trace is on). */
export function install(): void {
  if (installed) return;
  installed = true;
  const target = fs as unknown as Record<string, unknown>;
  for (const name of Object.keys(target)) {
    const orig = target[name];
    if (typeof orig !== "function" || /^[A-Z]/.test(name) || name === "promises") continue;
    const f = orig as Fn;
    let wrapper: Fn;
    if (READS.has(name)) wrapper = reader(name, f);
    else if (WRITES.has(name)) wrapper = function (this: unknown, ...a: unknown[]) { wrote(a[0], name); if (name === "copyFileSync" || name === "cpSync") probe("content", a[0], name); return f.apply(this, a); };
    else if (name === "renameSync") wrapper = function (this: unknown, ...a: unknown[]) { wrote(a[0], name); wrote(a[1], name); return f.apply(this, a); };
    // A folder made by mkdtempSync is the run's scratch: what it writes and reads there is its own.
    else if (name === "mkdtempSync") wrapper = function (this: unknown, ...a: unknown[]) { const d = f.apply(this, a) as string; if (trace.on) trace.scratch.add(resolve(d)); return d; };
    else if (name === "openSync") wrapper = function (this: unknown, ...a: unknown[]) {
      const flags = a[1] ?? "r";
      if (flags === "r" || flags === fs.constants.O_RDONLY) probe("content", a[0], name); else wrote(a[0], name);
      return f.apply(this, a);
    };
    // A descriptor is had only from an open, which records (openSync) or marks the run untraceable (open, and
    // fs.promises); node's module loader reads code by descriptor too, and the code is in the context.
    else if (DESCRIPTOR.test(name)) wrapper = f;
    else wrapper = function (this: unknown, ...a: unknown[]) { if (trace.on) trace.untraceable.add(`fs.${name}`); return f.apply(this, a); };
    // A function of node:fs calls others (readFileSync calls openSync and readSync): only the outermost call records.
    const inner = wrapper;
    const outer = function (this: unknown, ...a: unknown[]) {
      if (depth > 0) return f.apply(this, a);
      depth++;
      try { return inner.apply(this, a); } finally { depth--; }
    };
    Object.assign(outer, orig);
    target[name] = outer;
  }
  const promises = fs.promises as unknown as Record<string, unknown>;
  for (const name of Object.keys(promises)) {
    const orig = promises[name];
    if (typeof orig !== "function" || /^[A-Z]/.test(name)) continue;
    const f = orig as (...a: unknown[]) => unknown;
    promises[name] = function (this: unknown, ...a: unknown[]) { if (trace.on) trace.untraceable.add(`fs.promises.${name}`); return f.apply(this, a); };
  }
  traceDescendants();
  syncBuiltinESMExports();
  // A module loaded from outside the code the context hashes (engine/dist, node_modules) is a read it does not cover.
  const code = [join(ROOT, "engine", "dist") + sep, join(ROOT, "node_modules") + sep];
  registerHooks({
    resolve(specifier, context, next) {
      const r = next(specifier, context);
      if (trace.on && r.url.startsWith("file:") && !code.some((c) => fileURLToPath(r.url).startsWith(c))) trace.untraceable.add(`a module loaded from ${fileURLToPath(r.url)}`);
      return r;
    },
  });
}

/** Forget what was recorded (the self-test runs several builds in one process). */
function resetTrace(): void { for (const k of ["probes", "writes", "untraceable", "expects", "scratch"] as const) trace[k].clear(); }

/** Start recording (the build's process, from its first module; a worker, when the build traces). */
export function start(): void { install(); trace.on = true; }

/** The NODE_OPTIONS of a traced node child: its own, and this module loaded first. */
function tracedNodeOptions(env: NodeJS.ProcessEnv): string {
  const own = `--import=${import.meta.url}`;
  const was = env["NODE_OPTIONS"] ?? "";
  return was.includes(own) ? was : `${was} ${own}`.trim();
}

/** A child's or worker's environment, given an id to record under; undefined when the trace is off. */
function descendantEnv(env: NodeJS.ProcessEnv | undefined): NodeJS.ProcessEnv | undefined {
  if (!trace.on) return env;
  const dir = process.env[TRACE_DIR];
  if (!dir) { trace.untraceable.add("a worker or child started with no trace folder"); return env; }
  const id = randomUUID();
  trace.expects.add(id);
  const base = env ?? process.env;
  return { ...base, [TRACE_DIR]: dir, [TRACE_ID]: id, NODE_OPTIONS: tracedNodeOptions(base) };
}

/** Worker threads and child processes started while the trace is on are traced too: a worker or a node child gets
 * an id and records under it (a worker module imports this module first; a node child loads it through NODE_OPTIONS);
 * any other program, a shell, an environment shared with a worker, or output a child writes straight to this
 * process's own stdout or stderr marks the run untraceable. */
function traceDescendants(): void {
  const workers = wt as unknown as Record<string, unknown>;
  const Orig = wt.Worker;
  workers["Worker"] = class extends Orig {
    constructor(file: string | URL, opts: wt.WorkerOptions = {}) {
      if (trace.on && opts.env === wt.SHARE_ENV) trace.untraceable.add("a worker sharing the environment");
      super(file, trace.on && opts.env !== wt.SHARE_ENV ? { ...opts, env: descendantEnv(opts.env as NodeJS.ProcessEnv | undefined)! } : opts);
    }
  };
  const procs = cp as unknown as Record<string, Fn>;
  const isNode = (file: unknown): boolean => typeof file === "string" && (file === process.execPath || basename(file) === "node");
  const ownStream = (x: unknown): boolean => x === "inherit" || x === 1 || x === 2 || x === process.stdout || x === process.stderr;
  for (const name of ["spawn", "spawnSync", "execFile", "execFileSync", "fork"]) {
    const f = procs[name]!;
    procs[name] = function (this: unknown, ...a: unknown[]) {
      if (!trace.on) return f.apply(this, a);
      const file = name === "fork" ? process.execPath : a[0];
      const at = Array.isArray(a[1]) ? 2 : 1;
      const opts = (a[at] && typeof a[at] === "object" ? a[at] : {}) as { env?: NodeJS.ProcessEnv; stdio?: unknown };
      if (!isNode(file)) trace.untraceable.add(`a child process ${String(file)}`);
      const stdio = opts.stdio;
      if (ownStream(stdio) || (Array.isArray(stdio) && (ownStream(stdio[1]) || ownStream(stdio[2])))) trace.untraceable.add(`a child writing to this process's own output`);
      const args = [...a];
      if (at === 2 && !Array.isArray(a[1])) args.splice(1, 0, []);
      while (args.length < 3) args.push(undefined);
      args[2] = { ...opts, env: descendantEnv(opts.env) };
      return f.apply(this, name === "fork" ? [a[0], ...args.slice(1)] : args);
    };
  }
  for (const name of ["exec", "execSync"]) {
    const f = procs[name]!;
    procs[name] = function (this: unknown, ...a: unknown[]) { if (trace.on) trace.untraceable.add(`a shell (child_process.${name})`); return f.apply(this, a); };
  }
}

/** The record of a traced descendant, written when it exits. */
interface DescendantTrace { probes: [string, string][]; writes: string[]; untraceable: string[]; expects: string[]; scratch: string[] }

// A worker or child of a traced run records from its first module and writes its record when it ends.
if (process.env[TRACE_ID] && process.env[TRACE_DIR]) {
  start();
  const dir = process.env[TRACE_DIR];
  const id = process.env[TRACE_ID];
  process.on("exit", () => {
    const record: DescendantTrace = { probes: [...trace.probes], writes: [...trace.writes], untraceable: [...trace.untraceable],
      expects: [...trace.expects], scratch: [...trace.scratch] };
    real.writeFileSync(join(dir, `${id}.json`), JSON.stringify(record));
  });
} else if (isMainThread && process.argv[2] === "build" && mode() !== "off") start();

/** Merge into this process's trace the records of its descendants in `dir`, each expected id's and those it expected
 * in turn; a missing record (a descendant that did not load this module, or did not end) marks the run untraceable. */
function collect(dir: string): void {
  const seen = new Set<string>();
  const queue = [...trace.expects];
  while (queue.length) {
    const id = queue.shift()!;
    if (seen.has(id)) continue;
    seen.add(id);
    let t: DescendantTrace;
    try { t = JSON.parse(real.readFileSync(join(dir, `${id}.json`), "utf8") as string) as DescendantTrace; }
    catch { trace.untraceable.add("a worker or child left no record of its reads"); continue; }
    for (const [k, v] of t.probes) if (!trace.probes.has(k)) trace.probes.set(k, v);
    for (const w of t.writes) trace.writes.add(w);
    for (const u of t.untraceable) trace.untraceable.add(u);
    for (const x of t.scratch) trace.scratch.add(x);
    queue.push(...t.expects);
  }
}

const within = (path: string, dirs: Iterable<string>): boolean => [...dirs].some((d) => path === d || path.startsWith(d + sep));
/** The probes and writes outside the run's scratch folders. */
function ownProbes(): [string, string][] { return [...trace.probes].filter(([k]) => !within(k.split("\0")[1]!, trace.scratch)); }
function ownWrites(): string[] { return [...trace.writes].filter((w) => !within(w, trace.scratch)); }

export function mode(): "use" | "verify" | "off" {
  const m = process.env["BUILD_CACHE"];
  if (m === "use" || m === "verify" || m === "off") return m;
  return process.env["ENGINE_CACHE"] === "verify" ? "verify" : "use";
}

// ---- the record ----

function filesUnder(base: string, skip: ReadonlySet<string> = new Set()): string[] {
  const out: string[] = [];
  const walk = (dir: string): void => {
    let entries: fs.Dirent[];
    try { entries = real.readdirSync(dir, { withFileTypes: true }) as fs.Dirent[]; } catch { return; }
    for (const e of entries.sort((a, b) => (a.name < b.name ? -1 : a.name > b.name ? 1 : 0))) {
      const p = join(dir, e.name);
      if (e.isDirectory()) { if (!skip.has(e.name)) walk(p); } else out.push(p);
    }
  };
  walk(base);
  return out;
}

/** The digest of the code a build runs: engine/dist, node_modules, the package files, Node and the platform. */
function codeDigest(root: string): string {
  const h = createHash("sha256");
  h.update(`${process.version} ${process.platform} ${process.arch}\0`);
  for (const base of ["engine/dist", "node_modules"]) {
    for (const p of filesUnder(join(root, base))) h.update(`${relative(root, p)}\0${sha(real.readFileSync(p))}\0`);
  }
  for (const f of ["package.json", "package-lock.json"]) h.update(`${f}\0${probeValue("content", join(root, f))}\0`);
  return h.digest("hex");
}

/** The context digest: the code, the root and working directory, the command line, the year and the environment. */
export function contextDigest(root: string, year: number, argv: readonly string[], env: NodeJS.ProcessEnv, codeKey: string): string {
  const vars = Object.keys(env).filter((k) => !IGNORED_ENV.has(k)).sort().map((k) => [k, env[k]]);
  return sha(JSON.stringify({ version: VERSION, code: codeKey, root, cwd: process.cwd(), argv, year, env: vars }));
}

interface Entry { context: string; created: number; probes: [string, string][]; stats: string[]; outputs: [string, string][] }

function gitDir(root: string): string {
  const dotgit = join(root, ".git");
  try {
    const text = real.readFileSync(dotgit, "utf8") as string;
    const m = /^gitdir: (.+)$/m.exec(text);
    if (m) return isAbsolute(m[1]!.trim()) ? m[1]!.trim() : resolve(root, m[1]!.trim());
  } catch { /* a directory */ }
  return dotgit;
}

/** The folder of the records: BUILD_CACHE_DIR, else engine-cache/ in the worktree's git directory; the build's records
 * are in build/, a step's in steps/<command>/. */
export function cacheDir(root: string = ROOT, kind = "build"): string {
  return join(process.env["BUILD_CACHE_DIR"] ?? join(gitDir(root), "engine-cache"), kind);
}

function readEntries(dir: string): { file: string; entry: Entry }[] {
  const files = real.existsSync(dir) ? (real.readdirSync(dir) as string[]).filter((f) => f.endsWith(".json")) : [];
  const out: { file: string; entry: Entry }[] = [];
  for (const f of files) {
    try { out.push({ file: join(dir, f), entry: JSON.parse(real.readFileSync(join(dir, f), "utf8") as string) as Entry }); } catch { /* a partial record */ }
  }
  return out.sort((a, b) => b.entry.created - a.entry.created);
}

/** The first probe of `entry` that does not give its recorded value now, or null when all do. */
export function staleProbe(entry: Entry): string | null {
  for (const [key, value] of entry.probes) {
    const [kind, path] = key.split("\0") as [Kind, string];
    if (probeValue(kind, path) !== value) return `${kind} ${path}`;
  }
  return null;
}

function outputsOf(outDir: string): [string, string][] {
  return filesUnder(outDir).map((p) => [relative(outDir, p).split(sep).join("/"), sha(real.readFileSync(p))]);
}

/** Make outDir hold exactly the entry's outputs, as a build leaves it: rewritten from the blobs when it differs, else
 * its files' times set to now (tools/build_fresh.py compares them with the sources'); false when a blob is gone. */
function restore(dir: string, outDir: string, entry: Entry): boolean {
  const now = outputsOf(outDir);
  if (JSON.stringify(now) === JSON.stringify(entry.outputs)) {
    const t = new Date();
    for (const [rel] of now) real.utimesSync(join(outDir, ...rel.split("/")), t, t);
    return true;
  }
  if (!entry.outputs.every(([, h]) => real.existsSync(join(dir, "blobs", h)))) return false;
  real.rmSync(outDir, { recursive: true, force: true });
  for (const [rel, h] of entry.outputs) {
    const p = join(outDir, ...rel.split("/"));
    real.mkdirSync(join(p, ".."), { recursive: true });
    real.writeFileSync(p, real.readFileSync(join(dir, "blobs", h)));
  }
  return true;
}

function store(dir: string, outDir: string, entry: Omit<Entry, "outputs">): void {
  real.mkdirSync(join(dir, "blobs"), { recursive: true });
  const outputs = outputsOf(outDir);
  for (const [rel, h] of outputs) {
    const blob = join(dir, "blobs", h);
    if (!real.existsSync(blob)) {
      const tmp = `${blob}.${process.pid}.tmp`;
      real.writeFileSync(tmp, real.readFileSync(join(outDir, ...rel.split("/"))));
      real.renameSync(tmp, blob);
    }
  }
  const full: Entry = { ...entry, outputs };
  const name = `${full.created}-${process.pid}.json`;
  real.writeFileSync(join(dir, `${name}.tmp`), JSON.stringify(full));
  real.renameSync(join(dir, `${name}.tmp`), join(dir, name));
  // Keep the newest KEEP records and the blobs they name.
  const entries = readEntries(dir);
  for (const { file } of entries.slice(KEEP)) real.rmSync(file, { force: true });
  const used = new Set(entries.slice(0, KEEP).flatMap(({ entry }) => entry.outputs.map(([, h]) => h)));
  for (const b of real.readdirSync(join(dir, "blobs")) as string[]) if (!used.has(b) && !b.endsWith(".tmp")) real.rmSync(join(dir, "blobs", b), { force: true });
}

export interface BuildResult { errors: string[]; stats: string[] }

/** Run `build` (which writes `outDir`), or reuse a passing build of the same inputs, as the mode says. */
export async function cachedBuild(outDir: string, year: number, build: () => Promise<BuildResult>, opts: { root?: string; argv?: readonly string[] } = {}): Promise<BuildResult> {
  const m = mode();
  if (m === "off") { trace.on = false; return build(); }
  const root = opts.root ?? ROOT;
  const dir = cacheDir(root);
  const context = contextDigest(root, year, opts.argv ?? process.argv.slice(2), process.env, codeDigest(root));
  const candidates = readEntries(dir).filter(({ entry }) => entry.context === context);
  const match = candidates.find(({ entry }) => staleProbe(entry) === null)?.entry ?? null;
  if (match && m === "use" && restore(dir, outDir, match)) {
    trace.on = false;
    return { errors: [], stats: [...match.stats, `build cache: every file this build reads is as a passing build read it (${match.probes.length} probes); ${relative(root, outDir)}/ is that build's output`] };
  }
  start();
  const traceDir = real.mkdtempSync(join(tmpdir(), "engine-trace."));
  process.env[TRACE_DIR] = traceDir;
  let result: BuildResult;
  try { result = await build(); } finally {
    trace.on = false;
    delete process.env[TRACE_DIR];
  }
  collect(traceDir);
  real.rmSync(traceDir, { recursive: true, force: true });
  if (result.errors.length > 0) return result;
  if (m === "verify" && match) {
    const now = outputsOf(outDir);
    if (JSON.stringify(now) !== JSON.stringify(match.outputs) || JSON.stringify(result.stats) !== JSON.stringify(match.stats)) {
      const differ = [...new Set([...now, ...match.outputs].map(([p]) => p))].filter((p) => JSON.stringify(now.find(([q]) => q === p)) !== JSON.stringify(match.outputs.find(([q]) => q === p)));
      return { errors: [`build cache: a stored build of the same inputs gave other output (${differ.slice(0, 5).join(", ") || "its printed stats"}); the cache is unsound for this build`], stats: result.stats };
    }
  }
  const outside = ownWrites().filter((w) => w !== outDir && !w.startsWith(outDir + sep));
  if (trace.untraceable.size > 0 || outside.length > 0) {
    const why = [...trace.untraceable, ...outside.map((w) => `a write to ${w}`)].slice(0, 3).join("; ");
    return { errors: [], stats: [...result.stats, `build cache: not stored (${why})`] };
  }
  try { store(dir, outDir, { context, created: Date.now(), probes: ownProbes(), stats: result.stats }); }
  catch (e) { return { errors: [], stats: [...result.stats, `build cache: not stored (${String(e)})`] }; }
  return result;
}

// ---- the steps ----
//
// An engine command of STEP_COMMANDS (the check-all steps that check and write nothing) is a step: run from a shell,
// not as a traced descendant, it looks for a record of a passing run with the same context whose probes all hold, and
// if there is one prints that run's output (stdout and stderr, in order) and a line saying so, and exits 0 without
// running. Otherwise it runs traced, its descendants with it, its output captured as it is written, and when it exits
// 0 having read nothing untraceably and written nothing outside its scratch folders, its record is stored. The
// context is the build's, less the tax year (years.json is read, so it is a probe). In verify mode every step runs;
// one that fails where a stored passing run of the same reads exists says so (the cache would have passed it).
//
// WRITE_CHECK pairs a command's writing form with its checking form, where a passing writing run is the checking run
// with its file written: the checking form's record is derived from it, with the file it wrote as one more probe
// (its contents as written) and its output less the line saying it wrote it. So the preflight's
// `interview-coverage --write` stands for the step's `interview-coverage`.

export const STEP_COMMANDS = new Set(["interview-coverage", "tick-groups", "spouse-wording", "check-self-test", "interview-rules",
  "step-cache-probe"]);

/** command -> (the flag of its writing form, the line its writing form prints for the file it wrote). interviewCoverage
 * (interview-coverage.ts), on its own rows and unscoped, exits 0 with --write exactly when it finds no problem, having
 * written the report; without --write it finds the same problems and compares the report with the same text, printing
 * the same lines but that one. */
const WRITE_CHECK: Record<string, { flag: string; wrote: RegExp; refuse: string[] }> = {
  "interview-coverage": { flag: "--write", wrote: /^ {2}wrote \S+$/, refuse: ["--rows", "--schema", "--forms"] },
  "step-cache-probe": { flag: "--write", wrote: /^probe: wrote \S+$/, refuse: [] },
};

/** A step's record; `files` are the files of the worktree it wrote (path from the root, sha256 of what it left there,
 * the bytes kept as blobs), written again when it is reused. */
interface StepEntry { context: string; created: number; probes: [string, string][]; output: [1 | 2, string][]; files?: [string, string][] }

function stepContext(root: string, argv: readonly string[], env: NodeJS.ProcessEnv, codeKey: string): string {
  const vars = Object.keys(env).filter((k) => !IGNORED_ENV.has(k)).sort().map((k) => [k, env[k]]);
  return sha(JSON.stringify({ version: VERSION, kind: "step", code: codeKey, root, cwd: process.cwd(), argv, env: vars }));
}

function readStepEntries(dir: string): { file: string; entry: StepEntry }[] {
  return readEntries(dir) as unknown as { file: string; entry: StepEntry }[];
}

function storeStep(dir: string, entry: StepEntry, root: string = ROOT): void {
  real.mkdirSync(join(dir, "blobs"), { recursive: true });
  for (const [rel, h] of entry.files ?? []) {
    const blob = join(dir, "blobs", h);
    if (!real.existsSync(blob)) { real.writeFileSync(`${blob}.${process.pid}.tmp`, real.readFileSync(join(root, rel))); real.renameSync(`${blob}.${process.pid}.tmp`, blob); }
  }
  const name = `${entry.created}-${process.pid}-${randomUUID().slice(0, 8)}.json`;
  real.writeFileSync(join(dir, `${name}.tmp`), JSON.stringify(entry));
  real.renameSync(join(dir, `${name}.tmp`), join(dir, name));
  const entries = readStepEntries(dir);
  for (const { file } of entries.slice(KEEP)) real.rmSync(file, { force: true });
  const used = new Set(entries.slice(0, KEEP).flatMap(({ entry: e }) => (e.files ?? []).map(([, h]) => h)));
  for (const b of real.readdirSync(join(dir, "blobs")) as string[]) if (!used.has(b) && !b.endsWith(".tmp")) real.rmSync(join(dir, "blobs", b), { force: true });
}

/** The files of the worktree a run wrote, as [path from the root, sha256], or null when it wrote anything else (a
 * folder, a path outside the worktree, a file it then removed). */
function writtenFiles(writes: string[], root: string): [string, string][] | null {
  const out: [string, string][] = [];
  for (const w of writes) {
    if (!w.startsWith(root + sep)) return null;
    let st;
    try { st = real.statSync(w); } catch { return null; }
    if (!st.isFile()) return null;
    out.push([relative(root, w).split(sep).join("/"), sha(real.readFileSync(w))]);
  }
  return out.sort((a, b) => (a[0] < b[0] ? -1 : 1));
}

function runStep(command: string): void {
  const m = mode();
  const root = ROOT;
  const argv = process.argv.slice(2);
  const dir = cacheDir(root, join("steps", command));
  const codeKey = codeDigest(root);
  const context = stepContext(root, argv, process.env, codeKey);
  const match = readStepEntries(dir).filter(({ entry }) => entry.context === context).find(({ entry }) => staleProbe(entry as unknown as Entry) === null)?.entry ?? null;
  // The folder whose files a step may write and have written again: the worktree (ENGINE_CACHE_WORKTREE: the self-test's).
  const tree = process.env["ENGINE_CACHE_WORKTREE"] ?? root;
  const blobsKept = (e: StepEntry): boolean => (e.files ?? []).every(([, h]) => real.existsSync(join(dir, "blobs", h)));
  if (match && m === "use" && blobsKept(match)) {
    // The files the run wrote, as it left them (rewritten only where they differ).
    for (const [rel, h] of match.files ?? []) {
      const p = join(tree, ...rel.split("/"));
      if (probeValue("content", p) !== `sha256:${h}`) { real.mkdirSync(join(p, ".."), { recursive: true }); real.writeFileSync(p, real.readFileSync(join(dir, "blobs", h))); }
    }
    for (const [fd, text] of match.output) fs.writeSync(fd, text);
    fs.writeSync(1, `step cache: every file this run reads is as a passing run read it (${match.probes.length} probes); the output above is that run's\n`);
    process.exit(0);
  }
  const envBefore = { ...process.env };
  start();
  const traceDir = real.mkdtempSync(join(tmpdir(), "engine-trace."));
  process.env[TRACE_DIR] = traceDir;
  process.env["NODE_OPTIONS"] = tracedNodeOptions(process.env);
  const output: [1 | 2, string][] = [];
  for (const [fd, stream] of [[1, process.stdout], [2, process.stderr]] as const) {
    const write = stream.write.bind(stream) as (...a: unknown[]) => boolean;
    (stream as unknown as { write: unknown }).write = (chunk: unknown, ...rest: unknown[]) => {
      output.push([fd, typeof chunk === "string" ? chunk : Buffer.from(chunk as Uint8Array).toString("utf8")]);
      return write(chunk, ...rest);
    };
  }
  process.on("exit", (code) => {
    trace.on = false;
    collect(traceDir);
    real.rmSync(traceDir, { recursive: true, force: true });
    if (code !== 0) {
      if (match) fs.writeSync(2, "step cache: a stored passing run of the same reads exists; the cache would have passed this step\n");
      return;
    }
    const writes = ownWrites();
    const files = writtenFiles(writes, tree);
    if (match && m === "verify" && files && JSON.stringify(files) !== JSON.stringify(match.files ?? [])) {
      fs.writeSync(2, `step cache: a stored run of the same reads wrote other files (${files.map(([r]) => r).join(", ") || "none"}); the cache is unsound for this step\n`);
      process.exitCode = 1;
      return;
    }
    const why = [...trace.untraceable, ...(files ? [] : writes.map((w) => `a write to ${w}`))];
    const pair = WRITE_CHECK[command];
    const probes = ownProbes();
    try {
      let stored = why.length === 0;
      if (stored) storeStep(dir, { context, created: Date.now(), probes, output, ...(files!.length ? { files: files! } : {}) }, tree);
      // A writing run of a WRITE_CHECK pair that read only what it may and wrote one file stands for its checking form too.
      if (pair && argv.includes(pair.flag) && !pair.refuse.some((r) => argv.includes(r)) && trace.untraceable.size === 0 && writes.length === 1) {
        const file = writes[0]!;
        const checkArgv = argv.filter((a) => a !== pair.flag);
        const checkProbes: [string, string][] = [...probes.filter(([k]) => k !== `content\0${file}`), [`content\0${file}`, probeValue("content", file)]];
        const checkOutput = output.map(([fd, text]): [1 | 2, string] => [fd, fd === 1 ? text.split("\n").filter((l) => !pair.wrote.test(l)).join("\n") : text])
          .filter(([, text]) => text !== "");
        storeStep(dir, { context: stepContext(root, checkArgv, envBefore, codeKey), created: Date.now(), probes: checkProbes, output: checkOutput });
        stored = true;
      }
      if (!stored) fs.writeSync(2, `step cache: not stored (${why.slice(0, 3).join("; ")})\n`);
    } catch (e) { fs.writeSync(2, `step cache: not stored (${String(e)})\n`); }
  });
}

if (isMainThread && !process.env[TRACE_ID] && STEP_COMMANDS.has(process.argv[2] ?? "") && mode() !== "off") runStep(process.argv[2]!);

/** The planted step of the self-test: `step-cache-probe DIR [--write] [--stray] [--python] [--fail]` reads DIR/a.txt,
 * lists DIR/d, reads DIR/b.txt in a node child and DIR/c.txt in a worker, and prints what it read; --write writes
 * DIR/report.txt, and without it the run fails unless DIR/report.txt holds what it read; --stray writes beside DIR; --leak writes
 * DIR/leak.txt from a variable the context leaves out (a divergence for verify to find);
 * --python starts python3; --fail exits 1. */
export async function stepProbe(args: string[]): Promise<number> {
  const [dir] = args;
  if (args[0] === "--child") { process.stdout.write(fs.readFileSync(join(args[1]!, "b.txt"), "utf8")); return 0; }
  if (!dir) return 2;
  const a = fs.readFileSync(join(dir, "a.txt"), "utf8");
  const d = fs.readdirSync(join(dir, "d")).join(",");
  const b = cp.spawnSync(process.execPath, [process.argv[1]!, "step-cache-probe", "--child", dir], { encoding: "utf8" }).stdout;
  const c = await new Promise<string>((done, fail) => {
    const w = new wt.Worker(new URL("./step-cache-probe-worker.js", import.meta.url), { workerData: join(dir, "c.txt") });
    let text = "";
    w.once("message", (m: string) => { text = m; });
    w.once("error", fail);
    // A worker records its reads when it ends: the run waits for that, as the engine's pools do (TaskWorkers.close).
    w.once("exit", () => done(text));
  });
  if (args.includes("--python")) cp.spawnSync("python3", ["-c", "pass"]);
  if (args.includes("--stray")) fs.writeFileSync(join(dir, "..", "stray.txt"), "x");
  if (args.includes("--leak")) fs.writeFileSync(join(dir, "leak.txt"), process.env["BUILD_WORKERS"] ?? "");
  const text = `a=${a} b=${b} c=${c} d=${d}`;
  console.log(`probe: ${text}`);
  if (args.includes("--write")) { fs.writeFileSync(join(dir, "report.txt"), text); console.log(`probe: wrote ${join(dir, "report.txt")}`); }
  else if (!fs.existsSync(join(dir, "report.txt")) || fs.readFileSync(join(dir, "report.txt"), "utf8") !== text) { console.error("probe: report.txt is not what was read"); return 1; }
  return args.includes("--fail") ? 1 : 0;
}

/** Runs of the planted step in a temporary folder: reuse; misses on a change to what the process, its child or its
 * worker reads, a listing, or the environment; no record for a stray write, a python child or a failure; the writing
 * form's record standing for the checking form; verify and off always run. */
export function stepCacheSelfTest(): number {
  const problems: string[] = [];
  const tmp = real.mkdtempSync(join(tmpdir(), "step-cache-test."));
  const dir = join(tmp, "in");
  real.mkdirSync(join(dir, "d"), { recursive: true });
  for (const f of ["a", "b", "c"]) real.writeFileSync(join(dir, `${f}.txt`), f);
  const main = join(ROOT, "engine", "dist", "main.js");
  const run = (what: string, extra: string[], expect: "reused" | "ran" | "failed", env: Record<string, string> = {}): void => {
    const r = cp.spawnSync(process.execPath, [main, "step-cache-probe", dir, ...extra], { encoding: "utf8",
      env: { ...Object.fromEntries(Object.entries(process.env).filter(([k]) => !k.startsWith("ENGINE_TRACE") && k !== "BUILD_CACHE")), BUILD_CACHE_DIR: join(tmp, "cache"), ENGINE_CACHE_WORKTREE: dir, ...env } });
    const reused = r.stdout.includes("step cache: every file this run reads");
    const got = r.status !== 0 ? "failed" : reused ? "reused" : "ran";
    if (got !== expect) problems.push(`${what}: ${got}, expected ${expect} (${(r.stdout + r.stderr).trim().split("\n").slice(-2).join(" | ")})`);
  };
  try {
    run("checking form before any report", [], "failed");
    run("writing form", ["--write"], "ran");
    real.writeFileSync(join(dir, "report.txt"), "tampered");
    run("writing form again, its file changed since", ["--write"], "reused");
    if (real.readFileSync(join(dir, "report.txt"), "utf8") !== "a=a b=b c=c d=") problems.push("a reused writing run did not write its file again");
    run("checking form after the writing form (its record derived)", [], "reused");
    run("checking form again", [], "reused");
    real.writeFileSync(join(dir, "a.txt"), "a2");
    run("the process's own read changed", [], "failed");
    run("writing form after the change", ["--write"], "ran");
    run("checking form after it", [], "reused");
    real.writeFileSync(join(dir, "report.txt"), "tampered");
    run("the written file changed since", [], "failed");
    run("writing form, reused, writes its file again", ["--write"], "reused");
    run("checking form after it", [], "reused");
    // A change to what the child, the worker or the listing reads: the checking form is not reused (it runs, and fails on
    // the report written before the change), and after a new writing run it is.
    for (const [what, change] of [["the child's read", () => real.writeFileSync(join(dir, "b.txt"), "b2")],
      ["the worker's read", () => real.writeFileSync(join(dir, "c.txt"), "c2")],
      ["a listed folder's entries", () => real.writeFileSync(join(dir, "d", "e"), "")]] as const) {
      change();
      run(`${what} changed`, [], "failed");
      run(`writing form after ${what} changed`, ["--write"], "ran");
      run(`checking form after it`, [], "reused");
    }
    real.writeFileSync(join(tmp, "unread.txt"), "u");
    run("a file nobody reads added beside the folder", [], "reused");
    run("checking form with another environment", [], "ran", { STEP_CACHE_SELF_TEST: "1" });
    run("checking form with that environment again", [], "reused", { STEP_CACHE_SELF_TEST: "1" });
    run("checking form, only a worker count changed", [], "reused", { BUILD_WORKERS: "3" });
    run("a stray write (outside the worktree)", ["--stray"], "ran");
    run("a stray write again (not stored)", ["--stray"], "ran");
    run("a python child", ["--python"], "ran");
    run("a python child again (not stored)", ["--python"], "ran");
    run("a failing run", ["--fail"], "failed");
    run("verify mode", [], "ran", { BUILD_CACHE: "verify" });
    run("a run writing what its reads do not determine", ["--leak"], "ran", { BUILD_WORKERS: "1" });
    run("the same, reused", ["--leak"], "reused", { BUILD_WORKERS: "2" });
    run("the same in verify mode, which finds the divergence", ["--leak"], "failed", { BUILD_WORKERS: "2", BUILD_CACHE: "verify" });
    run("off", [], "ran", { BUILD_CACHE: "off" });
  } finally { real.rmSync(tmp, { recursive: true, force: true }); }
  for (const p of problems) console.error(`step-cache self-test: ${p}`);
  if (problems.length) return 1;
  console.log("step-cache self-test: ok (reuse; misses on a change read by the process, its child or its worker, a listing, the environment; nothing stored for a write outside the worktree, a python child or a failure; a writing run writes its files again; the writing form stands for the checking form; verify fails a divergence; off runs)");
  return 0;
}

// ---- self-test ----

/** The probes, the record and its reuse on a planted build in a temporary folder: a second build of the same inputs
 * is reused and restores its output; changing a file read, a directory listed, a path tested, the environment or the
 * code is not; a build that reads untraceably or writes outside its output is not stored. */
export async function buildCacheSelfTest(): Promise<number> {
  const problems: string[] = [];
  const root = real.mkdtempSync(join(tmpdir(), "build-cache-test."));
  const saved = { dir: process.env["BUILD_CACHE_DIR"], mode: process.env["BUILD_CACHE"] };
  process.env["BUILD_CACHE_DIR"] = join(root, "cache");
  delete process.env["BUILD_CACHE"];
  install();
  const out = join(root, "out");
  const src = join(root, "src");
  real.mkdirSync(join(src, "forms"), { recursive: true });
  real.mkdirSync(join(root, "engine", "dist"), { recursive: true });
  real.writeFileSync(join(root, "engine", "dist", "main.js"), "code 1");
  real.writeFileSync(join(src, "a.yaml"), "a: 1");
  real.writeFileSync(join(src, "forms", "f1.yaml"), "f: 1");
  let runs = 0;
  const planted = (extra?: () => void) => async (): Promise<BuildResult> => {
    runs++;
    const a = fs.readFileSync(join(src, "a.yaml"), "utf8");
    const forms = fs.readdirSync(join(src, "forms"));
    const opt = fs.existsSync(join(src, "optional.yaml"));
    extra?.();
    fs.rmSync(out, { recursive: true, force: true });
    fs.mkdirSync(out, { recursive: true });
    fs.writeFileSync(join(out, "result.json"), JSON.stringify({ a, forms, opt }));
    return { errors: [], stats: [`built ${forms.length} form(s)`] };
  };
  const build = (extra?: () => void) => { resetTrace(); return cachedBuild(out, 2025, planted(extra), { root, argv: ["build"] }); };
  const expect = async (what: string, b: () => Promise<BuildResult>, reused: boolean): Promise<void> => {
    const before = runs;
    const r = await b();
    const was = runs === before;
    if (was !== reused) problems.push(`${what}: ${reused ? "not reused" : "reused"}`);
    if (r.errors.length) problems.push(`${what}: errors ${r.errors.join("; ")}`);
  };
  try {
    await expect("first build", () => build(), false);
    const first = real.readFileSync(join(out, "result.json"), "utf8");
    await expect("same inputs", () => build(), true);
    real.writeFileSync(join(out, "result.json"), "tampered");
    await expect("same inputs, output tampered", () => build(), true);
    if (real.readFileSync(join(out, "result.json"), "utf8") !== first) problems.push("a reused build did not restore its output");
    real.writeFileSync(join(src, "a.yaml"), "a: 2");
    await expect("a file read changed", () => build(), false);
    real.writeFileSync(join(src, "forms", "f2.yaml"), "f: 2");
    await expect("a directory listed gained a file", () => build(), false);
    real.writeFileSync(join(src, "optional.yaml"), "o: 1");
    await expect("a path tested now exists", () => build(), false);
    await expect("unchanged again", () => build(), true);
    real.writeFileSync(join(src, "unread.yaml"), "u: 1");
    await expect("a file nobody reads added beside them", () => build(), true);
    process.env["BUILD_CACHE_SELF_TEST_VAR"] = "1";
    await expect("the environment changed", () => build(), false);
    process.env["BUILD_WORKERS"] = "3";
    await expect("only a worker count changed", () => build(), true);
    delete process.env["BUILD_WORKERS"];
    real.writeFileSync(join(root, "engine", "dist", "main.js"), "code 2");
    await expect("the code changed", () => build(), false);
    real.writeFileSync(join(src, "a.yaml"), "a: 3");
    await expect("a build that reads untraceably", () => build(() => { void fs.promises.readFile(join(src, "a.yaml")).catch(() => undefined); }), false);
    await expect("the same inputs after an untraceable build (not stored)", () => build(), false);
    real.writeFileSync(join(src, "a.yaml"), "a: 4");
    await expect("a build that writes outside its output", () => build(() => fs.writeFileSync(join(root, "stray.txt"), "x")), false);
    await expect("the same inputs after a stray write (not stored)", () => build(), false);
    process.env["BUILD_CACHE"] = "off";
    await expect("mode off", () => build(), false);
    process.env["BUILD_CACHE"] = "verify";
    await expect("mode verify", () => build(), false);
    // verify fails a build whose output its reads do not determine (here a counter), against its own earlier record.
    real.writeFileSync(join(root, "engine", "dist", "main.js"), "code 3");
    const leaky = async (): Promise<BuildResult> => {
      runs++;
      fs.rmSync(out, { recursive: true, force: true });
      fs.mkdirSync(out, { recursive: true });
      fs.writeFileSync(join(out, "result.json"), String(runs));
      return { errors: [], stats: ["leaky"] };
    };
    resetTrace();
    const once = await cachedBuild(out, 2025, leaky, { root, argv: ["build"] });
    resetTrace();
    const twice = await cachedBuild(out, 2025, leaky, { root, argv: ["build"] });
    if (once.errors.length) problems.push(`verify: the first build of an output its reads do not determine failed: ${once.errors.join("; ")}`);
    if (!twice.errors.some((e) => e.startsWith("build cache: a stored build of the same inputs gave other output (result.json)"))) problems.push(`verify: a build whose output differs from its record of the same inputs passed (${JSON.stringify(twice)})`);
  } catch (e) {
    problems.push(`threw: ${e instanceof Error ? e.stack ?? e.message : String(e)}`);
  } finally {
    if (saved.dir === undefined) delete process.env["BUILD_CACHE_DIR"]; else process.env["BUILD_CACHE_DIR"] = saved.dir;
    if (saved.mode === undefined) delete process.env["BUILD_CACHE"]; else process.env["BUILD_CACHE"] = saved.mode;
    delete process.env["BUILD_CACHE_SELF_TEST_VAR"];
    real.rmSync(root, { recursive: true, force: true });
  }
  for (const p of problems) console.error(`build-cache self-test: ${p}`);
  if (problems.length) return 1;
  console.log("build-cache self-test: ok (reuse, output restored; misses on a changed read, listing, existence, environment and code; untraceable reads and stray writes not stored; verify fails an output its reads do not determine)");
  return 0;
}
