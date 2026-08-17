# Client report pipeline

Three stages. Account data in, client report out. One run per month.

## Task routing

| Task | Stage |
|---|---|
| Pull the month's data | `stages/01-collect/CONTEXT.md` |
| Work out what it means | `stages/02-analyse/CONTEXT.md` |
| Write the report | `stages/03-write/CONTEXT.md` |

## Order

01, then 02, then 03. Each stage reads the previous stage's output folder.
