# Mimir

**Your agent's folder is misbehaving. Mimir tells you the one reason why, and
nothing else.**

Drop this folder into Claude Code next to a workspace that is not doing what you
asked it to, and Mimir works backward from what went wrong to the single
structural cause, shows the evidence trail, says what would prove it wrong, and
stops. Like a pathologist, not a surgeon.

## Who it is for

Anyone who has an agent folder that has started letting them down: it ignores
rules you definitely wrote down, does the wrong step, gives a different answer
every time, or has quietly got worse over months. You do not need to know how
these folders are supposed to be built. That is what is in here.

If you use Taurus: every agent and every project in your left rail is one of
these folders, whether or not anyone set it up that way.

## Start here

Open this folder in Claude Code and say:

> "My agent at `<path>` keeps ignoring the rules I gave it. Here is what
> happened last time it went wrong."

Paste the conversation that went wrong along with it if you have one. If you do
not, Mimir will ask for two things and tell you where to find them.

## What you get back

One page, always the same shape:

```
DIAGNOSIS              one sentence, one cause
EVIDENCE TIER          what you gave it, and what that can and cannot prove
EVIDENCE CHAIN         numbered, each link marked [seen] / [inferred] / [general]
WHY IT STOPS HERE      the step below it rejected, and the step above it passed
RULED OUT              what was checked and cleared, with the evidence
CONTRIBUTING FACTORS   real, and kept subordinate
WEAKEST LINK           the part of its own case Mimir thinks is thinnest
CONFIDENCE             high / moderate / provisional / UNRESOLVED
WHAT WOULD OVERTURN    the observation that would prove it wrong
```

Every `[seen]` claim can be found in your folder with a text search. Every
number comes from a script, not from the model. If the evidence will not carry a
cause, it says so and names the one thing that would settle it, rather than
guessing.

## What it will not do

- **It will not fix anything.** No target folder layout, no "move this file", no
  plan. That is `icm-architect`'s job, and it will ask you questions Mimir has
  not asked.
- **It will not grade your folder** or list everything wrong with it. One cause,
  ranked. Twelve findings is an inventory, not a diagnosis.
- **It will not tell you what your folder does.** That is a map, and it needs no
  failure at all.
- **It will not invent a problem.** If your folder is fine and what you are
  seeing is the method working, it says so and stops.

## Try it in two minutes, on the broken folder shipped with it

```bash
python checks/verify.py --selftest   # proves the gate works: 1 pass, 12 named fails
python checks/mine.py --selftest     # proves the fingerprints fire
python checks/mine.py checks/fixtures/workspace
```

Then open `checks/fixtures/workspace/` and `checks/fixtures/transcript.txt`,
paste them at Mimir cold, and compare what you get with
`checks/fixtures/good-finding.md`. Needs Python 3 and nothing else. No install,
no keys, no network.

**The bar:** from dropping this folder in to a diagnosis you can act on, under
five minutes.

## Folder map

| File | Job |
|---|---|
| `identity.md` | Who Mimir is, and what he refuses to be |
| `rules.md` | The method: nine steps, each with a gate |
| `intake.md` | How he walks you to the evidence when you arrive with only a complaint |
| `examples.md` | Three worked cases, including one where nothing is broken |
| `reference/evidence-grades.md` | What each source proves, and what it cannot |
| `reference/cause-taxonomy.md` | Twenty bounded causes, each with its fingerprint |
| `reference/cause-vs-symptom.md` | The translation drill: complaint in, cause out |
| `reference/output-contract.md` | The finding's shape and the five frozen returns |
| `reference/disguised-asks.md` | The seven ways "just fix it" arrives in costume |
| `checks/mine.py` | Reads a folder, computes every number. The model never counts |
| `checks/verify.py` | Ten gates on the finding itself, plus `--selftest` |
| `eval/` | Blind cases with answer keys committed before any run, and the receipts |
| `TESTING.md` | What has been proved, what is still `PENDING`, and by whom |
| `BLIND-SPOTS.md` | What Mimir structurally cannot see |
| `DEFECTS.md` | What has gone wrong, kept rather than polished away |
| `HOW-IT-WORKS.md` | The whole machine in one file: the nine steps, the twenty cause families, the two scripts |
| `BUILD.md` | How to point this same machine at a different kind of broken thing |
| `CREDITS.md` | Whose ideas these are |

## Where it sits

Seven roles work on an ICM workspace, one folder each. Mimir is the
**diagnostician**, and he is the only one of the seven that works backward from
something that already broke.

So if nothing is broken, you want one of the other six — and three of them are
close enough that their questions land here by mistake. He will not tell you
what the folder should become, whether it is good enough, or what it is. Those
belong to the architect, the editor and the cartographer.

The full list of seven, with the question each answers, is in `identity.md`.
