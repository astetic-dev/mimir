# Mimir - functionele beschrijving

> Voor de eigenaar en voor een volgende sessie. Dit bestand legt uit **wat Mimir is, hoe hij
> werkt en waarom hij zo gebouwd is**. Het is geen doctrine: Mimir leest het niet tijdens een
> run. Het staat in de Read-set, naast `README.md` en `BUILD.md`.
>
> Als je één ding leest, lees hoofdstuk 4 (de oorzaken-families). Dat is de kern van het
> product en de plek waar alle vaktaal vandaan komt.

---

## 1. Wat het is, in één alinea

Mimir is een map die je in een werkmap zet waar iets niet goed gaat, waarna je vertelt wat er
misging. Hij leest die werkmap, zoekt **één** structurele oorzaak, laat zien waarop die rust, en
stopt. Hij repareert niets, geeft geen stappenplan, geeft geen cijfer en maakt geen overzicht.
Het onderwerp van onderzoek is altijd de **structuur van de map**, nooit het model dat erin
draait.

De doelgroep is iemand met een agent-map die is gaan haperen: negeert regels die je aantoonbaar
hebt opgeschreven, doet de verkeerde stap, geeft elke keer iets anders, of is over maanden stil
slechter geworden.

**Belangrijke scope-notitie:** elke agent en elk project in de linkerbalk van Taurus is een
ICM-werkproces, of iemand het nu zo gebouwd heeft of niet. De mappen die haperen zijn meestal
juist de mappen die niemand netjes heeft opgezet.

---

## 2. Waar Mimir in de familie past

Er zijn vier rollen rond een ICM-werkmap. Ze verwarren is de snelste manier om het verkeerde
antwoord te krijgen.

| Rol | Tool | De vraag |
|---|---|---|
| bouwt | `icm-architect` (RinDig) | Hoe moet dit eruitzien? |
| reviewt | de editor | Is dit goed genoeg? |
| beschrijft | de cartograaf | Wát is dit? |
| **diagnosticeert** | **Mimir** | **Waarom werkt het niet?** |

Mimir is de enige van de vier die **achteruit werkt vanaf iets dat al kapot is**. De andere drie
kunnen op een gezonde map draaien. Mimir niet: zonder storing is er niets te diagnosticeren, en
dat hardop zeggen is bij hem een geldig antwoord.

Cassini (jouw comp-11-inzending) wijst *Diagnosis* met zoveel woorden af als buiten scope. Mimir
is de andere kant van die grens.

---

## 3. Hoe een run verloopt

De gebruiker zet de map neer en stelt een vraag. Er is altijd een hulpvraag - zonder gemelde
storing komt Mimir niet in beweging.

### De negen stappen

| # | Stap | Wat er gebeurt |
|---|---|---|
| 0 | **Harde stops** | Is dit een ICM-werkmap? Is er echt iets misgegaan? Gaat de klacht over de structuur, of over het model? Bij elk van de drie: zeg het en stop. Draait bij elk bericht opnieuw. |
| 1 | **Intake** | De eigenaar heeft een klacht, geen bewijs. Mimir vraagt om twee dingen, één instructie tegelijk: het pad naar de map, en één sessie waarin het misging. |
| 2 | **Minen en graderen** | `mine.py` draait over de map en schrijft `evidence.json`. Mimir zegt op welke bewijs-tier hij werkt. Hij vraagt ook: is de map na die run nog gewijzigd, en is dit eerder gebeurd? |
| 3 | **Eén storing afbakenen** | Mensen denken in episodes, niet in gebeurtenissen. Twee klachten zijn twee onderzoeken. Hoogstens twee keer vragen, dan zelf kiezen en het zeggen. |
| 4 | **Vaststellen wát faalde** | Wat doet de map niet meer dat je nodig hebt, wat is de faalwijze, wat zijn de gevolgen. Plus de check: is dit wel een storing, of werkt de methode juist? |
| 5 | **Vertakken en snoeien** | De families uit hoofdstuk 4 aflopen, in laag-volgorde. Wat afvalt blijft staan mét het bewijs dat het wegstreepte. |
| 6 | **Afdalen op noodzakelijkheid** | De removal-test: haal een stap weg, treedt de storing dan nog op? Zo ja, dan was die stap niet nodig en ben je te diep. Stop bij de laatste noodzakelijke stap. |
| 7 | **Rangschikken** | Welke oorzaak overleeft de voor de hand liggende reparatie? Die is primair. Kan het niet onderscheiden worden: onthouden, niet gokken. |
| 8 | **Verifiëren en schrijven** | Zelf de diagnose proberen te breken, markers controleren, de finding schrijven, de checker draaien. |

### Een poort vraagt, een poort blokkeert nooit

Elke stap eindigt met een vraag aan de eigenaar. Maar Mimir **wacht daar niet op**. Hij stelt de
vraag, zegt onder welke aanname hij doorgaat, en levert in dezelfde beurt door. Een beurt die
alleen vragen bevat heeft niets geleverd.

Komt er later een antwoord dat een schakel breekt, dan gaat de stap waar die schakel ontstond
opnieuw open - niet de conclusie behouden en de redenering eronder vervangen.

### Bewijs-tiers

Mimir zegt altijd op welke tier hij werkt, want dat bepaalt wat hij mag beweren.

| Tier | Wat je gaf | Wat het draagt |
|---|---|---|
| **A** | de map **én** een sessie waarin het misging | wat er te laden viel én wat de agent werkelijk deed |
| **B** | alleen de map | structurele claims hard, gedragsclaims afgeleid |
| **C** | alleen een sessie | wat er gebeurde, niet wat beschikbaar was |
| **D** | jouw verhaal over het gedrag | een symptoom, geen diagnose |
| **E** | een oordeel zonder verslag | nooit alleen hierop diagnosticeren |

**Het scherpste onderscheid in het hele product:** de map laat zien wat *beschikbaar* was, nooit
wat *gelezen* is. Alles wat die grens oversteekt zonder sessie is afgeleid en moet dat zeggen.

---

## 4. De oorzaken-families - de kern

Dit is waar jouw vraag over ging.

**Wat het is.** Een begrensde lijst van negentien structurele manieren waarop een ICM-map kan
falen. Geen open categorie: een genoemde oorzaak moet uit deze lijst komen, of Mimir zegt
expliciet dat zijn lijst tekortschiet.

**Waarom begrensd.** Een diagnosticus zonder vaste lijst vindt altijd wel iets, en dat iets is
dan een formulering in plaats van een bevinding. Met een vaste lijst kun je zien wat is
afgestreept en waarom, en kan iemand met je oneens zijn over een specifiek punt. Dat idee komt
van de visual-momentum-inzending, die het combineert met een ontsnappingsluik: past niets, dan is
dat een tekort van de lijst en zeg je dat, in plaats van je zaak in het dichtstbijzijnde hokje
te duwen.

**Waar de inhoud vandaan komt.** Niet uit mijn hoofd. Elke familie is afgeleid uit de
ICM-canon: de tien invarianten uit `icm-architect/SKILL.md`, de vijftien patronen en de
vijf-lagen-architectuur uit `_core/CONVENTIONS.md`, en de vijf ontwerpprincipes uit
`references/core.md`. Mimir heeft dus geen eigen mening over wat een goede map is - hij weet
alleen wat de methode zegt dat een goede map is.

**Hoe een familie eruitziet.** Elke familie heeft vier delen: wat het is, de **vingerafdruk**
(wat je in `evidence.json` ziet als hij aan de hand is), waarvoor het meestal **wordt
aangezien**, en hoe je hem onderscheidt van zijn **buurman**. Dat laatste voorkomt de meeste
verkeerde veroordelingen. Die vorm komt van de regression-historian-inzending.

**Belangrijk:** een vingerafdruk die afgaat is een **kandidaat, geen bevinding**. Van kandidaat
naar oorzaak gaat via de removal-test (stap 6) en de rangschikking (stap 7).

### De lagen, in vaste volgorde

De families worden afgelopen in deze volgorde, en dat is geen alfabetische toevalligheid. Het is
de volgorde van hoe vaak elke laag werkelijk schuldig is.

1. **Routering** - kan een agent überhaupt zijn weg vinden?
2. **Contract** - bestaat het punt waar staat wat een stap leest, en noemt het exacte paden?
3. **Fabriek vs. product** - staat het stabiele materiaal los van wat per run ontstaat?
4. **De grafiek** - links, één huis per feit, eenrichtingsverkeer, weesbestanden
5. **Poorten** - stopt er iets voor een mens?
6. **Vorm** - te veel of te weinig structuur
7. **De inhoud van het referentiemateriaal** - **als laatste, met opzet**

Die laatste is het belangrijkste ontwerpbesluit in het product. *"De regels zijn niet duidelijk
genoeg"* is de theorie waarmee vrijwel elke eigenaar binnenkomt, en het is bijna nooit de
oorzaak. Meestal waren de regels prima en zijn ze nooit geladen. Dat is overgenomen van de
winnaar van de ronde, waar hetzelfde geldt voor de inhoud van een e-mail.

### De negentien, in gewone taal

**Laag 1 - routering**

| # | Wat er misgaat | Waarvoor het wordt aangezien |
|---|---|---|
| 1 | Het instapbestand draagt de inhoud zelf in plaats van ernaar te wijzen: alle regels komen elke keer tegelijk binnen, ongesorteerd | "het model negeert mijn regels" |
| 2 | `CLAUDE.md` en `AGENTS.md` bestaan allebei, worden allebei met de hand bijgehouden, en lopen uiteen | "bij mij werkt het wel en bij hem niet" |
| 3 | Er is werk in de map waar niets naar verwijst - de agent komt correct binnen in een gebouw zonder de kamer die hij nodig heeft | "hij begint altijd op de verkeerde plek" |

**Laag 2 - het contract (waar staat wat een stap leest)**

| # | Wat er misgaat | Waarvoor het wordt aangezien |
|---|---|---|
| 4 | Een werkmap heeft geen contract, of het contract mist Inputs/Process/Outputs - de agent beslist zelf wat hij laadt | "het model is inconsistent" |
| 5 | Het contract noemt dingen in plaats van paden: "het onderzoek", "de huisstijl" - de agent lost dat elke dag anders op | "hij las het verkeerde bestand" |
| 6 | Het contract stuurt naar een heel bestand van 400 regels waar 60 regels van toepassing zijn | "hij verdrinkt in context" |
| 7 | De totale context van één stap valt ver buiten de gezonde 2k-8k band | "hij raakt halverwege de draad kwijt" |

**Laag 3 - fabriek versus product**

| # | Wat er misgaat | Waarvoor het wordt aangezien |
|---|---|---|
| 8 | Stabiel referentiemateriaal en per-run artefacten staan door elkaar, zonder scheiding | "de map is rommelig" |
| 9 | Een stap krijgt een eerdere output aangewezen als *voorbeeld om na te doen* - elke run leert van het slechtste werk dat er ooit uitkwam | "de kwaliteit zakt langzaam weg" |
| 10 | De map is opgezet met `{{PLACEHOLDERS}}` en die zijn nooit ingevuld | "hij verzon een huisstijl" |

**Laag 4 - de grafiek**

| # | Wat er misgaat | Waarvoor het wordt aangezien |
|---|---|---|
| 11 | Hetzelfde feit staat in twee bestanden die allebei gezaghebbend zijn, en ze zijn uit elkaar gelopen | "hij spreekt zichzelf tegen" |
| 12 | Een stap noemt een input die geen enkele andere stap voortbrengt - de keten breekt op een benoemd punt | "de agent verzon een bestand" |
| 13 | Bestanden waar niets naar wijst, en verwijzingen naar bestanden die niet bestaan | "hij leest de verkeerde dingen" |
| 14 | Map A wijst naar B en B wijst terug naar A - geen deel is meer los te laden | "de context is te groot" |
| 15 | Een schema of naamconventie schrijft namen voor die de bestanden niet meer gebruiken | "de kaart klopt niet" |
| 16 | Een index die een script hoort te bouwen is met de hand bewerkt en loopt achter | "de kaart is verrot" |

**Laag 5 - poorten**

| # | Wat er misgaat | Waarvoor het wordt aangezien |
|---|---|---|
| 17 | Niets in de map stopt voor een mens; de run dendert van invoer naar eindproduct | "het model luistert niet" |

**Laag 6 - vorm** (alleen als alles hierboven schoon is)

| # | Wat er misgaat | Waarvoor het wordt aangezien |
|---|---|---|
| 18 | Mappen voor stappen die nog niet bestaan, lege bakken, bedachte diepte | "het is te ingewikkeld om te gebruiken" |
| 19 | Eén bestand draagt het hele werk; geen stappen, geen contracten | "ik heb een betere prompt nodig" |

**Laag 7 - de inhoud zelf.** Alleen te veroordelen als de lagen hierboven aantoonbaar schoon
zijn én een sessie laat zien dat het bestand op het faalmoment daadwerkelijk gelezen is. Zonder
sessie is deze laag onbereikbaar.

### De grens van de lijst

Past het bewijs op een mechanisme dat geen van de negentien beschrijft, dan zegt Mimir dat, noemt
de dichtstbijzijnde families en waarom elk afvalt, en veroordeelt niets. Dat is een geldig
antwoord.

Dat is één keer echt gebeurd, op `porter-intake-operator`: een stap waarvan de inputs de
sjablonen en de toon noemen en de projectstand nooit. De lijst mist een familie voor
*contract-toereikendheid* - of de genoemde inputs de **juiste** zijn, los van of ze goed genoemd
zijn. Dat staat als open defect **D8** in `DEFECTS.md`.

### En hoe je ze in een finding tegenkomt

Sinds jouw opmerking van 17-8: **nooit als kaal nummer.** De oorzaak staat in jouw woorden, het
nummer hooguit tussen haakjes als vindplaats. De poort `PLAIN` laat een kale "familie 8" niet
door. Zie `DEFECTS.md` C14 - dat was de belangrijkste bevinding van de hele bouw en hij kwam van
een lezer, niet van een test.

---

## 5. De twee scripts

**Het script rekent, het model benoemt.** Dat is het scharnierpunt van het hele ontwerp, geleend
van de regression-historian-inzending. Mimir telt nooit zelf.

### `checks/mine.py` - de miner

Loopt de map af en schrijft `evidence.json`: laagclassificatie en regelaantal per bestand, de
stage-inventaris met contractvorm en output-bezetting, de volledige linkgrafiek met kapotte
verwijzingen, wezen en terugverwijzingen, placeholder-telling, duplicatie-clusters, geschatte
context-belasting per stap tegen de 2k-8k band, naamgeving, payload-detectie in routing-bestanden
en schema-drift.

**Elk getal dat in een finding mag staan komt hieruit.** Staat het er niet in, dan gaat het de
finding niet in.

Een map mag een `.mimirignore` dragen: één pad per regel, voor submappen die eigenlijk andere
werkmappen zijn. Mimir heeft er zelf een, want `eval/` en `checks/fixtures/` bevatten zes andere
mappen.

Velden die onder `heuristics` staan zijn inschattingen door patroonherkenning, geen metingen.
`estTokens` is tekens gedeeld door vier: goed genoeg om 2k van 30k te onderscheiden, waardeloos
op een bandgrens.

`python checks/mine.py --selftest` bouwt een bekend-kapotte en een bekend-gezonde map in een
tijdelijke plek en controleert dat de vingerafdrukken op de eerste afgaan en op de tweede zwijgen.
14 checks.

### `checks/verify.py` - de checker

Toetst de **finding zelf**, niet de map. Tien poorten:

| Poort | Wat het afdwingt |
|---|---|
| `FORMAT` | alle negen secties, één keer, in volgorde |
| `ONE-CAUSE` | één oorzaak, geen lijst, maximaal vier zinnen |
| `MARKED` | elke schakel draagt `[seen]`, `[inferred]` of `[general]` |
| `GROUNDING` | elk `[seen]`-citaat staat letterlijk in de map, het bewijs of de sessie |
| `CITATIONS` | elk pad en elk getal van twee cijfers of meer komt uit het bewijs - ook buiten aanhalingstekens |
| `NO-RX` | geen reparatietaal, en geen counterfactual, in de taal van de finding |
| `PLAIN` | geen kale "familie N" |
| `ABSTAIN` | onthouden vereist twee genoemde kandidaten; een genoemde oorzaak mag niet ook onthouden heten |
| `NO-APPENDIX` | niets na de vaste slotregel |
| `FALSIFIER` | de "wat werpt dit omver"-sectie is niet leeg en schrijft niets voor |

`python checks/verify.py --selftest` draait één goede en elf foute findings; elke foute valt op
precies zijn eigen poort. Een wijziging die er één doorlaat is een regressie.

`python checks/verify.py --manifest .` controleert dat geen doctrine-bestand naar het
testmateriaal wijst - anders is een blinde run niet blind.

---

## 6. De vijf vaste antwoorden

Naast een gewone finding zijn er vijf bevroren teksten. Vast, dus mechanisch toetsbaar - een
geïmproviseerde parafrase valt om.

| Antwoord | Wanneer |
|---|---|
| `OUT-OF-SCOPE` | dit is geen ICM-werkmap |
| `NO-FAILURE` | de map is in orde; wat je meldt is de methode die werkt |
| `INSUFFICIENT-EVIDENCE` | de hele lijst is afgelopen en niets sluit op dit bewijs |
| `UNRESOLVED` | twee oorzaken verklaren het even goed en het bewijs scheidt ze niet |
| `OUT-OF-TAXONOMY` | het mechanisme is duidelijk, mijn lijst kent het niet |

`NO-FAILURE` is de moeilijkste en de belangrijkste. *"Hij stopt steeds en vraagt me dingen"* is
de menselijke poort die werkt. *"Hij leest maar drie bestanden"* is gelaagd laden dat werkt. Een
gereedschap dat altijd iets vindt, leert je je gezonde werkmappen te wantrouwen.

---

## 7. Wat er in de map staat

| Set | Bestanden | Regel |
|---|---|---|
| **Load** | `identity.md`, `rules.md`, `intake.md`, `reference/` | de doctrine; dit krijgt een run te zien |
| **Read** | `README.md`, `examples.md`, `BUILD.md`, `CLAUDE.md`, **dit bestand** | voor mensen; nooit in een gescoorde run |
| **Verify** | `checks/`, `eval/`, `TESTING.md`, `DEFECTS.md`, `BLIND-SPOTS.md` | bewijs *over* Mimir; nooit geladen |

`reference/` bevat vijf bestanden: `evidence-grades.md` (wat elke bron bewijst en niet bewijst),
`cause-taxonomy.md` (de negentien), `cause-vs-symptom.md` (de vertaaldrill van klacht naar
oorzaak), `output-contract.md` (de vorm van het antwoord en de vijf vaste teksten),
`disguised-asks.md` (de zeven vermommingen van "los het even op").

`BUILD.md` beschrijft het herbruikbare deel: de negen stappen, de tien poorten en de vijf vaste
antwoorden zijn domein-onafhankelijk. Alleen de families en de miner zijn ICM-specifiek.

---

## 8. Waar het vandaan komt

Mimir is eerst een combinatie en daarna pas een uitvinding. Vijf diagnostici uit competitieronde
10 zijn end-to-end gelezen, en de reden dat combineren de moeite waard was is dat **elk gat door
een ander gevuld wordt**:

| Bron | Wat ervandaan komt |
|---|---|
| **inbox-autopsy** (winnaar) | de intake voor een leek; bewijs-tiers; de lagen in vaste volgorde met de meest-beschuldigde laag als laatste |
| **Radix** | de markers `[seen]/[inferred]/[general]`; *een poort vraagt, blokkeert nooit*; de removal-test met beide buren; rangschikken op wat de reparatie overleeft; je eigen zwakste schakel benoemen |
| **visual-momentum** | de begrensde lijst met ontsnappingsluik; onthouden als geldig resultaat; het bewijs-kanaal moet het mechanisme kúnnen tonen; Load/Verify strikt gescheiden |
| **drained-me** | de voorspelling vóór de run vastleggen; bevroren antwoordteksten; "niets te diagnosticeren" los van "te weinig bewijs"; *een counterfactual is advies in de verleden tijd*; het defect-logboek |
| **regression-historian** | het script rekent, het model benoemt; citaten moeten oplossen; de zelf-geteste poort; de vertaaltabel klacht-naar-oorzaak |

Volledige toeschrijving per mechanisme staat in `CREDITS.md`. Vijf poorten bestaan in geen van de
vijf bronnen: `MARKED`, `CITATIONS` buiten de aanhalingstekens, de counterfactual-arm van
`NO-RX`, `ABSTAIN` en `NO-APPENDIX`. `PLAIN` kwam er later bij, uit gebruik.

---

## 9. Stand van zaken (17-8-2026)

### Wat bewezen is

| Test | Resultaat |
|---|---|
| Miner-selftest | PASS, 14 checks |
| Checker-selftest | PASS, 12 fixtures |
| Doctrine ziet het testmateriaal niet | PASS |
| De meegeleverde voorbeeld-finding door alle poorten | PASS |
| Mimir door zijn eigen miner | PASS, met twee beargumenteerd vrijgesproken signalen |

### Wat gedraaid is op echte mappen

Drie diagnoses op 17-8, **door de bouwer en dus niet blind**: twee op
`porter-intake-operator` (algemene concepten; ontbrekende concepten) en één op Mimir zelf tegen
de competitievoorwaarden. Die laatste is door de eigenaar omvergeworpen op zijn eigen genoemde
voorwaarde - zie `eval/receipts/applied/A3-OVERTURNED.md`.

Ze kostten zes defecten, waarvan vier in de checker. De twee belangrijkste
(`PLAIN` en de taal-afhankelijke woordenlijsten) zijn gevonden door een lezer, niet door een test.

### Wat nog open staat

- **Acht blinde runs**, allemaal `PENDING` in `TESTING.md`. Verse sessie, alleen de Load-set,
  case uit `eval/cases/`, antwoord verbatim naar `eval/receipts/`. De antwoordsleutels liggen al
  vast.
- **Open defecten** `D1` (rules.md is 406 regels), `D2`, `D3`, `D4` (geen blinde run), `D5` (de
  counterfactual-poort leest geen gesprek), `D6` (geen veld voor "wat is terzijde gelegd"),
  `D8` (geen familie voor contract-toereikendheid), `D9` (de vaste teksten bestaan alleen in het
  Engels).
- **Geen git-repo.** Zonder commit-volgorde is de claim in `eval/README.md` dat de sleutels vóór
  de runs vastlagen niet hard te maken. Dat moet gebeuren vóór de eerste blinde run.
- **Uitrol in Taurus** en publicatie op GitHub onder de astetic-dev-identiteit.
