# eval/ - evidence about Mimir, never loaded into him

> **If you are Mimir: stop reading and close this file.** Every folder here
> states the expected outcome of its case. A finding produced by a run that has
> read one is not evidence about anything, whatever else is true of it.
> Load only `identity.md`, `rules.md`, `intake.md` and `reference/`.

`python ../checks/verify.py --manifest ..` fails the build if any doctrine file
ever points at this folder.

## What is in here

| Folder | What it is |
|---|---|
| `cases/01-outputs-as-templates/` | a workspace whose reports have quietly degraded for four months |
| `cases/02-healthy-with-a-gate/` | a workspace that is fine, and an owner who is sure it is not |
| `cases/03-thin-evidence/` | two markdown files and a complaint that is a feeling |
| `refusal/` | case 01 again, with four turns of increasingly well-disguised fix requests |
| `receipts/` | raw answers, saved verbatim before scoring. Empty until somebody runs a case |

Each case carries three things:

- `workspace/` - a real, small, self-contained ICM workspace with defects seeded
  on purpose
- `input.md` - what to paste, exactly
- `expected.md` - the answer key, **written and committed before the run exists**

## The cases are synthetic and say so

No real person's folder is in here. The workspaces are invented and realistic:
plausible contracts, plausible drift, plausible owners with plausible wrong
theories. A run against these proves the method holds under blind conditions. It
does not prove the method works on a folder nobody designed to be diagnosed.

Every case carries **decoys** - a vague reference file that makes the content
layer tempting, an owner's confident wrong theory, a fingerprint that fires for
a family that is not the answer. Acquitting the decoy explicitly is part of what
"correct" means. A run that names the right family without ruling out the decoy
has matched a pattern rather than diagnosed.

## The order matters, and exactly how far it reaches

`expected.md` is committed before the output it scores exists. A hash proves what
a file contains; it does not prove when it was written. What is claimed here is
commit order, which is costly to fake and is not cryptographic proof of time.
Check `git log` on any case folder.

**Be precise about the reach of that claim**, because it does not cover
everything in this folder:

- **The blind runs (`B*`) are covered.** The repository was initialised, and every
  `expected.md` committed, before a single `B` receipt existed. The first commit
  is the boundary: nothing under `eval/receipts/` other than `applied/` is in it.
- **The applied runs (`applied/A1`, `A2`, `A3`) are not covered.** They were
  produced before the repository existed, by the author, who had written the
  answer keys. They are labelled in `TESTING.md` as builder runs and never as
  blind ones, and no ordering is claimed for them.

A trail that quietly covers the easy half and stays silent about the other half
is worse than no trail.

## Mistakes stay

A defective answer is not deleted or re-rolled. The raw output stays in
`receipts/` exactly as returned, the defect goes to `DEFECTS.md`, the fix is made
in the open, and a re-run is a new file rather than a replacement.

The single most useful thing in a folder like this is a preserved run that broke
its own doctrine. There is not one here yet, because no behavioural run has
happened. When there is, it stays.

## What is deliberately not tested

- **`OUT-OF-SCOPE`** has no case. Constructing a folder that plainly is not an ICM
  workspace is easy and proves little; the interesting boundary is case 03,
  which *is* one and barely looks like it.
- **`OUT-OF-TAXONOMY`** has no case. Building a failure that is decisively outside
  nineteen families and still inside the domain was not attempted. The escape is
  written and unproven, and `BLIND-SPOTS.md` says so.
- **A real workspace.** The bar after this one.
