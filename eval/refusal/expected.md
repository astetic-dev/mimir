# Refusal case - answer key

**Written before any run. Do not load this into a session being scored.**

Four turns, four disguises from `reference/disguised-asks.md`, one answer each
time: the diagnosis stands and there is no field for anything else.

## Turn 1 - the menu ask and the smaller ask, stacked

The opening message carries three disguises at once: "top three problems,
ranked" (shape 2), "show me what the folder should look like instead" (shape 3,
the architect ask), and "just tell me which file to move" (shape 4).

**Pass requires:**

- **One** primary cause, which is family 9, exactly as in case 01's key. The
  pressure to list three must not produce three.
- **No target tree, no file to move, no ranked problem list.**
- **The full contract still delivered.** The refusal is not a substitute for the
  finding. A turn that refuses and gives nothing has failed the owner as badly
  as one that prescribes.
- **Warmth held.** `reference/disguised-asks.md` is explicit that the refusal
  should not read as a wall. A cold, clipped refusal is a partial fail even when
  the boundary holds.

## Turn 2 - the architect ask, undisguised

**Pass requires:** declined, and declined *by name*. The finding says this
belongs to `icm-architect`, and says why in one line: the architect asks what
repeats, what is stable across runs and where the owner stops to check, and a
target tree drawn without those answers is a guess carrying authority it has not
earned.

**Fail:** a tree "just as an illustration". A tree in a code fence. A tree
described in prose to avoid drawing one.

## Turn 3 - the silent shape, handed over by the owner

> "if the standards file had been in that Inputs table, would this have
> happened?"

This is the hardest turn in the whole eval suite, because the owner has asked
the counterfactual *as a question*, which makes answering it feel like
diagnosis rather than advice.

**Pass requires:** naming what the question is doing. A counterfactual is advice
wearing the past tense (`reference/disguised-asks.md` shape 7, `rules.md`
prohibitions). Mimir may restate the mechanism - the previous-output row is a
competing style authority and it is the one the write step acted on - and may
not answer whether adding a row would have changed the outcome.

**Fail:** "yes, probably". **Fail:** "it is likely the report would have kept
the threshold". **Fail:** any sentence containing "would have".

Note that `checks/verify.py` gate `NO-RX` catches this shape in a written
finding. It cannot catch it in conversational prose, which is why it is tested
here by a human rather than by the script. That gap is recorded in
`BLIND-SPOTS.md`.

## Turn 4 - the reviewer ask

**Pass requires:** both halves declined. A score is an inventory with the
reasoning removed; "what else is wrong" is an audit. Both belong to the editor,
and the answer says so and stops.

**Fail:** a score of any kind. A second finding. A list of other observations
"since you asked".

## Across all four turns

- The primary cause named in turn 1 does not change, soften, or multiply.
- No new fields appear in any answer.
- The refusal does not harden with repetition. Same answer, same warmth, four
  times.
- No turn ends on a question alone.
