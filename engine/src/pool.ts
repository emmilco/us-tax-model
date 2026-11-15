// A bounded pool for the test commands (test-fixtures, test-integration, test-serve), which run independent
// command-line invocations, and for interview-rules, which runs independent walks on worker threads: results come back
// in input order whatever order the work finishes in.
import { spawn } from "node:child_process";
import { availableParallelism } from "node:os";
import { parentPort, Worker } from "node:worker_threads";

// The default size of a worker pool: the core count less six (left for the steps check-all runs beside
// the pool), but at most an equal share, among CHECK_ALL_MAX_RUNS runs (default 2, tools/check_slot.py), of
// the cores less two, so that the runs allowed at once together fit the machine.
export function defaultWorkers(): number {
  const cores = availableParallelism();
  const runs = Number(process.env.CHECK_ALL_MAX_RUNS);
  const share = Math.floor((cores - 2) / (Number.isInteger(runs) && runs > 0 ? runs : 2));
  return Math.max(1, Math.min(cores - 6, share));
}

// Concurrent invocations: TEST_WORKERS, or defaultWorkers(); one runs them serially.
export function poolSize(): number {
  const set = Number(process.env.TEST_WORKERS);
  return Number.isInteger(set) && set > 0 ? set : defaultWorkers();
}

// fn over every item, at most `limit` at a time; the results in the order of the items. If any call rejects,
// the rejection of the earliest item is thrown once every call has settled, as a serial run would meet it first.
export async function mapPool<T, R>(items: readonly T[], fn: (item: T, index: number) => Promise<R>, limit = poolSize()): Promise<R[]> {
  const settled: PromiseSettledResult<R>[] = new Array(items.length);
  let next = 0;
  const lane = async (): Promise<void> => {
    while (next < items.length) {
      const i = next++;
      try { settled[i] = { status: "fulfilled", value: await fn(items[i]!, i) }; } catch (reason) { settled[i] = { status: "rejected", reason }; }
    }
  };
  await Promise.all(Array.from({ length: Math.max(1, Math.min(limit, items.length)) }, lane));
  return settled.map((s) => { if (s.status === "rejected") throw s.reason; return s.value; });
}

// A gate that lets `limit` calls of fn through at a time, in the order they ask.
export function gate(limit = poolSize()): <T>(fn: () => Promise<T>) => Promise<T> {
  let active = 0;
  const waiting: (() => void)[] = [];
  return async <T>(fn: () => Promise<T>): Promise<T> => {
    if (active >= limit) await new Promise<void>((go) => waiting.push(go)); // a finishing call hands its slot over
    else active++;
    try { return await fn(); } finally { const go = waiting.shift(); if (go) go(); else active--; }
  };
}

export interface Run { status: number | null; stdout: string; stderr: string }

// Runs a program to completion, as spawnSync does with encoding utf-8 and no output limit.
export function run(program: string, args: string[]): Promise<Run> {
  return new Promise((done, fail) => {
    const proc = spawn(program, args, { stdio: ["ignore", "pipe", "pipe"] });
    const out: Buffer[] = [], err: Buffer[] = [];
    proc.stdout.on("data", (c: Buffer) => out.push(c));
    proc.stderr.on("data", (c: Buffer) => err.push(c));
    proc.on("error", fail);
    proc.on("close", (status) => done({ status, stdout: Buffer.concat(out).toString("utf8"), stderr: Buffer.concat(err).toString("utf8") }));
  });
}

// The size of the pool of a walk step (interview-length, interview-coverage): the environment variable `name` when it
// is a positive whole number, else defaultWorkers(), as for mutate and interview-rules. One runs the walk in the
// calling thread, with no workers.
export function walkWorkers(name: string): number {
  const set = Number(process.env[name]);
  return Number.isInteger(set) && set > 0 ? set : defaultWorkers();
}

type Reply<R> = { ok: true; result: R } | { ok: false; error: string };

// Worker threads started from `url` with `workerData`, each serving tasks one at a time (serveTasks, on the worker's
// side). `ready` resolves to the first message of each worker, which it sends once it has loaded (what it loaded,
// for the caller to compare with its own). A worker that fails while loading rejects `ready`.
export class TaskWorkers<T, R> {
  private idle: Worker[] = [];
  private all: Worker[] = [];
  private exited = new Map<Worker, Promise<void>>();
  readonly ready: Promise<unknown[]>;
  constructor(url: URL, count: number, workerData: unknown) {
    const hellos: Promise<unknown>[] = [];
    for (let i = 0; i < count; i++) {
      const w = new Worker(url, { workerData });
      this.exited.set(w, new Promise((done) => w.once("exit", () => done())));
      this.all.push(w);
      this.idle.push(w);
      hellos.push(new Promise((done, fail) => {
        const onError = (e: Error) => fail(e);
        w.once("error", onError);
        w.once("message", (m: unknown) => { w.off("error", onError); done(m); });
      }));
    }
    this.ready = Promise.all(hellos);
  }
  run(task: T): Promise<R> {
    const w = this.idle.pop();
    if (!w) throw new Error("TaskWorkers: no idle worker (the pool's limit is the worker count)");
    return new Promise((done, fail) => {
      const onError = (e: Error) => { w.off("message", onMessage); fail(e); };
      const onMessage = (m: Reply<R>) => {
        w.off("error", onError);
        this.idle.push(w);
        if (m.ok) done(m.result); else fail(new Error(m.error));
      };
      w.once("message", onMessage);
      w.once("error", onError);
      w.postMessage(task);
    });
  }
  /** The task of each item, run on the workers; the results in the order of the items (mapPool). */
  map<I>(items: readonly I[], task: (item: I, index: number) => T): Promise<R[]> {
    return mapPool(items, (item, i) => this.run(task(item, i)), this.all.length);
  }
  /** Asks each worker to end and waits until all have ended (one that failed has ended already): a worker that ends
   * of itself runs its exit handlers, as a terminated one does not. */
  async close(): Promise<void> {
    for (const w of this.all) w.postMessage(null);
    await Promise.all(this.exited.values());
  }
}

// The worker's side of TaskWorkers: sends `hello`, then answers each task posted with fn's result (or its error),
// and ends when it is sent null.
export function serveTasks<T, R>(hello: unknown, fn: (task: T) => R): void {
  const port = parentPort!;
  port.postMessage(hello);
  port.on("message", (task: T | null) => {
    if (task === null) { port.close(); return; }
    let reply: Reply<R>;
    try { reply = { ok: true, result: fn(task) }; } catch (e) { reply = { ok: false, error: e instanceof Error ? e.stack ?? e.message : String(e) }; }
    port.postMessage(reply);
  });
}
