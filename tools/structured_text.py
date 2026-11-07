# SPDX-License-Identifier: Apache-2.0
"""Structured text in the review tools: the Markdown subset form text shown as a question or help may use
(engine/src/text.ts defines it and the build validates it).

Text with no line break is plain and every function here returns it unchanged, so a prompt built from plain
text is byte-identical to one built before structured text existed. Text with a line break is already its own
plain-text form (one-line paragraphs, headings ending in ":", "- " bullets, "  - " nested bullets); a prompt
that prints it after a prefix indents its continuation lines (indent_rest), names it by its first line where
one line is wanted (summary), or, where the text sits inside a line that goes on after it (a value, a type, a
"; "-joined list), puts it on one line with its item boundaries and nesting kept (inline).
"""
import re


def is_structured(text):
    return isinstance(text, str) and "\n" in text


def summary(text):
    """The first line: how a structured label is named (a helper reference, a log heading)."""
    return text.split("\n", 1)[0] if is_structured(text) else text


def indent_rest(text, pad):
    """The text with every continuation line prefixed by `pad`; blank lines stay empty."""
    if not is_structured(text):
        return text
    first, *rest = text.split("\n")
    return "\n".join([first] + [pad + l if l else "" for l in rest])


def inline(text):
    """The text on one line that keeps its structure: the question, then each further block after " — ";
    a list as "Heading: (1) item; (2) item [nested: sub; sub]", numbered per list. Plain text is returned
    unchanged."""
    if not is_structured(text):
        return text
    lines = [l for l in text.split("\n") if l]
    blocks, i = [], 0
    while i < len(lines):
        head = None
        if not lines[i].startswith("- ") and lines[i].endswith(":") and i + 1 < len(lines) and lines[i + 1].startswith("- "):
            head, i = lines[i], i + 1
        if lines[i].startswith("- "):
            items = []
            while i < len(lines) and lines[i].startswith(("- ", "  - ")):
                if lines[i].startswith("- "):
                    items.append([lines[i][2:], []])
                else:
                    items[-1][1].append(lines[i][4:])
                i += 1
            body = "; ".join(f"({n}) {t}" + (f" [nested: {'; '.join(sub)}]" if sub else "") for n, (t, sub) in enumerate(items, 1))
            blocks.append(f"{head} {body}" if head else body)
        else:
            blocks.append(lines[i])
            i += 1
    return " \u2014 ".join(blocks)


def continued(body, start):
    """The continuation of a rendered field (rendered/<year>/*.md) whose first line ends at `start` in `body`:
    the lines after it that are blank or indented by two spaces, up to the next unindented line, dedented, with
    trailing blank lines dropped. '' when the field is one line."""
    out = []
    for line in body[start:].split("\n")[1:]:
        if line and not line.startswith("  "):
            break
        out.append(line[2:])
    while out and not out[-1]:
        out.pop()
    return "\n" + "\n".join(out) if out else ""
