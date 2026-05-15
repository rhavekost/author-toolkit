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

### Narrative Nonfiction
For self-help, prescriptive nonfiction, and structural-argument books with storytelling elements:
- **Transformation Arc** - Reader journey design
- **Metaphor Consistency** - Extended metaphor management
- **Exercise Design** - Practical application sections
- **Reveal Engineering** - Twist/reframe setup and payoff (permission-reframe pattern)
- **Voice Editing** - Tone and persona consistency

### Prose Mechanics
Sentence-level diagnostic audits for finished or near-finished drafts (fiction or nonfiction):
- **Active/Passive Audit** - Unjustified passive constructions, hidden agency
- **Parallel Structure Audit** - Broken grammatical parallels in lists, comparisons, series
- **Sentence Length Variance** - Flat-rhythm detection at the paragraph level
- **Accessibility Audit** - Readability scoring and structural accessibility (prose, not WCAG)

Run audits one at a time, in order. Each pass produces a flagged-issues report for author review.

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
/author-toolkit:narrative-nonfiction
/author-toolkit:prose-mechanics
```

Once activated, work with the editorial personas:

```
# Fiction
"As developmental editor, analyze Chapter 3"
"As line editor, polish this dialogue"
"Brainstorm mode—I need to solve [plot problem]"

# Nonfiction
"Help me design the transformation arc for my self-help book"
"Check metaphor consistency in chapters 4-8"
"Engineer the reveal for chapter 16"

# Prose mechanics
"Run active/passive audit on chapter 3"
"Run sentence-variance audit on chapter 7"
"Run accessibility audit on the whole manuscript"
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
| Nonfiction writing | `/author-toolkit:narrative-nonfiction` | "Let's build a blueprint for [book]" |
| Reader journey | `/author-toolkit:narrative-nonfiction` | "Design the transformation arc" |
| Metaphor consistency | `/author-toolkit:narrative-nonfiction` | "Check metaphor consistency in chapters 4-8" |
| Exercise design | `/author-toolkit:narrative-nonfiction` | "Design exercises for [concept]" |
| Active/passive pass | `/author-toolkit:prose-mechanics` | "Run active/passive audit on [chapter]" |
| Parallel structure | `/author-toolkit:prose-mechanics` | "Run parallel-structure audit on [chapter]" |
| Sentence variance | `/author-toolkit:prose-mechanics` | "Run sentence-variance audit on [chapter]" |
| Readability audit | `/author-toolkit:prose-mechanics` | "Run accessibility audit on [chapter]" |

## License

MIT
