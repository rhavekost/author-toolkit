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
2. **Scan the requested scope** (scene, chapter, or sketch) for moments where the character's actions, dialogue, or reactions match the archetype entry's baseline pattern (narrative-role "Common signals" or personality "Strategy"/"Voice/dialogue tendencies") **without** any individualizing detail layered on top.
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
