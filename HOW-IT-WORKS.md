# How Mimir works

The whole machine in one file, for someone who is going to use it, extend it, or decide whether
to trust it. It is documentation, not doctrine: Mimir does not load it during a run.

If you read one section, read section 4. That is the core of the product and the source of every
piece of vocabulary the rest of the folder uses.

---

## 1. What it is

Mimir is a folder you drop next to a workspace that is misbehaving. You say what went wrong. He
reads that workspace, finds **one** structural cause, shows what the claim rests on, and stops.
He repairs nothing, ranks nothing, scores nothing and maps nothing. The patient is always the
**structure of the folder**, never the model running inside it.

He is for someone whose agent folder has started letting them down: it ignores rules that are
demonstrably written down, does the wrong step, answers differently every time, or has quietly
got worse over months.

**Scope note that is easy to miss.** Every agent and every project in the left rail of Taurus is
an ICM workspace, whether or not anyone built it as one. The folders that misbehave are usually
the ones nobody scaffolded.

## 2. Where it sits

Seven roles work on an ICM workspace, and confusing them is the fastest way to get a confident
answer to a question you did not ask. **The table lives in `identity.md`** - it is doctrine, not
documentation, because Mimir has to know his neighbours in order to decline their questions by
name. It is not repeated here.

What matters for understanding the machine is the one property that separates him from the other
six: Mimir works **backward from something that already broke**. The others can run on a healthy
workspace. He cannot, and saying so is a valid answer rather than a failure.

Three neighbours sit close enough that their questions arrive at his door - what the workspace
should become, whether it is good enough, and what it is. He declines all three by name.

## 3. How a run goes

You drop the folder in and say what went wrong. There is always a stated problem - without one
there is nothing to diagnose.

| # | Step | What happens |
|---|---|---|
| 0 | **Hard stops** | Is this an ICM workspace? Did something actually go wrong? Is the complaint about the structure or about the model? Any of the three: say so and stop. Re-runs on every message. |
| 1 | **Intake** | The owner has a complaint, not evidence. Two things are asked for, one instruction at a time: the folder, and one session where it went wrong. |
| 2 | **Mine, maybe reproduce, then grade** | `mine.py` walks the folder and writes `evidence.json`. Where it is safe, the failing step is re-run in a sandbox so behaviour is observed rather than inferred. The evidence tier is stated. |
| 3 | **Scope one failure** | People think in episodes, not events. Two complaints are two investigations. Ask twice at most, then choose and say which. |
| 4 | **Establish what failed** | What the workspace stopped doing, the failure mode, the effects - plus the check that asks whether this is the method working correctly. |
| 5 | **Branch and prune** | Walk the cause families in layer order. Everything killed stays, with the evidence that killed it. |
| 6 | **Descend by necessity** | Remove a step: does the failure still happen? If yes, that step was not necessary and you went too deep. Stop at the last necessary one and name both its neighbours. |
| 7 | **Rank** | Which cause survives the obvious repair? That one is primary. If the evidence cannot separate two, abstain rather than guess. |
| 8 | **Verify and write** | Attack your own finding, check the markers, write it, run the checker. |

**A gate asks; a gate never blocks.** Every step ends with a question to the owner, and Mimir
does not wait for the answer. He states the assumption he is proceeding on and delivers in the
same turn. A turn containing only questions has delivered nothing. If an answer later breaks a
link, the step where that link was formed reopens - the conclusion is not kept while the
reasoning underneath it is swapped.

### Evidence tiers

| Tier | What you gave | What it carries |
|---|---|---|
| **R** | a sandboxed re-run of the failing step | behaviour observed, not reported |
| **A** | the folder **and** a session where it went wrong | what was available, and what the agent did |
| **B** | the folder only | structural claims hard, behavioural claims inferred |
| **C** | a session only | what happened, not what was available |
| **D** | your account of the behaviour | a symptom |
| **E** | a verdict with no account | never diagnose on this alone |

**The sharpest distinction in the product:** a tree shows what was *available*, never what was
*read*. Anything crossing that line without a session or a reproduction is inferred and must say
so.

## 4. The cause families

**What they are.** A bounded list of twenty structural ways an ICM workspace can fail. Not an
open category: a named cause comes from the list, or Mimir says explicitly that his list falls
short.

**Why bounded.** A diagnostician with no fixed list always finds something, and that something is
a phrasing rather than a finding. With a fixed list you can see what was struck off and why, and
you can disagree with a specific point.

**Where the content comes from.** Not from opinion. Every family is derived from the ICM canon:
the ten invariants in `icm-architect/SKILL.md`, the fifteen patterns and the five-layer
architecture in `_core/CONVENTIONS.md`, and the five design principles in `references/core.md`.
Mimir has no view of his own about what a good workspace is - he only knows what the method says
one is.

**What a family looks like.** Four parts: what it is, the **fingerprint** (what shows in
`evidence.json` when it is live), what it is usually **mistaken for**, and how to tell it from its
**neighbour**. That last part prevents most wrong convictions.

**A fingerprint that fires is a candidate, not a finding.** Candidate to cause runs through the
removal test at step 6 and the ranking at step 7.

### The layers, in fixed order

1. **Routing** - can an agent orient at all?
2. **Contract** - does the place that says what a step reads exist, name exact paths, and name the right ones?
3. **Factory vs product** - is stable material separated from what each run produces?
4. **The graph** - links, one home per fact, one-way references, orphans
5. **Gates** - does anything stop for a person?
6. **Shape** - too much structure, or too little
7. **The content of the reference material** - **last, deliberately**

That last one is the most important design decision in the folder. *"The rules are not clear
enough"* is the theory almost every owner arrives with, and it is almost never the cause. Usually
the rules were fine and were never loaded.

### The twenty, in plain terms

**Routing**

| # | What goes wrong | Usually called |
|---|---|---|
| 1 | The entry file carries the content instead of pointing at it, so every rule arrives at once, unsorted | "it ignores my rules" |
| 2 | `CLAUDE.md` and `AGENTS.md` both exist, both hand-maintained, and have drifted apart | "it works for me and not for him" |
| 3 | There is live work in the folder that nothing points at | "it always starts in the wrong place" |

**Contract**

| # | What goes wrong | Usually called |
|---|---|---|
| 4 | A working folder has no contract, or one missing Inputs / Process / Outputs, so the agent decides for itself what to load | "it is inconsistent" |
| 5 | The contract names things instead of paths - "the research", "the brand voice" - and the agent resolves them differently each day | "it read the wrong file" |
| 6 | The contract sends the agent to a whole 400-line file where 60 lines apply | "it drowns in context" |
| 7 | One step's total context lands far outside the healthy 2k-8k band | "it loses the thread halfway" |
| 20 | The contract is well formed and simply does not name the material the step needs | "the output is generic" |

**Factory versus product**

| # | What goes wrong | Usually called |
|---|---|---|
| 8 | Stable reference material and per-run artifacts share a home with no wall between them | "the folder is messy" |
| 9 | A step is pointed at an earlier output as *a pattern to copy*, so each run learns from the worst work the folder has produced | "quality is slowly getting worse" |
| 10 | The folder shipped with `{{PLACEHOLDERS}}` and setup never finished | "it invented a brand voice" |

**The graph**

| # | What goes wrong | Usually called |
|---|---|---|
| 11 | The same fact lives in two authoritative files that have drifted apart | "it contradicts itself" |
| 12 | A step names an input that no other step produces; the chain breaks at a named joint | "the agent hallucinated a file" |
| 13 | Files nothing points at, and pointers to files that do not exist | "it reads the wrong things" |
| 14 | Folder A points at B and B points back at A, so no part can be loaded alone | "the context is too big" |
| 15 | A schema or naming convention mandates names the files stopped using | "the map is wrong" |
| 16 | An index a script should rebuild has been hand-edited and fallen behind | "the map rotted" |

**Gates, and shape**

| # | What goes wrong | Usually called |
|---|---|---|
| 17 | Nothing in the folder stops for a person; the run goes from input to deliverable unattended | "it does not listen" |
| 18 | Folders for steps that do not exist yet, empty buckets, imagined depth | "it is too complicated to use" |
| 19 | One file carries the whole job; no steps, no contracts | "I need a better prompt" |

**Content.** Only convictable when every layer above is demonstrably clean **and** a session shows
the file was actually read at the failing step. Without a session this layer is unreachable.

### When the list falls short

If the evidence supports a mechanism none of the twenty describes, Mimir says so, names the
nearest families and why each fails, and convicts nothing. That is a valid answer, and it has
fired twice on real workspaces - both times finding the same gap, which became family 20.

### How families appear in an answer

**Never as a bare number.** The cause is stated in the reader's own words and the index rides in
brackets afterwards. The `PLAIN` gate rejects a bare "family 8".

## 5. The two scripts

**The script computes, the model names.** Mimir never counts.

**`checks/mine.py`** walks the folder and writes `evidence.json`: layer classification and line
counts per file, the stage inventory with contract shape and output occupancy, the link graph
with broken links separated from citations of other documents, orphans, back-references,
placeholder counts, duplication clusters, estimated context load per step against the 2k-8k band,
naming conformance, routing-payload detection and schema drift. **Every number a finding may cite
comes from here.**

A workspace may carry a `.mimirignore`, one path prefix per line, for subtrees that are really
other workspaces. Fields listed under `heuristics` are pattern-matching judgements, not
measurements. `estTokens` is characters over four: good enough to tell 2k from 30k and useless at
a band edge.

**`checks/verify.py`** gates the **finding**, not the folder. Ten gates: all nine sections present
once and in order; one cause and no list; every chain link carrying `[seen]`, `[inferred]` or
`[general]`; every `[seen]` quote literally present in the evidence; every path and multi-digit
number traceable, quoted or not; no remedy language and no counterfactual, checked in the
finding's own language; no bare family numbers; abstention that names its tied candidates;
nothing after the closing line; and a falsifier section that is non-empty and prescribes nothing.

Both carry `--selftest`. The miner builds a known-broken and a known-healthy tree and proves the
fingerprints fire on one and stay quiet on the other. The checker runs one good finding and
twelve bad ones, each of which must fail on its own named gate.

## 6. The five frozen returns

Fixed texts, so they are mechanically checkable and an improvised paraphrase fails.

| Return | When |
|---|---|
| `OUT-OF-SCOPE` | this is not an ICM workspace |
| `NO-FAILURE` | the folder is fine; what you are describing is the method working |
| `INSUFFICIENT-EVIDENCE` | the whole list was swept and nothing closes on this evidence |
| `UNRESOLVED` | two causes explain it equally well and the evidence cannot separate them |
| `OUT-OF-TAXONOMY` | the mechanism is clear and the list does not describe it |

`NO-FAILURE` is the hardest and the most important. *"It keeps stopping and asking me things"* is
the human gate working. *"It only reads three files"* is layered loading working. A tool that
always finds something teaches an owner to distrust the folders that are fine.

## 7. What is in the folder

| Set | Files | Rule |
|---|---|---|
| **Load** | `identity.md`, `rules.md`, `intake.md`, `reference/` | the doctrine; this is what a run receives |
| **Read** | `README.md`, `examples.md`, `BUILD.md`, `CLAUDE.md`, this file | for people; never loaded in a scored run |
| **Verify** | `checks/`, `eval/`, `TESTING.md`, `DEFECTS.md`, `BLIND-SPOTS.md` | evidence *about* Mimir; never loaded |

`BUILD.md` describes the reusable part: the nine steps, the ten gates and the five frozen returns
are domain-independent. Only the cause families and the miner are ICM-specific.

## 8. Where it comes from

Mimir is a combination before it is an invention. Five diagnosticians were read end to end, and
the reason combining them was worth doing is that **each one's gap is filled by another's
strength**. Full attribution per mechanism is in `CREDITS.md`.

Five gates exist in none of the five sources: the marker check, grounding extended past the quote
marks, the counterfactual arm, abstention consistency, and the no-appendix rule. `PLAIN` was
added later, from use.

## 9. State (2026-08-17)

**Proven, deterministic:** miner selftest, checker selftest, doctrine-cannot-see-the-answer-keys
check, the shipped worked finding through all gates, and Mimir through his own miner.

**Behavioural:** seven blind runs in fresh contexts. Six passed. One on a smaller model tier found
the right cause and failed the run, which located the floor precisely: *the smaller tier
recognises, and does not rule out.* Two runs found defects in the fixtures they were given. They
cost six defects, four of them in the gate.

**Not proven, and it is the last gap of its kind:** nobody who did not build this has used it.
Those seven runs were fresh contexts, not independent readers.

**Open defects** are in `DEFECTS.md`. The sharpest is D10: the falsifier section still launders a
remedy phrased as an experiment.
