"""Edit entries of interview/2025/questions.yaml in place, block by block, leaving every other entry's text untouched."""
import yaml, re, sys
PATH = 'interview/2025/questions.yaml'
BOILER = 'Married filing separately and unsupported items are refused with citations.'
class Bank:
    def __init__(self):
        t = open(PATH).read()
        i = t.index('\n  - input: ')
        self.head = t[:i+1]
        body = t[i+1:]
        parts = re.split(r'(?m)^(?=  - input: )', body)
        self.blocks = [p for p in parts if p]
        # the last block may carry trailing non-entry text
        self.ids = [yaml.safe_load(b)[0]['input'] if b.startswith('  - input: ') else None for b in self.blocks]
    def _dump(self, d):
        order = ['input', 'order', 'seq', 'help', 'prompt']
        e = {k: d[k] for k in order if k in d}
        e.update({k: v for k, v in d.items() if k not in e})
        s = yaml.safe_dump([e], sort_keys=False, width=118, allow_unicode=True, default_flow_style=False)
        return ''.join('  ' + ln + '\n' for ln in s.splitlines())
    def get(self, id):
        return yaml.safe_load(self.blocks[self.ids.index(id)])[0]
    def set(self, id, **kw):
        i = self.ids.index(id)
        d = yaml.safe_load(self.blocks[i])[0]
        for k, v in kw.items():
            if v is None: d.pop(k, None)
            else: d[k] = v
        if d.get('help') == BOILER: d.pop('help')
        self.blocks[i] = self._dump(d)
    def remove(self, id):
        i = self.ids.index(id); del self.blocks[i]; del self.ids[i]
    def add_after(self, after, id, **kw):
        assert id not in self.ids, id
        i = self.ids.index(after)
        d = {'input': id}; d.update({k: v for k, v in kw.items() if v is not None})
        self.blocks.insert(i+1, self._dump(d)); self.ids.insert(i+1, id)
    def save(self):
        open(PATH, 'w').write(self.head + ''.join(self.blocks))
