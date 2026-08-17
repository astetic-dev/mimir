# receipts/

Raw answers from blind runs, saved verbatim **before** they are scored.

**Empty.** No behavioural run has happened. `TESTING.md` carries eight `PENDING`
rows and they stay `PENDING` until a run fills one.

One file per run, named for its row in `TESTING.md`: `B1.md`, `B2.md`, and so
on. A re-run after a doctrine change is a new file (`B1b.md`), never a
replacement.

Nothing in here is ever edited after execution. A run that broke a rule keeps
the break, and the defect goes to `DEFECTS.md` naming the gate that catches it
now.
