// A bounded pool for the test commands (test-fixtures, test-integration, test-serve), which run independent
// command-line invocations: results come back in input order whatever order the work finishes in.
import { spawn } from "node:child_process";
import { availableParallelism } from "node:os";

// Concurrent invocations: TEST_WORKERS, or the core count less six (left for the steps check-all runs
// beside these); one runs them serially.
export function poolSize(): number {
  const set = Number(process.env.TEST_WORKERS);
  return Number.isInteger(set) && set > 0 ? set : Math.max(1, availableParallelism() - 6);
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
