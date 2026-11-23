// An interview-coverage worker: loads the context once (loadCtx in interview-coverage.ts), sends the tax year it
// loaded, then walks each row it is sent (walkRow). The tax year comes from the main thread, put on the command line
// before year.ts loads.
// First: a traced step records this worker's reads too (build-cache.ts).
import "./build-cache.js";
import { workerData } from "node:worker_threads";
import { serveTasks } from "./pool.js";

const { year } = workerData as { year: number };
process.argv.push("--year", String(year));
const { loadCtx, walkRow } = await import("./interview-coverage.js");
const { YEAR } = await import("./year.js");
type WalkTask = import("./interview-coverage.js").WalkTask;
const ctx = loadCtx();
serveTasks(YEAR, (t: WalkTask) => walkRow(ctx, t.row, t.file));
