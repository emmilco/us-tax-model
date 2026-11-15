# Restates New York fixture inputs for the lane-ny model (docs/provisional/lanes/ny.md, "Fixtures"). Expected values are
# never touched. Run from the worktree root on the files as committed at the lane's start (git show <base>:...).
import json, subprocess, sys
BASE = sys.argv[1]
def load(path): return json.loads(subprocess.check_output(["git","show","%s:%s"%(BASE,path)]))
changed = {}
EXTRA = sys.argv[2:]
for name in ["it201","classm","classm.deepseek","mutation"]:
    path="fixtures/ny/2025/%s.json"%name
    d=load(path)
    for cs in d["cases"]:
        i=cs["inputs"]; before=json.dumps(i, sort_keys=True); cid=cs["id"]
        # special_code is a derived line: its Yes becomes the one item not gated on another answer (abroad)
        if "ny_it201.ask.special_code" in i:
            v=i.pop("ny_it201.ask.special_code")
            if v is True: i["ny_it201.ask.abroad"]=True
            elif v is None: i["ny_it201.ask.abroad"]=None
            if name!="it201":
                # a case that states every answer (no defaults): the items not gated on another answer, stated No
                for k in ["ny_it201.ask.moved_in","ny_it201.ask.moved_out","ny_it201.ask.abroad","ny_it201.ask.installment"]: i.setdefault(k, False)
                if "sa.dependent" not in i: i["sa.dependent"]=False
        if name!="it201" and any(k.startswith("ny_it201.ask.") for k in i):
            # the federal answers the New York part now reads, stated as the case's facts (none of them)
            i.setdefault("f1040.tax_exempt_interest", 0)
            for k in ["ny_it201.ask.public_job","ny_it201.ask.bab"]: i.setdefault(k, False)
            if i.get("f1040.status")=="mfs": i.setdefault("ny_it201.ask.spouse_itemizes", False)
            for who in (i.get("$person") or ["taxpayer"]): i.setdefault("person[%s].x_edu_account"%who, False)
            if i.get("ny_it201.ask.owes_use_tax") is True and i.get("ny_it201.ask.use_tax_st141") is False: i.setdefault("ny_it201.ask.use_tax_exact", False)
            if i.get("ny_it201.ask.gov_pension") is False: i.setdefault("ny_it201.ask.gov_pension_other", False)
            i.setdefault("ny_it201.ask.apply_any", False)
            for k in EXTRA: i.setdefault(k, False)
        # line 75 is a derived line: a plain parent over the amount
        if "ny_it201.line75" in i:
            v=i.pop("ny_it201.line75")
            if v is None: i["ny_it201.ask.est_any"]=None
            elif v>0: i["ny_it201.ask.est_any"]=True; i["ny_it201.line75_amount"]=v
            elif name!="it201": i["ny_it201.ask.est_any"]=False
        # line 79: a plain parent over the amount
        if i.get("ny_it201.line79_amount") not in (None,0): i["ny_it201.ask.apply_any"]=True
        # tax-exempt interest is now read by the New York part (line 20's question); a case that withheld it had none
        if "f1040.tax_exempt_interest" in i and i["f1040.tax_exempt_interest"] is None: i["f1040.tax_exempt_interest"]=0
        # the facts a gated question now stands behind, where a case answered it Yes
        t=lambda k: i.get(k) is True
        if t("ny_it201.ask.special_accrual"): i["ny_it201.ask.moved_out"]=True
        if t("ny_it201.ask.414h"): i["ny_it201.ask.public_job"]=True
        if t("ny_it201.ask.529_nonqualified") or t("ny_it201.ask.529_owner"):
            i["person[taxpayer].x_edu_account"]=True; i["ny_it201.ask.ny_529"]=True
        if t("ny_it201.ask.out_of_state_bond_interest"): i["f1040.tax_exempt_interest"]=50000
        if t("ny_it201.ask.inflation_check"):
            i["$oi8z"]=["inflation_check"]; i["oi8z[inflation_check].kind"]="kickbacks"; i["oi8z[inflation_check].amount"]=27000
        if t("ny_it201.ask.itemize"):
            i["sa.personal_property_tax_any"]=True; i["sa.line5c"]=60000
        if t("ny_it201.ask.city_credits"):
            i["$sc@person[taxpayer]"]=["consulting"]
        if t("ny_it201.ask.college_tuition"): i["f8863.paid"]=True
        if t("ny_it201.ask.other_withholding"):
            i["$retirement@person[taxpayer]"]=["p"]; i["person[taxpayer].retirement[p].account"]="plan"
            i["person[taxpayer].retirement[p].box1"]=1200000; i["person[taxpayer].retirement[p].box5"]=120000
        if t("ny_it201.ask.real_property_credit"):
            # the credit needs federal AGI of $18,000 or less: one small W-2 in place of the two
            for k in [k for k in i if k.startswith("person[taxpayer].w2[")]: del i[k]
            i["$w2@person[taxpayer]"]=["emp_a"]
            for box,v in [("box1",1500000),("box2",0),("box3",1500000),("box4",93000),("box5",1500000),("box6",21750)]:
                i["person[taxpayer].w2[emp_a].%s"%box]=v
        if json.dumps(i, sort_keys=True)!=before: changed.setdefault(name,[]).append(cid)
    open(path,"w").write(json.dumps(d, indent=2, ensure_ascii=False)+"\n")
for k,v in changed.items(): print(k, len(v), v if len(v)<40 else v[:40])
