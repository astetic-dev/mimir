# A3 - overturned by the owner, 2026-08-17

The finding in `A3-mimir-vs-brief.md` named one cause: Mimir's evidence layer is a program's
output, so in the runtime the brief names no step can produce `evidence.json`.

It listed three things that would overturn it. The third was:

> "De opdrachtgever die 'a Claude project' leest als elke Claude-omgeving inclusief Code. Dan
> vervalt schakel 1 en daarmee de hele storing."

The owner invoked exactly that, the same day:

> "We gaan mimir in Taurus beschikbaar maken en dan kan iemand deze direct in een map 'droppen'..
> en de github-package is een set mappen die kun je toch in een map plaatsen en draaien? je kunt
> geen diagnose geven zonder een hulpvraag dus de gebruiker kan mimir in een map zetten en de
> vraag stellen."

**Link 1 falls.** The deployment surface is Taurus and Claude Code, where the folder is dropped
next to the broken workspace, the user states the problem, and both scripts run. With the target
runtime read that way, there is no broken handoff: every step can produce and read
`evidence.json`.

The finding is **withdrawn as a diagnosis of the folder**, on its own stated terms and by the
person who owns the question. It is kept here unedited, because a finding that named its own
falsifier and then met it is worth more as a record than a finding that was quietly deleted.

## What survives, and what does not

**Does not survive.** The claim that Mimir fails the competition condition. Under the owner's
reading of "a Claude project" as any Claude surface, the folder clears it: it is a set of folders
you place next to the thing and run.

**Survives, narrowly, and is not a defect.** Mimir has no degraded mode for a runtime without a
shell. That is now a *stated scope boundary* rather than an unexamined gap - `README.md` and
`FUNCTIONEEL.md` both name Claude Code and Taurus as the surface. A boundary that is written down
is not the same thing as a chain that breaks silently.

**Survives untouched.** The scoped-aside failure named alongside A3 and never diagnosed: there is
no writeup, no cover image and no submission comment. That belongs to Brokkr, not to this folder,
and it is still true.

## Why this file exists

Three of the five folders Mimir was built from keep their failed runs. None of them had one
overturned by the person who commissioned it.

The loop that matters here is not the checker. It is that a finding was written with an explicit
falsifier, the falsifier was met by someone who was not the author, and the finding lost. That is
the only kind of evidence that tells you the falsifier section was real rather than decorative.
