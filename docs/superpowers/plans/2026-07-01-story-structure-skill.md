# Story Structure Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a new standalone `story-structure` skill (a percentage-anchored landmark-beat skeleton from K.M. Weiland, overlaid with James Scott Bell's 14-signpost catalog, plus Map/Audit modes) to the `author-toolkit` plugin, wire it into `fiction-workshop`, and update the root README and plugin metadata.

**Architecture:** This repo has no code and no test runner — it is a Claude Code plugin made entirely of skill markdown files (`SKILL.md` + `references/*.md` + `assets/*.md`), consumed by an agent at runtime. There is nothing to compile or unit-test. Every task's "test cycle" is therefore a **structural verification pass**: grep-based checks that required sections/entries exist, and a placeholder scan — run in place of a test suite. This mirrors how `character-archetypes` (the most recently added skill) is structured; this plan follows its established patterns (frontmatter format, `references/`+`assets/` split, Stopping Points / Common Mistakes tables) rather than inventing new ones.

**Tech Stack:** None — Markdown files only, versioned via `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`.

## Global Constraints

- New skill lives at `skills/story-structure/` with this exact file tree:
  ```
  skills/story-structure/
    SKILL.md
    references/
      landmark-beats.md
      signposts.md
      structure-map.md
      structure-audit.md
    assets/
      structure-profile-template.md
  ```
- `SKILL.md` frontmatter must match the exact two-field format used by sibling skills (`name`, `description` only — see `skills/character-archetypes/SKILL.md:1-4`).
- `description` frontmatter field must include these trigger phrases verbatim: "story structure," "plot point," "inciting event," "midpoint," "structure audit," "structure map," "signpost scene," "mirror moment."
- Reference files use a plain `# Title` header, no YAML frontmatter — confirmed pattern from every existing `references/*.md` file in this repo.
- The landmark beat skeleton is exactly these 11 beats, in this order, with these percentages (reconciled from K.M. Weiland's *5 Secrets of Story Structure* and *Structuring Your Novel*): Hook (opening), Inciting Event (~12%), Key Event (end of Act 1), First Plot Point (25%, range 18–27%), First Pinch Point (37.5%), Midpoint/Moment of Truth (50%), Second Pinch Point (62.5%), Third Plot Point (70–75%), Third Act Turning Point (88%), Climactic Moment (90–98%), Resolution (final 1–2%).
- Two named failure-mode diagnostics must appear in `landmark-beats.md`, each with Weiland's own diagnostic test: the Inciting Event / Key Event / First Plot Point confusion, and the Faux Climax trap.
- Bell's signpost catalog is exactly these 14, in this order, from *Super Structure*: Disturbance, Care Package, Argument Against Transformation, Trouble Brewing, Doorway of No Return #1, Kick in the Shins, Mirror Moment, Pet the Dog, Doorway of No Return #2, Mounting Forces, Lights Out, Q Factor, Final Battle, Transformation.
- Six of the 14 signposts overlay a landmark beat directly and must be cross-referenced as such in `signposts.md`: Disturbance→Hook/Inciting Event, Doorway #1→First Plot Point, Mirror Moment→Midpoint, Doorway #2→Third Plot Point, Final Battle→Climactic Moment, Transformation→Climax/Resolution. The other 8 (Care Package, Argument Against Transformation, Trouble Brewing, Kick in the Shins, Pet the Dog, Mounting Forces, Lights Out, Q Factor) get relative (not percentage) placement per Bell's own guidance.
- Two modes, one reference file each: **Map** (outline-stage, for a story not yet drafted) and **Audit** (draft-stage, for an existing manuscript). Map hands back a Structure Map block; Audit hands back a flagged-beat report. Neither writes to the Story Bible directly.
- Scope is macro/plot structure only. Do **not** add scene/sequel micro-structure content (already covered by `fiction-workshop/references/developmental-editing.md`'s Scene-Level section) and do **not** add full Lie/Ghost/Wound character-arc mechanics (already covered by `fiction-workshop/references/character-work.md`'s Core Four). Cross-link to both instead of duplicating.
- Do not modify `narrative-nonfiction`, `prose-mechanics`, `avoid-ai-writing`, or `character-archetypes`.
- Integration footprint into `fiction-workshop` is exactly three edits: a short cross-link inserted into `developmental-editing.md`'s Act-Level section, a short cross-link inserted into `character-work.md`'s Arc Milestones section, and one updated line in `SKILL.md`'s Files list (the `developmental-editing.md` entry). Do not modify `fiction-workshop/assets/story-bible-template.md` itself — the new `structure-profile-template.md` is a standalone paste-in block, same rule `character-archetypes/assets/archetype-profile-template.md` follows for character entries.
- `README.md` gets a new "Story Structure" subsection under "Skills Included," placed directly after "Character Archetypes" and before "Narrative Nonfiction," plus an invocation line, a usage example block, and Quick Reference rows — matching the exact formatting of the `character-archetypes` entries already there.
- Plugin version bumps from `1.2.0` to `1.3.0` in both `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` (new feature, no breaking changes → minor bump). Add `"story-structure"` to the `keywords` array in `plugin.json` only (`marketplace.json` has no `keywords` field). Do not change `description` in either file.
- No placeholder text anywhere (no "TBD", "TODO", "fill in", bracketed blanks) in any new or modified file except `assets/structure-profile-template.md`, whose bracketed fields are its intended fill-in-the-blank design (matching `assets/archetype-profile-template.md`'s existing pattern).

---

### Task 1: Scaffold the skill and write `SKILL.md`

**Files:**
- Create: `skills/story-structure/SKILL.md`

**Interfaces:**
- Produces: The skill's frontmatter `name: story-structure`, which every later task's files live under. Produces the "Files" list that Tasks 2–6 must each be reflected in.
- Consumes: Nothing from other tasks (entry point), but forward-references the four reference files and one asset file Tasks 2–6 create.

- [ ] **Step 1: Create the directory structure**

```bash
mkdir -p skills/story-structure/references skills/story-structure/assets
```

- [ ] **Step 2: Write `skills/story-structure/SKILL.md`**

```markdown
---
name: story-structure
description: "Use when planning or diagnosing a novel's macro plot structure. Trigger on: 'story structure', 'plot point', 'inciting event', 'midpoint', 'structure audit', 'structure map', 'signpost scene', 'mirror moment', or macro-structure analysis."
---

# Story Structure

A percentage-anchored landmark-beat skeleton (K.M. Weiland's *5 Secrets of Story Structure* / *Structuring Your Novel*) overlaid with James Scott Bell's 14-signpost catalog (*Super Structure*) — plus two modes for using them: mapping a new story's structure before drafting, and auditing an existing manuscript against it.

Weiland's beats answer **where** a turning point should fall; Bell's signposts answer **what psychological or emotional work** that turning point needs to do. Together they give a placement skeleton with content diagnostics at each joint, not just a percentage ladder.

## When to Use

This skill is for:
- ✅ Fiction manuscripts — novels, novellas, short stories
- ✅ Placing landmark beats (Inciting Event, Plot Points, Pinch Points, Midpoint, Climax) into a new outline before drafting
- ✅ Checking where beats actually land in an existing draft, by approximate percentage
- ✅ Checking whether a beat that's present is doing the psychological work it needs to (via Bell's signposts)
- ✅ Catching two specific, commonly-missed failure modes: Inciting Event/Key Event/First Plot Point confusion, and the Faux Climax trap

## When NOT to Use

This skill is NOT for:
- ❌ Scene-level micro-structure (Goal/Conflict/Outcome, Scene/Sequel) — use `fiction-workshop`'s `references/developmental-editing.md` Scene-Level section instead.
- ❌ Character-arc mechanics (Lie, Ghost, Wound, Thematic Truth) — use `fiction-workshop`'s `references/character-work.md` Core Four instead. This skill only notes *which* structural beat is where the Lie is tested (Third Plot Point) and resolved (Climax).
- ❌ Narrative nonfiction structure — use `narrative-nonfiction`'s transformation-arc guidance instead; this skill's beats assume a plotted fiction conflict.
- ❌ Prose-level pacing (sentence rhythm, word choice) — use `prose-mechanics`.

## Session Continuity

Structure placement is meant to persist in the project's Story Bible, not be re-derived each session.

- **At session start:** If a Story Bible exists, check its "Plot Foundation" section for an existing Structure Profile block (see `assets/structure-profile-template.md`). Don't re-run Map on a story that already has one unless the author asks for a re-check.
- **When a beat is newly placed or moved:** Hand the profile block back to the author to paste into the Story Bible yourself — this skill does not write to the Story Bible directly (see each mode's stop condition below).

## The Landmark Beat Skeleton

Full skeleton, percentages, and the two named failure-mode diagnostics (Inciting/Key/First-Plot-Point confusion, Faux Climax): `references/landmark-beats.md`.

## Bell's 14 Signposts

Full catalog, in Bell's own order, cross-referenced to the landmarks above where they overlay one: `references/signposts.md`.

## The Two Modes

| Mode | Invocation | Question | Reference file |
|---|---|---|---|
| **Map** | "Map the structure for this story" | Where should each beat and signpost land, for a story not yet fully drafted? | `references/structure-map.md` |
| **Audit** | "Audit this manuscript's structure" | Where do beats actually land, and is each doing its job? | `references/structure-audit.md` |

**Ordering guidance:** Map is for pre-draft planning; Audit is for anything already written. They are not sequential stages of one session — run whichever mode matches the story's current stage.

Load only the reference file matching the currently invoked mode, plus `landmark-beats.md` and `signposts.md` (both modes need both). Do not preload mode files you're not running.

## Workflow

1. **Identify the mode** the author is invoking (see table above). If unclear, ask.
2. **Load `references/landmark-beats.md` and `references/signposts.md`**, plus the mode file for the identified mode.
3. **Run the mode's workflow** exactly as documented in its reference file.
4. **Stop at the mode's documented stop condition** (see Stopping Points below). Hand results back to the author.
5. **If a new or changed Structure Profile results**, offer the `assets/structure-profile-template.md` block for the author to paste into their Story Bible's Plot Foundation section — do not write it there yourself.

## Integration with `fiction-workshop`

- `fiction-workshop/references/developmental-editing.md`'s Act-Level section links here for the deeper percentage-anchored skeleton and signpost content-checks.
- `fiction-workshop/references/character-work.md`'s Arc Milestones section links here, noting Third Plot Point and Climax as the beats where the Lie is tested and resolved.
- `assets/structure-profile-template.md` is designed to paste directly into the Story Bible's existing "Plot Foundation → Three-Act Structure" section (see `fiction-workshop/assets/story-bible-template.md`), adding finer beat percentages and signpost notes on top of the existing Act I/Midpoint/Act II-B/Act III placeholders.
- This skill never restructures `fiction-workshop/assets/story-bible-template.md` — it only adds an optional block.

## Stopping Points

Each mode has a defined end. Stop at it. Do not auto-advance to the other mode, do not silently expand scope, do not write to the Story Bible without being asked.

| Mode | Stops when... | Then |
|---|---|---|
| **Map** | Structure Map block completed for all 11 landmarks | Hand back for author confirmation. Do not auto-write to Story Bible. |
| **Audit** | Flagged-beat report delivered (missing/mistimed/thin beats, Faux Climax check) | Stop. No auto-rewrite — author decides which flags to act on. |

## Common Mistakes

| Mistake | Fix |
|---|---|
| Treating the percentages as exact page counts | Weiland's own framing: aim for rough quarters, not surgical precision — a beat within a few points of its mark is fine |
| Conflating Inciting Event, Key Event, and First Plot Point into one beat | They can be three distinct scenes with three distinct jobs — see `landmark-beats.md`'s callout |
| Declaring an early goal-achieved scene "the climax" | Check for Faux Climax — is there a bigger obstacle still standing between the protagonist and the true goal? |
| Running Audit on a story with no draft yet | Audit needs actual manuscript text to locate beats in — use Map instead for pre-draft planning |
| Checking only placement, not content | A beat can land at the right percentage and still be hollow — always run the matching Bell signpost content-check too |

## Quick Reference Commands

| Need | Command |
|---|---|
| Plan a new story's structure | "Map the structure for this story" |
| Check an existing draft | "Audit this manuscript's structure" |
| Check one beat's placement | "Where does the Midpoint land in this draft?" |
| Check for a specific trap | "Check this manuscript for a Faux Climax" |

---

## Files

- `references/landmark-beats.md` - The 11-beat percentage skeleton, diagnostics, two failure-mode callouts
- `references/signposts.md` - Bell's full 14-signpost catalog, cross-referenced to the landmarks
- `references/structure-map.md` - Map mode workflow
- `references/structure-audit.md` - Audit mode workflow
- `assets/structure-profile-template.md` - Story Bible block for a story's structure profile
```

- [ ] **Step 3: Verify structure**

```bash
grep -c "^---$" skills/story-structure/SKILL.md
```
Expected: `2` (opening and closing frontmatter fence).

```bash
grep -E "^## (When to Use|When NOT to Use|Session Continuity|The Landmark Beat Skeleton|Bell's 14 Signposts|The Two Modes|Workflow|Integration with|Stopping Points|Common Mistakes|Quick Reference Commands|Files)$" skills/story-structure/SKILL.md | wc -l
```
Expected: `12` (all twelve required sections present).

```bash
grep -in "TBD\|TODO\|fill in" skills/story-structure/SKILL.md
```
Expected: no output (empty).

- [ ] **Step 4: Commit**

```bash
git add skills/story-structure/SKILL.md
git commit -m "feat: scaffold story-structure skill with SKILL.md"
```

---

### Task 2: Write `references/landmark-beats.md`

**Files:**
- Create: `skills/story-structure/references/landmark-beats.md`

**Interfaces:**
- Consumes: Nothing from other tasks.
- Produces: The 11 beat names and percentages that `references/signposts.md`, `references/structure-map.md`, `references/structure-audit.md`, and `assets/structure-profile-template.md` all reference by exact name.

- [ ] **Step 1: Write `skills/story-structure/references/landmark-beats.md`**

```markdown
# Landmark Beats Reference

The 11 beats that divide a novel's macro structure, reconciled from K.M. Weiland's *5 Secrets of Story Structure* and *Structuring Your Novel*. Percentages are fractions of total manuscript length, not fixed word counts, and are explicitly flexible — Weiland's own guidance is to aim for rough quarters, not surgical precision.

## The 11 Beats

| # | Beat | Placement | Function | Diagnostic |
|---|---|---|---|---|
| 1 | **Hook** | Opening page/line | Poses the story's driving question | Does the opening line/scene raise an implicit or explicit question that makes a reader want the next line? |
| 2 | **Inciting Event** | ~12% | First touch of conflict on the Normal World; often initially resisted | Does this scene touch the protagonist's Normal World with the conflict for the first time, without yet fully engulfing them? |
| 3 | **Key Event** | End of Act 1, may coincide with First Plot Point | The moment the protagonist *leaves* the Normal World (physically or mentally) | Can you point to the exact moment the character exits — not merely encounters — the old world? |
| 4 | **First Plot Point** | 25% (range ~18–27%) | Point of no return; enters the "adventure world" | Is this genuinely irreversible and dynamic, not just a bigger version of earlier events? |
| 5 | **First Pinch Point** | 37.5% (3/8 mark) | Antagonist "flexes muscle"; delivers new clues about the conflict's true nature | Does it foreshadow the Midpoint's Moment of Truth with real new information, not just tension? |
| 6 | **Midpoint / Moment of Truth** | 50% | Reaction → action pivot; protagonist grasps the central truth of the conflict | Is there a visible, legible shift in the character's understanding and behavior before vs. after this scene? |
| 7 | **Second Pinch Point** | 62.5% (5/8 mark) | Stakes raised concretely (cost, not just new clues) | Does it raise the stakes with a concrete cost (e.g., a character's death), rather than just repeating pressure? |
| 8 | **Third Plot Point** | 70–75% | Low point; climax of the character's *inner* arc — faces the Lie/Truth (see `fiction-workshop/references/character-work.md`) | Does the protagonist face their hardest truth here, after a false victory at the end of Act 2? |
| 9 | **Third Act Turning Point** | 88% | Forces final direct confrontation | Does this launch the climax proper, with no more room for delay or avoidance? |
| 10 | **Climactic Moment** | 90–98% | Protagonist's (or antagonist's) goal is realized or denied — the true story end | When is the protagonist's/antagonist's goal *actually* realized, such that no more obstacles remain? (Weiland's own test — see Faux Climax below.) |
| 11 | **Resolution** | Final 1–2% | "Exhale to the Climax's inhale" | Does this scene address the thematic question raised at the Hook, without introducing new conflict? |

## Failure Mode: Inciting Event / Key Event / First Plot Point Confusion

These three are commonly conflated into a single beat, but they can be distinct scenes with distinct jobs:

- **Inciting Event** (~12%): conflict first *touches* the Normal World. The protagonist may not yet be pulled in.
- **Key Event** (end of Act 1): the protagonist *leaves* the Normal World — a doorway metaphor, where the Inciting Event and Key Event are "two sides of the same coin," usually near-simultaneous but sometimes separable (e.g., in stories where a character delays acting on the inciting conflict for a stretch of Act 1).
- **First Plot Point** (25%): the point of no return into the "adventure world" — often fused with the Key Event, but conceptually distinct (leaving the old world vs. committing to the new one).

**Diagnostic:** for each of the three, can you name the specific scene, and is each doing a different job? If all three collapse into one scene with no distinction, Act 1 is likely rushing the setup.

## Failure Mode: The Faux Climax

A scene that *reads* as climactic — the protagonist appears to achieve their goal — but isn't the true climax because a bigger obstacle remains standing. Multiple climax-shaped scenes may exist in a manuscript, but only one is the true Climactic Moment.

**Diagnostic (Weiland's own test):** "When is the protagonist's (or antagonist's) goal actually realized?" No more obstacles = no more conflict = the story is over. If a scene resolves *a* goal but a larger conflict or obstacle remains, it's a Faux Climax, not the Climactic Moment — check whether it's actually resolving a subplot rather than the main throughline.
```

- [ ] **Step 2: Verify structure**

```bash
grep -c "^| [0-9]* |" skills/story-structure/references/landmark-beats.md
```
Expected: `11` (all eleven beats present as table rows).

```bash
grep -E "^## (The 11 Beats|Failure Mode: Inciting Event / Key Event / First Plot Point Confusion|Failure Mode: The Faux Climax)$" skills/story-structure/references/landmark-beats.md | wc -l
```
Expected: `3`.

```bash
grep -in "TBD\|TODO\|fill in" skills/story-structure/references/landmark-beats.md
```
Expected: no output (empty).

- [ ] **Step 3: Commit**

```bash
git add skills/story-structure/references/landmark-beats.md
git commit -m "feat: add landmark-beats reference to story-structure skill"
```

---

### Task 3: Write `references/signposts.md`

**Files:**
- Create: `skills/story-structure/references/signposts.md`

**Interfaces:**
- Consumes: The 11 beat names from Task 2 — the 6 overlaying signposts must reference them by exact name.
- Produces: The 14 signpost names that `references/structure-map.md` and `references/structure-audit.md` reference.

- [ ] **Step 1: Write `skills/story-structure/references/signposts.md`**

```markdown
# Signposts Reference

James Scott Bell's 14 named "signposts" from *Super Structure* — a content/psychology layer overlaid on the landmark beat skeleton (`landmark-beats.md`). Bell's framing: these answer *what psychological or emotional work* a beat must do, not just where it falls. Six overlay a landmark beat directly; the other eight fall at looser, relative placement between landmarks.

## Signposts That Overlay a Landmark Beat

| Signpost | Overlays | Function | Diagnostic |
|---|---|---|---|
| **Disturbance** | Hook / Inciting Event | Opening trouble — ideally the first page or line | Is there a disturbance from line one, rather than an opening in "Happy People in Happy Land" with no conflict? |
| **Doorway of No Return #1** | First Plot Point | Forces the Lead into Act 2; should land before the 1/5 mark | Have you created a scene strong enough that the Lead could resist, but doesn't? Does it land before the 1/5 mark? |
| **Mirror Moment** | Midpoint | The dead-center gut-check: "Who am I? What have I become?" (must become a different/better person) or "I'm probably going to die" (must become stronger) | Does the protagonist confront one of these two questions here, not just experience a plot twist? |
| **Doorway of No Return #2** | Third Plot Point | A crisis/setback or discovery that makes the Final Battle inevitable; roughly the last quarter of the book remaining | Is there no way back from here — is the Final Battle now unavoidable? |
| **Final Battle** | Climactic Moment | External, internal, or both; resolves the "death stakes" (physical, professional, or psychological) | Does this scene resolve the actual death stakes established in Act 1, not a lesser or subplot conflict? |
| **Transformation** | Climax / Resolution | Proof the Lead has changed (or tragically refused to) | Is there a concrete, visible sign — action, not just statement — that the Lead is different than at the Hook? |

## Signposts at Relative Placement

These eight fall between landmarks. Bell gives relative, not percentage, guidance for each.

| Signpost | Placement | Function | Diagnostic |
|---|---|---|---|
| **Care Package** | Act 1, before Doorway #1 | A pre-existing relationship showing the Lead's capacity to care | Does the reader see the Lead care about someone *before* the plot forces heroics — humanizing them ahead of the action? |
| **Argument Against Transformation** | Act 1, early | The Lead states or embodies the belief they'll have to abandon by the end | Can you name the specific line or belief that Transformation (at the end) will overturn? |
| **Trouble Brewing** | Mid-Act 1 | A portent of the larger conflict to come | Does something in Act 1 foreshadow the true scale of the conflict, beyond the Inciting Event itself? |
| **Kick in the Shins** | Just after Doorway #1 | The first real obstacle in Act 2, confirming the new stakes | Does Act 2 open with a genuine setback, rather than the Lead coasting on the momentum of Doorway #1? |
| **Pet the Dog** | Near the Mirror Moment | The Lead pauses to help someone weaker, ideally at some risk to themselves | Is there a moment of selflessness near the midpoint that isn't strictly required by the plot? |
| **Mounting Forces** | Act 3, before Lights Out | The antagonist/opposition visibly gathers strength | Is the opposition's power escalating visibly, not just being asserted in dialogue? |
| **Lights Out** | Act 3, before Final Battle | The darkest moment — all seems lost | Is there a genuine low point where success looks impossible, immediately before the Final Battle? |
| **Q Factor** | Planted Act 1, paid off Act 3 | An object, memory, or mentor's voice planted early that returns to supply courage or means for the Final Battle | Can you trace a specific Act 1 plant (object, line, relationship) that pays off directly in the Final Battle? |

## Using This Alongside the Landmark Skeleton

Run both checks at each of the six overlay points: does the beat land at roughly the right *percentage* (landmark-beats.md), and is it doing the right *psychological work* (this file)? A beat can be perfectly timed and still be hollow, or emotionally strong but badly misplaced — both checks matter.
```

- [ ] **Step 2: Verify structure**

```bash
grep -cE "^\| \*\*(Disturbance|Doorway of No Return #1|Mirror Moment|Doorway of No Return #2|Final Battle|Transformation|Care Package|Argument Against Transformation|Trouble Brewing|Kick in the Shins|Pet the Dog|Mounting Forces|Lights Out|Q Factor)\*\* \|" skills/story-structure/references/signposts.md
```
Expected: `14` (all fourteen signposts present as table rows).

```bash
grep -in "TBD\|TODO\|fill in" skills/story-structure/references/signposts.md
```
Expected: no output (empty).

- [ ] **Step 3: Commit**

```bash
git add skills/story-structure/references/signposts.md
git commit -m "feat: add signposts reference to story-structure skill"
```

---

### Task 4: Write `references/structure-map.md`

**Files:**
- Create: `skills/story-structure/references/structure-map.md`

**Interfaces:**
- Consumes: The 11 beat names (Task 2) and 14 signpost names (Task 3) — this workflow walks through them in order.
- Produces: The Map mode workflow that `SKILL.md` (Task 1) references and `assets/structure-profile-template.md` (Task 6) is filled out by.

- [ ] **Step 1: Write `skills/story-structure/references/structure-map.md`**

```markdown
# Structure Map Mode

For a story not yet drafted, or only partially drafted. Places the landmark beats and relevant signposts into a plan before the author writes toward them.

## Workflow

1. **Confirm scope.** Ask what's already decided (premise, protagonist, antagonist, ending) versus still open. Map mode works best once the core premise and protagonist's goal are known — if they aren't, suggest `fiction-workshop`'s Story Bible Building stage first.
2. **Walk the 11 landmark beats in order** (see `landmark-beats.md`). For each: ask what the author envisions for that beat, or propose an option if they're stuck. Note the intended chapter/scene and its approximate percentage-through-manuscript.
3. **At each of the 6 overlay points** (see `signposts.md`), also check the matching signpost: does the plan give that beat the psychological content Bell's diagnostic asks for? If not, flag it as a gap — don't invent content on the author's behalf without asking.
4. **Offer the 8 relative-placement signposts** as optional enrichment once the core 11 beats are mapped: Care Package, Argument Against Transformation, Trouble Brewing, Kick in the Shins, Pet the Dog, Mounting Forces, Lights Out, Q Factor. These are not required — ask which, if any, the author wants to plan for.
5. **Flag gaps explicitly.** If a beat has no clear plan yet, say so rather than filling it in with a generic placeholder. The author decides.
6. **Compile the Structure Map.** Once all 11 beats have at least a placeholder decision (even "undecided — will discover in draft" is a valid answer), fill out `assets/structure-profile-template.md` and hand it back.

## Stop Condition

Stop once the Structure Map block is complete for all 11 landmarks (or explicitly marked "undecided" per beat). Hand it back for the author to paste into their Story Bible. Do not write to the Story Bible directly, and do not proceed to drafting scenes — that's `fiction-workshop`'s job.

## Common Pitfalls in Map Mode

| Pitfall | Fix |
|---|---|
| Forcing an answer for every beat immediately | "Undecided — will discover in draft" is valid; don't manufacture false certainty |
| Skipping the signpost content-check because placement is decided | Placement and psychological content are different questions — check both |
| Planning all 8 relative-placement signposts by default | These are optional enrichment; ask which the author actually wants, don't assume all 8 |
| Treating percentages as exact chapter/page numbers | They're guidance for rough quarters, not a rigid outline — note them as approximate |
```

- [ ] **Step 2: Verify structure**

```bash
grep -E "^## (Workflow|Stop Condition|Common Pitfalls in Map Mode)$" skills/story-structure/references/structure-map.md | wc -l
```
Expected: `3`.

```bash
grep -in "TBD\|TODO\|fill in" skills/story-structure/references/structure-map.md
```
Expected: no output (empty).

- [ ] **Step 3: Commit**

```bash
git add skills/story-structure/references/structure-map.md
git commit -m "feat: add structure-map mode to story-structure skill"
```

---

### Task 5: Write `references/structure-audit.md`

**Files:**
- Create: `skills/story-structure/references/structure-audit.md`

**Interfaces:**
- Consumes: The 11 beat names (Task 2), 14 signpost names (Task 3), and the two failure-mode diagnostics (Task 2).
- Produces: The Audit mode workflow that `SKILL.md` (Task 1) references and `assets/structure-profile-template.md` (Task 6) is filled out by.

- [ ] **Step 1: Write `skills/story-structure/references/structure-audit.md`**

```markdown
# Structure Audit Mode

For an existing manuscript, or a manuscript-in-progress with enough chapters written to locate beats in. Diagnoses where beats actually land against where they should, and whether each is doing its job.

## Workflow

1. **Establish total length.** Get total word count or chapter count so percentages can be computed. If the manuscript is incomplete, ask whether to audit what exists so far (percentages will be rougher) or wait until a fuller draft exists.
2. **Locate each of the 11 landmark beats** (see `landmark-beats.md`) in the actual text — ask the author to point to the scene, or read the manuscript if provided, and compute its approximate percentage-through.
3. **Compare actual vs. expected placement.** Flag any beat that has drifted more than ~10 percentage points from its expected mark (e.g., a Midpoint landing at 38% or 63% instead of ~50%) as **mistimed**.
4. **Flag missing beats.** If a beat cannot be located at all, flag it as **missing** — don't force-fit an unrelated scene onto it.
5. **Check content at the 6 overlay points** (see `signposts.md`): for each landmark that overlays a signpost, does the located scene actually do that signpost's psychological work? A beat that's present and correctly timed but doesn't do the work is **thin** — flag it with the specific diagnostic question it fails.
6. **Run the Faux Climax check explicitly.** If more than one scene in the back third of the manuscript reads as climactic, apply Weiland's test to each candidate ("when is the protagonist's/antagonist's goal *actually* realized, with no obstacles remaining?") and identify which is the true Climactic Moment versus a Faux Climax resolving a subplot.
7. **Run the Inciting Event / Key Event / First Plot Point check.** Confirm these are traceable to distinct scenes doing distinct jobs, or flag the conflation if they've collapsed into one beat with no differentiation.
8. **Compile the flagged-beat report**: one line per landmark beat — status (on-time / mistimed / missing / thin), and for mistimed/thin beats, the specific gap. Include the Faux Climax and Inciting/Key/FPP findings as their own report lines.

## Stop Condition

Stop once the flagged-beat report is delivered. Hand it back to the author. Do not rewrite manuscript prose, do not add or remove scenes, and do not silently decide which flags matter most — that's the author's call.

## Common Pitfalls in Audit Mode

| Pitfall | Fix |
|---|---|
| Flagging every beat within 5 points of its mark as mistimed | Use the ~10-point drift threshold — small variance is normal, not a defect |
| Skipping the signpost content-check on beats that are correctly timed | Timing and content are separate checks — a well-placed beat can still be thin |
| Declaring a beat missing because it doesn't match the expected genre convention exactly | Ask whether it's genuinely absent or just handled unconventionally before flagging |
| Auto-rewriting a flagged scene | Audit reports; it does not fix. Hand the report back and let the author decide |
```

- [ ] **Step 2: Verify structure**

```bash
grep -E "^## (Workflow|Stop Condition|Common Pitfalls in Audit Mode)$" skills/story-structure/references/structure-audit.md | wc -l
```
Expected: `3`.

```bash
grep -in "TBD\|TODO\|fill in" skills/story-structure/references/structure-audit.md
```
Expected: no output (empty).

- [ ] **Step 3: Commit**

```bash
git add skills/story-structure/references/structure-audit.md
git commit -m "feat: add structure-audit mode to story-structure skill"
```

---

### Task 6: Write `assets/structure-profile-template.md`

**Files:**
- Create: `skills/story-structure/assets/structure-profile-template.md`

**Interfaces:**
- Consumes: The 11 beat names (Task 2) — the template's fields must use them exactly.
- Produces: Nothing consumed downstream in this repo; this is the artifact handed to the author.

- [ ] **Step 1: Write `skills/story-structure/assets/structure-profile-template.md`**

```markdown
# Structure Profile Template

A block designed to paste directly into an existing Story Bible's "Plot Foundation → Three-Act Structure" section (see `fiction-workshop/assets/story-bible-template.md`), immediately after the existing Act I/Midpoint/Act II-B/Act III placeholders. Not a replacement for that section — this adds finer landmark-beat percentages and signpost notes on top.

```
Structure profile:
- Hook: [scene/chapter]
- Inciting Event (~12%): [scene/chapter]
- Key Event (end of Act 1): [scene/chapter]
- First Plot Point (25%): [scene/chapter] — Doorway of No Return #1 content check: [note]
- First Pinch Point (37.5%): [scene/chapter]
- Midpoint / Moment of Truth (50%): [scene/chapter] — Mirror Moment content check: [note]
- Second Pinch Point (62.5%): [scene/chapter]
- Third Plot Point (70-75%): [scene/chapter] — Doorway of No Return #2 content check: [note]
- Third Act Turning Point (88%): [scene/chapter]
- Climactic Moment (90-98%): [scene/chapter] — Final Battle / Transformation content check: [note]
- Resolution: [scene/chapter]
- Optional signposts planned: [Care Package / Argument Against Transformation / Trouble Brewing / Kick in the Shins / Pet the Dog / Mounting Forces / Lights Out / Q Factor — list which, or "none"]
- Last structure check: [Map / Audit — date]
```

## Usage Notes

- Fill in immediately after a Map session, or after an Audit session confirms a beat's actual location.
- The three "content check" fields correspond to the six landmarks that overlay a Bell signpost (see `references/signposts.md`) — leave the other landmarks' content checks out, since they don't have a corresponding signpost.
- Update "Last structure check" whenever Map or Audit runs against this story, so a later session knows whether a re-check is due.
```

- [ ] **Step 2: Verify structure**

```bash
grep -c "^- " skills/story-structure/assets/structure-profile-template.md
```
Expected: at least `13` (11 beats + optional-signposts line + last-check line, inside the fenced block).

```bash
grep -in "TBD\|TODO" skills/story-structure/assets/structure-profile-template.md
```
Expected: no output (the bracketed fields use `[...]` placeholders by design, matching `archetype-profile-template.md`'s pattern, not "TBD"/"TODO").

- [ ] **Step 3: Commit**

```bash
git add skills/story-structure/assets/structure-profile-template.md
git commit -m "feat: add structure-profile-template asset to story-structure skill"
```

---

### Task 7: Wire into `fiction-workshop`

**Files:**
- Modify: `skills/fiction-workshop/references/developmental-editing.md` (insert cross-link after the "### Act-Level" section, before "## Pacing Diagnostics")
- Modify: `skills/fiction-workshop/references/character-work.md` (insert cross-link after the "### Arc Milestones" section, before "## Common Character Issues")
- Modify: `skills/fiction-workshop/SKILL.md:267` (the `developmental-editing.md` line in the "Files" list)

**Interfaces:**
- Consumes: The `story-structure` skill name from Task 1.
- Produces: Nothing new — this closes the integration loop described in `SKILL.md`'s "Integration with fiction-workshop" section (Task 1).

- [ ] **Step 1: Insert the cross-link into `developmental-editing.md`**

In `skills/fiction-workshop/references/developmental-editing.md`, find this exact text:

```markdown
**Act III (75-100%)**
- Dark night of the soul
- Final confrontation
- Resolution that addresses the thematic question

## Pacing Diagnostics
```

Replace it with:

```markdown
**Act III (75-100%)**
- Dark night of the soul
- Final confrontation
- Resolution that addresses the thematic question

### Deeper Structure Work

This is a lightweight quarter-based read. For landmark-beat percentages (Inciting Event, Pinch Points, Third Plot Point, and the rest), Bell's signpost catalog (Mirror Moment, Q Factor, and the rest), and dedicated Map/Audit modes, see the `story-structure` skill.

## Pacing Diagnostics
```

- [ ] **Step 2: Insert the cross-link into `character-work.md`**

In `skills/fiction-workshop/references/character-work.md`, find this exact text:

```markdown
### Arc Milestones

Typical positive arc progression:
- **Act I**: Character demonstrates the lie in action
- **Midpoint**: Character glimpses the truth
- **Low point**: Character must choose between lie and truth
- **Climax**: Character acts from truth (or chooses lie = tragedy)
- **Resolution**: New normal reflecting growth

## Common Character Issues
```

Replace it with:

```markdown
### Arc Milestones

Typical positive arc progression:
- **Act I**: Character demonstrates the lie in action
- **Midpoint**: Character glimpses the truth
- **Low point**: Character must choose between lie and truth
- **Climax**: Character acts from truth (or chooses lie = tragedy)
- **Resolution**: New normal reflecting growth

These milestones map onto specific structural beats — the Low point is the Third Plot Point, the Climax is the Climactic Moment. For the full percentage-anchored placement model and content diagnostics at each beat, see the `story-structure` skill.

## Common Character Issues
```

- [ ] **Step 3: Update the Files list line in `SKILL.md`**

In `skills/fiction-workshop/SKILL.md`, find this exact line:

```markdown
- `references/developmental-editing.md` - Plot, structure, pacing analysis
```

Replace it with:

```markdown
- `references/developmental-editing.md` - Plot, structure, pacing analysis (see also the `story-structure` skill for landmark-beat percentages and signpost diagnostics)
```

- [ ] **Step 4: Verify**

```bash
grep -A2 "### Deeper Structure Work" skills/fiction-workshop/references/developmental-editing.md
```
Expected: the inserted paragraph, starting with "This is a lightweight quarter-based read."

```bash
grep "story-structure" skills/fiction-workshop/references/developmental-editing.md skills/fiction-workshop/references/character-work.md skills/fiction-workshop/SKILL.md
```
Expected: one match in each of the three files.

```bash
grep -c "^## Pacing Diagnostics$" skills/fiction-workshop/references/developmental-editing.md
grep -c "^## Common Character Issues$" skills/fiction-workshop/references/character-work.md
```
Expected: `1` and `1` (confirms the replace didn't duplicate or drop the following section header in either file).

- [ ] **Step 5: Commit**

```bash
git add skills/fiction-workshop/references/developmental-editing.md skills/fiction-workshop/references/character-work.md skills/fiction-workshop/SKILL.md
git commit -m "feat: link story-structure skill from fiction-workshop"
```

---

### Task 8: Update root `README.md`

**Files:**
- Modify: `README.md`

**Interfaces:**
- Consumes: Skill name `story-structure`, its two mode names, and the landmark/signpost framing from Tasks 1-5.
- Produces: Nothing new — documentation only.

- [ ] **Step 1: Add the "Story Structure" subsection**

In `README.md`, find this exact text:

```markdown
Archetype is a starting scaffold, not a finished character — pair with Fiction Workshop's Want/Need/Wound/Lie framework to individualize.

### Narrative Nonfiction
```

Replace it with:

```markdown
Archetype is a starting scaffold, not a finished character — pair with Fiction Workshop's Want/Need/Wound/Lie framework to individualize.

### Story Structure
Percentage-anchored macro plot structure, drawn from K.M. Weiland's landmark-beat model and James Scott Bell's signpost catalog:
- **Landmark Beats** - 11-beat skeleton (Hook, Inciting Event, First Plot Point, Pinch Points, Midpoint, Third Plot Point, Climax, Resolution) with percentages and diagnostics
- **Signposts** - Bell's 14 named checkpoints (Disturbance, Mirror Moment, Doorways of No Return, Q Factor, and more), overlaid on the landmarks or placed relatively between them
- **Map** - Place beats and signposts for a story not yet drafted
- **Audit** - Locate where beats actually land in an existing manuscript and flag missing, mistimed, or thin ones

Weiland's beats answer *where* a turning point falls; Bell's signposts answer *what psychological work* it needs to do.

### Narrative Nonfiction
```

- [ ] **Step 2: Add the invocation line and usage example**

Find this exact text:

```markdown
```bash
/author-toolkit:fiction-workshop
/author-toolkit:character-archetypes
/author-toolkit:narrative-nonfiction
/author-toolkit:prose-mechanics
/author-toolkit:avoid-ai-writing
```
```

Replace it with:

```markdown
```bash
/author-toolkit:fiction-workshop
/author-toolkit:character-archetypes
/author-toolkit:story-structure
/author-toolkit:narrative-nonfiction
/author-toolkit:prose-mechanics
/author-toolkit:avoid-ai-writing
```
```

Find this exact text:

```markdown
# Character archetypes
"What archetype is this character?"
"Audit this scene for archetype cliché"
"Check archetype conformance for chapters 4-8"
"Run an ensemble balance check on the cast"

# Nonfiction
```

Replace it with:

```markdown
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
```

- [ ] **Step 3: Add rows to the Quick Reference table**

Find this exact text:

```markdown
| Cast balance check | `/author-toolkit:character-archetypes` | "Run an ensemble balance check on the cast" |
| Nonfiction writing | `/author-toolkit:narrative-nonfiction` | "Let's build a blueprint for [book]" |
```

Replace it with:

```markdown
| Cast balance check | `/author-toolkit:character-archetypes` | "Run an ensemble balance check on the cast" |
| Plan new story structure | `/author-toolkit:story-structure` | "Map the structure for this story" |
| Audit existing structure | `/author-toolkit:story-structure` | "Audit this manuscript's structure" |
| Nonfiction writing | `/author-toolkit:narrative-nonfiction` | "Let's build a blueprint for [book]" |
```

- [ ] **Step 4: Verify**

```bash
grep -c "^### Story Structure$" README.md
```
Expected: `1`.

```bash
grep -c "story-structure" README.md
```
Expected: exact count depends on final wording — run the command and confirm every match is one of: the invocation-block line, the two Quick Reference rows, or an incidental mention; there is no fixed number to assert blindly, read the actual matches.

```bash
grep -c "^/author-toolkit:" README.md
```
Expected: `6` (all six skills now listed in the invocation block).

- [ ] **Step 5: Commit**

```bash
git add README.md
git commit -m "docs: add story-structure to README"
```

---

### Task 9: Bump plugin metadata

**Files:**
- Modify: `.claude-plugin/plugin.json`
- Modify: `.claude-plugin/marketplace.json`

**Interfaces:**
- Consumes: Nothing from other tasks — purely a version/keyword bump reflecting the new skill's existence.
- Produces: Nothing consumed downstream.

- [ ] **Step 1: Update `.claude-plugin/plugin.json`**

Read the current file, then replace its full contents with:

```json
{
  "name": "author-toolkit",
  "description": "Writing skills for fiction and narrative nonfiction authors, including an AI-writing audit/rewrite skill",
  "version": "1.3.0",
  "author": {
    "name": "rhavekost",
    "email": "rob@kostlabs.com"
  },
  "homepage": "https://github.com/rhavekost/author-toolkit",
  "repository": "https://github.com/rhavekost/author-toolkit",
  "license": "MIT",
  "keywords": ["writing", "fiction", "nonfiction", "editing", "author", "skills", "ai-writing", "avoid-ai-writing", "character-archetypes", "story-structure"]
}
```

- [ ] **Step 2: Update `.claude-plugin/marketplace.json`**

Read the current file, then replace its full contents with:

```json
{
  "name": "author-toolkit",
  "description": "Writing skills for fiction and narrative nonfiction authors, including an AI-writing audit/rewrite skill",
  "owner": {
    "name": "rhavekost",
    "email": "rob@kostlabs.com"
  },
  "plugins": [
    {
      "name": "author-toolkit",
      "description": "Writing skills for fiction and narrative nonfiction authors, including an AI-writing audit/rewrite skill",
      "version": "1.3.0",
      "source": "./",
      "author": {
        "name": "rhavekost",
        "email": "rob@kostlabs.com"
      }
    }
  ]
}
```

- [ ] **Step 3: Verify both files are valid JSON and consistent**

```bash
python3 -m json.tool .claude-plugin/plugin.json > /dev/null && echo "plugin.json: valid JSON"
python3 -m json.tool .claude-plugin/marketplace.json > /dev/null && echo "marketplace.json: valid JSON"
grep '"version": "1.3.0"' .claude-plugin/plugin.json .claude-plugin/marketplace.json
grep "story-structure" .claude-plugin/plugin.json
```
Expected: both files print "valid JSON", the version grep matches in both files, and the keyword grep matches once in `plugin.json`.

- [ ] **Step 4: Commit**

```bash
git add .claude-plugin/plugin.json .claude-plugin/marketplace.json
git commit -m "chore: bump plugin version to 1.3.0 for story-structure skill"
```

---

## Task Order and Dependencies

Tasks 1-6 build the new skill; Task 1 (`SKILL.md`) can be written first since it only references paths, not content, but Tasks 2-6 have no dependencies on each other or on Task 1 and could run in any order. Task 7 depends on Task 1 existing (references the skill by name). Task 8 depends on Task 1 (skill name and mode names). Task 9 has no content dependency but should run last as the "this feature is complete" version bump. Recommended sequential order for a single-session run: 1, 2, 3, 4, 5, 6, 7, 8, 9.
