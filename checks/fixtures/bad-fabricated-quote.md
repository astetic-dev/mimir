DIAGNOSIS: The voice rules live in the entry file, so no stage contract can
route to them.

EVIDENCE TIER: B - the workspace tree, mined.

EVIDENCE CHAIN:
1. [seen] `CLAUDE.md` is 135 lines against an entry-file limit of 60 -> the
   entry file carries content.
2. [seen] Its headings include "Editorial standards for the house voice" -> the
   content is the voice rules.
3. [inferred] No stage contract names that file -> the rules cannot be routed to
   a step.

WHY IT STOPS HERE:
- Deeper step tested and rejected: "the builder did not know the guardrail".
  Remove it: the guardrail was known. The failure still requires these rules to
  sit in this file.
- Shallower step passed over: the contract could have named a section of the style guide instead of the whole file (family 6). The routed guide is
  22 lines, so a section scope changes nothing.

RULED OUT:
- That a stage carries no contract at all (family 4): both stage contracts carry Inputs, Process and Outputs.
- That setup never finished and placeholders are still in the files (family 10): none outside templates.

CONTRIBUTING FACTORS: none

WEAKEST LINK: Link 3 is `[inferred]`. It survives because the mined contract
inputs are complete.

CONFIDENCE: moderate

WHAT WOULD OVERTURN THIS: A contract input that resolves to the voice rules
contradicts link 3.

> *This finding was produced by an AI system from the evidence listed above. It
> names a cause only and proposes no change to the workspace. Conclusions are
> bounded by that evidence.*
