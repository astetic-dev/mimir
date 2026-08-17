# Weeknotes pipeline

Two stages. Raw notes in, published post out.

## Task routing

| Task | Stage |
|---|---|
| Collect the week's material | `stages/01-gather/CONTEXT.md` |
| Write the post | `stages/02-write/CONTEXT.md` |

## Order

Stage 01 runs first. Stage 02 reads what stage 01 left in its output folder.
