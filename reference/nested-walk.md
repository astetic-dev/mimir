# The nested walk - diagnosing one output

Used at the **nested layer** (`identity.md`): a specific thing a workspace produced came out
wrong, and you are working back from that output rather than from the folder.

The ICM layer walks `cause-taxonomy.md` from routing down to content. This walk goes the other
way: from the output, back up the chain that made it, until you reach the step where what was
required stopped being available. Same families at the end of it. Different door.

---

## Before you start: the standard is not yours

At this layer the standard is **the target workspace's own reference layer**. What "good" means
for this output is whatever that folder says it means, in writing, and nothing else.

- Find it before you diagnose. It is usually in `references/`, `_shared/`, a standards file, or
  the reference row of the producing step's Inputs table.
- **If the folder declares no standard for this output, stop.** That is the finding, and it is
  the whole finding: nothing produced by this workspace can be wrong, because the workspace has
  never said what right is. Return it at the ICM layer as family 20 and do not proceed to guess a
  standard.
- Your own view of good output is never the standard. Not once, not as a sanity check, not
  "obviously a report should mention that". If the folder does not require it, the output did not
  fail.

---

## The six steps

Run them in order. The first one that answers is the answer.

### 1. Which step produced this?

Read the `Outputs` tables until you find the one that declares this artifact. If no step declares
it, the output came from outside the pipeline - say so and stop, because nothing in this folder
was responsible for it.

**Evidence:** `stages[].declaredOutputs[]` in the mined evidence.

### 2. What did that step declare as its inputs?

The producing step's `Inputs` table, in full. This is the list of everything the step was told to
have in front of it.

**Evidence:** `stages[].declaredInputs[]`.

### 3. Is the standard the output missed on that list?

Take the specific requirement the output failed - the threshold it omitted, the field it left
blank, the tone it broke - and find which file in the folder carries that requirement. Then ask
whether that file is among the step's declared inputs.

**Not declared → family 20**, the contract omits what the step needs. This is the most common
answer at this layer and it was the answer at the first real workspace this was run on: a
drafting step whose inputs named the templates and the tone and never the project's own state.

Stop here. The rest of the walk is about a standard that *was* declared.

### 4. Was it declared but not read?

A declared input is not a loaded one. Only a transcript can tell you, and only a recorded read -
a model narrating *"consulting the standards"* is a sentence, not a read
(`reference/evidence-grades.md`).

**Declared and not read →** look upstream at why. A step that skipped a declared input is usually
carrying too much (family 7), or the input was routed as a whole file where a section was needed
and the relevant part was buried (family 6).

**No transcript →** you cannot separate step 4 from step 5. Say so, mark the branch unresolvable,
and name the transcript as the evidence that would close it. Do not pick the more interesting of
the two.

### 5. Was it read and not applied?

This is **layer 7, the content**, and here is where the nested layer differs sharply from the ICM
layer. Upstairs, content is the most-accused and least-often-guilty layer and you walk it last on
purpose. Down here it is a routine answer, because you are diagnosing the work rather than the
factory.

It is still not the *first* answer. Steps 1 to 4 come first, every time, because a rule that was
never in the room cannot have been ignored in it.

**Read and not applied → check the standard for a competing instruction before you convict the
content.** Two requirements in the same folder pulling opposite ways is family 11, not a lapse:
in the case that produced this file, a writing step was told both to meet a standard and to match
last month's output, and the second instruction won. The agent obeyed the folder. The folder
disagreed with itself.

### 6. Is the standard itself the defect?

The last question, and the one owners least expect. The requirement may be ambiguous, may
contradict another requirement, or may describe an output the workspace has no way to produce.

**Evidence:** quote the requirement and show why it cannot be met as written. This is a finding
about the folder returned at the nested layer, and it is legitimate - but it is last, because
"your standard is wrong" is the most comfortable conclusion available and comfort is not
evidence.

---

## What changes in the finding

The contract in `reference/output-contract.md` is unchanged - nine sections, same markers, same
gates. Three things differ in how you fill it:

- **`EVIDENCE TIER`** says which layer you are in as well as which tier.
- **`RULE`-style anchors** quote the *target workspace's* standard, not the ICM canon, whenever
  the standard exists. Canon citations appear only where the folder is silent, and where it is
  silent about something it should have declared, that is family 20 and probably the finding.
- **`WHAT WOULD OVERTURN THIS`** almost always includes: *a transcript of that run showing the
  standard among the reads*. At this layer that single artifact separates step 4 from step 5, and
  it is usually the cheapest thing the owner has that you do not.

---

## The two mistakes this walk exists to prevent

**Diagnosing the output against your own taste.** You will read a report and see three things you
would have done differently. None of them is a finding unless the folder asked for them. This is
the failure that makes a nested diagnostician worthless, because it is indistinguishable from an
opinionated reader and the owner already has one of those.

**Stopping at "the model did it wrong".** The output is the behaviour you were asked to explain,
not an explanation of it. `rules.md` forbids stopping at the model and it binds here hardest,
because at this layer the model's output is sitting right in front of you and blaming it costs
nothing.
