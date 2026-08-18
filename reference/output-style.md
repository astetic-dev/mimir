# Output style - handing back the finding as a page, not a wall of text

`reference/output-contract.md` governs what the finding says: nine sections, the markers, the
five frozen returns. This file governs the last step only - how the finished, checker-passed
finding is handed back to the person who is reading it.

A finding that passes every gate in `checks/verify.py` and is then pasted into the chat as raw
markdown is still hard to read: no hierarchy, no separation between what was observed and what
was concluded, a wall the owner has to parse by eye. So the finding is also rendered as a
self-contained HTML file, in the house style below, and that file - not the pasted markdown, not
a code block in the chat - is what gets handed back. `rules.md` step 8 point 8 is where this
happens, after `verify.py` has passed, never before.

The markdown finding is still what gets checked. This is a rendering step on top of it, not a
replacement for the discipline that produced it - every marker, every quote, every ranking stays
exactly as verified. Nothing gets softened, summarised or reworded on the way into HTML.

---

## The tokens, and what already carries a fixed value

The template below has Mimir's fixed values filled in directly - `{{NAME}}`, `{{ROLE_NOUN}}` and
`{{FIELD_CAPTION}}` are gone from the code block; they are `MÍMIR`, `diagnostician` and
`DIAGNOSIS`. That styling of the name (the accent on the í) is the masthead's typography, not a
respelling - Mimir stays Mimir everywhere else in this folder's prose.

Three tokens are left for you to fill at generation time, once per finding:

| Token | What goes there for a diagnosis |
|---|---|
| `{{DATE}}` | The date this finding was produced. |
| `{{SUBJECT_OR_SESSION_ID}}` | One line: the scoped failure from step 3, in the owner's words - e.g. "weeknotes agent - wrong voice" or the workspace name plus the failure mode from step 4. |
| `{{DOCUMENT_TITLE}}` | A short phrase naming the functional failure from step 4 - what the workspace stopped doing, not the cause. E.g. "Cannot produce a usable draft without a second pass." The `<title>` tag and the page `<h1>` both use it. |

Everything else in the body is structural: `<h2>`, `.callout`, `.lede` and `table` are repeatable
blocks, not tokens. Use as many `<h2>` blocks as the finding needs; the template shows the pattern
once.

## Where each of the nine sections goes

The finding's shape does not change. This is only where each already-written section lands on the
page.

| Finding section | Template element |
|---|---|
| `DIAGNOSIS` | `.lede`, verbatim - "the single thing this document says, in plain language" is exactly what `DIAGNOSIS` already is. Do not shorten it to fit. |
| `EVIDENCE TIER` | A `.callout` right under the lede, labelled `evidence tier`. State the letter and what it means in one clause, same as the finding does. |
| `EVIDENCE CHAIN` | An `<h2>Evidence chain</h2>` followed by an ordered list (`<ol>`), one `<li>` per link. Keep `[seen]`, `[inferred]` and `[general]` visible at the start of each item exactly as written - do not turn them into colour alone. A reader who copies the page as plain text must still see the markers. |
| `WHY IT STOPS HERE` | An `<h2>Why it stops here</h2>` with the two sub-points ("deeper step tested and rejected" / "shallower step passed over") as two `<p>`s or a two-row `table`, whichever reads cleaner for that finding's length. Both neighbours stay named. |
| `RULED OUT` | `<h2>Ruled out</h2>` plus a `<ul>`, one family per item, in the plain words the finding already uses - the family index still rides in brackets, per `PLAIN`. |
| `CONTRIBUTING FACTORS` | `<h2>Contributing factors</h2>` - a short paragraph, or the literal word "None" if the finding says none. Never dropped even when empty; its absence would read as an oversight rather than a stated result. |
| `WEAKEST LINK` | A `.callout` labelled `weakest link`. |
| `CONFIDENCE` | A `.callout` labelled `confidence`, holding just the word (`high` / `moderate` / `provisional` / `UNRESOLVED`). |
| `WHAT WOULD OVERTURN THIS` | `<h2>What would overturn this</h2>` plus a `<ul>`. |
| The frozen closing line | A `<hr class="divider">` then the line itself, unedited, as a `.lede`-styled paragraph at the foot of `.page`. It is the one paragraph on the page that is never paraphrased. |

For the five frozen returns (`OUT-OF-SCOPE`, `NO-FAILURE`, `INSUFFICIENT-EVIDENCE`, `UNRESOLVED`,
`OUT-OF-TAXONOMY`), render the frozen text as the `.lede` and skip the sections that do not apply
- an `OUT-OF-SCOPE` reply has no evidence chain to render. Do not invent content to fill an
unused block.

## The template

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>MÍMIR — {{DOCUMENT_TITLE}}</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=EB+Garamond:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
<style>
  :root{
    --paper:        #f3ead6;
    --paper-edge:   #e6d8b4;
    --ink:          #2b2013;
    --ink-soft:     #5b4c34;
    --wood-dark:    #201609;
    --wood-mid:     #34240f;
    --brass:        #b6893f;
    --brass-bright: #d9b06b;
    --rule:         rgba(43,32,19,0.28);
    --shadow:       rgba(0,0,0,0.35);
  }
  @media (prefers-color-scheme: dark){
    :root{
      --paper:      #241a10;
      --paper-edge: #1a1109;
      --ink:        #ecdfc0;
      --ink-soft:   #b8a37d;
      --wood-dark:  #120c05;
      --wood-mid:   #1c130a;
      --brass:      #c99b4c;
      --brass-bright:#e6bd76;
      --rule:       rgba(236,223,192,0.22);
      --shadow:     rgba(0,0,0,0.6);
    }
  }

  *{ box-sizing:border-box; }
  html,body{ margin:0; padding:0; }
  body{
    background: var(--wood-dark);
    background-image:
      radial-gradient(ellipse at 20% -10%, rgba(217,176,106,0.10), transparent 55%),
      linear-gradient(180deg, var(--wood-dark), var(--wood-mid));
    color: var(--ink);
    font-family: 'EB Garamond', Georgia, 'Times New Roman', serif;
    font-size: 18px;
    line-height: 1.6;
  }

  /* ---------- masthead ---------- */
  .masthead{
    padding: 3.2rem 2rem 2.2rem;
    text-align: left;
    max-width: 860px;
    margin: 0 auto;
  }
  .masthead .name{
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-weight: 600;
    font-size: clamp(2.4rem, 6vw, 3.6rem);
    letter-spacing: 0.18em;
    color: var(--brass-bright);
    text-shadow: 0 1px 0 rgba(0,0,0,0.4), 0 0 24px rgba(217,176,106,0.15);
    margin: 0;
    text-transform: uppercase;
  }
  .masthead .rule{
    height: 1px;
    background: linear-gradient(90deg, var(--brass) 0%, rgba(182,137,63,0.15) 70%, transparent 100%);
    margin: 0.55em 0 0.7em;
  }
  .masthead .role{
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-style: italic;
    font-weight: 500;
    font-size: 1.15rem;
    color: #cabb98;
    margin: 0 0 0.3em;
  }
  .masthead .meta{
    font-family: 'EB Garamond', Georgia, serif;
    font-size: 0.78rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #8a7a5c;
  }

  /* ---------- page / content card ---------- */
  .page{
    max-width: 860px;
    margin: 0 auto 3rem;
    background: var(--paper);
    border: 1px solid var(--paper-edge);
    box-shadow: 0 20px 50px var(--shadow);
    border-radius: 2px;
    padding: 3rem 3.2rem 3.4rem;
  }
  @media (max-width: 640px){
    .page{ padding: 2rem 1.3rem 2.4rem; margin-left:0.6rem; margin-right:0.6rem; }
    .masthead{ padding: 2.2rem 1.3rem 1.6rem; }
  }

  .page h1, .page h2, .page h3{
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-weight: 600;
    color: var(--ink);
  }
  .page h1{
    font-size: 1.9rem;
    letter-spacing: 0.02em;
    margin: 0 0 0.3em;
  }
  .page h2{
    font-size: 1.35rem;
    text-transform: uppercase;
    letter-spacing: 0.10em;
    color: var(--ink-soft);
    border-bottom: 1px solid var(--rule);
    padding-bottom: 0.35em;
    margin: 2.2em 0 0.9em;
  }
  .page h2:first-of-type{ margin-top: 0.4em; }
  .page h3{
    font-size: 1.1rem;
    font-style: italic;
    color: var(--ink);
    margin: 1.6em 0 0.5em;
  }
  .page p{ margin: 0 0 1em; }
  .page ul, .page ol{ margin: 0 0 1.1em; padding-left: 1.3em; }
  .page li{ margin: 0.3em 0; }

  .page .lede{
    font-size: 1.08rem;
    color: var(--ink-soft);
    font-style: italic;
    border-left: 2px solid var(--brass);
    padding-left: 0.9em;
    margin: 0 0 1.8em;
  }

  .callout{
    border-left: 2px solid var(--brass);
    background: rgba(182,137,63,0.08);
    padding: 0.85em 1.1em;
    margin: 1.2em 0;
    font-size: 0.98rem;
  }
  .callout .label{
    display:block;
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-style: italic;
    color: var(--brass);
    margin-bottom: 0.25em;
  }

  table{ width:100%; border-collapse: collapse; margin: 1.2em 0; font-size: 0.95rem; }
  th, td{ text-align:left; padding: 0.5em 0.7em; border-bottom: 1px solid var(--rule); }
  th{ font-family:'Cormorant Garamond', Georgia, serif; text-transform:uppercase; letter-spacing:0.06em; font-size:0.82rem; color: var(--ink-soft); }

  .divider{
    border: none;
    border-top: 1px solid var(--rule);
    margin: 2em 0;
  }

  .quote-source{
    display:block;
    font-size: 0.85rem;
    color: var(--ink-soft);
    margin-top: 0.4em;
  }

  footer{
    max-width: 860px;
    margin: 0 auto 3rem;
    padding: 0 3.2rem;
    display:flex;
    justify-content:space-between;
    align-items:center;
    font-size: 0.72rem;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: #8a7a5c;
  }
  footer .rule{ flex:1; height:1px; background:var(--rule); margin: 0 1em; }
</style>
</head>
<body>

  <div class="masthead">
    <div class="name">MÍMIR</div>
    <div class="rule"></div>
    <div class="role">the diagnostician</div>
    <div class="meta">{{DATE}} &middot; {{SUBJECT_OR_SESSION_ID}}</div>
  </div>

  <div class="page">

    <h1>{{DOCUMENT_TITLE}}</h1>
    <p class="lede">{{DIAGNOSIS - one or two sentences, verbatim from the finding.}}</p>

    <div class="callout">
      <span class="label">evidence tier</span>
      {{EVIDENCE TIER - the letter, and what it does and does not prove, verbatim.}}
    </div>

    <h2>Evidence chain</h2>
    <ol>
      <li>{{[seen] / [inferred] / [general] - one finished link, marker kept visible.}}</li>
    </ol>

    <h2>Why it stops here</h2>
    <p>{{Deeper step tested and rejected.}}</p>
    <p>{{Shallower step passed over.}}</p>

    <h2>Ruled out</h2>
    <ul>
      <li>{{One cause family, cleared, with the evidence that cleared it.}}</li>
    </ul>

    <h2>Contributing factors</h2>
    <p>{{Subordinate findings, or "None."}}</p>

    <div class="callout">
      <span class="label">weakest link</span>
      {{WEAKEST LINK - which link, and why the conclusion survives it.}}
    </div>

    <div class="callout">
      <span class="label">confidence</span>
      {{high / moderate / provisional / UNRESOLVED}}
    </div>

    <h2>What would overturn this</h2>
    <ul>
      <li>{{One observation that would break the finding.}}</li>
    </ul>

    <hr class="divider">

    <p class="lede">{{The frozen closing line, unedited.}}</p>

  </div>

  <footer>
    <span>TAURUS</span>
    <span class="rule"></span>
    <span>DIAGNOSIS</span>
  </footer>

</body>
</html>
```
