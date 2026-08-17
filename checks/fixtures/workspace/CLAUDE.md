# Weeknotes workspace

This workspace turns a week of raw notes into a published post.

## Folder map

```
weeknotes/
├── CLAUDE.md
├── CONTEXT.md
├── references/
│   └── style-guide.md
└── stages/
    ├── 01-gather/
    └── 02-write/
```

## Routing

| You want to | Go to |
|---|---|
| Run the pipeline | `CONTEXT.md` |
| Gather the week | `stages/01-gather/CONTEXT.md` |
| Write the post | `stages/02-write/CONTEXT.md` |

## Voice rules

The weeknotes voice is first person, past tense, and plain. It reads like a
message to one colleague who was away, not like a newsletter.

Write short sentences. A sentence with two clauses is usually two sentences.

Never open with the week. "This week I" is the most common opening in the genre
and it is the reason the genre is boring. Open with the thing that happened.

Do not use the word "excited". Do not use the word "journey". Do not use the
word "learnings". Use "learned", or better, say what was learned.

Numbers are written as digits from ten upward and as words below ten, except in
a heading, where digits are always used because a heading is scanned.

The reader knows what the product is. Do not re-introduce it. Do not explain an
acronym that appeared in last week's post.

Every claim about a result carries the measurement next to it or it is cut. "It
got faster" is not a claim, it is a mood.

Hedging is allowed and encouraged where the thing is genuinely uncertain, and is
banned where it is not. "It seems like the migration worked" when the migration
demonstrably worked is false modesty and it costs the reader trust.

The post ends where the week ended. There is no summary paragraph, no "next
week I will", and no sign-off. The last thing that happened is the last
sentence.

Links go inline on the phrase they describe. Never "click here". Never a bare
URL in the body.

Headings are sentence case. Only the first word is capitalised, and any proper
noun.

Lists are for things that are genuinely a list. Three sentences that happen to
be about related topics are a paragraph.

Bold is for a term being defined, once, at its definition. It is not for
emphasis. Italics are for titles of things.

The em dash is not used in this workspace. Use a colon where the second half
explains the first, a full stop where it does not.

Names of colleagues appear as first name only. Names of external people appear
in full on first mention.

A quote from a person is verbatim or it is not in quote marks. Paraphrase is
fine and it goes in ordinary prose.

Do not use "we" for work that one person did. Do not use "I" for work a team
did. Both errors are noticed by exactly the people who were there.

Screenshots carry a one-line caption saying what to look at. A screenshot with
no caption is decoration.

Code appears in the post only when a reader could copy it and it would run. An
illustrative fragment goes in prose instead.

The tone toward setbacks is flat and specific. Not cheerful, not dramatic. "The
deploy failed twice on Thursday because the certificate had expired" is the
register.

Do not thank the reader for reading.

## Examples

**Good opening:**

> The certificate expired at 04:12 on Thursday and took the staging environment
> with it. Nobody noticed until standup.

**Bad opening:**

> This week was an exciting one for the team! We went on a bit of a journey with
> our infrastructure.

**Good result claim:**

> The index rebuild took the query from 2.4 seconds to 180 milliseconds.

**Bad result claim:**

> Performance is much better now.

**Good ending:**

> The last thing I did on Friday was delete the old cron entry. It had been
> firing into a dead endpoint since March.

**Bad ending:**

> All in all a solid week. Next week I am excited to dig into the new dashboard.
> Thanks for reading!

## What a finished post looks like

A finished post is between 400 and 900 words. It has between two and five
headings. It contains at least one measurement and at least one setback.

It does not contain a table of contents, an introduction explaining what
weeknotes are, or a call to action.

## Triggers

| Keyword | Action |
|---|---|
| `setup` | Run the onboarding questionnaire |
| `status` | Show which stages have output |
