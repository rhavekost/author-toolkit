---
name: narrative-nonfiction
description: "Use when writing self-help books, memoirs, or prescriptive guides with story elements. Trigger on: 'self-help book', 'transformation arc', 'metaphor consistency', 'reader journey', 'exercise design', or narrative nonfiction projects."
---

# Narrative Nonfiction Workshop

Workflow for self-help and prescriptive nonfiction using narrative elements and metaphors to guide reader transformation.

**Core concept:** Reader is protagonist; book is map and method; transformation is the contract.

## Session Continuity

Book projects span weeks or months. Claude has no memory between sessions, so the project's blueprint document is your persistent state.

- **At session start:** Read `book-blueprint.md` (or whatever the project calls its blueprint) before doing any other work. Skim recent files in `sessions/` for unresolved threads.
- **At session end:** Write a brief note at `sessions/YYYY-MM-DD_topic-slug.md` summarizing what was done, decisions made, and the stopping point. Two to five sentences is enough.
- **When foundations shift:** Update the blueprint immediately when promise, central metaphor, reader-arc stages, or reveal structure change. The blueprint is the source of truth, not a one-time template.
- **Surface unresolved questions:** At the start of new work, list questions left open from prior sessions and ask the user which to address before continuing.

## When to Use

This skill is for:
- ✅ Self-help and prescriptive nonfiction books
- ✅ Memoirs with lessons or transformation arcs
- ✅ Books using extended metaphors or narrative framing
- ✅ Practical guides that include storytelling elements
- ✅ Reader journey design (before state → after state)
- ✅ Structural-argument nonfiction (books that reframe how readers understand a system or category)

## When NOT to Use

This skill is NOT for:
- ❌ Pure fiction (novels, short stories) - use `fiction-workshop` instead
- ❌ Academic writing or research papers - different conventions
- ❌ Straight journalism or reporting - no transformation arc
- ❌ Technical documentation or how-to guides without story elements
- ❌ Business books focused purely on data/case studies without reader journey

---

## Stage 1: Foundation Building

**Goal:** Establish promise, metaphor system, and transformation arc.

### Initial Questions

1. Target reader? (Demographics + psychographics)
2. Transformation promise?
3. Central metaphor/framing?
4. Reader's "before" and "after" states?
5. Book's unique angle?
6. How much outlined vs. drafted?

### Core Components

**Promise:** What reader gains. "This book will help you [transformation] by [method]"

**Metaphor:** Central metaphor, how it maps to advice, where it helps/misleads

**Reader's Journey:** Entry point (where they start), pain points, resistance, transformation stages, exit point (who they become)

**Twist/Reveal** (if applicable): What's revealed, setup needed, how to earn payoff

Use `assets/book-blueprint-template.md` if needed.

**Exit condition:** Clear grasp of reader, promise, metaphor, arc.

---

## Stage 2: Chapter Development

**Goal:** Draft or refine chapters balancing advice, story, and exercises.

**Chapter structure:** Hook (story/question) → Setup (why this matters) → Content (teaching) → Evidence (stories/research) → Application (exercises) → Bridge (to next)

### Writing Modes

Modes are primarily for Stage 2 (Chapter Development) and Stage 3 (Arc Integrity Check); Stage 1 is freeform foundation-building that does not require mode invocation. Switch between these as needed:

| Mode | Invocation | Focus |
|------|------------|-------|
| **Voice Editor** | "Check voice consistency..." | Tone, metaphor alignment, author persona |
| **Content Editor** | "Evaluate the teaching in..." | Clarity, completeness, accuracy |
| **Exercise Designer** | "Design exercises for..." | Practical application, appropriate difficulty |
| **Metaphor Consultant** | "Check metaphor consistency..." | Extended metaphor alignment, avoiding confusion |
| **Reveal Engineer** | "Set up the reveal..." | Foreshadowing, misdirection, payoff |

Load only the reference file matching the currently invoked mode. Do not preload all references at session start—it wastes context budget. If switching modes mid-session, load the new reference file and treat the prior one as out-of-scope unless the work explicitly bridges both.

For Reveal Engineer specifically: `reveal-engineering.md` is an index across four reveal patterns (permission-reframe, empirical, structural, conceptual). Read its "Choosing a Reveal Pattern" section first, identify which pattern fits the project, then load *only* that pattern's reference file. Don't preload all four.

See `references/` for detailed guidance on each mode.

### Creation Workflow

1. **Purpose Check:** Key takeaway? Where in arc? What must reader believe before next chapter?

2. **Outline Beats:** Hook options, teaching points (2-4), stories/examples, exercises, bridge

3. **Draft:** Write chapter. Use "write like you talk" voice.

4. **Layer Metaphor:** Present but not forced.

5. **Add Exercises:** Use `references/exercise-design.md`

6. **Polish:** Check voice, pacing, reader energy

### Editing Workflow

1. **Read as Target Reader:** Engaged? Understand? Believe I can do this? Overwhelmed or ready?

2. **Diagnose:** Confusion → clarify | Boredom → add story | Resistance → address objections | Overwhelm → simplify

3. **Invoke Mode:** Load relevant reference file

4. **Implement:** Use `str_replace`

---

## Stage 3: Arc Integrity Check

**Goal:** Verify book works as complete transformation journey.

**Read full outline/manuscript for:**

1. **Promise Delivery:** Book delivers promise? Transformation clear and achievable?
2. **Pacing:** Change speed appropriate? Integration plateaus? Energy builds?
3. **Metaphor:** Maintained throughout? Breaks or contradicts? Still serves at end?
4. **Reveal** (if applicable): Twist earned? Seeds planted? Reframe lands emotionally?
5. **Exercise Progression:** Build on each other? Difficulty matches stage? Variety?

### Common Issues

| Symptom | Cause | Fix |
|---------|-------|-----|
| "Too preachy" | Not enough story/example | Add narrative |
| "Too abstract" | Missing concrete advice | Add specific how-to |
| "Overwhelming" | Too much per chapter | Narrow focus, add chapters |
| "Why should I care?" | Missing pain point connection | Open with reader's struggle |
| "I can't do this" | Missing scaffolding | Add smaller steps, examples |

---

## Self-Check: Is This Working?

Use these checkpoints to verify you're following the workflow correctly.

**After Foundation Building:**
- [ ] Can you state the book's promise in one sentence?
- [ ] Can you describe the reader's "before" and "after" states clearly?
- [ ] Do you understand the central metaphor and how it maps to the advice?
- [ ] Can you outline the transformation arc stages without looking at notes?

**After drafting a chapter:**
- [ ] Does the chapter have all six elements: hook, setup, content, evidence, application, bridge?
- [ ] Is the metaphor present but not forced?
- [ ] Is the voice consistent with previous chapters?
- [ ] Would the target reader understand and believe they can apply this?

**After designing an exercise:**
- [ ] Does the exercise difficulty match where the reader is in their journey?
- [ ] Can the reader complete it with the knowledge they have so far?
- [ ] Is it specific enough to be actionable (not "improve your productivity" but "track your time for three days")?
- [ ] Does it build on previous exercises?

**After invoking a mode:**
- [ ] Did you explicitly request "Voice Editor" or "Metaphor Consultant" or specific mode?
- [ ] Is the feedback focused on that mode's domain?
- [ ] Did you avoid mixing concerns (voice + content + exercises all at once)?

**Before claiming "done":**
- [ ] Does the full arc deliver on the promise made in chapter 1?
- [ ] Is the metaphor consistent throughout (or intentionally evolved)?
- [ ] Do exercises progress logically from simple to complex?
- [ ] If there's a reveal/twist, are seeds planted in earlier chapters?

If you answered "no" to any checkpoint, return to that stage before proceeding.

---

## Stopping Points

Each mode and stage has a defined end. Stop at it. Do not auto-advance to the next mode, do not silently expand scope, do not start rewriting when you were asked to diagnose.

| Tool / Stage | Stop when... | Then |
|--------------|--------------|------|
| **Foundation Building (Stage 1)** | The Foundation Building Self-Check passes | Hand back to author. Do not auto-advance into Chapter Development. |
| **Voice Editor** | One pass on the requested scope is complete and findings are reported | Wait for author to apply changes. Do not re-check other chapters unless asked. |
| **Content Editor** | Diagnosis of clarity/completeness/accuracy issues is delivered | Stop. Do not write the fix—that's the author's call. |
| **Exercise Designer** | 2–3 exercise options delivered with rationale for each | Do not pick for the author. Do not embed without confirmation. |
| **Metaphor Consultant** | Consistency report produced (alignments, breaks, suggestions) | Do not rewrite metaphor moments unilaterally. Report and stop. |
| **Reveal Engineer** | Seeding plan or planting recommendations for the current chapter delivered | Do not draft the chapter from the recommendations. They are inputs, not output. |
| **Arc Integrity Check (Stage 3)** | Full-arc report (promise delivery, pacing, metaphor, reveal, exercise progression) delivered | Hand back. Let author decide which findings to act on and in what order. |
| **Session** | Stopping point reached or context window is filling | Update the blueprint if foundations shifted; write a `sessions/` note; stop. |

If the author explicitly asks you to continue past a stopping point, fine—but name what's about to happen ("I'll now move from diagnosis to rewriting Chapter 4's hook") so the scope shift is visible.

---

## Common Mistakes

| Mistake | Why It Happens | Fix |
|---------|---------------|-----|
| **Skipping Foundation Building** | "I just want to start writing" | Without clarity on promise, metaphor, and arc, chapters drift. Spend 30 minutes on blueprint—saves hours of rewriting. |
| **Forcing the metaphor** | Trying to make every sentence fit the frame | Metaphor should illuminate, not constrain. Use it where it helps understanding, skip where it doesn't. Natural beats forced. |
| **Too much teaching, not enough story** | Wanting to share all your knowledge | Readers connect through story first. Aim for 40% story/example, 40% teaching, 20% application. Adjust per chapter needs. |
| **Exercises that don't match reader readiness** | Copying exercise formats from other books | Exercise difficulty must match where reader is in arc. Early chapters = simple reflection. Later chapters = bigger challenges. |
| **Losing voice consistency** | Switching between academic and conversational tone | Pick one voice (usually conversational for self-help) and maintain it. Use "Voice Editor" mode to check consistency. See example below. |
| **Ignoring reader resistance** | Assuming reader agrees with premise | Address objections explicitly. "You might be thinking..." shows you understand their skepticism and builds trust. |
| **Reveal without setup** | Planning twist ending but not planting seeds | If book has reframe/reveal, every chapter needs subtle foreshadowing. Use "Reveal Engineer" mode to plant and track seeds. |

### Example: Voice Consistency

**Inconsistent voice (Chapter 1 conversational, Chapter 4 academic):**

Chapter 1: "You know that feeling of finishing a 'productive' day without accomplishing anything important? That's your brain telling you something's off."

Chapter 4: "Empirical research demonstrates that individuals who engage in time-blocking methodologies exhibit significantly higher levels of task completion and subjective productivity (Chen et al., 2019)."

**Consistent voice (both conversational):**

Chapter 4: "Here's what the research shows: people who use time-blocking finish more important work. One study tracked 500 knowledge workers for six months and found time-blockers completed 60% more high-priority projects. Your instinct was right."

**The difference:** Conversational voice maintains "you/your" address, uses plain language, and connects research to reader experience.

### Example: Forced vs. Natural Metaphor

**Book metaphor: "Think Like an Architect"**

**Forced:** "When you wake up in the morning, draft your day's blueprint. Pour your foundation coffee. Every moment is a chance to design your life's structure."

**Natural:** "Architects plan for what they need before breaking ground. When you start a project, identify your requirements first—don't just start building and hope it works out."

**The difference:** Natural metaphor illuminates specific advice. Forced metaphor tries to shoehorn every detail into the frame.

### Example: Exercise Design with Scaffolding

**Early chapter exercise (reader just learning concept):**
```
EXERCISE: Track Your Time
This week, log what you actually do for three full workdays.
Just notice. Don't judge yourself or try to optimize yet.
Write down: Where did your time go? When were you most focused?
```

**Later chapter exercise (reader has practiced basics):**
```
EXERCISE: Block Your First Deep Work Session
Choose one morning this week (not your busiest day—start manageable).
1. Identify your most important task
2. Block 90 minutes using the protocol from Chapter 3
3. Practice saying it out loud three times before the actual conversation
4. Deliver the boundary
5. Journal: What happened? How did you feel? What would you do differently?
```

**The difference:** Early exercises are observation-only with no pressure. Later exercises build on established skills and ask for action.

---

## Quick Reference Commands

| Need | Command |
|------|---------|
| Start new project | "Let's build a blueprint for [project]" |
| Voice check | "Check voice consistency in [chapter]" |
| Content edit | "Evaluate the teaching in [chapter]" |
| Design exercises | "Design exercises for [concept]" |
| Metaphor check | "Check metaphor consistency across [chapters]" |
| Setup the reveal | "Help me plant seeds for [reveal] in [chapter]" |
| Arc review | "Review the transformation arc in [outline/draft]" |

---

## Finding Format

This skill's diagnostic modes (reveal-engineering plant/payoff gaps,
metaphor-consistency checks, reader-journey audits) conform to
`../../references/finding-schema.json`: `audit` = the mode
name, `technique` = the specific craft element (e.g. "Reveal plant without
payoff"), `severity`, `location`, `issue`, `confidence: "judgment"`,
`exemplar` optional. Exercise-design and transformation-arc scaffolding
output (generative, not diagnostic) is NOT in scope.

---

## Files

- `references/transformation-arc.md` - Reader journey structure
- `references/metaphor-consistency.md` - Extended metaphor management
- `references/exercise-design.md` - Practical application design
- `references/reveal-engineering.md` - Reveal-pattern index; permission-reframe pattern in detail
- `references/empirical-reveal.md` - Counterintuitive-data reveal pattern (Freakonomics-style)
- `references/structural-reveal.md` - Invisible-mechanism reveal pattern (Bastiat-style)
- `references/conceptual-reveal.md` - Category-shift reveal pattern (Antifragile-style)
- `references/voice-editing.md` - Tone and persona consistency
- `assets/book-blueprint-template.md` - Book planning document
- `assets/chapter-template.md` - Chapter structure template
