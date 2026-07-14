# Active/Passive Audit Reference

A diagnostic pass for unjustified passive constructions and hidden agency in prose.

## What This Audit Catches

- **Unjustified passive voice:** constructions where the actor is known and significant but absent from the subject position.
- **Hidden agency:** "mistakes were made," "it was decided"—prose that obscures who did what.
- **Nominalized verbs:** action smuggled into noun form ("made a decision" for "decided"), which often co-occurs with passive framing.
- **Stative weakness:** chains of "to be" verbs that drain motion from the prose, especially in narrative passages.

## What This Audit Does NOT Catch

- **Justified passive voice.** Passive is a legitimate tool. This audit flags candidates; it does not condemn them.
- **Voice consistency across characters or chapters.** That's a line-editing or character-work concern.
- **Tense errors or subject-verb agreement.** Out of scope.
- **Whether the active rewrite is *good* prose.** The audit identifies; the author rewrites.

## Why It Matters

Active voice is not inherently superior to passive—but unjustified passive voice has predictable costs:

1. **Loss of agency:** Readers attach to actors. "She slammed the door" engages; "the door was slammed" recedes.
2. **Diffused responsibility:** In nonfiction, passive often hides who is accountable. In fiction, it can mute character.
3. **Word count inflation:** Passive is structurally longer.
4. **Energy drain:** Passive constructions stack into a tone of distance and abstraction, even when the writer wanted intimacy.

The reverse cost applies to **forced active voice**: turning every sentence active produces a relentless, hammering rhythm and can foreground actors who should be backgrounded.

## Detection Patterns

A passage is flagged if it contains:

1. **"To be" + past participle** with a known actor: "the report was filed by Marcus" → flag, because the actor is named and significant.
2. **Agentless passive with an identifiable agent:** "the door was locked" when the prose has just established Marcus walking out. Flag if the actor is recoverable from context and the obscuring isn't intentional.
3. **"It was [verb]ed that..." constructions:** almost always a flag in non-academic prose.
4. **Three or more "to be" main verbs in five consecutive sentences:** stative chain, flag the run.
5. **Nominalizations:** "made a decision," "reached an agreement," "conducted an analysis." Flag for review—often (not always) the verb form is stronger.
6. **"There was/were" sentence openings followed by a noun that could be the actor:** "There was a man waiting in the hallway" → consider "A man waited in the hallway."

## Remediation Patterns

For each flag:

- **Restore the actor:** "The report was filed by Marcus" → "Marcus filed the report."
- **Recover the verb from the noun:** "Marcus made a decision to leave" → "Marcus decided to leave."
- **Replace "to be" with a motion verb:** "She was at the door" → "She stood at the door" (when "stood" carries meaning).
- **Leave it.** Sometimes the passive is right: when the patient is more important than the actor ("the manuscript was rejected"), when the actor is unknown ("the window had been forced open"), when style demands ("the prophecy must be fulfilled").

## Failure Modes

**Over-application** — turning every passive into active produces:
- Forensic, choppy prose with no rest beats
- Foregrounded actors in passages where focus should sit on the patient
- Loss of stylistic range in literary or formal registers

**Under-application** — leaving the audit's flags unaddressed produces:
- Diffused agency in scenes that need impact
- Bureaucratic tone in narrative
- Word count creep

The audit's job is to surface candidates. The author's job is to weigh each one.

## Worked Examples

### Example 1: Hidden Agent in a Thriller Scene

**Before:**

> The safehouse had been compromised. Documents were scattered on the floor, and the laptop had been taken. Alex's contact would have to be informed.

Flags: three passive constructions in three sentences, all with recoverable actors.

**After:**

> Someone had compromised the safehouse. Documents littered the floor; the laptop was gone. Alex would have to call her contact.

Notes: "the laptop was gone" survives because the actor isn't the point—the absence is. The other two passives became active.

### Example 2: Nominalization in a Self-Help Chapter

**Before:**

> The creation of a morning routine is the foundation upon which lasting habits are built. The implementation of small daily actions leads to the development of automatic behaviors.

Flags: "creation," "implementation," "development" are all verbs hiding in nouns. Two passives stack on top.

**After:**

> A morning routine is where lasting habits start. Implement small daily actions and the behaviors become automatic.

Notes: nominalizations unpacked, passive removed, sentence length cut by a third without losing meaning.

### Example 3: Justified Passive (Do Not Flag)

> The manuscript was rejected on the same Tuesday her father died.

The actor (the publisher, the editor) is irrelevant. The patient—the manuscript, the protagonist—is the subject of the scene's emotional weight. **This passive is correct.** A version that surfaces the agent ("Some editor at Knopf rejected the manuscript on the same Tuesday her father died") trades the right focus for grammatical "correctness."

## Engine Hook

If `command -v scriptorium` succeeds, run
`scriptorium prose prepare active-passive <chapter>` to get code-detected
candidates, judge each per the Detection/Remediation Patterns above, then
submit via `scriptorium prose submit-findings`. Otherwise apply the
detection patterns directly against the chapter text.
