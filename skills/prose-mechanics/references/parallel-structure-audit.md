# Parallel Structure Audit Reference

A diagnostic pass for broken grammatical parallelism in lists, comparisons, and coordinated series.

## What This Audit Catches

- **Mixed grammatical forms in lists:** infinitives crossed with gerunds, nouns crossed with verb phrases, full clauses crossed with fragments.
- **Coordinated phrases that drift in tense, mood, or voice:** "She walked to the store, was bought milk, and is paying with cash."
- **Comparisons that compare unlike things:** "Her writing is better than her sister."
- **Correlative conjunctions with non-matching elements:** "Either you go now or leaving tomorrow."
- **Headers and bullet lists that break their own pattern:** the silent failure mode in nonfiction.

## What This Audit Does NOT Catch

- **Stylistic asymmetry used deliberately for rhythm or emphasis.** Some of the best sentences violate parallelism on purpose. The audit flags; the author decides.
- **Repetition for rhetorical effect** (anaphora, epistrophe, etc.). These are intentional patterns; do not flag.
- **Long-range thematic parallels across chapters.** Out of scope.
- **Logical parallelism of ideas.** This audit is grammatical, not conceptual.

## Why It Matters

Parallel structure does three things:

1. **Reduces cognitive load.** The reader's brain locks into a pattern and processes the rest of the list almost subconsciously. Breaking the pattern forces re-parsing, which feels like a stumble even when the reader can't name what went wrong.
2. **Signals control.** Tight parallelism is one of the clearest markers of prose written by someone who knows what they're doing. Broken parallelism—even when grammatical—reads as amateur.
3. **Sharpens meaning.** Coordinated elements should be on equal logical footing. When form breaks, readers often suspect the ideas don't actually fit together.

## Detection Patterns

A passage is flagged if it contains:

1. **A list of three or more items where item N+1 has a different grammatical form than item N.** Example: "He liked running, to swim, and bike rides." Flag.
2. **A series joined by "and," "or," "but" where coordinated elements differ in form.** "She was tall, ambitious, and walked with purpose." Flag (adjective, adjective, verb phrase).
3. **Comparisons using "than" or "as ... as" with mismatched grammatical anchors.** "Her writing is sharper than her sister." Flag—should be "than her sister's."
4. **Correlative pairs (either/or, neither/nor, not only/but also, both/and) where the elements after each half differ in form.** "Not only running marathons but he also climbs mountains." Flag.
5. **Bullet lists or headers where some entries start with verbs and others with nouns.** Flag the entire list.
6. **Coordinated "to" infinitives where "to" appears inconsistently.** "She wanted to leave, to rest, and finally sleep." Flag—does "finally sleep" belong inside or outside the infinitive scope? Make it consistent.

## Remediation Patterns

- **Lift one item to match the others' form.** "He liked running, to swim, and bike rides" → "He liked running, swimming, and biking."
- **Rewrite the whole series to a single pattern.** Often easier than surgical patching.
- **Split into two sentences if the elements really aren't parallel.** Sometimes the audit reveals that the author was trying to coordinate things that shouldn't be coordinated.
- **For comparisons, supply the implied element.** "Her writing is sharper than her sister's [writing]" — using the possessive is enough.
- **For correlatives, place the conjunction so the elements after each half match.** "He not only runs marathons but also climbs mountains" (verb + object after each half).

## Failure Modes

**Over-application** — forcing parallelism everywhere produces:
- Sing-song, formulaic prose
- Loss of natural speech rhythm in dialogue (people don't speak in parallel)
- Stilted lists that read like résumé bullets

**Under-application** — leaving flags unaddressed produces:
- Reader stumbles in lists that should be smooth
- An amateur sheen in otherwise polished prose
- Compromised rhetorical force in passages built around parallel structure

Dialogue is the most common place to under-apply on purpose. Real speech is not parallel; insisting on parallelism in dialogue destroys voice.

## Worked Examples

### Example 1: Mixed Forms in a Self-Help List

**Before:**

> To build a sustainable practice, you need to wake up early, eating a real breakfast, and you should exercise before checking email.

Flag: infinitive ("to wake up"), gerund ("eating"), modal+verb ("should exercise"). Three different forms.

**After:**

> To build a sustainable practice, wake up early, eat a real breakfast, and exercise before checking email.

Notes: all imperatives now. The original was trying to do "you need to" + a list, but the list members drifted into their own grammars. Cleaner to imperative throughout.

### Example 2: Broken Correlative in a Thriller

**Before:**

> She had not only mastered the dead drop protocol but also the cipher work was something she practiced for years.

Flag: "not only" is followed by a verb phrase ("mastered the dead drop protocol") but "but also" is followed by an independent clause ("the cipher work was something she practiced..."). Forms don't match.

**After:**

> She had not only mastered the dead drop protocol but also practiced cipher work for years.

Notes: now both halves take verb phrases. Sentence is also shorter and punchier.

### Example 3: Drifting Bullet List (Nonfiction)

**Before:**

> Three things separate consistent writers from inconsistent ones:
> - A fixed time and place
> - They protect that block from intrusion
> - Writing even when they don't feel like it

Flag: noun phrase, independent clause, gerund phrase. Three different forms in a three-item list.

**After:**

> Three things separate consistent writers from inconsistent ones:
> - A fixed time and place
> - A protected block, free from intrusion
> - A willingness to write even when uninspired

Notes: all noun phrases now. The list scans cleanly because the reader's pattern-matching engine isn't being thrown.

## Engine Hook

If `command -v scriptorium` succeeds, run
`scriptorium prose prepare parallel-structure <chapter>`, judge per the
patterns above, then `submit-findings`. Otherwise apply the patterns
directly against the chapter text.
