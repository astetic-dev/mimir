#!/usr/bin/env python3
"""verify.py - structural gate on a Mimir finding.

A must in a markdown file is a request. A must in code is a constraint.
This checker enforces, offline and without an API key, what
reference/output-contract.md requires in prose.

  FORMAT       all nine sections, once each, in order
  ONE-CAUSE    DIAGNOSIS names a single primary cause: no list, bounded length
  MARKED       every EVIDENCE CHAIN link carries [seen] / [inferred] / [general]
  GROUNDING    every quoted span on a [seen] line appears verbatim in the
               evidence or the transcript
  CITATIONS    every path and every multi-digit number anywhere in the finding
               is present in the evidence or the transcript, quoted or not
  NO-RX        no remedy language, and no counterfactual - advice wearing the
               past tense is still advice
  ABSTAIN      UNRESOLVED requires named tied candidates; a named cause may not
               also claim UNRESOLVED
  NO-APPENDIX  nothing after the closing line
  FALSIFIER    the overturn section is non-empty and prescribes nothing

Five of these nine exist in no other diagnostic folder we know of: GROUNDING's
extension to unquoted details, MARKED, NO-RX's counterfactual arm, ABSTAIN and
NO-APPENDIX. See CREDITS.md.

Usage:
  python verify.py <finding.md> <evidence.json> [transcript.txt]
  python verify.py --selftest
  python verify.py --manifest <workspace-path>
"""

import argparse
import json
import os
import re
import sys

SECTIONS = [
    "DIAGNOSIS:",
    "EVIDENCE TIER:",
    "EVIDENCE CHAIN:",
    "WHY IT STOPS HERE:",
    "RULED OUT:",
    "CONTRIBUTING FACTORS:",
    "WEAKEST LINK:",
    "CONFIDENCE:",
    "WHAT WOULD OVERTURN THIS:",
]

MARKERS = ("[seen]", "[inferred]", "[general]")

CLOSING_STEMS = (
    "this finding was produced by an ai system",
)

# The two permitted forms of the frozen closing line, normalised. Every
# non-blank line after the stem must be a contiguous fragment of one of them,
# and nothing else may follow. Checked per variant, because a fragment that
# spans the seam between two variants is not a fragment of either.
ALLOWED_CLOSING = (
    "this finding was produced by an ai system from the evidence listed above. "
    "it names a cause only and proposes no change to the workspace. "
    "conclusions are bounded by that evidence.",
    "this finding was produced by an ai system from the evidence listed above. "
    "it names no cause: it records why the evidence cannot carry one, and "
    "proposes no change to the workspace. "
    "conclusions are bounded by that evidence.",
)


def is_closing_fragment(piece):
    return any(piece in variant for variant in ALLOWED_CLOSING)

CONFIDENCE_LEVELS = ("high", "moderate", "provisional", "unresolved")

FROZEN_UNRESOLVED = (
    "two causes explain this evidence equally well and the workspace cannot "
    "separate them"
)

# Paths a finding may legitimately name without them being in the mined tree:
# Mimir's own doctrine, and the ICM canon the taxonomy tells findings to cite.
CITATION_ALLOWLIST = (
    "identity.md", "rules.md", "intake.md", "examples.md", "readme.md",
    "reference/", "checks/", "evidence.json", "mine.py", "verify.py",
    "_core/conventions.md", "_core/placeholder-syntax.md",
    "icm-architect/skill.md", "references/core.md", "references/forms.md",
    "references/system-map.md", "assets/templates/",
)

# Number tokens that are canon references rather than measurements.
CANON_NUMBER_PREFIX = re.compile(
    r"(family|families|invariant|invariants|pattern|patterns|step|steps|"
    r"section|layer|arxiv:|principle|shape|tier)\s*[:#]?\s*$", re.I)

PATH_RE = re.compile(r"(?<![\w`])((?:\.{0,2}/)?(?:[\w.\-]+/)+[\w.\-]+"
                     r"\.(?:md|markdown|json|ya?ml|txt|py|mjs|js))")
NUMBER_RE = re.compile(r"(?<![\w.\-])(\d{2,}(?:[.,]\d+)?)(?![\w])")

RX_PATTERNS = [
    r"\byou (should|need to|must|ought to|could|can) (move|split|add|remove|delete|"
    r"rename|create|write|put|change|update|refactor|restructure|extract|point|route)\b",
    r"\bto fix (this|it|that)\b",
    r"\bthe fix (is|would be)\b",
    r"\bnext steps?\b",
    r"\brecommend(ation|ations|ed|s)?\b",
    r"\btry (this|that|instead)\b",
    r"\binstead,? (use|move|put|split|point|route|keep)\b",
    r"\b(move|split|extract|relocate|consolidate) (the|this|that|those|these|your)\s+"
    r"[\w\- ]{0,30}(file|rule|rules|section|folder|content|payload|reference|table)\b",
    r"\b(should|ought to) (live|sit|go|move|point|be split|be moved|be extracted)\b",
    r"\bwould (fix|solve|resolve|repair)\b",
    r"\bconsider (moving|splitting|adding|removing|using|routing|extracting)\b",
    r"\btarget tree\b",
    r"\bmigration (map|plan)\b",
    r"^\s*#{0,6}\s*(recommendations?|next steps?|solution|remediation|"
    r"what to do|suggested changes?)\b",
]

# The counterfactual arm. "A counterfactual is advice wearing the past tense."
CF_PATTERNS = [
    r"\bif (the|this|that|it|you|they|there|a|an)\b[^.\n]{0,80}\b(had|had been|were)\b",
    r"\bhad (the|this|that|it|there|they|a|an)\b[^.\n]{0,80}\b(been|existed|named|"
    r"pointed|routed|loaded|carried|lived)\b",
    r"\bwould (not )?have (been|happened|occurred|loaded|failed|arrived|"
    r"prevented|avoided|caught|stopped)\b",
    r"\b(could|would) have been (avoided|prevented|caught)\b",
    r"\bwith(out)? a [\w\- ]{0,30}, (this|the failure|it) would\b",
]

# An evidence act asks a question about the world; a remedy changes it.
# Deliberately narrow: bare "check" and "confirm" are ordinary domain words
# here - "Human check" is a section name in every ICM stage contract - so an
# allowlist built on them would exempt half the remedies in the language.
EVIDENCE_ACT = (r"\b(would confirm|would overturn|would contradict|"
                r"check whether|check that|confirm whether|confirm that|"
                r"look ?up|compare|re-?run|run `?mine\.py|run `?verify\.py|"
                r"show me|paste|read back)\b")

# --------------------------------------------------------------- languages
#
# output-contract.md 6 says the finding is written in the owner's language.
# A gate that only speaks English therefore passes every other language
# vacuously, which is worse than having no gate: it issues a receipt it has
# not earned. So each supported language carries its own word lists, and a
# finding in a language with no list FAILS rather than passing.

RX_NL = [
    r"\b(je|jij|u) (moet|zou moeten|kunt|kan|moest|dient te) (verplaats|splits|"
    r"voeg|verwijder|hernoem|maak|schrijf|zet|wijzig|pas|verhuis|neem|route)\w*\b",
    r"\bde (oplossing|fix|remedie) (is|zou)\b",
    r"\bvolgende stap(pen)?\b",
    r"\baanbevel(ing|ingen|en|t|ingsw)\w*\b",
    r"\b(advies|adviseer|adviseren)\b",
    r"\bin plaats daarvan\b",
    r"\b(verplaats|splits|verhuis|hernoem|consolideer) (de|het|die|dat|deze|je)\b",
    r"\bzou (moeten|beter) (staan|zijn|worden|liggen|gaan)\b",
    r"\bhoort (thuis |te staan )?in\b",
    r"\bmoet (naar|in) (de|het|een)\b",
    r"^\s*#{0,6}\s*(aanbevelingen?|volgende stappen?|oplossing|remedie|wat te doen)\b",
]

CF_NL = [
    r"\bals (de|het|die|dat|je|er|een|deze)\b[^.\n]{0,80}\b(had|hadden|was|waren)\b",
    r"\bzou (dit|dat|het|de storing|de fout|hij|ze) (niet )?(zijn |hebben )?"
    r"(gebeurd|opgetreden|voorgekomen|plaatsgevonden|geladen|gemist)\b",
    r"\bwas (dit|dat|het|de storing) (niet )?(gebeurd|opgetreden|voorgekomen)\b",
    r"\bhad (de|het|je|die|dat|er)\b[^.\n]{0,60}\b(genoemd|geladen|gestaan|bestaan|"
    r"gerouteerd|gedekt)\b",
    r"\bwas er (maar |wel )?(een|de|het)\b[^.\n]{0,40}\bgeweest\b",
]

EVIDENCE_ACT_NL = (r"\b(zou bevestigen|zou weerleggen|weerlegt|bevestigt|"
                   r"controleer of|controleer dat|kijk of|vergelijk|"
                   r"opnieuw draaien|draai .{0,15}opnieuw|laat zien|plak|"
                   r"lees terug)\b")

LANGUAGES = {
    "en": {"rx": RX_PATTERNS, "cf": CF_PATTERNS, "act": EVIDENCE_ACT,
           "stops": ("the", "and", "of", "that", "is", "not", "with", "this",
                     "which", "from", "does")},
    "nl": {"rx": RX_NL, "cf": CF_NL, "act": EVIDENCE_ACT_NL,
           "stops": ("de", "het", "een", "van", "dat", "niet", "wordt", "voor",
                     "met", "zijn", "die", "geen", "staat")},
}


def detect_language(text):
    """Which word lists to police this finding with. Returns a key of
    LANGUAGES, or None when no list covers it - which is a gate failure, not
    a free pass."""
    words = re.findall(r"[a-zA-ZÀ-ſ]+", text.lower())
    if not words:
        return None
    counts = {}
    for key, spec in LANGUAGES.items():
        counts[key] = sum(1 for w in words if w in spec["stops"])
    best = max(counts, key=counts.get)
    # A real finding is prose; if almost no stopword of any known language
    # shows up, we are not looking at a language we can police.
    if counts[best] < max(8, len(words) // 60):
        return None
    return best


def norm(s):
    return re.sub(r"\s+", " ", s).strip().lower()


def strip_quoted(text):
    """Blank out double-quoted spans so material the owner wrote is not scanned
    as if Mimir had written it.

    The span may cross a line break - prose in this contract wraps constantly -
    and a newline-bounded pattern does not merely miss those, it desynchronises
    quote parity for the rest of the line and blanks the wrong text.
    """
    return re.sub(r'"[^"]*"', '""', text)


def strip_closing(text):
    """Everything up to the frozen closing line."""
    low = text.lower()
    for stem in CLOSING_STEMS:
        idx = low.find(stem)
        if idx != -1:
            back = text.rfind("\n", 0, idx)
            return text[:back if back != -1 else idx], text[back if back != -1 else idx:]
    return text, ""


def section_index(text):
    idx = {}
    for s in SECTIONS:
        idx[s] = [m.start() for m in re.finditer(re.escape(s), text)]
    return idx


def get_section(text, idx, name):
    if not idx.get(name):
        return ""
    start = idx[name][0] + len(name)
    later = [idx[s][0] for s in SECTIONS if idx.get(s) and idx[s][0] > idx[name][0]]
    end = min(later) if later else len(text)
    return text[start:end]


def load_workspace_text(evidence, evidence_path):
    """Read the mined workspace itself, so a [seen] quote from a file in the
    tree can be grounded. output-contract.md defines [seen] as present in the
    tree, in evidence.json, or in the transcript - all three, not just the two
    that happen to be JSON.

    The absolute path in evidence.json belongs to the machine that mined it, so
    fall back to a `workspace/` folder beside the evidence file. That is what
    makes the shipped fixtures verifiable on someone else's disk.
    """
    roots = []
    if isinstance(evidence, dict) and evidence.get("workspace"):
        roots.append(evidence["workspace"])
    if evidence_path:
        roots.append(os.path.join(os.path.dirname(os.path.abspath(evidence_path)),
                                  "workspace"))
    for root in roots:
        if not root or not os.path.isdir(root):
            continue
        chunks = []
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if d not in (".git", "node_modules")]
            for fn in sorted(filenames):
                if fn.lower().endswith((".md", ".markdown", ".txt")):
                    try:
                        with open(os.path.join(dirpath, fn), "r",
                                  encoding="utf-8", errors="replace") as fh:
                            chunks.append(fh.read())
                    except OSError:
                        pass
        if chunks:
            return "\n".join(chunks)
    return ""


def collect_evidence_strings(evidence, transcript, tree_text=""):
    """Everything a finding is allowed to quote or cite."""
    blob = json.dumps(evidence, sort_keys=True) if evidence is not None else ""
    blob = blob + "\n" + tree_text
    paths = set()
    if isinstance(evidence, dict):
        for rec in evidence.get("files", []):
            paths.add(rec.get("path", "").lower())
        for st in evidence.get("stages", []):
            if st.get("folder"):
                paths.add(st["folder"].lower())
            if st.get("contract"):
                paths.add(st["contract"].lower())
            for e in st.get("declaredInputs", []) + st.get("declaredOutputs", []):
                for key in ("path", "resolved"):
                    if e.get(key):
                        paths.add(str(e[key]).lower())
            of = st.get("outputFolder")
            if of and of.get("path"):
                paths.add(of["path"].lower())
        for d in evidence.get("graph", {}).get("dangling", []):
            if d.get("target"):
                paths.add(str(d["target"]).lower())
    numbers = set(NUMBER_RE.findall(blob))
    numbers |= set(NUMBER_RE.findall(transcript or ""))
    return {
        "blob": norm(blob) + " " + norm(transcript or ""),
        "paths": {p for p in paths if p},
        "numbers": numbers,
        "raw": (blob + "\n" + (transcript or "")),
    }


def check(finding_path, evidence_path, transcript_path=None, quiet=False):
    failures = []
    text = open(finding_path, "r", encoding="utf-8").read()
    evidence = None
    if evidence_path and os.path.exists(evidence_path):
        with open(evidence_path, "r", encoding="utf-8") as fh:
            evidence = json.load(fh)
    transcript = ""
    if transcript_path and os.path.exists(transcript_path):
        transcript = open(transcript_path, "r", encoding="utf-8").read()
    tree_text = load_workspace_text(evidence, evidence_path)
    ev = collect_evidence_strings(evidence, transcript, tree_text)

    body, closing = strip_closing(text)
    idx = section_index(body)

    # ---------------------------------------------------------------- FORMAT
    for s in SECTIONS:
        if len(idx[s]) == 0:
            failures.append(("FORMAT", "missing section %r" % s))
        elif len(idx[s]) > 1:
            failures.append(("FORMAT", "section %r appears %d times" % (s, len(idx[s]))))
    if not failures:
        order = [idx[s][0] for s in SECTIONS]
        if order != sorted(order):
            failures.append(("FORMAT", "sections out of order"))

    diagnosis = get_section(body, idx, "DIAGNOSIS:")
    chain = get_section(body, idx, "EVIDENCE CHAIN:")
    stops = get_section(body, idx, "WHY IT STOPS HERE:")
    confidence = get_section(body, idx, "CONFIDENCE:")
    overturn = get_section(body, idx, "WHAT WOULD OVERTURN THIS:")

    # ------------------------------------------------------------- ONE-CAUSE
    if diagnosis:
        if re.search(r"^\s*(\d+[.)]|[-*+])\s+", diagnosis, re.M):
            failures.append(("ONE-CAUSE",
                             "DIAGNOSIS contains a list; one primary cause only"))
        if re.search(r"\b(several|multiple|two|three|four|a number of|both)\s+"
                     r"(possible |likely |candidate |primary )?causes\b",
                     diagnosis, re.I) and "unresolved" not in confidence.lower():
            failures.append(("ONE-CAUSE", "DIAGNOSIS hedges across multiple causes"))
        sentences = [s for s in re.split(r"(?<=[.!?])\s+", diagnosis.strip()) if s.strip()]
        if len(sentences) > 4:
            failures.append(("ONE-CAUSE",
                             "DIAGNOSIS is %d sentences; state one cause, tightly (max 4)"
                             % len(sentences)))

    # ---------------------------------------------------------------- MARKED
    # A chain link is a numbered line plus its continuation lines. Treating a
    # link as one line lets a quote escape GROUNDING simply by being long
    # enough to wrap, and prose in this contract wraps constantly.
    chain_blocks = []
    for raw in chain.splitlines():
        if re.match(r"^\s*\d+[.)]\s+", raw):
            chain_blocks.append([raw])
        elif chain_blocks and raw.strip():
            chain_blocks[-1].append(raw)
    chain_links = [re.sub(r"\s+", " ", " ".join(b)).strip() for b in chain_blocks]

    if chain.strip() and not chain_links:
        failures.append(("MARKED", "EVIDENCE CHAIN has no numbered links"))
    for link in chain_links:
        if not any(m in link for m in MARKERS):
            failures.append(("MARKED",
                             "chain link carries no marker: %s" % link[:70]))

    # ------------------------------------------------------------- GROUNDING
    grounded = 0
    for link in chain_links:
        if "[seen]" not in link:
            continue
        for q in re.findall(r'"([^"]+)"', link):
            grounded += 1
            parts = [p for p in re.split(r"\(\.\.\.\)|\.\.\.", q) if p.strip()]
            for p in parts:
                if norm(p) not in ev["blob"]:
                    failures.append(("GROUNDING",
                                     "[seen] quote not found in evidence: \"%s\""
                                     % p.strip()[:70]))

    # ------------------------------------------------------------- CITATIONS
    scannable = strip_quoted(body)
    for m in PATH_RE.finditer(scannable):
        cited = m.group(1).lower().lstrip("./")
        if any(cited.startswith(a) or cited == a or a in cited
               for a in CITATION_ALLOWLIST):
            continue
        if ev["paths"] and any(cited in p or p.endswith(cited) or cited.endswith(p)
                               for p in ev["paths"]):
            continue
        if norm(cited) in ev["blob"]:
            continue
        failures.append(("CITATIONS", "path not present in the evidence: %s" % m.group(1)))
    for m in NUMBER_RE.finditer(scannable):
        before = scannable[max(0, m.start() - 24):m.start()]
        if CANON_NUMBER_PREFIX.search(before):
            continue
        if m.group(1) in ev["numbers"]:
            continue
        if m.group(1) in ev["blob"]:
            continue
        failures.append(("CITATIONS",
                         "number not present in the evidence: %s" % m.group(1)))

    # ------------------------------------------------------------------ NORX
    # Scan a whitespace-flattened copy: a remedy that happens to wrap across
    # two lines is still a remedy, and prose in this contract wraps constantly.
    flat = re.sub(r"[ \t]*\n[ \t]*", " ", scannable)
    flat = re.sub(r"[ \t]+", " ", flat)
    lang = detect_language(body)
    if lang is None:
        failures.append(("NO-RX",
                         "no remedy word list for the language of this finding; "
                         "the gate cannot certify it (supported: %s)"
                         % ", ".join(sorted(LANGUAGES))))
        spec = LANGUAGES["en"]
    else:
        spec = LANGUAGES[lang]
    for pat in spec["rx"]:
        for m in re.finditer(pat, flat, re.I | re.M):
            if re.search(spec["act"], _sentence_of(flat, m.start()), re.I):
                continue
            failures.append(("NO-RX", "remedy language: %r" % m.group(0).strip()))
    # The removal test legitimately lives in WHY IT STOPS HERE, so the
    # counterfactual arm exempts that section only (rules.md step 6).
    stops_flat = re.sub(r"[ \t]*\n[ \t]*", " ", strip_quoted(stops))
    stops_flat = re.sub(r"[ \t]+", " ", stops_flat).strip()
    cf_scannable = flat
    if stops_flat and stops_flat in flat:
        cf_scannable = flat.replace(stops_flat, " " * len(stops_flat))
    for pat in spec["cf"]:
        for m in re.finditer(pat, cf_scannable, re.I):
            failures.append(("NO-RX",
                             "counterfactual (advice in the past tense): %r"
                             % m.group(0).strip()[:70]))

    # ----------------------------------------------------------------- PLAIN
    # A cause family is engine vocabulary. The reader owns the failure, not the
    # taxonomy, so the sentence must carry the meaning in their own words and
    # the label may only ride along in brackets as an index for auditing.
    # Without this the finding reads as "family 8" to the person it is for.
    for m in re.finditer(r"\bfami(?:ly|lie)\s+\d+", body, re.I):
        before = body[max(0, m.start() - 2):m.start()]
        after = body[m.end():m.end() + 2]
        if "(" in before and ")" in after:
            continue
        failures.append(("PLAIN",
                         "cause family named as a bare label: %r - state the "
                         "cause in the reader's words and put the index in "
                         "brackets" % m.group(0)))

    # --------------------------------------------------------------- ABSTAIN
    conf_low = confidence.lower()
    level = [l for l in CONFIDENCE_LEVELS if re.search(r"\b%s\b" % l, conf_low)]
    if not level:
        failures.append(("ABSTAIN",
                         "no stated level (high | moderate | provisional | UNRESOLVED)"))
    elif "unresolved" in level:
        if FROZEN_UNRESOLVED not in norm(body):
            failures.append(("ABSTAIN",
                             "UNRESOLVED without the frozen text of output-contract 5.4"))
        families = set(re.findall(r"\bfami(?:ly|lie)\s+(\d+)", body, re.I))
        if len(families) < 2:
            failures.append(("ABSTAIN",
                             "UNRESOLVED must name at least two tied candidates, "
                             "each with its taxonomy index; found %d"
                             % len(families)))
    else:
        if re.search(r"\bunresolved\b", diagnosis, re.I):
            failures.append(("ABSTAIN",
                             "DIAGNOSIS claims UNRESOLVED but CONFIDENCE is %s"
                             % level[0]))

    # ----------------------------------------------------------- NO-APPENDIX
    # The closing line wraps across however many lines the author's column
    # width dictates, so match on content rather than on line shape: every
    # non-blank line after the stem must be a fragment of the frozen text.
    if closing == "":
        failures.append(("NO-APPENDIX", "the frozen closing line is missing"))
    else:
        extra = []
        started = False
        for raw in closing.splitlines():
            stripped = raw.strip()
            if not stripped:
                continue
            piece = norm(stripped.lstrip("> ").strip("*_ "))
            if not started:
                if any(stem in piece for stem in CLOSING_STEMS):
                    started = True
                    # the stem line may carry the whole sentence; that is fine
                    continue
                continue
            if piece and is_closing_fragment(piece):
                continue
            if piece:
                extra.append(stripped)
        if extra:
            failures.append(("NO-APPENDIX",
                             "text after the closing line: %r" % extra[0][:70]))

    # ------------------------------------------------------------- FALSIFIER
    if len(overturn.strip()) < 20:
        failures.append(("FALSIFIER",
                         "WHAT WOULD OVERTURN THIS is empty or too thin to be a test"))

    if not quiet:
        if failures:
            print("FAIL %s" % finding_path)
            for gate, msg in failures:
                print("  [%s] %s" % (gate, msg))
        else:
            print("PASS %s  (9 gates; %d chain links, %d quotes grounded)"
                  % (finding_path, len(chain_links), grounded))
    return failures


def _line_of(text, pos):
    start = text.rfind("\n", 0, pos) + 1
    end = text.find("\n", pos)
    return text[start:end if end != -1 else len(text)]


def _sentence_of(text, pos):
    """The sentence a match sits in. The evidence-act exemption is scoped to
    the sentence, not to a character window: a legitimate evidence act two
    sentences away must not launder a remedy."""
    start = max(text.rfind(". ", 0, pos), text.rfind("\n", 0, pos))
    end = text.find(". ", pos)
    return text[(start + 1 if start != -1 else 0):(end if end != -1 else len(text))]


# ------------------------------------------------------- doctrine/eval split

DOCTRINE_FILES = ("identity.md", "rules.md", "intake.md")
DOCTRINE_DIRS = ("reference",)
EVAL_MARKERS = ("eval/", "tests/", "expected.md", "answer key", "TESTING.md")


def manifest(workspace):
    """The doctrine must not be able to see its own answer key.

    A blind run loads identity.md, rules.md, intake.md and reference/. If any
    of those points at eval material, the run is not blind and every receipt
    taken from it is worth nothing.
    """
    problems = []
    checked = 0
    targets = []
    for name in DOCTRINE_FILES:
        p = os.path.join(workspace, name)
        if os.path.exists(p):
            targets.append(p)
    for d in DOCTRINE_DIRS:
        full = os.path.join(workspace, d)
        if os.path.isdir(full):
            for fn in sorted(os.listdir(full)):
                if fn.endswith(".md"):
                    targets.append(os.path.join(full, fn))
    for p in targets:
        checked += 1
        text = open(p, "r", encoding="utf-8").read()
        for i, line in enumerate(text.splitlines(), start=1):
            for marker in EVAL_MARKERS:
                if marker in line:
                    problems.append((os.path.basename(p), i, marker, line.strip()[:70]))
    if problems:
        print("FAIL manifest: doctrine references evaluation material")
        for name, line, marker, snippet in problems:
            print("  [MANIFEST] %s:%d refers to %r  -> %s" % (name, line, marker, snippet))
    else:
        print("PASS manifest: %d doctrine files, none reference eval material" % checked)
    return problems


# --------------------------------------------------------------- self test

def selftest():
    here = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures")
    evidence = os.path.join(here, "evidence.json")
    transcript = os.path.join(here, "transcript.txt")
    plan = [
        ("good-finding.md", None),
        ("bad-format.md", "FORMAT"),
        ("bad-two-causes.md", "ONE-CAUSE"),
        ("bad-unmarked.md", "MARKED"),
        ("bad-fabricated-quote.md", "GROUNDING"),
        ("bad-wrapped-quote.md", "GROUNDING"),
        ("bad-invented-number.md", "CITATIONS"),
        ("bad-prescription.md", "NO-RX"),
        ("bad-counterfactual.md", "NO-RX"),
        ("bad-jargon.md", "PLAIN"),
        ("bad-hidden-tie.md", "ABSTAIN"),
        ("bad-appendix.md", "NO-APPENDIX"),
    ]
    ok = True
    for name, expected in plan:
        path = os.path.join(here, name)
        if not os.path.exists(path):
            print("BAD  %s: fixture missing" % name)
            ok = False
            continue
        failures = check(path, evidence, transcript, quiet=True)
        gates = {f[0] for f in failures}
        if expected is None:
            passed = not failures
            verdict = "clean pass" if passed else "unexpected failures %s" % sorted(gates)
        else:
            passed = expected in gates
            verdict = ("fails on [%s] as designed" % expected if passed
                       else "expected [%s], got %s" % (expected, sorted(gates) or "clean pass"))
        print("%s %-26s %s" % ("OK  " if passed else "BAD ", name, verdict))
        ok &= passed
    print("CHECKER SELFTEST %s (%d fixtures)" % ("PASS" if ok else "FAIL", len(plan)))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description="Gate a Mimir finding")
    ap.add_argument("finding", nargs="?", help="the finding markdown file")
    ap.add_argument("evidence", nargs="?", help="evidence.json from mine.py")
    ap.add_argument("transcript", nargs="?", help="optional transcript of the failing run")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--manifest", metavar="WORKSPACE",
                    help="check that doctrine files do not reference eval material")
    args = ap.parse_args()

    if args.selftest:
        return selftest()
    if args.manifest:
        return 1 if manifest(args.manifest) else 0
    if not args.finding or not args.evidence:
        ap.print_help()
        return 1
    return 1 if check(args.finding, args.evidence, args.transcript) else 0


if __name__ == "__main__":
    sys.exit(main())
