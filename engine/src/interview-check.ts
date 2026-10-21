// Build-time finite path checks. Numeric/collection representatives come from
// synthetic fixtures; finite enum/Boolean domains are exhaustively enumerated
// over the questions the interview actually asks: the walk branches on every
// value of a finite question when it is asked, so each distinct path runs once
// and inputs the interview never reaches add no work.
import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import { isDeepStrictEqual } from "node:util";
import { interviewState, replay, type InterviewData } from "./interview.js";
import type { CanonicalData, Inputs } from "./types.js";
import { yearPath } from "./year.js";

export function checkInterview(data: CanonicalData, config: InterviewData, paths?: string[]): string[] {
  const errors: string[] = [];
  const fixtures = (JSON.parse(readFileSync(yearPath("fixtures", "stage2.json"),"utf8")) as {cases:{id:string;inputs:Inputs}[]}).cases;
  const domain = (key: string): unknown[] | undefined => {
    const template = key.replace(/(?:[a-zA-Z0-9_]+\[[^\]]+\]\.)+/g, m => m.split(".").filter(Boolean).at(-1)!.split("[")[0]+".");
    const line = data.forms.flatMap(d=>d.lines).find(l=>l.id===template);
    if (line?.type === "Bool") return [false,true];
    if (line?.type.startsWith("Enum(")) return data.params.enums[line.type.slice(5,-1)]!.values;
    return undefined;
  };
  for (const fixture of fixtures) {
    if (fixture.id === "ss.early.refusal") continue;
    if (JSON.stringify(fixture.inputs["$person"]) !== JSON.stringify(config.initial["$person"])) continue;
    const walk = (current: Inputs, events: {input:string;value:unknown}[]): void => {
      try {
        if (events.length >= 100) throw new Error("path did not terminate");
        const state=interviewState(data,config,current);
        if(state.status!=="incomplete") {
          paths?.push(`${fixture.id} ${JSON.stringify(events)}`);
          const reversed=replay(config,[{version:1,tax_year:config.tax_year},...events.toReversed()]);
          const b=interviewState(data,config,reversed);
          if(!isDeepStrictEqual(state.values,b.values)||state.status!==b.status) throw new Error("answer order changes result");
          return;
        }
        const question=state.question;
        if(!question || !(question.input in fixture.inputs)) throw new Error(`missing reachable question/representative ${question?.input}`);
        if(question.input in current) throw new Error(`repeated question ${question.input}`);
        if(!state.reachableInputs.includes(question.input)) throw new Error("irrelevant question");
        for (const value of domain(question.input) ?? [fixture.inputs[question.input]])
          walk({...current,[question.input]:value}, [...events,{input:question.input,value}]);
      } catch(e) {errors.push(`${fixture.id}: ${String(e)}`);}
    };
    walk(structuredClone(config.initial), []);
  }
  return errors;
}

// Sales fixtures cover complete paths and refusal paths. Unlike the Stage 2
// enumeration above, this is representative coverage, not a Cartesian proof.
export function checkSalesInterview(data: CanonicalData, config: InterviewData, stage = "stage3"): string[] {
  const errors: string[]=[];
  const fixtures=JSON.parse(readFileSync(yearPath("fixtures", `${stage}.json`),"utf8")) as {cases:{id:string;inputs:Inputs}[]};
  for (const fixture of fixtures.cases) {
    try {
      let current: Inputs=structuredClone(config.initial);
      const events:{input:string;value:unknown}[]=[];
      let ended=false;
      for(let step=0;step<200;step++) {
        const state=interviewState(data,config,current);
        if(state.status!=="incomplete") {ended=true;break;}
        const key=state.question?.input;
        if(!key || !(key in fixture.inputs) || key in current) throw new Error(`missing or repeated question ${key}`);
        if(!state.reachableInputs.includes(key)) throw new Error(`irrelevant question ${key}`);
        events.push({input:key,value:fixture.inputs[key]});
        current={...current,[key]:fixture.inputs[key]};
      }
      if(!ended) throw new Error("path did not terminate");
      const reversed=replay(config,[{version:1,tax_year:config.tax_year},...events.toReversed()]);
      const a=interviewState(data,config,current), b=interviewState(data,config,reversed);
      if(!isDeepStrictEqual(a.values,b.values)||a.status!==b.status)throw new Error("answer order changes result");
    } catch(e) {errors.push(`${fixture.id}: ${String(e)}`);}
  }
  return errors;
}
