---
name: fiction-workshop
description: "Use when writing or editing novels, short stories, or any fiction manuscript. Trigger on: 'write fiction', 'edit my novel', 'developmental edit', 'line edit', 'character voice', 'plot hole', 'brainstorm', or fiction writing tasks."
---

# Fiction Workshop

Editorial workflow for collaborative fiction writing in three stages: Story Bible Building, Chapter Development, and Reader Testing.

## Session Continuity

Novel projects span weeks or months. Claude has no memory between sessions, so the Story Bible is your persistent state.

- **At session start:** Read `story-bible.md` (or whatever the project calls it) before doing any other work. Skim recent files in `sessions/` for unresolved threads.
- **At session end:** Write a brief note at `sessions/YYYY-MM-DD_topic-slug.md` summarizing what was done, decisions made, and the stopping point. Two to five sentences is enough.
- **When foundations shift:** Update the Story Bible immediately when premise, character bios, world rules, or major plot turns change. The Story Bible is the source of truth, not a one-time template.
- **Surface unresolved questions:** At the start of new work, list questions left open from prior sessions and ask the user which to address before continuing.

## When to Use

This skill is for:
- ✅ Long-form fiction (novels, novellas, short story collections)
- ✅ Multi-chapter manuscripts requiring character/plot consistency
- ✅ Fiction projects needing developmental or line editing
- ✅ Stories with complex worldbuilding or multiple POV characters

## When NOT to Use

This skill is NOT for:
- ❌ Flash fiction or single scenes (< 2000 words) - too lightweight for the workflow
- ❌ Poetry or experimental prose - needs different editorial approach
- ❌ Screenplays or stage plays - different format conventions
- ❌ Technical writing, documentation, or academic papers
- ❌ Business writing or marketing copy

For narrative nonfiction (memoir, self-help with story elements), use the `narrative-nonfiction` skill instead.

## Editorial Personas

Personas are primarily for Stage 2 (Chapter Development) and Stage 3 (Reader Testing); Stage 1 is freeform Story Bible building that does not require persona invocation. Switch between these roles by requesting a specific lens:

| Role | Invocation | Focus |
|------|------------|-------|
| **Developmental Editor** | "As developmental editor..." | Plot, pacing, structure, stakes, theme |
| **Line Editor** | "As line editor..." | Prose rhythm, word choice, "show don't tell" |
| **Character Consultant** | "As character consultant..." | Voice consistency, motivation, arc, relationships |
| **Continuity Tracker** | "As continuity tracker..." | Timeline, world facts, internal consistency |
| **Brainstorm Partner** | "Brainstorm mode..." | "What if" exploration, problem-solving, unsticking |

Load only the reference file matching the currently invoked persona. Do not preload all references at session start—it wastes context budget. If switching personas mid-session, load the new reference file and treat the prior one as out-of-scope unless the work explicitly bridges both.

See `references/` for detailed guidance on each role.

---

## Stage 1: Story Bible Building

**Goal:** Establish shared story foundation before drafting or editing.

### Initial Questions

1. Genre and target reader?
2. Core premise/logline?
3. Protagonist: who they are, what they want?
4. Central conflict?
5. Reader's intended emotional journey?
6. How much written vs. planned?

### Story Bible Components

**Plot:** Premise, three-act structure/beat sheet, major turns, ending (even if rough)

**Characters:** Protagonist (want/need/wound/arc), antagonist (motivation/threat), supporting cast (function/relationships), POV voice notes

**World:** Setting (time/place/rules), tech/magic systems, social structures, sensory palette

**Theme:** Central question, moral argument, recurring motifs

If a Story Bible document exists, review it. If not, offer to create one using `assets/story-bible-template.md`.

**Example Story Bible entry (character):**
```
ALEX CHEN - Protagonist
Want: Expose the conspiracy and clear her name
Need: Learn to trust her instincts over institutional authority
Wound: Mentor betrayed her at previous agency, causing career setback
Arc: Lone wolf → realizes she needs allies → builds trust with team
Voice notes: Analytical, dry humor when stressed, avoids emotional language
Key relationship: Tension with Handler (wants to trust, can't fully)
```

**Exit condition:** Confident grasp of story fundamentals. Can discuss character motivations, predict plot implications, and identify thematic threads without asking basic questions.

---

## Stage 2: Chapter Development

**Goal:** Draft or refine chapters through brainstorm → curate → draft → refine cycles.

**Drafting new?** → Creation workflow | **Editing existing?** → Editing workflow

### Creation Workflow

1. **Scene Planning**
   - What must happen (plot)? Whose POV?
   - Chapter's emotional arc?
   - What reader learns/feels by end?

2. **Brainstorm Beats** (5-15 options): Opening hooks, key moments, dialogue, sensory details, closing

   **Example (thriller scene):** Same car outside coffee shop three days running | Phone buzzing at 3am with blocked caller | Surveillance photo under door | Colleague mentions detail only surveillance would know | Camera lens reflection in window | Dead drop cleaned out | Safe house key doesn't fit | Contact misses first check-in

   Then curate: "Which create immediate tension? Combine any?"

3. **Curate:** Ask which to keep, combine, or discard. Reasons help calibrate.

4. **Draft:** Write chapter. Use `str_replace` for revisions, never reprint.

5. **Refine:** Iterate on feedback. After 3 passes with minimal changes, ask: "What could be cut?"

### Editing Workflow

1. **Read and Diagnose:** What chapter tries to do, where it succeeds, where it loses energy/clarity

2. **Invoke Persona:** Structure/pacing → Developmental | Prose → Line | Voice → Character | Facts → Continuity

3. **Propose Changes:** Specific, surgical edits with brief "why"

4. **Implement:** Use `str_replace`. Link to file after changes.

5. **Iterate:** Until chapter achieves purpose

### Role-Specific Guidance

When a specific editorial persona is invoked, load the corresponding reference file:

- Developmental editing → `references/developmental-editing.md`
- Line editing → `references/line-editing.md`
- Character work → `references/character-work.md`
- Continuity → `references/continuity-tracking.md`
- Brainstorming → `references/brainstorming.md`
- Thriller-specific craft → `references/thriller-craft.md`
- Sci-fi worldbuilding → `references/scifi-worldbuilding.md`

---

## Stage 3: Reader Testing

**Goal:** Verify manuscript works without author context.

**Using fresh sub-agent (no story bible):**

1. **Comprehension:** Can they summarize plot, understand motivations, identify stakes?
2. **Engagement:** Where did they lose interest, have questions, feel confused?
3. **Emotional:** Did key moments land? Ending satisfying? Theme clear?

**Common issues:** Unclear motivation | Pacing lags | Unearned moments | Confusion

**If struggles:** Identify gap → Return to Stage 2 → Re-test

**Exit condition:** Reader understands and engages without author explanations.

---

## Self-Check: Is This Working?

Use these checkpoints to verify you're following the workflow correctly.

**After Story Bible building:**
- [ ] Can you describe the protagonist's want vs. need without re-reading notes?
- [ ] Can you predict how the antagonist would react to a new scenario?
- [ ] Do you understand the thematic question the book explores?
- [ ] Could you summarize the three-act structure in 2-3 sentences?

**After invoking a persona:**
- [ ] Did you explicitly say "As [persona name]..." in your request?
- [ ] Is the feedback focused on that persona's domain (developmental = structure, line = prose)?
- [ ] Did you avoid mixing feedback from multiple personas in one pass?

**After making edits:**
- [ ] Did you use `str_replace` for surgical changes, not reprinting entire sections?
- [ ] Can you articulate what changed and why it's better?
- [ ] Is the change consistent with the Story Bible (character voice, plot logic, world rules)?

**After brainstorming:**
- [ ] Did you generate 5+ options before selecting one?
- [ ] Did you curate collaboratively rather than taking the first suggestion?
- [ ] Can you explain why the selected option is stronger than alternatives?

**Before claiming "done":**
- [ ] Has a fresh sub-agent (without Story Bible context) read the manuscript?
- [ ] Did the fresh reader understand plot, character motivations, and stakes?
- [ ] Were any gaps or confusion points identified and addressed?

If you answered "no" to any checkpoint, return to that stage before proceeding.

---

## Stopping Points

Each persona and stage has a defined end. Stop at it. Do not auto-advance to the next persona, do not silently expand scope, do not start drafting when you were asked to diagnose.

| Tool / Stage | Stop when... | Then |
|--------------|--------------|------|
| **Story Bible Building (Stage 1)** | The Story Bible Self-Check passes | Hand back to author. Do not auto-advance into drafting. |
| **Developmental Editor** | One full structural pass on the requested scope is complete and issues list is delivered | Wait for author to apply edits. Do not loop into rewriting unless explicitly asked. |
| **Line Editor** | One chapter (or named scope) is line-edited; after 3 passes with minimal changes, ask "what could be cut?" once | If no further direction, stop. Line editing has a natural ceiling. |
| **Character Consultant** | One consult on the named character/scene is complete | Do not reflexively check other characters or scenes. Wait for the next invocation. |
| **Continuity Tracker** | Audit produces flag list | Stop. Do not fix automatically. Author decides which flags are real and how to resolve. |
| **Brainstorm Partner** | Curate step produces a chosen direction (or 5+ options reviewed and declined) | Hand back. Do not draft into a chapter unless explicitly asked. |
| **Reader Testing (Stage 3)** | Fresh sub-agent's report is delivered | Stop. Author decides whether to return to Stage 2 and on which findings. |
| **Session** | Stopping point reached or context window is filling | Update the Story Bible if foundations shifted; write a `sessions/` note; stop. |

If the author explicitly asks you to continue past a stopping point, fine—but name what's about to happen ("I'll now move from continuity audit to applying fixes") so the scope shift is visible.

---

## Common Mistakes

| Mistake | Why It Happens | Fix |
|---------|---------------|-----|
| **Skipping Story Bible** | "I know my story well enough" | Story Bible isn't for you—it's for Claude. Without shared context, feedback will miss key story elements. Build it. |
| **Generic feedback without persona** | Rushing, forgetting to invoke specific role | Explicitly say "As developmental editor..." or "As line editor..." in your prompt. Different lenses catch different issues. |
| **Reprinting entire chapters** | Habit from other editing contexts | Use `str_replace` for surgical edits only. Reprinting burns context and makes changes hard to track. Link to file after edits. |
| **Jumping to line edits before structure** | Wanting to "fix" prose immediately | If plot/pacing/character issues exist, line edits are wasted effort. Always developmental pass first. See example below. |
| **Skipping Reader Testing** | "I've read it so many times already" | You have author context. Reader Testing uses fresh sub-agent without story bible to catch gaps readers will hit. |
| **Too many personas at once** | Trying to fix everything in one pass | Invoke one persona per pass. Developmental → Character → Line → Continuity. Focused feedback is actionable feedback. |
| **Brainstorming without curation** | Taking first idea that sounds good | Generate 5-15 options, then curate. First idea is rarely best idea. Quantity enables quality. |

### Example: Developmental vs. Line Editing

**Same passage, different lenses:**

> Sarah walked into the office. Her boss looked angry. "We need to talk," he said. She sat down nervously.

**Line Editor feedback (prose-level):**
- "Walked" is weak—try "strode" or "slipped"
- "Looked angry" tells rather than shows—describe furrowed brow, tight jaw
- "Nervously" is an adverb crutch—show the nervousness through action

**Developmental Editor feedback (structure/stakes):**
- What does Sarah want in this scene? What does her boss want?
- If this is the confrontation, we need setup—what's the conflict history?
- Stakes feel low—why does this conversation matter to the story?
- Pacing: Is this the right chapter for this confrontation, or should tension build longer?

**The difference:** Line edits polish sentences. Developmental edits ensure the scene earns its place in the story. Always developmental first.

---

## Quick Reference Commands

| Need | Command |
|------|---------|
| Start new project | "Let's build a story bible for [project]" |
| Developmental pass | "As developmental editor, analyze [chapter/section]" |
| Line edit | "As line editor, polish [scene/passage]" |
| Character check | "As character consultant, is [character]'s [action] in character?" |
| Continuity audit | "As continuity tracker, check [chapters X-Y] for inconsistencies" |
| Get unstuck | "Brainstorm mode—I need to [solve problem]" |
| Test readability | "Run a fresh read on [chapter/section]" |

---

## Finding Format

When this skill's diagnostic modes (developmental-editing critique,
continuity-tracking flags) produce findings, emit them conforming to
`../../references/finding-schema.json`: `audit` (use the mode
name, e.g. "developmental-editing"), `technique` (the named craft
technique — e.g. "Want/Need/Wound/Lie alignment"), `severity`
(note/suggestion/warning), `location` (file/line/quote), `issue`,
`confidence` ("judgment" — this skill has no deterministic component), and
optionally `exemplar` (a one-sentence illustration inline, since this
skill has no curated exemplar library yet — grow one opportunistically).
Brainstorming and drafting-proposal output is NOT in scope for this
contract.

---

## Files

- `references/developmental-editing.md` - Plot, structure, pacing analysis (see also the `story-structure` skill for landmark-beat percentages and signpost diagnostics)
- `references/line-editing.md` - Prose-level refinement
- `references/character-work.md` - Voice, motivation, arc tracking (see also the `character-archetypes` skill for role/personality archetype analysis)
- `references/continuity-tracking.md` - Timeline and fact consistency
- `references/brainstorming.md` - Idea generation techniques
- `references/thriller-craft.md` - Genre-specific guidance for suspense
- `references/scifi-worldbuilding.md` - Technical accuracy, speculation rules
- `assets/story-bible-template.md` - Blank story bible structure
- `assets/scene-worksheet.md` - Scene-level analysis template
