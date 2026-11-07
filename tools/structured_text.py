# SPDX-License-Identifier: Apache-2.0
"""Structured text in the review tools: the Markdown subset form text shown as a question or help may use
(engine/src/text.ts defines it and the build validates it).

Text with no line break is plain and every function here returns it unchanged, so a prompt built from plain
text is byte-identical to one built before structured text existed. Text with a line break is already its own
plain-text form (one-line paragraphs, headings ending in ":", "- " bullets, "  - " nested bullets); a prompt
that prints it after a prefix indents its continuation lines (indent_rest), names it by its first line where
one line is wanted (summary), or puts it on one line where only one line fits (flat).
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


def flat(text):
    """The text on one line, each line break and the indentation around it one space."""
    return re.sub(r"\s*\n\s*", " ", text) if is_structured(text) else text


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
