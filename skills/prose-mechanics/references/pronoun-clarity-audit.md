# Pronoun-Clarity Audit Reference

Pure session judgment — no reliable deterministic signal for antecedent
ambiguity.

## What This Catches
Pronouns whose referent a careful first-time reader would have to guess or
backtrack to resolve — most common with two same-gender characters in one
scene, or "it"/"this"/"that" referring to an idea rather than a concrete
noun.

## What This Does NOT Catch
Technically-ambiguous pronouns that are clear from context or proximity —
flagging every technical ambiguity would bury real problems in noise.

## Engine Hook
If `command -v scriptorium` succeeds, run
`scriptorium prose prepare pronoun-clarity <chapter>`, judge per the
instructions embedded in the prepared payload, then `submit-findings`.
Otherwise apply the same judgment directly while reading.
