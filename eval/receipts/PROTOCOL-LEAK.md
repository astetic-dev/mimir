# The blind protocol leaks, and the runs found it

**Dated 2026-08-17, before any run was scored.**

`TESTING.md` says a blind run loads exactly `identity.md`, `rules.md`, `intake.md` and
`reference/`. Every run was asked to report the exact list of files it opened, so the isolation
could be audited afterwards.

One run reported this, unprompted:

> "Disclosure for the audit: `mimir\CLAUDE.md` was injected into my context automatically by the
> harness as a project instruction file before my first action. I did not open it and did not act
> on its routing beyond what `identity.md`/`rules.md` already say. Also auto-injected:
> the operator's global `~/.claude/CLAUDE.md` and the parent workspace's `CLAUDE.md`."

That is correct and it applies to **every run in this folder**, not only the one that noticed.

## What actually leaked

Three files, none of them an answer key, none of them under `eval/`:

| File | What it carries | Does it give anything away |
|---|---|---|
| `mimir/CLAUDE.md` | the routing table and the Load / Read / Verify split | It names `examples.md` and `TESTING.md` as files that exist. It contains no case, no cause and no expected answer. |
| `~/.claude/CLAUDE.md` | the operator's own global instructions | Nothing about Mimir. |
| `ontwikkelmap/CLAUDE.md` | the parent workspace's instructions | Nothing about Mimir. |

So the runs saw slightly more doctrine than the protocol declares, and saw no answers.

## Why it is recorded anyway

Because "no answers leaked" is a judgement, and the protocol said something narrower and more
checkable than that. A protocol that is 95% honoured and described as fully honoured is how a
test suite starts lying, and the gap is exactly the size nobody notices.

There is also a structural point worth stating plainly: **a folder that carries a `CLAUDE.md`
cannot be blind-tested from inside itself in Claude Code.** The harness injects it before the
agent takes its first action; there is no flag the runner controls. Any future run of this suite
has the same leak unless it is executed from outside the folder tree, or the entry file is
temporarily moved aside.

## What was NOT compromised

- No run opened an `expected.md`. All file lists were checked.
- No run opened `DEFECTS.md`, `BLIND-SPOTS.md` or anything under `eval/` other than the case
  workspace it was given and the input pasted into its prompt.
- The one exception is B5, which diagnoses Mimir itself and was therefore permitted the folder as
  evidence, with `DEFECTS.md`, `TESTING.md` and `eval/` explicitly forbidden. That relaxation is
  declared in the run's own prompt and here.

## The other caveat, which is larger

These runs are **fresh contexts, not independent readers.** Same model family, and every prompt
was written by the person who wrote the doctrine and the answer keys. What they demonstrate is
that the doctrine survives a context with no memory of the build. What they cannot demonstrate is
what a stranger gets. That remains `B8`, and it remains `PENDING`.
