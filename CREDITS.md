# Credits

Mimir is a combination before it is an invention. Five diagnosticians were read
end to end - doctrine, reference, test machinery and defect logs - and the thing
that made the combination worth building is that **each one's gap is filled by
another one's strength.**

Credit travels with the idea. Each line names the idea, whose it is, and where
in this folder it is used.

## The five

| Idea | From | Where it is used here |
|---|---|---|
| **The stranger is the product.** A separate intake file that walks a non-expert to the evidence one instruction at a time, checking each answer before building on it. | Colm Whelan, *Inbox Autopsy* | `intake.md`, whole. The branch table and the "never float a theory during intake" rule are his shape. |
| **Grade the evidence before trusting it, and say which tier you are on.** | Colm Whelan, *Inbox Autopsy* | `reference/evidence-grades.md`; `EVIDENCE TIER` is a required section of every finding. |
| **Walk the causal layers in a fixed order, with the most-accused layer last.** Content is the most blamed and least often guilty. | Colm Whelan, *Inbox Autopsy* | `rules.md` step 5 and layer 7 of `reference/cause-taxonomy.md`. In this domain the most-accused layer is "the rules are not clear enough". |
| **The output format has no field a fix could live in**, and the fix request arrives in disguises that must be named. | Colm Whelan, *Inbox Autopsy* | `reference/output-contract.md` 4; `reference/disguised-asks.md`. |
| **Mark every link: `[seen]` / `[inferred]` / `[general]`, and `[seen]` only if you can point at it.** | Sergey Manevitch, *Radix* | The `MARKED` gate, the markers in `identity.md` and `reference/output-contract.md`. His tokens, his words. |
| **Put the marker tokens in `identity.md`, not only in `rules.md`.** A partial load once produced correct discipline in a private language. | Sergey Manevitch, *Radix* | `identity.md` carries the tokens as well as the obligation, for exactly that reason. |
| **A gate asks. A gate never blocks.** Never end a turn on questions; state the assumption and carry the question into the finding. | Sergey Manevitch, *Radix* | `rules.md`, stated once at the top and binding at all nine steps. He found this rule by testing, not by design. |
| **Descend by necessity, and name both neighbours of where you stopped.** The rejected step below and the shallower step above, with the reason. | Sergey Manevitch, *Radix* | `rules.md` step 6; `WHY IT STOPS HERE` is a required section. The shallower neighbour is usually the one everybody else would have named. |
| **Rank by persistence: the cause that survives the obvious repair** - and test every candidate against *the same* repair, or the rule inverts into a tautology. | Sergey Manevitch, *Radix* | `rules.md` step 7. |
| **Name your own weakest link, first.** | Sergey Manevitch, *Radix* | `WEAKEST LINK`, a required section. |
| **For each evidence source: what it proves, what it does NOT prove, and its traps.** | Sergey Manevitch, *Radix* | The shape of `reference/evidence-grades.md`. |
| **Never stop at a person.** Behind almost every human error is a system that made it likely. | Sergey Manevitch, *Radix* | Doubled here: never stop at the owner, and never stop at the model. |
| **The discriminability gate.** One cause only when the evidence channel can actually show that mechanism, and the strongest alternative is contradicted or explains less. | Pemmy Broke, *Visual Momentum* | `rules.md` step 7. Her evidence-channel clause is why a claim about what an agent *loaded* requires a transcript. |
| **Localisation is not discrimination.** | Pemmy Broke, *Visual Momentum* | `rules.md` step 7. "It always fails at stage 03" chooses between nothing. |
| **`UNRESOLVED` is a result, not a failed run - and confidence language may not disguise a tie.** | Pemmy Broke, *Visual Momentum* | `reference/output-contract.md` 5.4; the `ABSTAIN` gate. |
| **A bounded ontology with an `OUT-OF-TAXONOMY` escape.** Do not force-fit; say the ontology is the limit. | Pemmy Broke, *Visual Momentum* | `reference/cause-taxonomy.md` and contract 5.5. |
| **A declaration is not an event.** A declared action proves only that the declaration exists. | Pemmy Broke, *Visual Momentum* | `reference/evidence-grades.md`: a model saying "I have read the design system" is a sentence, not a read. |
| **Runtime and evaluation are different file sets, and the separation is enforced.** | Pemmy Broke, *Visual Momentum* | The Load / Read / Verify table in `TESTING.md`, and `verify.py --manifest`. |
| **Preserve the failing run.** Publish the run that broke your own doctrine, fix the doctrine, keep both. | Pemmy Broke, *Visual Momentum* | `DEFECTS.md` C1-C11: every entry names the test that found it. |
| **Commit the prediction before the run exists.** | Marcelo Michelsohn, *Why This Conversation Drained Me* | Every `eval/cases/*/expected.md`, written before any run. |
| **Frozen return texts.** A fixed string is mechanically testable; an improvised paraphrase is not. | Marcelo Michelsohn | The five frozen returns in `reference/output-contract.md` 5. |
| **"Nothing to diagnose" is distinct from "not enough evidence"** - and a tool that always finds something teaches its owner to distrust the healthy cases. | Marcelo Michelsohn | `NO-FAILURE` vs `INSUFFICIENT-EVIDENCE`; eval case 02 exists to test it. |
| **A counterfactual is advice wearing the past tense.** | Marcelo Michelsohn | `reference/disguised-asks.md` shape 7, and the counterfactual arm of the `NO-RX` gate. No checker in the field catches this; here one does. |
| **Character-for-character quoting, and every concrete detail from the source even outside quote marks.** His OD-G: an invented "Saturday" in the diagnostician's own prose escaped a quote-only check. | Marcelo Michelsohn | `GROUNDING` extended to unquoted paths and numbers - the `CITATIONS` gate. |
| **The answer ends where the contract ends.** His OD-E, recurring: the model appends a closing paragraph that reads well and is still a field the structure does not have. | Marcelo Michelsohn | The `NO-APPENDIX` gate. Colm logged the same defect as D3 and neither closed it in code. |
| **Confess defects in a dated log, with the check that now catches each one.** | Marcelo Michelsohn | `DEFECTS.md`, structure and spirit. |
| **The script computes, the model labels.** Every citable number comes from a deterministic miner; the arithmetic cannot drift because it was never the model's. | Craig Howard, *JS/TS Regression Historian* (crediting Greg Faysash) | `checks/mine.py`. This is the single largest borrowing in the folder. |
| **A must in markdown is a request; a must in code is a constraint.** | Jodi Paige-Lee, via Craig Howard | `checks/verify.py` exists at all. |
| **Citations must resolve, or the claim is cut.** A fabricated citation fails mechanically however well it reads. | Craig Howard (crediting Alex Brown) | The `CITATIONS` gate. |
| **The self-tested gate:** good and bad fixtures, each bad one blocked on its own named check. | Craig Howard (crediting Gabriel Azoulay) | `verify.py --selftest`: 1 pass, 9 named fails. Extended here to the miner: `mine.py --selftest`. |
| **A numeric signal floor, below which declining is a pass.** | Craig Howard | The signal floor in `reference/cause-taxonomy.md`; eval case 03 tests it. |
| **The cause-versus-symptom translation table, with a forbidden middle column.** | Craig Howard | `reference/cause-vs-symptom.md`, his three-column shape exactly. |
| **The loudest number is where a cause surfaced, not why.** | Craig Howard | `reference/cause-vs-symptom.md`, "The trap". |
| **Each taxonomy entry carries its fingerprint and what it is mistaken for.** | Craig Howard | The shape of every family in `reference/cause-taxonomy.md`. |
| **Credit travels with the idea.** | Craig Howard | This file. |

## Also drawn on

**Cassini** (Arjen Stet, comp 11) declines *Diagnosis* by name and in writing:
"a cause is a claim about the past and needs logs and a timeline it has not
asked for." Mimir is the other side of that boundary, and Cassini's insistence
that the reader is often a model with a small context window shaped the decision
that findings are markdown a text search can audit.

**The method itself** is Van Clief and McDermott, *Interpretable Context
Methodology: Folder Structure as Agent Architecture* (arXiv:2603.16021, MIT),
with `RinDig/icm-architect` and `_core/CONVENTIONS.md` as the working canon. Every
cause family in `reference/cause-taxonomy.md` is derived from an invariant, a
pattern or a principle in those documents. Mimir has no theory of his own about
what a good workspace is; he only knows what the method says one is.

## What is new here

Five things, as far as the reading went, exist in none of the five:

1. **`MARKED` in code.** Radix's marker discipline verified by a script rather
   than by sampling, which is how he verified it and said so.
2. **`GROUNDING` extended past the quote marks** to paths and numbers in the
   diagnostician's own prose - Marcelo's OD-G, which he could only close with a
   sentence in a contract.
3. **A counterfactual detector.**
4. **`NO-APPENDIX`.** The same defect is open in two of the five repositories.
5. **`ABSTAIN` consistency:** `UNRESOLVED` must name its tied candidates by
   number, and a named cause may not also claim `UNRESOLVED`.

And one thing the domain made possible rather than the design: **Mimir is himself
an ICM workspace, so his own miner runs on him.** That test found seven of the
eleven closed defects in `DEFECTS.md`.

Thank you all.
