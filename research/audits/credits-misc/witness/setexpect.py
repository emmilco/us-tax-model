"""Replace one expected value inside one fixture case, as text: setexpect.py <file> <case id> <line id> <json value>

Only the value object of "<line id>": inside the case's "expect" block is rewritten; the rest of the file is untouched.
"""
import json
import re
import sys

path, case_id, line_id, value = sys.argv[1:5]
text = open(path).read()
start = text.index(f'"id": "{case_id}"')
m = re.compile(r'"id": "').search(text, start + 1)
end = m.start() if m else len(text)
exp = text.index('"expect": {', start)
assert exp < end
key = f'"{line_id}": {{'
k = text.index(key, exp)
assert k < end
i = k + len(key) - 1
depth = 0
for j in range(i, end):
    if text[j] == "{":
        depth += 1
    elif text[j] == "}":
        depth -= 1
        if depth == 0:
            break
indent = text[text.rindex("\n", 0, k) + 1:k]
body = json.dumps(json.loads(value), indent=2).replace("\n", "\n" + indent)
text = text[:k] + f'"{line_id}": ' + body + text[j + 1:]
json.loads(text)
open(path, "w").write(text)
