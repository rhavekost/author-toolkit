# Crutch-Words Audit Reference

Author-specific: reads a `crutch-words.txt` file (one term per line, `#`
comments allowed) from the novel repo's root and flags every occurrence.

## What This Catches
Words *you personally* overuse across projects — seed the list from the
`frequency` audit's recurring offenders, or from prior manuscripts' known
tics.

## What This Does NOT Catch
Anything not on your list. This audit has no universal opinion about which
words are crutches — that's the point.

## Engine Hook
If `command -v scriptorium` succeeds, run
`scriptorium prose audit crutch-words <chapter>` (reads `crutch-words.txt`
from the current directory). Otherwise ask the author for their list and
scan manually. Missing config file → zero findings, not an error.
