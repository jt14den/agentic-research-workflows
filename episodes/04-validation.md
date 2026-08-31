---
title: "Validation Strategies: The Approval Gate"
teaching: 35
exercises: 65
---

:::::::::::::::::::::::::::::::::::::::::::::::::::: questions

- What evidence makes AI-generated code safe to approve?
- What can rewrite time tell me about my workflow, and what can it not?
- How can I use one AI to catch the errors of another without treating it as an authority?

::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::: objectives

- Given an AI-generated script, state the evidence supporting it, name the missing evidence, and decide to approve, revise, or reject.
- Describe the four-layer validation stack (immutable requirements, automated checks, metamorphic tests, domain plausibility).
- Turn validation into checks you can run, by finishing `validate_data.py`.
- Use a multi-model critique, in a fresh session, to widen review without treating it as an authority.

::::::::::::::::::::::::::::::::::::::::::::::::::

## The approval gate: verification over generation

In an agentic research workflow, you read, question, and approve code as much as you write it. The standard has shifted from vibe coding to a disciplined, validated workflow.

The approval gate is the point where you decide AI-generated code is robust enough for research production. It separates a working prototype from validated science.

:::::::::::::::::::::::::::::::::::::::::::::::::::::: callout

## The review-first standard
The bottleneck in research is no longer writing code; it is verifying it. A high-performance workflow follows this cycle:
Plan → Agent Implementation → Automated AI-Powered Testing → Human Review.

::::::::::::::::::::::::::::::::::::::::::::::::::::::

## Rewrite time: a signal, not a score

Rewrite time is the manual effort, in minutes, you spend making AI-generated output ready to trust. It is useful, but be careful what you claim from it.

Rewrite time does **not** prove AI makes researchers faster in general. Measuring programmer productivity is genuinely hard, and a single timing on a single task tells you almost nothing about productivity overall. This caution isn't hypothetical: a 2026 survey of 868 scientists who program found that *feeling* more productive with a genAI tool was associated with less programming experience and less use of practices like testing and code review, not with better outcomes. The single strongest predictor of feeling productive was simply how many lines of generated code someone accepted at once ([O'Brien et al., 2026][obrien-2026]) — the authors' own conclusion is that scientists may be "gauging productivity by code generation rather than validation." That gap between feeling productive and being correct is exactly what this validation stack exists to close. Treat rewrite time as a **formative signal** about *this* workflow, on *this* task:

- It is local and contextual.
- High rewrite time usually means the task was underspecified, the model overreached, or you did not yet have the mental model to evaluate the output.
- It helps you decide what to improve next: the prompt, the spec, or the validation step.

::::::::::::::::::::::::::::::::::::::::: caution

## Don't turn rewrite time into a productivity claim

A low rewrite time on one script is not evidence that AI saved you time overall. It does not count the time spent prompting, reviewing, debugging, or validating, and it says nothing about whether the result is scientifically correct. Use it to tune your workflow, not to justify it.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::: discussion

## Think aloud while you work

Work in pairs. One person uses the AI for five minutes on a small, constrained task (for example, adding a single validation check to the cleaning script). Say out loud what you are doing as you do it: what you expect, what you trust, where you hesitate.

The observer takes notes: Where did the worker hesitate? Where did they trust the output without checking? Where did they backtrack or get confused?

Afterward, discuss as a group: what one change to the prompt, spec, or validation step would have helped most? That is what rewrite time is really pointing at.

Working alone? Keep a two-column log instead: what you expected before each step, and what you actually had to change afterward. The gap between the two columns is what the observer would have noticed.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::

## The four-layer validation stack

To minimise rewrite time and ensure research rigor, use a structured validation stack.

### Layer 1: Immutable Requirements (No-Go Zones)
Before the AI writes code, define immutable requirements in your `CLAUDE.md`. These are rules the AI is not allowed to break.

*Example (from our project):* "Do not change the column names in `data/site_*.csv`" and "Do not drop any rows: the merge must have 60."

### Layer 2: Automated checks you can run
Validation should be executable, not just a feeling. Your project ships `validate_data.py` with two checks written and three left as TODO. Ask the agent to help you implement the rest, then read and run them, so that "valid" means "these checks passed," not "it looked fine."

### Layer 3: Metamorphic and invariant checks
Test the relationships in your data that should never change.
- **Invariants:** the merged file must have 60 rows (3 sites x 20 samples), and no `sample_id` should be lost.
- **Metamorphic checks:** if you shuffle the order of the input rows, the merged mean score should not change.

### Layer 4: Domain plausibility
This is where your research expertise is irreplaceable. A check can pass while the science is wrong. In our data, a water quality score above 100 is impossible, and site C's January samples must not appear in May. The clearest case: if the date-format trap goes uncaught, the cleaning runs, the row count is right, and the **trend you plot is still wrong**.

::::::::::::::::::::::::::::::::::::::::: callout

## Validation is yours to own

The stack only works if you stay in charge of it. Four things to keep in front of you:

- **You cannot validate what you cannot explain.** If you cannot say what the code does, you are not validating it, you are hoping.
- **Passing tests is not the same as being scientifically correct.** Tests check what you thought to check. They do not check the assumption you missed.
- **A second AI model is a reviewer, not an authority.** It has its own blind spots. Use it to widen your view, not to settle the question.
- **Domain plausibility is where your expertise matters most.** No model can replace knowing what a sensible result looks like in your field.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: build the validator

Open `validate_data.py`. Two checks are written for you; three are left as TODO (every sample's date matches the raw source, every `sample_id` is present exactly once, scores within 0-100).

1. Implement the three TODO checks. Write them yourself, or ask the agent and then read every line before you trust them. For the date check specifically: don't settle for "parses without error and falls in 2023" — a misparsed site C date can still produce a valid-looking 2023 date. Compare against the raw file instead (see the hint already in `validate_data.py`).
2. Run `python validate_data.py` against your `data/master_dataset.csv`. Make the checks pass by fixing the data or the cleaning script, never by editing a value to satisfy a check. A passing run looks like this (captured from the reference implementation, `instructors/files/backup_validate_data.py`):

   ```
   [PASS] row count is 60
   [PASS] all canonical columns present
   [PASS] every sample's date matches the raw source
   [PASS] every original sample_id is present exactly once
   [PASS] score values fall within 0-100

   All 5 checks passed.
   ```

3. Now break it on purpose: ask the agent to re-clean site C's dates using `pd.to_datetime(..., format="mixed")` instead of the explicit `%d-%m-%Y` format. Run the validator again. A good date check should now fail, for example:

   ```
   [FAIL] every sample's date matches the raw source - 8 mismatch(es), e.g. ['SC001', 'SC002', 'SC006']
   ```

   Notice this doesn't crash, and it doesn't obviously bunch the whole site C line at one edge of a plot either — only some rows are wrong, because `format="mixed"` guesses each date individually and gets some of them right by accident. If instead everything still passes, your date check is too weak (see the solution).

::::::::::::::::::::::::::::::::::::::::::::::::::: solution

If your validator still passes on the misparsed data, the date check is too weak. A good check reconstructs the expected date for each sample from the raw file (parsed with the explicit format) and compares it exactly — not merely that `pd.to_datetime` did not raise an error, or that the year is 2023. See `instructors/files/backup_validate_data.py` for a complete reference implementation. A validator that cannot fail on a known-bad input is not protecting you.

:::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: challenge

## Quick check: what does a passing validator actually tell you?

Your `validate_data.py` reports all five checks passed: row count, date accuracy, ID uniqueness, score range, and no lost rows. Which of the following can you now claim?

1. The data is correct, no further review is needed.
2. The five specific properties you wrote checks for hold on this run; anything you didn't write a check for is still unverified.
3. The AI's cleaning logic is correct in general, since it produced data that passes validation.
4. The result would validate the same way on a re-run with a different model.

:::::::::::::::::::::::::::::::::::::::: solution

**2.** A passing validator tells you exactly what it checked, nothing more. Option 1 overclaims: domain plausibility (Layer 4) and anything outside your five checks are still unverified. Option 3 mistakes passing output for correct logic, the same misparse bug could resurface on a different input the checks don't happen to cover. Option 4 assumes determinism the lesson has already ruled out, a different run or model could produce different intermediate code that still happens to pass, or fail differently. A validator earns trust by what it would catch, not by passing once.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

---

## Multi-model critique

A second model can widen your review, but switching models inside the same Claude Code session is not independent verification: it shares your conversation history, tools, and context with the first model. Treat what it returns as a hypothesis to check, not a second opinion from a clean slate.

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: get a multi-model critique

1. Use Model A (Claude Code) to generate a data cleaning script.
2. Provide the code to Model B, a *different* model, in a **fresh session** if you can (a new terminal, a different tool such as Codex CLI, or at minimum `/clear` first) — not just a `/model` switch inside the same conversation, which still carries the first model's framing. Give it the specification, the code, and any tests, not the first model's narrative about its own work. Then give it this prompt:

   "Read this script. Act as a skeptical senior data scientist. Identify three potential edge cases where this script will fail, such as empty strings, NaN values, or encoding issues. Suggest specific assert statements to catch these."

3. Reflect: Did the second model find something the first missed? Which of its findings still need a deterministic check or your own domain judgment before you'd act on them?

::::::::::::::::::::::::::::::::::::::::::::::::: solution

## Why this works, and its limit
Models have different blind spots, so a second read can surface edge cases and review questions the first one glossed over. But it is a hypothesis generator, not an authority: it shares training data and general tendencies with the first model, and a same-session `/model` switch shares even more (conversation history, tools, framing). Treat its findings as more questions to investigate with a deterministic check or your own expertise, not as proof.

:::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: instructor

## Teaching tip: approval fatigue
Warn learners about approval fatigue, the tendency to accept AI suggestions without reading them. The four-layer stack is designed to make the AI prove it is correct before you review the code.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: explain the approval gate

Take a script you (or a partner) generated earlier and walk through the approval gate out loud or in writing. Answer all five:

1. What did the AI produce?
2. What evidence do you have that it works?
3. What evidence is still missing?
4. What domain assumption could still be wrong?
5. Would you approve, revise, or reject this output, and why?

::::::::::::::::::::::::::::::::::::::::::::::::::: solution

## What a good answer looks like

A strong answer names the output precisely, points to *specific* checks as evidence (row counts, invariant checks, a test that passed), and is honest about gaps ("I have not checked the date parsing on the 2019 files"). The domain-assumption answer is the hardest and the most important: it is where you show you are judging the science, not only the code. "Approve" is only justified when the evidence covers the claim; otherwise the honest answer is "revise."

:::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: keypoints

- The approval gate separates experimental prototypes from validated research.
- Rewrite time is a local, formative signal about your workflow, not a productivity score.
- Immutable requirements prevent the AI from drifting away from research specs.
- A multi-model critique, run in a fresh session, is a reviewer, not an authority.
- You cannot validate what you cannot explain.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
