# Cause versus symptom - the drill

The single discipline that separates a diagnosis from an audit. The owner hands you symptoms.
The mined tree hands you more symptoms, in numbers. Your output must hand back a cause.

This is the translation table. The middle column is the trap: it sounds like an answer, it is
accurate, and it is still a symptom wearing a technical vocabulary. A finding that lands in the
middle column has renamed the complaint and stopped.

| What the owner says (or the miner counts) | Lazy restatement - **forbidden as a diagnosis** | The cause |
|---|---|---|
| "It ignores my rules" | "The rules are not being followed" | Every rule is in `CLAUDE.md`, so all of them arrive in every conversation with nothing marking which apply to this step, and the ones that matter compete with the ones that do not |
| "It is inconsistent between runs" | "The output varies" | No stage names its inputs, so what gets loaded is decided by the agent afresh each run, and the decision is not the same twice |
| "Quality is slowly getting worse" | "The outputs are declining" | Stage 03 loads stage 02's previous output as its style reference, so each run learns from the worst work the workspace has ever produced |
| "It invented a brand voice" | "It hallucinated" | `voice.md` still contains `{{VOICE_DESCRIPTION}}`, so the agent met a literal placeholder where a fact should be and filled the gap itself |
| "It contradicts itself" | "The docs are inconsistent" | The retention rule has two homes and both read as authoritative, so the agent quotes whichever one the current step happened to load |
| "The agent hallucinated a file" | "It made up a path" | Stage 03's Inputs name `../02-draft/output/brief.md`, which no stage's Outputs table produces |
| "It loses the thread halfway" | "The context is too big" | Stage 02's Inputs pull a 900-line reference in full where Pattern 4 would route to one section, so the step opens at four times the healthy band |
| "It reads the wrong things" | "It picks bad files" | Six reference files are pointed at by nothing; the agent finds them by search and cannot tell a leftover from a live one |
| "It never stops to let me steer" | "It is too autonomous" | No contract in the workspace has a human check, so there is no step at which steering is the work |
| "It works for me and not for him" | "It is unreliable" | `CLAUDE.md` and `AGENTS.md` are both maintained by hand and have diverged, so which instructions apply depends on which tool opened the folder |
| `entry.lines: 412` | "The entry file is long" | The entry file is carrying the voice rules and the examples, which is the catalog holding books |
| `duplication[0].files: 2` | "Two files are similar" | The same constraint is stated in two places that must be kept in sync by hand, and the last edit only touched one |
| `graph.dangling: 4` | "There are broken links" | Four contracts point at outputs that no stage writes, so the chain breaks at a named joint every time it is walked |
| `stages[3].outputFolder.onlyGitkeep: true` (in five of six stages) | "Most stages have not run" | The workspace was scaffolded for a pipeline that has run once, so five of its six contracts have never been tested against real material |

---

## The test

For any candidate line in your finding, ask:

> **Does this tell the reader *why* the behaviour keeps happening, or only *that* it happened?**

- *That it happened* is a symptom. Keep going.
- *Why it keeps happening* is a cause. That is the finding.

A second test, for the numbers: **a count is never a cause.** `entry.lines: 412` is a
measurement. What 412 lines in the entry file *does* to an agent is the cause. If your sentence
would still be true with a different number in it, you have not finished.

---

## The trap

**The loudest number is almost never the cause. It is usually where a cause becomes visible.**

The biggest file, the most duplicated block, the stage with the most dangling references: each of
these is where something surfaced, not why it surfaced. Follow the graph outward from the loud
file to the structure that keeps feeding it.

The ICM version of this trap has a specific shape, and it catches most first attempts:

> The failing step is stage 04. Stage 04's contract is fine. The cause is in stage 02, whose
> output stage 04 is reading, and which nobody looked at because it did not fail.

---

## The two floors nothing may drop below

**Never stop at the owner.** "He did not follow the process" is a symptom of a workspace that
allowed the process not to be followed. Ask what the contract required, what it made easy, and
what it left to memory. An investigation that produces a name gets no further information from
anyone, ever.

**Never stop at the model.** "Claude ignored the instructions" is not a cause, it is the
behaviour you were asked to explain. Ask what the structure did that made ignoring likely: what
arrived, in what order, competing with what. If the honest answer is that the structure did
nothing wrong and the behaviour is a model property, that is not a structural diagnosis at all
and `rules.md` step 0 says to stop and say so.
