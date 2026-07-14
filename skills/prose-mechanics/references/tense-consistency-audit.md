# Tense-Consistency Audit Reference

Classifies narration sentences (dialogue lines excluded) as past- or
present-dominant via a curated irregular-verb list plus regular `-ed`
detection, flags sentences that don't match the chapter's dominant tense.

## What This Catches
Unintentional slips into the wrong tense mid-narration.

## What This Does NOT Catch
Intentional shifts (flashbacks, present-tense framing devices) — the
heuristic has no concept of narrative intent; that's the session's job in
the judgment step. Ambiguous sentences (no clear tense signal) are never
classified, so never flagged.

## Judgment Protocol
Run `scriptorium prose prepare tense-consistency <chapter>`, judge each
candidate against narrative intent, then `submit-findings`. Without the
engine, read for tense drift by eye, remembering dialogue is exempt.
