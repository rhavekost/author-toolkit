# Filter-Words Audit Reference

Flags filter verbs (felt/saw/heard/realized/noticed/watched/knew/
wondered, all forms) that place the POV character's perception between
the reader and the action.

## What This Catches
"She felt the cold seep in" — the filter verb "felt" is unnecessary
scaffolding; "The cold seeped in" delivers the same information with more
immediacy in deep POV.

## What This Does NOT Catch
- Legitimate uses where the ACT of perceiving is the point (a character
  consciously deciding to notice something, an unreliable narrator's
  perception being foregrounded on purpose).
- Omniscient or distant-POV narration, where filter verbs are often
  correct, not a flaw.

## Engine Hook
If `command -v scriptorium` succeeds, run
`scriptorium prose audit filter-words <chapter>`. Otherwise scan for the
listed verb forms manually.
