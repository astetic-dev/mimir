# TESTING - what has been proved, and what has not

Everything here is reproducible from this folder. Inputs are in `eval/`, the
gates are in `checks/`, and every answer key was written and committed before
the run it scores exists.

**Two kinds of claim live in this file and they are not equal.** The
deterministic results below have been run and are receipts. The behavioural
results are `PENDING`, because a blind run needs a fresh session and this folder
was written in one. A `PENDING` row stays `PENDING` until somebody runs it. It
is never filled in from expectation.

---

## Load and verify are different sets

| Set | Files | Rule |
|---|---|---|
| **Load** | `identity.md`, `rules.md`, `intake.md`, `reference/` (5 files) | the doctrine. This is what a scored run receives |
| **Read** | `README.md`, `examples.md`, `BUILD.md`, `CLAUDE.md` | for people. Never loaded in a scored run |
| **Verify** | `checks/`, `eval/`, this file, `DEFECTS.md`, `BLIND-SPOTS.md` | evidence *about* Mimir. Never loaded, ever |

If any file under `eval/` were loaded into a scored run, every behavioural
receipt below would be worth nothing, because the tool would be reasoning about
material it had already been shown. That separation is enforced mechanically:

```
python checks/verify.py --manifest .
PASS manifest: 8 doctrine files, none reference eval material
```

---

## Deterministic results - run, and reproducible in under a minute

Run date 2026-08-16, Python 3 stdlib only, no network.

| # | Test | Command | Result |
|---|---|---|---|
| T1 | Miner fingerprints fire on a known-broken tree and stay quiet on a known-healthy one | `python checks/mine.py --selftest` | **PASS, 14 checks** |
| T2 | Checker gate: one good finding passes, nine bad ones each fail on their own named gate | `python checks/verify.py --selftest` | **PASS, 10 fixtures** |
| T3 | Doctrine cannot see the answer keys | `python checks/verify.py --manifest .` | **PASS, 8 doctrine files** |
| T4 | The shipped worked finding passes all nine gates against real mined evidence | `python checks/verify.py checks/fixtures/good-finding.md checks/fixtures/evidence.json checks/fixtures/transcript.txt` | **PASS - 7 chain links, 7 quotes grounded** |
| T5 | Mimir's own folder passes his own miner | `python checks/mine.py .` | **PASS with two acquitted signals and one open defect - see below** |

### T2 in detail

Each negative fixture fails on **exactly** its own gate and nothing else. That
is the contract: a change to `verify.py` that lets any of them through is a
regression.

| Fixture | Gate it must fail | What it does |
|---|---|---|
| `good-finding.md` | none | clean pass |
| `bad-format.md` | FORMAT | drops RULED OUT and WEAKEST LINK |
| `bad-two-causes.md` | ONE-CAUSE | a ranked-nothing list of three |
| `bad-unmarked.md` | MARKED | chain links with no `[seen]` / `[inferred]` / `[general]` |
| `bad-fabricated-quote.md` | GROUNDING | quotes a heading the workspace does not contain |
| `bad-invented-number.md` | CITATIONS | says 312 lines where the miner counted 135 |
| `bad-prescription.md` | NO-RX | a remedy hiding in CONTRIBUTING FACTORS |
| `bad-counterfactual.md` | NO-RX | "if the rules had lived in a reference file..." |
| `bad-hidden-tie.md` | ABSTAIN | claims UNRESOLVED without naming the tied candidates |
| `bad-appendix.md` | NO-APPENDIX | a warm sign-off after the closing line |

### T5 in detail - Mimir mined by Mimir

Mimir is himself an ICM workspace, so his own miner is a real test rather than a
gesture. Run against this folder, with `eval/` and `checks/fixtures/` excluded by
`.mimirignore` (they hold other workspaces, not this one):

| Signal | Result |
|---|---|
| `form.guess` | `specialist` - correct |
| `totals.markdownFiles` | 17 |
| `entry.lines` | 42, against a limit of 60 - the catalog holds no books |
| `routingPayload` | empty |
| `graph.orphans` | empty |
| `naming.violations` | empty |
| `duplication` | empty - no fact has two homes |
| `placeholders.outsideTemplates` | **15** - acquitted, see `DEFECTS.md` D2 |
| `graph.backReferencesByFolder` | **3** - acquitted, see `DEFECTS.md` D3 |
| `graph.dangling` | none a broken internal link, see `BLIND-SPOTS.md` |
| longest doctrine file | `rules.md` at 406 lines - **open defect D1** |

Two of those are judgement calls and one is an open defect. All three are
written up rather than tuned away, which is the point of running the tool on
itself.

The self-mine is also where seven of the eleven closed defects in `DEFECTS.md`
came from. Before C1 to C7 it reported this folder as a pipeline with ten
numbered stages, its own doctrine files as routing files carrying payload, and
its own shell commands as broken links. None of that was found by reading.

---

## Applied runs - real workspaces, by the builder, not blind

**Status: 3 runs, 2026-08-17. These are not blind and must never be counted as blind.** They
were produced by the author, who wrote the doctrine and knew every answer key in the folder.
What they demonstrate is that the doctrine survives contact with a real workspace and that the
gates catch a real author. What they cannot demonstrate is diagnostic judgement, which needs the
blind table below.

| # | Subject | Result | Gate |
|---|---|---|---|
| A1 | `porter-intake-operator`, failure 1: drafts are generic rather than project-substantive | `OUT-OF-TAXONOMY` - a drafting step whose declared inputs never include the project state | PASS, 9 gates, 7 links, 10 quotes grounded |
| A2 | `porter-intake-operator`, failure 2: no draft where one is expected | family 11, no canonical source - the draft trigger has three homes that disagree, and the two conflict rules order them differently | PASS, 9 gates, 7 links, 5 quotes grounded |
| A3 | Mimir on Mimir, against the competition conditions | broken handoff (family 12) - the evidence layer is a program's output, so in a Claude Project no step can produce the declared input. **OVERTURNED by the owner the same day, on the finding's own third falsifier** - see `eval/receipts/applied/A3-OVERTURNED.md` | PASS, 9 gates, 8 links, 9 quotes grounded |

A3 is the most useful of the three and it is the one that was wrong. It named three observations
that would break it; the owner met the third within hours, by stating that the deployment surface
is Taurus and Claude Code, where the folder is dropped beside the broken workspace and both
scripts run. The finding is withdrawn and kept.

That is the first evidence in this folder that the `WHAT WOULD OVERTURN THIS` section is real
rather than decorative: a falsifier written by the author, met by someone else, and honoured.

**All three now fail the `PLAIN` gate** - eight violations in A1, three in A2, five in A3 - and
they are kept exactly as returned. That gate did not exist when they were written; it exists
because of them. See `DEFECTS.md` C14.

**What these runs cost, and it is the point of running them:** six defects, four of them in the
checker, and the two most important found by a reader rather than by a test.

- **C12 and C13** - two gates were silently blind to a quote that wrapped across a line. C12 meant
  a fabricated quote could pass GROUNDING by being long. Both fixed, with a regression fixture;
  the selftest is now 11.
- **D6** - `rules.md` step 3 produces "what was set aside" and the finding contract has no field
  for it. Surfaced immediately, because the first real workspace held two failures.
- **D7** - the remedy word lists are English only, so all three Dutch findings passed `NO-RX`
  vacuously. That pass is recorded as worth nothing.
- **D8** - the taxonomy has no family for contract sufficiency. A1 exercised the
  `OUT-OF-TAXONOMY` escape, which `BLIND-SPOTS.md` had listed as written and unproven.

A2 is the one to read if you only read one: it is the only in-taxonomy conviction of the three,
and its evidence chain is entirely quotes from the diagnosed folder.

## Behavioural results - the protocol, and why the table is empty

**Status: PENDING. Zero of five model-facing cases have been run.**

Writing a folder and scoring it in the same session is not a blind run, and a
receipt produced that way would be a lie that happens to be typed accurately.
The cases and their answer keys are shipped ready to run; the table below fills
in when somebody runs them.

### Method, frozen before any run

1. **Fresh session per case.** No memory of any other run, and no knowledge that
   it is being tested.
2. **Allowlist.** The session loads exactly the **Load** set above: `identity.md`,
   `rules.md`, `intake.md`, and every file in `reference/`. Not `examples.md`,
   not `README.md`, not anything under `eval/`. The run should report the file
   list it read, so the isolation can be audited afterwards.
3. **Input.** The fenced case text from `eval/cases/<case>/input.md`, pasted as
   the first message. The workspace sits at `workspace/` beside it.
4. **Save before scoring.** The raw answer goes to `eval/receipts/<case>.md`
   verbatim, before anyone compares it to anything.
5. **Score afterwards** against `eval/cases/<case>/expected.md`, which was
   committed before the run existed.
6. **The owner is played adversarially** where the case has follow-up turns: be
   vague, think in episodes rather than events, push back on being asked to
   narrow the scope, and ask for the fix at least once.
7. **No coaching, no retries, no revealing the expected cause inside a scored
   run.**
8. **Failures stay.** A run that breaks a rule is kept verbatim, the defect goes
   in `DEFECTS.md` naming the gate that catches it now, and a re-run is a new
   file rather than a replacement.

### The cases

| # | Case | Expected result | What it is really testing | Status |
|---|---|---|---|---|
| B1 | `eval/cases/01-outputs-as-templates` | family 9, one cause | can it show a compounding drift rather than matching a fingerprint, and acquit both the owner's model-got-worse theory and the vague-standards decoy | **PENDING** |
| B2 | `eval/cases/02-healthy-with-a-gate` | `NO-FAILURE` | can it decline to find something when the complaint is loud, repeated, accurate and describes the method working | **PENDING** |
| B3 | `eval/cases/03-thin-evidence` | `INSUFFICIENT-EVIDENCE` | can it hold the signal floor when every fingerprint for under-structure superficially fires | **PENDING** |
| B4 | `eval/refusal` turns 1-4 | one cause, zero fixes | four disguises in four turns, including a counterfactual handed over as a question | **PENDING** |
| B5 | Mimir diagnoses Mimir | a finding that passes `verify.py` | the folder is the patient and the patient wrote the doctrine | **PENDING** |
| B6 | Model floor: B1 re-run on a smaller model tier | same primary cause | does the method degrade in stated ways, or unstated ones | **PENDING** |
| B7 | Reproducibility: B1 run twice, fresh sessions | same cause, same evidence | is the conviction reproducible, is the confidence grade | **PENDING** |
| B8 | Cold stranger, human | a useful answer in under five minutes from `README.md` alone | any question they have to ask is a README defect | **PENDING** |

### How to run one

```bash
# fresh session, load only: identity.md rules.md intake.md reference/*.md
# paste eval/cases/01-outputs-as-templates/input.md
# save the answer verbatim to eval/receipts/B1.md, then:
python checks/mine.py eval/cases/01-outputs-as-templates/workspace -o /tmp/ev.json
python checks/verify.py eval/receipts/B1.md /tmp/ev.json
# then score against eval/cases/01-outputs-as-templates/expected.md
```

---

## What this testing is, and is not

The deterministic suite proves that the gates work and that the miner measures
what it says it measures. It proves nothing about diagnostic judgement.

The behavioural suite, once run, will support only those cases on the model and
date recorded. That is not universal diagnostic accuracy and this file will keep
saying so.

**All eval cases are synthetic.** The workspaces are invented, realistic, and
seeded with defects on purpose. No real person's folder is in here. A real case,
diagnosed live on somebody else's broken workspace with the outcome confirmed by
them afterwards, is the next bar and has not been cleared.

**Nobody who did not build this has used it.** That is the bar after that one.
