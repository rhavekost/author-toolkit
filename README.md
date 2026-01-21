# Writing Skills for Claude Code

A Claude Code plugin with specialized skills for fiction and narrative nonfiction authors.

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
For self-help and prescriptive nonfiction with storytelling elements:
- **Transformation Arc** - Reader journey design
- **Metaphor Consistency** - Extended metaphor management
- **Exercise Design** - Practical application sections
- **Reveal Engineering** - Twist/reframe setup and payoff
- **Voice Editing** - Tone and persona consistency

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

Skills activate automatically based on context, or invoke them directly:

```
# Fiction
"As developmental editor, analyze Chapter 3"
"As line editor, polish this dialogue"
"Brainstorm mode—I need to solve [plot problem]"

# Nonfiction
"Help me design the transformation arc for my self-help book"
"Check metaphor consistency in chapters 4-8"
"Engineer the reveal for chapter 16"
```

## Quick Reference

| Need | Command |
|------|---------|
| Start fiction project | "Let's build a story bible for [project]" |
| Developmental pass | "As developmental editor, analyze [chapter]" |
| Line edit | "As line editor, polish [scene]" |
| Character check | "As character consultant, is this in character?" |
| Continuity audit | "As continuity tracker, check for inconsistencies" |
| Get unstuck | "Brainstorm mode—I need to [solve problem]" |
| Start nonfiction project | "Let's build a blueprint for [book]" |
| Reader journey | "Design the transformation arc" |
| Metaphor check | "Check metaphor consistency" |
| Exercise design | "Design exercises for [concept]" |

## License

MIT
