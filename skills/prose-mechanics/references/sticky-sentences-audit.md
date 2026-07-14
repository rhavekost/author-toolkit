# Sticky-Sentences Audit Reference

Flags sentences (8+ words) where 45%+ of words are "glue words" — common
function words (of, to, that, was, in, the, ...) that carry no imagery or
information.

## What This Catches
Sentences that are grammatically correct but feel dense/hard to parse
because content words are diluted by connective tissue.

## What This Does NOT Catch
- Short sentences (under 8 words) — glue-word ratio is noisy at that
  length.
- Sentences spanning a line break — this audit operates per-line;
  multi-line sentences may be split or missed. A future pass could
  reassemble paragraphs before sentence-splitting.

## Engine Hook
If `command -v scriptorium` succeeds, run
`scriptorium prose audit sticky-sentences <chapter>`. Otherwise estimate
glue-word density by eye on long sentences.
