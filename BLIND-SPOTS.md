# Blind spots

What Mimir structurally cannot see. These are not bugs and better prompting does
not close them. They are properties of what he is given and how he is built, and
a diagnostician who will not diagnose himself is not worth trusting.

Defects found in testing live in `DEFECTS.md`. This file is written from the
design, not from the runs.

---

## He trusts the folder he is handed

The tree is a snapshot. If the owner edited the workspace after the run that
failed, the folder Mimir mines is not the folder that failed, and a confident
wrong finding follows with nothing to mark it. `rules.md` step 2 asks the
question outright and `mine.py` records `mtime` per file, but an owner who
answers "no, nothing changed" and is wrong will get a diagnosis of a workspace
that no longer exists.

The same applies to a transcript. An excerpt is chosen by somebody who already
has a theory, and a run that was steered mid-way is evidence about two different
runs. Mimir asks for the whole thing. He cannot make it arrive.

## The tree shows what was available, never what was read

This is the sharpest limit in the whole folder, and it is why the evidence tiers
exist. Structural claims are provable from `evidence.json`. **Behavioural claims
are not.** That a rule was in a file that a contract routed to does not
establish that the rule reached the model at the moment it applied.

Every finding that crosses from structure to behaviour without a transcript is
`[inferred]`, and must say so. Where it says `[seen]`, `verify.py` can check the
claim is in the evidence, and cannot check that the inference was fair.

A transcript narrows the gap without closing it: a model writing *"I have read
the design system"* is a sentence, not a read. Only a recorded tool call is an
observation.

## He cannot look anything up

No running of the workspace, no reproducing the failure, no querying the model
that produced it, no checking whether a different model tier behaves
differently. Every external fact arrives through the owner's hands. A diagnosis
is only as current as what was pasted.

He also cannot see the runtime: which files a harness auto-loaded, what a system
prompt added, whether a context limit was hit mid-run, whether a tool was
unavailable. `rules.md` step 0 exists because some of those produce behaviour
that looks exactly like a structural failure and is not one.

## The miner cannot tell a citation from a broken link

`mine.py` resolves every path it finds against the tree. It has no way to know
that `_core/CONVENTIONS.md` in `reference/cause-taxonomy.md` is a citation of
another repository rather than a missing file in this one.

This is visible in Mimir's own self-mine: **40 dangling rows, every one of them a
citation of the ICM canon or a generic example filename.** The mitigation is that
each dangling row carries the source line in a `context` field, so a reader sees
in three seconds which kind it is. That is a mitigation, not a fix, and it means
`graph.dangling` is the one field in `evidence.json` that must be read rather
than counted. A finding that convicts family 12 or 13 on a raw count has not
read it.

## The reference layer ages

`reference/cause-taxonomy.md` is distilled from the ICM canon as it stands. The
conventions will drift: patterns get added, guardrails get renumbered, the
line-count thresholds may move. A finding that leans on a stale threshold is a
real failure mode of this folder itself.

The mitigation is ordering: the mined tree always outranks the reference layer,
and where a threshold is cited it is cited as a threshold from a named document
rather than as a fact about the world.

## The taxonomy is bounded, and bounded is not complete

Nineteen families cover what the canon describes and what shows up in practice.
They do not cover everything, and Mimir's escape hatch - `OUT-OF-TAXONOMY` - has
been written and never exercised. Constructing a case that is decisively outside
the ontology and still inside the domain has not been attempted here. The escape
exists; it is unproven.

## The counterfactual gate only reads written findings

`checks/verify.py` catches "if the rules had lived in a reference file" inside a
finding. It cannot read the conversation around the finding, where the same
sentence is far more likely to appear, because that is where an owner asks the
question directly and it feels rude not to answer.

That gap is tested by a human in `eval/refusal` turn 3 and by nothing else. It
is the single largest hole in the enforcement story, and it is a hole shared
with every checker in this class: a gate on the artifact is not a gate on the
session.

## Per-workspace factors he will never see

Some workspaces fail for reasons no file in them will ever show: a colleague who
edits the folder without saying so, an owner whose expectations were never
written down anywhere, a job that changed shape while the pipeline did not, a
model that behaves differently on Tuesdays for reasons nobody has published.

That is why the taxonomy has a signal floor and why `NO-FAILURE` and
`INSUFFICIENT-EVIDENCE` are first-class returns rather than admissions of
defeat.
