# Frequency Audit Reference

Counts distinctive-word (4+ letters, non-stopword) usage per chapter and
flags any word appearing 6+ times.

## What This Catches
Overused nouns/verbs/adjectives — words the author reaches for
unconsciously across a chapter.

## What This Does NOT Catch
- Manuscript-wide (multi-chapter) aggregation — v2 is per-chapter only; a
  later `prose report` mode may roll multiple chapters' JSON together.
- Words that are correctly repeated because they're the chapter's subject
  (a chapter about "the ledger" will legitimately say "ledger" often) —
  the audit flags candidates; the author judges relevance.

## Engine Hook
If `command -v scriptorium` succeeds, run
`scriptorium prose audit frequency <chapter>`. Otherwise count manually.
