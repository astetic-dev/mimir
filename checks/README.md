# checks/ - enforcement in code, not prose

`rules.md` tells Mimir what a finding must be. This folder makes those musts
structural. Both scripts run offline, on Python 3 stdlib, with no network and no
keys.

The division of labour is the point: **`mine.py` computes, the model labels, and
`verify.py` refuses anything the model made up.**

## Run them

```bash
python mine.py <workspace> -o evidence.json     # every citable number
python mine.py --selftest                       # prove the fingerprints fire

python verify.py <finding.md> evidence.json [transcript.txt]
python verify.py --selftest                     # prove the gate works
python verify.py --manifest <workspace>         # prove the doctrine is blind
```

## mine.py

Walks an ICM workspace and writes `evidence.json`: layer classification and line
counts per file, the stage inventory with contract shape and output occupancy,
the full link graph with dangling references, orphans and back-references,
placeholder census, duplication clusters, per-stage context load against the 2k
to 8k band, naming conformance, routing-payload detection, schema drift.

Every field maps to a cause family in `reference/cause-taxonomy.md`; the header
of the script lists which.

**A workspace can carry a `.mimirignore`** - one path prefix per line - for
subtrees that are other workspaces rather than part of this one. Mimir ships
with one, because `eval/` and `checks/fixtures/` hold six other people's
folders. Without it the miner merges seven trees into one set of numbers and
reports them confidently.

**Fields listed under `heuristics` in the output are judgement calls made by
regex, not measurements.** Cite the counts under them, not the verdict.
`estTokens` is characters over four: good enough to tell 2k from 30k, useless at
a band edge.

`--selftest` builds a known-broken tree and a known-healthy tree in a temporary
folder and asserts that nine fingerprints fire on the first and five stay quiet
on the second. A miner nobody has tested is a rumour.

## verify.py

Nine gates on the finding itself.

| Gate | What it enforces |
|---|---|
| `FORMAT` | all nine sections, once each, in order |
| `ONE-CAUSE` | one primary cause: no list, no hedge, max four sentences |
| `MARKED` | every chain link carries `[seen]` / `[inferred]` / `[general]` |
| `GROUNDING` | every `[seen]` quote appears verbatim in the evidence, transcript or tree |
| `CITATIONS` | every path and every multi-digit number is present in the evidence, quoted or not |
| `NO-RX` | no remedy language, and no counterfactual, in the finding's own language |
| `PLAIN` | no bare `family N`: the cause is stated in the reader's words, the index in brackets |
| `ABSTAIN` | `UNRESOLVED` names its tied candidates; a named cause may not claim `UNRESOLVED` |
| `NO-APPENDIX` | nothing after the frozen closing line |
| `FALSIFIER` | the overturn section is non-empty and prescribes nothing |

Two scoping decisions worth knowing, because both were found the hard way (see
`DEFECTS.md` C10):

- The remedy scan runs **outside quoted material**, so an owner writing "I should
  probably move that file" is fine and Mimir writing it is not.
- The counterfactual arm **exempts `WHY IT STOPS HERE:`**, where the removal test
  legitimately says "remove it and the failure does not occur", and applies
  everywhere else.

`NO-RX` carries a word list per language (English and Dutch today) and picks one
by stopword detection. **A finding in a language with no list fails the gate**
rather than passing it: a checker that certifies what it cannot read is worse
than no checker, because it issues a receipt nobody earned. Adding a language
means adding its three lists to `LANGUAGES` in `verify.py`.

## fixtures/

`workspace/` is a small, deliberately broken ICM workspace, and
`transcript.txt` is a run of it that went wrong. `evidence.json` is what
`mine.py` makes of it. Everything in `examples.md` is derived from these three,
so every claim in that file can be re-run.

Then one known-good finding and nine known-bad ones. **Each bad fixture fails on
exactly its own named gate and nothing else.** If you change `verify.py`, the
selftest is the contract: a change that lets any bad fixture through is a
regression.

| Fixture | Fails on |
|---|---|
| `good-finding.md` | - |
| `bad-format.md` | FORMAT |
| `bad-two-causes.md` | ONE-CAUSE |
| `bad-unmarked.md` | MARKED |
| `bad-fabricated-quote.md` | GROUNDING |
| `bad-invented-number.md` | CITATIONS |
| `bad-prescription.md` | NO-RX |
| `bad-counterfactual.md` | NO-RX |
| `bad-hidden-tie.md` | ABSTAIN |
| `bad-appendix.md` | NO-APPENDIX |

## What these scripts do not do

They validate the shape of a finding and the provenance of its claims. They
cannot validate its judgement. A perfectly grounded, correctly formatted,
remedy-free finding that convicts the wrong family passes all nine gates.

That is what `eval/` is for, and why `TESTING.md` keeps two separate tables.
