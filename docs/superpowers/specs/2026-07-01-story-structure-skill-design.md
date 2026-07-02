# Design Spec: `story-structure` Skill

**Date:** 2026-07-01
**Status:** Approved by user, pending implementation plan

## Purpose

A new skill, `story-structure`, that gives Claude a concrete, percentage-anchored model of macro story structure — where the major turning points of a novel should land, what psychological/dramatic work each one needs to do, and how to tell when one is missing, mistimed, or hollow.

It is a companion to `fiction-workshop`, following the same pattern already established by `character-archetypes`: `fiction-workshop` keeps a lightweight generic framework for quick reads, and the new skill is the deeper, opt-in diagnostic layer for when structure needs serious scrutiny.

## Source Material

Three craft books were extracted directly (full epub read, not general knowledge) to ground the skill in accurate, citable terminology:

1. **K.M. Weiland, *5 Secrets of Story Structure*** — the primary placement skeleton and its five "secrets": the Inciting Event, the Key Event, the Pinch Points, the Moment of Truth, the Climactic Moment.
2. **K.M. Weiland, *Structuring Your Novel*** — the same skeleton with finer fractional placement (3/8, 5/8 marks) and additional diagnostics (Faux Climax, Inciting-vs-Key-Event distinction, opening/closing-line checklists).
3. **James Scott Bell, *Super Structure*** — a complementary framework of 14 named "signposts," which the book itself frames as being about *what psychological/emotional work* a beat must do rather than *where* it falls. Used as the content-diagnostic layer overlaid on Weiland's placement skeleton.

A fourth book, Weiland's *Creating Character Arcs* (which owns the full Lie/Ghost/Thematic-Truth apparatus), was **not** extracted — this skill cross-links to `fiction-workshop`'s existing Want/Need/Wound/Lie framework instead of re-deriving arc mechanics from a different source, to avoid two non-identical versions of the same concept living in this repo.

## Scope

**In scope:**
- Macro-level structure: the landmark beats that divide a manuscript into acts, by percentage.
- Bell's 14 signposts, in full, as a content/psychology check layered onto (or between) those landmarks.
- Two named failure-mode diagnostics that are genuinely distinctive and commonly missed: the Inciting Event / Key Event / First Plot Point confusion, and the Faux Climax trap.
- Two modes: **Map** (outline-stage placement for a new story) and **Audit** (draft-stage diagnosis of an existing manuscript).

**Out of scope (deliberately, to avoid duplicating existing skills):**
- Scene/sequel micro-structure (Goal-Conflict-Disaster / Reaction-Dilemma-Decision). `fiction-workshop/references/developmental-editing.md` already has an equivalent Scene-Level Goal/Conflict/Outcome/Sequel section — not worth a second, slightly-different version.
- Full character-arc mechanics (Lie, Ghost, Wound, Thematic Truth). Owned by `fiction-workshop/references/character-work.md`. This skill only notes *which structural beat* is where the Lie is tested (Third Plot Point) and resolved (Climax), and links out rather than redefining.
- Any book/genre/series-level guidance beyond a brief FAQ-style note — low value relative to the core skeleton, and risks scope creep into a different skill entirely.
- Replacing `developmental-editing.md`'s existing generic Structure Analysis Framework. It stays as-is; one cross-link is added pointing to this new skill for deeper work.

## The Landmark Beat Skeleton (Weiland)

Reconciled from both Weiland books — "5 Secrets" naming, "Structuring Your Novel"'s finer fractional placement where more precise:

| Beat | Placement | Function |
|---|---|---|
| Hook | Opening page/line | Poses the story's driving question |
| Inciting Event | ~12% | First touch of conflict on the Normal World; often initially resisted |
| Key Event | End of Act 1, may coincide with FPP | The moment the protagonist *leaves* the Normal World (distinct from merely encountering it) |
| First Plot Point | 25% (range ~18–27%) | Point of no return; enters the "adventure world" |
| First Pinch Point | 37.5% (3/8) | Antagonist "flexes muscle"; new clues about the conflict's true nature |
| Midpoint / Moment of Truth | 50% | Reaction → action pivot; protagonist grasps the central truth of the conflict |
| Second Pinch Point | 62.5% (5/8) | Stakes raised concretely (cost, not just clues) |
| Third Plot Point | 70–75% | Low point; climax of the character's *inner* arc — faces the Lie/Truth |
| Third Act Turning Point | 88% | Forces final direct confrontation |
| Climactic Moment | 90–98% | Protagonist's (or antagonist's) goal is realized or denied — true story end |
| Resolution | Final 1–2% | "Exhale to the Climax's inhale" |

**Two named failure-mode diagnostics get their own callouts:**
- **Inciting Event vs. Key Event vs. First Plot Point** — commonly conflated into one beat; they can be distinct scenes and each has a different job.
- **Faux Climax** — a scene that reads as climactic (apparent goal achieved) but isn't the true climax because a bigger obstacle remains; diagnostic test is Weiland's own: "when is the protagonist's/antagonist's goal *actually* realized, such that no more obstacles remain?"

## Bell's 14 Signposts — Full Catalog

All 14 are included, split by how they relate to the Weiland skeleton above:

**Six overlay a Weiland landmark directly** (become that landmark's content/psychology check):
| Signpost | Overlays |
|---|---|
| Disturbance | Hook / Inciting Event |
| Doorway of No Return #1 | First Plot Point |
| Mirror Moment | Midpoint |
| Doorway of No Return #2 | Third Plot Point |
| Final Battle | Climactic Moment |
| Transformation | Climax / Resolution |

**Eight fall between landmarks at looser, relative placement** (their own catalog entries, Bell's own order and placement language, not forced onto a percentage):
Care Package, Argument Against Transformation, Trouble Brewing, Kick in the Shins, Pet the Dog, Mounting Forces, Lights Out, Q Factor.

Each of the 14 gets: name, placement (percentage if landmark-anchored, relative if not), function, and a diagnostic question — drawn from Bell's "Why This Works" sections and his closing Checklist of Reminders where available.

## Modes

### Map (outline-stage)
For a story not yet drafted (or only partially). Walks through the landmark skeleton in order, asks what's planned for each beat and each relevant signpost, and flags gaps (e.g., no planned Mirror Moment content, no Q Factor plant). Ends by handing back a Structure Map block for the user to paste into their Story Bible. Does not write to the Story Bible directly (same rule as `character-archetypes`).

### Audit (draft-stage)
For an existing manuscript or manuscript-in-progress. Locates where beats actually land (by approximate percentage through the draft), checks each against both its placement expectation and its Bell content-check, and flags: missing beats, mistimed beats (drifted more than ~10 points from expected placement), and thin beats (present but not doing the psychological work Bell's diagnostic asks for). Reports the Faux-Climax check explicitly if multiple climax-shaped scenes exist. Hands back a flagged-beat report; does not rewrite the manuscript.

**Ordering guidance:** Map is for pre-draft planning; Audit is for anything already written. They are not sequential stages of the same session — a user runs whichever mode matches their current stage, same as `character-archetypes`' mode-selection pattern.

## File Structure

Mirrors the `character-archetypes` skill exactly:

```
skills/story-structure/
  SKILL.md                          — overview, when/when-not, mode table, integration notes
  references/
    landmark-beats.md               — the Weiland skeleton, percentages, diagnostics, two failure-mode callouts
    signposts.md                    — Bell's full 14-signpost catalog, in his order, cross-referenced to landmarks
    structure-map.md                — Map mode workflow
    structure-audit.md              — Audit mode workflow
  assets/
    structure-profile-template.md   — pasteable Story Bible block (beat-by-beat placement + signpost notes)
```

## Integration with Existing Skills

- One cross-link added from `fiction-workshop/references/developmental-editing.md`'s existing Structure Analysis Framework section, pointing to this skill for deeper work. No other changes to that file.
- One cross-link added from `fiction-workshop/references/character-work.md`, noting that Third Plot Point / Climax are where the Lie is tested/resolved, pointing back to this skill for the full placement model (mirrors the existing `character-archetypes` ↔ `character-work.md` link).
- `assets/structure-profile-template.md` designed to paste into the Story Bible immediately alongside (not replacing) the existing "Plot Foundation → Three-Act Structure" section in `fiction-workshop/assets/story-bible-template.md` — that section already has Act I/Midpoint/Act II-B/Act III placeholders; the new template adds the finer landmark-beat percentages and signpost notes on top, the same "additive block, not a restructure" rule `character-archetypes` follows for character entries.
- README.md gets a new "Story Structure" section describing the skill, modeled on the existing "Character Archetypes" section.
- `.claude-plugin/marketplace.json` gets updated to register the new skill (same as was done for `character-archetypes`).

## Stopping Points

Same discipline as `character-archetypes`: each mode has a defined end (Map → hand back Structure Map block; Audit → hand back flagged-beat report). Do not auto-advance between modes, do not write to the Story Bible without being asked, do not rewrite manuscript prose as part of Audit.
