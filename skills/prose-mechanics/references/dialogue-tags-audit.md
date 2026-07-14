# Dialogue-Tags Audit Reference

Flags said-bookisms (exclaimed, declared, proclaimed, ...) and
adverb-modified tags ("said sharply"). A hybrid audit: code finds
candidates; the session judges density and appropriateness.

## What This Catches
Tags that call attention to themselves instead of disappearing behind the
dialogue, and adverbs doing a stronger verb's job.

## What This Does NOT Catch
Overall tag density issues (too many/too few tags across a scene) — that
needs full-chapter judgment, not line-by-line pattern matching.

## Judgment Protocol
Run `scriptorium prose prepare dialogue-tags <chapter>` to get code
candidates, judge each (keep/reject) plus scan density across the whole
chapter, then `scriptorium prose submit-findings`. Without the engine,
scan manually for both patterns and eyeball tag density.
