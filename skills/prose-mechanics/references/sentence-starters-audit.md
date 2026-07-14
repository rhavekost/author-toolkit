# Sentence-Starters Audit Reference

Flags runs of 3+ consecutive sentences opening with the same construction
type: pronoun, article, coordinating conjunction, or `-ing` participial.

## What This Catches
"She ran. She jumped. She laughed." — three pronoun-led openers in a row
produce a monotonous rhythm.

## What This Does NOT Catch
Runs classified as "other" (proper nouns, adverbs, prepositional phrases,
etc.) — the classifier only tracks the four listed patterns; broader
opener variety is a judgment call left to the author.

## Engine Hook
If `command -v scriptorium` succeeds, run
`scriptorium prose audit sentence-starters <chapter>`. Otherwise scan
paragraph openers by eye for repeated patterns.
