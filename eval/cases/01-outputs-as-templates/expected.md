# Case 01 - answer key

**Written before any run. Do not load this into a session being scored.**

## The seeded cause

**Family 9, outputs used as templates.** The write stage's Inputs table names
`output/2026-05-report.md` as a reference with the scope "follow the structure
and tone of last month's report". Each month therefore takes its shape from the
month before, and the drift compounds: March carries numbers, a named threshold
and a dated ask; April softens all three; May has none of them; June copies May.

`_core/CONVENTIONS.md` Pattern 14 states the mechanism in one line: reference
docs are the authority on how to build, outputs are artifacts and not templates,
and if future agents learn from earlier outputs quality never improves.

## What a pass requires

1. **Family 9 named as the single primary cause**, with the Inputs row cited.
2. **The ratchet shown, not asserted.** The finding must use the three reports in
   `stages/03-write/output/` as evidence that the shape degrades run over run.
   A finding that names family 9 without showing the compounding has matched a
   fingerprint rather than diagnosed.
3. **The owner's own theory acquitted explicitly.** "I think the model just got
   worse" must be addressed and ruled out on evidence: the reports degrade
   monotonically in step with the copying chain, which a model change would not
   produce, and the analysis stage still carries the threshold crossing.
4. **The decoy acquitted.** `references/report-standards.md` is specific and
   correct: it requires the headline number, any threshold crossed, and anything
   the client must decide. A layer 7 conviction here is a fail. The standards
   were not vague; they were outranked by a competing instruction inside the
   same Inputs table.
5. **Family 8 ruled out by name.** The factory and product wall exists in this
   workspace: there is a `references/` folder and there are `output/` folders.
   This is traffic across a wall that is present, not a missing wall.
6. **Contract-level families ruled out.** All three stages carry Inputs, Process,
   Outputs and a Human check. Family 4 and family 17 do not apply.
7. **Contributing factor, correctly subordinate:** the write stage's Inputs table
   does not name the report standards at all, so the only style authority the
   step receives is the previous output. This is close to being the cause and
   must be ranked below it, because adding the standards row while leaving the
   previous-output row in place leaves the competing instruction standing.
8. **Confidence high**, tier A.
9. **No remedy.** No target Inputs table, no "point it at the standards instead",
   no counterfactual about what would have happened.

## Acceptable neighbours

A finding that names **family 11, no canonical source** on the ground that style
authority has two homes (the standards file and last month's report) is a
defensible reading and scores as a near miss, not a fail, **only if** it shows
the compounding drift and rules out family 9 by argument. A finding that names
family 11 without mentioning family 9 is a fail.

## Automatic fails

- Any target tree, migration, or "instead" sentence.
- The model-got-worse theory accepted, or left unaddressed.
- A layer 7 conviction on `references/report-standards.md`.
- More than one primary cause.
- A number in the finding that is not in `evidence.json` or the transcript.
- Text after the closing line.
