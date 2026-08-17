I read the folder. It is a specialist-shaped workspace, `identity.md` and `rules.md` at the root, and what you describe is a real event with a real artifact behind it, so there is something here to diagnose.

Two things before the finding.

I have the tree and I do not have your run. That is tier B: I can prove what the folder says and I cannot prove what your agent did with it. Your account of the run is the only evidence I have for the behaviour, and I mark every place I lean on it.

The question I have to ask, because it changes what I am looking at: has this folder been edited since the answer you are describing, and has this happened to you before on it? A folder edited after the run is not the folder that failed, and a repair that did not hold is the strongest evidence I get. I am proceeding on the assumption that nothing material has changed since, and the finding says which link rests on that.

There is one failure in what you sent, not several, so there is nothing to split.

One more thing, and it is the reason the finding is shaped the way it is:

*The evidence supports a mechanism that none of my bounded cause families describes. The limit here is my taxonomy, not your evidence.*

DIAGNOSIS: The finding is a closed form of nine named sections, and none of them is a place to record what the diagnosis was scoped to, so the scope decision can only be delivered at the conversational gate, which is not the thing you keep. The absence is not an oversight in the section list: `rules.md` step 3 separately forbids the set-aside from appearing in the finding at all.

EVIDENCE TIER: B - the workspace tree, mined by `checks/mine.py`, with no transcript of the run. B is the tier where structural claims are provable and behavioural ones are inferred; my cause is structural, and the one behavioural claim is yours, marked where it appears.

EVIDENCE CHAIN:
1. [seen] `reference/output-contract.md` opens by defining the answer as "Nine sections, each exactly once, in this order, with these names." and the list that follows runs from the diagnosis to what would overturn it -> the artifact is a closed form, and scope is not among the things it has a place for.
2. [seen] The same file says of everything it excludes: "There is no field in the contract where these could live" -> a section the form does not name is not available to carry the scope decision either.
3. [seen] `rules.md` step 3 says of the failures not chosen: "What is set aside is not diagnosed, not alluded to, and not smuggled into the finding." -> the exclusion is stated outright, so the silence in the artifact is by construction rather than by omission.
4. [seen] The same step puts the scope statement somewhere else instead: "and name the others as set aside", said at a gate, and a gate is defined a few lines earlier as "Put the question in front of the owner" -> the saying happens in the reply, on the conversational channel.
5. [seen] The workspace ships the matching pair. In `examples.md` the scope statement sits in the spoken turn - "The gather step is out of scope and I am not diagnosing it." - and the finding that turn introduces, `checks/fixtures/good-finding.md`, carries no equivalent anywhere in its nine sections -> the split you experienced is reproduced in the workspace's own reference material.
6. [inferred] From links 1, 2 and 3: a writer at the last step has made a scope decision, is told not to put it in the finding, and has no section to put it in -> the only channel left is the surrounding conversation.
7. [general] A conversational turn is discarded and an artifact is filed; that asymmetry is why the choice of channel decides what survives. [general - not measured in this tree]

WHY IT STOPS HERE:
- Deeper step tested and rejected: that the doctrine conceives scope as something negotiated with the owner rather than as a property of the finished finding. Remove it: suppose scope is conceived from the start as a property of the finding. Does that require this section list to contain a place for it? No. A form is a list of names somebody wrote down, and a designer holding either conception can still write down exactly these nine. The failure still requires this particular list to omit it. Not necessary, so I stop above it.
- Shallower step passed over: the sentence in `rules.md` step 3 that the set-aside is not to be alluded to in the finding. It is the loud line and the one most readers name first, and it is true. Remove it: the sentence is gone, and a writer who wants the scope on the record still meets a list of nine named sections, a rule that nothing may be added to an answer beyond what that file defines, and a prohibition on anything after the closing line. The record still has nowhere to land and the failure still occurs, so that sentence restates the exclusion rather than creating it.

RULED OUT:
- That the entry file is carrying the rules themselves instead of pointing at them (family 1): the miner reports an empty routing-payload list, and `CLAUDE.md` is 43 lines against the 60-line entry cap the taxonomy cites.
- That the same fact has two homes that disagree, so the agent quotes whichever it loaded (family 11): the miner reports no duplication cluster at all.
- That a step reads a path nothing produces (family 12), or that files sit in the tree with nothing pointing at them (family 13): the miner reports no orphans, and the unresolved names it does report are illustrative filenames inside prose and citations of the ICM canon that lives outside this folder, not live reads at a step.
- That nothing in the workspace stops for a person (family 17): the reverse holds here. `rules.md` says "Nine steps. Each ends with a gate." and the gate fired - you were told, at the time, clearly. Where the telling landed is the complaint, not whether it happened.
- That setup never finished and placeholders still stand where facts belong (family 10): the miner reports 16 outside templates, and its sample places them in the port-this-machine document and in two taxonomy entries that quote a placeholder as an example of one. None of them sits where a step needs a fact.
- The content of the doctrine itself, which is the layer walked last and the one most owners suspect first: the doctrine is not vague here. It is precise, and it precisely excludes the thing you wanted kept.
- And the four that come nearest to describing the mechanism itself, each of which I have to reject by name. The wall between stable reference material and per-run artifacts (family 8) is nearest in spirit, being the family about the boundary between what configures a machine and what a run emits; it fails because it describes the two mixing in one place, where here they are cleanly separated and the fault is the opposite shape - a fact the run produces has no place in the run's own artifact - and its fingerprint is gated on pipeline-shaped workspaces, which the miner reports this one is not. A chain that breaks at a named joint (family 12) is nearest in shape; it fails because it describes a read that resolves to nothing, where this break runs the other way, with step 3 producing a fact that no later step declares as an input. Nothing stopping for a person (family 17) is nearest in subject, since the gate is where the decision was spoken; it fails by being the inverse of what happened. The entry file carrying content instead of routes (family 1) is nearest in consequence, since both end with material reaching the reader on the wrong channel; it fails because nothing here is misfiled inside the folder, the material simply never entered the artifact.

CONTRIBUTING FACTORS: Two, both subordinate. First, the gate discipline near the top of `rules.md` tells the agent to "carry the question into the finding", while step 3 tells it the set-aside is not to be alluded to there; the two pull opposite ways, which is why the outcome reads as deliberate in the moment and accidental in the artifact. It stays below the primary cause because even the instruction that pulls toward the finding names no section to land in. Second, `rules.md` step 8 lists what the writing step works from - "Working: the ranked cause, the killed branches, the inventory." - and the scope decision made at step 3 is not among them, nor named as an input by any step in between. Also subordinate: carried forward, it still meets a form with no section for it.

WEAKEST LINK: The weakest thing here is not a numbered link, it is the claim that no bounded family covers this, which is a judgement about where my own filing system ends rather than an observation of your folder. The families in `reference/cause-taxonomy.md` all describe how a workspace routes and loads context into a step; this is a fault in what the workspace's deliverable is required to record, which is a different axis. A reader who finds that close enough to the wall between stable material and per-run artifacts (family 8) has a real argument, and the paragraph above is where I answer it rather than where I settle it. The conclusion survives it because the mechanism does not depend on the label: the closed section list, the rule against adding to it, and the workspace's own paired example stand whether or not the fault carries a family number.

CONFIDENCE: high

WHAT WOULD OVERTURN THIS:
- The limiting factor here is my own ontology, and that is the first thing that moves it: a family in `reference/cause-taxonomy.md` that does describe an artifact schema with no field for a decision the process requires. That turns this from a gap in my taxonomy into an ordinary finding filed under that family, and the mechanism below it stays as written.
- A section of `reference/output-contract.md` that names a place for the scope decision and that I have read past. Check the nine section names against your own copy first; if one of them is meant to carry it, link 1 falls and the rest with it.
- A finding produced by this workspace that does carry its own scope inside the nine sections rather than in the turn around them. That contradicts link 5.
- Your transcript of the run you are describing, whole, from your first message. It shows whether the split you saw came from step 3 as written or from something else in that session, and I am reasoning about that step from the doctrine rather than from your run.

> *This finding was produced by an AI system from the evidence listed above. It names a cause only and proposes no change to the workspace. Conclusions are bounded by that evidence.*
