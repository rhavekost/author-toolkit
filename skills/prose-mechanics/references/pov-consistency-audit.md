# POV-Consistency Audit Reference

Pure session judgment — flags head-hopping and knowledge-timeline
violations against the chapter's established POV character(s).

## What This Catches
Narration reporting another character's unperceivable internal state, or
the POV character acting on knowledge they haven't yet learned.

## What This Does NOT Catch
Legitimate close-third inference from observable behavior — inferring
emotion from action is not head-hopping.

## Engine Hook
If `command -v scriptorium` succeeds, run
`scriptorium prose prepare pov-consistency <chapter>`, judge per the
embedded instructions, then `submit-findings`. Otherwise apply the same
judgment directly while reading.
