# Sentence Length Variance Audit Reference

A diagnostic pass for rhythm flatness at the paragraph level.

## What This Audit Catches

- **Runs of five or more consecutive sentences within a narrow word-count band.** This is the primary trigger for revision.
- **Paragraphs whose sentence-length standard deviation is below the target range for the prose register.**
- **Whole chapters built on a single dominant sentence length.**
- **Mechanical alternation patterns** (short-long-short-long-short-long) that produce a different kind of monotony.

## What This Audit Does NOT Catch

- **Whether the sentences are well-written.** A paragraph with perfect variance can still be bad prose.
- **Whether long sentences are well-constructed.** Variance is a precondition for rhythm, not a guarantee of it.
- **Dialogue rhythm.** Spoken lines follow different patterns; this audit is for narrative and exposition.
- **Cross-paragraph rhythm.** Audit operates on paragraph scope.

## Why It Matters

Sentence-length variance is one of the strongest single predictors of prose that "feels good." Readers don't consciously track it, but the absence of variance produces a flat, hypnotic, drone-like quality that the reader experiences as boredom—often without being able to say why.

Two specific failure modes are worth naming:

- **Uniform short sentences** read as breathless or amateurish (the "Hemingway-imitator" failure: short rhythm without Hemingway's compression).
- **Uniform long sentences** read as dense, academic, or smothering, regardless of whether the content is interesting.

The fix is not "write more long sentences" or "write more short sentences" but **introduce variance**.

## Calculating Variance

For a working diagnostic, compute the **standard deviation of sentence lengths in each paragraph**, measured in words.

**Procedure:**
1. Tokenize the paragraph into sentences (split on `. ! ?`, accounting for quoted dialogue).
2. Count words per sentence.
3. Compute the mean and standard deviation.

**Heuristic targets by register:**

| Register | Mean sentence length | Target std dev |
|----------|---------------------|----------------|
| Literary fiction | 12–18 words | ≥ 7 |
| Commercial fiction | 10–15 words | ≥ 6 |
| Thriller / action | 8–14 words | ≥ 5 (lower bound is fine; rhythm comes from extremes) |
| Self-help / prescriptive | 12–18 words | ≥ 6 |
| Long-form narrative nonfiction | 14–22 words | ≥ 8 |
| Academic / journal | 18–28 words | ≥ 6 |

These are starting points, not laws. A paragraph below the target is a candidate for a flag, not an automatic failure.

## Detection Patterns

A paragraph is flagged if it contains:

1. **Five or more consecutive sentences within a narrow length band.** "Narrow" = where the longest sentence is at most 3 words longer than the shortest sentence in the run. This is the most reliable trigger; even a single such run is worth surfacing.
2. **Paragraph-level standard deviation below the register's target.**
3. **Three consecutive paragraphs where every paragraph's mean sentence length is within ±2 words of the others.** Chapter-scale flatness.
4. **Mechanical alternation:** strict short/long/short/long for six or more sentences. This is a different failure mode but produces similar reader fatigue.
5. **A chapter whose overall std dev is below the register target for ≥ 70% of its paragraphs.** Pattern-level flag worth raising even if no single paragraph is egregious.

## Remediation Patterns

For a flagged run:

- **Compress one sentence to a fragment.** "It hit her." "He knew." "Too late." A four-word sentence in a run of fifteen-word sentences resets the reader's ear.
- **Combine two adjacent sentences with a semicolon or em dash.** Creates a longer beat without adding content.
- **Split one sentence into two when the natural pause is mid-sentence.** Often the comma that's been carrying the weight should be a period.
- **Add a single very long sentence** that earns its length—an inventory, a chain of clauses, a long-breath description. One long sentence in a paragraph of medium ones reshapes the whole rhythm.

A useful target: in any flagged paragraph, the **shortest sentence should be at most 30% of the longest's word count**.

## Failure Modes

**Over-application** produces:
- Frantic, manic prose that swings constantly
- Loss of the steady, gathering rhythm that some passages need (long contemplative scenes, formal exposition)
- A "trying too hard" quality

**Under-application** produces:
- The drone effect described above
- Reader fatigue independent of content quality
- Prose that "tests well" sentence-by-sentence but reads dead in paragraphs

A useful sanity check: read the flagged paragraph aloud. If you find yourself breathing at the same point in every sentence, the variance is too low. If you can't catch your breath at all, it's too high.

## Worked Examples

### Example 1: Flat Short-Sentence Run in a Thriller

**Before** (mean 7.0, std dev 1.3, five sentences in a tight band):

> Alex checked the dead drop. The package was gone. She felt her pulse rise. The contact was burned. She had to move fast.

Flag: five consecutive sentences between 5 and 9 words. Std dev far below target. Rhythm is hammering without payoff.

**After** (mean 7.2, std dev 5.1):

> Alex checked the dead drop. Empty. The contact was burned, and her pulse spiked the way it always did when an operation pivoted. Move.

Notes: a one-word sentence ("Empty"), a long sentence with clause stacking, a one-word imperative. Same content, three different sentence lengths, rhythm restored.

### Example 2: Flat Long-Sentence Run in a Self-Help Chapter

**Before** (mean 22.4, std dev 2.1):

> Most readers come to a productivity book hoping that the act of reading will be sufficient to produce change. They open the first chapter ready to underline, eager to highlight, certain that this time will be different from the last. They settle into the reading with a comforting sense that something useful is being absorbed even when the page count does not yet reflect any progress.

Flag: three sentences between 20 and 25 words. Std dev too low for the register's target. Reader sinks into a drone.

**After** (mean 17.0, std dev 11.8):

> Most readers come to a productivity book hoping that reading will be enough. Underline. Highlight. Settle in with the comforting sense that something useful is being absorbed, even when the page count does not yet reflect any progress.

Notes: two one-word fragments break the drone. The final sentence keeps the long-breath rhythm but now lands with more weight because it's earned by contrast.

### Example 3: Run Without a Flag (Do Not Surface)

> She walked into the room. He looked up. Their eyes met. The silence held. Then she spoke.

Five short sentences, narrow band—but in a high-tension dialogue beat, this rhythm is doing work. Mechanical detection would flag it; judgment leaves it alone. Note the flag for the author and explain why it might be intentional.

## Engine Hook

If `command -v scriptorium` succeeds, run
`scriptorium prose audit sentence-variance <chapter>`. The engine implements
detection pattern #1 only (narrow-band runs, ±3 words) as a fast deterministic
pass; patterns #2-5 above (std-dev targets, chapter-scale flatness, mechanical
alternation) are for conversational/manual application when working without
the engine, or as additional judgment on top of the engine's findings.
Otherwise apply the detection patterns above by eye.
