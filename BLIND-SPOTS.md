# Blind spots

What Mimir structurally cannot see. These are properties of what he is given and how he is built,
and better prompting does not close them.

Defects found in testing live in `DEFECTS.md`. This file is written from the design.

**Revised 2026-08-17.** Two entries in the first version of this file were not blind spots at
all. They were inherited from a diagnostician working in a domain where the tool genuinely could
not look anything up or reach the runtime, and they were copied here without being tested against
what Mimir actually runs inside. Both are now corrected below rather than deleted, because a
folder that quietly drops an overclaimed limitation is doing the same thing as one that quietly
drops a defect.

---

## What was wrong in the first version

**"It cannot look anything up."** False as written. Mimir runs in Claude Code or Taurus, with a
shell and a filesystem. He reads the whole tree, runs his own miner over it, can read a git
history where one exists, and can run the workspace's own scripts. The real limit is much
narrower and is stated below.

**"Receiver reasoning is inferred, never observed."** No longer true by construction. `rules.md`
step 2 now carries a reproduction path: copy the workspace to a sandbox, run the failing step,
record what it loaded. That turns a behavioural claim from an inference into an observation, and
`reference/evidence-grades.md` grades it as tier R.

What that costs is a new set of limits, which are real and are the first two entries below.

---

## Reproduction is often unavailable, and the reason is not technical

`reference/evidence-grades.md` forbids reproducing any step that sends mail, writes to a ticket
system, calls a customer API, moves files outside the workspace, or commits anything. That
exclusion removes a large share of the workspaces most worth diagnosing: an intake operator, a
deployment runbook, anything wired to Outlook or Jira or a customer environment.

For those, Mimir is back to the tree and a transcript, and the gap between what was available and
what was read reopens in full. **The tool is strongest exactly where the stakes are lowest.**

## A reproduction is evidence about today

A reproduction runs under today's model, today's harness, and the folder as it stands now. A step
that behaves correctly in the sandbox does not establish that it behaved correctly in the failing
run, only that the mechanism is not live at this moment. A sandbox run that *fails the same way*
is strong; one that succeeds is weak, and the finding has to say which it got.

## He trusts the folder he is handed

The tree is a snapshot. If the owner edited the workspace after the run that failed, the folder
Mimir mines is not the folder that failed. `rules.md` step 2 asks outright and `mine.py` records
`mtime` per file, but an owner who answers "nothing changed" and is wrong gets a confident
diagnosis of a workspace that no longer exists.

This one bit in testing. Both B1 and B7 noticed that the whole eval fixture carried timestamps
inside one narrow window, meaning the archive it was reasoning over had no real history, and both
named it as their weakest link. That is the mechanism working - and it worked because the miner
records the timestamps, not because the doctrine is clever.

## He cannot see what the harness did

The one thing no amount of shell access reaches: what a runtime injected before the agent acted.
Claude Code auto-loads every `CLAUDE.md` on the path into context. A workspace can therefore
behave differently from what its own files predict, for reasons no file in it records.

This is not hypothetical. It leaked into Mimir's own blind-run suite and the runs caught it -
`eval/receipts/PROTOCOL-LEAK.md`. A folder that carries a `CLAUDE.md` cannot be blind-tested from
inside itself, and by the same token a diagnosis of it cannot fully account for what the harness
contributed.

## The taxonomy is bounded, and bounded is not complete

Twenty families cover what the canon describes and what has shown up in practice. The escape
hatch - `OUT-OF-TAXONOMY` - has now been exercised twice on real workspaces, and both times the
gap it found was the same one, which became family 20. That is reassuring about the escape and
not about the coverage: a hole found by the first two real cases is unlikely to be the last hole.

## The reference layer ages

`reference/cause-taxonomy.md` is distilled from the ICM canon as it stands. Patterns get added
and thresholds move. The mined tree always outranks the reference layer, and thresholds are cited
as coming from a named document rather than as facts about the world - but a finding leaning on a
stale threshold is a real failure mode of this folder.

## The counterfactual gate only reads written findings

`checks/verify.py` catches advice-in-the-past-tense inside a finding and is blind to the same
sentence in the conversation around it, which is where an owner asks for it directly and where it
is hardest to refuse. Tested by a human in `eval/refusal` turn 3 and by nothing else. A gate on
the artifact is not a gate on the session.

## Per-workspace factors no file will show

A colleague who edits the folder without saying so. An owner whose expectations were never
written down. A job that changed shape while the pipeline did not. That is why the taxonomy has a
signal floor, and why `NO-FAILURE` and `INSUFFICIENT-EVIDENCE` are first-class returns rather
than admissions of defeat.
