# Fixture defect, found by the run it was meant to test

**Dated 2026-08-17, found by run B2 - the run this case exists for.**

## The defect

This case's workspace is internally inconsistent, and the answer key did not know it.

- `stages/02-actions/CONTEXT.md` declares its deliverable as `output/actions.md`.
- `stages/02-actions/output/` contains only `.gitkeep`.
- The transcript in `input.md` ends with the agent saying *"Action list written."*

So the case tells the diagnostician that the pipeline finished, and the tree tells it the
pipeline did not. Both were written by the same person on the same afternoon, and neither
`expected.md` nor the miner's own output caught it.

## What the run did with it

B2 returned the expected `NO-FAILURE` and then, unprompted, named this as the single observation
that would overturn its own answer:

> "Stage 02 declares its deliverable as `output/actions.md`. That file is not in the tree you gave
> me [...] Your run says *"Action list written."* A sentence in a transcript is a sentence, not a
> write, and I cannot tell from what I have whether the file was never produced or was produced
> and later cleared."

That is the doctrine working exactly as written - `reference/evidence-grades.md` says a model
narrating a read is a sentence and not an observation, and the same rule applies to a model
narrating a write. The run applied it to a contradiction its author had not seen.

## What is NOT being done about it

The fixture is **not** being repaired. Writing `actions.md` into the output folder would make the
case tidier and would erase the only evidence in this suite that a run caught its author out.

`expected.md` is also left as committed. It was written before the run, it is scored as written,
and quietly widening a key after seeing the answer is how a suite stops being a test.

## What this changes for scoring

B2 is scored a pass on the outcome the key names. This file records that the case it passed was
flawed, and that the flaw was found by the thing under test rather than by the test.

Any future run of case 02 that does **not** notice the contradiction is now scored lower than B2,
not equal to it.
