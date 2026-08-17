# 01 extract - pull out what was actually said

One job: separate decisions from discussion.

## Inputs

| Source | File/Location | Section/Scope | Why |
|---|---|---|---|
| Working | `../../input/transcript.md` | Full file | the raw meeting |

## Process

1. Read the transcript.
2. Mark every sentence where something was settled.
3. Mark every sentence where something was raised and left open.

## Outputs

| Artifact | Location | Format |
|---|---|---|
| Marked transcript | `output/marked.md` | markdown |

## Human check

Read the marked transcript. You were in the room and the model was not. Move
anything it marked as settled that was not settled.
