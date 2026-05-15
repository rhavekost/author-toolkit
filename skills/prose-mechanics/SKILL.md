---
name: prose-mechanics
description: "Use when auditing prose at the sentence level on stabilized drafts. Trigger on: 'audit prose', 'active voice', 'sentence variance', 'passive voice pass', 'parallel structure check', 'readability audit', 'prose mechanics', or sentence-level diagnostic work on fiction or nonfiction."
---

# Prose Mechanics

Diagnostic audits for sentence-level prose quality on near-final drafts. Each audit is a focused pass that produces a flagged-issues report; the author reviews and applies fixes before moving to the next audit. Works for fiction or nonfiction.

## Session Continuity

Audit work is iterative across multiple sessions. Claude has no memory between them, so the audit tracker is your persistent state.

- **At session start:** Read `audit-tracker.md` in the project directory (copy from `assets/audit-tracker-template.md` if it doesn't exist). Check which audits have run on which chapters and what's still outstanding.
- **At session end:** Update the tracker with what was audited, what was flagged, and what was resolved. Note the stopping point.
- **Surface unresolved questions:** If prior audits flagged issues the author hasn't addressed, list them at session start so the user can decide what to take on.

## Core Concept

Audits are diagnostics, not edits. Each pass scans for one specific class of failure, produces a list of flagged passages, and stops. The author—not the audit—decides whether each flag is a real problem and how to fix it.

## When to Use

This skill is for:
- ✅ Sentence-level audits on finished or near-finished drafts (fiction or nonfiction)
- ✅ Final polish before submission, query, or publication
- ✅ Catching the mechanical failures that survive developmental editing
- ✅ Complementing `fiction-workshop` or `narrative-nonfiction` work after structural editing is done

## When NOT to Use

This skill is NOT for:
- ❌ Early drafting—audits are for revision, not generation
- ❌ Developmental editing tasks—use `fiction-workshop` or `narrative-nonfiction` instead
- ❌ Manuscripts that haven't stabilized structurally yet (you'll audit prose that's about to be cut)
- ❌ Single scenes or short passages where eyeballing is faster than running a pass
- ❌ Heavy stylistic departures (e.g., experimental prose) where the audits' assumptions don't hold

## Audit Passes

Run audits **one at a time, in order**. Order matters because earlier audits change what later audits flag—an active-voice rewrite reshuffles sentence lengths, and a parallel-structure fix can ripple into the variance pass.

| # | Audit | Invocation | Catches |
|---|-------|------------|---------|
| 1 | **Active/Passive** | "Run active/passive audit on..." | Unjustified passive constructions, hidden agents |
| 2 | **Parallel Structure** | "Run parallel-structure audit on..." | Broken grammatical parallels in lists, comparisons, series |
| 3 | **Sentence Length Variance** | "Run sentence-variance audit on..." | Five-plus consecutive sentences in a narrow length band; flat rhythm |
| 4 | **Accessibility** | "Run accessibility audit on..." | Reading-grade spikes, paragraph bloat, structural impenetrability |

Load only the reference file matching the currently invoked audit. Do not preload all references at session start—it wastes context budget. If switching audits mid-session, load the new reference file and treat the prior one as out-of-scope.

See `references/` for detailed guidance on each audit.

## Workflow

For each audit:

1. **Scope:** Confirm which chapter(s) or passage(s) to audit. Audit one chapter at a time unless the user asks for broader scope.

2. **Run the pass:** Read the prose looking for the specific patterns named in the relevant reference file. Do **not** look for other classes of issue—keep the lens narrow.

3. **Produce a flagged-issues report:** For each flagged passage, output:
   - File and approximate location
   - The flagged text (short excerpt)
   - Why it was flagged (which detection pattern matched)
   - A suggested fix or two—not a mandate, just options

4. **Stop. Wait for author review.** Do not apply fixes automatically. The author decides which flags are real and which are stylistic choices.

5. **Apply approved fixes:** Use `str_replace` for surgical edits on the flags the author confirms. Skip the rest without comment.

6. **Update the tracker:** Note which audit ran, on which chapter, what was flagged, and what was resolved.

7. **Move to the next audit.** Repeat.

## Common Mistakes

| Mistake | Why It Happens | Fix |
|---------|---------------|-----|
| **Running all audits simultaneously** | Wanting to be thorough in one pass | Each audit has a different lens. Stacked, they produce a noise-flood the author can't act on. One pass at a time. |
| **Applying fixes mechanically** | Treating flags as instructions, not diagnostics | Every flag needs a judgment call. A flagged passive may be the right passive. Surface the flag; let the author choose. |
| **Treating audits as line edits** | Conflating diagnostics with revision | Audits identify candidate issues; line editing is the craft of resolving them. Run the audit, then do the line edit—not both at once. |
| **Auditing unstable drafts** | "Polish as I go" instinct | If chapters are still being cut or reordered, audited prose is wasted work. Wait for structural stability. |
| **Skipping the report step** | Wanting to be efficient by fixing in place | The report is the deliverable. It teaches the author to see the pattern themselves, which is the long-term value of the audit. |
| **Running audits out of order** | Convenience or user request | Each audit changes what the next will flag. If the user insists on a different order, note that downstream audits may need a re-run. |
| **Auditing during developmental work** | Mistaking line-mechanical issues for structural ones | Prose mechanics are downstream of structure. If the chapter's purpose isn't clear, the prose isn't the problem. Use the developmental skills first. |

## Self-Check: Is This Working?

Use these checkpoints to verify you're running audits correctly.

**Before starting an audit:**
- [ ] Is the manuscript structurally stable (no pending major cuts or reorders)?
- [ ] Have prior developmental and character-work passes been completed?
- [ ] Is the audit scope clearly defined (which chapter, which passages)?

**During an audit:**
- [ ] Are you using only the patterns from the relevant reference file?
- [ ] Are you producing a flagged-issues report rather than applying fixes directly?
- [ ] Are you ignoring issues outside the audit's scope, even when you notice them?

**After producing the report:**
- [ ] Can the author act on each flag without re-reading the audit reference?
- [ ] Did you include a short excerpt and a suggested fix for each flag?
- [ ] Did you stop and wait for review rather than continuing to the next audit?

**After applying fixes:**
- [ ] Did you use `str_replace` for surgical changes only?
- [ ] Did you skip the flags the author didn't confirm, without re-raising them?
- [ ] Did you update the tracker before ending the session?

**Before moving to the next audit:**
- [ ] Is the current audit's flags fully resolved (applied, dismissed, or deferred with a note)?
- [ ] Have you confirmed the author wants to proceed?

If you answered "no" to any checkpoint, stop and resolve it before continuing.

## Quick Reference Commands

| Need | Command |
|------|---------|
| Start audit sequence | "Run the prose-mechanics audits on [chapter]" |
| Active/passive only | "Run active/passive audit on [chapter]" |
| Parallel structure only | "Run parallel-structure audit on [chapter]" |
| Sentence variance only | "Run sentence-variance audit on [chapter]" |
| Accessibility only | "Run accessibility audit on [chapter]" |
| Check audit status | "What audits have run on [chapter]?" |

---

## Files

- `references/active-passive-audit.md` - Voice and agency at the sentence level
- `references/parallel-structure-audit.md` - Grammatical parallelism in lists, comparisons, series
- `references/sentence-length-variance.md` - Rhythm diagnostics for paragraphs
- `references/accessibility-audit.md` - Readability scoring and structural accessibility
- `assets/audit-tracker-template.md` - Per-project tracker for audit runs and findings
