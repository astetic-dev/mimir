# DEFECTS - dated, and kept rather than polished away

Defects found in this folder, confessed here instead of tuned out. Closed
entries stay: the history of a fix is part of the evidence.

Nothing in this file is loaded into Mimir. It is for a reader auditing the
build.

Structural limits that no fix would close are in `BLIND-SPOTS.md`.

---

## Open

**D1 - `rules.md` is 406 lines (2026-08-16).** The ICM guardrail for a reference
file is 200 lines, and for a `CONTEXT.md` it is 80. `rules.md` is neither: it is
the method, and it is the file a step reader loads every time. It is still long,
and a cold reader meets 406 lines before they meet a worked example.

Two options were weighed. Splitting the standing obligations and prohibitions
into a fourth doctrine file would bring `rules.md` to about 300 lines and would
mean every step now loads two files instead of one, which is the cost the
layered-loading principle exists to avoid. Leaving it means the control point is
long.

It is left, deliberately, and recorded here with the number rather than
defended in prose. If a behavioural run shows a step being skipped or a rule
being missed in the back half of the file, this entry becomes the first
suspect - and `TESTING.md` B6, the smaller-model-tier run, is where that would
show up first.

**D2 - the self-mine reports 15 unresolved placeholders (2026-08-16).**
`mine.py` reports `placeholders.outsideTemplates: 15` - nine in `BUILD.md`
(`{{PATIENT}}`, `{{TAXONOMY}}`, `{{MINER}}` and the rest), three in this file,
and three in `reference/`.

**Examined and acquitted.** The `BUILD.md` ones are documentation of the chassis
slots, in a file that is in the Read set and never in the Load set. The three in
`reference/cause-taxonomy.md` and `reference/cause-vs-symptom.md` are worked
illustrations of the family 10 fingerprint, which is a diagnostician quoting the
thing it diagnoses.

That last group is the one worth naming out loud: **three of these fifteen sit
in the Load set.** They are inert - no agent is going to substitute a value into
an example - but a doctrine file containing the literal string it teaches you to
hunt for is a real, if small, way to be misread, and pretending otherwise here
would be exactly the move this file exists to refuse.

It is left visible rather than exempted, for two reasons. Hardcoding `BUILD.md`
into the miner's exemption list would put one folder's filename into a general
tool. And a fingerprint that fires and is argued down in writing is a better
demonstration of the discipline than one that was quietly configured away: a
fingerprint match is a candidate, not a finding.

**D3 - three folder-level back-references (2026-08-16).** Root and `reference/`,
root and `checks/`, `checks/` and `reference/`. Pattern 3 says every folder
points outward and no folder points back. `rules.md` names which reference file
loads at which step, and the reference files name the step that reads them. That
is a cycle at the folder level and the miner reports it.

**Examined and acquitted, with the reason.** Family 14's actual harm is that no
subtree can be loaded without pulling the rest. It does not apply here: the file
being pointed back at is `rules.md`, which is loaded in every run regardless, so
the back-pointer costs nothing at load time and buys a reference file that can
be read on its own. Radix encodes the same relationship in frontmatter
(`read_by: rules.md stage 4`), which is the same edge wearing different clothes.

The miner was changed rather than the folder: it now reports back-references at
both the file and the folder level, because Pattern 3 is written about folders
and file-level mutual links within one layer are the documented ICM shape. See
C7.

**D4 - no run by an independent reader (2026-08-16, narrowed 2026-08-17).**

*Original wording, kept because a defect log that quietly rewrites itself is not a log:* "no
behavioural run has happened. Eight rows in `TESTING.md` are `PENDING`. The deterministic gates
are proved; diagnostic judgement is not."

**What changed on 2026-08-17.** B1 to B7 ran in fresh contexts. Six passed, B6 found the right
cause and failed the run, and between them they surfaced six defects. Diagnostic judgement is no
longer wholly unproven.

**What is still open, and it is the whole of what remains.** Those runs were fresh contexts and
**not independent readers**: same model family, every prompt written by the author of the
doctrine and the answer keys. B8 - a person who did not build this, five minutes, `README.md`
only - has not happened, and it is the one row that cannot be filled in from inside this folder.

This entry stays open until B8 runs. It is no longer the largest gap; it is the last one of its
kind.

**D10 - the falsifier section is a loophole for remedies (2026-08-17).** `WHAT WOULD
OVERTURN THIS` is meant to carry evidence acts. A remedy phrased as a hypothetical experiment
lands there untouched, because `NO-RX` is looking for instructions and this arrives as a
proposed observation.

Found in run B6, whose falsifier reads: *"Show me a run of June where stage 03 is told to read
June's findings and a reference on brand standards (not a previous output) as its template."*
That is the repair, wearing the clothes of a test. It passed all nine gates.

The line the doctrine draws is that an evidence act asks a question about the world and a remedy
changes it - so *"show me a run where the contract was different"* is on the wrong side of it,
and neither the gate nor `reference/disguised-asks.md` currently says so. Open because the fix is
not obvious: the legitimate form of that falsifier (*"show me a run that read the exemplar and
carried the finding anyway"*) is grammatically near-identical.

**D11 - four of the five frozen returns are ungated (2026-08-17).** `checks/verify.py` only knows
the nine-section shape. `OUT-OF-SCOPE`, `NO-FAILURE`, `INSUFFICIENT-EVIDENCE` and
`OUT-OF-TAXONOMY` returns are not nine-section findings, so running the checker on one fails on
`FORMAT` and tells you nothing. In practice they are never checked at all.

Two of the eight blind runs (B2, B3) returned frozen texts, and neither could be gated. Both were
scored by reading. Related contract gaps the same runs exposed: `output-contract.md` does not say
whether a special return carries the closing line (B2 omitted it), nor whether a preamble may
precede the frozen text (B2 and B3 both wrote one), nor - for `NO-FAILURE` - it permits "one
sentence" and B2 wrote five.

**D12 - two eval fixtures claim outputs their trees do not contain (2026-08-17).** Case 01's
transcript ends with a June report that stage 03 declares as `output/2026-06-report.md` and that
is not in the folder. Case 02's transcript says *"Action list written."* and
`stages/02-actions/output/` holds only `.gitkeep`. Same flaw, two cases, written the same
afternoon by the same person.

Both were found by the runs, not by the author and not by the miner: B1 named case 01's as a
second failure it was setting aside, and B2 named case 02's as the single thing that would
overturn its own answer. Neither fixture is being repaired - see
`eval/cases/02-healthy-with-a-gate/FIXTURE-DEFECT.md` for why. Kept open because the pattern is
the author's, not the fixture's: a transcript is easy to write and a tree is work, and the
mismatch is invisible until something reads both.

**D6 - the finding has no field for what was set aside (2026-08-17).** `rules.md` step 3
requires scoping exactly one failure and produces "the failure under investigation, in one line,
and an explicit list of what is set aside". `reference/output-contract.md` defines nine sections
and **none of them is that list.** So the scope decision is either dropped, or smuggled into
`DIAGNOSIS`, where `ONE-CAUSE` caps it at four sentences.

Found by applying Mimir to `porter-intake-operator`, which contained two distinct failures. The
split had to be reported outside the finding, in ordinary prose, which is exactly the kind of
thing that stops being reported once nobody is watching. Radix has this field; Mimir dropped it
when the contract was compressed from Radix's seven-part shape to nine sections.

**D8 - CLOSED 2026-08-17, same day, as family 20.** The gap below was real and is now
`reference/cause-taxonomy.md` family 20, "the contract omits what the step needs". The original
entry is kept because the way it was found is the point: the escape hatch fired twice on real
workspaces before anyone thought to look for a missing family, which is the escape doing exactly
the job it was built for. What remains open is the worry in the last line of the entry - a hole
found by the first two real cases is unlikely to be the last one - and that now lives in
`BLIND-SPOTS.md` rather than here.

*Original entry:* The taxonomy has no family for contract sufficiency. Layer 2 of
`reference/cause-taxonomy.md` covers the *shape* of a contract: does it exist (4), does it name
paths (5), does it scope sections (6), is the load in band (7). It has no family for whether the
**named inputs are the right ones** - whether the step's declared inputs include the material the
step's output requires.

Found on the first real workspace Mimir was pointed at. The porter case returned
`OUT-OF-TAXONOMY` for exactly this: a drafting step whose inputs name the templates and the tone
and never the project state. The nearest three families each fail on a stated ground - 5 is about
an input named vaguely, 6 about an input routed coarsely, 8 about the two layers being mixed -
and the observed mechanism is a step that reads only the factory and never the product.

The escape hatch worked, which `BLIND-SPOTS.md` said was unproven. It is now exercised once, on a
real folder. That is the good news. The bad news is that a hole found by the first real case is
probably not a rare hole.

**D9 - the five frozen returns exist only in English (2026-08-17).** `output-contract.md` 6 says
the answer is written in the owner's language, and 5 freezes five return texts so a checker can
match them. Those two rules collide for every owner who does not work in English: either the
frozen text is returned in a language the owner does not use, or it is translated and stops being
frozen. Marcelo's original froze each text in two languages for this reason; Mimir froze one.

**D5 - the counterfactual gate cannot read a conversation (2026-08-16).**
`verify.py` catches advice-in-the-past-tense inside a written finding and is
blind to the same sentence in the surrounding chat, which is exactly where an
owner asks for it directly. Covered by a human test only (`eval/refusal` turn 3).
A checker that could read a live turn and validate it against the contract would
close this. It does not exist.

---

## Closed - found by the build's own tests

**C16 - the remedy gate punished the doctrine (found and fixed 2026-08-17, by run B4).**
`reference/disguised-asks.md` instructs Mimir to name what he is declining and say who owns it.
`NO-RX` was looking for remedy phrases and could not tell naming one from offering one, so B4's
refusal - *"The target tree and 'just tell me which file to move' are the same request in two
sizes, and both are repairs"* - failed the gate for obeying the doctrine.

Fixed with a refusal exemption per language, scoped to the sentence, so a remedy sitting in its
own sentence beside a refusal in another is still caught. `fixtures/bad-laundered-remedy.md` is
the regression: it declines a target tree in one sentence and prescribes the move in the next,
and must still fail. The same exemption was extended to the counterfactual arm for the same
reason.

**A deliberate limit on that fix.** B4's third turn writes *"it does not get to say what would
have avoided it"*, stating the prohibition rather than committing it, and the counterfactual arm
still flags it because the refusal marker is in the previous sentence. That is left flagged.
On this gate a false positive costs a rewrite and a false negative costs a laundered remedy, so
it errs toward flagging, and widening the exemption until it caught every way of phrasing a
prohibition would eventually launder the thing it exists to catch.

**C17 - the scoring harness could not ground a transcript quote (found and fixed 2026-08-17, by
runs B1, B4 and B7).** Three findings failed `GROUNDING` on quotes that were correct. The
transcript they quoted existed only inside the run's prompt and was never written to disk, so the
checker was asked to ground a quote against evidence it had not been given.

The runs were right and the harness was wrong, which is the more dangerous direction: a scoring
setup that fails good work teaches you to loosen the gate. Fixed by shipping the case transcript
as `eval/cases/01-outputs-as-templates/transcript.txt`, so the suite is re-scorable by someone
who was not in the room.

**C14 - the finding spoke the engine's vocabulary at the reader (found and fixed 2026-08-17, by
the owner reading a finding).** The three findings delivered on 2026-08-17 cited cause families
by number. The owner's response was: *"ik zie steeds: familie 8, familie 3.. ik snap er helemaal
niets van."*

That is the whole product failing at the last inch. The reader owns the failure; they do not own
the taxonomy, and a label is not an explanation. Worse, the folder **required** it: the `ABSTAIN`
gate checked for `family \d+`, so a gate written to enforce honesty was mandating the exact
jargon that made the finding unreadable.

Fixed in three places. `output-contract.md` gained section 3b: the cause is stated in the
reader's words and the index rides in brackets afterwards, never the label alone and never the
label first. `verify.py` gained a ninth-and-a-half gate, `PLAIN`, which fails any bare
`family N` in either language. `ABSTAIN` no longer demands the bare form.
`fixtures/bad-jargon.md` is the regression; the selftest is now 12.

**The three delivered findings stay exactly as returned** and all three now fail `PLAIN` - eight
violations in the first, three in the second, five in the third. They are the evidence for this
entry, and a corrected re-run would erase it.

The lesson is not "add a gate". It is that every check in this folder was written by someone who
already knew what the words meant, and the one thing none of them tested was whether the answer
lands. This defect was found by a reader in one sentence, and by no test.

**C15 - the remedy word lists were English only (found and fixed 2026-08-17, by the owner).**
`output-contract.md` 6 says the finding is written in the owner's language; `RX_PATTERNS` and
`CF_PATTERNS` were English regexes. A Dutch finding therefore passed `NO-RX` **vacuously** -
"je moet dat bestand verplaatsen" matched nothing. All three findings of 2026-08-17 were Dutch
and all three "passed".

This was first logged as an open limitation. The owner rejected that framing: input language,
output language and engine language have to agree, and a rule that says one thing while the gate
does another is an incoherence, not a limitation. He was right, and the entry was the wrong shape
before it was the wrong content.

Fixed by giving each supported language its own remedy, counterfactual and evidence-act lists,
selecting by stopword detection, and - the part that matters - **failing loudly when the finding
is in a language with no list**. A gate that passes what it cannot read issues a receipt it has
not earned, which is worse than having no gate at all.

**C12 - GROUNDING could not see a quote that wrapped (found and fixed 2026-08-17, by the first
real diagnosis).** `MARKED` and `GROUNDING` walked the evidence chain line by line, and the quote
regex excluded newlines. A quoted span that wrapped across two lines was therefore **not checked
at all** - not failed, not flagged, simply skipped.

Caught by accident: the first real finding reported "2 quotes grounded" where it carried five.
Only the two short enough to fit on one line had been checked. A fabricated quote could have
escaped this gate by being long, which is the opposite of the property a grounding gate needs.

Fixed by treating a chain link as a numbered line plus its continuation lines, flattened before
the quotes are extracted. `fixtures/bad-wrapped-quote.md` is the regression: a fabricated quote
that wraps, which must fail on GROUNDING. The selftest is now 11 fixtures.

This is the same defect class as C9 and C10 - a pattern written against one line in a contract
whose prose wraps constantly - and it is the third time it has been found. That it keeps
recurring is itself the finding: line-oriented matching is the wrong default here, and every
remaining line-oriented check in `verify.py` should be read with that in mind.

**C13 - stripping quoted spans desynchronised on a wrapped quote (found and fixed 2026-08-17, by
the first real diagnosis).** `strip_quoted` blanks quoted material so an owner's words are not
scanned as Mimir's. Its pattern also excluded newlines, so when a quote wrapped, the closing
quote mark on the next line paired with the *following* opening quote mark, and the checker
blanked the gap between two quotes while leaving the second quote's contents exposed.

The visible effect was a false `NO-RX` failure: text inside a quotation from the diagnosed
workspace was scanned as if Mimir had written it. The invisible effect is worse and is why this
is logged rather than shrugged at - the same desynchronisation can blank a real remedy, and a
gate that fails open is a gate that lies.

Fixed by allowing the span to cross a newline. Found the same way as C12, in the same finding, on
the same underlying assumption.

Every entry below was found by a test, not by reading. Each names the test that
found it, because a defect log without that is a list of things somebody
happened to notice.

**C1 - the miner walked into nested workspaces and merged them (found and fixed
2026-08-16, by T5).** Running `mine.py` on Mimir returned
`form.guess: pipeline, why: 10 numbered stage folders`. Mimir has no stages. It
had walked into `eval/cases/*/workspace/` and counted six other people's
workspaces as its own. Every downstream number was measuring a union of seven
trees.

Fixed by `.mimirignore`: one path prefix per line, read from the workspace root.
Chosen over a hardcoded skip list because "skip anything called eval" is an
assumption about other people's folders.

**C2 - the routing-payload heuristic fired on the doctrine (found and fixed
2026-08-16, by T5).** The self-mine reported `identity.md`, `intake.md` and
`rules.md` as routing files carrying payload. They are the method. A specialist
folder's `rules.md` is L2 and is *supposed* to carry content, and measuring it
against a `CONTEXT.md` guardrail produces a confident wrong finding about the
most important file present.

Fixed by scoping the heuristic to files whose job is routing: entry files and
`CONTEXT.md`. This is the defect that would have hurt most in the field, because
almost every Taurus agent is in specialist form.

**C3 - backticked commands were mined as broken links (found and fixed
2026-08-16, by T5).** `` `python checks/mine.py <workspace-path>` `` was
resolved as a path and reported dangling. Fixed by rejecting backticked spans
containing whitespace: ICM naming forbids spaces in file and folder names, so a
span with one is a command.

**C4 - prior run outputs were reported as orphans (found and fixed 2026-08-16,
by the eval case 01 mine).** Two earlier monthly reports in a stage's `output/`
folder came back as `graph.orphans`, which points at family 13, ghost wiring. A
run artifact that nothing points at is the normal state of a product folder.
Fixed by excluding L4 from the orphan set. The signal that an output is being
*used* as reference is `declaredInputs[].fromOutput`, which is where family 9
should read it.

**C5 - an un-run stage was reported as a broken handoff (found and fixed
2026-08-16, by the fixture mine).** A stage's Outputs table names
`output/post.md` before the stage has ever run, and the miner reported it as
`graph.dangling`, which points at family 12. Fixed: declared outputs that do not
exist yet are moved to `graph.declaredOutputsNotYetProduced`. The fact is still
carried by `outputFolder.fileCount`.

**C6 - SCREAMING-CASE root documents were flagged as naming drift (found and
fixed 2026-08-16, by T5).** `BUILD.md` was reported as violating
lowercase-with-hyphens. README, LICENSE, TESTING and their kin are a near
universal convention. Fixed with a rule rather than a list: an all-caps stem is
conventional. Real violations were being buried in that noise.

**C7 - back-references were only reported at the file level (found and fixed
2026-08-16, by T5).** The self-mine reported 11 file-level cycles, which read as
a serious Pattern 3 violation. Pattern 3 is written about folders. Fixed by
reporting both levels; the taxonomy convicts on the folder level. See D3.

**C8 - backticked paths were excluded from the link graph (found and fixed
2026-08-16, by T1).** The miner's own selftest failed on the healthy tree: a
correctly wired workspace reported orphans. Inline code had been stripped before
hunting paths, to avoid mining fenced examples - but fenced blocks were already
skipped, and inline code is exactly where ICM contracts keep their paths
(`_core/CONVENTIONS.md` Pattern 1). The healthy-tree half of the selftest is
what caught it; the broken-tree half was passing throughout.

**C9 - `NO-RX` missed any remedy that wrapped across two lines (found and fixed
2026-08-16, by T2).** `bad-prescription.md` passed clean. The fixture says "You
should\nadd one", and the patterns had a literal space between the modal and the
verb. Fixed by scanning a whitespace-flattened copy. Prose in this contract
wraps constantly, so this was not an edge case; it was most of them.

**C10 - the evidence-act allowlist laundered remedies (found and fixed
2026-08-16, by T2).** After C9, `bad-prescription.md` still passed. The
allowlist exempted any nearby sentence containing "check" - and **"Human check"
is a section name in every ICM stage contract**, so the allowlist exempted
roughly every remedy in the domain. Fixed twice over: the verbs were narrowed to
unambiguous evidence acts (`would confirm`, `check whether`, `look up`, `re-run`)
and the exemption was scoped from a 140-character window to the sentence the
match sits in, so a legitimate evidence act two sentences away can no longer
launder a remedy.

This is the defect this folder is least comfortable with. A domain-specific
word appearing in a general allowlist is exactly the failure the whole
enforcement story is meant to prevent, and it survived until a negative fixture
demanded otherwise.

**C11 - `NO-APPENDIX` broke on the closing line wrapping (found and fixed
2026-08-16, by T4).** The gate matched the frozen closing line by line prefix,
so a closing line wrapped at a different column read as an appendix. Fixed by
matching content: every non-blank line after the stem must be a contiguous
fragment of one of the two permitted forms.
