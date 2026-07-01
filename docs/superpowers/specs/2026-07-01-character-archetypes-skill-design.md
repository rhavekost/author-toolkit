# Character Archetypes Skill — Design

## Purpose

`fiction-workshop` has no vocabulary for character archetypes (Hero, Mentor,
Trickster, Jungian personality types, etc.) — only the Want/Need/Wound/Lie
framework in `character-work.md`. This adds a dedicated, fiction-scoped skill
covering the two main universal archetype taxonomies, plus four analysis
modes for using them diagnostically across a manuscript.

Scope: fiction only. Not intended to serve `narrative-nonfiction` (author
voice / reader-persona archetypes are a different, unaddressed problem).

## Location and naming

New top-level skill, sibling to the existing four:

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

Standalone skill rather than folding into `fiction-workshop` because: (a) the
two taxonomies plus four modes are comparable in size to `fiction-workshop`
itself (which already has 7 references and 5 personas — adding this would
roughly double it), and (b) the plugin already has precedent for splitting
complementary-but-distinct concerns into their own skill (`prose-mechanics`,
`avoid-ai-writing` both sit alongside `fiction-workshop` rather than inside
it).

Trigger phrases: "character archetype," "archetype audit," "what archetype
is this character," "archetype conformance," "Hero's Journey character
role," "Jungian archetype."

## The two taxonomies

A character gets tagged with **one archetype from each list** — they
describe different things (plot function vs. psychology) and normally
combine (e.g., narrative-role Mentor + personality Sage).

**`narrative-role-archetypes.md`** — Vogler/Campbell's 8 character
functions. Each entry: definition, narrative purpose, common signals,
subversion patterns, one worked example.
- Hero, Mentor, Threshold Guardian, Herald, Shapeshifter, Shadow, Trickster,
  Ally

**`personality-archetypes.md`** — Jungian 12 (Mark & Pearson model). Each
entry: core desire, greatest fear, strategy, characteristic weakness/trap,
voice/dialogue tendencies, one worked example.
- Innocent, Everyman, Hero, Caregiver, Explorer, Rebel, Lover, Creator,
  Jester, Sage, Magician, Ruler

Both files state explicitly: **archetype is a starting scaffold, not a
finished character.** Individualizing detail (voice, wound, specific flaw —
from `character-work.md`) is what keeps an archetype from reading as a
stock type. The Audit mode enforces this directly.

## The four analysis modes

Ordering guidance: **Analyzer → (optional) Audit → Conformance → Ensemble.**
Skip straight to Audit or Conformance if the archetype is already decided.
Ensemble is a late-stage check — it needs most main characters to already
have an assigned archetype.

### Analyzer (`archetype-analyzer.md`)
"What archetype is this character?" — bidirectional:
- **Diagnose:** given existing traits/actions/dialogue or a Story Bible
  entry, score against both taxonomies, name the best-fit narrative-role +
  personality pairing, flag blends and deliberate subversions.
- **Recommend:** given a stated story role for a not-yet-built character,
  suggest a pairing to start from.

Stops when the pairing (or recommendation) is named with rationale. Hands
back for author confirmation — does not auto-write into the Story Bible.

### Audit (`archetype-audit.md`)
"Is this archetype used well, or as cliché?" — scans a scene/chapter/sketch
for moments where a character behaves as a stock instance of their
archetype with no individualizing detail. Requires a target archetype
already established (via Analyzer or stated author intent) — audit can't
judge stock use without knowing what's being checked against.

Output: flagged list, each with the cliché beat + a suggested
individualizing angle. No auto-rewrite.

### Conformance (`archetype-conformance.md`)
"Is this character still who we said they were?" — checks whether actions
across a chapter range stay consistent with the character's established
archetype pairing, distinguishing legitimate arc progression (Hero maturing
into Ruler) from unexplained drift (established Sage abruptly acting like
an impulsive Rebel with no setup). Same delivery pattern as
`continuity-tracking.md`, but archetype-specific rather than fact/timeline-
specific.

Output: drift flags anchored to chapter/scene. No auto-fix.

### Ensemble (`archetype-ensemble.md`)
"Is the cast balanced?" — the one cast-level mode; the other three operate
on a single character. Tallies narrative-role + personality distribution
across the full cast (once each has an assigned archetype) and flags:
- redundancy (multiple characters sharing a pairing with no
  differentiation)
- structural gaps (protagonist has no Mentor/Shadow/Threshold Guardian
  presence anywhere in the cast)
- static relational pairs (two Rulers with no power-dynamic arc)

Output: a cast balance report. Author decides on cast changes — doesn't
auto-invent new characters.

**Why four modes, not fewer:** Audit and Conformance check *opposite*
failure directions (too-stock-in-one-scene vs. drifted-over-chapters), so
they aren't redundant. Ensemble operates at a different altitude (cast vs.
single character) than all three others. Analyzer's "recommend" direction
was folded into Analyzer itself rather than spun out as a fifth mode, since
the taxonomy lookup is identical either direction.

## Integration with `fiction-workshop`

Minimal footprint — no structural changes to existing files:
- `fiction-workshop/references/character-work.md` gets a short added
  section (~5 lines) pointing to `character-archetypes` as a complementary
  lens, positioned alongside (not replacing) the Want/Need/Wound/Lie
  framework.
- `fiction-workshop/SKILL.md`'s "Files" list gets a one-line addition
  noting the related skill.
- Root `README.md`'s skill list and Quick Reference table get an entry for
  `character-archetypes`, matching the existing pattern for each skill.
- `assets/archetype-profile-template.md` is a small block format (pairing +
  individualizing notes + subversion notes) designed to be pasted directly
  into the existing Story Bible character entry format already shown in
  `fiction-workshop/SKILL.md` (after "Voice notes:"). `story-bible-
  template.md` itself is not restructured.

## Stopping points

| Mode | Stops when... |
|---|---|
| Analyzer | Archetype pairing (or recommendation) named with rationale — hands back, doesn't auto-write to Story Bible |
| Audit | Flagged cliché list delivered — no auto-rewrite |
| Conformance | Drift flags delivered for requested range — author decides what's real drift vs. legitimate arc |
| Ensemble | Cast balance report delivered — author decides on cast changes |

## Common mistakes

| Mistake | Fix |
|---|---|
| Treating archetype as a rigid mold | Archetype is scaffold, not finished character — individualizing detail is mandatory |
| Confusing narrative-role with personality-type | They're independent axes; a Hero (role) can be a Sage (personality) |
| Running Audit before an archetype is established | Audit needs a target to judge cliché against — run Analyzer first (or use stated intent) |
| Flagging arc growth as Conformance drift | Legitimate arc progression isn't drift — only *unexplained* inconsistency is |
| Running Ensemble before main cast has archetypes assigned | Ensemble is a late-stage check, not a starting point |

## Out of scope

- Narrative-nonfiction archetype use (author voice, reader persona,
  branding archetypes) — explicitly excluded per scope decision.
- Enneagram or other personality typologies — two canonical frameworks
  (Vogler narrative-role, Jungian 12) are sufficient; adding more blurs
  into general personality-typing rather than archetype work.
- Plot/genre archetypes (monomyth stages, genre tropes) — this skill is
  character-scoped only; plot-level concerns remain in
  `developmental-editing.md`.
