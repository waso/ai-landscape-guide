"""Validate the glossary: every entry has an id, a definition and a Why-it-matters line; ids and names are unique."""
import re, sys
from glossary_lib import ROOT, GLOSSARY_DIR, load_all, HEAD

errors = []
sections = load_all()
ids, names = {}, {}
for sec in sections:
    if sec["num"] is None:
        errors.append(f"{sec['file']}: missing '# N. Title' heading")
    if not sec["entries"]:
        errors.append(f"{sec['file']}: no entries found")
    for e in sec["entries"]:
        where = f"{e['file']}:{e['line']} ({e['name']})"
        if e["id"] in ids:
            errors.append(f"{where}: duplicate id #{e['id']} (also in {ids[e['id']]})")
        ids[e["id"]] = where
        if e["name"].lower() in names:
            errors.append(f"{where}: duplicate term name (also in {names[e['name'].lower()]})")
        names[e["name"].lower()] = where
        if not e["definition"]:
            errors.append(f"{where}: missing definition paragraph")
        if not e["why"]:
            errors.append(f"{where}: missing '**Why it matters:**' line")
        elif len(e["why"]) > 400:
            errors.append(f"{where}: 'Why it matters' is over 400 characters; keep it to one sentence")
        if len(e["definition"]) > 900:
            errors.append(f"{where}: definition is over 900 characters; consider splitting the entry")
# headings that look like entries but do not match the format
for path in sorted(GLOSSARY_DIR.glob("*.md")):
    for i, ln in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if ln.startswith("### ") and not HEAD.match(ln):
            errors.append(f"{path.name}:{i}: entry heading does not match ### Term <a id='id'></a>: {ln}")
core = [e for sec in sections for e in sec["entries"] if e["core"]]
if not 20 <= len(core) <= 40:
    errors.append(f"{len(core)} terms are marked ★; keep the 'learn these first' list between 20 and 40")
if errors:
    print("\n".join(errors)); print(f"\n{len(errors)} problem(s)"); sys.exit(1)
print(f"OK: {sum(len(s['entries']) for s in sections)} entries in {len(sections)} sections, {len(core)} core terms")
