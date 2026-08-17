# BUILD - pointing this machine at a different broken thing

Most of Mimir is not about ICM workspaces. The nine steps, the nine gates, the
five frozen returns and the marker discipline are a **diagnostician chassis**,
and only two parts of this folder are domain-specific: the cause taxonomy and
the miner.

This file is how you build a second diagnostician on the same chassis. It is
also, read the other way, the explanation of why this one is shaped as it is.

---

## What is domain-independent

Copy these across unchanged. They carry no ICM in them:

| Part | File | What it is |
|---|---|---|
| The nine-step method | `rules.md` | hard stops, intake, grade, scope one, establish, branch and prune, descend by necessity, rank, verify and write |
| The gate rule | `rules.md` | a gate asks, a gate never blocks. A turn that ends on questions has delivered nothing |
| The finding contract | `reference/output-contract.md` | nine sections, three markers, the frozen closing line |
| The five frozen returns | `reference/output-contract.md` 5 | OUT-OF-SCOPE, NO-FAILURE, INSUFFICIENT-EVIDENCE, UNRESOLVED, OUT-OF-TAXONOMY |
| The disguise catalogue | `reference/disguised-asks.md` | seven shapes, one answer, and the line between an evidence act and a remedy |
| The nine gates | `checks/verify.py` | everything except the domain word lists |
| The proving protocol | `TESTING.md` | pre-registered keys, blind allowlist, adversarial owner, unattended run, tier ladder |

## What you replace

Nine slots. The taxonomy is four fifths of the work and there is no shortcut
through it: it is the thing a fresh chat cannot reproduce, and a thin one turns
the whole folder into an opinion generator.

| Slot | Lives in | ICM's answer, as an illustration |
|---|---|---|
| `{{PATIENT}}` | `identity.md` | the workspace structure, never the model |
| `{{FAILURE_CLASS}}` | `identity.md` | an ICM workspace that does not do what its owner expects |
| `{{ARTIFACT}}` | `intake.md` | the folder, plus a transcript of one failing run |
| `{{EVIDENCE_TIERS}}` | `reference/evidence-grades.md` | A tree+transcript, B tree, C transcript, D account, E verdict |
| `{{CAUSAL_LAYERS}}` | `rules.md` step 5 | routing, contract, factory/product, graph, gates, shape, content **last** |
| `{{TAXONOMY}}` | `reference/cause-taxonomy.md` | nineteen families, each with a fingerprint and a "mistaken for" |
| `{{HARD_STOPS}}` | `rules.md` step 0 | not an ICM workspace; no failure reported; the cause is the model not the structure |
| `{{REMEDY_VERBS}}` | `checks/verify.py` `RX_PATTERNS` | move, split, extract, restructure, target tree, migration map |
| `{{MINER}}` | `checks/mine.py` | layers, link graph, contracts, placeholders, duplication, load bands |

---

## The six phases

### 1. SCOPE

One failure class, one patient, one artifact type. Write the one-line character
before anything else: *"X reads a broken Y the way a Z reads a W."* If that
sentence needs two clauses, the scope is two specialists.

Then run the kill test, honestly: **could a fresh chat with no folder get 80%
of this?** If yes, the answer is not more prose. It is a narrower failure class
or a real taxonomy, and if neither is available, do not build it.

### 2. SLOTS

Fill them in the order above. Two rules that are easy to skip and expensive to
skip:

- **Order the causal layers by how often each is truly guilty, not by how the
  system is drawn.** Mimir walks routing first and content last because content
  is the most-accused and least-often-guilty layer. Nearly every domain has one
  of those. Find it and put it last, deliberately, and say in the file that the
  order is not alphabetical convenience.
- **Every taxonomy entry needs its neighbour.** "What it is" and "fingerprint"
  are the easy two thirds. The line that prevents wrong convictions is *how to
  tell it from the family next to it*, and a taxonomy without those is a list of
  labels.

### 3. GROUND

**Write the miner before the examples.** This is the phase that separates a
diagnostician from a confident essayist, and it is the one most likely to be
skipped because it is the least fun.

The rule is: *the script computes, the model labels.* Anything countable in your
domain goes in the miner, and the checker then refuses any number the miner did
not produce. If nothing in your domain is countable, say so in `BLIND-SPOTS.md`
rather than pretending, and expect the finding to be weaker for it.

Then build one fixture the thing is *about*: a real, small, self-contained
broken example with seeded defects, plus decoys that tempt a wrong conviction.
Acquitting the decoy explicitly is part of what "correct" means.

### 4. PROVE

Write `expected.md` **before** the run and commit it before the output exists.
A prediction written afterwards is not a prediction. Then run the protocol in
`TESTING.md`.

**Preserve failures.** A run that broke a rule stays in the folder with the
break in it, and the defect goes in `DEFECTS.md` naming the gate that catches it
now. A folder with no failures in it is a folder whose testing was theatre.

### 5. CONFESS

`BLIND-SPOTS.md` is what the thing structurally cannot see, and it is written
from the design, not from the runs. Four classes fit almost every
diagnostician:

1. it trusts the artifact it is given
2. it infers rather than observes some part of the mechanism
3. it cannot look anything up
4. its reference material ages

### 6. HAND OFF

Cold-stranger test: someone who has never read any of this opens the folder,
reads only `README.md`, and gets a useful answer inside five minutes using the
shipped fixture. Any question they have to ask you is a README defect, and the
fix is in the README, not in the conversation.

---

## The one thing not to copy

Mimir's warmth in refusal is tuned for an owner who built the broken thing
themselves and is mildly embarrassed about it. A domain where the patient is a
stranger, a machine, or someone else's work needs a different register, and
copying this one will read as either cold or oddly familiar.

`identity.md` is where that lives. Rewrite it rather than editing it.
