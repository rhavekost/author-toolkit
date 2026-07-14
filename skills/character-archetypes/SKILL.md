---
name: character-archetypes
description: "Use when identifying, auditing, or tracking character archetypes in fiction. Trigger on: 'character archetype', 'archetype audit', 'what archetype is this character', 'archetype conformance', 'Hero's Journey character role', 'Jungian archetype', or archetype-based character analysis."
---

# Character Archetypes

Diagnostic vocabulary for character archetypes — narrative-role functions (Hero, Mentor, Trickster, and the rest of Vogler/Campbell's eight) and Jungian personality types (Sage, Rebel, Caregiver, and the rest of the Mark & Pearson twelve) — plus four modes for using them across a manuscript: naming a pairing, auditing for cliché, checking for drift, and balancing a cast.

Archetype is a **starting scaffold, not a finished character**. This skill complements `fiction-workshop`'s Want/Need/Wound/Lie framework (see `references/character-work.md` there) rather than replacing it — the archetype names the pattern; the Core Four individualizes it.

## When to Use

This skill is for:
- ✅ Fiction manuscripts — novels, novellas, short stories, screenplays-in-prose-form
- ✅ Naming a character's narrative-role and personality-type pairing
- ✅ Checking whether an established archetype is being used well or as cliché
- ✅ Checking whether a character's actions still match their established archetype, or have drifted without explanation
- ✅ Checking whether a cast's archetypes are balanced (no redundancy, no structural gaps)

## When NOT to Use

This skill is NOT for:
- ❌ Narrative nonfiction (memoir, self-help) — author-voice and reader-persona archetypes are a different, unaddressed problem. Use `narrative-nonfiction` instead.
- ❌ Enneagram or other personality typologies — this skill covers exactly two canonical frameworks (Vogler narrative-role, Jungian twelve). Adding more blurs into general personality-typing rather than archetype work.
- ❌ Plot- or genre-level archetypes (monomyth stages, genre tropes) — this skill is character-scoped only. For plot-level structure, use `fiction-workshop`'s `references/developmental-editing.md`.
- ❌ Building a character from scratch with no story context — Analyzer's "recommend" direction needs at least a stated story role to work from.

## Session Continuity

Archetype pairings are meant to persist in the project's Story Bible, not be re-derived each session.

- **At session start:** If a Story Bible exists, check each main character's entry for an existing Archetype Profile block (see `assets/archetype-profile-template.md`). Don't re-run Analyzer on a character who already has one unless the author asks for a re-check.
- **When a pairing is newly named or changed:** Hand the profile block back to the author to paste into the Story Bible yourself — this skill does not write to the Story Bible directly (see each mode's stop condition below).

## The Two Taxonomies

A character gets tagged with **one archetype from each list** — they describe different things (plot function vs. psychology) and normally combine (e.g., narrative-role Mentor + personality Sage).

| Taxonomy | Reference file | Covers |
|---|---|---|
| **Narrative-Role** | `references/narrative-role-archetypes.md` | Vogler/Campbell's 8 character functions: Hero, Mentor, Threshold Guardian, Herald, Shapeshifter, Shadow, Trickster, Ally |
| **Personality** | `references/personality-archetypes.md` | Jungian 12 (Mark & Pearson model): Innocent, Everyman, Hero, Caregiver, Explorer, Rebel, Lover, Creator, Jester, Sage, Magician, Ruler |

Both files state explicitly that the archetype is a starting scaffold, not a finished character — individualizing detail (voice, wound, specific flaw, from `fiction-workshop`'s Want/Need/Wound/Lie) is what keeps an archetype from reading as a stock type.

## The Four Analysis Modes

| Mode | Invocation | Question | Reference file |
|---|---|---|---|
| **Analyzer** | "What archetype is this character?" | Diagnose or recommend a pairing | `references/archetype-analyzer.md` |
| **Audit** | "Audit this scene for archetype cliché" | Is the archetype used well, or as cliché? | `references/archetype-audit.md` |
| **Conformance** | "Check archetype conformance for chapters X-Y" | Is this character still who we said they were? | `references/archetype-conformance.md` |
| **Ensemble** | "Run an ensemble balance check on the cast" | Is the cast balanced? | `references/archetype-ensemble.md` |

**Ordering guidance:** Analyzer → (optional) Audit → Conformance → Ensemble. Skip straight to Audit or Conformance if the archetype is already decided. Ensemble is a late-stage check — run it once most main characters already have an assigned archetype, not as a starting point.

Load only the reference file matching the currently invoked mode. Do not preload all references at session start — it wastes context budget. If switching modes mid-session, load the new reference file and treat the prior one as out-of-scope.

## Workflow

1. **Identify the mode** the author is invoking (see table above). If unclear, ask.
2. **Load only that mode's reference file** (and the taxonomy file(s) it needs — Analyzer and Audit need both taxonomies; Conformance and Ensemble need whichever taxonomy the character's existing profile already names).
3. **Run the mode's workflow** exactly as documented in its reference file.
4. **Stop at the mode's documented stop condition** (see Stopping Points below). Hand results back to the author.
5. **If a new or changed Archetype Profile results**, offer the `assets/archetype-profile-template.md` block for the author to paste into their Story Bible — do not write it there yourself.

## Integration with `fiction-workshop`

- `fiction-workshop/references/character-work.md` links here as a complementary lens alongside Want/Need/Wound/Lie.
- `assets/archetype-profile-template.md` is designed to paste directly into the Story Bible character entry format shown in `fiction-workshop/SKILL.md`, immediately after the Voice Notes field.
- This skill never restructures `fiction-workshop/assets/story-bible-template.md` — it only adds an optional block to individual character entries.

## Stopping Points

Each mode has a defined end. Stop at it. Do not auto-advance to the next mode, do not silently expand scope, do not write to the Story Bible without being asked.

| Mode | Stops when... | Then |
|---|---|---|
| **Analyzer** | Pairing (or recommendation) named with rationale | Hand back for author confirmation. Do not auto-write to Story Bible. |
| **Audit** | Flagged cliché list delivered | Stop. No auto-rewrite — author decides which flags to act on. |
| **Conformance** | Drift flags delivered for the requested range | Stop. Author decides what's real drift vs. legitimate arc progression. |
| **Ensemble** | Cast balance report delivered | Stop. Author decides on any cast changes — do not auto-invent new characters. |

## Finding Format

Audit, Conformance, and Ensemble mode output (diagnostic — cliché flags,
drift flags, cast-balance gaps) conforms to
`../../references/finding-schema.json`: `audit` = the mode
name ("archetype-audit", "archetype-conformance", "archetype-ensemble"),
`technique` = the specific archetype pattern involved (e.g. "Mentor
archetype cliché" or "Trickster/Shadow cast overlap"), `severity`,
`location`, `issue`, `confidence: "judgment"`, `exemplar` optional (inline
one-liner; no curated library yet). Analyzer mode (pairing/recommendation,
not a flag) is NOT in scope for this contract.

## Common Mistakes

| Mistake | Fix |
|---|---|
| Treating archetype as a rigid mold | Archetype is scaffold, not finished character — individualizing detail is mandatory |
| Confusing narrative-role with personality-type | They're independent axes; a Hero (role) can be a Sage (personality) |
| Running Audit before an archetype is established | Audit needs a target to judge cliché against — run Analyzer first, or use stated author intent |
| Flagging arc growth as Conformance drift | Legitimate arc progression isn't drift — only *unexplained* inconsistency is |
| Running Ensemble before the main cast has archetypes assigned | Ensemble is a late-stage check, not a starting point |

## Quick Reference Commands

| Need | Command |
|---|---|
| Name a pairing | "What archetype is this character?" |
| Get a recommendation for a new character | "What archetype should a [stated role] character be?" |
| Check for cliché | "Audit [character] in [scene] for archetype cliché" |
| Check for drift | "Check archetype conformance for [character] across chapters [X-Y]" |
| Check cast balance | "Run an ensemble balance check on the cast" |

---

## Files

- `references/narrative-role-archetypes.md` - Vogler/Campbell's 8 character functions
- `references/personality-archetypes.md` - Jungian 12 (Mark & Pearson model)
- `references/archetype-analyzer.md` - Diagnose or recommend an archetype pairing
- `references/archetype-audit.md` - Flag stock/cliché archetype use
- `references/archetype-conformance.md` - Check for unexplained archetype drift
- `references/archetype-ensemble.md` - Check cast-level archetype balance
- `assets/archetype-profile-template.md` - Story Bible block for an archetype pairing
