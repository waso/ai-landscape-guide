"""Parse the glossary Markdown files. Shared by build_index.py and check.py."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GLOSSARY_DIR = ROOT / "docs" / "glossary"
HEAD = re.compile(r"^### (?P<name>.+?)(?P<core> ★)? \{ #(?P<id>[a-z0-9-]+) \}\s*$")
AKA = re.compile(r"^\*Also known as:\* (?P<aka>.+)$")
WHY = re.compile(r"^\*\*Why it matters:\*\* (?P<why>.+)$")
ALIASES = re.compile(r"^<small>\*Index aliases:\* (?P<al>.+)</small>$")
SECTION_TITLE = re.compile(r"^# (?P<num>\d+)\. (?P<title>.+)$")

def parse_file(path):
    """Return (section_num, section_title, entries). Each entry is a dict."""
    text = path.read_text(encoding="utf-8").splitlines()
    num = title = None
    entries, cur = [], None
    for ln in text:
        m = SECTION_TITLE.match(ln)
        if m and num is None:
            num, title = int(m.group("num")), m.group("title"); continue
        m = HEAD.match(ln)
        if m:
            cur = dict(name=m.group("name").strip(), core=bool(m.group("core")), id=m.group("id"),
                       aka=[], why=None, aliases=[], definition=[], file=path.name, line=text.index(ln) + 1)
            entries.append(cur); continue
        if cur is None or not ln.strip():
            continue
        if ln.startswith("### ") or ln.startswith("## ") or ln.startswith("# "):
            cur = None; continue
        m = AKA.match(ln)
        if m:
            cur["aka"] = [a.strip() for a in re.split(r",\s*", m.group("aka")) if a.strip()]; continue
        m = WHY.match(ln)
        if m:
            cur["why"] = m.group("why").strip(); continue
        m = ALIASES.match(ln)
        if m:
            cur["aliases"] = [a.strip() for a in re.split(r",\s*", m.group("al")) if a.strip()]; continue
        cur["definition"].append(ln.strip())
    for e in entries:
        e["definition"] = " ".join(e["definition"])
    return num, title, entries

def load_all():
    sections = []
    for path in sorted(GLOSSARY_DIR.glob("*.md")):
        num, title, entries = parse_file(path)
        sections.append(dict(num=num, title=title, file=path.name, entries=entries))
    return sections
