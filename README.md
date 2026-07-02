# Writing Skills for Claude Code

A Claude Code plugin with specialized skills for fiction and narrative nonfiction authors.

## Session Continuity

Book projects span weeks or months, and Claude has no memory between sessions. All three skills now treat the project's blueprint or Story Bible as persistent state: read it at session start, update it when foundations change, and write a short note to `sessions/YYYY-MM-DD_topic-slug.md` at session end. The prose-mechanics skill uses a per-project audit tracker the same way.

## Skills Included

### Fiction Workshop
Collaborative fiction writing and editing with 5 editorial personas:
- **Developmental Editor** - Plot, pacing, structure, stakes
- **Line Editor** - Prose rhythm, word choice, "show don't tell"
- **Character Consultant** - Voice consistency, motivation, arc
- **Continuity Tracker** - Timeline, world facts, internal consistency
- **Brainstorm Partner** - "What if" exploration, problem-solving

Includes genre-specific guides for:
- Spy thrillers (tradecraft, tension, moral complexity)
- Hard sci-fi (technical accuracy, worldbuilding, geopolitics)

### Character Archetypes
Fiction-only companion to Fiction Workshop's character work. Two taxonomies plus four analysis modes for using archetypes diagnostically:
- **Narrative-Role Archetypes** - Vogler/Campbell's 8 character functions (Hero, Mentor, Threshold Guardian, Herald, Shapeshifter, Shadow, Trickster, Ally)
- **Personality Archetypes** - Jungian 12 (Mark & Pearson model): Innocent, Everyman, Hero, Caregiver, Explorer, Rebel, Lover, Creator, Jester, Sage, Magician, Ruler
- **Analyzer** - Diagnose or recommend an archetype pairing
- **Audit** - Flag stock/cliché use of an established archetype
- **Conformance** - Check for unexplained archetype drift across chapters
- **Ensemble** - Check cast-level archetype balance and gaps

Archetype is a starting scaffold, not a finished character — pair with Fiction Workshop's Want/Need/Wound/Lie framework to individualize.

### Story Structure
Percentage-anchored macro plot structure, drawn from K.M. Weiland's landmark-beat model and James Scott Bell's signpost catalog:
- **Landmark Beats** - 11-beat skeleton (Hook, Inciting Event, First Plot Point, Pinch Points, Midpoint, Third Plot Point, Climax, Resolution) with percentages and diagnostics
- **Signposts** - Bell's 14 named checkpoints (Disturbance, Mirror Moment, Doorways of No Return, Q Factor, and more), overlaid on the landmarks or placed relatively between them
- **Map** - Place beats and signposts for a story not yet drafted
- **Audit** - Locate where beats actually land in an existing manuscript and flag missing, mistimed, or thin ones

Weiland's beats answer *where* a turning point falls; Bell's signposts answer *what psychological work* it needs to do.

### Narrative Nonfiction
For self-help, prescriptive nonfiction, and structural-argument books with storytelling elements:
- **Transformation Arc** - Reader journey design
- **Metaphor Consistency** - Extended metaphor management
- **Exercise Design** - Practical application sections
- **Reveal Engineering** - Twist/reframe setup and payoff across four patterns:
  - *Permission-reframe* (training-wheels frame released as validation)
  - *Empirical* (counterintuitive data overturns received wisdom)
  - *Structural* (visible surface reframed by hidden mechanism)
  - *Conceptual* (new category installed; old framework dissolved)
- **Voice Editing** - Tone and persona consistency

### Prose Mechanics
Sentence-level diagnostic audits for finished or near-finished drafts (fiction or nonfiction):
- **Active/Passive Audit** - Unjustified passive constructions, hidden agency
- **Parallel Structure Audit** - Broken grammatical parallels in lists, comparisons, series
- **Sentence Length Variance** - Flat-rhythm detection at the paragraph level
- **Accessibility Audit** - Readability scoring and structural accessibility (prose, not WCAG)

Run audits one at a time, in order. Each pass produces a flagged-issues report for author review.

### Avoid AI Writing
Audits and rewrites text to remove AI-ism patterns that make prose sound
machine-generated. Supports two modes:
- **Detect mode** — Flag AI-isms only; no rewriting. Use when auditing
  published content, someone else's writing, or when you want to decide
  yourself what to fix.
- **Rewrite mode** (default) — Flag AI-isms and rewrite the text to fix them.

Recommended workflow: run `avoid-ai-writing` after the line-edit pass in
either `fiction-workshop` or `narrative-nonfiction` to catch any residual
AI patterns before final polish.

Vendored from [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing)
(MIT). See [ATTRIBUTION.md](ATTRIBUTION.md).

## Installation

### Direct from GitHub
```bash
/plugin install github:rhavekost/author-toolkit
```

### For Team Projects
Add to `.claude/settings.json`:
```json
{
  "enabledPlugins": [
    "github:rhavekost/author-toolkit"
  ]
}
```

## Usage

Invoke skills directly:

```bash
/author-toolkit:fiction-workshop
/author-toolkit:character-archetypes
/author-toolkit:story-structure
/author-toolkit:narrative-nonfiction
/author-toolkit:prose-mechanics
/author-toolkit:avoid-ai-writing
```

Once activated, work with the editorial personas:

```
# Fiction
"As developmental editor, analyze Chapter 3"
"As line editor, polish this dialogue"
"Brainstorm mode—I need to solve [plot problem]"

# Character archetypes
"What archetype is this character?"
"Audit this scene for archetype cliché"
"Check archetype conformance for chapters 4-8"
"Run an ensemble balance check on the cast"

# Story structure
"Map the structure for this story"
"Audit this manuscript's structure"
"Check this manuscript for a Faux Climax"

# Nonfiction
"Help me design the transformation arc for my self-help book"
"Check metaphor consistency in chapters 4-8"
"Engineer the reveal for chapter 16"

# Prose mechanics
"Run active/passive audit on chapter 3"
"Run sentence-variance audit on chapter 7"
"Run accessibility audit on the whole manuscript"

# Avoid AI Writing
"Audit this chapter for AI-isms" (detect mode)
"Rewrite this chapter to remove AI patterns" (rewrite mode)
```

## Quick Reference

| Need | Invoke Skill | Then Say |
|------|--------------|----------|
| Fiction writing/editing | `/author-toolkit:fiction-workshop` | "Let's build a story bible" or "As developmental editor, analyze Chapter 3" |
| Developmental pass | `/author-toolkit:fiction-workshop` | "As developmental editor, analyze [chapter]" |
| Line editing | `/author-toolkit:fiction-workshop` | "As line editor, polish [scene]" |
| Character work | `/author-toolkit:fiction-workshop` | "As character consultant, is this in character?" |
| Continuity check | `/author-toolkit:fiction-workshop` | "As continuity tracker, check for inconsistencies" |
| Get unstuck | `/author-toolkit:fiction-workshop` | "Brainstorm mode—I need to [solve problem]" |
| Archetype identification | `/author-toolkit:character-archetypes` | "What archetype is this character?" |
| Archetype cliché check | `/author-toolkit:character-archetypes` | "Audit [scene] for archetype cliché" |
| Archetype drift check | `/author-toolkit:character-archetypes` | "Check archetype conformance for chapters [X-Y]" |
| Cast balance check | `/author-toolkit:character-archetypes` | "Run an ensemble balance check on the cast" |
| Plan new story structure | `/author-toolkit:story-structure` | "Map the structure for this story" |
| Audit existing structure | `/author-toolkit:story-structure` | "Audit this manuscript's structure" |
| Nonfiction writing | `/author-toolkit:narrative-nonfiction` | "Let's build a blueprint for [book]" |
| Reader journey | `/author-toolkit:narrative-nonfiction` | "Design the transformation arc" |
| Metaphor consistency | `/author-toolkit:narrative-nonfiction` | "Check metaphor consistency in chapters 4-8" |
| Exercise design | `/author-toolkit:narrative-nonfiction` | "Design exercises for [concept]" |
| Active/passive pass | `/author-toolkit:prose-mechanics` | "Run active/passive audit on [chapter]" |
| Parallel structure | `/author-toolkit:prose-mechanics` | "Run parallel-structure audit on [chapter]" |
| Sentence variance | `/author-toolkit:prose-mechanics` | "Run sentence-variance audit on [chapter]" |
| Readability audit | `/author-toolkit:prose-mechanics` | "Run accessibility audit on [chapter]" |
| Audit chapter for AI-isms | `/author-toolkit:avoid-ai-writing` | "Detect mode — flag AI patterns in this chapter" |
| Clean AI-isms from chapter | `/author-toolkit:avoid-ai-writing` | "Rewrite mode — remove AI patterns from this chapter" |

## Attribution

This plugin vendors the `avoid-ai-writing` skill by
[Conor Bronsdon (@ConorBronsdon)](https://github.com/conorbronsdon),
sourced from
[conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing)
and licensed under the MIT License. The upstream `LICENSE` and `README` are
preserved unmodified inside
[`skills/avoid-ai-writing/`](skills/avoid-ai-writing/). Full attribution and
vendored commit SHA are recorded in [ATTRIBUTION.md](ATTRIBUTION.md).

## License

MIT. See [LICENSE](LICENSE). Vendored third-party skills retain their
original licenses inside their skill directories — see
[ATTRIBUTION.md](ATTRIBUTION.md) for details.
