# Clichés Audit Reference

List-based detection of well-worn phrases (curated list in
`scriptorium/prose/audits/cliches.py`, mirrored here for the no-engine
path), judged in-session for whether the usage is genuinely tired or
deliberately, ironically, or idiomatically fine.

## What This Catches
Exact-match stock phrases: "at the end of the day," "her blood ran cold,"
"little did she know," and similar.

## What This Does NOT Catch
Clichéd IDEAS expressed in fresh language (a stock plot beat described
without stock phrasing) — this audit is lexical, not structural.
Redundancies not on the list ("reversed back") are left to session
judgment.

## Judgment Protocol
Run `scriptorium prose prepare cliches <chapter>`, judge each candidate,
then `submit-findings`. Without the engine, scan for the listed phrases
plus any other tired constructions by eye.
