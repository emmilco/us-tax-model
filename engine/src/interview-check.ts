// Build-time path check: each fixture a profile walks is answered through the interview, question by question,
// and must reach its end. Every answer becomes its event through `answerEvent` and the state is the log
// replayed, as for every client of the interview.
import { isDeepStrictEqual } from "node:util";
import { answerEvent, interviewStatus, loadInterview, replay, replayState, type Event, type InterviewData } from "./interview.js";
import { loadCanonical } from "./canonical.js";
import { walkedCases } from "./fixture-inputs.js";
import type { CanonicalData, Inputs } from "./types.js";
import { TaskWorkers } from "./pool.js";
import { YEAR } from "./year.js";

// The fixtures cover complete paths and refusal paths: representative coverage, not a Cartesian proof.
// `cases`: the fixture cases the profile walks, inputs resolved (fixture-inputs.ts).
export function checkInterviewPaths(data: CanonicalData, config: InterviewData, cases: { id: string; inputs: Inputs }[], maxSteps = 200): string[] {
  const errors: string[]=[];
  for (const fixture of cases) {
    try {
      const header: Event = {version:1,tax_year:config.tax_year};
      let replayed=replayState(config,[header]);
      let current: Inputs=replayed.inputs;
      const events: Event[]=[];
      let ended=false;
      // Each step answers a distinct input of the fixture (a repeat throws), so a path takes at most one step
      // per input plus the final check: the bound is exact, not a guess.
      const bound=Math.max(maxSteps,Object.keys(fixture.inputs).length+1);
      for(let step=0;step<bound;step++) {
        const state=interviewStatus(data,config,current);
        if(state.status!=="incomplete") {ended=true;break;}
        const key=state.question?.input;
        if(!key || !(key in fixture.inputs) || key in current) throw new Error(`missing or repeated question ${key}`);
        if(!state.reachableInputs.includes(key)) throw new Error(`irrelevant question ${key}`);
        const event=answerEvent(config,replayed,key,fixture.inputs[key]);
        // What the choice records must be what the fixture states: otherwise the interview cannot produce this return.
        for(const r of event.records??[]) if(r.input in fixture.inputs && JSON.stringify(fixture.inputs[r.input])!==JSON.stringify(r.value)) throw new Error(`the answer to ${key} records ${r.input} = ${JSON.stringify(r.value)}, and the fixture states ${JSON.stringify(fixture.inputs[r.input])}`);
        events.push(event);
        replayed=replayState(config,[header,...events]);
        current=replayed.inputs;
      }
      if(!ended) throw new Error("path did not terminate");
      const reversed=replay(config,[header,...events.toReversed()]);
      const a=interviewStatus(data,config,current), b=interviewStatus(data,config,reversed);
      if(a.valuesKey()!==b.valuesKey()||a.status!==b.status)throw new Error("answer order changes result");
    } catch(e) {errors.push(`${fixture.id}: ${String(e)}`);}
  }
  return errors;
}

// checkInterviewPaths on `workers` worker threads (interview-check-worker.ts), one case per task. A case's errors depend
// only on the data, the profile and that case, and are returned in the order of the cases, so the result is the same
// for every worker count; one, or a single case, checks them in this thread.
export async function checkInterviewPathsOn(data: CanonicalData, config: InterviewData, cases: { id: string; inputs: Inputs }[], maxSteps: number, workers: number): Promise<string[]> {
  if (workers <= 1 || cases.length < 2) return checkInterviewPaths(data, config, cases, maxSteps);
  const pool = new TaskWorkers<number, string[]>(new URL("./interview-check-worker.js", import.meta.url), Math.min(workers, cases.length), { year: YEAR, data, config, cases, maxSteps });
  try {
    if ((await pool.ready).some((y) => y !== YEAR)) throw new Error("interview path checks: a worker loaded another tax year");
    return (await pool.map(cases, (_, i) => i)).flat();
  } finally { await pool.close(); }
}

// The self-test of checkInterviewPathsOn, on the built data (canonical/<year>/) and the federal walked fixtures: a few
// of them and two broken copies (no answers; half the answers), checked here and on three workers, must give the same
// errors in the same order, the broken copies at least one each.
export async function pathsSelfTest(): Promise<number> {
  const data = loadCanonical();
  const config = loadInterview("full");
  const good = walkedCases("full", data).slice(0, 3);
  if (good.length === 0) { console.error("interview-paths self-test: no federal walked fixtures"); return 1; }
  const half = Object.fromEntries(Object.entries(good[0]!.inputs).slice(0, Math.floor(Object.keys(good[0]!.inputs).length / 2)));
  const broken = [{ id: "self-test-no-answers", inputs: {} }, { id: "self-test-half-answers", inputs: half }];
  const cases = [broken[0]!, ...good, broken[1]!];
  const serial = checkInterviewPaths(data, config, cases);
  const pooled = await checkInterviewPathsOn(data, config, cases, 200, 3);
  const problems: string[] = [];
  if (!isDeepStrictEqual(serial, pooled)) problems.push(`the errors on three workers differ from the errors in one thread:\n  ${JSON.stringify(serial)}\n  ${JSON.stringify(pooled)}`);
  for (const b of broken) if (!serial.some((e) => e.startsWith(`${b.id}: `))) problems.push(`the broken case ${b.id} gave no error`);
  for (const p of problems) console.error(`interview-paths self-test: ${p}`);
  if (problems.length) return 1;
  console.log(`interview-paths self-test: ok (${cases.length} cases, ${serial.length} errors, the same on one thread and three workers)`);
  return 0;
}
