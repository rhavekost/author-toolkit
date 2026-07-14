# Echoes Audit Reference

Flags a word (4+ letters, not a common function word) that repeats within
a 100-word window — the classic "echo" that snags a reader's attention
without adding meaning.

## What This Catches
- Distinctive nouns/verbs/adjectives repeated close together, e.g. "stone"
  twice within a paragraph.

## What This Does NOT Catch
- Deliberate repetition for rhythm or emphasis (anaphora, refrains) — the
  audit flags candidates; the author judges intent.
- Common function words (the/and/that/...) — excluded by design.
- Repeats more than 100 words apart — those rarely read as echoes.

## Engine Hook
If `command -v scriptorium` succeeds, run
`scriptorium prose audit echoes <chapter>` and treat its JSON as
authoritative. Otherwise scan manually for the pattern above.

## Worked Example
**Before:** "The stone wall stood strong. A cold wind crossed the stone yard."
**Flag:** second "stone" (9 words after the first) — consider "granite yard"
or restructuring to avoid the repeat.
