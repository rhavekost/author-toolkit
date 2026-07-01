# Archetype Conformance Reference

When invoked to check whether a character is still consistent with their established archetype pairing across a chapter range. Same delivery pattern as `fiction-workshop`'s `continuity-tracking.md`, but archetype-specific rather than fact/timeline-specific. Requires a target archetype already established (via `archetype-analyzer.md` or stated author intent).

## What This Checks

Whether the character's actions across the requested range stay consistent with their established narrative-role and personality-type pairing — distinguishing:

- **Legitimate arc progression** (e.g., a Hero maturing into a Ruler as the story's power dynamics shift) — not a flag.
- **Unexplained drift** (e.g., an established Sage abruptly acting like an impulsive Rebel with no setup, pressure, or turning point to justify it) — a flag.

## Workflow

1. **Confirm the character's established pairing** for the requested range.
2. **Read the requested chapter range**, tracking the character's choices and reactions scene by scene.
3. **For each moment that departs from the established pairing's pattern**, check for justification: does the story show a pressure, a turning point, or a setup earlier in the range that explains the shift? (See the narrative-role entry's "Subversion patterns" — an explained shift into one of those is not drift.)
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
