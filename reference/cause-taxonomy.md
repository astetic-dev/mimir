# Cause taxonomy

The bounded set of structural causes behind an ICM workspace that does not do what its owner
expects. A named primary cause must come from this list. There are twenty, numbered within seven
layers; the numbers are an index for auditing and never a label to hand a reader
(`reference/output-contract.md` 3b).

Distilled from the ICM canon: the ten invariants in `icm-architect/SKILL.md`, the fifteen
patterns and five-layer architecture in `_core/CONVENTIONS.md`, and the five principles in
`icm-architect/references/core.md`. Where a family maps to a named invariant or pattern, the
reference is given, because a finding that cites the canon is arguable and one that does not is
an opinion.

Each entry gives: **what it is**, its **fingerprint** in `evidence.json`, what it is
**mistaken for**, and **how to tell it from its neighbour**. That last line is where most wrong
convictions are prevented.

---

## How to use this file

1. **The families are walked in layer order** (`rules.md` step 5). Routing before contract,
   contract before factory/product, graph before gates, and the *content* of reference material
   last of all. That order is not alphabetical convenience. It is the order of how often each
   layer is the true cause.
2. **A fingerprint match makes a candidate, not a finding.** The step from candidate to cause
   needs the necessity test (`rules.md` step 6) and the ranking rule (step 7).
3. **Choose the most upstream family the evidence actually supports.** Do not reach for a broad
   family when the evidence only supports a narrow one, and do not name a visible defect when a
   supported family explains it.
4. **The escape is real.** If the evidence positively supports a mechanism none of these
   families describes, return `OUT-OF-TAXONOMY` (`reference/output-contract.md` 5.5). Do not
   force-fit. A confident wrong family is worse than an accurate abstention. The escape is not
   for thin evidence, which is `INSUFFICIENT-EVIDENCE`.

---

# Layer 1 - Routing (L0 / L1)

Can an agent orient at all? Everything downstream assumes it can.

## 1. Payload in the catalog

**What it is.** The entry file or a routing file carries the content itself instead of pointing
at it. Rules, definitions, voice guidance, worked examples sitting in `CLAUDE.md` or a
`CONTEXT.md`. The catalog is holding books.

The consequence is not that the content is unavailable. It is that it arrives *always*,
undifferentiated, in every conversation, and competes with the task. Invariant 2 caps the entry
file at about 60 lines for this reason. Pattern 6 says a `CONTEXT.md` answers three questions
and holds no reference material.

**Fingerprint.** `routingPayload[]` non-empty. `entry.lines` over 60. An L1 or L2 file over 80
lines. A routing file with a high `proseLines` to `headings` ratio, or with headings that name
content (`Voice rules`, `Examples`, `Definitions`) rather than routes.

**Mistaken for.** *"The model ignores my rules."* It does not ignore them. It received all of
them at once, at the moment it was least able to use them, with nothing marking which ones
applied to the step in hand.

**Not this family when.** The file is long but every line is a route (a large routing table for
a large workspace is not payload; it is a catalog doing its job). Check `routingPayload[]`
before convicting on `entry.lines` alone.

**Neighbour.** Family 7 (token blowout) is the same symptom one layer down: there the contract
is clean and the *declared inputs* are too heavy. If the weight is in the routing file, this is
family 1. If the routing file is small and the load is still large, it is family 7.

## 2. Twin entry files that drift

**What it is.** `CLAUDE.md` and `AGENTS.md` (or `routing.md`) both exist and are both maintained
by hand. They diverge. Which one an agent reads depends on which tool opened the folder, so the
workspace behaves differently for different people and nobody can reproduce it. Named as an
anti-pattern in `icm-architect/SKILL.md`; the fix pattern is that one is generated from the
other or is a one-line pointer.

**Fingerprint.** `entry.twins[]` has more than one file and `entry.twinsIdentical` is false.

**Mistaken for.** *"It works for me and not for him."* Correct observation, wrong subject: the
difference is not the person.

**Neighbour.** Family 11 (no canonical source) is the general case. Convict family 2 only when
the duplicated fact is the *entry file itself*, because that one determines everything else that
gets read.

## 3. Unrouted work

**What it is.** The entry file is small and clean and simply does not point at the folder where
the work happens. A stage exists, has a contract, and nothing routes to it. The agent orients
correctly into a building that does not contain the room it needs.

**Fingerprint.** A folder classified `L2` that appears in no `graph.edges` with an L0 or L1
source. `graph.orphans[]` containing a contract file.

**Mistaken for.** *"It always starts in the wrong place."*

**Neighbour.** Family 13 (ghost wiring) covers files nothing points at in general. This family
is specifically the case where the unpointed-at thing is *live work*, which makes it a routing
failure rather than a leftover.

---

# Layer 2 - Contract (L2, the control point)

`references/core.md` calls L2 "the control surface of the whole system". Its Inputs section is
what makes context selection explicit, editable and auditable instead of left to agent judgement.
Most workspaces that misbehave misbehave here.

## 4. No contract at the control point

**What it is.** A working folder with no `CONTEXT.md`, or a `CONTEXT.md` that is not the three-
section contract (Inputs / Process / Outputs, plus a human check). The agent decides for itself
what to load, so it loads differently every time. Invariant 4, Pattern 1.

**Fingerprint.** `stages[].contract` is null, or `stages[].contractSections` has any of
`inputs` / `process` / `outputs` false.

**Mistaken for.** *"The model is inconsistent."* It is consistent: consistently deciding, because
nothing decided for it.

**Not this family when.** The workspace is in specialist form (`form.guess: "specialist"`) rather
than pipeline form. A specialist folder carries its contract in `rules.md`, not in a per-stage
`CONTEXT.md`, and demanding stage contracts of it is a category error.

## 5. Contract without exact paths

**What it is.** The contract exists and its Inputs section names things instead of paths: "the
research", "the brand voice", "the previous output". The agent resolves the name by guessing,
which means it resolves it differently on different days. `references/core.md`: "inputs are
exact paths, split working vs reference".

**Fingerprint.** `stages[].declaredInputs[]` entries whose `path` did not parse to a filesystem
path, or whose `exists` is false because the text was a description rather than a location.

**Mistaken for.** *"It read the wrong file."* It read *a* file matching a description you wrote.

**Neighbour.** Family 12 (broken handoff) is when the path is exact and points at something no
stage produces. Here the path was never exact to begin with.

## 6. No section routing on a heavy reference

**What it is.** The contract says "read `voice-rules.md`" for a 400-line file where 60 lines
apply to this step. Pattern 4 exists to prevent exactly this: Inputs tables name the section, not
just the file. The other 340 lines are not merely wasted; they dilute the 60 that matter.

**Fingerprint.** `stages[].declaredInputs[]` with `scope: "Full file"` (or no scope) pointing at
a file whose `lines` exceeds 200.

**Mistaken for.** *"It drowns in context"*, or worse, *"the reference file needs to be shorter"*.
Shortening it loses the material. Routing to a section keeps it.

**Neighbour.** Family 7 (token blowout) is the measured consequence. Convict family 6 when the
mechanism is visible in the Inputs table; convict family 7 when the load is over band and no
single input explains it.

## 7. Token blowout at the control point

**What it is.** A stage's full context (entry + contract + references + inputs) lands far outside
the 2k to 8k band `references/core.md` names as healthy. The model is being asked to hold more
than the step needs, and performance degrades in the middle of the work rather than at the start.

**Fingerprint.** `stages[].loadEstimate.band` is `"over"`. Read `loadEstimate.inputs` against
`loadEstimate.contract` to see where the weight sits.

**Mistaken for.** *"It loses the thread halfway through."* The thread was never held; the context
was.

**Not this family when.** One oversized input explains the whole overage. That is family 6, one
step upstream, and naming family 7 there stops at the measurement instead of the reason.

## 20. The contract omits what the step needs

**What it is.** The contract exists, names exact paths, scopes its sections and opens in band -
and the material the step's own output requires is not on the list at all. The step reads the
factory and never the product, or reads the product and never the standard, and produces
something shaped correctly with nothing in it.

Families 4 to 7 all ask whether the declared inputs are *well declared*. This one asks whether
they are *the right ones*. A contract can be perfect by every other measure and still send an
agent to write a client report with no access to what the client's account did this month.

**Fingerprint.** No single field. Read `stages[].declaredInputs[]` against what the stage's
`Outputs` claims to produce and ask what a person would need to produce it. Two shapes recur and
both are visible in the mined tree: a step whose inputs are all classified `L3` where its output
requires per-run fact, and a step whose inputs are all `L4` where its output requires a standard.
Where the workspace has no stage contracts (`form.guess: "specialist"`), the same question is
asked of whatever file carries the step, and the miner cannot help - this is the one family that
is read rather than measured.

**Mistaken for.** *"The output is generic."* Also, and more expensively, mistaken for the tone or
the template being wrong: the shape is fine, the words are fine, and there was nothing to put in
them.

**Neighbour.** Family 5 is an input named as a category instead of a location, where the harm is
that the agent guesses and guesses differently each time. Here the agent does not guess: it
reaches a gap the contract left and fills it with whatever the doctrine's fallback says, which is
usually a placeholder or a generality. Convict family 5 when a named thing fails to resolve;
convict this one when nothing was named at all.

**Where it came from.** Added 2026-08-17, after the escape hatch fired twice on real workspaces
for the same missing family - once on a drafting step whose inputs named the templates and the
tone and never the project state, and once on a finding contract with no field for a decision its
own procedure produces. See `DEFECTS.md` D8.

---

# Layer 3 - Factory and product (L3 vs L4)

Principle 5: configure the factory once; the product is what each run emits. Where the two mix,
the workspace slowly teaches itself its own worst output.

## 8. Factory and product collapse

**What it is.** Stable reference material and per-run artifacts live in the same place with no
structural separation. There is no `output/` folder, or reference files sit inside it, or run
artifacts sit next to the rules. Invariant 5.

**Fingerprint.** No `L4` layer at all in a workspace whose `form.guess` is `"pipeline"`;
`stages[].outputFolder` null; files classified `L3` living under an `output/` path.

**Mistaken for.** *"The workspace is messy."* It is, and the mess has a specific consequence,
which is family 9.

## 9. Outputs used as templates

**What it is.** A contract points an agent at a previous run's output as a *pattern to follow*
rather than as input to transform. Pattern 14 forbids this in one line: "Early outputs are the
worst outputs. If future agents learn from them, quality never improves." Reference docs are the
authority on how to build; outputs are artifacts, not templates.

**Fingerprint.** `stages[].declaredInputs[]` with a path under another stage's `output/` and a
`scope` or `why` naming style, tone, format, structure or example rather than content.

**Mistaken for.** *"Quality is slowly getting worse"*, and then *"the model got worse"*. The
model did not change. The workspace acquired a feedback loop pointing the wrong way.

**Neighbour.** Family 8 is the missing wall. This is the traffic that crosses where the wall
should be. Where both are present, family 8 is upstream and usually the cause; family 9 is how it
became visible.

## 10. Placeholders never resolved

**What it is.** The workspace shipped with `{{PLACEHOLDER}}` variables and setup was never run,
or was run and did not finish. `_core/placeholder-syntax.md` is explicit: onboarding is complete
only when zero placeholders remain. Until then the agent meets a literal string where a fact
should be, and fills the gap itself.

**Fingerprint.** `placeholders.outsideTemplates` greater than zero. Check `placeholders.sample[]`
for where.

**Mistaken for.** *"It invented a brand voice."* It did, because the file told it the brand voice
was `{{VOICE_DESCRIPTION}}`.

**Not this family when.** The remaining placeholders are all inside `_templates/`,
`assets/templates/` or `setup/questionnaire.md`. Those are supposed to have them.

---

# Layer 4 - The graph

One home per fact, one direction of reference, nothing pointing at nothing. Duplication is how
structures rot.

## 11. No canonical source

**What it is.** The same fact lives in two files and both are meant to be authoritative. Someone
updates one. The workspace now contains two answers and the agent picks by proximity. Pattern 5;
`references/core.md`: "one home per fact; a link beats a copy".

**Fingerprint.** `duplication[]` entries with `lines` above the threshold and two or more
`files`, where neither file is a template.

**Mistaken for.** *"It contradicts itself."* Both statements are in the folder. It is quoting.

**Neighbour.** Family 2 is this family applied to the entry file specifically. Family 15 is this
family applied to a schema and the tree it describes.

## 12. Broken handoff

**What it is.** A stage's declared input is an exact path that no stage's declared output
produces, or that does not exist. The chain is broken at a named joint. Pattern 2 is the whole
handoff convention: stage N writes to its `output/`, stage N+1 reads from there.

**Fingerprint.** `stages[].declaredInputs[]` with `exists: false`, or a path under an `output/`
folder that appears in no `stages[].declaredOutputs[]`, or an entry in `graph.brokenLinks[]`.

**Mistaken for.** *"The agent hallucinated a file."* It was told the file would be there.

**Read `graph.brokenLinks[]`, never `graph.dangling[]`.** The miner splits every unresolved
pointer into `kind: "broken"` (it aims at this tree: a contract declares it, or it is written
relative, or its first segment exists here) and `kind: "external"` (its first segment names
nothing in this tree, so it is almost always a citation of another document). A folder that cites
the ICM canon carries dozens of the second kind and none of them is a defect. Each entry also
carries the source line in `context`, so the two-second check is available. A finding that
convicts on `dangling` as a raw count has not looked.

## 13. Ghost wiring

**What it is.** Files nothing points at, and pointers at files that do not exist. A reference
file that no contract loads is not neutral: the next person builds on it, and the next agent
finds it by search and treats it as live. Cassini's version of this: "the name that looked wired
- defined, exported, registered, called by nothing".

**Fingerprint.** `graph.orphans[]` non-empty, or `graph.brokenLinks[]` non-empty. Same warning as
family 12: `graph.dangling[]` mixes broken links with citations of other documents, and only the
`kind: "broken"` half is evidence of anything.

**Mistaken for.** *"It reads the wrong things."*

**Neighbour.** Family 12 is the case where the broken pointer sits in a contract's Inputs, which
makes it a live break in the chain rather than a leftover. Convict family 12 there.

## 14. Back-references

**What it is.** Folder A points at B and B points back at A. Pattern 3 forbids it: every folder
points outward to what it needs, no folder points back. Without it, reference growth goes
N-squared and no subtree can be loaded without pulling the rest.

**Fingerprint.** `graph.backReferences[]` non-empty.

**Mistaken for.** *"The context is too big."* It is, and this is the reason it cannot be made
smaller by trimming files.

## 15. Schema and tree drift

**What it is.** A schema or naming convention document mandates names the actual files stopped
using. Named as an anti-pattern in `icm-architect/SKILL.md`: "update the schema or the files,
pick one". `references/core.md` calls drift between schema and files "the most common decay".

**Fingerprint.** `schemaDrift.missingInTree[]` non-empty; `naming.violations[]` clustered on one
rule rather than scattered.

**Mistaken for.** *"The map is wrong."*

## 16. Hand-edited generated index

**What it is.** An index, file map or status list that a script should rebuild has been edited by
hand and no longer matches the tree. Invariant 9: "generated indexes are rebuilt by script, never
hand-edited." A hand-curated index always drifts; the drift is invisible because the index reads
as authoritative.

**Fingerprint.** `index.listedNotPresent[]` or `index.presentNotListed[]` non-empty.

**Mistaken for.** *"The map rotted."* Cassini's phrase for it: "true when written, wrong four
months later, and nothing in it said so."

---

# Layer 5 - Gates

## 17. No human gate

**What it is.** Nothing in the workspace stops for a person. Invariant 6: every output is an edit
surface, and nothing moves forward until a person has read the last output. Pattern 11 adds
checkpoints for creative stages. Without a gate, the run bulldozes from input to deliverable and
the human sees only the end, at which point steering costs a rerun.

**Fingerprint.** `gates.contractsWithHumanCheck` is zero, or far below `gates.contractsTotal`, in
a workspace with more than two stages.

**Mistaken for.** *"The model does not listen."* It was never given a moment in which listening
was the step.

**Not this family when.** The workspace is a single linear conversion (extract, render, convert).
`_core/CONVENTIONS.md` Pattern 11 says plainly that not every stage needs a checkpoint.

---

# Layer 6 - Shape

Reach for these only when the layers above are clean. A shape verdict on a workspace with a
broken contract is a diagnosis of the wrong thing.

## 18. Over-structure

**What it is.** Folders for stages that do not exist yet, speculative depth, empty buckets. The
guardrail in `icm-architect/SKILL.md`: "Three real stages beat seven imagined ones. If the whole
job fits in one saved prompt, say so and do not build a workspace at all."

**Fingerprint.** A majority of `stages[].outputFolder.onlyGitkeep` true; empty folders in the
tree; `stages[]` count high against `totals.markdownFiles`.

**Mistaken for.** *"It is too complicated to use."* That is the symptom, and it is accurate. The
cause is that the structure was designed for work that has not happened.

## 19. Under-structure

**What it is.** One file carrying the whole job. No stages, no contracts, no separation. The
ladder in the canon runs chat, then saved prompt or skill, then folders plus one agent. This
workspace is on a rung it has not climbed.

**Fingerprint.** `form.guess: "flat"`; `stages[]` empty; a single markdown file holding most of
`totals.estTokens`.

**Mistaken for.** *"I need a better prompt."*

**Careful here.** Under-structure is a real cause and it is also the easiest thing in this file to
say about a small workspace that is working fine. The same guardrail cuts both ways: a workspace
for a thing done twice is scaffolding, not architecture, and finding it unstructured is not a
finding. Convict this family only where the evidence shows the work *is* repeating and the single
file is where the failure happens.

---

# Layer 7 - The content of the reference material

**Walked last, on purpose.**

This is the most-accused and least-often-guilty layer in an ICM workspace, exactly as content is
in a deliverability investigation. *"The rules are not clear enough"* is the first theory almost
every owner arrives with, and it is almost never the cause. In the overwhelming majority of cases
the rules are clear and were never loaded, or were loaded along with forty other things at a
moment when nothing marked them as relevant.

**Only convict at this layer when layers 1 to 6 are demonstrably clean:** the routing is small,
the contract names exact paths and sections, the load is in band, the reference file was
provably loaded at the failing step, and it still produced the wrong behaviour.

**Fingerprint.** A transcript (tier A or C) showing the file was read at the failing step, plus
an internal contradiction or a genuine gap in that file. Without a transcript this layer cannot
be reached, because you cannot show the material was in front of the agent.

**And even then:** a reference file that contradicts itself is usually family 11 (the same fact
with two homes) wearing a different coat. Check that first.

---

## The signal floor

A structural cause needs enough structure to have a cause. **Decline to name one**, and say
plainly that the signal is insufficient, when:

- `totals.markdownFiles` is under 3 and there is no transcript; or
- `form.guess` is `"unknown"` and no transcript shows what the agent loaded; or
- no family's fingerprint fires and no transcript is available to reach layer 7.

Declining correctly is a pass, not a failure. Over-diagnosing a small clean workspace is the
error this file exists to prevent.
