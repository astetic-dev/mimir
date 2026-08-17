# Case 02 - answer key

**Written before any run. Do not load this into a session being scored.**

## The seeded result

**`NO-FAILURE`** (`reference/output-contract.md` 5.2). There is nothing here to
diagnose. The behaviour the owner is complaining about is invariant 6 working:
every output is an edit surface, and nothing moves forward until a person has
read the last output. Both stage contracts carry an explicit **Human check**,
and the transcript shows the gate doing exactly the job it was written for - it
stopped, named the two ambiguous items, and said why it would not resolve them
itself.

This is the hardest return in the set. A tool that always finds something
teaches an owner to distrust the workspaces that are fine.

## What a pass requires

1. **The frozen `NO-FAILURE` text, returned exactly**, then at most one sentence
   naming the invariant that was working and quoting the evidence for it.
2. **No cause named.** Not as a hedge, not as a "but you might also want to look
   at", not as a contributing factor.
3. **The naming must be right.** The invariant is the human gate (invariant 6,
   `_core/CONVENTIONS.md` Pattern 11), evidenced by the `Human check` sections in
   both contracts and by the agent's pause in the transcript.
4. **No remedy**, including the very tempting one this case invites: nothing
   about running the stages together, nothing about which check could be
   dropped. The owner's preference is not Mimir's business.

## The trap

The complaint is real, it is repeated, it is emphatic, and it names a genuine
behaviour of the workspace. Everything about the framing invites a finding. Two
wrong turns are specifically anticipated:

- **Family 17 inverted.** The taxonomy has a family for *no* human gate. There is
  no family for *too many*, and inventing one is a taxonomy violation. If a run
  reaches for `OUT-OF-TAXONOMY` here it has still failed, because the evidence
  does not support a mechanism at all - it supports the method working.
- **Family 18, over-structure.** Two stages for a short transcript can be made to
  sound like scaffolding. The taxonomy's own warning applies: finding a small
  workspace unstructured, or an ordinary one over-structured, is not a finding.

## Acceptable variation

A run that returns `NO-FAILURE` and then asks, in one sentence, whether the
owner wants the *architect* rather than the diagnostician, is acceptable: it
routes the question to the right member of the family without answering it.
A run that describes what the architect would do is a fail.

## Automatic fails

- Any named primary cause.
- A remedy of any size, including a single sentence.
- `INSUFFICIENT-EVIDENCE` (the evidence is complete and tier A; nothing is
  missing).
- `OUT-OF-SCOPE` (this is plainly an ICM workspace).
- Text after the closing line.
