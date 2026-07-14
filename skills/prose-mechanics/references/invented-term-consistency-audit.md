# Invented-Term Consistency Audit Reference

Reads canonical invented terms from `invented-terms.txt` (one per line,
exact casing/hyphenation as it should appear — e.g. `the Ledger`) and
flags every occurrence whose casing doesn't match exactly.

## What This Catches
"the Ledger" vs "the ledger" vs "The ledger" — capitalization, spelling,
or hyphenation drift on names the author invented for this world.

## What This Does NOT Catch
Terms not in the config file. If working inside a novel repo that has a
structural story bible, `invented-terms.txt` can be seeded from the
bible's character/place/object names — see the engine hook below.

## Engine Hook
If `command -v scriptorium` succeeds, run
`scriptorium prose audit invented-term-consistency <chapter>`. If a
structural bible exists, `scriptorium prose seed-terms` can generate a
starting `invented-terms.txt` from it (see Task 21). Otherwise ask the
author for their canon list and scan manually.
