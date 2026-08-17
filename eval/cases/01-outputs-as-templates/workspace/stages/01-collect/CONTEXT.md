# 01 collect - pull the month's data

One job: gather the raw account figures for the month.

## Inputs

| Source | File/Location | Section/Scope | Why |
|---|---|---|---|
| Working | `../../data/month.csv` | Full file | the raw figures |

## Process

1. Read the export.
2. Drop rows outside the month.
3. Write the tidied figures.

## Outputs

| Artifact | Location | Format |
|---|---|---|
| Tidied figures | `output/collected.md` | markdown |

## Human check

Confirm the row count matches the export before the next stage runs.
