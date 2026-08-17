#!/usr/bin/env python3
"""mine.py - deterministic miner for an ICM workspace.

Mimir never counts. This script computes every number a finding is allowed to
cite, and writes it to evidence.json. The model interprets; the arithmetic
cannot drift, because it was never the model's.

Runs offline, Python 3 stdlib only, reads nothing outside the target folder.

Usage:
  python mine.py <workspace-path> [-o evidence.json]   mine a workspace
  python mine.py --selftest                            build known-broken trees
                                                       and prove the fingerprints fire

What it computes, and which cause family each field feeds
(see reference/cause-taxonomy.md):

  routingPayload  -> 1  payload in the catalog
  entry.twins     -> 2  twin entry files that drift
  graph.orphans   -> 3  unrouted work / 13 ghost wiring
  stages[].contractSections -> 4  no contract at the control point
  declaredInputs[].exists   -> 5  contract without exact paths / 12 broken handoff
  declaredInputs[].scope    -> 6  no section routing
  loadEstimate.band         -> 7  token blowout
  layers.L4 / outputFolder  -> 8  factory and product collapse
  declaredInputs from output-> 9  outputs used as templates
  placeholders              -> 10 placeholders never resolved
  duplication               -> 11 no canonical source
  graph.dangling            -> 12 broken handoff / 13 ghost wiring
  graph.backReferences      -> 14 back-references
  schemaDrift / naming      -> 15 schema and tree drift
  index                     -> 16 hand-edited generated index
  gates                     -> 17 no human gate
  outputFolder.onlyGitkeep  -> 18 over-structure
  form.guess                -> 19 under-structure

Fields marked in "heuristics" below are judgement calls made by regex, not
measurements. Cite the counts under them, not the verdict.
"""

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile

VERSION = "mine.py 1.1"

SKIP_DIRS = {
    ".git", ".hg", ".svn", "node_modules", "__pycache__", ".venv", "venv",
    ".mypy_cache", ".pytest_cache", "dist", "build", ".idea", ".vscode",
}
MAX_READ_BYTES = 2 * 1024 * 1024
TEXT_EXT = {".md", ".markdown", ".txt", ".json", ".yml", ".yaml"}

ENTRY_NAMES = {"claude.md", "agents.md", "routing.md"}
CONTEXT_NAME = "context.md"

REFERENCE_DIRS = {
    "reference", "references", "_shared", "shared", "_system", "system",
    "skills", "design-system", "brand-vault", "_meta", "_config", "_core",
    "assets", "docs",
}
OUTPUT_DIRS = {"output", "outputs", "_output"}
TEMPLATE_DIRS = {"_templates", "templates"}
META_DIRS = {"_archive", "archive", "_index", "eval", "tests", "checks", "receipts"}

STAGE_RE = re.compile(r"^(\d{2,3})[-_](.+)$")

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
MD_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s#]+)[^)]*\)")
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)")
BARE_PATH_RE = re.compile(
    r"(?<![\w`(\[])((?:\.{1,2}/|/)?(?:[\w.\-]+/)+[\w.\-]+\.(?:md|markdown|json|ya?ml|txt|py|mjs|js))"
)
PLACEHOLDER_RE = re.compile(r"\{\{[#/?]?([A-Za-z0-9_]+)\}\}")

CONTENT_HEADING_WORDS = {
    "voice", "rules", "examples", "example", "definitions", "definition",
    "guidelines", "guideline", "principles", "tone", "style", "brand",
    "glossary", "background", "philosophy", "standards", "checklist",
    "conventions", "instructions", "prompt", "template", "schema",
}
SECTION_WORDS_INPUT = ("input",)
SECTION_WORDS_PROCESS = ("process", "steps", "procedure", "workflow", "method")
SECTION_WORDS_OUTPUT = ("output", "deliverable", "artifact", "artefact")
SECTION_WORDS_HUMAN = ("human check", "human gate", "checkpoint", "human review",
                       "human", "gate")

STYLE_WORDS = ("style", "tone", "voice", "format", "example", "pattern",
               "shape", "template", "structure", "as a model", "like the")

BAND_LOW = 2000
BAND_HIGH = 8000

DUP_WINDOW = 4          # consecutive meaningful lines forming a shingle
DUP_MIN_CHARS = 120     # a shingle shorter than this is not interesting


# ----------------------------------------------------------------- utilities

def est_tokens(text):
    """Characters over four. Good enough to tell 2k from 30k, useless at band
    edges. reference/evidence-grades.md says so out loud."""
    return len(text) // 4


def norm_line(line):
    return re.sub(r"\s+", " ", line).strip().lower()


def rel(path, root):
    return os.path.relpath(path, root).replace(os.sep, "/")


def read_text(path):
    try:
        if os.path.getsize(path) > MAX_READ_BYTES:
            return None
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            return fh.read()
    except (OSError, ValueError):
        return None


def split_sections(text):
    """Return [(heading_text, level, [body lines])] for a markdown document."""
    out = []
    current = ("", 0, [])
    for line in text.splitlines():
        m = HEADING_RE.match(line)
        if m:
            out.append(current)
            current = (m.group(2).strip(), len(m.group(1)), [])
        else:
            current[2].append(line)
    out.append(current)
    return [s for s in out if s[0] or s[2]]


def find_section(sections, words):
    """First section whose heading contains any of the given words."""
    for head, level, body in sections:
        low = head.lower()
        for w in words:
            if w in low:
                return (head, level, body)
    return None


# ------------------------------------------------------------- walking files

def read_ignore(root):
    """A workspace may carry a .mimirignore: one path prefix per line, relative
    to the workspace root, blank lines and # comments skipped.

    This exists because a workspace can contain other workspaces - test
    fixtures, worked examples, a folder someone is diagnosing. Walking into
    them silently merges two trees into one set of numbers, which is how a
    miner produces a confident wrong measurement.
    """
    path = os.path.join(root, ".mimirignore")
    prefixes = []
    if os.path.isfile(path):
        try:
            with open(path, "r", encoding="utf-8") as fh:
                for line in fh:
                    line = line.split("#")[0].strip().strip("/")
                    if line:
                        prefixes.append(line.replace(os.sep, "/"))
        except OSError:
            pass
    return prefixes


def ignored(relpath, prefixes):
    for p in prefixes:
        if relpath == p or relpath.startswith(p + "/"):
            return True
    return False


def walk(root, ignore_prefixes=()):
    """Returns (files, folders, ignored_files).

    Ignored files are still listed, by path only. They are excluded from every
    structural measurement - that is what the ignore file is for - but a reader
    of the evidence still needs to know they exist. A reviewer pointing at a
    real file in an ignored subtree is not citing a file that is not there, and
    a checker that cannot tell those apart rejects correct work.
    """
    files = []
    folders = []
    ignored_files = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        keep = []
        for d in dirnames:
            full = os.path.join(dirpath, d)
            if ignored(rel(full, root), ignore_prefixes):
                for sub, _sd, sfn in os.walk(full):
                    for f in sorted(sfn):
                        ignored_files.append(rel(os.path.join(sub, f), root))
            else:
                keep.append(d)
        dirnames[:] = keep
        for d in dirnames:
            folders.append(os.path.join(dirpath, d))
        for fn in sorted(filenames):
            full = os.path.join(dirpath, fn)
            if ignored(rel(full, root), ignore_prefixes):
                ignored_files.append(rel(full, root))
                continue
            files.append(full)
    return files, folders, sorted(set(ignored_files))


def classify_layer(relpath, name):
    """Which of the five ICM layers this file sits in.

    L0 entry, L1 root routing, L2 folder contract, L3 factory reference,
    L4 per-run product, plus template / meta / unclassified.
    """
    parts = relpath.split("/")
    low = name.lower()
    depth = len(parts) - 1
    dirs = [p.lower() for p in parts[:-1]]

    if any(d in TEMPLATE_DIRS for d in dirs):
        return "template"
    if any(d in OUTPUT_DIRS for d in dirs):
        return "L4"
    if low in ENTRY_NAMES and depth == 0:
        return "L0"
    if low == CONTEXT_NAME and depth == 0:
        return "L1"
    if low == CONTEXT_NAME:
        return "L2"
    if low in ENTRY_NAMES:
        return "L2"
    if low in ("rules.md", "identity.md", "intake.md", "skill.md") and depth == 0:
        return "L2"
    if any(d in META_DIRS for d in dirs):
        return "meta"
    if any(d in REFERENCE_DIRS for d in dirs):
        return "L3"
    if low in ("readme.md", "license", "license.txt", "license.md"):
        return "meta"
    if depth == 0 and low.endswith(".md"):
        return "L3"
    return "unclassified"


def prose_profile(text):
    """Count headings, and lines that are neither heading, list, table, code,
    blockquote nor blank. A routing file should be mostly not-prose."""
    headings = 0
    prose = 0
    in_code = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if in_code or not stripped:
            continue
        if HEADING_RE.match(line):
            headings += 1
            continue
        if stripped.startswith(("-", "*", "+", ">", "|")) or re.match(r"^\d+[.)]\s", stripped):
            continue
        prose += 1
    return headings, prose


# ------------------------------------------------------------- the link graph

def extract_links(text):
    """Every path this file points at: markdown links, wikilinks, bare paths."""
    found = []
    in_code = False
    for i, line in enumerate(text.splitlines(), start=1):
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        for m in MD_LINK_RE.finditer(line):
            found.append((m.group(1), i))
        for m in WIKILINK_RE.finditer(line):
            found.append((m.group(1).strip(), i))
        # Inline code is where ICM contracts actually keep their paths
        # (_core/CONVENTIONS.md Pattern 1), so backticked spans are the
        # primary carrier, not noise. Fenced blocks are already skipped above.
        rest = line
        for m in re.finditer(r"`([^`]+)`", line):
            span = m.group(1).strip()
            # A backticked span with whitespace in it is a command, not a path:
            # ICM naming forbids spaces in file and folder names. Without this,
            # `python checks/mine.py <workspace>` is mined as a broken link.
            if re.search(r"\s", span):
                rest = rest.replace(m.group(0), " ")
                continue
            if BARE_PATH_RE.search(span) or span.endswith((".md", ".markdown")):
                found.append((span, i))
            rest = rest.replace(m.group(0), " ")
        for m in BARE_PATH_RE.finditer(rest):
            found.append((m.group(1), i))
    seen = set()
    out = []
    for target, line in found:
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        key = (target, line)
        if key in seen:
            continue
        seen.add(key)
        out.append((target, line))
    return out


def resolve(target, from_relpath, all_relpaths, root):
    """Resolve a link target to a workspace-relative path, or None."""
    target = target.split("#")[0].strip()
    if not target:
        return None
    base = os.path.dirname(from_relpath)
    candidates = []
    if target.startswith("/"):
        candidates.append(target.lstrip("/"))
    else:
        candidates.append(os.path.normpath(os.path.join(base, target)))
        candidates.append(os.path.normpath(target))
    for cand in candidates:
        cand = cand.replace(os.sep, "/")
        if cand in all_relpaths:
            return cand
        if cand + ".md" in all_relpaths:
            return cand + ".md"
        # a directory target resolves to its contract or entry file
        for extra in ("/CONTEXT.md", "/CLAUDE.md", "/README.md"):
            if cand + extra in all_relpaths:
                return cand + extra
        # A target inside an ignored subtree still exists. Not measuring a
        # folder is not the same as the folder being absent, and reporting it
        # as a broken link would be an artifact of the ignore file.
        if os.path.exists(os.path.join(root, cand.replace("/", os.sep))):
            return cand
    return None


# --------------------------------------------------------- contract parsing

def parse_declared(body_lines):
    """Pull declared paths out of an Inputs or Outputs section.

    Handles both canon shapes: the markdown table of _core/CONVENTIONS.md
    Pattern 1, and the bullet list of icm-architect references/core.md.
    Returns [{raw, path, scope, note}].
    """
    entries = []
    for line in body_lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("```"):
            continue
        cells = None
        if stripped.startswith("|"):
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if not cells or set("".join(cells)) <= set("-: "):
                continue
            if all(c.lower() in ("source", "file", "file/location", "location",
                                 "section/scope", "section to load", "scope",
                                 "why", "artifact", "format", "skill")
                   for c in cells if c):
                continue
        elif stripped.startswith(("-", "*", "+")):
            cells = [stripped.lstrip("-*+ ").strip()]
        else:
            continue

        joined = " | ".join(cells)
        paths = []
        for cell in cells:
            for m in re.finditer(r"`([^`]+)`", cell):
                paths.append(m.group(1).strip())
            if not paths:
                for m in BARE_PATH_RE.finditer(cell):
                    paths.append(m.group(1).strip())
        scope = ""
        for cell in cells:
            low = cell.lower()
            if "full file" in low:
                scope = "Full file"
                break
            if '"' in cell and "through" in low or "section" in low:
                scope = cell
                break
        if len(cells) >= 3 and not scope:
            scope = cells[2]
        entries.append({
            "raw": joined,
            "path": paths[0] if paths else None,
            "scope": scope or None,
            "note": joined,
        })
    return entries


def contract_sections(text):
    sections = split_sections(text)
    return {
        "inputs": find_section(sections, SECTION_WORDS_INPUT) is not None,
        "process": find_section(sections, SECTION_WORDS_PROCESS) is not None,
        "outputs": find_section(sections, SECTION_WORDS_OUTPUT) is not None,
        "humanCheck": find_section(sections, SECTION_WORDS_HUMAN) is not None,
    }, sections


# --------------------------------------------------------------- duplication

def duplication_clusters(file_texts):
    """Shingled hashes of DUP_WINDOW consecutive meaningful lines.
    A hash appearing in two or more non-template files is a candidate
    canonical-source violation (family 11)."""
    buckets = {}
    for path, text in file_texts.items():
        lines = [norm_line(l) for l in text.splitlines()]
        lines = [l for l in lines if len(l) > 20 and not l.startswith("|--")]
        for i in range(len(lines) - DUP_WINDOW + 1):
            window = lines[i:i + DUP_WINDOW]
            blob = "\n".join(window)
            if len(blob) < DUP_MIN_CHARS:
                continue
            h = hashlib.sha1(blob.encode("utf-8")).hexdigest()[:12]
            buckets.setdefault(h, {"files": set(), "sample": window[0], "lines": DUP_WINDOW})
            buckets[h]["files"].add(path)
    out = []
    for h, data in sorted(buckets.items()):
        if len(data["files"]) >= 2:
            out.append({
                "hash": h,
                "lines": data["lines"],
                "files": sorted(data["files"]),
                "sample": data["sample"][:120],
            })
    # collapse overlapping clusters over the same file pair
    collapsed = {}
    for entry in out:
        key = tuple(entry["files"])
        if key not in collapsed:
            collapsed[key] = entry
            collapsed[key]["blocks"] = 1
        else:
            collapsed[key]["blocks"] += 1
    return sorted(collapsed.values(), key=lambda e: -e["blocks"])


# --------------------------------------------------------------- the miner

def mine(root):
    root = os.path.abspath(root)
    if not os.path.isdir(root):
        raise SystemExit("not a folder: %s" % root)

    ignore_prefixes = read_ignore(root)
    files, folders, ignored_files = walk(root, ignore_prefixes)
    all_rel = set(rel(f, root) for f in files)
    folder_rel = set(rel(d, root) for d in folders)

    file_records = []
    texts = {}
    total_bytes = 0

    for full in files:
        rp = rel(full, root)
        name = os.path.basename(full)
        ext = os.path.splitext(name)[1].lower()
        try:
            size = os.path.getsize(full)
            mtime = int(os.path.getmtime(full))
        except OSError:
            size, mtime = 0, 0
        total_bytes += size
        layer = classify_layer(rp, name)
        record = {
            "path": rp, "layer": layer, "bytes": size, "mtime": mtime,
            "lines": 0, "estTokens": 0, "headings": 0, "proseLines": 0, "links": 0,
        }
        if ext in TEXT_EXT:
            text = read_text(full)
            if text is not None:
                texts[rp] = text
                record["lines"] = len(text.splitlines())
                record["estTokens"] = est_tokens(text)
                if ext in (".md", ".markdown"):
                    h, p = prose_profile(text)
                    record["headings"] = h
                    record["proseLines"] = p
        file_records.append(record)

    by_path = {r["path"]: r for r in file_records}
    md_paths = [r["path"] for r in file_records
                if r["path"].lower().endswith((".md", ".markdown"))]

    # ---- link graph
    edges = []
    dangling = []
    for rp, text in texts.items():
        if not rp.lower().endswith((".md", ".markdown")):
            continue
        links = extract_links(text)
        by_path[rp]["links"] = len(links)
        for target, line in links:
            resolved = resolve(target, rp, all_rel, root)
            if resolved:
                if resolved != rp:
                    edges.append({"from": rp, "to": resolved})
            else:
                base = os.path.dirname(rp)
                cand = os.path.normpath(os.path.join(base, target.split("#")[0]))
                cand = cand.replace(os.sep, "/")
                if cand in folder_rel:
                    continue
                # Carry the source line. The miner cannot tell a citation of
                # another repository from a broken internal link, so it hands
                # the reader the sentence and lets them see which it is.
                source_lines = text.splitlines()
                context = (source_lines[line - 1].strip()[:160]
                           if 0 < line <= len(source_lines) else "")
                dangling.append({"from": rp, "target": target, "line": line,
                                 "context": context})

    pointed_at = set(e["to"] for e in edges)
    # L4 is excluded: a run artifact that nothing points at is the normal state
    # of a product folder, not ghost wiring. The family 9 signal for an output
    # being *used* as reference is declaredInputs[].fromOutput, not this list.
    orphans = sorted(p for p in md_paths
                     if p not in pointed_at
                     and by_path[p]["layer"] not in ("L0", "L1", "L4",
                                                     "meta", "template")
                     and os.path.basename(p).lower() != "readme.md")

    pairs = set((e["from"], e["to"]) for e in edges)
    back_refs = []
    for a, b in sorted(pairs):
        if (b, a) in pairs:
            if not any(x["a"] == b and x["b"] == a for x in back_refs):
                back_refs.append({"a": a, "b": b})

    # Pattern 3 is about folders pointing back at folders, not about two files
    # in the same layer naming each other. Both are reported; the taxonomy
    # convicts on the folder level and treats the file level as information.
    folder_pairs = set()
    for e in edges:
        fa, fb = os.path.dirname(e["from"]) or ".", os.path.dirname(e["to"]) or "."
        if fa != fb:
            folder_pairs.add((fa, fb))
    back_refs_folder = []
    for a, b in sorted(folder_pairs):
        if (b, a) in folder_pairs:
            if not any(x["a"] == b and x["b"] == a for x in back_refs_folder):
                back_refs_folder.append({"a": a, "b": b})

    # ---- entry files
    entry_files = sorted(p for p in all_rel
                         if "/" not in p and os.path.basename(p).lower() in ENTRY_NAMES)
    entry_lines = sum(by_path[p]["lines"] for p in entry_files if p in by_path)
    entry_tokens = sum(by_path[p]["estTokens"] for p in entry_files if p in by_path)
    twins_identical = None
    if len(entry_files) > 1:
        blobs = set()
        for p in entry_files:
            blobs.add(hashlib.sha1(texts.get(p, "").encode("utf-8")).hexdigest())
        twins_identical = len(blobs) == 1

    # ---- stages
    stages = []
    contracts_total = 0
    contracts_with_gate = 0
    stage_dirs = []
    for d in sorted(folder_rel):
        base = os.path.basename(d)
        m = STAGE_RE.match(base)
        contract = None
        for cand in (d + "/CONTEXT.md", d + "/context.md"):
            if cand in all_rel:
                contract = cand
                break
        if m or contract:
            stage_dirs.append((d, m, contract))

    for d, m, contract in stage_dirs:
        sections_present = {"inputs": False, "process": False,
                            "outputs": False, "humanCheck": False}
        declared_in, declared_out = [], []
        contract_tokens = 0
        if contract and contract in texts:
            contracts_total += 1
            sections_present, sections = contract_sections(texts[contract])
            if sections_present["humanCheck"]:
                contracts_with_gate += 1
            contract_tokens = by_path[contract]["estTokens"]
            sec_in = find_section(sections, SECTION_WORDS_INPUT)
            sec_out = find_section(sections, SECTION_WORDS_OUTPUT)
            if sec_in:
                declared_in = parse_declared(sec_in[2])
            if sec_out:
                declared_out = parse_declared(sec_out[2])

        def annotate(entries, from_path):
            for e in entries:
                if not e["path"]:
                    # No path in this row at all. That is family 5 - a contract
                    # that names things instead of locations.
                    e["exists"] = False
                    e["resolved"] = None
                    e["reason"] = "no path in this row"
                    e["fromOutput"] = False
                    e["styleReference"] = False
                    e["targetLines"] = None
                    e["targetTokens"] = None
                    continue
                resolved = resolve(e["path"], from_path or (d + "/CONTEXT.md"),
                                   all_rel, root)
                e["resolved"] = resolved
                e["exists"] = resolved is not None
                target_path = (resolved or e["path"]).replace(os.sep, "/")
                e["fromOutput"] = ("/output/" in target_path
                                   or target_path.startswith("output/"))
                low = (e["note"] or "").lower()
                e["styleReference"] = any(w in low for w in STYLE_WORDS)
                if resolved and resolved in by_path:
                    e["targetLines"] = by_path[resolved]["lines"]
                    e["targetTokens"] = by_path[resolved]["estTokens"]
                else:
                    e["targetLines"] = None
                    e["targetTokens"] = None
            return entries

        declared_in = annotate(declared_in, contract)
        declared_out = annotate(declared_out, contract)

        out_dir = None
        for cand in sorted(folder_rel):
            if cand.startswith(d + "/") and os.path.basename(cand).lower() in OUTPUT_DIRS:
                out_dir = cand
                break
        out_info = None
        if out_dir:
            contents = [p for p in all_rel if p.startswith(out_dir + "/")]
            real = [p for p in contents if os.path.basename(p) != ".gitkeep"]
            out_info = {
                "path": out_dir,
                "fileCount": len(real),
                "onlyGitkeep": len(contents) > 0 and len(real) == 0,
                "empty": len(contents) == 0,
            }

        inputs_tokens = sum(e["targetTokens"] or 0 for e in declared_in)
        total_load = entry_tokens + contract_tokens + inputs_tokens
        band = "in"
        if total_load < BAND_LOW:
            band = "under"
        elif total_load > BAND_HIGH:
            band = "over"

        stages.append({
            "folder": d,
            "index": m.group(1) if m else None,
            "name": m.group(2) if m else os.path.basename(d),
            "contract": contract,
            "contractSections": sections_present,
            "declaredInputs": declared_in,
            "declaredOutputs": declared_out,
            "outputFolder": out_info,
            "loadEstimate": {
                "entry": entry_tokens, "contract": contract_tokens,
                "inputs": inputs_tokens, "total": total_load, "band": band,
            },
        })

    # ---- declared outputs across the whole workspace, for handoff checking
    produced = set()
    for st in stages:
        for e in st["declaredOutputs"]:
            if e["resolved"]:
                produced.add(e["resolved"])
            elif e["path"]:
                produced.add(e["path"])

    for st in stages:
        for e in st["declaredInputs"]:
            target = (e["resolved"] or e["path"] or "")
            # Only meaningful for a path under an output folder. A workspace
            # input that no stage produces is normal, not a broken handoff.
            if not target or not e.get("fromOutput"):
                e["producedBySomeStage"] = None
            else:
                e["producedBySomeStage"] = (
                    target in produced or any(target.endswith(p) for p in produced))

    # A declared output that does not exist yet is an un-run stage, not a
    # dangling reference. outputFolder.fileCount already carries that fact.
    declared_out_pairs = set()
    for st in stages:
        if st["contract"]:
            for e in st["declaredOutputs"]:
                if e.get("path"):
                    declared_out_pairs.add((st["contract"], e["path"]))
    not_yet_produced = [d for d in dangling
                        if (d["from"], d["target"]) in declared_out_pairs]
    dangling = [d for d in dangling
                if (d["from"], d["target"]) not in declared_out_pairs]

    # ---- separate a broken internal link from a citation of another repo
    #
    # Without this the two are indistinguishable and graph.dangling is unusable:
    # a folder that cites the ICM canon reports dozens of "broken links" and a
    # real break is buried among them. Families 12 and 13 read kind == "broken";
    # nothing should ever be convicted on the raw count.
    contract_link_pairs = set()
    for st in stages:
        if st["contract"]:
            for e in st["declaredInputs"]:
                if e.get("path"):
                    contract_link_pairs.add((st["contract"], e["path"]))
    tree_roots = {p.split("/")[0] for p in all_rel}
    tree_roots |= {d.split("/")[0] for d in folder_rel}
    for d in dangling:
        target = d["target"].split("#")[0].strip()
        if (d["from"], d["target"]) in contract_link_pairs:
            # a contract declares it as an input and it is not there
            d["kind"] = "broken"
            d["why"] = "declared as a contract input"
        elif target.startswith(("./", "../")):
            # written relative to this tree, so it means this tree
            d["kind"] = "broken"
            d["why"] = "relative path into this tree"
        elif target.split("/")[0] in tree_roots:
            # its first segment exists here, so it is aiming at this tree
            d["kind"] = "broken"
            d["why"] = "first segment exists in this tree"
        else:
            d["kind"] = "external"
            d["why"] = "first segment names nothing in this tree"
    broken_links = [d for d in dangling if d["kind"] == "broken"]
    external_refs = [d for d in dangling if d["kind"] == "external"]

    # ---- placeholders
    ph_total, ph_outside, ph_sample = 0, 0, []
    for rp, text in texts.items():
        is_template = (by_path[rp]["layer"] == "template"
                       or "questionnaire" in rp.lower()
                       or "placeholder-syntax" in rp.lower())
        for i, line in enumerate(text.splitlines(), start=1):
            for m in PLACEHOLDER_RE.finditer(line):
                ph_total += 1
                if not is_template:
                    ph_outside += 1
                    if len(ph_sample) < 25:
                        ph_sample.append({"path": rp, "token": m.group(0), "line": i})

    # ---- routing payload heuristic
    # Scoped to files whose job is *routing*: the entry file and CONTEXT.md.
    # A specialist folder's rules.md or identity.md is also L2, and it is
    # supposed to carry the method - measuring it against a routing guardrail
    # produces a confident wrong finding about the most important file present.
    routing_payload = []
    for rp, text in texts.items():
        layer = by_path[rp]["layer"]
        name = os.path.basename(rp).lower()
        is_routing_file = name in ENTRY_NAMES or name == CONTEXT_NAME
        if layer not in ("L0", "L1", "L2") or not is_routing_file:
            continue
        lines = by_path[rp]["lines"]
        limit = 60 if layer == "L0" else 80
        headings = [h for h, lvl, body in split_sections(text) if h]
        content_headings = [h for h in headings
                            if any(w in h.lower() for w in CONTENT_HEADING_WORDS)]
        prose = by_path[rp]["proseLines"]
        ratio = round(prose / lines, 3) if lines else 0.0
        if lines > limit or content_headings:
            routing_payload.append({
                "path": rp, "layer": layer, "lines": lines, "limit": limit,
                "proseLines": prose, "proseRatio": ratio,
                "contentHeadings": content_headings[:10],
            })

    # ---- naming
    naming = []
    for rp in sorted(all_rel):
        base = os.path.basename(rp)
        if " " in rp:
            naming.append({"path": rp, "rule": "no-spaces"})
        stem = os.path.splitext(base)[0]
        # A SCREAMING-CASE stem at any depth is the near-universal convention
        # for a root document (README, LICENSE, TESTING, BLIND-SPOTS). Flagging
        # those as naming drift buries the real violations in noise.
        conventional = stem.upper() == stem and stem.replace("-", "").isalpha()
        if stem and stem.lower() != stem and not conventional:
            naming.append({"path": rp, "rule": "lowercase-with-hyphens"})
    for d in sorted(folder_rel):
        base = os.path.basename(d)
        if " " in base:
            naming.append({"path": d, "rule": "no-spaces"})
        elif base.lower() != base:
            naming.append({"path": d, "rule": "lowercase-with-hyphens"})

    # ---- schema drift
    schema_drift = {"schemaFile": None, "declared": [], "missingInTree": []}
    schema_path = None
    for p in md_paths:
        if os.path.basename(p).lower() == "schema.md":
            schema_path = p
            break
    if schema_path:
        declared = set()
        for m in re.finditer(r"`([A-Za-z0-9_.\-/]{3,})`", texts.get(schema_path, "")):
            token = m.group(1)
            if token.endswith((".md", ".json")) or "/" in token:
                declared.add(token)
        missing = []
        for token in sorted(declared):
            needle = token.strip("/").replace(os.sep, "/")
            if not any(needle in p for p in all_rel) and \
               not any(needle in d for d in folder_rel):
                missing.append(token)
        schema_drift = {"schemaFile": schema_path,
                        "declared": sorted(declared), "missingInTree": missing}

    # ---- generated index drift
    index_files = [p for p in md_paths
                   if os.path.basename(p).lower() in ("_index.md", "index.md")]
    listed_not_present, present_not_listed = [], []
    for idx in index_files:
        folder = os.path.dirname(idx)
        listed = set()
        for target, _line in extract_links(texts.get(idx, "")):
            resolved = resolve(target, idx, all_rel, root)
            if resolved:
                listed.add(resolved)
            else:
                listed_not_present.append({"index": idx, "target": target})
        siblings = set(p for p in md_paths
                       if p.startswith(folder + "/") and p != idx
                       and os.path.basename(p).lower() != "context.md")
        for s in sorted(siblings - listed):
            present_not_listed.append({"index": idx, "file": s})

    # ---- form guess
    has_specialist = all(("identity.md" in all_rel, "rules.md" in all_rel))
    numbered = [s for s in stages if s["index"]]
    if len(numbered) >= 2:
        form, why = "pipeline", "%d numbered stage folders" % len(numbered)
    elif has_specialist:
        form, why = "specialist", "identity.md and rules.md at the root"
    elif len(index_files) >= 1 and len(md_paths) > 8:
        form, why = "record-library", "an index file over a body of same-shaped notes"
    elif len(md_paths) <= 2 and not stages:
        form, why = "flat", "%d markdown files, no folder contracts" % len(md_paths)
    elif contracts_total >= 1:
        form, why = "mixed", "folder contracts present but no numbered sequence"
    else:
        form, why = "unknown", "no entry file, no contracts, no numbered stages"

    # ---- signal floor
    reasons = []
    if len(md_paths) < 3:
        reasons.append("under 3 markdown files")
    if form == "unknown":
        reasons.append("form could not be identified")
    if not entry_files and contracts_total == 0:
        reasons.append("no entry file and no folder contract")
    note = "LOW" if reasons else ("MEDIUM" if len(md_paths) < 8 else "HIGH")

    mtimes = [r["mtime"] for r in file_records if r["mtime"]]

    return {
        "generatedBy": VERSION,
        "workspace": root.replace(os.sep, "/"),
        "mtimeRange": {"oldest": min(mtimes) if mtimes else None,
                       "newest": max(mtimes) if mtimes else None},
        "form": {"guess": form, "why": why},
        "ignoredFiles": ignored_files,
        "totals": {
            "files": len(file_records), "markdownFiles": len(md_paths),
            "folders": len(folder_rel), "bytes": total_bytes,
            "estTokens": sum(r["estTokens"] for r in file_records),
        },
        "entry": {
            "files": entry_files, "lines": entry_lines, "estTokens": entry_tokens,
            "twins": entry_files if len(entry_files) > 1 else [],
            "twinsIdentical": twins_identical,
        },
        "layers": {
            layer: sorted(r["path"] for r in file_records if r["layer"] == layer)
            for layer in ("L0", "L1", "L2", "L3", "L4",
                          "template", "meta", "unclassified")
        },
        "files": sorted(file_records, key=lambda r: r["path"]),
        "stages": stages,
        "graph": {
            "edges": edges, "dangling": dangling, "orphans": orphans,
            "brokenLinks": broken_links,
            "externalCitations": external_refs,
            "brokenLinkCount": len(broken_links),
            "externalCitationCount": len(external_refs),
            "backReferences": back_refs,
            "backReferencesByFolder": back_refs_folder,
            "declaredOutputsNotYetProduced": not_yet_produced,
        },
        "placeholders": {"total": ph_total, "outsideTemplates": ph_outside,
                         "sample": ph_sample},
        "duplication": duplication_clusters(
            {p: t for p, t in texts.items()
             if by_path[p]["layer"] != "template"
             and p.lower().endswith((".md", ".markdown"))}),
        "routingPayload": routing_payload,
        "naming": {"violations": naming},
        "schemaDrift": schema_drift,
        "index": {"indexFiles": index_files,
                  "listedNotPresent": listed_not_present,
                  "presentNotListed": present_not_listed},
        "gates": {"contractsTotal": contracts_total,
                  "contractsWithHumanCheck": contracts_with_gate},
        "signal": {"note": note, "reasons": reasons},
        "heuristics": [
            "form.guess", "routingPayload", "duplication",
            "declaredInputs[].styleReference", "estTokens",
            "loadEstimate.band", "schemaDrift",
        ],
    }


# ---------------------------------------------------------------- self test

SELFTEST_TREES = {
    "broken": {
        "CLAUDE.md": "# Workspace\n\n## Voice rules\n" + ("Write warmly and clearly.\n" * 80),
        "AGENTS.md": "# Workspace\n\nDifferent instructions entirely.\n",
        "stages/01-research/CONTEXT.md":
            "# 01 research\n\n## Inputs\n- the brief\n\n## Process\n1. Read it.\n\n"
            "## Outputs\n- `output/research.md`\n",
        "stages/01-research/output/.gitkeep": "",
        "stages/02-draft/CONTEXT.md":
            "# 02 draft\n\n## Inputs\n"
            "| Source | File | Section | Why |\n|---|---|---|---|\n"
            "| Working | `../01-research/output/missing.md` | Full file | input |\n"
            "| Reference | `../../shared/voice.md` | Full file | tone |\n\n"
            "## Process\n1. Draft it.\n\n## Outputs\n- `output/draft.md`\n",
        "stages/02-draft/output/.gitkeep": "",
        "shared/voice.md": "# Voice\n\n" + ("A long reference file line.\n" * 260),
        "shared/orphan-notes.md": "# Notes\n\nNothing points at this file at all.\n",
        "shared/brand.md": "# Brand\n\nThe brand colour is {{PRIMARY_COLOR}}.\n",
    },
    "healthy": {
        "CLAUDE.md": "# Workspace\n\n| You want to | Go to |\n|---|---|\n"
                     "| Run the pipeline | `CONTEXT.md` |\n",
        "CONTEXT.md": "# Pipeline\n\n| Task | Stage |\n|---|---|\n"
                      "| research | `stages/01-research/CONTEXT.md` |\n",
        "stages/01-research/CONTEXT.md":
            "# 01 research\n\nOne job: gather the source material.\n\n"
            "## Inputs\n- Working (this run): `../../input/brief.md`\n\n"
            "## Process\n1. Read the brief.\n\n"
            "## Outputs\n- `output/research.md`\n\n"
            "## Human check\nRead the research before the next stage runs.\n",
        "stages/01-research/output/research.md": "# Research\n\nFindings.\n",
        "input/brief.md": "# Brief\n\nThe ask.\n",
    },
}


def write_tree(base, tree):
    for relpath, content in tree.items():
        full = os.path.join(base, relpath.replace("/", os.sep))
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as fh:
            fh.write(content)


def selftest():
    """Build two known trees and prove the fingerprints fire on one and stay
    quiet on the other. A miner nobody has tested is a rumour."""
    checks = []
    with tempfile.TemporaryDirectory() as tmp:
        broken_dir = os.path.join(tmp, "broken")
        healthy_dir = os.path.join(tmp, "healthy")
        write_tree(broken_dir, SELFTEST_TREES["broken"])
        write_tree(healthy_dir, SELFTEST_TREES["healthy"])
        b = mine(broken_dir)
        h = mine(healthy_dir)

        checks.append(("family 1  routing payload fires",
                       len(b["routingPayload"]) > 0))
        checks.append(("family 2  drifting twins detected",
                       len(b["entry"]["twins"]) == 2
                       and b["entry"]["twinsIdentical"] is False))
        checks.append(("family 6  full-file row on a >200 line reference",
                       any(e.get("scope") == "Full file"
                           and (e.get("targetLines") or 0) > 200
                           for st in b["stages"] for e in st["declaredInputs"])))
        checks.append(("family 10 placeholder outside templates",
                       b["placeholders"]["outsideTemplates"] == 1))
        checks.append(("family 12 declared input that does not exist",
                       any(e["exists"] is False and e["path"]
                           for st in b["stages"] for e in st["declaredInputs"])))
        checks.append(("broken link separated from external citation",
                       b["graph"]["brokenLinkCount"] >= 1
                       and all(d["kind"] in ("broken", "external")
                               for d in b["graph"]["dangling"])))
        checks.append(("family 13 orphan reference file",
                       "shared/orphan-notes.md" in b["graph"]["orphans"]))
        checks.append(("family 17 no human check in any contract",
                       b["gates"]["contractsWithHumanCheck"] == 0
                       and b["gates"]["contractsTotal"] == 2))
        checks.append(("family 18 every output folder holds only .gitkeep",
                       all(st["outputFolder"]["onlyGitkeep"]
                           for st in b["stages"] if st["outputFolder"])))
        checks.append(("form guessed as pipeline",
                       b["form"]["guess"] == "pipeline"))

        checks.append(("healthy tree: no routing payload",
                       len(h["routingPayload"]) == 0))
        checks.append(("healthy tree: no dangling references",
                       len(h["graph"]["dangling"]) == 0))
        checks.append(("healthy tree: no orphans",
                       len(h["graph"]["orphans"]) == 0))
        checks.append(("healthy tree: the human check is found",
                       h["gates"]["contractsWithHumanCheck"] == 1))
        checks.append(("healthy tree: output folder is not empty",
                       h["stages"][0]["outputFolder"]["fileCount"] == 1))

    ok = True
    for label, passed in checks:
        print("%s %s" % ("OK  " if passed else "BAD ", label))
        ok &= bool(passed)
    print("MINER SELFTEST %s (%d checks)" % ("PASS" if ok else "FAIL", len(checks)))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description="Mine an ICM workspace into evidence.json")
    ap.add_argument("workspace", nargs="?", help="path to the workspace folder")
    ap.add_argument("-o", "--out", help="write evidence.json here (default: stdout)")
    ap.add_argument("--selftest", action="store_true",
                    help="build known trees and prove the fingerprints fire")
    args = ap.parse_args()

    if args.selftest:
        return selftest()
    if not args.workspace:
        ap.print_help()
        return 1

    data = mine(args.workspace)
    blob = json.dumps(data, indent=2, sort_keys=False)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(blob + "\n")
        print("wrote %s  (%d files, %d markdown, signal %s)"
              % (args.out, data["totals"]["files"],
                 data["totals"]["markdownFiles"], data["signal"]["note"]))
    else:
        print(blob)
    return 0


if __name__ == "__main__":
    sys.exit(main())
