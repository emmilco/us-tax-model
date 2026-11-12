// Integration checks invoke the command-line backend, including negative cases.
import assert from "node:assert/strict";
import { mkdtempSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { loadCanonical } from "./canonical.js";
import { runChecks } from "./check.js";
import { loadCases } from "./fixtures.js";
import type { CanonicalData, Inputs } from "./types.js";
import { YEAR, YEAR_ARGS } from "./year.js";
import { gate, mapPool, run } from "./pool.js";

// The checks fall into groups that share nothing (each has its own log and files); the groups run side by side,
// their command-line invocations passing through one gate (pool.ts), and the error of the earliest failing
// group is thrown once all have finished.
export async function integrationChecks(): Promise<void> {
  const dir=mkdtempSync(join(tmpdir(),"stage2-integration-"));
  let checks=0;
  const through=gate();
  const main=(args:string[])=>through(()=>run(process.execPath,[resolve(import.meta.dirname,"main.js"),...YEAR_ARGS,...args]));
  const cli=async(args:string[],ok=true):Promise<any>=>{
    const p=await main(args);
    assert.equal(p.status===0,ok,`${args.join(" ")}: ${p.stderr || p.stdout}`);
    checks++;
    return ok ? JSON.parse(p.stdout) : null;
  };
  let inputFiles=0;
  const evaluate=(inputs:Inputs,ok=true,target="f1040.line31")=>{
    const path=join(dir,`inputs-${inputFiles++}.json`);writeFileSync(path,JSON.stringify(inputs));
    return cli(["eval","--inputs",path,"--target",target,"--json"],ok);
  };
  const groups:(()=>Promise<void>)[]=[];
  try {
    const fixture=loadCases().cases.find(c=>c.id==="ss.multi")!;
    const inputs=fixture.inputs;
    groups.push(async()=>{
      const log=join(dir,"answers.jsonl");
      let state=await cli(["interview","start","--log",log]);
      const answer=(key:string,value:unknown)=>cli(["interview","answer","--log",log,"--input",key,"--value",JSON.stringify(value)]);
      assert.equal(state.question.input,"f1040.status");
      state=await answer("f1040.status",null);
      assert.equal(state.status,"incomplete");assert.equal(state.question.helpRequested,true);
      let steps=0;
      while(state.status==="incomplete"&&steps++<30){
        const key=state.question.input;assert.ok(key in inputs,key);
        state=await answer(key,inputs[key]);
      }
      assert.equal(state.status,"complete");
      assert.deepEqual(state.values["f1040.line31"].value,{kind:"money",cents:148180});
      assert.match(state.sheet,/\$1,481\.80/);assert.match(state.sheet,/sha|482e9c|i1040gi/);
      const before=readFileSync(log,"utf8");
      state=await answer("person[taxpayer].w2[a].box4",1091821);
      assert.equal(state.status,"refused");assert.match(state.refusal.remedy,/Form 843/);
      assert.ok(readFileSync(log,"utf8").startsWith(before));
      state=await answer("person[taxpayer].w2[a].box4",620000);assert.equal(state.status,"complete");
      state=await answer("$w2@person[taxpayer]",["a"]);assert.equal(state.values["f1040.line31"].value.cents,0);
      state=await answer("$w2@person[taxpayer]",["a","b"]);assert.equal(state.status,"complete");
      await cli(["interview","start","--log",log],false); // never overwrite a log
    });
    groups.push(async()=>{
      const early={...inputs};delete early["person[taxpayer].w2[b].box4"];
      delete early["person[taxpayer].w2[a].box3"];early["person[taxpayer].w2[a].box4"]=1091821;
      assert.equal((await evaluate(early)).values["f1040.line31"].value.kind,"refusal");
    });
    // Cross-document references are memoized under the target line's key, not an alias of
    // the caller's collection frame (audit 1.1: person[taxpayer].f8606[form].person.x).
    groups.push(async()=>{
      const data=loadCanonical();
      const ids=new Set(data.forms.map(f=>f.id));
      const probe=await evaluate(inputs);
      const alias=Object.keys(probe.values).filter(k=>{
        let bracketed=false;
        for(const seg of k.split(".")){
          if(seg.includes("["))bracketed=true;
          else if(bracketed&&ids.has(seg))return true;
        }
        return false;
      });
      assert.deepEqual(alias,[],`cross-document aliases in values: ${alias.join(",")}`);checks++;
    });
    // T-096: an interval tiling whose first bound is above the operand's domain and has no
    // cited precondition must fail the checker.
    groups.push(async()=>{
      const data=loadCanonical();
      const tcw=data.defs.find(d=>d.id==="tcw")!;
      const line=tcw.lines.find(l=>l.id==="single.result")!;
      const alt=(line.expr as any).alternatives[0];
      alt.guard.all[0].ge[1]={const:20000000};
      line.label="Section A—Use if your filing status is Single. Tax.";
      const errors=runChecks(data).errors;
      assert.ok(errors.some(e=>e.includes("values below the first bound")),`T-096 regression: ${errors.slice(0,3).join("; ")}`);checks++;
    });
    groups.push(async()=>{
      const missing={...inputs};delete missing["$w2@person[taxpayer]"];
      for(const k of Object.keys(missing))if(k.includes(".w2["))delete missing[k];
      assert.equal((await evaluate(missing)).values["f1040.line31"].value.kind,"unknown");
    });
    // Spec 8: the standing notices close every JSON result, once per batch.
    groups.push(async()=>{
      const notice=(n:unknown)=>Array.isArray(n)&&n.some(s=>String(s).includes("not tax or legal advice"))&&n.some(s=>String(s).includes("responsible for the return"));
      assert.ok(notice((await evaluate(inputs)).notices),"eval --json carries the standing notices");checks++;
      const batchPath=join(dir,"batch.json");writeFileSync(batchPath,JSON.stringify([{id:"one",inputs}]));
      const batch=await cli(["eval","--batch",batchPath,"--target","f1040.line31"]);
      assert.ok(notice(batch.notices)&&batch.cases.one.values&&!("notices" in batch.cases.one),"eval --batch carries the standing notices once");checks++;
    });
    groups.push(async()=>{
      await Promise.all([-1,0.5,"100",Number.MAX_SAFE_INTEGER+1].map(bad=>evaluate({...inputs,"person[taxpayer].w2[a].box4":bad as number},false)));
      await evaluate({...inputs,"$w2@person[taxpayer]":["a","a"]},false);
      await evaluate({...inputs,"person[taxpayer].w2[ghost].box4":1},false);
      await evaluate({...inputs,"person[taxpayer].w2[a].box3":Number.MAX_SAFE_INTEGER,"person[taxpayer].w2[a].box7":1},false);
    });
    // At most one person entry has role taxpayer: a second one is an input error, while the same
    // second entry as a spouse evaluates (the roster refusal handles a spouse the status does not allow).
    groups.push(async()=>{
      const people=(inputs["$person"] as string[]|undefined)??["taxpayer"];
      await evaluate({...inputs,"$person":[...people,"t2"],"person[t2].role":"taxpayer"},false);
      await evaluate({...inputs,"$person":[...people,"t2"],"person[t2].role":"spouse"});
    });
    groups.push(async()=>{
      const htmlPath=join(dir,"html-input.json");writeFileSync(htmlPath,JSON.stringify(inputs));
      const html=await main(["eval","--inputs",htmlPath,"--target","f1040.line31","--html"]);
      assert.equal(html.status,0);assert.match(html.stdout,/<!doctype html>/);assert.match(html.stdout,/\$1,481\.80/);checks++;
    });
    // Entry sections: a business, its implicit Form 4562 after it, and each asset with only the
    // lines Form 4562 reports it on (a listed asset on 25 and 26, the other on 14 and 19).
    groups.push(async()=>{
      const assetCase=loadCases().cases.find(c=>c.id==="stage14.asset.listed_and_not")!;
      const sheetPath=join(dir,"sheet-input.json");writeFileSync(sheetPath,JSON.stringify(assetCase.inputs));
      const sheet=await main(["eval","--inputs",sheetPath]);
      assert.equal(sheet.status,0);
      const section=(entry:string)=>{const parts=sheet.stdout.split(/\n(?=== )/);const s=parts.find(p=>p.split("\n")[0]!.endsWith(`— ${entry} ==`));assert.ok(s,`no section for ${entry}`);return s!;};
      const order=sheet.stdout.indexOf("— person[taxpayer].sc[d] =="), f4562=sheet.stdout.indexOf("— person[taxpayer].sc[d].f4562[form] ==");
      assert.ok(order>=0&&f4562>order,"the Form 4562 section follows its Schedule C");checks++;
      const printed=(s:string)=>s.split("\n").slice(1).filter(l=>/^ {2}\S/.test(l)).map(l=>l.trim().split(/\s+/)[0]);
      const cam=printed(section("person[taxpayer].sc[d].asset[cam]")), pc=printed(section("person[taxpayer].sc[d].asset[pc]"));
      assert.ok(cam.includes("25")&&cam.includes("26(h)")&&!cam.includes("14")&&!cam.includes("19(g)"),`listed asset lines: ${cam.join(",")}`);checks++;
      assert.ok(pc.includes("14")&&pc.includes("19(g)")&&!pc.includes("25")&&!pc.includes("26(h)"),`other asset lines: ${pc.join(",")}`);checks++;
    });
    const checksData=loadCanonical();
    let badFiles=0;
    const badData=(change:(d:CanonicalData)=>void)=>{
      const d=structuredClone(checksData);change(d);const path=join(dir,`bad-${badFiles++}.json`);writeFileSync(path,JSON.stringify(d));return cli(["check",path],false);
    };
    const line=(d:CanonicalData,id:string)=>d.forms.flatMap(f=>f.lines).find(l=>l.id===id)!;
    groups.push(async()=>{
      await Promise.all([
        badData(d=>{line(d,"person.over").expr={op:"test",eq:["person.over",{const:true}]};}),
        // shown_when must name a Bool line of the same document; an implicit collection needs a parent.
        badData(d=>{line(d,"asset.bonus").shown_when="asset.cost";}),
        // ... and may hide a printed or worksheet line, never a helper.
        badData(d=>{line(d,"s8812.show13").shown_when="s8812.clwb_complete";}),
        badData(d=>{const f=d.forms.find(x=>x.id==="f4562")!;f.collection={implicit:"form",cite:f.collection!.cite};}),
        badData(d=>{line(d,"person.credit").expr={op:"choose",alternatives:[{guard:{op:"test",eq:["person.credit",{const:0}]},then:"person.zero"}]};}),
        badData(d=>{line(d,"person.withheld").expr={op:"sum_over",collection:"w2",field:"w2.over"};}),
        badData(d=>{line(d,"person.withheld").expr={op:"sum_over",collection:"w2",field:"f1040.line15"};}),
        badData(d=>{line(d,"s3.line11").expr={op:"sum_over",collection:"w2",field:"w2.box4"};}),
        badData(d=>{line(d,"person.employers").expr={op:"sum_over",collection:"w2",field:"w2.one",where:{op:"test",eq:["missing.field",{const:true}]}};}),
        badData(d=>{line(d,"person.over").expr={op:"test",gt:["person.overcount",{const:0}]};}),
        // A filter edge back to the aggregate must not escape the cycle walk.
        badData(d=>{line(d,"w2.over").expr={op:"test",gt:["person.overcount",{const:0,type:"Count"}]};}),
      ]);
    });
    // Sales profile: complete, corrected refusal, restored roster, and early digital refusal.
    for (const id of ["sales.official.basis", "sales.official.two_aggregate", "sales.refuse.digital.G", "sales.select.sdtw.election"]) {
      groups.push(async()=>{
        const sales = loadCases().cases.find(c=>c.id===id)!;
        const salesLog=join(dir,id+".jsonl");
        let salesState=await cli(["interview","start","--profile","sales","--log",salesLog]);
        let count=0;
        while(salesState.status==="incomplete" && count++<150) {
          const key=salesState.question.input;
          assert.ok(key in sales.inputs, `missing sales input ${key}`);
          salesState=await cli(["interview","answer","--log",salesLog,"--input",key,"--value",JSON.stringify(sales.inputs[key])]);
        }
        assert.equal(salesState.status, id.includes("refuse") ? "refused" : "complete");
        if (id==="sales.official.basis") {
          assert.equal(salesState.values["f1040.line7a"].value.cents,90000);
          const correction=(input:string,value:unknown)=>cli(["interview","answer","--log",salesLog,"--input",input,"--value",JSON.stringify(value)]);
          salesState=await correction("sales[a].box","G"); assert.equal(salesState.status,"refused");
          salesState=await correction("sales[a].box","A"); assert.equal(salesState.status,"complete");
          salesState=await correction("$sales",[]); assert.equal(salesState.values["f1040.line7a"].value.cents,0);
          salesState=await correction("$sales",["a"]); assert.equal(salesState.values["f1040.line7a"].value.cents,90000);
          await cli(["interview","advance","--profile","social-security","--log",salesLog],false);
        }
      });
    }
    groups.push(async()=>{
      const sale=loadCases().cases.find(c=>c.id==="sales.official.basis")!.inputs;
      await evaluate({...sale,"$sales":["a","a"]},false,"f1040.line7a");
      await evaluate({...sale,"sales[a].wash_loss":-1},false,"f1040.line7a");
      await evaluate({...sale,"sales[a].box":"Z"},false,"f1040.line7a");
      assert.equal((await evaluate({...sale,"$sales":["a","missing"]},true,"f1040.line7a")).values["f1040.line7a"].value.kind,"unknown");
    });
    groups.push(async()=>{
      await badData(d=>{line(d,"sd.limited_loss").expr={op:"larger_of",of:["sd.limited_loss","sd.loss_limit"]};});
    });
    for(const id of ["stage4.base","stage4.sdtw.special_rates","stage4.refuse.scope.schedule1"]) {
      groups.push(async()=>{
        const fixture=loadCases().cases.find(c=>c.id===id)!;
        const path=join(dir,id+".jsonl");
        let state=await cli(["interview","start","--profile","stage4","--log",path]);
        for(let step=0;state.status==="incomplete"&&step<150;step++) {
          const key=state.question.input;assert.ok(key in fixture.inputs,`missing ${key}`);
          state=await cli(["interview","answer","--log",path,"--input",key,"--value",JSON.stringify(fixture.inputs[key])]);
        }
        assert.equal(state.status,id.includes("refuse")?"refused":"complete");
        if(id==="stage4.sdtw.special_rates")assert.equal(state.values["f1040.line16"].value.cents,6166300);
        if(id==="stage4.base") {
          assert.equal(state.values["sa.deduction"].value.cents,1575000);
          state=await cli(["interview","answer","--log",path,"--input","sa.line8a","--value","2000000"]);
          assert.equal(state.values["sa.deduction"].value.cents,2000000);
          await cli(["interview","answer","--log",path,"--input","f8959.line18","--value","1"],false);
        }
      });
    }
    for(const id of ["stage5.return.owed","stage5.return.refund"]) {
      groups.push(async()=>{
        const fixture=loadCases().cases.find(c=>c.id===id)!;
        const path=join(dir,id+".jsonl");
        let state=await cli(["interview","start","--profile","full","--log",path]);
        for(let step=0;state.status==="incomplete"&&step<200;step++) {
          const key=state.question.input;assert.ok(key in fixture.inputs,`missing ${key}`);
          state=await cli(["interview","answer","--log",path,"--input",key,"--value",JSON.stringify(fixture.inputs[key])]);
        }
        assert.equal(state.status,"complete");
        if(id==="stage5.return.owed")assert.equal(state.values["f1040.line37"].value.cents,150000);
        if(id==="stage5.return.refund")assert.equal(state.values["f1040.line34"].value.cents,173300);
      });
    }
    // The opening of the whole return: one question for a couple, two for one person, and the answers the first
    // question's choice records (each entry's role; the couple's filing status).
    groups.push(async()=>{
      const path=join(dir,"opening.jsonl");
      const answer=(key:string,value:unknown,ok=true)=>cli(["interview","answer","--log",path,"--input",key,"--value",JSON.stringify(value)],ok);
      const events=()=>readFileSync(path,"utf8").trim().split("\n").slice(1).map(l=>JSON.parse(l) as {input:string;value:unknown;records?:{input:string;value:unknown}[]});
      const pendingKeys=(s:any):string[]=>s.pending.map((q:any)=>q.input);
      let state=await cli(["interview","start","--profile","full","--log",path]);
      assert.equal(state.question.input,"$person");
      assert.equal(state.question.prompt,"Who is this tax return for?");
      assert.deepEqual(state.question.choices.map((c:any)=>c.label),["Just me","Me and my husband or wife, together on one return"]);
      assert.deepEqual(state.recorded,[]);
      // Not a declared choice: refused, nothing written.
      await answer("$person",["taxpayer","second"],false);
      await answer("$person",["spouse"],false);
      assert.equal(events().length,0);
      // The couple: one answer records both roles and the joint status; neither is asked.
      state=await answer("$person",["taxpayer","spouse"]);
      assert.deepEqual(events().at(-1)!.records!.map(r=>[r.input,r.value]),[["person[taxpayer].role","taxpayer"],["person[spouse].role","spouse"],["f1040.status","mfj"]]);
      assert.deepEqual(state.recorded.map((r:any)=>[r.input,r.value,r.by]),[["f1040.status","mfj","$person"],["person[spouse].role","spouse","$person"],["person[taxpayer].role","taxpayer","$person"]]);
      assert.ok(state.recorded.every((r:any)=>typeof r.shown==="string"&&r.shown!==""));
      assert.ok(!pendingKeys(state).some(k=>k==="f1040.status"||k.endsWith(".role")),"after the couple's choice neither the status nor a role is pending");
      assert.equal(state.values["f1040.status"].value.value,"mfj");
      // Per-person questions say whose they are; a once-per-return question names the spouse.
      const perPerson=state.pending.filter((q:any)=>q.frame);
      assert.ok(perPerson.some((q:any)=>q.frame==="About you"&&q.input.includes("person[taxpayer]")&&q.prompt.startsWith("About you — ")));
      assert.ok(perPerson.some((q:any)=>q.frame==="About your spouse"&&q.input.includes("person[spouse]")&&q.prompt.startsWith("About your spouse — ")));
      assert.ok(state.pending.every((q:any)=>!q.prompt.includes("For this person (you, or your spouse on a joint return)")),"no stored per-person frame is shown");
      // A recorded answer is changed through the choice, not directly.
      const before=readFileSync(path,"utf8");
      for (const [key,value] of [["f1040.status","single"],["f1040.status",null],["person[spouse].role","taxpayer"],["person[taxpayer].role","taxpayer"]] as const) await answer(key,value,false);
      assert.equal(readFileSync(path,"utf8"),before,"a refused answer writes nothing");
      const spouseQuestion=perPerson.find((q:any)=>q.frame==="About your spouse"&&q.entry.startsWith("true or false")).input as string;
      state=await answer(spouseQuestion,true);
      assert.ok(!pendingKeys(state).includes(spouseQuestion));
      // Changing the choice: the recorded status is withdrawn and asked, the spouse's answers are inactive.
      state=await answer("$person",["taxpayer"]);
      assert.deepEqual(state.recorded.map((r:any)=>r.input),["person[taxpayer].role"]);
      assert.equal(state.question.input,"f1040.status");
      assert.equal(state.question.prompt,"Which of these fits you on December 31, 2025?");
      assert.deepEqual(state.question.withheld,["mfj"]);
      assert.match(state.question.entry,/^one of: "mfs" \(Married, and filing apart[^"]*\), "qss" \([^"]*\), "hoh" \([^"]*\), "single" \(None of these: I was not married \(single\)\); null asks for help$/);
      assert.ok(!(spouseQuestion in state.values)&&!pendingKeys(state).some(k=>k.includes("person[spouse]")));
      assert.ok(state.pending.every((q:any)=>q.frame===undefined&&!q.prompt.startsWith("About you")&&!q.prompt.includes("For this person (you")),"one person on the return: no per-person frame");
      // Married filing separately is refused at once, with what the filer can do.
      state=await answer("f1040.status","mfs");
      assert.equal(state.status,"refused");assert.equal(state.refusal.form,"Married filing separately");
      assert.match(state.refusalNote,/go back to “Who is this tax return for\?” and choose “Me and my husband or wife, together on one return”/);
      state=await answer("f1040.status","hoh");
      assert.equal(state.refusalNote,null);assert.equal(state.question.withheld,undefined);
      // Back to the couple: the joint status is recorded over the status answered alone, and the spouse's answer returns.
      state=await answer("$person",["spouse","taxpayer"]);
      assert.deepEqual(events().at(-1)!.value,["taxpayer","spouse"]);
      assert.equal(state.values["f1040.status"].value.value,"mfj");
      assert.ok(!pendingKeys(state).includes(spouseQuestion)&&pendingKeys(state).some(k=>k.includes("person[spouse]")),"the spouse's earlier answer is active again");
      // And alone again: the status answered alone before is not brought back; it is asked.
      state=await answer("$person",["taxpayer"]);
      assert.equal(state.question.input,"f1040.status");
      assert.equal(state.values["f1040.status"].value.kind,"unknown");
      // A help request on the first question withdraws what its answer recorded.
      state=await answer("$person",null);
      assert.deepEqual(state.recorded,[]);assert.equal(state.question.input,"$person");assert.equal(state.question.helpRequested,true);

      // Logs answered under the earlier questions (the roster, the status and each role as separate answers) give
      // the same values as today's one answer; a log that stopped before a role was answered asks the first question again.
      const write=(name:string,lines:object[])=>{const p=join(dir,name);writeFileSync(p,[{version:1,tax_year:YEAR,profile:"full"},...lines].map(l=>JSON.stringify(l)).join("\n")+"\n");return p;};
      const comparable=(s:any)=>JSON.stringify([s.status,s.refusal,s.values,s.reachableInputs,s.pending]);
      for (const [name,old,now] of [
        ["joint",[{input:"$person",value:["taxpayer","spouse"]},{input:"f1040.status",value:"mfj"},{input:"person[spouse].role",value:"spouse"},{input:"person[taxpayer].role",value:"taxpayer"}],["taxpayer","spouse"]],
        ["single",[{input:"$person",value:["taxpayer"]},{input:"f1040.status",value:"single"},{input:"person[taxpayer].role",value:"taxpayer"}],["taxpayer"]],
      ] as const) {
        const oldState=await cli(["interview","advance","--log",write(`old-${name}.jsonl`,[...old,{input:"scope.other_line16",value:false}])]);
        const newLog=join(dir,`new-${name}.jsonl`);
        await cli(["interview","start","--profile","full","--log",newLog]);
        await cli(["interview","answer","--log",newLog,"--input","$person","--value",JSON.stringify(now)]);
        if (name==="single") await cli(["interview","answer","--log",newLog,"--input","f1040.status","--value",'"single"']);
        const newState=await cli(["interview","answer","--log",newLog,"--input","scope.other_line16","--value","false"]);
        assert.equal(comparable(oldState),comparable(newState),`${name}: a log of the earlier questions gives today's state`);
        assert.deepEqual(oldState.recorded,[],"answers given directly are not recorded ones");
        // The earlier log stays correctable: its status was answered directly, and changing the first answer records anew.
        const oldPath=join(dir,`old-${name}.jsonl`);
        const corrected=await cli(["interview","answer","--log",oldPath,"--input","$person","--value",JSON.stringify(now)]);
        assert.equal(comparable(corrected),comparable(newState),`${name}: answering the first question again leaves the values`);
      }
      const partial=await cli(["interview","advance","--log",write("old-partial.jsonl",[{input:"$person",value:["taxpayer","spouse"]},{input:"f1040.status",value:"mfj"}])]);
      assert.ok(partial.reachableInputs.includes("person[spouse].role")&&partial.reachableInputs.includes("person[taxpayer].role"));
      assert.equal(partial.question.input,"$person","an unanswered role is asked through the first question, whose choice records it");
      assert.equal(partial.pending.filter((q:any)=>q.input==="$person").length,1);
      const healed=await cli(["interview","answer","--log",join(dir,"old-partial.jsonl"),"--input","$person","--value",'["taxpayer","spouse"]']);
      assert.ok(!healed.reachableInputs.some((k:string)=>k.endsWith(".role"))&&healed.question.input!=="$person");
    });
    await mapPool(groups,(g)=>g(),groups.length);
    console.log(`integration: ${checks} CLI invocations passed (interview, corrections, early refusals, invalid inputs, graph/type failures)`);
  } finally {rmSync(dir,{recursive:true,force:true});}
}
