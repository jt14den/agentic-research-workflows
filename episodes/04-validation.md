---
title: "Validation Strategies: The Approval Gate"
teaching: 30
exercises: 20
---

:::::::::::::::::::::::::::::::::::::::::::::::::: objectives

## Objectives

- Use the approval gate to take responsibility for AI-generated code.
- Use rewrite time as a formative signal about your workflow, not a productivity score.
- Use a four-layer validation stack with explicit requirement constraints.
- Use multi-model verification to peer-review research code.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::: questions

- What evidence makes AI-generated code safe to approve?
- What can rewrite time tell me about my workflow, and what can it not?
- How can I use one AI to catch the errors of another without treating it as an authority?

::::::::::::::::::::::::::::::::::::::::::::::::::::

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

Rewrite time does **not** prove AI makes researchers faster in general. Measuring programmer productivity is genuinely hard, and a single timing on a single task tells you almost nothing about productivity overall. Treat rewrite time as a **formative signal** about *this* workflow, on *this* task:

- It is local and contextual.
- High rewrite time usually means the task was underspecified, the model overreached, or you did not yet have the mental model to evaluate the output.
- It helps you decide what to improve next: the prompt, the spec, or the validation step.

::::::::::::::::::::::::::::::::::::::::: caution

## Don't turn rewrite time into a productivity claim

A low rewrite time on one script is not evidence that AI saved you time overall. It does not count the time spent prompting, reviewing, debugging, or validating, and it says nothing about whether the result is scientifically correct. Use it to tune your workflow, not to justify it.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: think aloud while you work

Work in pairs. One person uses the AI for five minutes on a small, constrained task (for example, adding a single validation check to the cleaning script). Say out loud what you are doing as you do it: what you expect, what you trust, where you hesitate.

The observer takes notes: Where did the worker hesitate? Where did they trust the output without checking? Where did they backtrack or get confused?

Afterward, discuss as a group: what one change to the prompt, spec, or validation step would have helped most? That is what rewrite time is really pointing at.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::

## The four-layer validation stack

To minimise rewrite time and ensure research rigor, use a structured validation stack.

### Layer 1: Requirement constraints (No-Go Zones)
Before the AI writes code, define requirement constraints in your `CLAUDE.md`. These are rules the AI is not allowed to break.

*Example:* "Do not change the column names in `raw_data.csv`" or "Use only base R for this visualisation to ensure compatibility."

### Layer 2: Automated unit tests
Ask the agent to write tests before the implementation. Use a prompt pattern like: "First, write five Pytest cases that define the success of this data cleaning script. I will approve the tests before you write the logic."

### Layer 3: Metamorphic and invariant checks
Test the relationships in your data that should never change.
- **Invariants:** The total number of participants must remain 150 after merging.
- **Metamorphic checks:** If I change the order of the input rows, the final mean score should not change.

### Layer 4: Domain plausibility
This is where your research expertise is irreplaceable. AI does not know that a negative blood pressure reading is impossible.

::::::::::::::::::::::::::::::::::::::::: callout

## Validation is yours to own

The stack only works if you stay in charge of it. Four things to keep in front of you:

- **You cannot validate what you cannot explain.** If you cannot say what the code does, you are not validating it, you are hoping.
- **Passing tests is not the same as being scientifically correct.** Tests check what you thought to check. They do not check the assumption you missed.
- **A second AI model is a reviewer, not an authority.** It has its own blind spots. Use it to widen your view, not to settle the question.
- **Domain plausibility is where your expertise matters most.** No model can replace knowing what a sensible result looks like in your field.

::::::::::::::::::::::::::::::::::::::::::::::::::

---

## Multi-model verification

We use a challenger model to audit an implementation model rather than trusting a single AI.

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: orchestrate a peer review

1. Use Model A (Claude Code) to generate a data cleaning script.
2. Provide the code to Model B, a *different* model. The simplest way is to switch models inside your Claude Code session with `/model`; if you have Codex CLI or another agent installed, you can use that instead. Then give it this prompt:
   
   "Read this script. Act as a skeptical senior data scientist. Identify three potential edge cases where this script will fail, such as empty strings, NaN values, or encoding issues. Suggest specific assert statements to catch these."

3. Reflect: Did the challenger model find something the implementation model missed?

::::::::::::::::::::::::::::::::::::::::::::::::: solution

## Why this works
Models have different blind spots. Forcing a second AI to act as an auditor helps bypass the tendency of the primary assistant to be over-confident. This process reduces your manual rewrite time.

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
- Requirement constraints prevent the AI from drifting away from research specs.
- Multi-model verification uses a second AI as a reviewer, not an authority.
- You cannot validate what you cannot explain.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
