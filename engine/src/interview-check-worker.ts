// A worker of the build's interview path checks (checkInterviewPathsOn in interview-check.ts): it is given the built
// data, the profile and the cases once, sends the tax year it loaded, then checks each case whose index it is sent,
// answering with that case's errors. The tax year comes from the main thread, put on the command line before year.ts
// loads.
// First: a build that records its reads records this worker's too (build-cache.ts).
import "./build-cache.js";
import { workerData } from "node:worker_threads";
import { serveTasks } from "./pool.js";
import type { CanonicalData, Inputs } from "./types.js";
import type { InterviewData } from "./interview.js";

const { year, data, config, cases, maxSteps } = workerData as {
  year: number; data: CanonicalData; config: InterviewData; cases: { id: string; inputs: Inputs }[]; maxSteps: number;
};
process.argv.push("--year", String(year));
const { checkInterviewPaths } = await import("./interview-check.js");
const { YEAR } = await import("./year.js");
serveTasks(YEAR, (i: number) => checkInterviewPaths(data, config, [cases[i]!], maxSteps));
