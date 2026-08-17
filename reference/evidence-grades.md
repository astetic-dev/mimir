# Evidence grades

What each source can carry in a finding, what it cannot prove no matter how it reads, and the
traps in each. Most weak diagnoses fail here rather than in the reasoning: they take a record as
proof of a state of the world when it is only proof that somebody wrote something down.

---

## The tiers

Diagnose from the strongest tier available, and **say in the finding which tier you are working
from** (`EVIDENCE TIER` is a required section).

| Tier | Evidence | Weight |
|---|---|---|
| **A** | The workspace tree **and** a transcript of one run where it went wrong | What was there to load, and what the agent actually loaded and did. The only tier that can reach layer 7. |
| **B** | The workspace tree, mined into `evidence.json` | Structural claims are provable. Behavioural claims are inferred from structure and must be marked `[inferred]`. |
| **C** | A transcript alone | Shows what happened. Does not show what was available to load, so it cannot separate "the file was bad" from "the file was never read". |
| **D** | The owner's account of the behaviour | "It keeps forgetting the voice rules." A presenting symptom, and a good one. Not a diagnosis. |
| **E** | A verdict with no account | "It does not really work." Never diagnose from tier E alone. |

**If you are on tier D or E, try to move up before you reason.** `intake.md` walks the owner to a
tier A artifact in a handful of steps, and in this domain that is cheap: the tree is already on
disk and the transcript is already in their session history.

**If tier A is genuinely unavailable** and the tree is present, you are on tier B. Diagnose the
structural families and say plainly which conclusions would need a transcript. Do not substitute
a branch you *can* close for the one you cannot.

---

## The workspace tree

**Proves** what exists, what points at what, how large each file is, which contracts have which
sections. Everything in `evidence.json` is a fact about the tree at the moment it was mined.

**Does not prove** what the agent read. A file being present, well written and correctly routed
does not establish that it was loaded at the failing step. It establishes that it *could* have
been. That gap is the single most common place a structural diagnosis overreaches.

**Traps.**

- *A tree is a snapshot.* If the owner edited the workspace after the failing run, the tree you
  mined is not the tree that failed. Ask when the run happened and when the folder last changed.
  `mine.py` records `mtime` per file for exactly this.
- *A clean tree is not an innocent tree.* Absence of a fingerprint means no family fired, not
  that the workspace is healthy. Say which, honestly.
- *Not every ICM workspace looks like a pipeline.* An agent or project in the left rail of Taurus
  is an ICM workspace whether or not anybody scaffolded it as one. `form.guess` may be
  `specialist`, `record-library` or `flat`, and several families do not apply outside pipeline
  form. Check `form.guess` before convicting family 4 or 8.

## `evidence.json` (the mined tree)

**Proves** every number a finding is permitted to cite. `mine.py` computed it deterministically
and offline.

**Does not prove** anything about intent, quality or behaviour. A duplication cluster proves two
files share text. Whether both are meant to be authoritative is a question, and the answer is
frequently the difference between family 11 and a deliberate quote.

**Traps.**

- *A heuristic is not a measurement.* `routingPayload[]`, `duplication[]` and `form.guess` are
  heuristics, and `mine.py` labels them as such in the file. Cite the underlying counts, not the
  heuristic verdict, when the heuristic is what a link rests on.
- *Token estimates are estimates.* `estTokens` is characters divided by four. It is good enough
  to tell 2k from 30k and useless for telling 7k from 8k. Never build a finding on a band edge.
- *Mining a workspace that is mid-edit* produces dangling references that are just unfinished
  work. Check `mtime` clustering before convicting family 13.

## The transcript of a failing run

**Proves** what the agent was given, what it said it read, what it produced, and where the run
went off. In this domain the transcript is the closest thing to a witness, and it is the only
evidence that can reach layer 7.

**Does not prove** what the agent actually loaded. A model saying "I have read the voice rules"
is a claim inside the artifact, not an observation of the runtime. Where the transcript shows a
tool call reading a path, that is `[seen]`. Where it shows only the model's own narration, that
is at best `[inferred]`, and the finding must say so.

**Traps.**

- *A declaration is not an event.* This is the exact trap the Visual Momentum diagnostician names
  about storyboard metadata: a declared action proves only that the declaration exists. In a
  transcript, `"Loading the design system"` is a sentence, not a read.
- *The run may have been steered.* If the owner corrected the agent mid-run, everything after the
  correction is evidence about a different run. Find the first divergence and scope to it.
- *An excerpt is chosen by the person who already has a theory.* Ask for the whole run from the
  first message. If only an excerpt is available, mark the gap.

## The owner's account

**Proves** that something happened that was worth complaining about, and it is usually the most
precisely dated thing available: people remember when a thing started annoying them.

**Does not prove** the mechanism, and rarely names it correctly. The account is a presenting
symptom. `reference/cause-vs-symptom.md` exists because the owner's own words are almost always
one layer downstream of the cause.

**Traps.**

- *The account arrives with a theory attached, and the theory is usually the content layer.*
  "The rules are not clear enough" is the single most common opening, and layer 7 is the single
  least common cause. Take the observation, leave the theory.
- *"Nothing changed"* is consistent with a failure whose onset is elsewhere, not evidence against
  a cause. Ask what changed *around* the machine: a new model, a new tool, a colleague editing
  the folder, a file added.
- *Do not stop at the owner.* "He did not follow the process" is never a finished diagnosis. Ask
  what the contract allowed. See `rules.md` prohibitions.

## Git history of the workspace, where it exists

**Proves** when files changed and in what order. Useful for one question above all: did the
failure onset track a change to the folder?

**Does not prove** who intended what, and is absent in most Taurus workspaces, which are not
repositories. Treat it as a bonus, never as a requirement.

---

## Two general rules

**Absence of a record is evidence, and it points at the workspace, not at the model.** No
contract in a stage. No human check in any contract. No output folder. Each of these is a fact
about how the workspace is built, and each is directly citable.

**Negative findings belong in the finding.** Routing is small and clean. No dangling references.
Every declared input exists. Reporting these is what stops a diagnosis reading as the first idea
that occurred to you, and it is what `RULED OUT` is for.
