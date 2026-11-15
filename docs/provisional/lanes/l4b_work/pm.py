"""Text edits of a form file's lines, block by block (a block is one `- id:` line entry); other blocks are untouched."""
import re
class Form:
    def __init__(self, path):
        self.path=path; t=open(path).read()
        parts=re.split(r'(?m)^(?=    - id: )', t)
        self.head, self.blocks = parts[0], parts[1:]
        # the last block may run into the form's trailing keys (collection:, note:)
        m=re.search(r'(?m)^  [a-z#]', self.blocks[-1]) if self.blocks else None
        self.tail=''
        if m: self.tail=self.blocks[-1][m.start():]; self.blocks[-1]=self.blocks[-1][:m.start()]
        self.ids=[re.match(r'    - id: (\S+)', b).group(1) for b in self.blocks]
    def blk(self,i): return self.blocks[self.ids.index(i)]
    def field(self,i,name):
        m=re.search(r'(?ms)^      %s:.*?(?=^      [a-z_]+:|\Z)'%name, self.blk(i)); return m.group(0) if m else ''
    def cite(self,i): return self.field(i,'cite')
    def set_field(self,i,name,text):
        k=self.ids.index(i); b=self.blocks[k]
        m=re.search(r'(?ms)^      %s:.*?(?=^      [a-z_]+:|\Z)'%name, b)
        self.blocks[k]=b[:m.start()]+text+b[m.end():]
    def insert_field_after(self,i,after,text):
        k=self.ids.index(i); b=self.blocks[k]
        m=re.search(r'(?ms)^      %s:.*?(?=^      [a-z_]+:|\Z)'%after, b)
        self.blocks[k]=b[:m.end()]+text+b[m.end():]
    def replace_in(self,i,a,b_,n=1):
        k=self.ids.index(i); assert self.blocks[k].count(a)==n,(i,a,self.blocks[k].count(a)); self.blocks[k]=self.blocks[k].replace(a,b_)
    def add_after(self,after,text):
        k=self.ids.index(after)
        new=[x for x in re.split(r'(?m)^(?=    - id: )', text) if x]
        nid=[re.match(r'    - id: (\S+)', x).group(1) for x in new]
        for i in nid: assert i not in self.ids, i
        self.blocks[k+1:k+1]=new; self.ids[k+1:k+1]=nid
    def save(self): open(self.path,'w').write(self.head+''.join(self.blocks)+self.tail)
def gate(newid, gate_id, cond, label, cite, zero='person.no', typ='Bool', printed='(gate)'):
    return f"""    - id: {gate_id}
      printed: {printed}
      type: {typ}
      label: {label}
      expr:
        op: choose
        alternatives:
        - guard:
            op: test
            eq:
            - {cond}
            - const: true
          then: {newid}
        - guard:
            op: test
            eq:
            - {cond}
            - const: false
          then: {zero}
{cite}"""
def inp(newid, question, cite, gated_by=None, typ='Bool', label=None, printed='(helper)'):
    g=f"      gated_by: {gated_by}\n" if gated_by else ''
    q=question if '\n' not in question else None
    return f"""    - id: {newid}
      printed: {printed}
      type: {typ}
{g}      label: {yq(label or question)}
      expr:
        op: input
        source: {yq(question)}
{cite}"""
def yq(s):
    import json
    return json.dumps(s, ensure_ascii=False)
