"""Regenerate docs/index-a-z.md and data/glossary.json from the glossary Markdown files."""
import json, re, unicodedata
from pathlib import Path
from glossary_lib import ROOT, load_all

def key(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", s)

sections = load_all()
rows, seen = [], set()
def add(name, see, sec, entry):
    k = key(name)
    if not k or k in seen:
        return
    seen.add(k); rows.append((name, see, sec, entry))
for sec in sections:
    for e in sec["entries"]:
        add(e["name"], None, sec, e)
for sec in sections:
    for e in sec["entries"]:
        for a in e["aka"] + e["aliases"]:
            if a.lower() != e["name"].lower():
                add(a, e["name"], sec, e)
rows.sort(key=lambda r: key(r[0]))

out = ["# A–Z index", "",
       f"{len(rows)} entries. The number in brackets is the glossary section. “→” means “explained under”. Everything here is also reachable through the search box.", ""]
letter = None
for name, see, sec, e in rows:
    first = key(name)[0]
    first = first.upper() if first.isalpha() else "0–9"
    if first != letter:
        letter = first
        out += ["", f"## {letter}", ""]
    link = f"glossary/{sec['file']}#{e['id']}"
    if see:
        out.append(f"- {name} → [{see}]({link}) [{sec['num']}]")
    else:
        out.append(f"- [{name}]({link}) [{sec['num']}]")
(ROOT / "docs" / "index-a-z.md").write_text("\n".join(out) + "\n", encoding="utf-8")

data = [dict(section=sec["num"], section_title=sec["title"], id=e["id"], term=e["name"], core=e["core"],
             also_known_as=e["aka"], definition=e["definition"], why_it_matters=e["why"], aliases=e["aliases"],
             url=f"glossary/{sec['file']}#{e['id']}") for sec in sections for e in sec["entries"]]
(ROOT / "data").mkdir(exist_ok=True)
(ROOT / "data" / "glossary.json").write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"index: {len(rows)} entries, {len(data)} terms, {len(sections)} sections")
