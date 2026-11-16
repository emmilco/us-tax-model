// Build-time path check: each fixture a profile walks is answered through the interview, question by question,
// and must reach its end. Every answer becomes its event through `answerEvent` and the state is the log
// replayed, as for every client of the interview.
import { answerEvent, interviewStatus, replay, replayState, type Event, type InterviewData } from "./interview.js";
import type { CanonicalData, Inputs } from "./types.js";

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
