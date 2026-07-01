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
3. **Check for redundancy:** any pairing shared by two or more characters? If so, check whether individualizing detail (voice, wound, specific flaw) differentiates them enough to justify the overlap, or whether they're functionally interchangeable.
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
