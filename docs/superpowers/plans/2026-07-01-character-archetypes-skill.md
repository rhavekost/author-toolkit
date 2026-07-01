# Character Archetypes Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a new standalone `character-archetypes` skill (two archetype taxonomies + four analysis modes) to the `author-toolkit` plugin, wire it into `fiction-workshop`, and update the root README and plugin metadata.

**Architecture:** This repo has no code and no test runner — it is a Claude Code plugin made entirely of skill markdown files (`SKILL.md` + `references/*.md` + `assets/*.md`), consumed by an agent at runtime. There is nothing to compile or unit-test. Every task's "test cycle" is therefore a **structural verification pass**: grep-based checks that required sections/entries exist, and a placeholder scan — run in place of a test suite. This mirrors how the three existing skills (`fiction-workshop`, `prose-mechanics`, `narrative-nonfiction`) are structured; this plan follows their established patterns (frontmatter format, `references/`+`assets/` split, Stopping Points / Common Mistakes tables) rather than inventing new ones.

**Tech Stack:** None — Markdown files only, versioned via `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`.

## Global Constraints

- New skill lives at `skills/character-archetypes/` with this exact file tree:
  ```
  skills/character-archetypes/
    SKILL.md
    references/
      narrative-role-archetypes.md
      personality-archetypes.md
      archetype-analyzer.md
      archetype-audit.md
      archetype-conformance.md
      archetype-ensemble.md
    assets/
      archetype-profile-template.md
  ```
- `SKILL.md` frontmatter must match the exact two-field format used by sibling skills (`name`, `description` only — see `skills/fiction-workshop/SKILL.md:1-4`).
- `description` frontmatter field must include these trigger phrases verbatim (from the design spec): "character archetype," "archetype audit," "what archetype is this character," "archetype conformance," "Hero's Journey character role," "Jungian archetype."
- Reference files (everything under `references/`) use a plain `# Title` header, no YAML frontmatter — confirmed pattern from `character-work.md`, `continuity-tracking.md`, `active-passive-audit.md`.
- Narrative-role taxonomy is exactly these 8 (Vogler/Campbell): Hero, Mentor, Threshold Guardian, Herald, Shapeshifter, Shadow, Trickster, Ally.
- Personality taxonomy is exactly these 12 (Jungian / Mark & Pearson): Innocent, Everyman, Hero, Caregiver, Explorer, Rebel, Lover, Creator, Jester, Sage, Magician, Ruler.
- Four analysis modes, one reference file each: Analyzer, Audit, Conformance, Ensemble. Ordering guidance to document: **Analyzer → (optional) Audit → Conformance → Ensemble**; Audit/Conformance can be entered directly if the archetype is already decided; Ensemble is a late-stage, cast-level check.
- Every mode file must state an explicit stop condition, matching the design spec's table:
  - Analyzer stops after naming the pairing/recommendation with rationale — hands back, does not auto-write to the Story Bible.
  - Audit stops after delivering the flagged cliché list — no auto-rewrite.
  - Conformance stops after delivering drift flags for the requested range — author judges real drift vs. legitimate arc.
  - Ensemble stops after delivering the cast balance report — author decides on cast changes, no auto-invented characters.
- Scope is fiction only. Do not modify `narrative-nonfiction` or `prose-mechanics`.
- Integration footprint into `fiction-workshop` is minimal, per the design spec: a short (~5-line) added section in `character-work.md` pointing to the new skill as a complementary lens (not replacing Want/Need/Wound/Lie), and a one-line addition to `SKILL.md`'s Files list. Do not restructure `story-bible-template.md`.
- `README.md` gets a new "Character Archetypes" subsection under "Skills Included" (placed directly after "Fiction Workshop," before "Narrative Nonfiction," since it's a fiction-only companion skill), an invocation line under "Usage," and rows in the "Quick Reference" table — matching the exact formatting of existing entries.
- Plugin version bumps from `1.1.0` to `1.2.0` in both `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` (new feature, no breaking changes → minor bump). Add `"character-archetypes"` to the `keywords` array in both files. Do not change `description` in either file.
- No placeholder text anywhere (no "TBD", "TODO", "fill in", bracketed blanks) in any new or modified file except `assets/archetype-profile-template.md`, whose bracketed fields are its intended fill-in-the-blank design (matching `assets/story-bible-template.md`'s existing pattern).

---

### Task 1: Scaffold the skill and write `SKILL.md`

**Files:**
- Create: `skills/character-archetypes/SKILL.md`

**Interfaces:**
- Produces: The skill's frontmatter `name: character-archetypes`, which every later task's files live under. Produces the "Files" list that Tasks 2–8 must each be reflected in.
- Consumes: Nothing from other tasks (this is the entry point), but must forward-reference the six reference files and one asset file that Tasks 2–8 create (they don't exist yet when this task runs — that's fine, this task only writes the `SKILL.md` text referencing their paths).

- [ ] **Step 1: Create the directory structure**

```bash
mkdir -p skills/character-archetypes/references skills/character-archetypes/assets
```

- [ ] **Step 2: Write `skills/character-archetypes/SKILL.md`**

```markdown
---
name: character-archetypes
description: "Use when identifying, auditing, or tracking character archetypes in fiction. Trigger on: 'character archetype', 'archetype audit', 'what archetype is this character', 'archetype conformance', 'Hero's Journey character role', 'Jungian archetype', or archetype-based character analysis."
---

# Character Archetypes

Diagnostic vocabulary for character archetypes — narrative-role functions (Hero, Mentor, Trickster, and the rest of Vogler/Campbell's eight) and Jungian personality types (Sage, Rebel, Caregiver, and the rest of the Mark & Pearson twelve) — plus four modes for using them across a manuscript: naming a pairing, auditing for cliché, checking for drift, and balancing a cast.

Archetype is a **starting scaffold, not a finished character**. This skill complements `fiction-workshop`'s Want/Need/Wound/Lie framework (see `references/character-work.md` there) rather than replacing it — the archetype names the pattern; the Core Four individualizes it.

## When to Use

This skill is for:
- ✅ Fiction manuscripts — novels, novellas, short stories, screenplays-in-prose-form
- ✅ Naming a character's narrative-role and personality-type pairing
- ✅ Checking whether an established archetype is being used well or as cliché
- ✅ Checking whether a character's actions still match their established archetype, or have drifted without explanation
- ✅ Checking whether a cast's archetypes are balanced (no redundancy, no structural gaps)

## When NOT to Use

This skill is NOT for:
- ❌ Narrative nonfiction (memoir, self-help) — author-voice and reader-persona archetypes are a different, unaddressed problem. Use `narrative-nonfiction` instead.
- ❌ Enneagram or other personality typologies — this skill covers exactly two canonical frameworks (Vogler narrative-role, Jungian twelve). Adding more blurs into general personality-typing rather than archetype work.
- ❌ Plot- or genre-level archetypes (monomyth stages, genre tropes) — this skill is character-scoped only. For plot-level structure, use `fiction-workshop`'s `references/developmental-editing.md`.
- ❌ Building a character from scratch with no story context — Analyzer's "recommend" direction needs at least a stated story role to work from.

## Session Continuity

Archetype pairings are meant to persist in the project's Story Bible, not be re-derived each session.

- **At session start:** If a Story Bible exists, check each main character's entry for an existing Archetype Profile block (see `assets/archetype-profile-template.md`). Don't re-run Analyzer on a character who already has one unless the author asks for a re-check.
- **When a pairing is newly named or changed:** Hand the profile block back to the author to paste into the Story Bible yourself — this skill does not write to the Story Bible directly (see each mode's stop condition below).

## The Two Taxonomies

A character gets tagged with **one archetype from each list** — they describe different things (plot function vs. psychology) and normally combine (e.g., narrative-role Mentor + personality Sage).

| Taxonomy | Reference file | Covers |
|---|---|---|
| **Narrative-Role** | `references/narrative-role-archetypes.md` | Vogler/Campbell's 8 character functions: Hero, Mentor, Threshold Guardian, Herald, Shapeshifter, Shadow, Trickster, Ally |
| **Personality** | `references/personality-archetypes.md` | Jungian 12 (Mark & Pearson model): Innocent, Everyman, Hero, Caregiver, Explorer, Rebel, Lover, Creator, Jester, Sage, Magician, Ruler |

Both files state explicitly that the archetype is a starting scaffold, not a finished character — individualizing detail (voice, wound, specific flaw, from `fiction-workshop`'s Want/Need/Wound/Lie) is what keeps an archetype from reading as a stock type.

## The Four Analysis Modes

| Mode | Invocation | Question | Reference file |
|---|---|---|---|
| **Analyzer** | "What archetype is this character?" | Diagnose or recommend a pairing | `references/archetype-analyzer.md` |
| **Audit** | "Audit this scene for archetype cliché" | Is the archetype used well, or as cliché? | `references/archetype-audit.md` |
| **Conformance** | "Check archetype conformance for chapters X-Y" | Is this character still who we said they were? | `references/archetype-conformance.md` |
| **Ensemble** | "Run an ensemble balance check on the cast" | Is the cast balanced? | `references/archetype-ensemble.md` |

**Ordering guidance:** Analyzer → (optional) Audit → Conformance → Ensemble. Skip straight to Audit or Conformance if the archetype is already decided. Ensemble is a late-stage check — run it once most main characters already have an assigned archetype, not as a starting point.

Load only the reference file matching the currently invoked mode. Do not preload all references at session start — it wastes context budget. If switching modes mid-session, load the new reference file and treat the prior one as out-of-scope.

## Workflow

1. **Identify the mode** the author is invoking (see table above). If unclear, ask.
2. **Load only that mode's reference file** (and the taxonomy file(s) it needs — Analyzer and Audit need both taxonomies; Conformance and Ensemble need whichever taxonomy the character's existing profile already names).
3. **Run the mode's workflow** exactly as documented in its reference file.
4. **Stop at the mode's documented stop condition** (see Stopping Points below). Hand results back to the author.
5. **If a new or changed Archetype Profile results**, offer the `assets/archetype-profile-template.md` block for the author to paste into their Story Bible — do not write it there yourself.

## Integration with `fiction-workshop`

- `fiction-workshop/references/character-work.md` links here as a complementary lens alongside Want/Need/Wound/Lie.
- `assets/archetype-profile-template.md` is designed to paste directly into the Story Bible character entry format shown in `fiction-workshop/SKILL.md`, immediately after "Voice notes:".
- This skill never restructures `fiction-workshop/assets/story-bible-template.md` — it only adds an optional block to individual character entries.

## Stopping Points

Each mode has a defined end. Stop at it. Do not auto-advance to the next mode, do not silently expand scope, do not write to the Story Bible without being asked.

| Mode | Stops when... | Then |
|---|---|---|
| **Analyzer** | Pairing (or recommendation) named with rationale | Hand back for author confirmation. Do not auto-write to Story Bible. |
| **Audit** | Flagged cliché list delivered | Stop. No auto-rewrite — author decides which flags to act on. |
| **Conformance** | Drift flags delivered for the requested range | Stop. Author decides what's real drift vs. legitimate arc progression. |
| **Ensemble** | Cast balance report delivered | Stop. Author decides on any cast changes — do not auto-invent new characters. |

## Common Mistakes

| Mistake | Fix |
|---|---|
| Treating archetype as a rigid mold | Archetype is scaffold, not finished character — individualizing detail is mandatory |
| Confusing narrative-role with personality-type | They're independent axes; a Hero (role) can be a Sage (personality) |
| Running Audit before an archetype is established | Audit needs a target to judge cliché against — run Analyzer first, or use stated author intent |
| Flagging arc growth as Conformance drift | Legitimate arc progression isn't drift — only *unexplained* inconsistency is |
| Running Ensemble before the main cast has archetypes assigned | Ensemble is a late-stage check, not a starting point |

## Quick Reference Commands

| Need | Command |
|---|---|
| Name a pairing | "What archetype is this character?" |
| Get a recommendation for a new character | "What archetype should a [stated role] character be?" |
| Check for cliché | "Audit [character] in [scene] for archetype cliché" |
| Check for drift | "Check archetype conformance for [character] across chapters [X-Y]" |
| Check cast balance | "Run an ensemble balance check on the cast" |

---

## Files

- `references/narrative-role-archetypes.md` - Vogler/Campbell's 8 character functions
- `references/personality-archetypes.md` - Jungian 12 (Mark & Pearson model)
- `references/archetype-analyzer.md` - Diagnose or recommend an archetype pairing
- `references/archetype-audit.md` - Flag stock/cliché archetype use
- `references/archetype-conformance.md` - Check for unexplained archetype drift
- `references/archetype-ensemble.md` - Check cast-level archetype balance
- `assets/archetype-profile-template.md` - Story Bible block for an archetype pairing
```

- [ ] **Step 3: Verify structure**

```bash
grep -c "^---$" skills/character-archetypes/SKILL.md
```
Expected: `2` (opening and closing frontmatter fence).

```bash
grep -E "^## (When to Use|When NOT to Use|Session Continuity|The Two Taxonomies|The Four Analysis Modes|Workflow|Integration with|Stopping Points|Common Mistakes|Quick Reference Commands|Files)$" skills/character-archetypes/SKILL.md | wc -l
```
Expected: `11` (all eleven required sections present).

```bash
grep -in "TBD\|TODO\|fill in" skills/character-archetypes/SKILL.md
```
Expected: no output (empty).

- [ ] **Step 4: Commit**

```bash
git add skills/character-archetypes/SKILL.md
git commit -m "feat: scaffold character-archetypes skill with SKILL.md"
```

---

### Task 2: Write `references/narrative-role-archetypes.md`

**Files:**
- Create: `skills/character-archetypes/references/narrative-role-archetypes.md`

**Interfaces:**
- Consumes: Nothing (self-contained reference content).
- Produces: 8 archetype entries (Hero, Mentor, Threshold Guardian, Herald, Shapeshifter, Shadow, Trickster, Ally), each with Definition / Narrative purpose / Common signals / Subversion patterns / Worked example — this is the exact field set `archetype-analyzer.md` (Task 4) and `archetype-audit.md` (Task 5) instruct the reader to score characters against.

- [ ] **Step 1: Write `skills/character-archetypes/references/narrative-role-archetypes.md`**

```markdown
# Narrative-Role Archetypes Reference

Vogler/Campbell's eight character functions — the role a character plays in driving the plot forward. Pair with a personality archetype from `personality-archetypes.md` to complete a character's archetype profile. Both taxonomies describe different things: this file answers "what does this character *do* in the story?"

Archetype is a starting scaffold, not a finished character. Individualizing detail — voice, wound, specific flaw, from `fiction-workshop`'s Want/Need/Wound/Lie framework — is what keeps a character from reading as a stock type.

## Hero

**Definition:** The character whose journey the story follows; the audience surrogate who must change or grow to resolve the central conflict.

**Narrative purpose:** Drives the plot forward through action and choice; embodies the story's central question via their arc.

**Common signals:** Named early, given a clear want, faces the inciting incident directly, other characters orient around their goal.

**Subversion patterns:** Reluctant Hero (must be pushed into the journey); Anti-Hero (pursues the right goal through morally compromised means); Passive Hero (a deliberate subversion to critique heroism itself — risky, and often reads as a plotting flaw unless the subversion is clearly the point).

**Worked example:** In a heist thriller, the recently disgraced ex-cop who takes the job to clear her name is the Hero — her want (money, redemption) and the plot's central question (can she trust anyone again?) are the same thread.

## Mentor

**Definition:** Provides wisdom, training, or a gift that enables the Hero to proceed; often a guide who cannot complete the journey themselves.

**Narrative purpose:** Transfers capability or insight the Hero lacks; frequently exits the story near the end of Act I (death, departure, betrayal), forcing the Hero to act alone.

**Common signals:** Appears early, has already completed a version of the Hero's journey, gives a tool, skill, or piece of knowledge, often carries their own unresolved wound tied to what they're teaching.

**Subversion patterns:** False Mentor (guidance is self-serving or a trap); Fallible Mentor (an ordinary human, not infallible — makes the Hero's eventual self-reliance mean more); Reluctant Mentor (resists the role, must be talked into it).

**Worked example:** The retired handler who trains the new asset one last time, then is killed by the very agency the Hero must now expose alone — the mentor's death removes the safety net.

## Threshold Guardian

**Definition:** Tests the Hero's resolve at a boundary between the ordinary world and the story's true stakes; not necessarily an antagonist.

**Narrative purpose:** Filters unprepared heroes, forcing a demonstration of commitment before the plot allows deeper access to the conflict.

**Common signals:** Positioned at a literal or figurative gate (a bureaucrat, a bouncer, a locked door, a skeptical ally); poses an obstacle proportional to the Hero's current readiness.

**Subversion patterns:** The Guardian who becomes an Ally once bested (a loyalty test disguised as an obstacle); the Guardian who is right to refuse (the Hero genuinely isn't ready, and ignoring the warning costs them).

**Worked example:** A hostile desk sergeant who won't release case files until the detective proves she has standing — passing the test earns access to the real investigation.

## Herald

**Definition:** Announces the need for change; delivers the inciting incident or the call to adventure.

**Narrative purpose:** The structural trigger that converts the ordinary world into a story by introducing the disruption the Hero must respond to.

**Common signals:** Appears briefly, often early and only once, carries information, an event, or a threat the Hero cannot ignore.

**Subversion patterns:** The Herald who is also the Shadow (the call to adventure is itself the trap); the impersonal Herald (a natural disaster, a diagnosis — no character at all, just an event).

**Worked example:** The anonymous tip that lands on a journalist's desk naming her own mentor as the source of a leak — the Herald function here is a single message, not a recurring character.

## Shapeshifter

**Definition:** A character whose loyalty, motive, or nature is genuinely ambiguous to the Hero (and often the reader) for a sustained stretch of the story.

**Narrative purpose:** Generates doubt and tension around trust; the audience's uncertainty about them should mirror the Hero's.

**Common signals:** Sends contradictory signals about intent, often a romantic or professional ally whose true allegiance is a mid-story reveal.

**Subversion patterns:** The Shapeshifter who never fully resolves (stays ambiguous through the ending, by design); the false Shapeshifter (a red herring — seems ambiguous but was loyal all along, used to misdirect suspicion from the real Shadow).

**Worked example:** The double agent whose reports keep helping the protagonist right up until they don't — neither the Hero nor the reader can be sure which side she's really on until the climax.

## Shadow

**Definition:** Embodies the force the Hero must overcome; not always a literal villain, but the story's antagonistic pressure given a face.

**Narrative purpose:** Externalizes the Hero's central obstacle (and often their Lie) so it can be dramatized and confronted directly.

**Common signals:** Directly opposes the Hero's want; frequently a dark mirror of the Hero (shares a wound, a skill, or a belief system, inverted).

**Subversion patterns:** The Shadow who is sympathetic, or right about something real, even though their method is wrong; the Shadow who isn't a person at all (an institution, an addiction, a system).

**Worked example:** The mentor-turned-cartel-boss who once taught the protagonist everything he knows about disappearing — the Shadow's competence is the Hero's own, aimed the other direction.

## Trickster

**Definition:** Disrupts the status quo through humor, chaos, or rule-breaking; provides comic relief but often reveals truths others won't say.

**Narrative purpose:** Releases tension, punctures pretension, and can voice the story's harshest honesty precisely because no one takes them fully seriously.

**Common signals:** Breaks tone or register when they enter a scene, undermines authority (including the Hero's), gets away with saying things that would cost another character dearly.

**Subversion patterns:** The Trickster whose chaos has real consequences (comic relief that gets someone killed — a tonal risk, but effective for a genre shift); the Trickster who is secretly the wisest character in the room (Jester-as-Sage).

**Worked example:** The wisecracking hacker who mocks the mission's gravity right up until the one line that reframes the whole team's blind spot — comedy used as the vehicle for the story's sharpest insight.

## Ally

**Definition:** Supports the Hero's journey without occupying one of the more specialized functional roles above; provides companionship, skill, or backup.

**Narrative purpose:** Humanizes the Hero (someone to talk to, someone who can be lost as a stake), and can carry subplot weight independent of the main arc.

**Common signals:** Consistent loyalty even under strain, a skill set that complements rather than duplicates the Hero's, a smaller want of their own that intersects the main plot.

**Subversion patterns:** The Ally whose loyalty has a limit and reaches it (believable and foreshadowed, not a cheap betrayal); the Ally who quietly does more narrative work than the Hero (common in ensemble pieces).

**Worked example:** The getaway driver who says almost nothing for two acts, then makes the one choice that saves the crew at personal cost — an Ally whose narrative weight arrives all at once.
```

- [ ] **Step 2: Verify structure**

```bash
grep -c "^## " skills/character-archetypes/references/narrative-role-archetypes.md
```
Expected: `8`.

```bash
for role in Hero Mentor "Threshold Guardian" Herald Shapeshifter Shadow Trickster Ally; do grep -q "^## $role$" skills/character-archetypes/references/narrative-role-archetypes.md || echo "MISSING: $role"; done
```
Expected: no output (all 8 present, exact names).

```bash
grep -c "\*\*Worked example:\*\*" skills/character-archetypes/references/narrative-role-archetypes.md
```
Expected: `8` (every entry has one).

- [ ] **Step 3: Commit**

```bash
git add skills/character-archetypes/references/narrative-role-archetypes.md
git commit -m "feat: add narrative-role archetypes reference"
```

---

### Task 3: Write `references/personality-archetypes.md`

**Files:**
- Create: `skills/character-archetypes/references/personality-archetypes.md`

**Interfaces:**
- Consumes: Nothing (self-contained reference content).
- Produces: 12 archetype entries (Innocent, Everyman, Hero, Caregiver, Explorer, Rebel, Lover, Creator, Jester, Sage, Magician, Ruler), each with Core desire / Greatest fear / Strategy / Weakness-trap / Voice-dialogue tendencies / Worked example — the field set `archetype-analyzer.md` and `archetype-audit.md` score characters against.

- [ ] **Step 1: Write `skills/character-archetypes/references/personality-archetypes.md`**

```markdown
# Personality Archetypes Reference

The Jungian twelve (Mark & Pearson model) — a character's core psychology, independent of their plot function. Pair with a narrative-role archetype from `narrative-role-archetypes.md` to complete a character's archetype profile. This file answers "who is this character, underneath what they do in the plot?"

Archetype is a starting scaffold, not a finished character. Individualizing detail — voice, wound, specific flaw, from `fiction-workshop`'s Want/Need/Wound/Lie framework — is what keeps a character from reading as a stock type.

## Innocent

**Core desire:** To be safe and happy; to do things right and be rewarded for it.

**Greatest fear:** Being punished for doing something wrong, or cast out for a mistake they didn't see coming.

**Strategy:** Stay optimistic, trust that things will work out, follow the rules as understood.

**Weakness/trap:** Naivety that curdles into denial — refuses to see danger or corruption even when it's obvious to everyone else.

**Voice/dialogue tendencies:** Simple, hopeful phrasing; asks earnest questions others would consider naive; avoids cynicism even when mimicking it would fit in.

**Worked example:** The new recruit who reports the corruption she's witnessed to her superiors, certain the system will fix itself — her arc's engine is what happens when it doesn't.

## Everyman

**Core desire:** To belong — connection, community, being one of the group rather than set apart.

**Greatest fear:** Standing out, being excluded, or being revealed as lesser than their peers.

**Strategy:** Develop ordinary virtues, blend in, find common ground with anyone.

**Weakness/trap:** Loses individual identity chasing consensus; won't take the stand that would isolate them from the group, even when it's the right stand.

**Voice/dialogue tendencies:** Plain, relatable diction; defers to group opinion; downplays personal exceptionalism even when it's real.

**Worked example:** The office worker who becomes the story's moral center precisely because he's the one person in the building nobody suspects of anything.

## Hero

**Core desire:** To prove worth through courageous, difficult action.

**Greatest fear:** Weakness, vulnerability, being seen as ineffectual or cowardly.

**Strategy:** Become as strong and competent as possible; meet every challenge head-on.

**Weakness/trap:** Arrogance — mistakes the willingness to fight for the wisdom to know when not to; can turn ally relationships into competitions.

**Voice/dialogue tendencies:** Direct, action-oriented statements; short on self-doubt in dialogue even when it's present internally; challenges others to rise to the occasion.

**Worked example:** The soldier who volunteers for every dangerous assignment, not from recklessness but because turning one down would mean admitting fear out loud.

## Caregiver

**Core desire:** To protect and help others, often at cost to self.

**Greatest fear:** Selfishness, or that their help wasn't enough and someone was harmed by their absence.

**Strategy:** Anticipate others' needs before being asked; do for others what they won't do for themselves.

**Weakness/trap:** Martyrdom and enabling — the giving becomes compulsive, and the people they protect never develop their own capability.

**Voice/dialogue tendencies:** Solicitous phrasing ("Have you eaten?", "Let me handle that"); redirects conversations toward others' welfare; minimizes their own needs even when asked directly.

**Worked example:** The team medic who quietly gives up her own escape seat, framing it as logistics rather than sacrifice, so no one has to feel the weight of what she chose.

## Explorer

**Core desire:** Freedom to find out who they are through discovering the world.

**Greatest fear:** Getting trapped, conforming, feeling stuck in a life that isn't theirs.

**Strategy:** Keep moving; seek out new, more authentic experiences; avoid commitments that box them in.

**Weakness/trap:** Aimless wandering as avoidance — the search for authenticity becomes a permanent excuse never to land anywhere or commit to anyone.

**Voice/dialogue tendencies:** Restless phrasing, questions authority and convention by default, resists being pinned down even in casual conversation ("we'll see," "depends").

**Worked example:** The smuggler pilot who takes every job that keeps her off one planet too long, not for the money, but because staying anywhere reads as surrender.

## Rebel

**Core desire:** Revolution — to overturn what isn't working, especially systems that feel unjust or obsolete.

**Greatest fear:** Being powerless, ineffectual, or indistinguishable from the establishment they're fighting.

**Strategy:** Disrupt, shock, break the rule everyone else is too afraid to break.

**Weakness/trap:** Crosses from disruption into destruction for its own sake; can't tell the difference between a system that needs burning down and one that just needs reform.

**Voice/dialogue tendencies:** Confrontational, unfiltered speech; rejects euphemism and diplomatic hedging; needles authority figures by name.

**Worked example:** The whistleblower who leaks the files to the press instead of the inspector general, because working within the system reads to her as complicity.

## Lover

**Core desire:** Intimacy and connection with the people, work, or experiences they're passionate about.

**Greatest fear:** Being alone, unloved, or undesired.

**Strategy:** Become ever more attractive and devoted; prioritize relationships and passion above nearly everything.

**Weakness/trap:** Loses independent identity in pursuit of a relationship; may stay in something destructive rather than face being unloved.

**Voice/dialogue tendencies:** Sensory, emotionally expressive language; frequently references how choices affect the relationship in question; struggles to speak in purely transactional terms even in professional settings.

**Worked example:** The diplomat who keeps negotiating with a hostile counterpart long after her government has ordered her to walk away, because she still believes the relationship, not the treaty, is what will actually hold.

## Creator

**Core desire:** To make something of enduring value; give form to a vision.

**Greatest fear:** Mediocrity — producing something inauthentic or unoriginal.

**Strategy:** Develop artistic control and skill; keep iterating until the vision matches the execution.

**Weakness/trap:** Perfectionism that never ships; values the vision so highly that any compromise feels like failure, even the compromises survival requires.

**Voice/dialogue tendencies:** Precise, often technical language about their craft; frustrated when others don't see the flaw they see; describes problems in terms of what's "wrong" with the design.

**Worked example:** The engineer who keeps redesigning the escape pod even as the ship is dying around her, because a flawed solution that ships doesn't feel like a solution at all.

## Jester

**Core desire:** To live in the moment, with full enjoyment; to lighten the world.

**Greatest fear:** Being boring, or bored — irrelevance through solemnity.

**Strategy:** Play, joke, find the absurd angle on anything, including danger.

**Weakness/trap:** Frivolity that curdles into irresponsibility — uses humor to dodge every moment that actually calls for gravity.

**Voice/dialogue tendencies:** Quips, wordplay, deflects sincere questions with a joke, comfortable being the only person laughing.

**Worked example:** The comic-relief navigator who jokes through the ship's final approach — until the one scene where he doesn't, and the silence lands harder than any speech would have.

## Sage

**Core desire:** To understand the world through intelligence and analysis.

**Greatest fear:** Being duped, misled, or exposed as ignorant.

**Strategy:** Seek out information and truth; think before acting; trust expertise over instinct.

**Weakness/trap:** Analysis paralysis — can study a problem so long that the window to act on it closes; can also become insufferably didactic.

**Voice/dialogue tendencies:** Measured, precise diction; answers questions with more context than asked for; distrusts claims without evidence, and says so.

**Worked example:** The academic who has the correct theory about the artifact's danger three chapters before anyone will listen to her — her arc's tension is watching her try to be believed in time.

## Magician

**Core desire:** Understanding the fundamental laws of how the world (or a system) works, in order to transform it.

**Greatest fear:** Unintended, negative consequences from their own intervention.

**Strategy:** Develop a vision and align it with underlying principles; work through leverage points rather than brute force.

**Weakness/trap:** Becomes manipulative — the confidence that they understand the system well enough to change it tips into using people as levers rather than partners.

**Voice/dialogue tendencies:** Speaks in systems and cause-effect ("if we change this, that follows"); comfortable with ambiguity others find unsettling; rarely explains the full plan before acting.

**Worked example:** The strategist who engineers a rival faction's collapse through three unrelated-seeming moves made months apart — by the time anyone sees the pattern, it's already done.

## Ruler

**Core desire:** Control — creating a prosperous, stable, successful environment (a family, a company, a kingdom).

**Greatest fear:** Chaos, being overthrown, loss of control.

**Strategy:** Exercise authority; take responsibility; enforce the order they believe the group needs.

**Weakness/trap:** Authoritarian rigidity — mistakes control for competence, and punishes dissent even when the dissent is correct.

**Voice/dialogue tendencies:** Declarative, decision-final phrasing; delegates by instruction rather than discussion; reframes disagreement as a discipline problem.

**Worked example:** The CEO who fires the analyst for being right about the coming collapse in front of the board, because being contradicted publicly is a threat to order she can't tolerate — regardless of the analyst's accuracy.
```

- [ ] **Step 2: Verify structure**

```bash
grep -c "^## " skills/character-archetypes/references/personality-archetypes.md
```
Expected: `12`.

```bash
for type in Innocent Everyman Hero Caregiver Explorer Rebel Lover Creator Jester Sage Magician Ruler; do grep -q "^## $type$" skills/character-archetypes/references/personality-archetypes.md || echo "MISSING: $type"; done
```
Expected: no output.

```bash
grep -c "\*\*Worked example:\*\*" skills/character-archetypes/references/personality-archetypes.md
```
Expected: `12`.

- [ ] **Step 3: Commit**

```bash
git add skills/character-archetypes/references/personality-archetypes.md
git commit -m "feat: add personality archetypes reference"
```

---

### Task 4: Write `references/archetype-analyzer.md`

**Files:**
- Create: `skills/character-archetypes/references/archetype-analyzer.md`

**Interfaces:**
- Consumes: Entry names from `narrative-role-archetypes.md` (Task 2) and `personality-archetypes.md` (Task 3) — reference them by file path, do not duplicate their content.
- Produces: The Analyzer workflow, referenced by `SKILL.md`'s mode table (Task 1) and `archetype-audit.md` (Task 5), which requires an archetype to already be established before it can run.

- [ ] **Step 1: Write `skills/character-archetypes/references/archetype-analyzer.md`**

```markdown
# Archetype Analyzer Reference

When invoked to identify, diagnose, or recommend a character's archetype pairing. Bidirectional: **Diagnose** an existing character, or **Recommend** a starting pairing for one not yet built.

## Diagnose Workflow

Use when the author asks "what archetype is this character?" for a character who already exists (in the manuscript or the Story Bible).

1. **Gather material:** existing traits, actions, and dialogue provided by the author, or the character's Story Bible entry.
2. **Score against both taxonomies independently.** Read `narrative-role-archetypes.md` and `personality-archetypes.md` and check the character's signals against each entry's "Common signals" (narrative-role) or "Voice/dialogue tendencies" and "Strategy" (personality). The two axes are independent — don't force one to imply the other.
3. **Name the best-fit pairing with rationale**, citing which signals matched which entry.
4. **Flag blends:** a character can straddle two archetypes within one taxonomy (e.g., a Mentor sliding into Shadow). Name both, and say which is dominant.
5. **Flag deliberate subversions:** check the matched entry's "Subversion patterns" section — if the character's behavior matches a named subversion rather than the base pattern, say so instead of reporting a mismatch.

## Recommend Workflow

Use when the author wants a starting pairing for a character who isn't fully built yet.

1. **Get the stated story role:** what does this character need to *do* in the plot (the narrative-role question), and/or what personality would create interesting friction with the existing cast (the personality question)? If neither is stated, ask before proceeding.
2. **Suggest 1-3 pairing candidates**, each with a one-line rationale.
3. **Note cast contrast:** if relevant, name which existing cast members the pairing would create tension or contrast with.

## Output Format

- **Diagnose:** "[Character] reads as [Narrative-Role] + [Personality-Type]. Signals: [cite the matched signals]. [Blend or subversion note, if any.]"
- **Recommend:** "For a character who needs to [stated role], consider [Pairing A] ([why]), or [Pairing B] ([why])."

## Stops When

The pairing (or recommendation) is named with rationale. Hand back to the author for confirmation. Do not auto-write the result into the Story Bible — offer the `assets/archetype-profile-template.md` block and let the author decide whether and how to record it.

## Common Pitfalls

| Pitfall | Fix |
|---|---|
| Forcing a pairing when signals are genuinely mixed | Say so, and offer the blend instead of picking one |
| Diagnosing off too little material (a single line of dialogue) | Ask for more before committing to a pairing |
| Treating a Recommend suggestion as a decision | Frame it as a starting point — the author still chooses |
```

- [ ] **Step 2: Verify structure**

```bash
grep -E "^## (Diagnose Workflow|Recommend Workflow|Output Format|Stops When|Common Pitfalls)$" skills/character-archetypes/references/archetype-analyzer.md | wc -l
```
Expected: `5`.

```bash
grep -in "TBD\|TODO\|fill in" skills/character-archetypes/references/archetype-analyzer.md
```
Expected: no output.

- [ ] **Step 3: Commit**

```bash
git add skills/character-archetypes/references/archetype-analyzer.md
git commit -m "feat: add archetype analyzer mode reference"
```

---

### Task 5: Write `references/archetype-audit.md`

**Files:**
- Create: `skills/character-archetypes/references/archetype-audit.md`

**Interfaces:**
- Consumes: Assumes an archetype pairing has already been established (via Task 4's Analyzer, or stated author intent) — this mode cannot run without one.
- Produces: The Audit workflow, referenced by `SKILL.md`'s mode table (Task 1) and ordering guidance (Analyzer → Audit → Conformance → Ensemble).

- [ ] **Step 1: Write `skills/character-archetypes/references/archetype-audit.md`**

```markdown
# Archetype Audit Reference

When invoked to check whether an established archetype is being used well, or as cliché. Requires a target archetype already established — via `archetype-analyzer.md`'s Diagnose mode, or stated author intent. Audit can't judge stock use without knowing what's being checked against; if no archetype is established yet, run Analyzer first.

## What This Audit Catches

- A character behaving as a stock instance of their archetype with no individualizing detail — dialogue, choices, or reactions that could belong to any character with that archetype, rather than this specific one.
- Archetype behavior used as a substitute for characterization, rather than a scaffold for it.

## What This Audit Does NOT Catch

- Whether the archetype pairing itself is correct — that's `archetype-analyzer.md`'s job.
- Whether the character's archetype has drifted over a longer span — that's `archetype-conformance.md`'s job (opposite failure direction: too-stock-in-one-scene vs. drifted-over-chapters).
- Prose-level issues (word choice, sentence rhythm) — that's `prose-mechanics`.

## Workflow

1. **Confirm the target archetype pairing** for the character being audited (ask if not already known).
2. **Scan the requested scope** (scene, chapter, or sketch) for moments where the character's actions, dialogue, or reactions match the archetype entry's baseline pattern (narrative-role "Common signals" or personality "Strategy"/"Voice tendencies") **without** any individualizing detail layered on top.
3. **For each flagged moment**, note: the cliché beat (quote or describe it), which archetype pattern it's a stock instance of, and a suggested individualizing angle (drawn from the character's Want/Need/Wound/Lie, if known, or a prompt to establish one).
4. **Do not rewrite.** Deliver the flagged list only.

## Output Format

A flagged list, one entry per instance:

```
[Location] — [Cliché beat, quoted or described]
Stock pattern: [archetype] + [which field it matches — e.g., Sage's "Strategy"]
Suggested individualizing angle: [specific detail that would make this beat unmistakably this character's, not any Sage's]
```

## Stops When

The flagged cliché list is delivered for the requested scope. No auto-rewrite — the author decides which flags are real problems and how to fix them.

## Common Pitfalls

| Pitfall | Fix |
|---|---|
| Running Audit with no established archetype | Run `archetype-analyzer.md` first, or confirm stated author intent |
| Flagging every archetype-consistent beat as cliché | Consistency isn't the problem — the *absence of individualizing detail* is. A consistent beat with specific voice/detail is not a flag. |
| Rewriting flagged passages | Audit is diagnostic only. Deliver the list; let the author revise. |
```

- [ ] **Step 2: Verify structure**

```bash
grep -E "^## (What This Audit Catches|What This Audit Does NOT Catch|Workflow|Output Format|Stops When|Common Pitfalls)$" skills/character-archetypes/references/archetype-audit.md | wc -l
```
Expected: `6`.

- [ ] **Step 3: Commit**

```bash
git add skills/character-archetypes/references/archetype-audit.md
git commit -m "feat: add archetype audit mode reference"
```

---

### Task 6: Write `references/archetype-conformance.md`

**Files:**
- Create: `skills/character-archetypes/references/archetype-conformance.md`

**Interfaces:**
- Consumes: Assumes an archetype pairing has already been established for the character being checked.
- Produces: The Conformance workflow, referenced by `SKILL.md`'s mode table (Task 1).

- [ ] **Step 1: Write `skills/character-archetypes/references/archetype-conformance.md`**

```markdown
# Archetype Conformance Reference

When invoked to check whether a character is still consistent with their established archetype pairing across a chapter range. Same delivery pattern as `fiction-workshop`'s `continuity-tracking.md`, but archetype-specific rather than fact/timeline-specific. Requires a target archetype already established (via `archetype-analyzer.md` or stated author intent).

## What This Checks

Whether the character's actions across the requested range stay consistent with their established narrative-role and personality-type pairing — distinguishing:

- **Legitimate arc progression** (e.g., a Hero maturing into a Ruler as the story's power dynamics shift) — not a flag.
- **Unexplained drift** (e.g., an established Sage abruptly acting like an impulsive Rebel with no setup, pressure, or turning point to justify it) — a flag.

## Workflow

1. **Confirm the character's established pairing** for the requested range.
2. **Read the requested chapter range**, tracking the character's choices and reactions scene by scene.
3. **For each moment that departs from the established pairing's pattern**, check for justification: does the story show a pressure, a turning point, or a setup earlier in the range that explains the shift? (See each taxonomy entry's "Subversion patterns" — an explained shift into one of those is not drift.)
4. **If justified:** do not flag — this is arc progression, not drift.
5. **If unjustified:** flag it, anchored to the chapter/scene where it occurs.

## Output Format

Drift flags anchored to location:

```
[Chapter/Scene] — [Character] acts as [departing pattern] instead of established [archetype pairing]
Established pattern: [what the pairing's baseline behavior would predict here]
What actually happens: [the departure]
Justification found: [none / describe what's present but insufficient]
```

## Stops When

Drift flags are delivered for the requested range. No auto-fix — the author decides which flags represent real, unintended drift versus arc progression the audit failed to recognize as legitimate.

## Common Pitfalls

| Pitfall | Fix |
|---|---|
| Flagging arc growth as drift | Legitimate arc progression (e.g., Hero → Ruler) is not drift. Check for setup/pressure before flagging. |
| Running Conformance with no established archetype | Establish one via `archetype-analyzer.md` first |
| Treating every character inconsistency as archetype-related | Some inconsistencies are plain continuity errors (see `fiction-workshop`'s `continuity-tracking.md`), not archetype drift |
```

- [ ] **Step 2: Verify structure**

```bash
grep -E "^## (What This Checks|Workflow|Output Format|Stops When|Common Pitfalls)$" skills/character-archetypes/references/archetype-conformance.md | wc -l
```
Expected: `5`.

- [ ] **Step 3: Commit**

```bash
git add skills/character-archetypes/references/archetype-conformance.md
git commit -m "feat: add archetype conformance mode reference"
```

---

### Task 7: Write `references/archetype-ensemble.md`

**Files:**
- Create: `skills/character-archetypes/references/archetype-ensemble.md`

**Interfaces:**
- Consumes: Assumes most main cast members already have an assigned archetype pairing — the one cast-level mode, versus the other three which operate on a single character.
- Produces: The Ensemble workflow, referenced by `SKILL.md`'s mode table and ordering guidance (Task 1) as the final, late-stage mode.

- [ ] **Step 1: Write `skills/character-archetypes/references/archetype-ensemble.md`**

```markdown
# Archetype Ensemble Reference

When invoked to check whether a cast's archetypes are balanced. The one cast-level mode — `archetype-analyzer.md`, `archetype-audit.md`, and `archetype-conformance.md` all operate on a single character; this operates on the full cast at once. Late-stage check: run it once most main characters already have an assigned archetype pairing, not as a starting point.

## What This Checks

Tallies narrative-role and personality distribution across the full main cast and flags three failure patterns:

1. **Redundancy:** multiple characters sharing a pairing with no meaningful differentiation between them.
2. **Structural gaps:** the protagonist has no Mentor, Shadow, or Threshold Guardian presence anywhere in the cast.
3. **Static relational pairs:** two characters with the same archetype (e.g., two Rulers) locked in a relationship with no power-dynamic arc.

## Workflow

1. **Confirm the cast list** and each member's established archetype pairing (ask for any that are missing; do not guess).
2. **Tally narrative-role and personality distribution** across the cast.
3. **Check for redundancy:** any pairing shared by two or more characters? If so, check whether the design spec's individualizing detail (voice, wound, specific flaw) differentiates them enough to justify the overlap, or whether they're functionally interchangeable.
4. **Check for structural gaps:** does the protagonist's cast include a Mentor, a Shadow, and a Threshold Guardian somewhere? A missing one isn't automatically wrong, but is worth surfacing.
5. **Check for static relational pairs:** any two same-archetype characters in an ongoing relationship (rivals, co-leads, family) with no arc to their power dynamic across the story?
6. **Deliver a cast balance report.** Do not invent new characters to fill gaps — that's the author's call.

## Output Format

A cast balance report, grouped by finding type:

```
Redundancy:
- [Character A] and [Character B] both read as [pairing] — [differentiated by X / functionally interchangeable]

Structural gaps:
- No [archetype] presence found for [protagonist]'s cast

Static relational pairs:
- [Character A] and [Character B] are both [archetype] in an ongoing [relationship type] with no power-dynamic arc across [range checked]
```

## Stops When

The cast balance report is delivered. The author decides on any cast changes — do not auto-invent new characters or reassign existing ones.

## Common Pitfalls

| Pitfall | Fix |
|---|---|
| Running Ensemble before the cast has archetypes assigned | This is a late-stage check — assign pairings via `archetype-analyzer.md` first |
| Treating any redundancy as automatically wrong | Two characters can share a pairing if individualizing detail differentiates them — check before flagging |
| Inventing new characters to fill a structural gap | Report the gap; let the author decide whether and how to fill it |
```

- [ ] **Step 2: Verify structure**

```bash
grep -E "^## (What This Checks|Workflow|Output Format|Stops When|Common Pitfalls)$" skills/character-archetypes/references/archetype-ensemble.md | wc -l
```
Expected: `5`.

- [ ] **Step 3: Commit**

```bash
git add skills/character-archetypes/references/archetype-ensemble.md
git commit -m "feat: add archetype ensemble mode reference"
```

---

### Task 8: Write `assets/archetype-profile-template.md`

**Files:**
- Create: `skills/character-archetypes/assets/archetype-profile-template.md`

**Interfaces:**
- Consumes: Nothing.
- Produces: The Story Bible paste-in block referenced by `SKILL.md` (Task 1, "Integration with fiction-workshop") and by Task 9's edit to `fiction-workshop/references/character-work.md`. Must fit directly after the "Voice notes:" line in the example Story Bible entry shown in `fiction-workshop/SKILL.md:81-90`.

- [ ] **Step 1: Write `skills/character-archetypes/assets/archetype-profile-template.md`**

```markdown
# Archetype Profile Template

A small block designed to paste directly into an existing Story Bible character entry, immediately after "Voice notes:" (see the example entry in `fiction-workshop/SKILL.md`). Not a replacement for the Want/Need/Wound/Lie fields already there — this adds the archetype layer on top.

```
Archetype profile:
- Narrative-role: [e.g., Mentor — see character-archetypes/references/narrative-role-archetypes.md]
- Personality-type: [e.g., Sage — see character-archetypes/references/personality-archetypes.md]
- Individualizing detail: [the specific voice/wound/flaw — from this entry's Want/Need/Wound/Lie — that keeps this character from reading as a stock instance of the pairing above]
- Subversion (if any): [how this character deliberately breaks the pairing's expected pattern, and why — leave blank if none]
- Last archetype check: [Analyzer / Audit / Conformance / Ensemble — date]
```

## Usage Notes

- Fill in immediately after naming a pairing via `archetype-analyzer.md`'s Diagnose or Recommend workflow.
- "Individualizing detail" should point back at the character's existing Want/Need/Wound/Lie fields, not restate the archetype's generic weakness/trap.
- Update "Last archetype check" whenever any of the four modes runs against this character, so a later session knows whether a re-check is due.
```

- [ ] **Step 2: Verify structure**

```bash
grep -c "^- Narrative-role:\|^- Personality-type:\|^- Individualizing detail:\|^- Subversion (if any):\|^- Last archetype check:" skills/character-archetypes/assets/archetype-profile-template.md
```
Expected: `5`.

- [ ] **Step 3: Commit**

```bash
git add skills/character-archetypes/assets/archetype-profile-template.md
git commit -m "feat: add archetype profile Story Bible template"
```

---

### Task 9: Wire into `fiction-workshop`

**Files:**
- Modify: `skills/fiction-workshop/references/character-work.md` (insert new subsection after the existing "### Character Arc Types" subsection, before "## Voice Consistency")
- Modify: `skills/fiction-workshop/SKILL.md:269` (the `character-work.md` line in the "Files" list)

**Interfaces:**
- Consumes: The `character-archetypes` skill name and `archetype-analyzer.md` mode name from Tasks 1 and 4 — must reference them exactly.
- Produces: Nothing new — this is the integration point closing the loop described in `SKILL.md`'s "Integration with fiction-workshop" section (Task 1).

- [ ] **Step 1: Insert the new subsection into `character-work.md`**

In `skills/fiction-workshop/references/character-work.md`, find this exact text (lines 22-27):

```markdown
### Character Arc Types

**Positive arc**: Character overcomes lie, gets need, may or may not get want
**Negative arc**: Character clings to lie, fails to grow, often tragic outcome
**Flat arc**: Character already knows truth, changes the world around them

## Voice Consistency
```

Replace it with:

```markdown
### Character Arc Types

**Positive arc**: Character overcomes lie, gets need, may or may not get want
**Negative arc**: Character clings to lie, fails to grow, often tragic outcome
**Flat arc**: Character already knows truth, changes the world around them

### Complementary Lens: Archetypes

Want/Need/Wound/Lie describes a character's individual psychology. For the
patterns a character shares with a role or personality type — Hero, Mentor,
Sage, Trickster, and so on — see the `character-archetypes` skill. Run its
Analyzer mode to name a narrative-role and personality-type pairing, then
keep using the Core Four here to individualize it so the archetype doesn't
read as a stock type.

## Voice Consistency
```

- [ ] **Step 2: Update the Files list line in `SKILL.md`**

In `skills/fiction-workshop/SKILL.md`, find this exact line (line 269):

```markdown
- `references/character-work.md` - Voice, motivation, arc tracking
```

Replace it with:

```markdown
- `references/character-work.md` - Voice, motivation, arc tracking (see also the `character-archetypes` skill for role/personality archetype analysis)
```

- [ ] **Step 3: Verify**

```bash
grep -A1 "### Complementary Lens: Archetypes" skills/fiction-workshop/references/character-work.md
```
Expected: the inserted paragraph text, starting with "Want/Need/Wound/Lie describes...".

```bash
grep "character-archetypes" skills/fiction-workshop/references/character-work.md skills/fiction-workshop/SKILL.md
```
Expected: one match in each file.

```bash
grep -c "^## Voice Consistency$" skills/fiction-workshop/references/character-work.md
```
Expected: `1` (confirms the replace didn't duplicate or drop the following section header).

- [ ] **Step 4: Commit**

```bash
git add skills/fiction-workshop/references/character-work.md skills/fiction-workshop/SKILL.md
git commit -m "feat: link character-archetypes skill from fiction-workshop"
```

---

### Task 10: Update root `README.md`

**Files:**
- Modify: `README.md`

**Interfaces:**
- Consumes: Skill name `character-archetypes`, its four mode names, and its two taxonomy names from Tasks 1-3.
- Produces: Nothing new — this is documentation only.

- [ ] **Step 1: Add the "Character Archetypes" subsection**

In `README.md`, find this exact text (the boundary between the Fiction Workshop and Narrative Nonfiction subsections, lines 18-23):

```markdown
Includes genre-specific guides for:
- Spy thrillers (tradecraft, tension, moral complexity)
- Hard sci-fi (technical accuracy, worldbuilding, geopolitics)

### Narrative Nonfiction
```

Replace it with:

```markdown
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

### Narrative Nonfiction
```

- [ ] **Step 2: Add the invocation line and usage example**

Find this exact text (lines 80-85):

```markdown
```bash
/author-toolkit:fiction-workshop
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
/author-toolkit:narrative-nonfiction
/author-toolkit:prose-mechanics
/author-toolkit:avoid-ai-writing
```
```

Find this exact text (lines 88-93):

```markdown
```
# Fiction
"As developmental editor, analyze Chapter 3"
"As line editor, polish this dialogue"
"Brainstorm mode—I need to solve [plot problem]"

# Nonfiction
```
```

Replace it with:

```markdown
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

# Nonfiction
```
```

- [ ] **Step 3: Add rows to the Quick Reference table**

Find this exact text (the "Get unstuck" row and the blank line before "Nonfiction writing" in the Quick Reference table):

```markdown
| Get unstuck | `/author-toolkit:fiction-workshop` | "Brainstorm mode—I need to [solve problem]" |
| Nonfiction writing | `/author-toolkit:narrative-nonfiction` | "Let's build a blueprint for [book]" |
```

Replace it with:

```markdown
| Get unstuck | `/author-toolkit:fiction-workshop` | "Brainstorm mode—I need to [solve problem]" |
| Archetype identification | `/author-toolkit:character-archetypes` | "What archetype is this character?" |
| Archetype cliché check | `/author-toolkit:character-archetypes` | "Audit [scene] for archetype cliché" |
| Archetype drift check | `/author-toolkit:character-archetypes` | "Check archetype conformance for chapters [X-Y]" |
| Cast balance check | `/author-toolkit:character-archetypes` | "Run an ensemble balance check on the cast" |
| Nonfiction writing | `/author-toolkit:narrative-nonfiction` | "Let's build a blueprint for [book]" |
```

- [ ] **Step 4: Verify**

```bash
grep -c "^### Character Archetypes$" README.md
```
Expected: `1`.

```bash
grep -c "character-archetypes" README.md
```
Expected: `5` (1 invocation-block line + 4 Quick Reference table rows — the new "### Character Archetypes" section heading and body use the spaced/capitalized skill name, not the `character-archetypes` slug, so they don't count here).

```bash
grep -c "^/author-toolkit:" README.md
```
Expected: `5` (all five skills now listed in the invocation block).

- [ ] **Step 5: Commit**

```bash
git add README.md
git commit -m "docs: add character-archetypes to README"
```

---

### Task 11: Bump plugin metadata

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
  "version": "1.2.0",
  "author": {
    "name": "rhavekost",
    "email": "rob@kostlabs.com"
  },
  "homepage": "https://github.com/rhavekost/author-toolkit",
  "repository": "https://github.com/rhavekost/author-toolkit",
  "license": "MIT",
  "keywords": ["writing", "fiction", "nonfiction", "editing", "author", "skills", "ai-writing", "avoid-ai-writing", "character-archetypes"]
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
      "version": "1.2.0",
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
grep '"version": "1.2.0"' .claude-plugin/plugin.json .claude-plugin/marketplace.json
grep "character-archetypes" .claude-plugin/plugin.json
```
Expected: both files print "valid JSON", the version grep matches in both files, and the keyword grep matches once in `plugin.json`.

- [ ] **Step 4: Commit**

```bash
git add .claude-plugin/plugin.json .claude-plugin/marketplace.json
git commit -m "chore: bump plugin version to 1.2.0 for character-archetypes skill"
```

---

## Task Order and Dependencies

Tasks 1-8 build the new skill; Task 1 (SKILL.md) can be written first since it only references paths, not content, but Tasks 2-8 have no dependencies on each other or on Task 1 and could run in any order. Task 9 depends on Tasks 1 and 4 existing (references the skill and Analyzer mode by name). Task 10 depends on Task 1 (skill name and mode names). Task 11 has no content dependency but should run last as the "this feature is complete" version bump. Recommended sequential order for a single-session run: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11.
