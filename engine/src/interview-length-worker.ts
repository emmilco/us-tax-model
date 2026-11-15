// An interview-length worker: builds the context and the list of returns as the main thread does, sends the list's
// digest, then measures each return it is sent by index (measureCase in interview-length.ts). The tax year comes from
// the main thread, put on the command line before year.ts loads.
import { workerData } from "node:worker_threads";
import { serveTasks } from "./pool.js";

const { year } = workerData as { year: number };
process.argv.push("--year", String(year));
const { casesDigest, casesOf, context, measureCase } = await import("./interview-length.js");
const ctx = context();
const cases = casesOf(ctx);
serveTasks(casesDigest(cases), (i: number) => measureCase(ctx, cases[i]!));
