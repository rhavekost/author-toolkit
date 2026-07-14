# Adverb Audit Reference

Flags `-ly` adverbs, labeling each as occurring in dialogue or narration —
these are different problems with different remediation.

## What This Catches
Any `-ly` word not on the excluded non-adverb list (family, only, early,
ugly, and similar false positives).

## What This Does NOT Catch
Adverbs that ARE the right word ("she smiled sadly" may be exactly
correct). In dialogue, adverbs in tags are usually the bigger issue
(see `dialogue-tags-audit.md`); in narration, they're usually a sign a
stronger verb exists.

## Engine Hook
If `command -v scriptorium` succeeds, run
`scriptorium prose audit adverb-audit <chapter>`. Otherwise scan for `-ly`
words manually, noting dialogue vs. narration context.
