DIAGNOSIS: The voice rules live in the entry file, so no stage contract can
route to them, and the write step opens with only the general style guide in
front of it.

EVIDENCE TIER: A - the workspace tree and the verbatim transcript of the session
of the 14th.

EVIDENCE CHAIN:
1. [seen] `CLAUDE.md` is 135 lines against an entry-file limit of 60, and its
   headings include "Voice rules" and "Examples" -> the entry file is carrying
   content rather than routes.
2. [seen] The write stage contract names two inputs and no third:
   `../01-gather/output/gathered.md` and `../../references/style-guide.md` ->
   nothing in the contract points at the voice rules.
3. [seen] The routed reference is 22 lines and says "Keep it grounded." where
   the entry file says "Never open with the week." -> the file the contract can
   reach is the general one; the specific one is unroutable.
4. [seen] The transcript records the reads at the failing step: "Read
   stages/02-write/CONTEXT.md" and "Read references/style-guide.md" -> the
   explicit context of the writing step was the contract and the general guide.
5. [inferred] The specific rules did arrive, inside the auto-loaded entry file,
   alongside the folder map, the routing table and the trigger table -> they
   were present and undifferentiated, competing with material about where
   things live.
6. [seen] The post opens "This week was an exciting one on the infrastructure
   side!" and ends "Thanks for reading!", and the owner replies "this is exactly
   the voice I told it not to use" -> the rules were available and unapplied.
7. [general] An instruction that arrives with the folder map competes with the
   folder map; layered loading exists so that the rule for a step arrives at the
   step. [general - not measured in this tree]

WHY IT STOPS HERE:
- Deeper step tested and rejected: "the workspace was built without reading the
  conventions". Remove it: the conventions were read. Does that require this
  entry file to hold these rules? No. Entry files accumulate content because
  they are the file everyone opens, whether or not the builder knew the
  guardrail. The failure still requires these rules to sit in this file.
- Shallower step passed over: the contract could have named a section of
  the style guide instead of the whole file (family 6). The Inputs row for the style guide does say "Full file". But the
  routed guide is 22 lines, so no section scope changes what arrives, and the
  rules that were broken are not in it at any scope. Naming section routing (family 6) here would
  stop at a true observation that explains nothing.

RULED OUT:
- That a stage carries no contract at all (family 4): both stage contracts carry Inputs,
  Process and Outputs.
- That a declared input is produced by nothing (family 12): every declared input resolves, and the graph
  reports no dangling reference.
- That setup never finished and placeholders are still in the files (family 10): none outside templates.
- That the same fact has two homes that disagree (family 11): no duplication cluster is reported. The voice
  rules have exactly one home. It is the wrong one, which is the entry file carrying content it should only point at (family 1).
- Layer 7, the content of the reference material: the specific rules are
  unambiguous and were applied nowhere. A rule that is clear and unapplied is a
  routing question, not a wording one.

CONTRIBUTING FACTORS: The write stage contract has no human check where the
gather stage contract has one. Subordinate, and deliberately so: the missing
gate governs when the owner sees the output, not what the writing step had in
front of it.

WEAKEST LINK: Link 5, which is `[inferred]`. The transcript shows the reads the
agent made explicitly and does not show the auto-loaded entry file, so the claim
that the rules arrived at all rests on how the runtime loads an entry file
rather than on an observation in this run. The conclusion survives it because
links 1 to 4 establish that no contract routes to the rules, which holds whether
or not the entry file reached that turn.

CONFIDENCE: high

WHAT WOULD OVERTURN THIS:
- A transcript of this workspace in which the write step reads a file carrying
  the specific voice rules and still produces the same opening. That moves the
  finding to layer 7.
- A run of `mine.py` reporting a contract input that resolves to the voice
  rules, which contradicts link 2.
- The owner confirming the entry file was not loaded in that session, which
  breaks link 5 and reopens the ranking against section routing (family 6).

> *This finding was produced by an AI system from the evidence listed above. It
> names a cause only and proposes no change to the workspace. Conclusions are
> bounded by that evidence.*
